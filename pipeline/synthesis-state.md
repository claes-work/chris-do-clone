# Synthesis state

_Tracks the synthesis **high-water mark** so the synthesis loop never misses material and never
re-does work. Companion to the ingest ledger (`ledger.csv`). The detailed debt lives in `log.md`
as `Synthesis notes:` lines (every ingest batch appends one). See `tools/SYNTHESIS.md` for the loop
and `tools/synthesis_batch.py` for the driver._

## High-water mark
Synthesized through: **P2 long-tail through ingest batch 27 (L2=207) — all L2 source pages 2014–2017 (mid/late-2017 @thefutur P2 era).** Synthesis pass 3 ran 2026-07-17 → system-prompt v4.

## Pending checkpoints
_(oldest first; the synthesis loop drains these top-down)_

_(none — caught up through batch 27. Next checkpoint: after ~10 more ingest batches or an era boundary.)_

## Done checkpoints

- [x] **2026-07-17 · pass 3 · system-prompt v4** — P2 long-tail 2017 mid/late era (batches 18–27, ~78 L2 pages, L2 129→207). ENRICHED all 7 topic hubs: pricing 11→15 (price-bracketing, confirm-before-propose, too-expensive playbook, logo-pricing); sales-clients 14→18 (first-call doctrine, introvert/ambassador BD, Pitch This! presenting doctrine, show-up-empty presence); design-craft 11→16 (logo ideation, turn-off-layers critique, art-of-search, anti-originality/timeless, restraint/logo-is-tip-of-beast); mindset 13→21 (confidence/ego, introvert power, public-commitment ladder, too-dumb-to-fail, goal-setting/overwhelm/motivation, self-confidence-vs-self-esteem); content-strategy 13→16 (awareness funnel, Behance lead-gen, show-your-work); branding 23→25 (logo-is-tip-of-beast, restraint=timelessness); business 12→13 (sell-through-curiosity + take-care-of-your-people). Persona: beliefs ~41→~62, voice +16 catchphrases (typography + design-philosophy + presenting + mindset), biography +12 facts (burnout→teaching/Futur origin mythology, ~1995 start, INTJ→ENTJ, childhood conditioning). system-prompt v3→v4 (compiled_from 129→207). Contradictions flagged: pricing 2017-discount vs 2023-no-discount; content 2017-quality-over-frequency vs 2022-consistency; mindset too-dumb-to-fail vs disprove-your-ideas; design judge-mark-alone vs judge-system. Family names kept out; military/two-Emmys claims withheld per gaps.md.
- [x] **2026-07-17 · pass 2 · system-prompt v3** — P2 era 2014–2017 (batches 9–17, ~69 L2 pages). ENRICHED all 6 active topic hubs (sales-clients +5 sections incl. Embrace-and-Pivot/big-meeting/negotiation; business +5 incl. culture/education-mission/bid-model; mindset +4 incl. self-doubt/integrity/growth; design-craft +5 incl. remix/handoff/freelance/teaching; branding +6 incl. Trojan Storage workflow + WIN Venn; content-strategy +3 incl. web-copy/lead-gen/resume-is-dead). Persona: beliefs 40→~57, voice v2→v3 (self-aware traits + 6 catchphrases), biography +8 facts (Coldplay 'Ink', Second Shift, education-reform, Lynda Weinman), appearance.md SEEDED (empty→15 cited facts). system-prompt v2→v3. Family names kept out; watched-video visual sample still a gap.
- [x] **2026-07-17 · pass 1 · system-prompt v2** — P1 tier (60 L2 pages, 8 batches). Built all 7 `wiki/topics/` hubs from empty stubs (pricing 11 frameworks, sales-clients 9, branding 17, business 7, content-strategy 10, mindset 10, design-craft 6); lifted `persona/beliefs.md` (16→~40 cited beliefs), `persona/voice.md` (v2, ~55 catchphrases + real cadence), `persona/biography.md` (~25 facts folded in, 5 contradictions flagged); recompiled `persona/system-prompt.md` v1→v2. Family names kept out throughout.
