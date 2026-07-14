---
description: Run synthesis passes (promote genuinely-new L2 material into topics/persona, recompile the system prompt) until no pending checkpoints remain. Run via "/loop /synthesis-loop" or once as /synthesis-loop.
---

You are the CURATOR (see CLAUDE.md). Run the SYNTHESIS loop per
[`tools/SYNTHESIS.md`](../../tools/SYNTHESIS.md) — read it now.

**Preconditions**: `SUBJECT.md` is INITIALIZED, and **no ingest loop is running on this
repo right now** (never both loops at once — two agents editing one working tree
corrupts it).

Per iteration (one checkpoint):

1. `python tools/synthesis_batch.py status` → if no pending checkpoints AND no debt,
   report "caught up" and STOP the loop.
2. `python tools/synthesis_batch.py prepare` → work order for the next checkpoint.
3. Promote each genuinely-**new** finding (framework, bio fact, position change,
   contradiction) into the right `wiki/topics/` / `persona/` page — **one agent edits
   ONE file** — dated, cited to its `wiki/sources/` page, verbatim-vs-paraphrase kept,
   contradictions flagged with a `>` callout. Drop pure repeats (they stay L2).
   Quality over volume: 5 real promotions beat 20 bloated pages.
4. If any `persona/` file changed → recompile `persona/system-prompt.md` (bump the
   version + `compiled_from_sources` count; every trait must trace to a citation).
5. Bookkeeping: move the checkpoint to **## Done** + advance the high-water mark in
   `pipeline/synthesis-state.md`; update `index.md` for new topic pages; append a
   `## [YYYY-MM-DD] lint | synthesis pass N — <scope>` log entry; commit + push.
6. More pending checkpoints → next iteration (schedule a wakeup if running via /loop).
