"""Set fields on one ledger row by id, preserving the ledger's minimal-quoting style.

Usage:
  python tools/ledger_set.py <id> status=L2 published=2025-03-17 domains="a;b" notes="..."
"""
import csv
import sys
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "pipeline" / "ledger.csv"
COLS = [
    "id", "type", "title", "channel_or_publisher", "url", "published",
    "discovered", "status", "priority", "domains", "notes",
]


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit("usage: ledger_set.py <id> field=value [field=value ...]")
    row_id = sys.argv[1]
    updates = dict(kv.split("=", 1) for kv in sys.argv[2:])
    bad = set(updates) - set(COLS)
    if bad:
        sys.exit(f"unknown field(s): {bad}")

    with LEDGER.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    hit = False
    for r in rows:
        if r["id"] == row_id:
            r.update(updates)
            hit = True
            break
    if not hit:
        sys.exit(f"id not found: {row_id}")

    with LEDGER.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLS})
    print(f"updated {row_id}: {updates}")


if __name__ == "__main__":
    main()
