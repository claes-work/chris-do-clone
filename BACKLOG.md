# BACKLOG — everything still open in this project

**How to use this in a NEW session:** just say _"Read BACKLOG.md and summarize what's
still open."_ This is the single human-readable checklist of all planned work. Tick
`[x]` when done; keep it current after each work block. (Machine state of truth for
sources stays in `pipeline/ledger.csv`; this file is the plain-language overview.)

**Snapshot (2026-07-14):** Bootstrap complete for **Chris Do** (The Futur). Ledger:
2,345 items, all L0 — 66 P1 / 1,069 P2 / 1,210 P3; 1,251 long-form + 859 shorts +
235 streams across @thefutur, @TheFuturAcademy (catalog tier), @ChrisDo. Books
identified: *Pocket Full of Do* (2019), *Unbland Yourself* (2025) — texts needed
from user. Next: `/loop /ingest-loop`.

---

## A. Bootstrap — DONE 2026-07-14
- [x] Run `/clone-setup Chris Do` (identity check → SUBJECT.md → biography research
      → source map → taxonomy → channel enumeration → first commit)

## B. Video ingest — OPEN
- [ ] Drain P1 (landmark), then P2 long-form per channel (ingest loop)
- [ ] P3 guest content with attribution pass
- [ ] Shorts dedup (dupes → skipped with `dup-of:`, new → L2)
- [ ] Retry rows flagged `429` / `no-captions` / `unavailable`
- [ ] **Blocker (2026-07-21):** yt-dlp caption fetch is globally blocked by YouTube's PO-token
      requirement on this machine (confirmed against an unrelated control video, not corpus-
      specific) — 0/8 fetched in the last attempted batch. Install/configure a PO-token
      provider (e.g. `bgutil-ytdlp-pot-provider`) or update yt-dlp before running further ingest
      batches; see `log.md` 2026-07-21 entry for the verification steps.
- [ ] Checkpoint synthesis every ~10 batches / channel boundary (see E)

## C. Books / courses / landmark documents — OPEN
- [x] Identify what exists: *Pocket Full of Do* (2019, ISBN 9780578551333) and
      *Unbland Yourself* (Dec 2025 digital workbook); 15 Teachable courses at
      academy.thefutur.com (see media inventory dossier)
- [ ] Obtain texts from the user → `raw/books/` → L3 ingest

## D. Other sources — OPEN (23 named guest appearances listed in the media
      inventory dossier are ready ledger candidates)
- [ ] Websites/blog · press · X · Instagram · LinkedIn · podcast feeds · newsletters

## E. Synthesis / persona — ongoing once B starts
- [ ] Keep synthesis debt drained (`python tools/synthesis_batch.py status`)
- [ ] Recompile `persona/system-prompt.md` after every persona-touching pass (bump version)
- [ ] Persona-QA sessions → feed `wiki/gaps.md`
- [ ] Final lint when the corpus drains

## F. Multi-clone future — see VISION.md
- [ ] More people, each in its own repo built from this template
- [ ] Clones as cooperating agents (shared data contract, knowledge never mixed)
