# Log

_Append-only change record. Entry format: `## [YYYY-MM-DD] <type> | <title>` with_
_`<type>` ∈ `setup | plan | ingest | query | lint | persona-qa`._
_Ingest entries end with a synthesis-notes line (the synthesis-debt trail)._

## [2026-07-14] setup | research: biography dossier

Phase-2 web research → `wiki/sources/2026-07-14-research-biography-dossier.md` +
`persona/biography.md` v1. Key finds: Chris Do's own resume PDF (primary source for
teaching years, boards, early jobs, "Cofounded The Skool with Jose Caballer");
Emmy registry-verified via Television Academy (2010, Outstanding Individual
Achievement in Animation, as ART DIRECTOR on "Heart of Stone" — press "director"/
"Grammy" errors flagged); new pre-Blind details (Kansas City 1975 via church
sponsorship, San Jose ~1977, San Diego City College 1990 → ArtCenter BFA 1995 with
honors). Contradiction logged: Skool founding 10/2013 (resume) vs 2014 (press) —
reconciled as partnership 2013, launch 2014. Open: exact DOB, high-school name.

## [2026-07-14] setup | research: media inventory dossier

Phase-2 web research → `wiki/sources/2026-07-14-research-media-inventory-dossier.md`.
Podcast RSS pinned (Megaphone TFL6245334029, 445 eps); course platform
academy.thefutur.com (Teachable, 15 named courses); thefutur.com/watch = YouTube
mirrors (do-not-ledger rule); 23 external guest appearances named (18 with episode
URLs) as future ledger candidates. Instagram: 1M displayed vs ~837K tracker — both
recorded.

## [2026-07-14] setup | research: entity pages

Phase-2 research → 6 pages in `wiki/entities/` (blind, the-futur, the-skool,
jose-caballer [context], futur-instructors [context], thefutur-youtube).
Registry-verified via CA SOS: THE FUTUR, LLC #201621110421 (filed 2016-07-25,
active); BLIND VISUAL PROPAGANDA, INC. #C1988167 (filed 1997-07-18 — founding 1995
is self-reported only; status "Merged Out" 2020-12-31 into Palisades Investment
Management, Inc.). Revenue figures all self-reported and flagged; Futur year-1
revenue contradiction ($15K vs $18K) flagged in-page.

## [2026-07-14] setup | bootstrap: Chris Do

Repo initialized for Chris Do (The Futur) — identity user-confirmed 2026-07-14.
SUBJECT.md written; 7-domain taxonomy (pricing, sales-clients, business, branding,
content-strategy, mindset, design-craft) user-confirmed, hubs created; /chrisdo
persona alias created; P1/P3 markers added to merge_staging.py. Corpus enumerated:
2,345 ledger rows, all L0 — @thefutur 2,249 (1,177 videos + 837 shorts + 235
streams), @TheFuturAcademy 86 (catalog tier, P3), @ChrisDo 10. Priorities: 66 P1 /
1,069 P2 / 1,210 P3; dates+views backfilled for 1,072 @thefutur videos (105
unavailable/members-only), top-50 by views promoted to P1. Streams typed `stream`,
P3 long tail. Next: /loop /ingest-loop.

## [2026-07-17] lint | Persona pass — v1 compile

First `/ingest-loop` iteration → Stage P (first-run = persona treated as stale; product
was uncompiled). Delegated to one agent (single writer, persona-files-only). Compiled
persona **v1** from the two existing research dossiers (biography + media-inventory):
- `persona/beliefs.md`: 16 dated, cited beliefs (Frameworks/Values/Opinions) with
  self-reported/press-corroborated/registry-verified markers; critic "fraud" material
  fenced as third-party; pricing pushback flagged as external contradiction.
- `persona/voice.md`: 7 signature catchphrases as marked direct quotes; cadence/register
  limited to what's supportable, with a prominent flag that spoken-voice data is THIN
  pending transcript ingestion.
- `persona/system-prompt.md`: recompiled to **v1** (compiled_from_sources: 2) with
  first-person Persona prompt + grounding guardrails (Emmy≠Grammy; family names not
  public; $80M/Futur revenue self-reported; deflect where wiki is silent).
Gaps logged to wiki/gaps.md (spoken cadence, humor, tactical belief depth, appearance).
index.md persona lines updated. No wiki/topics or ledger changes (nothing ingested yet).

Synthesis notes: none (no new source material this iteration — persona built from
already-filed dossiers).
