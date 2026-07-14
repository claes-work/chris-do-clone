# Synthesis loop (harness-neutral)

Ingesting grows the wiki **outward** (one `wiki/sources/` page per source, L2). Synthesizing grows it
**inward**: it promotes the genuinely-new material from many L2 pages into the `wiki/topics/` frameworks
and the `persona/` files, reconciles contradictions, dates positions, and recompiles the clone
(`persona/system-prompt.md`). Without it the library grows but the clone doesn't get smarter.

Synthesis runs as its own autonomous loop, the same in any harness (Claude Code, Codex, Pi).

---

## When to run a synthesis pass — CHECKPOINT SYNTHESIS
Not every batch (wasteful churn — most long-tail clips add nothing new) and not only at the very end
(unwieldy, and the persona stays stale for months). Trigger a pass when **EITHER**:
- an ingest **channel or a coherent era finishes**, **OR**
- **~10 ingest batches (~100 videos) have accumulated** since the last checkpoint,

whichever comes first. Landmark sources (books, origin-story / canonical-framework videos) are promoted
**inline at ingest time** (L3) and do not wait. The high-water mark lives in `pipeline/synthesis-state.md`.

## The two loops (how the whole system runs autonomously)
```
[ Ingest loop ]   tools/ingest_batch.py     drains ledger -> L2 source pages,
    │                                        logs a `Synthesis notes:` line per batch.
    │   (at a checkpoint: channel done / ~10 batches)
    ▼
[ Synthesis loop ] tools/synthesis_batch.py  drains the debt -> topics/persona (L3),
                                             recompiles system-prompt, advances the mark.
```
Alternate them: ingest a channel → synthesize it → next channel. Each is loopable until limit/stop.

---

## Step 0 — orient
```
python tools/synthesis_batch.py status
```
Shows the high-water mark, the pending checkpoints, and how many `Synthesis notes:` lines of debt
have accumulated in `log.md`.

## Step 1 — prepare (mechanical: gather the work order)
```
python tools/synthesis_batch.py prepare
```
Takes the next pending checkpoint and prints: its description, the accumulated `Synthesis notes:`
findings, the promotion targets (every `persona/` and `wiki/topics/` file), and the instructions.
(`--scope <keyword>` filters the notes, e.g. a channel or topic keyword.)

## Step 2 — promote (judgement: the agent)
For each genuinely-**new** finding (a new framework, a bio fact, a position change, a contradiction),
edit the right topic/persona page — **one agent edits ONE file** (the concurrency rule) — dated, cited
to its `wiki/sources/` page, verbatim-vs-paraphrase kept, contradictions/position-changes flagged with a
`>` callout. **Do NOT re-add material already on the page.** Long-tail repeats that add nothing are
dropped — they stay L2 (already captured as source pages). Quality over volume: a synthesis pass that
promotes 5 real new things beats one that bloats 20 pages with restated basics.

## Step 3 — recompile + record (bookkeeping)
1. If any `persona/` file changed → recompile `persona/system-prompt.md`, **bump the version** (e.g. v18→v19)
   and its `compiled_from_sources` count. Every trait must trace to a `wiki/sources/` citation.
2. In `pipeline/synthesis-state.md`: move the finished checkpoint to **## Done** (with date + version)
   and **advance the high-water mark**.
3. Append a `## [YYYY-MM-DD] lint | synthesis pass N — <scope>` entry to `log.md`.
4. Update `index.md` if new topic pages were created. Commit + push.
5. If looping and more pending checkpoints remain → back to Step 1.

---

## Running the synthesis loop in Codex / Pi (no slash commands)
Paste this as the session opener:

```
Read AGENTS.md and tools/SYNTHESIS.md. Then run one synthesis pass:
run  python tools/synthesis_batch.py prepare
For each genuinely-new finding, promote it into the right wiki/topics or persona file under the
fidelity rules (one file at a time; date + cite; flag contradictions; drop pure repeats). Then
recompile persona/system-prompt.md (bump the version), move the checkpoint to Done + advance the
high-water mark in pipeline/synthesis-state.md, append a log.md 'synthesis pass' entry, and commit +
push. Then repeat for the next pending checkpoint until none remain or I say stop.
```

- Use Codex full-auto approval + workspace-write sandbox with **network on** (for `git push`).
- **Never run an ingest loop and a synthesis loop on the same repo at the same time** (two agents editing
  one working tree corrupts it). One loop at a time per repo.

## Notes
- This is framework-shared: every persona repo uses the same two loops + `synthesis-state.md` contract.
- Full open-work overview: [`../BACKLOG.md`](../BACKLOG.md).
