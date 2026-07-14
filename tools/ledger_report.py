"""Ledger status report: counts per status/priority and the next open batch.

Usage: python tools/ledger_report.py [N]   (N = batch size, default 20)
"""
import csv
import sys
from collections import Counter
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "pipeline" / "ledger.csv"
OPEN_STATUSES = {"L0-discovered", "L1"}


def main() -> None:
    batch_size = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    with LEDGER.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"total: {len(rows)}")
    for key in ("status", "priority", "type"):
        print(f"by {key}: {dict(Counter(r[key] for r in rows))}")

    open_rows = sorted(
        (r for r in rows if r["status"] in OPEN_STATUSES),
        key=lambda r: (r["priority"], r["published"] or "9999"),
    )
    print(f"\nnext batch ({min(batch_size, len(open_rows))} of {len(open_rows)} open):")
    for r in open_rows[:batch_size]:
        print(f"  [{r['priority']}] {r['id']} | {r['title'][:70]} | {r['status']}")


if __name__ == "__main__":
    main()
