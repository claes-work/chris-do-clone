"""Merge staging CSV(s) from fetch_channel.ps1 into pipeline/ledger.csv.

Dedupes by id (existing ledger rows always win and are preserved verbatim), fills
the channel handle, forces `type=short` on rows from a channel's /shorts tab, and
assigns a priority to each NEW long-form row from a title heuristic:

  P1 (landmark solo): book launches, origin/"how I built" narratives, keynotes.
  P3 (guests present): interviews, podcast episodes, competition/reaction formats.
  P2: everything else long-form.
  Shorts: always P3 (deduped against long-form later, Stage C).

Title-based P1 is a FLOOR, not the whole story: the roadmap also wants the channel's
~top-50 by views at P1, but flat enumeration returns no view_count for the /videos
tab, so a later view-based refinement pass is expected (logged, not silent).

Usage:
  python tools/merge_staging.py --channel @ChannelHandle \
      --videos pipeline/staging-channelhandle-videos.csv \
      --shorts pipeline/staging-channelhandle-shorts.csv
"""
import argparse
import csv
import re
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "pipeline" / "ledger.csv"
COLS = [
    "id", "type", "title", "channel_or_publisher", "url", "published",
    "discovered", "status", "priority", "domains", "notes",
]

# Guest/interview/podcast markers -> P3 (other speakers present). High-precision only:
# generic "competition"/"vs"/"[Ep NN]" are deliberately excluded because many subjects'
# SOLO videos use them.
# BOOTSTRAP HOOK: /clone-setup appends subject-specific markers here —
#   P3_EXTRA: guest/Q&A formats named after the subject (e.g. "ask alex|asks alex")
#   P1_EXTRA: landmark markers — book titles, signature courses, company origin stories
P3_EXTRA: list[str] = []
P1_EXTRA: list[str] = []

P3_RE = re.compile(
    "|".join([
        r"\bw/\b", r"\bft\.?\b", r"\bfeat\b", r"interview", r"podcast", r"\breacts?\b",
        r"q&a", r"q & a", r"answering your", r"\bama\b", r"sits? down", r"\bguest\b",
    ] + P3_EXTRA),
    re.IGNORECASE,
)
# Landmark solo markers -> P1 (book launch / origin / keynote).
P1_RE = re.compile(
    "|".join([
        r"how i (built|made|went|scaled|started|lost)", r"my story", r"origin story",
        r"keynote", r"how i got", r"how i turned", r"net worth", r"billion dollar",
        r"from \$?\d+.*to \$?\d+", r"broke to", r"zero to",
    ] + P1_EXTRA),
    re.IGNORECASE,
)


def priority_for(title: str) -> str:
    # Guest signal wins: interview content is P3 even if the title name-drops a book.
    if P3_RE.search(title):
        return "3"
    if P1_RE.search(title):
        return "1"
    return "2"


def read_rows(path: Path) -> list[dict]:
    if not path or not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", required=True, help="Handle to stamp, e.g. @ChannelHandle")
    ap.add_argument("--videos", type=Path, help="Staging CSV from the /videos tab")
    ap.add_argument("--shorts", type=Path, help="Staging CSV from the /shorts tab")
    args = ap.parse_args()

    existing = read_rows(LEDGER)
    seen = {r["id"] for r in existing}
    added, counts = [], {"1": 0, "2": 0, "3": 0}

    def stage(rows: list[dict], is_short: bool) -> None:
        for r in rows:
            rid = r["id"]
            if rid in seen:
                continue  # existing ledger row wins; also dedupes within staging
            seen.add(rid)
            r["channel_or_publisher"] = args.channel
            if is_short:
                r["type"] = "short"
                r["priority"] = "3"
            else:
                r["priority"] = priority_for(r["title"])
            counts[r["priority"]] += 1
            added.append({c: r.get(c, "") for c in COLS})

    stage(read_rows(args.videos), is_short=False)
    stage(read_rows(args.shorts), is_short=True)

    with LEDGER.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in existing:
            w.writerow({c: r.get(c, "") for c in COLS})
        for r in added:
            w.writerow(r)

    print(f"merged {len(added)} new rows for {args.channel} "
          f"(P1={counts['1']} P2={counts['2']} P3={counts['3']}); "
          f"ledger now {len(existing) + len(added)} rows")


if __name__ == "__main__":
    main()
