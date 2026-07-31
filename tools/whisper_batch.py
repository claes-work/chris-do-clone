#!/usr/bin/env python3
"""Transcribe no-caption ledger rows with local whisper.cpp.

WHY THIS EXISTS
---------------
`tools/fetch_captions.ps1` only retrieves YouTube's own subtitle tracks. Rows whose
notes say `no-captions` have none, and were therefore permanently unreachable — 102 of
them as of 2026-07-30, including 41 @thefutur long-form videos and 10 livestreams.

⚠️ AI transcription is NEVER run without explicit user approval (AGENTS.md / ROADMAP
principle 4: "Captions first, AI transcription only as fallback — and only with user
approval, it costs money"). This script does not bypass that; it is the tool the approval
enables. Approval for the 41+10 long-form set was given 2026-07-31.

REQUIREMENTS (all already present on this machine, verified 2026-07-31)
    whisper-cli            brew install whisper-cpp   -> /opt/homebrew/bin/whisper-cli
    a ggml model           ~/.cache/whisper/ggml-medium.bin
    yt-dlp, ffmpeg

OUTPUT
    raw/youtube/<channel-dir>/<YYYY-MM-DD>-<videoid>.en.txt

    ⚠️ Written with the SAME naming convention as caption-derived transcripts so the rest
    of the pipeline cannot tell them apart mechanically — which is exactly why every page
    built from one MUST be marked `transcript: whisper` in its frontmatter. A machine
    transcript is not a caption track: it has no speaker turns, invents punctuation, and
    mis-hears proper nouns. Treat names in it as UNVERIFIED.

USAGE
    python3 tools/whisper_batch.py --channel @thefutur --n 5 [--dry-run]
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEDGER = REPO / "pipeline" / "ledger.csv"
MODEL = Path.home() / ".cache" / "whisper" / "ggml-medium.bin"
WHISPER = "/opt/homebrew/bin/whisper-cli"

CHANNEL_DIRS = {
    "@thefutur": "thefutur",
    "@TheFuturAcademy": "thefuturacademy",
    "@ChrisDo": "chrisdo",
}

# Only these types. Shorts are excluded by default: of ~800 already triaged, the hit rate
# was 1 in 80, so transcription budget spent on them is the worst available use of it.
LONGFORM = {"video", "stream"}


def targets(channel: str, limit: int, include_shorts: bool) -> list[dict]:
    rows = list(csv.DictReader(LEDGER.open(encoding="utf-8")))
    types = LONGFORM | {"short"} if include_shorts else LONGFORM
    out = [
        r for r in rows
        if r["channel_or_publisher"] == channel
        and r["type"] in types
        and r["status"] in {"L0-discovered", "L1"}
        and "no-captions" in (r.get("notes") or "")
    ]
    return out[:limit]


def already_done(vid: str, cdir: Path) -> bool:
    return any(cdir.glob(f"*{vid}.en.txt"))


def transcribe(row: dict, cdir: Path, tmp: Path) -> tuple[bool, str]:
    vid = row["id"].replace("yt-", "")
    wav = tmp / f"{vid}.wav"
    # 16 kHz mono is what whisper.cpp wants; anything else is resampled internally at a cost.
    dl = subprocess.run(
        ["yt-dlp", "-q", "--no-warnings", "--extract-audio", "--audio-format", "wav",
         "--postprocessor-args", "ffmpeg:-ar 16000 -ac 1",
         "--print-to-file", "%(upload_date)s", str(tmp / f"{vid}.date"),
         "-o", str(tmp / f"{vid}.%(ext)s"), row["url"]],
        capture_output=True, text=True, timeout=1800,
    )
    if not wav.exists():
        return False, (dl.stderr or "audio download failed").strip().splitlines()[-1][:120]

    datef = tmp / f"{vid}.date"
    upload = datef.read_text().strip()[:8] if datef.exists() else ""
    date = f"{upload[:4]}-{upload[4:6]}-{upload[6:8]}" if len(upload) == 8 else (row.get("published") or "NA")
    if not re.match(r"\d{4}-\d{2}-\d{2}", date):
        return False, f"no usable date (ledger said {row.get('published')!r})"

    stem = tmp / vid
    r = subprocess.run(
        [WHISPER, "-m", str(MODEL), "-f", str(wav), "-l", "en",
         "-np", "-nt", "-otxt", "-of", str(stem)],
        capture_output=True, text=True, timeout=7200,
    )
    txt = stem.with_suffix(".txt")
    if not txt.exists():
        return False, (r.stderr or "whisper produced no output").strip().splitlines()[-1][:120]

    body = txt.read_text(encoding="utf-8").strip()
    if len(body.split()) < 50:
        return False, f"transcript too short ({len(body.split())} words) — likely music/silence"

    dest = cdir / f"{date}-{vid}.en.txt"
    dest.write_text(body + "\n", encoding="utf-8")
    wav.unlink(missing_ok=True)
    return True, f"{dest.name} ({len(body.split()):,} words)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", required=True)
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--include-shorts", action="store_true",
                    help="NOT recommended: 1-in-80 hit rate across ~800 already triaged")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if not MODEL.exists():
        print(f"model missing: {MODEL}", file=sys.stderr)
        return 1
    cdir = REPO / "raw" / "youtube" / CHANNEL_DIRS.get(a.channel, a.channel.lstrip("@").lower())
    cdir.mkdir(parents=True, exist_ok=True)
    tmp = Path("/tmp/whisper_batch")
    tmp.mkdir(exist_ok=True)

    rows = targets(a.channel, a.n, a.include_shorts)
    print(f"{len(rows)} no-caption rows selected for {a.channel}")
    if a.dry_run:
        for r in rows:
            print(f"  {r['id']}  {r['type']:<7} {r['title'][:60]}")
        return 0

    ok = fail = 0
    for i, r in enumerate(rows, 1):
        vid = r["id"].replace("yt-", "")
        if already_done(vid, cdir):
            print(f"  [{i}/{len(rows)}] {r['id']}  SKIP (transcript exists)")
            continue
        good, msg = transcribe(r, cdir, tmp)
        print(f"  [{i}/{len(rows)}] {r['id']}  {'ok  ' if good else 'FAIL'}  {msg}")
        ok, fail = (ok + 1, fail) if good else (ok, fail + 1)

    print(f"\n{ok} transcribed, {fail} failed.")
    print("⚠️ Mark every page built from these with `transcript: whisper` and treat")
    print("   proper nouns as UNVERIFIED — machine transcripts mis-hear names.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
