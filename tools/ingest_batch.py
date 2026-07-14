"""ingest_batch.py — harness-neutral driver for the mechanical half of an ingest batch.

WHY THIS EXISTS
    The ingest workflow (see AGENTS.md) has two halves:
      1. MECHANICAL  — pick the next open ledger rows, fetch captions, clean them to text,
                       classify failures, keep the ledger tidy. Identical every time, error-prone
                       to do by hand, and must work the same in ANY agent harness (Claude Code,
                       Codex, Pi, ...).
      2. JUDGEMENT   — read each transcript and write a faithful wiki/sources/ page under the
                       fidelity rules. This is the model's job and stays with the agent.

    This script owns half 1 so the agent only has to do half 2. It does NOT write source pages,
    touch persona/, or commit — those stay judgement calls. It just hands the agent a clean,
    self-contained "work order".

USAGE
    # See what's still open (no network, no changes):
    python tools/ingest_batch.py status

    # Prepare the next 10 open long-form rows of a channel (fetches captions, writes raw/*.txt,
    # auto-marks no-caption/removed videos, prints a work order):
    python tools/ingest_batch.py prepare --channel @ChannelHandle --n 10

    # Preview the selection only, no network / no changes:
    python tools/ingest_batch.py prepare --channel @ChannelHandle --n 10 --dry-run

    # Options:
    #   --priority N       restrict to priority N (1 landmark / 2 standard / 3 long-tail)
    #   --include-shorts   also consider `short` rows (default: long-form `video` only)
    #   --no-mark          do NOT auto-update the ledger (no-captions/unavailable/published)

WHAT `prepare` DOES, PER SELECTED VIDEO
    - Runs yt-dlp exactly like tools/fetch_captions.ps1 (manual subs preferred, auto fallback,
      en.*, vtt) into raw/youtube/<channel-slug>/<YYYY-MM-DD>-<id>.en.vtt
    - Converts the .vtt to clean .txt (via tools/vtt_to_text.py)
    - Classifies the outcome: ok | no-captions | rate-limited(429) | unavailable | error
    - Learns the true upload date from the produced filename (backfills `published` if it was NA)
    - Auto-marks the ledger (unless --no-mark):
        no-captions  -> status=L1, notes="no-captions (no subtitles available)"
        unavailable  -> status=L1, notes="video unavailable (removed)"
        429          -> LEFT OPEN (transient) and reported for a later retry
    - Emits a work order: for every OK video, the metadata + transcript path + the target
      source-page path (wiki/sources/<published>-yt-<id>.md) + a machine-readable JSON block.

AFTER THE AGENT WRITES THE PAGES (half 2), the usual bookkeeping is unchanged:
    python tools/ledger_set.py <id> status=L2 "domains=a;b" "notes=..."
    ...then insert rows into wiki/sources/youtube-index.md in date order, bump the footer count
    + index.md count, append ONE log.md entry, and commit + push.

NOTE: raw/ is gitignored (copyright). This script only reads/writes there and the ledger.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEDGER = REPO / "pipeline" / "ledger.csv"
INDEX = REPO / "wiki" / "sources" / "youtube-index.md"
LOG = REPO / "log.md"
SYNTH_CHECKPOINT = 10  # ingest batches since last synthesis -> a synthesis pass is due
FLAG_RE = re.compile(r"429|no-captions|unavailable|dup-of", re.IGNORECASE)
OPEN_STATUSES = {"L0-discovered", "L1"}

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vtt_to_text import vtt_to_text  # noqa: E402  (local helper, reused not duplicated)


# ----------------------------------------------------------------------------- ledger helpers
def read_ledger() -> list[dict]:
    with LEDGER.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def channel_slug(handle: str) -> str:
    """@ChannelHandle -> channelhandle ; matches the raw/youtube/<slug>/ dirs and fetch_captions.ps1."""
    return handle.lstrip("@").lower()


def normalize_channel(arg: str) -> str:
    """Accept '@ChannelHandle', 'channelhandle', 'ChannelHandle' -> canonical '@ChannelHandle' from the ledger."""
    want = arg.lstrip("@").lower()
    for h in sorted({r["channel_or_publisher"] for r in read_ledger() if r["channel_or_publisher"].startswith("@")}):
        if h.lstrip("@").lower() == want:
            return h
    sys.exit(f"unknown channel '{arg}'. Known: " + ", ".join(
        sorted({r['channel_or_publisher'] for r in read_ledger() if r['channel_or_publisher'].startswith('@')})))


def batches_since_synthesis() -> int:
    """Count ingest-batch log entries since the last synthesis pass (the synthesis debt, in batches)."""
    count = 0
    for line in (LOG.read_text(encoding="utf-8", errors="replace") if LOG.exists() else "").splitlines():
        if line.startswith("## ["):
            low = line.lower()
            if "synthesis" in low:      # a synthesis/lint pass resets the counter
                count = 0
            elif "ingest |" in low or "| ingest" in low or "ingest |" in low:
                count += 1
    return count


def channel_open_count(rows: list[dict], channel: str) -> int:
    return sum(1 for r in rows if r["channel_or_publisher"] == channel and r["type"] == "video"
               and r["status"] in OPEN_STATUSES and not FLAG_RE.search(r.get("notes", "")))


def print_checkpoint(rows: list[dict], channel: str, batch_size: int) -> None:
    """Nudge the agent to switch to the synthesis loop at a checkpoint (channel done / ~10 batches)."""
    debt = batches_since_synthesis()
    remaining_after = channel_open_count(rows, channel) - batch_size
    if remaining_after <= 0:
        print("\n" + "!" * 78)
        print(f">>> CHECKPOINT: {channel} long-form will be COMPLETE after this batch.")
        print(">>> Run the SYNTHESIS loop before the next channel:  python tools/synthesis_batch.py prepare")
        print("!" * 78)
    elif debt >= SYNTH_CHECKPOINT:
        print("\n" + "!" * 78)
        print(f">>> CHECKPOINT: {debt} ingest batches since the last synthesis pass (>= {SYNTH_CHECKPOINT}).")
        print(">>> Run the SYNTHESIS loop now, then resume ingest:  python tools/synthesis_batch.py prepare")
        print("!" * 78)


def ledger_set(row_id: str, **fields: str) -> None:
    args = [sys.executable, str(REPO / "tools" / "ledger_set.py"), row_id]
    args += [f"{k}={v}" for k, v in fields.items()]
    subprocess.run(args, check=True)


# ----------------------------------------------------------------------------- selection
def select_rows(rows: list[dict], channel: str, n: int,
                priority: str | None, include_shorts: bool) -> list[dict]:
    types = {"video", "short"} if include_shorts else {"video"}
    pool = [
        r for r in rows
        if r["channel_or_publisher"] == channel
        and r["type"] in types
        and r["status"] in OPEN_STATUSES
        and not FLAG_RE.search(r.get("notes", ""))
        and (priority is None or r["priority"] == priority)
    ]

    def sort_key(r: dict):
        pub = r.get("published", "") or ""
        # oldest published first; NA/empty last
        pub_key = pub if re.fullmatch(r"\d{4}-\d{2}-\d{2}", pub) else "9999-99-99"
        prio = r["priority"] if r["priority"].isdigit() else "9"
        return (prio, pub_key)

    pool.sort(key=sort_key)
    return pool[:n]


# ----------------------------------------------------------------------------- caption fetch
def fetch_captions(url: str, slug: str, video_id: str) -> tuple[str, Path | None, str | None]:
    """Return (outcome, txt_path, learned_date). outcome in {ok,no-captions,429,unavailable,error}."""
    out_tmpl = f"raw/youtube/{slug}/%(upload_date>%Y-%m-%d)s-%(id)s.%(ext)s"
    cmd = [
        "yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs",
        "--sub-langs", "en.*", "--sub-format", "vtt", "-o", out_tmpl, url,
    ]
    proc = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, errors="replace")
    blob = (proc.stdout or "") + (proc.stderr or "")

    chan_dir = REPO / "raw" / "youtube" / slug
    vtts = sorted(chan_dir.glob(f"*-{video_id}.*.vtt")) if chan_dir.exists() else []
    if vtts:
        vtt = next((v for v in vtts if v.name.endswith(".en.vtt")), vtts[0])
        txt = vtt_to_text(vtt)
        m = re.search(r"(\d{4}-\d{2}-\d{2})-" + re.escape(video_id), vtt.name)
        return "ok", txt, (m.group(1) if m else None)

    low = blob.lower()
    if "http error 429" in low or "too many requests" in low:
        return "429", None, None
    if "video unavailable" in low or "not available" in low or "no longer available" in low:
        return "unavailable", None, None
    if "no subtitles" in low or "there are no subtitles" in low:
        return "no-captions", None, None
    return "error", None, None


# ----------------------------------------------------------------------------- commands
def cmd_status(_: argparse.Namespace) -> None:
    rows = read_ledger()
    channels = sorted({r["channel_or_publisher"] for r in rows if r["channel_or_publisher"].startswith("@")})
    print("OPEN long-form rows (L0/L1, excl. 429/no-captions/unavailable/dup):")
    for ch in channels:
        openv = [r for r in rows if r["channel_or_publisher"] == ch and r["type"] == "video"
                 and r["status"] in OPEN_STATUSES and not FLAG_RE.search(r.get("notes", ""))]
        if openv:
            by_p = {}
            for r in openv:
                by_p[r["priority"]] = by_p.get(r["priority"], 0) + 1
            pr = " ".join(f"P{k}:{v}" for k, v in sorted(by_p.items()))
            print(f"  {ch:<16} {len(openv):>5}   ({pr})")
    shorts = sum(1 for r in rows if r["type"] == "short" and r["status"] in OPEN_STATUSES)
    l2 = sum(1 for r in rows if r["status"] == "L2")
    l3 = sum(1 for r in rows if r["status"] == "L3")
    print(f"\n  open shorts (all channels): {shorts}")
    print(f"  ingested: L2={l2}  L3={l3}")
    debt = batches_since_synthesis()
    flag = "  <-- SYNTHESIS DUE (run tools/synthesis_batch.py)" if debt >= SYNTH_CHECKPOINT else ""
    print(f"  ingest batches since last synthesis: {debt} (checkpoint at {SYNTH_CHECKPOINT}){flag}")
    if INDEX.exists():
        m = re.search(r"_(\d+) videos ingested", INDEX.read_text(encoding="utf-8", errors="replace"))
        if m:
            print(f"  youtube-index.md footer count: {m.group(1)}")


def cmd_prepare(a: argparse.Namespace) -> None:
    channel = normalize_channel(a.channel)
    slug = channel_slug(channel)
    rows = read_ledger()
    batch = select_rows(rows, channel, a.n, a.priority, a.include_shorts)
    if not batch:
        print(f"Nothing open to prepare for {channel} (priority={a.priority}, "
              f"shorts={a.include_shorts}).")
        return

    print(f"# Batch preparation - {channel}  (slug: {slug})")
    print(f"# selected {len(batch)} open row(s), oldest-first\n")
    for r in batch:
        print(f"  {r.get('published','NA'):<10} {r['id']:<16} P{r['priority']}  {r['title'][:60]}")

    if a.dry_run:
        print("\n[--dry-run] no captions fetched, no ledger changes.")
        return

    ok, marked, retry = [], [], []
    print("\n# Fetching captions ...")
    for r in batch:
        vid = r["id"][3:] if r["id"].startswith("yt-") else r["id"]
        outcome, txt, learned = fetch_captions(r["url"], slug, vid)
        pub = learned or (r.get("published") if re.fullmatch(r"\d{4}-\d{2}-\d{2}", r.get("published", "") or "") else None)
        if outcome == "ok":
            # backfill a missing publish date from the real upload_date
            if learned and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r.get("published", "") or ""):
                if not a.no_mark:
                    ledger_set(r["id"], published=learned)
            target = f"wiki/sources/{pub or 'NA'}-yt-{vid}.md"
            ok.append({"id": r["id"], "vid": vid, "url": r["url"], "title": r["title"],
                       "published": pub or "NA", "channel": channel,
                       "transcript": str(txt.relative_to(REPO)).replace("\\", "/"),
                       "target": target})
            print(f"  ok           {r['id']}  -> {ok[-1]['transcript']}")
        elif outcome == "no-captions":
            if not a.no_mark:
                ledger_set(r["id"], status="L1", notes="no-captions (no subtitles available)")
            marked.append((r["id"], "no-captions"))
            print(f"  no-captions  {r['id']}  (marked L1)" if not a.no_mark else f"  no-captions  {r['id']}")
        elif outcome == "unavailable":
            if not a.no_mark:
                ledger_set(r["id"], status="L1", notes="video unavailable (removed)")
            marked.append((r["id"], "unavailable"))
            print(f"  unavailable  {r['id']}  (marked L1)" if not a.no_mark else f"  unavailable  {r['id']}")
        elif outcome == "429":
            retry.append(r["id"])
            print(f"  429          {r['id']}  (left open — retry later)")
        else:
            retry.append(r["id"])
            print(f"  error        {r['id']}  (left open — inspect manually)")

    # ------------------------------------------------ work order
    print("\n" + "=" * 78)
    print("WORK ORDER - write one wiki/sources/ page per video below, per AGENTS.md fidelity rules")
    print("=" * 78)
    print("""
For EACH video: read its transcript, then write the target page with YAML frontmatter
(type: youtube-video, source_date, url, channel, ingested, tier: L2, domains) + ## Summary
+ ## Key claims (paraphrase, DATED) + ## Notable verbatim quotes (>blockquotes = voice data).
Fidelity: cite; verbatim vs paraphrase; DATE opinions; attribute per speaker (only the SUBJECT trains
the persona); flag contradictions with a callout; watch caption garbles (names/numbers);
English only.
""")
    for v in ok:
        print(f"- {v['id']}  [{v['published']}]  {v['title']}")
        print(f"    transcript: {v['transcript']}")
        print(f"    write page: {v['target']}\n")

    # machine-readable block for harnesses that prefer to parse
    import json
    print("```json")
    print(json.dumps({"channel": channel, "ok": ok,
                      "marked": marked, "retry": retry}, indent=2))
    print("```")

    print("\nNEXT (bookkeeping - unchanged workflow):")
    print("  1. write the pages above")
    print("  2. python tools/ledger_set.py <id> status=L2 \"domains=...\" \"notes=...\"   (per video)")
    print("  3. insert rows into wiki/sources/youtube-index.md in DATE order")
    print(f"  4. bump the youtube-index footer count (+{len(ok)}) and the index.md count")
    print("  5. append ONE log.md entry, then commit + push")
    print(f"\nSummary: {len(ok)} ok, {len(marked)} marked, {len(retry)} retry/error.")
    print_checkpoint(rows, channel, len(batch))


def main() -> None:
    p = argparse.ArgumentParser(
        prog="ingest_batch.py",
        description="Harness-neutral driver for the mechanical half of an ingest batch "
                    "(select -> fetch captions -> clean -> work order). See the module "
                    "docstring for the full workflow.")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="show open counts per channel (no network, no changes)")

    pp = sub.add_parser("prepare", help="prepare the next N open rows of a channel")
    pp.add_argument("--channel", required=True, help="e.g. @ChannelHandle (or channelhandle)")
    pp.add_argument("--n", type=int, default=10, help="how many rows (default 10)")
    pp.add_argument("--priority", choices=["1", "2", "3"], help="restrict to a priority tier")
    pp.add_argument("--include-shorts", action="store_true", help="also consider `short` rows")
    pp.add_argument("--dry-run", action="store_true", help="selection only; no fetch, no changes")
    pp.add_argument("--no-mark", action="store_true", help="do not auto-update the ledger")

    args = p.parse_args()
    {"status": cmd_status, "prepare": cmd_prepare}[args.cmd](args)


if __name__ == "__main__":
    main()
