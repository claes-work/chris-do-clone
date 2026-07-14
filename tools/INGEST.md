# Ingest workflow (harness-neutral)

This repo is ingested the same way in **any** agent harness (Claude Code, Codex, Pi, …).
The rules live in [`AGENTS.md`](../AGENTS.md); this file is the operational how-to.
The subject + TARGET channels live in [`SUBJECT.md`](../SUBJECT.md) — read it first.

An ingest batch has two halves:

| Half | Who does it | Tool |
|------|-------------|------|
| **1. Mechanical** — pick next open rows, fetch captions, clean to text, tidy the ledger | a script | `tools/ingest_batch.py` |
| **2. Judgement** — read each transcript, write a faithful `wiki/sources/` page | the agent | (the model, under AGENTS.md fidelity rules) |

`ingest_batch.py` owns half 1 so the agent only has to do half 2. It never writes source
pages, touches `persona/`, or commits — those stay judgement calls.

---

## Prerequisites
- `yt-dlp` and `python` (3.10+) on PATH. (`ffmpeg` only needed later for video/audio work.)
- Run all commands from the **repo root**.

## Step 0 — orient
```
python tools/ingest_batch.py status
```
Shows open long-form rows per channel (by priority), open shorts, L2/L3 totals, and the
current `youtube-index.md` footer count.

## Step 1 — prepare the next batch (mechanical)
```
python tools/ingest_batch.py prepare --channel @ChannelHandle --n 10
```
For each selected row it: fetches captions (yt-dlp, manual→auto, `en.*`, vtt) into
`raw/youtube/<slug>/`, converts the `.vtt` to `.txt`, classifies the outcome, backfills a
missing `published` date from the real upload date, **auto-marks** `no-captions`/`unavailable`
rows in the ledger, leaves `429`/errors open for retry, and prints a **work order** (human
list + a `json` block) naming each transcript file and its target page path.

Useful flags:
- `--n N` — batch size (default 10)
- `--priority 1|2|3` — restrict to a tier (P1 landmark first, then P2, then P3)
- `--include-shorts` — also consider `short` rows (default: long-form only)
- `--dry-run` — selection only, no network, no changes (preview)
- `--no-mark` — do not modify the ledger at all (pure fetch test)

Selection order: priority ascending, then oldest `published` first (undated rows last, in
ledger order). Rows whose `notes` contain `429`, `no-captions`, `unavailable`, or `dup-of`
are skipped automatically.

## Step 2 — write the pages (judgement — the agent)
For every OK video in the work order, read `raw/.../<id>.en.txt` and write the target
`wiki/sources/<published>-yt-<id>.md` under the AGENTS.md **fidelity rules**:
frontmatter (`type: youtube-video`, `source_date`, `url`, `channel`, `ingested`, `tier: L2`,
`domains`) + `## Summary` + `## Key claims` (paraphrase, **dated**) + `## Notable verbatim
quotes` (`>` blockquotes = voice-training data). Cite; separate verbatim from paraphrase;
date opinions; attribute per speaker (**only the SUBJECT** trains the persona); flag
contradictions; catch caption garbles (names/numbers); **English only**.

Throughput tip: in harnesses without parallel sub-agents (Codex/Pi), just process the videos
sequentially, or bundle several heavily-overlapping short videos into one page-writing pass.
Slower than Claude Code's parallel fan-out, but the same quality.

## Step 3 — bookkeeping (unchanged, per video / per batch)
```
python tools/ledger_set.py <id> status=L2 "domains=a;b" "notes=short handle for the index"
```
Then:
1. Insert one row per new page into `wiki/sources/youtube-index.md`, **in date order**.
2. Bump the footer count `_NNN videos ingested (L2)…_` and the `index.md` count by the batch size.
3. Append **one** `log.md` entry for the batch (heading `## [YYYY-MM-DD] ingest | …`). End it with a
   short **`Synthesis notes:`** line naming anything genuinely new (a framework, bio detail, a
   contradiction) — L2 batches do NOT promote to topics/persona themselves; a later synthesis pass does,
   and it finds the debt via `grep -i "synthesis" log.md`. (If nothing new: `Synthesis notes: none`.)
4. Commit + push.

> **Synthesis is the OTHER loop** (by design — AGENTS.md tiers). Do not promote L2 material into
> `topics/`/`persona/` inside a normal batch unless a source is genuinely landmark. At a checkpoint —
> **after each channel/era, or every ~10 batches** — switch to the synthesis loop:
> `python tools/synthesis_batch.py status` → `… prepare`. See [`SYNTHESIS.md`](SYNTHESIS.md) and
> `pipeline/synthesis-state.md`.

> ⚠️ **Commit-message gotcha (Windows/PowerShell):** double quotes inside a here-string
> `-m` argument get word-split by PowerShell and break the commit. Keep commit messages
> free of embedded `"` quotes. In bash/Codex this is not an issue.

## Running a batch in Codex / Pi (no slash commands)

`/loop` and `/ingest-loop` are **Claude Code only** (self-scheduling + `.claude/` skills).
In Codex/Pi there are no slash commands and no unattended scheduling — you drive batches with a
plain instruction. Paste this as the session opener (adjust channel/count):

```
Read AGENTS.md, SUBJECT.md, tools/INGEST.md and tools/SYNTHESIS.md. Then run one ingest batch:
run  python tools/ingest_batch.py prepare --channel @ChannelHandle --n 10
For each OK video in the work order, read its transcript and write the wiki/sources page
under the fidelity rules. Then set each ledger row to L2 (tools/ledger_set.py), insert the
rows into wiki/sources/youtube-index.md in date order, bump the footer + index.md counts,
append one log.md entry (ending in a `Synthesis notes:` line), and commit + push.
IMPORTANT: if the driver prints a ">>> CHECKPOINT" banner (channel complete, or >=10 batches
since the last synthesis), STOP ingesting and run one full synthesis loop instead
(python tools/synthesis_batch.py prepare -> do the pass -> commit), then resume ingesting.
Repeat this ingest/checkpoint rhythm until I say stop.
```

This single opener runs **both loops in one session**: it ingests, and whenever the driver flags a
checkpoint it switches to synthesis, then resumes. One agent alternating the two loops is safe (the
"never both at once" rule is only about two *separate* sessions on the same repo).

- To run several batches back-to-back without prompts, use Codex's full-auto approval mode (with
  the workspace-write sandbox + **network enabled** — yt-dlp and `git push` need it).
- There is no "run while I'm away" like Claude's scheduled loop; it runs while the session is open.
- No parallel sub-agents in Codex/Pi → videos are processed sequentially (slower, same quality).

## Notes
- `raw/` is gitignored (copyrighted transcripts). The script only reads/writes there + the ledger.
- Every batch ends in a pushed commit, so an interruption loses at most the current batch; the
  ledger makes resume exact.
- Full open-work checklist across all workstreams: [`../BACKLOG.md`](../BACKLOG.md).
