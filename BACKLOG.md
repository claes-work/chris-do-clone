# BACKLOG — everything still open in this project

**How to use this in a NEW session:** just say _"Read BACKLOG.md and summarize what's
still open."_ This is the single human-readable checklist of all planned work. Tick
`[x]` when done; keep it current after each work block. (Machine state of truth for
sources stays in `pipeline/ledger.csv`; this file is the plain-language overview.)

**Snapshot:** _(not bootstrapped yet — run `/clone-setup <Full Name>`)_

---

## A. Bootstrap — OPEN
- [ ] Run `/clone-setup <Full Name>` (identity check → SUBJECT.md → biography research
      → source map → taxonomy → channel enumeration → first commit)

## B. Video ingest — blocked on A
- [ ] Drain P1 (landmark), then P2 long-form per channel (ingest loop)
- [ ] P3 guest content with attribution pass
- [ ] Shorts dedup (dupes → skipped with `dup-of:`, new → L2)
- [ ] Retry rows flagged `429` / `no-captions` / `unavailable`
- [ ] Checkpoint synthesis every ~10 batches / channel boundary (see E)

## C. Books / courses / landmark documents — blocked on A
- [ ] Identify what exists (bootstrap research fills this in)
- [ ] Obtain texts from the user → `raw/books/` → L3 ingest

## D. Other sources — blocked on A
- [ ] Websites/blog · press · X · Instagram · LinkedIn · podcast feeds · newsletters

## E. Synthesis / persona — ongoing once B starts
- [ ] Keep synthesis debt drained (`python tools/synthesis_batch.py status`)
- [ ] Recompile `persona/system-prompt.md` after every persona-touching pass (bump version)
- [ ] Persona-QA sessions → feed `wiki/gaps.md`
- [ ] Final lint when the corpus drains

## F. Multi-clone future — see VISION.md
- [ ] More people, each in its own repo built from this template
- [ ] Clones as cooperating agents (shared data contract, knowledge never mixed)
