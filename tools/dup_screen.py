#!/usr/bin/env python3
"""Detect re-uploads/clips of already-held material — across transcription systems.

WHY THIS EXISTS
---------------
On 2026-07-31 a whisper transcript (`yt-CbQNwT7FsVg`) was PROVEN to be a re-upload of an
already-ingested video (`yt-7snev8P4ENU`) by phrase spot-checks and 72% vocabulary overlap
— and then passed TWO exact-match screens as "unique":

    1. grep -F of a 7-gram        -> missed it (source .vtt has line breaks mid-phrase)
    2. whitespace-normalised      -> still missed it

The reason is structural, not a bug to tune away: **whisper and YouTube's caption engine
word the same audio differently.** Any exact n-gram method is blind across that boundary,
which is exactly the boundary that matters when back-filling no-caption rows.

THE METRIC THAT WORKS
    rare-word containment — restrict both documents to tokens whose corpus
    document-frequency is <= 2% (i.e. the distinctive vocabulary of a video: names, figures,
    idiosyncratic phrasing), then measure what fraction of the candidate's rare vocabulary
    appears in the other document. Word choice differs between transcribers; WHICH RARE
    THINGS GET TALKED ABOUT does not.

    Scored on the known case: 89%. Threshold 0.55 flags, 0.40 asks for a look.

⚠️ Run the exact-match screen as a COMPLEMENT, not a replacement (--exact). Containment can
miss short whisper-vs-whisper dups inside one batch, where exact matching is reliable.

⚠️⚠️ A HIT IS NOT A SKIP. See the CLIP RULE in SUBJECT.md: a clip is only a discardable
duplicate if its parent is L2/L3. If the parent is `skipped`, the content was never ingested
and the clip must be triaged on its own merits — 4 of 6 hits in the first run were exactly
that case, and one of them yielded a named concept at 0 corpus-wide.

USAGE
    python3 tools/dup_screen.py --channel @thefutur --since "2026-07-31 12:50"
    python3 tools/dup_screen.py --channel @thefutur --ids yt-abc123,yt-def456 [--exact]
"""
from __future__ import annotations

import argparse
import collections
import csv
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEDGER = REPO / "pipeline" / "ledger.csv"
CHANNEL_DIRS = {"@thefutur": "thefutur", "@TheFuturAcademy": "thefuturacademy", "@ChrisDo": "chrisdo"}

DF_CEILING = 0.02   # a token counts as "rare" if it appears in <=2% of corpus documents
FLAG = 0.55
LOOK = 0.40
MIN_RARE = 15       # below this the signal is too thin to judge; reported, never silently passed

TOKEN = re.compile(r"[a-z']{5,}")


def tokens(text: str) -> set[str]:
    return set(TOKEN.findall(text.lower()))


def vid_of(path: Path) -> str:
    """Filenames are YYYY-MM-DD-<videoid>.<ext...>; the id starts at offset 11."""
    return path.name[11:].split(".")[0]


def ledger() -> dict[str, dict]:
    return {r["id"].replace("yt-", ""): r for r in csv.DictReader(LEDGER.open(encoding="utf-8"))}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", required=True)
    ap.add_argument("--since", help='mtime cutoff, e.g. "2026-07-31 12:50"')
    ap.add_argument("--ids", help="comma-separated ledger ids instead of --since")
    ap.add_argument("--exact", action="store_true", help="also run the complementary exact-match screen")
    a = ap.parse_args()

    cdir = REPO / "raw" / "youtube" / CHANNEL_DIRS.get(a.channel, a.channel.lstrip("@").lower())
    if not cdir.is_dir():
        print(f"no such channel dir: {cdir}", file=sys.stderr)
        return 1

    if a.ids:
        want = {i.replace("yt-", "").strip() for i in a.ids.split(",")}
        cands = [p for p in cdir.iterdir() if p.is_file() and vid_of(p) in want]
    elif a.since:
        out = subprocess.run(["find", str(cdir), "-name", "*.en.txt", "-newermt", a.since],
                             capture_output=True, text=True).stdout.split()
        cands = [Path(p) for p in out]
    else:
        print("need --since or --ids", file=sys.stderr)
        return 1
    if not cands:
        print("no candidate files matched")
        return 0

    cand_ids = {vid_of(p) for p in cands}
    corpus: dict[str, set[str]] = {}
    for p in cdir.iterdir():
        if not p.is_file() or vid_of(p) in cand_ids:
            continue
        try:
            corpus[p.name] = tokens(p.read_text(errors="replace"))
        except OSError:
            continue

    df = collections.Counter()
    for s in corpus.values():
        df.update(s)
    ceiling = len(corpus) * DF_CEILING
    rare = lambda s: {w for w in s if df[w] <= ceiling}
    corpus_rare = {n: rare(s) for n, s in corpus.items()}

    led = ledger()
    print(f"{len(cands)} candidates vs {len(corpus)} corpus docs "
          f"(rare-word containment, df<={DF_CEILING:.0%}, flag>={FLAG:.0%})\n")

    hits = 0
    for p in sorted(cands):
        vid = vid_of(p)
        R = rare(tokens(p.read_text(errors="replace")))
        if len(R) < MIN_RARE:
            print(f"  {vid:14} UNSCREENED — only {len(R)} rare tokens (too short to judge)")
            continue
        score, best = max(((len(R & s) / len(R), n) for n, s in corpus_rare.items()), default=(0.0, "-"))
        if score < LOOK:
            continue
        hits += 1
        parent = led.get(vid_of(Path(best)), {})
        pstat = parent.get("status", "?")
        # The whole point of the clip rule: the parent's status decides what the hit MEANS.
        verdict = ("DISCARDABLE dup — parent already ingested" if pstat in {"L2", "L3"}
                   else f"TRIAGE INDIVIDUALLY — parent is '{pstat}', content never ingested")
        print(f"  {vid:14} {score:5.0%} vs {best}\n"
              f"  {'':14} -> {verdict}")

    print(f"\n{hits} candidate(s) at or above {LOOK:.0%}. "
          f"⚠️ A hit is not a skip — check the parent's status (see SUBJECT.md clip rule).")

    if a.exact:
        print("\n-- complementary exact-match screen (catches within-batch dups) --")
        for p in sorted(cands):
            w = p.read_text(errors="replace").split()
            if len(w) < 60:
                continue
            probe = " ".join(w[len(w) // 2: len(w) // 2 + 7])
            found = subprocess.run(["grep", "-rlF", probe, str(cdir)],
                                   capture_output=True, text=True).stdout.split()
            found = [f for f in found if vid_of(p) not in f]
            if found:
                print(f"  {vid_of(p):14} exact-match in {Path(found[0]).name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
