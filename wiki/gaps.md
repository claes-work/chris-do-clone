---
type: meta
updated: 2026-07-17
---

# Gaps

Known gaps in the clone. Fed by persona-session QA (voice that rang false, knowledge
that was missing) and by lint passes. Each entry: date noticed, what was missing, and
— once resolved — the source that filled it.

## Open

- **2026-07-17 — VERIFY: self-reported early-Blind financials.** In "Personal Projects After a Full-Time
  Job" ([[wiki/sources/2018-10-07-yt-kKLZYk6t7A8]]) Chris states he founded Blind by age 22 and did
  "$2M in billings in the first two years." Self-reported; corroborate against the biography dossier
  (which has the ~1995 founding) before entering these figures into `persona/biography.md`.

- **2026-07-17 — VERIFY: self-reported "military / Army background".** In the million-dollar-loss
  postmortem ([[wiki/sources/2017-05-23-yt-3LSk_YXpldc]]) Chris references a military/Army background
  and the Army "after-action review" (AAR) practice. This is NOT in the biography dossier (which has
  refugee→San Jose→ArtCenter→Blind, no military service). Source page is `attribution: uncertain`.
  Do NOT propagate "Army service" as biographical fact until corroborated — it may be a borrowed
  concept (AAR) rather than personal service. Also unresolved: self-reported "two Emmys"
  ([[wiki/sources/2017-02-17-yt-BFhxfcHCjK8]]) vs registry-verified single Emmy.

- **2026-07-17 — Spoken-voice cadence essentially uncaptured.** persona/voice.md v1 was
  built from the biography/media-inventory dossiers only (no transcripts ingested yet).
  Sentence rhythm, his Socratic/question-first role-play style, fillers, talk
  openers/closers, and humor delivery are all missing. voice.md should be substantially
  rewritten after the first long-form YouTube/podcast ingest batches. (Noticed in Stage P
  persona v1 compile.)
- **2026-07-17 — Humor thin.** Only dry irony (the "Blind" naming) is documented; needs
  transcript evidence for jokes/delivery.
- **2026-07-17 — Belief depth is biography-level, not tactical.** beliefs.md v1 covers
  worldview but lacks the granular course-level positions (negotiation moves, positioning
  mechanics, content-strategy specifics). Fills in during synthesis after topic ingest.
- **2026-07-17 — appearance.md still empty.** Needs a watched-video sample (~10–20 across
  years) per ROADMAP Phase 3; captions can't supply it.
- **2026-07-17 — POLICY QUESTION: a son's name is now self-reported on-camera.** In the
  AIGA 2019 keynote ([[wiki/sources/2019-08-12-yt-f7T1Zs28Deo]]) Chris names one of his
  sons. SUBJECT.md's standing rule treats family names as not-public, so the name was
  **redacted** from that source page. Decision needed from the repo owner: keep the
  blanket redaction, or allow names Chris himself has stated publicly. Until decided,
  loops keep redacting family names everywhere.

- ⭐ **PARTIALLY RESOLVED 2026-07-28 (batch 271).** [[wiki/sources/2019-03-22-yt-_1MIAMxixag]] — an
  @TheFuturAcademy art-direction tutorial opening *"Hey everybody, **Chris** here"* — contains
  ***"You're using **Futura** right there. **I like Futura.** It's part of the identity we've been
  using."*** ✅ **Self-identified, unscripted, and tied to a concrete decision** — everything the five
  *Fonts You NEED To Know* clips were not. **The clone can now name one typeface he likes.** The
  broader gap (a fuller picture of his typographic taste, and the narrator of that series) remains
  open. Original entry follows.

- **No recorded typeface preferences — a real hole for a designer persona.** (found 2026-07-28,
  Stage-C shorts batch 255) `favourite typeface` returns **0** across the whole corpus. The shorts
  queue contains a produced series, *Fonts You NEED To Know* (e.g. `yt-n18wQwjpt4k`, LaFarge,
  2022-02-16), whose script opens *"LaFarge is one of my favorite typefaces"* — but it is written in
  **third-person editorial register** (*"Gregory Shutters carefully inspected every original
  letter"*) with **no self-identification**, so it was closed `attribution-uncertain` rather than
  ingested. ⚠️ ✅ **Corroborated the next batch (256):** `yt-qtmpJi-4taw` opens *"**Archivo** is one of my favorite
  typefaces"* — **the identical formula**, same series, `archivo` also **0** corpus-wide. This is a
  recurring format with a templated first line, which **weakens** the case that any single instance
  reflects the subject's own taste and **strengthens** the need to identify the narrator once for the
  whole series rather than clip by clip.

  ✅ **Third instance, batch 257:** `yt-Su3KTdOhgro` — *"**News Reader** is one of my favorite
  typefaces."* **Five for five on the same opening line** (LaFarge · Archivo · News Reader · Lejeune · **Neue Haas Grotesque**, batch 259), each
  returning **0** corpus-wide. The formula is now conclusively a **series template**. ⚠️ Treat every
  remaining *Fonts You NEED To Know* row as ONE decision, not N findings.

  **Resolving who narrates that series would unlock a genuine persona dimension**: for a
  subject who taught typography at ArtCenter, the clone currently cannot name a single typeface he
  likes. Needs the video, not the captions.

## Resolved
