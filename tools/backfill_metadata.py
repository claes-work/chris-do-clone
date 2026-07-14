"""Backfill upload_date + view_count for a channel's long-form ledger rows, then
re-prioritize by views (ROADMAP: channel top-N by views -> P1).

flat enumeration (fetch_channel.ps1) is fast but returns no date/views. This second
pass fills them via yt-dlp per-video extraction, then promotes the most-viewed solo
videos to P1. Guest content (already P3) is NOT promoted — attribution matters more
than views there.

Requires network (yt-dlp). Run on a machine that can reach youtube.com.

Usage:
  python tools/backfill_metadata.py --channel @ChannelHandle          # backfill + rerank
  python tools/backfill_metadata.py --channel @ChannelHandle --top 50 # P1 = top 50 by views
  python tools/backfill_metadata.py --channel @ChannelHandle --batch 40
"""
import argparse
import csv
import subprocess
import sys
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "pipeline" / "ledger.csv"
COLS = [
    "id", "type", "title", "channel_or_publisher", "url", "published",
    "discovered", "status", "priority", "domains", "notes",
]
MISSING = {"", "NA", None}


def read_ledger() -> list[dict]:
    with LEDGER.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_ledger(rows: list[dict]) -> None:
    with LEDGER.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLS})


def fetch_meta(urls: list[str]) -> dict[str, tuple[str, str]]:
    """id -> (upload_date YYYYMMDD|'', view_count digits|'')."""
    cmd = [
        "yt-dlp", "--skip-download", "--no-warnings", "--ignore-errors",
        "--no-update", "--print", "%(id)s\t%(upload_date)s\t%(view_count)s",
        *urls,
    ]
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    meta: dict[str, tuple[str, str]] = {}
    for line in (out.stdout or "").splitlines():
        parts = line.split("\t")
        if len(parts) == 3:
            vid, date, views = parts
            meta[vid] = (date if date != "NA" else "", views if views.isdigit() else "")
    return meta


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", required=True)
    ap.add_argument("--top", type=int, default=50, help="Top-N by views promoted to P1")
    ap.add_argument("--batch", type=int, default=40)
    args = ap.parse_args()

    rows = read_ledger()
    targets = [
        r for r in rows
        if r["type"] == "video" and r["channel_or_publisher"] == args.channel
        and r["published"] in MISSING
    ]
    print(f"{len(targets)} long-form rows to backfill for {args.channel}")

    filled = 0
    for i in range(0, len(targets), args.batch):
        chunk = targets[i:i + args.batch]
        meta = fetch_meta([r["url"] for r in chunk])
        for r in chunk:
            vid = r["id"].removeprefix("yt-")
            if vid in meta:
                date, views = meta[vid]
                if date:
                    r["published"] = f"{date[0:4]}-{date[4:6]}-{date[6:8]}"
                if views:
                    r["notes"] = f"views={views}"
                    filled += 1
        print(f"  batch {i // args.batch + 1}: {min(i + args.batch, len(targets))}/{len(targets)}")

    # Re-rank: top-N by views among this channel's long-form -> P1, but never override
    # guest content (P3 — attribution matters more than view count there).
    def views_of(r: dict) -> int:
        n = r["notes"]
        return int(n[6:]) if n.startswith("views=") and n[6:].isdigit() else -1

    longform = [r for r in rows
                if r["type"] == "video" and r["channel_or_publisher"] == args.channel]
    ranked = sorted(longform, key=views_of, reverse=True)
    promoted = 0
    for r in ranked[:args.top]:
        if views_of(r) >= 0 and r["priority"] != "3":
            if r["priority"] != "1":
                promoted += 1
            r["priority"] = "1"

    write_ledger(rows)
    print(f"filled views for {filled} videos; promoted {promoted} new videos to P1 "
          f"(top {args.top} by views, guests excluded)")


if __name__ == "__main__":
    main()
