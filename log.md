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

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P1 2015–2016 Skool-era

First video batch. 8 P1 long-form → L2 source pages (one subagent per video, strict
Chris-vs-Jose/guest attribution for the co-hosted Skool era). All had captions.
- Pricing & Estimating (2015-10-08) — ★L3-candidate; Chris-led worked bid build-up
  (artist rate→markup→producer→AD→overhead→20% profit), 30-quote pricing bank.
- Branding w/ Yo Santosa (2015-12-13) — ★L3-candidate; logo≠brand/Neumeier, "brand
  filter" method; guest Yo Santosa (Ferroconcrete) flagged as entity candidate.
- Typography & Art Direction (2016-07-08) — ★L3-candidate; craft + how-to-give-art-
  direction masterclass, 10 Chris quotes.
- First Design Portfolio (2015-07-10) — positioning/T-shaped/"no filler all killer".
- Storytelling 5 tips (2016-03-15) — solo Chris; McKee/Kindra Hall/Glebas scaffolding.
- What is UX / Site Audit (2015-08-12, 2015-08-22) — UX process largely Jose-led;
  Chris supplies client/design-craft judgment; captions garbled, some attribution: uncertain.
- Dynamic Compositions (2016-07-16) — taught by Matthew Encina, NOT Chris → recorded as
  context, excluded from persona voice (only 2 Chris intro lines).
Caption garbles noted on-page for names/numbers/typefaces (verify before persona promotion).

Synthesis notes: 3 ★L3-candidates pending promotion → pricing (worked bid build-up +
value-based pricing logic: "how much would you pay someone else to do it", "you cannot
charge the same amount you pay the person", client-power/underbidding psychology),
branding (logo≠brand, brand-filter method, speak-the-language-of-business, equity-for-
value), design-craft (typography contrast/figure-ground/proportion + empowering-feedback
art-direction method). New entity candidate: Yo Santosa. voice.md gains real spoken-voice
quotes (portfolio, pricing, branding, storytelling) — refresh at next synthesis/persona pass.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P1 2016–2017 Skool→Futur transition

Second video batch (16 L2 total). 8 P1 long-form → L2 pages, one subagent each, strict
attribution across the Skool→Futur handoff (Jose gone by late 2016; Futur instructors
Encina/Burns/Livsey now appear).
- ★ Pricing Design Work (2016-10-22) — foundational value-based pricing doctrine
  ("price the client not the job", risk-as-lever, anti-hourly symmetry, discovery "meta
  moment", double-keystone margin, subcontract-and-keep-the-spread); 28 Chris quotes.
- ★ Typography 10 rules (2016-11-06) — motion "type manual", Chris/Blind authored; note
  it's WRITTEN voice (no narration), not spoken cadence.
- ★ Logo Design "I Wish" (2016-11-08) — w/ Ben Burns (context); "the difference is
  confidence", symmetry-of-logic, luxury-vs-volume; 9 Chris quotes.
- ★ Origin story Pt.1 (2016-12-16) — primary autobiography, pre-design-school chapter
  (silkscreen shop, "tracer", Tombow-marker epiphany, junior-year art nudge); 13 quotes.
  Adds specifics beyond the dossier (proper nouns need spelling verification). Biography.
- Day in the Life — Matthew Encina (2017-03-31) — Chris essentially ABSENT; context page,
  0 persona quotes (correctly excluded).
- Portfolio & passion (2017-04-22) — CSUN classroom Q&A (instructor Dave Moon context);
  "three shows a pattern", don't fake passion; 10 Chris quotes.
- ★ Run A Creative Business w/ Melinda Livsey (2017-06-21) — Chris coaches Livsey
  (context); full new-business "kiss-off" script, money-has-no-power mindset (immigrant
  backstory + poker + secret backup plan), "raise the gate" positioning; 11 Chris quotes.
- ★ Sean Campbell "Young Gun" (2017-11-15) — interview (Campbell context); conceptual
  logo-critique method (combine two symbols; curved corners = "dull"; crown-from-knives),
  discipline/constraint reframe; 5 Chris quotes.
Caption garbles flagged on-page (typefaces, names like Cisco/Draplin, Cal State Northridge).

Synthesis notes: debt now 2 batches / checkpoint 10. Strong L3 pipeline building — PRICING
especially (2 landmark pricing videos: 2015-10-08 + 2016-10-22) is ready for a topics/pricing
promotion; also design-craft/typography, branding/logo+confidence, mindset/money +
origin-story→biography, sales/kiss-off script. New context figures: Ben Burns, Melinda
Livsey (already in futur-instructors entity), Sean Campbell, Dave Moon, Yo Santosa.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P1 2017–2018 mature Futur (pricing/negotiation)

Third video batch (24 L2 total). 8 P1 → L2, one subagent each, strict attribution.
Pricing/sales-heavy era; two craft videos turned out to be led by Futur instructors, two
were guest interviews.
- ★ Price Buyers / Low-Budget Role Play (2018-04-04) — near-complete price-buyer
  negotiation script (take-away open, anchor reset, cost-of-inaction, Jim Rohn
  proportionality, "insurance policy" reframe, graceful exit); 17 quotes. Chris voices
  the designer role (labeled).
- ★ Raise Prices Without Losing Clients (2018-08-27) — 9 reusable frameworks for raising
  rates; 17 quotes.
- ★ Negotiate a Lowball Offer (2018-10-17) — anchoring/re-anchoring, "start high, make
  them negotiate against themselves", "whoever says it first"; 13 quotes.
- ★ What Not To Do With A Design Layout (2017-12-04) — layout craft critique; Chris-led
  with new co-host Molly; 6 quotes.
- Present Logo Designs to Clients (2017-12-20) — presenter is BEN BURNS, not Chris →
  context page, 0 Chris quotes (only Chris's "scaffolding" concept cited secondhand).
- Simple Tips to Improve your Design (2018-08-01) — MATTHEW ENCINA solo → context page,
  0 Chris quotes.
- Will Paterson interview (2018-11-01) — guest origin story (context, firewalled);
  Chris's imposter-syndrome reframe + "clients seeking you out qualifies you"; 6 quotes.
- Joey Cofone / Baron Fig Pt.1 (2018-12-01) — guest bio (context, firewalled); Chris's
  risk/resilience + parenting-vs-comfort framing; 4 quotes. Part 2 is a later ledger item.

Synthesis notes: debt now 3 batches / checkpoint 10. SALES-CLIENTS is now richly sourced
(role-play script + lowball anchoring + price-buyer handling) and PRICING even more so
(raise-rates frameworks join the 2 earlier landmark pricing videos) — both ripe for
topics promotion at the checkpoint. New context figures to consider for entities: Ben
Burns (already in futur-instructors), Molly (co-host), Will Paterson, Joey Cofone/Baron Fig.
Reminder: two @thefutur "craft tutorial" P1s are actually Encina/Burns, not Chris — keep
attribution vigilant on craft titles.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P1 2019 (VBP, Building A Brand, AIGA keynote)

Fourth video batch (32 L2 total). 8 P1 → L2, one subagent each, strict attribution.
- ★ How To Charge For Design / Value-Based Pricing (2019-04-12) — canonical VBP method:
  backwards sequence (desired future state → metrics → value → price → scope), diagnose-
  don't-pitch, let-the-client-name-the-value, price anchoring, discount-for-uncertainty,
  single-page round-number bid; 27 Chris quotes. Credits Blair Enns (Pricing Creativity),
  Jim Rohn. Landmark pricing source.
- ★ What You Believe Becomes Reality — AIGA 2019 full keynote (2019-08-12) — landmark
  MINDSET talk: belief-cycle model, interpretation-between-input-and-output, reframing
  ("congratulations", impossible→I'm possible, "War Jitsu"), inner-critic 3-column
  exercise (from his own therapy + Firestone), "design your life", "failure is the tuition
  I pay for future success"; 35 quotes + autobiography ($30k loss lesson, tough-immigrant-
  dad upbringing, forged report card, therapy). PROMOTE into beliefs/voice/mindset.
- Building A Brand series Eps 1,2,3,4,6,7 (2019-05-22 → 2019-07-03) — documentary of a
  real Blind engagement for client HAMILTON FAMILY BREWERY (owners Josh & Kristen
  Hamilton). KEY FINDING: this series is led by Blind creative directors MATTHEW ENCINA
  and BEN BURNS, NOT Chris. Chris is essentially absent (Eps 1/2/3), brief at the end of
  Ep4 (5 quotes), off-camera/uncertain in Ep6, and only in Ep7's cold-open (1 quote).
  Filed as CONTEXT pages; team/client material walled off from persona.

> ⚠️ POLICY: the AIGA keynote names one of Chris's sons on-camera. Per SUBJECT.md's
> family-privacy rule (names = not-public), the name was REDACTED from the source page and
> a decision item was logged to wiki/gaps.md for the repo owner.

Synthesis notes: debt now 4 batches / checkpoint 10. Two more landmark L3 sources this
batch — PRICING (2019 VBP joins the earlier pricing landmarks — pricing is now very well
sourced) and MINDSET (AIGA keynote is the first deep mindset/self-belief source, prime for
beliefs.md + voice.md + topics/mindset). Building A Brand is process context, not persona.
New context entities to consider: Matthew Encina (Blind CD), Hamilton Family Brewery
(client). Data point for SUBJECT.md rules: @thefutur "Building A Brand"/documentary series
are largely team-led — attribution vigilance required (several P1s yield ~0 Chris voice).

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P1 2019–2022 (sales, mindset, content-strategy)

Fifth video batch (39 L2 total). 8 selected; 7 → L2 (yt-lzmE3mYrbL0 hit a transient
caption-fetch failure — left OPEN for retry next batch, NOT marked no-captions). High
persona yield; content-strategy (previously thin) now well sourced.
- ★ Price Too High Role-Play (2019-12-26) — two-play price-objection script (qualify-then-
  walk + risk-reversal anchor); co-host Mo; 20+ quotes.
- ★ How to Learn Anything (2020-06-09) — "Five Ingredients" deconstruction + learn-reflect-
  implement-share cycle; 15 quotes.
- ★ Use This Sales Technique (2020-08-19) — "Eight Mile Principle" (name the client's
  objection before they do); Better Call Saul examples quarantined as teaching aids; 13 quotes.
- ★ Reinvent Yourself (2021-03-16) — reinvention/origin-story keynote (OREO formula,
  obstacle-as-opportunity, 80/20 reinvention, "you are more than what you make"); 19 quotes
  + rich autobiography (career arc; The Futur founded after AIGA + Art Center rejected his
  online-ed pitch; "wife is also a designer" — no name).
- ★ Tell Your Story Pt.1 (2021-07-11) — personal-branding storytelling framework (Unbland
  thesis on-ramp); 13 quotes. Part 2 is a later ledger item.
- ★ 800K Instagram Organically (2022-04-20) — content-strategy organic-growth playbook
  (give-first/teach/carousels/consistency); 14 quotes; growth metrics self-reported.
- What Is Branding? (2019-12-31) — actually a MARTY NEUMEIER interview; the branding
  definition is Neumeier's (context, credit him), only 2 Chris quotes ("brand = reputation").

Synthesis notes: debt now 5 batches / checkpoint 10. Six more L3 landmarks. Domain coverage
now strong across pricing, sales-clients, mindset, and content-strategy — the next Stage S
checkpoint (at ~10 batches) should promote: pricing (VBP + estimating landmarks), sales-
clients (role-play/negotiation/objection scripts + Eight Mile Principle), mindset (AIGA +
Reinvent + Learn-Anything), content-strategy (tell-your-story + Instagram playbook). New
context/influence figures: Marty Neumeier (The Brand Gap — recurring influence), co-host
"Mo", Michael Janda. Attribution reminder: a "What Is Branding" explainer was actually a
guest interview — keep checking who actually delivers the content.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P1 2022–2023 (masterclasses + money/scaling)

Sixth video batch (46 L2 total; 8 selected, 1 skipped). Skipped yt-lzmE3mYrbL0 ("Design
From Scratch" documentary TRAILER — promo, no page). 7 → L2.
- 3 GUEST masterclasses, expertise firewalled as context (NOT persona): Brendan Kane
  (social media; 4 Chris quotes), Joana Galvao (lead-gen; 5 Chris quotes), Ron Baker
  (value pricing; 6 Chris quotes). NOTE the Baker episode: Chris explicitly credits
  **Ron Baker + Blair Enns** as the sources of his value-based pricing — a documented
  influence link to record in beliefs at synthesis.
- ★ How I Scaled My Creative Agency To $80M (2022-12-01) — "I do / We do / You do"
  delegation model + Blind biography; the $80M is **[self-reported]** (flagged everywhere);
  studio credit: main titles for *Dogtown and Z-Boys* (2001); 16 quotes.
- ★ 5 Books That Made Me A Millionaire (2022-12-15) — takeaways from Blair Enns (Win
  Without Pitching), Michael Bungay Stanier, Kevin Daley (Socratic Selling), Jim Rohn,
  Marty Neumeier (Brand Flip); 11 quotes.
- ★ 5 Money Rules (2022-12-27) — delegate / value-price / focus / have-the-money-
  conversation / invest-in-compoundable-skills; 14 quotes. Mentions Kyle Cooper, R/Greenberg,
  Alex Hormozi.
- ★ Attract Customers Like a Magnet — Masterclass 5/5 (2023-03-09) — CHRIS-taught (host =
  context); attraction/permission-marketing playbook (Seth Godin lineage) + biography
  (15 yrs teaching, designer→teacher identity shift); 14 quotes.

Synthesis notes: debt 6 batches / checkpoint 10. Four more Chris L3 landmarks (scaling,
books, money rules, attraction marketing) + a documented pricing INFLUENCE MAP (Ron Baker,
Blair Enns) and reading list (adds Michael Bungay Stanier, Kevin Daley, Jim Rohn to the
Neumeier link). New context/influence entities worth pages later: Ron Baker, Blair Enns,
Brendan Kane, Joana Galvao, Marty Neumeier (recurring). Wealth/money content mapped to
business+mindset (no 'wealth' folder in taxonomy) — flag for user if a wealth domain is
wanted. @thefutur guest "masterclass" titles are guest-led — attribution vigilance holds.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P1 2023–2024 (personal branding, pricing, selling)

Seventh video batch (54 L2 total). 8 P1 → L2. Exceptionally high persona yield — SEVEN
★L3-candidates. Personal-branding-heavy (aligns with the Unbland Yourself thesis).
- ★ AdobeMAX 2023 — Personal Branding keynote (2023-12-19) — the full personal-branding
  framework (four-part comic mythology, Persona vs Shadow, two-word brand, shadow-word +
  transformer, "make enemies", naming-to-own, EO 5% rule); 28 quotes + rich biography
  ("loud introvert", Draplin origin of his framework, Jose Caballer pushed him onto camera,
  "-do" naming + C-D-O monogram). UNBLAND-CORE.
- ★ Personal Brand Masterclass (2023-12-14) — Chris-taught workshop; two-word-brand
  exercise, shadow→transformer, "loud introvert" self-analysis; 29 quotes.
- ★ Branding for Non-Creatives keynote (2024-01-10) — branding fundamentals for business
  audiences; pricing-as-positioning; The Ugly Company case; 33 quotes + biography.
- ★ Selling Without Being Salesy (2023-12-23) — "serve-don't-sell" philosophy + SALES
  framework; 45 quotes.
- ★ Don't Justify Your Prices (2023-10-19) — have-to-have vs nice-to-have redesign +
  never-cede-the-higher-ground (symmetry of logic); 18 quotes.
- ★ Raising Rates $2k→$5k (2023-04-24) — raise-your-rate-to-raise-client-quality ladder;
  guest (DesignJoy, likely Brett Williams — uncertain) context; 6 Chris quotes.
- ★ The Secret To 'Great' Design (2023-06-14) — Chris-led critique; teaching philosophy,
  "do less but do better", bad-to-good gradient critique; 7 quotes.
- Powerful LinkedIn Presence (2023-12-30) — GUEST "Yasin / Hey J" (context, name uncertain);
  Chris reframes only; 4 Chris quotes; not L3.

Synthesis notes: debt 7 batches / checkpoint 10. HUGE branding/personal-branding L3 backlog
now (2 keynotes + masterclass — the Unbland thesis is well sourced) plus more pricing/sales
landmarks. Influence/entity notes: Aaron Draplin (origin of Chris's branding framework),
Alex Hormozi (recurring reference), Brett Williams/DesignJoy, Yasin/Hey J. @thefutur P1
nearly drained (8 left). Plan: 1 more @thefutur P1 batch drains the tier → then Stage S
synthesis checkpoint (promote the large ★L3 backlog into topics + persona) → Stage P.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P1 2024–2025 (biography, pricing, personal branding)

Eighth video batch (60 L2 total). 8 selected; 6 → L2; 2 transient caption-fetch failures
(yt-A9rAaBPE7e0, yt-jX6RuXhlnss) left OPEN for retry. 5 more ★L3-candidates.
- ★ Who Is Chris Do & The Futur? Origin Story (2024-02-24) — richest biography source yet
  (guest on Travis Makes Friends podcast, republished): Vietnam→Kansas City→San Jose,
  middle of 3 brothers, SD City College (mentor Candace Lopez)→Art Center, **Blind founded
  Dec 1995 on a $5,000 check, ~25 yrs, grossed $80M+** [self-reported], The Futur "$4–5M";
  35 quotes. Corroborates + enriches the bio dossier.
- ★ $500→$100k Logo Pricing Deep-Dive (2025-04-08) — charge-more evolution + full price-the-
  client method; 30 quotes. NOTE: the title figure is illustrative — the real narrated deal
  is ~$69k for an event-branding package, flagged on-page.
- ★ 0→5M Followers: 10 Personal Branding Rules (2025-05-31) — his personal-branding playbook
  + mission ("teach a billion", "private art school without the crippling debt"); ~40 quotes.
- ★ 10 Habits I Quit (Broke→Millionaire) (2025-03-11) — discipline/mindset; 24 quotes.
- ★ The Scene Every Salesman Needs to See (2025-11-25) — Better Call Saul positioning
  breakdown (create-the-customer / Blue Ocean); film dialogue quarantined; 7 quotes.
- From $13 to $100K Brand Deals w/ Adrian Per (2024-11-06) — GUEST @OMGAdrian (context,
  firewalled); 6 Chris quotes; not L3.

Synthesis notes: debt 8 batches / checkpoint 10. @thefutur P1 nearly drained (only the 2
retries remain). The biography L3 backlog is now large (origin stories 2016 Pt1 + 2019
Reinvent + 2024 Travis + AdobeMAX/Branding keynotes) and consistent — strong feed for a
biography.md v2 at synthesis. Pricing/sales/mindset/branding/content-strategy all deeply
sourced. NEXT: finish the 2 @thefutur retries + 2 @ChrisDo P1 rows (drains P1 entirely),
then run the STAGE S synthesis checkpoint (promote the ★L3 backlog into topics + persona)
and STAGE P persona refresh. Influence map to encode: Blair Enns, Ron Baker, Marty Neumeier,
Aaron Draplin, Jim Rohn, Seth Godin.

## [2026-07-17] lint | synthesis pass 1 — P1 tier complete (system-prompt v2)

First substantive synthesis checkpoint, triggered by the P1 landmark tier completing
(60 L2 source pages across 8 ingest batches; @thefutur 2014–2025 + @ChrisDo) and the
ingest crossing the P1→P2 era boundary. Delegated one agent per file (concurrency rule).

Built all 7 `wiki/topics/` hubs from empty stubs, framework-organized, every claim dated
and cited to its `wiki/sources/` page, quotes vs paraphrase kept, contradictions flagged:
- pricing (11 frameworks) · sales-clients (9) · branding (17, client + personal/Unbland) ·
  business (7) · content-strategy (10) · mindset (10) · design-craft (6).
Promoted persona product from pre-video stubs:
- beliefs.md: 16 → ~40 cited beliefs + a Documented-influences subsection; 3 position-
  changes flagged (pricing posture 2019→2023; selling→"content that sells for you"; the
  external "price the client" critique retained).
- voice.md → v2: ~55 Chris-attributed catchphrases + a real cadence/humor/register profile
  (Socratic, role-play/demo, aphoristic, provocative-but-warm, loud introvert). The v1
  "cadence data thin" caveat removed.
- biography.md: ~25 first-person facts folded into the timeline ($5,000 founding check,
  $80M+ cross-cited, refugee/family detail, Cole & Weber chapter, designer→teacher shift);
  5 contradictions flagged (1995 vs 1997 Blind incorporation; ~23 vs ~25 yrs; Emmy≠Grammy;
  son detail; Santa Monica vs Pasadena move). NO family names included (privacy rule held).
- system-prompt.md: recompiled v1 → **v2** (compiled_from_sources: 60); doctrines-by-name,
  voice, influences, and guardrails (family names, Emmy-not-Grammy, self-reported flags,
  Blind studio ≠ app, deflect-where-silent).
Fidelity wins: agents declined to fabricate brief-suggested phrases not found in sources
("facts tell stories sell", "do less but do better", "money has no power", crab-traps);
Ron Baker influence marked attribution: uncertain (dossier-only, not in the 11 video sources).

High-water mark advanced (pipeline/synthesis-state.md); checkpoint moved to Done. Appearance
still ungrounded (needs a watched-video sample — Phase 3 note). Persona mode (/chrisdo) now
loads a real v2 clone.

Synthesis notes: none (this IS the synthesis pass; debt drained for the P1 tier).

## [2026-07-17] ingest | yt batch (@thefutur 6 + @ChrisDo 1) — P1 stragglers + earliest P2 (2014 Skool era)

Ninth video batch (67 L2 total). Post-synthesis. **P1 tier now fully drained.**
- Marked 2 stuck @thefutur P1 rows SKIPPED (yt-A9rAaBPE7e0 "My Daily Routine", yt-jX6RuXhlnss
  "Forget Your Epic Origin Story") — captions failed 3x while peers fetched OK (video-specific
  no-captions, not global rate-limiting; never Whisper without approval).
- Ingested the 6 EARLIEST @thefutur videos (Aug–Sep 2014, "The Skool" launch, co-hosted with
  Jose Caballer) — these predate all prior sources and are the ORIGIN POINTS of his sales
  frameworks:
  - ★ Ask for the Sale Pt1 (origin of the qualification triad: like-you / can-do-the-work /
    can-afford-it) + ★ Pt2 (earliest role-play-a-sale format; Chris plays the tough client).
  - ★ Overcoming Objections (seed of price→value pivot, opportunity-cost reframe; 11 Chris quotes).
  - Get Clients/Lead-Gen (closing/pricing Chris, lead-gen Jose), Social Media for Designers
    (early positions, platform specifics dated), ★ Confidence/Culture/Money (early money-mindset
    root; guest Rocio Villalobos correctly kept separate from Chris's own refugee backstory).
- @ChrisDo channel: Blue Ocean Strategy (2026-06-11) — solo Chris applying Kim & Mauborgne
  (+ Christensen); credited, not originated; not L3.
Attribution discipline held throughout (Chris vs Jose vs guest; role-play roles labeled;
2 videos left `attribution: uncertain` lines out of persona voice).

Synthesis notes: debt 1 batch / checkpoint 10 (fresh count after pass 1). Several 2014 ★L3
"origin point" tags queued — at the next checkpoint, add an EARLY-ROOTS / evolution note to
topics/sales-clients (the qualification triad, role-play format, and objection→value pivot all
trace to Aug–Sep 2014). NEW context entity: Rocio Villalobos (2014 guest). Now entering the P2
long-tail (@thefutur ~1,059 P2 + 44 P3, + @TheFuturAcademy 72 P3 catalog-tier) — expect lower
per-video novelty; promote sparingly, synthesize every ~10 batches.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 early-2015 ("The Process" era)

Tenth video batch (75 L2 total). First P2 long-tail batch — early-2015 Skool→"The Process"
era, all co-hosted with Jose Caballer. 7 substantive L2 + 1 minimal context page. 2 ★L3.
- ★ Trojan Storage Branding Case Study (2015-03-24) — a full end-to-end client identity
  WORKFLOW not yet in the branding hub: CORE user-profiling, "mind-walking" empathy map,
  6-category brand definition (Neumeier), scaffolding (Holtzman), fit-check, stylescapes
  review, fun↔functional sweet-spot, "straight-line system" PM (Belfort); 12 Chris quotes.
- ★ How to Position a Brand (2015-04-28) — the "WIN" three-circle Venn (love / good-at /
  pays-well; pick one), match-and-mirror, "say it first"; credits Ries & Trout (*Positioning*)
  + Neumeier; 7 Chris quotes.
- 2 GUEST eps firewalled as context: Sue Parker (Frank Creative agency model — caught the
  "money is respect / walk away" maxim being HERS, not Chris's), Mark Fidelman (social media,
  early-2015 tactics). 
- 2 design critiques (Akin; Leigh O'Brien) — Chris's critique lens = persona; recurring
  portfolio/showreel principles (single-claim positioning, best-work-first, T-shaped,
  "no filler all killer"), not distinct enough for L3.
- Design for Startups — Jose-led (his teaching kept as context), Chris co-host.
- Multi-Camera Live Streaming Setup — technical AV tutorial, 0 Chris persona content →
  minimal context page (presenter unnamed; likely Chris but attribution: uncertain).

Synthesis notes: debt 2 batches / checkpoint 10. Two ★L3 to fold at the next checkpoint:
add the Trojan Storage OPERATIONAL client-branding workflow (CORE/stylescapes/scaffolding/
straight-line) to topics/branding (currently philosophy-only), and the WIN positioning Venn
to topics/branding + persona/beliefs. Data point: early "The Process" episodes are Jose-heavy
and guest-heavy — per-video Chris novelty is lower in P2; keep filtering, promote sparingly.
New context entities: Sue Parker, Mark Fidelman, Rocio (prev). Show naming history captured:
"The Skool Live" → "The Process" (rebrand noted early 2015).

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 mid-2015 ("The Process")

Eleventh video batch (83 L2 total). Mid-2015 P2 long-tail. 0 ★L3 (expected — restatements
of already-captured frameworks, or Jose/guest-led). All Chris material still captured as L2.
- W Hotel brand-messaging (solo Chris; brand experience > logo; 5 quotes), "Is Now a Good
  Time to Be a Designer?" (solo Chris AMA; 18 quotes; career/mindset restatement), "Advice
  for Young Designers" (artist-vs-designer, two-word brief filter; 15 quotes), 2 site
  critiques (ImThatDesigner, recurring principles).
- Jose-led (context, minimal Chris): UX Design 2 (user stories) + UX Design 3 (feature
  prioritization) — the UX series is Jose's methodology.
- Guest/context: "Unfiltered: Imin Pao" (guest monologue, no confirmable Chris speech →
  context page, 0 Chris quotes); "Profitable Small Business Ideas" (clickbait title; actually
  an AMA with Chris's business consultant KIER McLAREN — his teaching is context; 4 Chris
  quotes). Kier McLaren recurs (also cited in the 2023 Selling source) — candidate entity.

> ⚠️ FAMILY PRIVACY: the Kier McLaren AMA has Chris name his wife (his business partner).
> Name REDACTED from the source page per SUBJECT.md; recorded only as "his wife / business
> partner". (Second time a family name has surfaced on-camera — see the 2019 AIGA son-name
> redaction and the wiki/gaps.md policy question.)

Tooling note: added memory that `tools/ingest_batch.py` needs `PYTHONIOENCODING=utf-8` on this
Windows box — a `►` in a 2015 title crashed the cp1252 stdout; re-running with UTF-8 fixed it.

Self-reported datapoint surfaced: Blind revenue ~$2.4M (glass ceiling) → ~$4M in the first
year with consultant Kier McLaren [self-reported].

Synthesis notes: debt 3 batches / checkpoint 10. Nothing new to promote this batch (all
restatement or non-Chris). Carrying forward the 2 prior-batch ★L3 (Trojan Storage workflow,
WIN positioning Venn). New context entities: Kier McLaren (recurring consultant), Imin Pao,
Sue Parker, Mark Fidelman. Continue P2 drain.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 late-2015→early-2016 ("The Process")

Twelfth video batch (91 L2 total). 8 → L2. 3 ★L3 (richer than the last P2 batch — several
solo-Chris lectures).
- ★ The Client Is Not Your Enemy (2015-10-20) — solo Cal State LA lecture; distinct client-
  relationship frameworks: "let go of the artist persona", "happy ears" (active listening),
  "embrace and pivot / mental jujitsu", "ask why three times" (need vs want), "shut up when
  the client says yes" (Belfort); 17 quotes.
- ★ 3 Most Common Client Objections (2016-01-09) — the EARLIEST/fullest articulation of his
  "Embrace and Pivot" objection method (own → make them dig in → paint alternative undesirable
  → pivot), the rock-paper-scissor "middle player" model, and Blair-Enns retreat-and-follow.
  This PREDATES and underpins the later Eight Mile Principle (topics/sales-clients §5); 21 quotes.
- ★ Is Your Design Resume Still Relevant? (2015-11-29) — "resume is dead → show the work,
  self-position deliberately, direct outreach past HR gatekeepers, build mockups"; 7 quotes.
- How To Be A Great Facilitator (2016-01-23) — Chris-led (confirmed), 9 quotes; but the named
  CORE framework is JOSE's — Chris explicitly adapts/diverges (personas-first; keep the
  negatives). Documented divergence, not L3.
- 3 Tips to Start an Agency (2016-02-24) — market-one-thing / branding-umbrella / make-vs-
  manage; 7 quotes.
- Context/low-value: UX3 pt2 (Jose-led), Books to Learn UX (not Chris on camera), Vlog Travel
  Camera Setup (gear tutorial, minimal context page, 0 Chris).

Synthesis notes: debt 4 batches / checkpoint 10. Growing ★L3 backlog for the NEXT checkpoint,
esp. SALES-CLIENTS evolution: the Embrace-and-Pivot method (2016-01-09) is the documented ROOT
of the objection-handling frameworks already in the hub — add an "origins/evolution" note.
Also client-relationship ("happy ears", ask-why-3x, shut-up-when-yes) and career-positioning
("resume is dead", direct outreach) are promotable. Carrying: Trojan Storage workflow + WIN
Venn (prev batch). Documented framework-attribution nuance: CORE = Jose's, Chris adapts it.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 spring-2016 ("The Process")

Thirteenth video batch (99 L2 total). 8 → L2. 4 ★L3.
- ★ Client Red Flags & Warning Signs (2016-03-08) — a named taxonomy of good vs bad client
  archetypes (Squirrel/Trump/micromanager/blamer... vs Zen-CEO/trust-the-expert/servant-leader)
  + gut-instinct screen + "resentment = underpricing → charge more"; 14 quotes.
- ★ Break Out of Your Comfort Zone (2016-03-23) — solo vlog; integrity credo ("all I have is
  my balls and my word") + rocket/escape-velocity momentum metaphor + serendipity story; 8 quotes.
- ★ Stay Motivated + Clients With Bad Taste (2016-04-01) — bad-taste-client MOVE: reframe taste
  as subjective → replace with client-agreed OBJECTIVE measures (deadline/budget/message/audience)
  → diagnose WITH the client → refund-and-refer if misaligned; + Blair Enns "diagnose before
  prescribing"; 14 quotes.
- ★ Big Client Meeting: Sell Large Digital Projects (2016-04-30) — role-play; big-meeting selling
  framework (listen+write, elicit each stakeholder's top-3 objections, mirror-to-validate, split
  problem from scope/cost, land paid discovery, clean walk-away); 9 quotes.
- Context/guest: Karen McGrane (UX content-strategy guest; Chris hosts; 3 Chris quotes), CRO
  Funnel (guest Alan Martinez/Noble Digital-led; 3 Chris quotes), Am I An Entrepreneur (guest-
  founder interview). Get a Design Job in LA (18 quotes but overlaps existing hiring/career).

Synthesis notes: debt 5 batches / checkpoint 10 (halfway). ★L3 backlog for the next checkpoint
keeps growing on SALES-CLIENTS especially — this batch adds client-SCREENING (red-flag archetypes,
resentment=underpricing), the bad-taste-client objective-measures move, and the big-client-meeting
framework; MINDSET gains the integrity credo + escape-velocity. Combined with the prior batches'
Embrace-and-Pivot, happy-ears, Trojan Storage workflow, and WIN Venn, the next Stage S should
meaningfully deepen topics/sales-clients + topics/mindset + topics/branding. New context entities:
Karen McGrane, Alan Martinez (Noble Digital). Continue P2.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 mid-2016 (design-education cluster)

Fourteenth video batch (106 L2 total). 8 selected; 7 → L2 (yt-d77cDtH8bo0 "Web Design Review"
transient caption fail, left OPEN). High yield — 6 ★L3, incl. a coherent DESIGN-EDUCATION cluster.
- ★ Rethinking Design Education (2016-06-30) — the GERM of The Futur's mission: quarter-million
  student-debt critique, "teach them not to be makers" (business of design > craft), offshoring/
  value-collapse, better creative education as a "moral obligation", Lynda Weinman After-Effects
  origin. Biography anchors [self-reported] (kids aged 12 & 10 in 2016 — no names). 11 quotes.
- ★ What to Learn in Design School (2016-06-28) — self-directed learning; deliberate discomfort as
  the marker of growth; 6 quotes.
- ★ Be a Happier, Better Designer (2016-06-16) — success=personal-growth (not vision-match);
  "absent a narrative, people invent one"; "hands up, no excuses" apology framework; 15 quotes.
  (Credits business-coach Kier for "all companies are customer-service companies".)
- ★ Where Do Good Ideas Come From? (2016-06-21) — creativity/originality: "everything is a remix",
  copy-transform-combine (cites Kirby Ferguson), "I'd ban the word plagiarism", master-copy
  pedagogy; 12 quotes.
- ★ Freelance Tips — Motion Design LA (2016-07-13) — freelance-negotiation framework: hold/book/
  challenge, "put yourself on hold first", rate-anchoring, cancellation clauses, bring-conflict-
  upfront; 18 quotes.
- ★ How to Write Content for Web (2016-08-11) — Chris coaches copywriter Janica; AIDA-for-web-
  headlines + "bridge the gap" positioning + "explain it to a fifth grader"; 10 quotes.
- Get Hired 2016 — overlaps existing hiring coverage; 3 quotes; not L3.

Synthesis notes: debt 6 batches / checkpoint 10. Growing multi-domain ★L3 backlog. This batch adds
a DESIGN-EDUCATION theme (not yet its own hub — the taxonomy has design-craft + business + mindset;
the education-reform thesis spans all three and is the ideological ROOT of The Futur — fold into
biography + business/mission + a design-craft "teaching philosophy" section at the next Stage S).
Also: freelance-negotiation (business), creativity/remix (design-craft/mindset), web-copywriting
(content-strategy). New biography anchors + the "moral obligation" education thesis are strong
persona/biography material. Context entities: Karen McGrane, Alan Martinez, Petrula Vrontikis &
Alison Goodman (Art Center faculty, 2016 panel). Continue P2.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 late-2016 (values + web-craft)

Fifteenth video batch (113 L2 total). 8 selected; 7 → L2 (yt-eN-Tti_iqwM "Responsive Web
Design" transient caption fail, left OPEN). 2 ★L3.
- ★ Integrity vs Profitability pt.1/3 (2016-08-25) — VALUES + negotiation: kill-the-engagement-
  3x (credits Blair Enns), first-minutes leverage, "the more I say no the more they say yes",
  Wonderbread-leverage rule, spec-work/RFP philosophy, no granular bidding; 11 quotes. (Guests
  Michael Stinson/Rachel Elnar TypeEd = context.) Note: Parts 2-3 are later ledger items.
- ★ Web Design Review pt.2 (2016-09-20) — process principles: the designer→developer HANDOFF
  rule (don't edit their CSS; screencap + annotate + let the dev own the code) and a first-pass
  review posture; 7 quotes.
- Web Design Review (2016-07-23) & Website from Wireframes (2016-08-14) — Chris-led craft
  reviews of Blind's own work (context: designers Jamie Van Wart, Charlene Chen); conventional
  web-craft, not L3. Marketing/Social Tips pt.3/3 — panel; standard content-strategy.
- Context/NOT-Chris: Gemma O'Brien lettering workshop (100% guest, Chris absent); "3 Things To
  Do Before You Design" — taught by MATTHEW ENCINA, not Chris (attribution catch — the title
  looked Chris-ish but it's Encina's pre-design/discovery framework). Both context-only pages.

Synthesis notes: debt 7 batches / checkpoint 10 (approaching). ★L3 to fold: integrity/values +
negotiation (kill-engagement-3x, first-minutes leverage, spec-work stance) into topics/sales-
clients + persona/beliefs; the designer→dev handoff + first-pass posture into design-craft. This
"Integrity vs Profitability" is a 3-part series — Parts 2/3 will surface later; cross-link. Repeated
lesson: @thefutur design videos are frequently instructor-led (Encina) or guest workshops (Gemma
O'Brien) — attribution vigilance holds. New context entities: Gemma O'Brien, TypeEd (Michael
Stinson/Rachel Elnar). Continue P2.
