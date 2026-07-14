---
description: Autonomous "finish everything" loop — persona refinement, remaining P1/P2 long-form, new channels, shorts dedup — until the whole corpus is done. Run via "/loop /ingest-loop".
---

You are the CURATOR (see CLAUDE.md — it governs everything). This loop runs ONE unit of
work per iteration and KEEPS GOING across wakeups until ALL remaining work is finished.
**Do not recommend stopping or pausing. Do not stop early.** Only Stage D (everything
drained) ends the loop. Batch size: $ARGUMENTS (default 8).

**Precondition**: `SUBJECT.md` says `STATUS: INITIALIZED` — otherwise stop and tell the
user to run `/clone-setup <Full Name>` first.

## 0. Orient (every iteration)

1. Read **SUBJECT.md** (the TARGET channel list + subject-specific rules — they grow
   over time and override this file's generic guidance).
2. `grep "^## \[" log.md | head -6` (recent history) and read ROADMAP.md status.
3. `python tools/ingest_batch.py status` for pipeline state (it also prints the
   synthesis debt counter).
4. Pick the stage — **first matching rule wins**:
   - **Synthesis checkpoint due** (driver prints `>>> CHECKPOINT`, a channel/era just
     completed, or ≥10 ingest batches since the last synthesis) → **Stage S**.
   - **Persona is stale** → **Stage P**. Stale means: ≥10 ingest batches since the last
     `lint | Synthesis`/`Persona` log entry, OR new topic pages exist that
     `persona/beliefs.md`+`voice.md` don't reflect, OR P1 just fully drained. **On the
     very first run of this loop, treat persona as stale.**
   - **A TARGET channel (SUBJECT.md) has ZERO ledger rows** → **Stage A** (enumerate).
   - **Open P1 long-form rows exist** → **Stage B** (ingest, P1 first).
   - **Open P2 long-form rows exist** → **Stage B** (ingest, P2).
   - **Only shorts open** → **Stage C** (shorts dedup).
   - **Nothing open** → **Stage D** (final wrap-up, then STOP the loop).

   If you discover another official channel of the subject during the loop, add it to
   SUBJECT.md's TARGET list (with a note) and enumerate it via Stage A.

## Stage S — Synthesis checkpoint (drains the debt)

Run one full synthesis pass per `tools/SYNTHESIS.md`:
`python tools/synthesis_batch.py prepare` → promote each genuinely-new finding into the
right `wiki/topics/` / `persona/` page (one agent edits ONE file; dated, cited,
contradictions flagged; drop pure repeats) → recompile `persona/system-prompt.md`
(bump version) → advance the high-water mark in `pipeline/synthesis-state.md` → log
`lint | synthesis pass N`, commit, push. Then resume ingest next iteration.

## Stage P — Persona refinement (delegate; persona-files-only)

Refresh the product from everything ingested since the last pass. Delegate to ONE agent
(keeps coordinator context clean; single writer avoids persona-file write races). The
agent edits ONLY persona/beliefs.md, persona/voice.md, persona/system-prompt.md. Its
brief: read the synthesized topic pages + current persona files; (a) add dated, cited
beliefs; (b) add characteristic verbatim quotes/catchphrases to voice.md;
(c) recompile system-prompt.md, bumping version + source count. Fidelity rules binding;
only subject-attributed material. Coordinator then updates index.md, logs
`lint | Persona pass`, commits, pushes.

## Stage A — Enumerate a channel (network)

Run `tools/fetch_channel.ps1` for the channel's /videos and /shorts tabs →
`python tools/merge_staging.py --channel <handle> --videos <v.csv> --shorts <s.csv>` →
`python tools/backfill_metadata.py --channel <handle> --top 50` (fills dates/views,
promotes top-by-views to P1; if it rate-limits, log and continue). Delete staging CSVs.
Log (`ingest`), commit (`ledger: enumerate <handle>`), push.

## Stage B — Ingest batch (the normal case)

Parallelize with one subagent per video. **Concurrency rule: subagents write ONLY their
own `wiki/sources/<page>.md`; they must NOT touch index.md, log.md, or
pipeline/ledger.csv — the coordinator does all shared-file updates after agents return.**
1. `python tools/ingest_batch.py prepare --channel <handle> --n $ARGUMENTS` (default 8).
   Eyeball titles first: skip promo trailers, joke videos, and videos featuring only
   OTHER people (mark them `skipped` with a reason); flag likely duplicates.
   Apply the **subject-specific rules from SUBJECT.md** (e.g. a company channel that is
   mostly not the subject → single-agent light-triage instead of one agent per video;
   a high-value topic the repo owner cares about → always full treatment).
2. Per OK video in the work order: a subagent reads the transcript and writes the
   source page: frontmatter (type, source_date, url, channel, ingested, tier: L2,
   domains, tags), summary, dated key claims, a verbatim quote bank, guest attribution
   (only subject-attributed = persona data; uncertain → flag). Note L3-candidates with
   ★ for the next synthesis (do not inline-promote). No captions → ledger
   `notes: no-captions`, skip (never Whisper without user approval).
3. Coordinator: `python tools/ledger_set.py <id> status=L2 "domains=…" "notes=…"` per
   video, insert rows into wiki/sources/youtube-index.md in date order + bump its
   footer count and the index.md count, append ONE `ingest` log entry **ending with a
   `Synthesis notes:` line** (anything genuinely new, or `none`), commit
   (`ingest: yt batch (<handle>, <n>)`), push.

## Stage C — Shorts dedup

Batch through open shorts (bigger batches, e.g. 20). Fetch captions; compare each
transcript against existing long-form source pages (title + content similarity).
Duplicate → ledger `status: skipped`, `notes: dup-of:<yt-id>`, no page. Genuinely-new
short → L2 ingest (light: summary + 2-3 quotes). Same bookkeeping. Log counts of
dup-vs-new per batch (no silent caps).

## Stage D — Final wrap-up (ends the loop)

When nothing is open: run a FINAL Stage S + Stage P (synthesis + persona refresh over
the whole corpus), then a lint pass (contradictions, orphans, index/ledger consistency,
system-prompt drift), mark the ROADMAP ingest phase done, write a
`lint | corpus complete` log entry with final counts, commit, push. Then STOP THE LOOP
(no further wakeup) and send a one-line PushNotification that the corpus is complete.

## Safety rails (non-negotiable)

- raw/ is immutable once written. Every batch ends in a pushed commit — an interruption
  loses at most one batch; the ledger makes resume exact.
- 3 consecutive yt-dlp failures → assume rate-limiting: log, commit done work, and end
  THIS iteration gracefully (still schedule the next wakeup — do not abandon the loop).
- Never fabricate; no captions → no ingest; all repo content English.
- **Keep the loop alive**: every iteration, after committing, schedule the next wakeup
  (delaySeconds ~60) with this same `/loop /ingest-loop` prompt, UNLESS Stage D ran.

## Report (end of every iteration)

Stage executed, items processed (ingested/skipped/no-captions/dup), ledger counts
(open P1/P2/shorts, L2, L3), synthesis debt, and what the next iteration will do.
