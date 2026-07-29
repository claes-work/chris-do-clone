# BACKLOG — everything still open in this project

**How to use this in a NEW session:** just say _"Read BACKLOG.md and summarize what's
still open."_ This is the single human-readable checklist of all planned work. Tick
`[x]` when done; keep it current after each work block. (Machine state of truth for
sources stays in `pipeline/ledger.csv`; this file is the plain-language overview.)

**Snapshot (2026-07-29):** **1,045 sources ingested (L2)**, system-prompt **v24**,
synthesis current through pass 27. Ledger, files and `youtube-index.md` reconcile
**as sets**, not merely as counts (verified 2026-07-28 after a lint found two
offsetting bookkeeping errors).

**Done:** @thefutur long-form and shorts · @ChrisDo · @TheFuturAcademy triage.
**In progress:** the **235 @thefutur livestreams**, brought into scope 2026-07-29 on
the owner's decision — `tools/ingest_batch.py` had hard-coded `type == "video"` at three
call sites, so streams were counted nowhere and selected never (found log.md batch 217).
**232 still open.** The first one fetched was the *Unbland* book launch.

**Two owner decisions still open** — see section B.

---

## A. Bootstrap — DONE 2026-07-14
- [x] Run `/clone-setup Chris Do` (identity check → SUBJECT.md → biography research
      → source map → taxonomy → channel enumeration → first commit)

## B. Video ingest — MOSTLY DONE, streams in progress
- [x] Drain P1 (landmark), then P2 long-form per channel (ingest loop)
- [x] P3 guest content with attribution pass
- [x] Shorts dedup — **~800 shorts triaged, ~20 ingested** (~1 in 80; the tail is recuts of
      long-form that was already ingested). @thefutur shorts complete 2026-07-28.
- [x] ~~PO-token blocker (2026-07-21)~~ — **RESOLVED.** Caption fetching has worked throughout
      the 2026-07-28/29 runs (batches 239–274). Kept visible rather than deleted so the history
      of the block stays readable.
- [ ] **Livestreams — 232 of 235 still open** (scope opened 2026-07-29). Expect a meaningful
      `members-only` fraction: 2 of the first 3 were auto-skipped by the batch-199 detector.
      ⚠️ Ledger `published` is `NA` for all stream rows; **the real date comes from the caption
      fetch** (raw filename), so set `published=` when writing each page.
- [ ] ⚠️ **OWNER DECISION 2 — 88 `no-captions` rows.** Approve Whisper transcription? 45 are
      @thefutur long-form (possibly valuable), 43 are shorts (likely recuts).
      **Recommendation: long-form only, if any.** Whisper is never run without explicit approval.
- [x] ⚠️ **OWNER DECISION 3 — @TheFuturAcademy.** Closed out 2026-07-28: instructor-led channel
      (Encina, Gunn, Contreras). Long-form drained; 3 Chris-fronted rows found and ingested,
      including the corpus's only self-identified typeface preference.
- [ ] Retry rows flagged `429` / `unavailable`
- [x] Checkpoint synthesis every ~10 batches / channel boundary (see E) — passes 1–27 done

## C. Books / courses / landmark documents — OPEN
- [x] Identify what exists: *Pocket Full of Do* (2019, ISBN 9780578551333) and
      *Unbland Yourself* (Dec 2025 digital workbook); 15 Teachable courses at
      academy.thefutur.com (see media inventory dossier)
- [ ] Obtain texts from the user → `raw/books/` → L3 ingest

## D. Other sources — OPEN (23 named guest appearances listed in the media
      inventory dossier are ready ledger candidates)
- [ ] Websites/blog · press · X · Instagram · LinkedIn · podcast feeds · newsletters

## E. Synthesis / persona — ongoing once B starts
- [x] Keep synthesis debt drained — **passes 1–27 complete**, high-water mark at batch 273
- [ ] ⚠️ **L3 promotion owed:** [[wiki/sources/2025-12-22-yt-Zo_SxRuUGjQ]] (the *Unbland* book
      launch) is a **LANDMARK** filed at L2. Promote the launch date, the digital-first publishing
      rationale, the public product pricing and the edition ladder — **not** the doctrine, which
      already sits in the hubs from 2026-04-07. ⚠️ The stream is 21.8k words and was **sampled,
      not read end to end**; re-read before treating its page as complete.
- [ ] Recompile `persona/system-prompt.md` after every persona-touching pass (bump version)
- [ ] Persona-QA sessions → feed `wiki/gaps.md`
- [ ] Final lint when the corpus drains

## F. Multi-clone future — see VISION.md
- [ ] More people, each in its own repo built from this template
- [ ] Clones as cooperating agents (shared data contract, knowledge never mixed)
