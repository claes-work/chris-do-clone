"""synthesis_batch.py — harness-neutral driver for the SYNTHESIS loop.

WHY THIS EXISTS
    Ingesting (see tools/ingest_batch.py) grows the wiki OUTWARD: one `wiki/sources/` page per
    source (L2). Synthesizing grows it INWARD: it promotes the genuinely-new material from many
    L2 source pages into the `wiki/topics/` frameworks and the `persona/` files (biography, voice,
    beliefs, appearance), reconciles contradictions, dates positions, then recompiles
    `persona/system-prompt.md` (the clone). That promotion is what turns a big linked library into
    a smarter clone — and it must not be forgotten, so it runs as its own autonomous loop.

    This driver owns the MECHANICAL + STATEFUL half of a synthesis pass:
      - track the high-water mark (what has already been synthesized) in pipeline/synthesis-state.md
      - surface the accumulated debt (the `Synthesis notes:` lines every ingest batch logs)
      - list the promotion targets (topic + persona files)
      - emit a work order
    The JUDGEMENT half (deciding what is genuinely new and writing the promotions) stays with the
    agent, under the AGENTS.md fidelity rules.

WHEN TO RUN A SYNTHESIS PASS (checkpoint synthesis — see AGENTS.md)
    Not every batch (wasteful churn) and not only at the very end (unwieldy, persona stays stale).
    Trigger a pass when EITHER an ingest channel/era completes, OR ~10 ingest batches (~100 videos)
    have accumulated since the last checkpoint — whichever comes first.

USAGE
    python tools/synthesis_batch.py status                 # show the mark, pending debt, targets
    python tools/synthesis_batch.py prepare                # work order for the next pending checkpoint
    python tools/synthesis_batch.py prepare --scope <keyword>    # filter the debt/notes by a keyword

STATE FILE: pipeline/synthesis-state.md
    - "## Pending checkpoints"  — markdown `- [ ]` items, oldest first; the loop drains top-down.
    - "## Done checkpoints"     — `- [x]` items with date + system-prompt version.
    The debt DETAIL lives in log.md as `Synthesis notes:` lines (every ingest batch appends one).

AFTER A PASS (the agent, then bump state):
    1. promote genuinely-new material into wiki/topics/ + persona/ (one agent edits ONE file)
    2. recompile persona/system-prompt.md (bump the version, e.g. v18 -> v19)
    3. in pipeline/synthesis-state.md: move the done checkpoint to "## Done", advance the mark
    4. append a `## [DATE] lint | synthesis pass N` entry to log.md; commit + push
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATE = REPO / "pipeline" / "synthesis-state.md"
LOG = REPO / "log.md"
TOPICS = REPO / "wiki" / "topics"
PERSONA = REPO / "persona"
NOTE_RE = re.compile(r"synthesis\s+(notes|backlog)\s*:", re.IGNORECASE)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def parse_checkpoints(state_text: str) -> tuple[list[str], list[str], str]:
    """Return (pending, done, high_water_line)."""
    pending, done = [], []
    section = None
    hwm = ""
    for line in state_text.splitlines():
        s = line.strip()
        if s.lower().startswith("## pending"):
            section = "pending"; continue
        if s.lower().startswith("## done"):
            section = "done"; continue
        if s.lower().startswith("## high-water"):
            section = "hwm"; continue
        if s.startswith("## "):
            section = None; continue
        if section == "pending" and s.startswith("- [ ]"):
            pending.append(s[5:].strip())
        elif section == "done" and s.startswith("- [x]"):
            done.append(s[5:].strip())
        elif section == "hwm" and s and not hwm:
            hwm = s
    return pending, done, hwm


def synthesis_notes(scope: str | None) -> list[str]:
    out = []
    for line in read(LOG).splitlines():
        if NOTE_RE.search(line):
            if scope is None or scope.lower() in line.lower():
                out.append(line.strip())
    return out


def list_targets() -> tuple[list[str], list[str]]:
    topics = sorted(str(p.relative_to(REPO)).replace("\\", "/")
                    for p in TOPICS.rglob("*.md")) if TOPICS.exists() else []
    persona = sorted(str(p.relative_to(REPO)).replace("\\", "/")
                     for p in PERSONA.glob("*.md")) if PERSONA.exists() else []
    return topics, persona


def cmd_status(_: argparse.Namespace) -> None:
    if not STATE.exists():
        print(f"No {STATE.relative_to(REPO)} yet — create it to start tracking synthesis.")
        return
    pending, done, hwm = parse_checkpoints(read(STATE))
    print("SYNTHESIS STATE")
    print(f"  high-water mark: {hwm or '(unset)'}")
    print(f"  done checkpoints:    {len(done)}")
    print(f"  PENDING checkpoints: {len(pending)}")
    for i, c in enumerate(pending, 1):
        print(f"    {i}. {c[:110]}")
    notes = synthesis_notes(None)
    print(f"\n  accumulated 'Synthesis notes:' lines in log.md: {len(notes)} "
          f"(the raw debt; run `prepare` to work them)")
    if pending:
        print("\n  -> next: python tools/synthesis_batch.py prepare")
    else:
        print("\n  -> no pending checkpoints: synthesis is caught up.")


def cmd_prepare(a: argparse.Namespace) -> None:
    pending, _done, hwm = parse_checkpoints(read(STATE))
    if not pending:
        print("No pending checkpoints — synthesis is caught up. Nothing to do.")
        return
    target = pending[0]
    print("# Synthesis work order")
    print(f"# high-water mark: {hwm}")
    print(f"# checkpoint: {target}\n")

    notes = synthesis_notes(a.scope)
    print(f"## Accumulated findings to promote ({len(notes)} 'Synthesis notes:' lines"
          + (f", filtered by '{a.scope}'" if a.scope else "") + "):")
    for n in notes:
        print(f"  - {n}")

    topics, persona = list_targets()
    print(f"\n## Promotion targets — persona/ ({len(persona)}):")
    for f in persona:
        print(f"  {f}")
    print(f"\n## Promotion targets — wiki/topics/ ({len(topics)}):")
    for f in topics:
        print(f"  {f}")

    print("""
================================================================================
DO THE SYNTHESIS (judgement half — one agent edits ONE file; per AGENTS.md)
================================================================================
For each genuinely-NEW finding above (a new framework, a bio fact, a position change, a
contradiction): promote it into the right topic/persona page — dated, cited to its
wiki/sources page, verbatim-vs-paraphrase kept, contradictions flagged (> callout),
position changes flagged. Do NOT re-add material already on the page. Long-tail repeats
that add nothing are dropped (they stay L2, already captured as source pages).

Then:
  1. If any persona file changed -> recompile persona/system-prompt.md (bump the version).
  2. In pipeline/synthesis-state.md: move this checkpoint to '## Done' (with date + version)
     and advance the high-water mark.
  3. Append a '## [YYYY-MM-DD] lint | synthesis pass N — <scope>' entry to log.md.
  4. Update index.md if new topic pages were created; commit + push.
  5. If more pending checkpoints remain and you are looping: run `prepare` again.
""")


def main() -> None:
    p = argparse.ArgumentParser(
        prog="synthesis_batch.py",
        description="Harness-neutral driver for the synthesis loop (promote L2 -> topics/persona). "
                    "See the module docstring and tools/SYNTHESIS.md.")
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # so em-dashes/emoji from the state file print cleanly
    except Exception:
        pass
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="show the high-water mark, pending checkpoints, accumulated debt")
    pp = sub.add_parser("prepare", help="emit a work order for the next pending checkpoint")
    pp.add_argument("--scope", help="filter the Synthesis-notes lines by a keyword (e.g. a channel handle)")
    args = p.parse_args()
    {"status": cmd_status, "prepare": cmd_prepare}[args.cmd](args)


if __name__ == "__main__":
    main()
