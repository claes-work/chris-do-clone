# ROADMAP — Mass Ingestion Plan

> 📋 **For the plain-language "what's still open" checklist across ALL workstreams, see
> [`BACKLOG.md`](BACKLOG.md).**

_The execution plan the curator follows autonomously across sessions. The ledger
tracks per-item progress; this file tracks per-phase progress. Phases 0–1 are done by
the bootstrap (`/clone-setup` / [`BOOTSTRAP.md`](BOOTSTRAP.md))._

## Guiding principles

1. **Persona-first prioritization.** Work is ordered by what improves the fidelity of
   `persona/system-prompt.md` fastest per unit of effort.
2. **Nothing enters the wiki untracked.** Every source gets a ledger entry before
   ingestion; every ingest updates the ledger status.
3. **Tiered ingestion** (L1 cataloged / L2 light / L3 full — see AGENTS.md). Books and
   landmark videos get L3; the long tail gets L2; everything starts at L1.
4. **Captions first, AI transcription only as fallback** (and only with user approval —
   it costs money).
5. **Attribution discipline.** Only subject-attributed material trains the persona;
   low-confidence attribution is flagged, never silently included.
6. **Recurring other people** get `wiki/entities/` context pages, clearly marked as
   context — the persona clones the subject only.

## Phase 0 — Identity & infrastructure _(done by bootstrap)_
Identity verified with the user; `SUBJECT.md` written; domain taxonomy + hub pages
created; persona alias command created; subject-specific priority markers added to
`tools/merge_staging.py`.

## Phase 1 — Biography & master source map _(done by bootstrap)_
Deep web research → biography dossier + `persona/biography.md` v1; media-inventory
dossier (every channel/podcast/site/social with verified IDs); entities pages;
channels enumerated into the ledger with view-based P1 promotion.

## Phase 2 — Books & landmark documents (L3, highest knowledge density)
If the subject has books/courses: file them under `raw/books/`, ingest chapter-by-
chapter (source page per chapter, framework pages in topics/), per-book synthesis +
voice/beliefs updates with verbatim quote banks, system-prompt recompile per book.
*Needs from user: the texts (purchased copies dropped into `raw/books/`).*

## Phase 3 — Video corpus (the bulk) — _COMPLETE within the approved scope_
Drain the ledger by priority via the ingest loop (`/loop /ingest-loop`, or the Codex/Pi
opener in `tools/INGEST.md`): P1 landmark → P2 long-form → P3 guest content (with
attribution pass) → shorts dedup. Checkpoint synthesis every ~10 batches / channel
boundary. A small watched-video sample (~10–20 across years) grounds
`persona/appearance.md` and the visual half of `voice.md`.

**Status 2026-07-29 — 1,045 sources at L2.** Long-form and shorts are drained across
@thefutur, @ChrisDo and @TheFuturAcademy. **232 livestreams remain**, opened on
2026-07-29 after a driver fix.

> ⚠️ **Lesson worth keeping — a queue can look drained because the tool cannot see it.**
> `tools/ingest_batch.py` hard-coded `type == "video"` at three separate call sites, so
> 235 `stream` rows were **counted nowhere and selected never**; `status` reported
> @thefutur as complete while a book launch, business Q&As and guest sessions sat
> untouched. Fixed by routing all three through one `LONGFORM_TYPES` constant.
> **When a channel reports "drained", check what the residual rows ARE before believing it.**

## Phase 4 — Articles, websites, social, press
Websites/blog, press coverage, X/Instagram/LinkedIn posts (best-effort; platform
limits may require exports from the user), podcast feeds not covered by YouTube.

## Phase 5 — Freshness automation (cron)
Weekly: enumerate channels/feeds → append new items → auto-L2 → commit + report.
Monthly lint. *Needs from user: consent to install schedules.*

## Phase status

- [x] Phase 0 — Identity & infrastructure (bootstrap) — done 2026-07-14
- [x] Phase 1 — Biography & source map (bootstrap) — done 2026-07-14
- [ ] Phase 2 — Books & landmark documents — ⚠️ *Unbland* launch ingested (L2, L3 owed); book TEXTS still needed from user
- [x] Phase 3 — Video corpus — ⭐⭐ **COMPLETE within the approved scope, 2026-07-31 (L2 1,086).** Long-form, shorts and all 235 livestreams triaged, **plus the whisper back-catalogue**: the 51 no-caption long-form/stream rows the owner approved for AI transcription on 2026-07-31 were transcribed (31 ok, 4 rejected by a 50-word floor as music/silence) and fully triaged. **Open long-form: ZERO.** ⚠️ **51 rows remain at L1, all `no-captions`: 45 @thefutur shorts (explicitly EXCLUDED from the transcription approval — a 1-in-80 hit rate made them the worst use of the budget), 5 @TheFuturAcademy software tutorials and 1 @ChrisDo trailer (outside the approved channel).** **These are blocked on an owner scope decision, not on work.** ✅ Verified 2026-07-31 that the shorts genuinely still have no caption tracks (yt-dlp, against a known-positive control).
- [ ] Phase 4 — Articles & social
- [ ] Phase 5 — Automation

> ⚠️ **Second lesson, 2026-07-31 — `no-captions` is not a permanent property.** Three rows flagged
> `no-captions` and whisper-transcribed that morning had **acquired real YouTube caption tracks** by the
> afternoon; `ingest_batch.py prepare` fetched them and replaced the machine transcripts. **Part of that
> day's transcription compute was avoidable.** ✅ The flag should be **re-checked** before any future
> transcription run, not trusted. ⚠️ It does not rescue everything: the two highest-value whisper sources
> (the Dublin keynote and the Roland Young origin stream) still have no captions.
