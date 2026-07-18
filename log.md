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

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 late-2016 (business + education thesis)

Sixteenth video batch (121 L2 total). 8 → L2. 6 ★L3 — a strong business/leadership + education run.
- ★ 3 Keys To Run A Design Business pt.1 (2016-10-11) — inverted success principles (moderation→
  intensity, patience→urgency, humility→self-love) + scaffolded referral-ask/reciprocity script; 12 quotes.
- ★ SEO & Lead Generation pt.2 (2016-10-19) — "when you do the talking you're selling; when they say
  it you're closing", educe/educate, warm-vs-cold leads, "market to marketers", alt-comp (equity/rev-
  share); 18 quotes.
- ★ Design→Business Transition (2016-10-28) — "sell what the world can do, not what you can do";
  entrepreneur vs "want-to-preneur" (Cuban); runway/"worry-date" cash-flow tool (Mike Janda, renamed);
  self-reported Blind numbers ($200k/mo burn, $600k LOC); 12 quotes.
- ★ Create a Creative Culture (2016-11-03) — values-based hire AND fire (Zappos), autonomy-mastery-
  purpose (Pink), low-cost culture tactics, "never fire for a first mistake"; 8 quotes. NEW venture
  surfaced: "Second Shift" consulting w/ Kier McLaren.
- ★ Logo Design Pt.2 (2016-11-12) — $5k-logo client-empathy framework, double-the-price/push-the-
  ceiling, three-things-every-business-needs, "you are good enough"; Ben Burns = context; 6 quotes.
- ★ Should You Go To Design School? (2016-12-06) — cost-vs-value math, "degree is a myth", pay-to-
  apprentice, flipped classroom; the clearest early seed of the Futur "private art school without the
  crippling debt" mission (cross-links 2016-06-30); 11 quotes.
- How to Be More Relatable? (2016-11-19) — Jose coaches Chris (Jose = context); NOT L3, but surfaced
  RICH self-aware persona traits for voice/appearance: relatability-as-acknowledged-weakness, "social
  wallflower" (jaw tenses, checks out at parties), people-pleasing/middle-child, self-frames as
  "logical/robotic" vs Jose's "spiritual", demands concrete-over-"woo". 10 Chris quotes.
- Responsive Web Design (2016-10-01) — Chris moderates a team-led technical walkthrough; not L3.

Synthesis notes: debt 8 batches / checkpoint 10 (checkpoint is 2 batches out — will run Stage S soon).
Big multi-domain ★L3 backlog. NEW for the next Stage P/persona pass: the relatability video's self-aware
traits materially deepen persona/voice.md ("loud introvert" → wallflower/logical-robotic/people-pleaser)
and give the first real persona/appearance.md-adjacent behavioral notes. Also: the education-reform thesis
now has THREE strong sources (2016-06-30, 2016-12-06, + Reinvent 2021) → promote a "design education /
The Futur mission" thread into persona/biography + topics/business. New entities: "Second Shift" (Chris+
Kier McLaren venture). Continue P2 — one more batch, then Stage S checkpoint.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 early-2017 (mindset + education)

Seventeenth video batch (129 L2 total; P2 now <1000). 8 → L2. 4 ★L3 + 2 minimal context + 1 portfolio-context.
- ★ Overcome Self Doubt (2016-12-24) — "hijack your mentors" (Beirut), Kanye reality-distortion
  self-belief, explorer-vs-GPS metaphor, a "dark night of the soul" autobiographical arc; 12 quotes.
  [self-reported: parents cut him off, ~21-year marriage — family kept unnamed].
- ★ Overcome Your Fears (2017-01-05) — "I copy and I steal relentlessly", "I just sucked less",
  growth-as-success; MORE self-aware persona traits: former severe social/public-speaking terror
  overcome only ~2 yrs prior, learns by MODELING (Louis CK for cadence), self-frames as analytical
  "robot" who deconstructs in layers, storyboard-only slides; 11 quotes.
- ★ 101 Things I Learned in Business School — Review (2017-01-30) — his layered bid model
  (COGS→overhead→profit→value-to-client); recurring signatures ("amateurs give advice, experts
  diagnose"; "not making a decision is a decision"); 15 quotes.
- ★ What Lies Were You Told in Design School? (2017-02-15) — degree-skepticism, practice-over-
  credentials, "amount of education ≠ value you get", his stuck adjunct title as evidence; a 4th
  strong education-reform source (host Petrula Vrontikis takes the pro-degree devil's-advocate =
  context); 12 quotes.
- Coldplay 'Ink' Making-Of (2017-01-08) — Blind's interactive branching music video (Post-It →
  story-matrix; 2D/3D/cel); narrator can't be confirmed as Chris → context page, but a real BLIND
  PORTFOLIO/biography fact (the "Ink" interactive video, publicly ~2014).
- Live Design Critique (2017-02-03) — 11 quotes, portfolio-presentation reinforcement; not L3.
- Typography-Cover Speed Design Pt.1 & Pt.2 (2017-02-12/17) — no narration → minimal context pages.

Synthesis notes: debt 9 batches / checkpoint 10 — NEXT ITERATION IS THE STAGE S CHECKPOINT.
Very large ★L3 backlog accumulated since pass 1 (~30+ across sales-clients, business, mindset,
design-craft, content-strategy, branding). Priorities to promote at Stage S: (1) SELF-AWARE PERSONA
TRAITS from the fears/relatability videos → materially upgrade persona/voice.md + seed persona/
appearance.md (former public-speaking terror, introvert/wallflower, learns-by-modeling, analytical-
"robot", storyboard-only slides); (2) EDUCATION-REFORM thesis (4 sources: 2016-06-30, 2016-12-06,
2017-02-15, + 2021 Reinvent) → persona/biography + topics/business mission; (3) the many sales/
business frameworks (Embrace-and-Pivot origin, client red-flags, big-meeting, integrity/negotiation,
3-keys, transition/runway, creative-culture) → topics/sales-clients + topics/business; (4) branding
(Trojan Storage workflow, WIN Venn); (5) new biography facts (Blind Coldplay 'Ink' credit, "Second
Shift" venture w/ Kier McLaren, $80M etc.). Next iteration: run Stage S, then resume P2.

## [2026-07-17] lint | synthesis pass 2 — P2 era 2014–2017 (system-prompt v3)

Second synthesis checkpoint (triggered at ~9 batches / ~69 L2 pages accumulated since pass 1;
the 2014–2017 "Skool → The Process" era). Delegated one agent per file (concurrency rule).
ENRICHED the existing hubs (did NOT rebuild) and lifted the persona product to v3.

Topic hubs enriched (new sections, all dated + cited, contradictions flagged):
- sales-clients (+5 sections / ~10 frameworks): qualification triad (2014), **Embrace-and-Pivot**
  method (+ rock-paper-scissor + retreat-and-follow; lineage 2014 seed → 2016 method → 2020
  Eight Mile), big-client-meeting (elicit each stakeholder's top-3 objections, paid discovery),
  "don't want the work" negotiation leverage / kill-the-engagement-3x, educe-don't-educate,
  client-archetype screen + bad-taste objective-measures + alternative compensation.
- business (+5 sections / ~22 frameworks): go-to-market & the-numbers (want-to-preneur, runway/
  worry-date), creative-culture (hire AND fire on values; Second Shift venture), the education-
  reform MISSION (root of The Futur), success-principles + referral ask, layered bid model.
- mindset (+4 sections / ~16): learning philosophy, momentum/integrity credo, success=growth,
  overcome self-doubt/fear (hijack-mentors, reality-distortion, "I just sucked less").
- design-craft (+5 sections / ~18): creativity-remix, copywriting, designer→dev handoff,
  teaching/education (craft angle), freelance working terms.
- branding (+6 frameworks): the Blind client-engagement WORKFLOW (CORE/mind-walking/6-category/
  scaffolding/stylescapes/straight-line) + WIN positioning Venn + brand-messaging.
- content-strategy (+3 sections / ~7): web-copy (AIDA/bridge-the-gap), content-as-lead-gen,
  "resume is dead → show work".
Persona:
- beliefs.md: ~40 → ~57 cited beliefs (integrity/values, education-reform, culture, self-belief);
  influences expanded (Mike Janda, Zappos/Hsieh, Daniel Pink, Michael Beirut, Kier McLaren).
- voice.md → v3: +6 catchphrases ("I copy and steal relentlessly", "I just sucked less",
  "amateurs give advice experts diagnose", "not making a decision is a decision"...) + deep
  self-awareness (overcame severe public-speaking terror; learns by MODELING; "logical/robotic"
  deconstructor; social wallflower). sources 13→18.
- appearance.md: SEEDED from empty stub → 15 cited self-reported facts (bald; hats + bold
  eyewear identity system; calm measured on-camera; storyboard-only slides). Watched-video
  visual sample still flagged as a GAP.
- biography.md: +~8 facts (Lynda Weinman After-Effects origin; parents-cut-him-off; Blind scale
  numbers [self-reported]; Second Shift venture; Coldplay 'Ink' interactive video ~2014;
  education-reform thesis; ~21-yr marriage; overcame anxiety ~2015). sources 9→17. NO family names.
- system-prompt.md: v2 → **v3** (compiled_from_sources: 129); added voice depth, appearance cues,
  and the new doctrines by name; guardrails intact (family names, Emmy≠Grammy, self-reported flags).

High-water mark advanced (through batch 17, L2=129); checkpoint → Done. index.md hub counts +
persona lines updated. Persona mode (/chrisdo) now loads v3.

Synthesis notes: none (this IS the synthesis pass; 2014–2017 P2 debt drained).

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 early-2017 (low-yield: tours/tutorials/guests)

Eighteenth video batch (137 L2 total). Low-persona-value cluster, as expected in the P2 tail. 1 ★L3.
- ★ Kyle Cooper interview PT1 (2017-03-29) — guest = KYLE COOPER (legendary main-title designer,
  Se7en; a documented Chris INFLUENCE who gave him his first title gigs — Island of Dr. Moreau,
  Celtic Pride). Kyle's craft/career = context (firewalled from Chris's bio). Chris's own reusable
  contributions: "going past the sale" vs "stop at yes", decision-maker-vs-order-taker, go-all-in-
  on-strengths; 6 Chris quotes. **Kyle Cooper is an ENTITY candidate** (wiki/entities/). PT2 exists.
- Blind/Futur Studio Tour (2017-02-17) — Chris-narrated; moderate value: "author not maker" media
  thesis, get-out-of-their-way management, 5pm no-work ritual; 8 quotes. ⚠️ CONTRADICTION: he says
  "two Emmys" here — conflicts with the registry-verified SINGLE Emmy (Heart of Stone 2010). Recorded
  as [self-reported]; flag for lint/biography (do NOT propagate "two" as fact).
- Legally Speaking PT1 & PT2 (Stuart Carroll, attorney) — guest LEGAL expertise = context, NOT
  encoded as Chris's knowledge or as legal advice; only Chris's business-realist framing kept
  (6+6 quotes). Stuart Carroll = minor entity candidate.
- Context/NOT-Chris (0 persona quotes → context pages): Book-Cover Speed Design (no narration),
  Double-Exposure Photoshop tutorial (Matthew Encina), Stop-Motion On-Set (Blind crew), Ayzenberg
  Studio Tour (Chris host-only).

Synthesis notes: debt 1 batch / checkpoint 10 (fresh after pass 2). Little to promote (mostly context).
For NEXT checkpoint: Kyle Cooper's "going past the sale / stop at sale-vs-yes" nuance for sales-clients;
create wiki/entities pages for Kyle Cooper (influence — first title gigs) and maybe Stuart Carroll
(legal). LINT ITEM: reconcile the self-reported "two Emmys" (2017 studio tour) vs registry single
Emmy — biography/system-prompt must keep "an Emmy" (Emmy≠Grammy guardrail already holds). Continue P2.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 spring-2017 (brand/strategy/discovery)

Nineteenth video batch (145 L2 total). 4 ★L3.
- ★ Designing for Business Goals + Client Empathy (2017-04-28) — design-as-business discovery
  pipeline (process → 3 business goals: revenue/repositioning/awareness → competitive audit
  vertical+horizontal → real customer feedback) + empathy-as-FIDUCIARY (the "Sam" refer-away
  parable; shoulder-to-shoulder vs face-to-face selling); 17 quotes. (Co-host Dave Moon context.)
- ★ Beliefs & Behavior Define Your Personal Brand (2017-04-25) — beliefs/behavior → brand;
  "think-say-do harmony"; "we trust people who believe what we believe" (Sinek); "gut feeling"
  (Neumeier, unnamed); Unbland-thesis material; 8 quotes. (Co-host Dave, context.)
- ★ Is Strategy for Creatives Who Can't Design? Pt.1/3 (2017-05-02) — "strategy supports the
  design, not vice versa"; can't-remove-it-or-you-make-shiny-objects; Tada!→of-course reveal
  (Blair Enns); load-bearing for Blind's brand-strategy pivot; 8 quotes. (Debate opponent Mark Posh
  + Jose clip = context.)
- ★ The Importance of Keeping a Journal (2017-04-21) — 21-day single-habit tracking pledge +
  weekly accountability ("Peak Performance") partner (Darren Hardy, The Compound Effect); 6 quotes.
- Kyle Cooper interview PT2 (2017-04-10) — Kyle=context; BIOGRAPHY anchor confirmed: Chris
  freelanced for Kyle Cooper as a young designer, Blind was ~1 yr old, Kyle tried to absorb Blind
  into Imaginary Forces (Chris joked "a million dollars"). 4 Chris quotes; not L3.
- Bad-Taste-in-1-min (2017-03-29) — near-verbatim clip of 2016-04-01; dup-ish. SEO Pro-Call
  (William Walczak/Hiilite, guest context; recorded Oct-2016). Golden-ratio Illustrator tutorial
  (no transcript → context).

Synthesis notes: debt 2 batches / checkpoint 10. ★L3 to fold next checkpoint: design-as-business
DISCOVERY + empathy-as-fiduciary → sales-clients/business; beliefs→brand + think-say-do → branding
(Unbland); strategy-supports-design → business/branding; 21-day-habit pledge → mindset. BIOGRAPHY:
add the Kyle Cooper mentor/freelance relationship (already in dossier as R/GA gigs — now first-person
corroborated) + create wiki/entities/kyle-cooper (influence). Data point: Futur Pro-Call publish
dates can lag recording by months (this one recorded Oct-2016, published Apr-2017) — date opinions to
the RECORDING when stated. Continue P2.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 May-2017 (strategy series + failure postmortem)

Twentieth video batch (153 L2 total). 5 ★L3.
- ★ Strategy debate Pt.2 (2017-05-03) + ★ Pt.3 conclusion (2017-05-05) — complete the "Hope or Hype"
  strategy series (Pt1 was 2017-05-02): symptoms-vs-root-cause, "common language of business",
  autonomy→creative-control (Pink), "design is the APPLICATION of strategy / a byproduct not the
  product", + the Pt3 origin story of Blind's post-2008 decline & brand-strategy pivot, the five
  collaboration rules, three golden questions, "ask why three times", and the "inverse bell curve /
  decline of the middle-class designer". 7 + 12 quotes. (Opponent Mark Posh + panel = context.)
- ★ What Does It Mean To Be Passionate? (2017-05-15) — passion = the visible VOLUME/DEPTH of
  exploration ("55 versions in 90 minutes"); Art Center intense-competitor origin; 5 quotes.
- ★ Never Too Late To Get Started In Design (2017-05-20) — age/life-experience as a design ASSET;
  "class is a job interview / professors are references"; serve-the-brief; 7 quotes. (Reviewee Evan,
  43-yr career-changer, = context.)
- ★ How to Deal with Defeat — Losing a $1M Job Pt.1 (2017-05-23) — candid Blind proposal postmortem:
  metabolizing defeat, the "what we did right" after-action checklist, pitching lessons; 14 quotes.
  Self-reported figures ($1M project, ~$900k award, $5M annual goal, ~20% of year's billings).
  ⚠️ NEW self-reported claim: a MILITARY/ARMY background (Army "after-action review"). NOT in the
  biography dossier; source is attribution:uncertain. Logged to wiki/gaps.md as a VERIFY item — do
  NOT propagate "Army service" as biographical fact (may be a borrowed AAR concept, not personal service).
- Context/NOT-Chris: Yo Santosa AIGA solo talk (Chris audience only, 0 quotes; Yo entity candidate),
  2 Nils Lindstrom typography sessions (guest instructor, Chris absent; Nils entity candidate).

Synthesis notes: debt 3 batches / checkpoint 10. Strategy series (3 parts) is a strong strategy/
business-of-design promotion cluster for the next checkpoint; also passion + never-too-late + the
failure-postmortem for mindset. NEW entity candidates: Nils Lindstrom (Art Center type prof), Yo
Santosa (recurring). VERIFY items carried in gaps.md: "Army background" and "two Emmys". Continue P2.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 late-May/June-2017 (defeat series + closing)

Twenty-first video batch (161 L2 total). 6 ★L3. Completes the 4-part "Dealing with Defeat" postmortem.
- ★ "Dealing with Defeat" postmortem Pt.2/3/4 (2017-05-27/29, 06-13) — completes the candid lost-$1M
  proposal series (Pt.1 = 2017-05-23): Pt2 "call the domain experts" winning formula + throw-yourself-
  on-the-sword + experts-ask-great-questions (11q); Pt3 "executive producer" mental model + "you must
  ask or you will fail" + trust-experts (10q); Pt4 conclusion "surface the unspoken objections" +
  diagnose-don't-prescribe + be-the-least-risky-option (8q). Rich sales/pitching/failure-handling.
- ★ Stop Selling. Start Closing. (2017-06-09) — "Whisper vs Scream" + consultative diagnostic closing;
  "when you say it you're selling, when they say it you're closing"; Blair Enns Win Without Pitching; 17q.
- ★ NAB 2017 keynote — Tell Your Brand Story (2017-05-25) — differentiate via story; shoemaker's-kids
  trap; Significant Objects 30× value experiment; 4 quotes.
- ★ Designer as Entrepreneur (2017-05-31) — go-beyond-aesthetics; Shark-Tank pitch-structure critique; 7q.
- Context: 2 Photoshop tutorials (Chris narrates but pure technique → 0 persona quotes, context pages).

Synthesis notes: debt 4 batches / checkpoint 10. STRONG sales-clients cluster for the next checkpoint:
the whole Defeat 4-parter (pitching/failure lessons: call-the-experts, executive-producer, must-ask,
surface-unspoken-objections, diagnose-don't-prescribe, least-risky-option) + Stop-Selling "Whisper vs
Scream" — these deepen topics/sales-clients materially. Plus NAB brand-storytelling → branding/content,
designer-as-entrepreneur → business. Note: even Chris-narrated Photoshop technique tutorials yield ~0
persona value (procedural) — correctly context. Continue P2.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 June/July-2017 (empathy, pitching, pricing)

Twenty-second video batch (168 L2 total). 8 selected; 7 → L2 (yt-1zLtfzsaP58 "Goal Setting" transient
caption fail, left OPEN). 5 ★L3.
- ★ How To Charge More For A Logo — Deep Dive ep.4 (2017-07-10) — dense value-based logo-pricing
  playbook (strategy-deconstruction "you can't see strategy", presentation-as-laziness, least-risky-
  option/zebra-vs-antelope, Paul Rand "don't try to be original / buy history", double-your-rate,
  Embrace-and-Pivot, BMW-tribe & jewelry storytelling scripts, "ledger of the mind"); real anchor $18k;
  24 quotes. (Melinda Livsey foil = context.)
- ★ Overcome Fears & Start Posting (2017-07-07) — detachment-from-work, give-value, fact-vs-opinion
  critique filter, anti-originality/anti-ownership, per-platform strategy; 17 quotes. MORE self-aware
  persona traits for voice: self-names his persona "the angry Asian guy" (angry-tone delivery), limited
  comfort WRITING in English (engineers the typeset-image hack for Twitter), calls his own content
  "regurgitated", will "firebomb back" at critics (combativeness). (Melinda = context.)
- ★ Can You Charge To Diagnose (2017-06-28) — paid-discovery framework: come-in-empty, Embrace-and-Pivot,
  be-prepared-to-recommend-a-solution-that-is-not-you (referral posture), mechanic-diagnostic template;
  8 quotes. (Blair Enns credited; Melinda context.)
- ★ Win More Clients — Empathy to Earn Trust (2017-06-14) — the haircut analogy (clients can't articulate
  needs), start-empty-and-listen, fit-assessment; 6 quotes.
- ★ How Pitching Works With Ad Agencies (2017-06-18) — the agency pitch system (reps, 3-studio spec
  pitches), hard anti-spec-work stance, "saying no is powerful"; ~$30k pitch-cost [self-reported]; 5 quotes.
- Context/NOT-Chris: Typographic Terminology (animated glossary, no speech), Day-in-Life of BEN BURNS
  (Chris absent, per the Encina precedent).

Synthesis notes: debt 5 batches / checkpoint 10 (halfway). Strong PRICING + sales cluster: the logo
deep-dive + charge-to-diagnose deepen topics/pricing; empathy/trust + ad-agency-pitching/anti-spec +
the prior Defeat series deepen topics/sales-clients. The 2017-07-07 self-aware traits ("angry Asian guy",
English-writing discomfort, combativeness) further enrich persona/voice at the next Stage P/synthesis.
Continue P2.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 July-2017 (goals, awareness, Deep-Dive eps, Blind)

Twenty-third video batch (176 L2 total). 6 ★L3.
- ★ Grow Your Business — Have Clear Goals Ep.5 (2017-07-20) — four-column prioritization grid
  (activity/impact/urgency/money, 1–5, top-3) + revenue goal-decomposition (annual→quarterly→monthly,
  overshoot) + daily focus-sheet; 10 quotes. (Melinda Livsey coachee = context.)
- ★ Feeling Overwhelmed — Information Overload Ep.6 (2017-07-26) — consume-with-purpose (shopping-list
  vs hoarding), limited-capacity backpack metaphor, business-self-sets-the-learning-agenda, the
  procrastination-via-craft diagnostic, action-beats-intent; 11 quotes. (Douglas Davis "3 Rs" credited;
  Melinda = context.)
- ★ How Will Customers Find You (2017-07-18) — the profit chain traced BACKWARDS (profit←work←close←
  proposal←RFP←meeting←contact) + awareness→validate→convert→delight→share funnel + "inform or inspire"; 7q.
- ★ Goal Setting (2017-06-24) — the "magic stairway" scaffolding for recursive goal decomposition +
  chunking calibration (monthly→weekly→daily→minute); 6 quotes.
- ★ Motivation, Focus & Grind (2017-07-28) — good-vs-BETTER requires extra effort/late nights;
  finesse-details-no-one-sees craft standard; 5 quotes. [self-reported: 21-hr shift, first sunrise in office in ~8-9 yrs]
- ★ Life Inside a Design Studio: Blind Ep.01 (2017-07-22) — "think more, make less"; "design from a
  place of Truth"; every-project-a-chance-to-learn; 5 quotes + Blind mentorship-culture CONTEXT (interns
  handed real client briefs; cross-link entities/blind).
- Document & Show Your Process (2017-07-13) — restatement of show-your-work-reduces-risk (speaker
  attribution: uncertain, likely Chris); not L3.
- Day-in-Life of GREG GUNN (2017-07-25) — Chris absent → context page (3rd day-in-life after Encina, Ben Burns).

Synthesis notes: debt 6 batches / checkpoint 10. Strong MINDSET/discipline cluster (goal-setting/magic-
stairway, prioritization grid + focus-sheet, overwhelm/backpack + procrastination-via-craft, motivation/
grind) + a CONTENT-STRATEGY awareness model (profit-chain-backwards + funnel + inform-or-inspire) for the
next checkpoint. Blind Ep01 adds studio-culture biography ("think more make less" is strong voice/beliefs).
The "Deep Dive"/Melinda-coaching series (eps 4/5/6) is a recurring format — Melinda = context throughout.
Continue P2.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 Aug-2017 (RFP, roleplays, Behance, Blind ideation)
Batch 24. Ingested 8 @thefutur videos (2017-08-01 → 2017-08-16) to L2:
- ★ RFP proposal response — price bracketing (two goal-post numbers) + competitive positioning (b9k6Ff0OMp8).
- Build a social-media following — show-your-work, process-not-product, quality>frequency (fX7m03XsGGI).
- ★ First client meeting sales-call role-play w/ Melinda Livsey Ep.7 — float budget, confirm price before proposing, charge for discovery; Melinda=context (YMFAFkbE5pw).
- ★ "You're too expensive" objection role-play — anchor, hold floor, calm walk-away, one-time-concession framing (FcyIGgFELGw).
- Blind hiring / Art Center — body-typography as #1 criterion + cultural fit (G06ljt6JGAo).
- ★ How To Get Work On Behance Ep.8 — portfolio-platform case study w/ measurable leads; Melinda=coachee/context (5S7n-OODN2A).
- ★ Logo Ideation — Life At Blind Ep.2 — logo ideation method (quantity, draw-don't-think, combine+simplify, avoid padlock cliche); team=context (AiAZAuvO2sY).
- CONTEXT: Greg Gunn's first motion-design portfolio; Chris hosts, teaching subsection separated, not persona-promoted (NFNTtSzuGvw).
Attribution: role-plays (YMFAFkbE5pw, FcyIGgFELGw) resolved per Chris-announced role direction; Life-at-Blind + Greg-Gunn team lines quarantined as context; 2 ambiguous performance beats flagged attribution:uncertain. No family names spoken; self-reported $/follower claims tagged. Counts: L2 176->184. 5 new L3-candidates.
Synthesis notes: NEW — (1) pricing: "price bracketing" (name two goal-post numbers, bracket up from client's stated figure) + confirm-price-before-proposing (never build free proposals); (2) sales-clients: first-call = high-level not scoping, float budget, "flirting/smile" warmth, charge for Discovery, objection bell-curve; (3) pricing objection: too-expensive playbook (anchor/hold-floor/walk-away/one-time-concession); (4) design-craft: logo ideation method + body-typography as top hiring signal + "fighting confusion/clarity" + layer-by-layer critique technique; (5) content-strategy: Behance/portfolio-platform growth as measurable lead-gen. Debt 6->? batches (driver: 6/10).

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 late-2017 (introvert series, NAB keynote, mindset)
Batch 25. Ingested 8 @thefutur videos (2017-08-22 → 2017-10-03) to L2:
- CONTEXT: Tristyn Pease storyboard-artist profile; Chris interviewer minimal, attribution:uncertain (lg28bG9xvks).
- CONTEXT: Julia Wright freelance career-change profile; a few Chris framing lines isolated (vA8d_z6cMxU).
- ★ Build Self Confidence / Overcome Imposter Syndrome — happiness formula (think-say-do harmony), ego-as-gap model, detachment/authenticity (6pHB0CgRBHg).
- ★ Launch A Creative Business In Your 40s Ep.1 — coaching series; Chris coaches Rebecca Hyneman (context); sell-through-curiosity BD + salary/profit/COGS lesson (D6bp5DGbSH4).
- ★ Typography Critique (Basic Typography poster) — turn-off-all-layers method, one-axis/one-grid, contrast-is-king; co-host Molly + instructor=context (dY7i4uiDHFA).
- ★ Introvert's Guide To Getting Clients Ep.2 — ambassador-not-salesperson, warm network, small mom-and-pop clients, inbound pull; Rebecca=context (pGzFzFJ04l8).
- ★ Master Your Creative Process — NAB 2017 keynote — creative-process-as-formula, positive-thinking vs positive-knowing, flow-state, burnout/insecurity origin (founding mythology of The Futur) (GgLhl71jVgw).
- ★ Secret Power of Introverts Ep.4 (Being A Great Listener) — INTJ->ENTJ over ~15yrs, boardroom-anxiety, ego/expectation as root of anxiety, design-gave-me-identity origin; Rebecca=context (-en6iRuZ9DM).
Attribution: 2 artist-profiles quarantined as CONTEXT; coaching-series mentee Rebecca Hyneman + co-host Molly kept out of persona; only Chris-attributed lines are persona data; ASR speaker boundaries flagged uncertain where fuzzy. No family names spoken; self-reported $/bio claims tagged. Counts: L2 184->192. 6 new L3-candidates. Note: NAB keynote + Introvert Ep.4 carry rich biography/voice/origin material for next synthesis.
Synthesis notes: NEW — (1) mindset: imposter-syndrome/confidence framework — "happiness = think/say/do in harmony", ego = gap between conscious & unconscious, positive-thinking vs positive-knowing, INTJ->ENTJ personality shift; (2) biography/origin: burnout + insecurity after ~5yrs pushed Chris into teaching (founding mythology of The Futur); design "gave him an identity"; ~1995 career start corroboration ("22 years" in 2017); (3) sales-clients: introvert BD method — ambassador-not-salesperson, start from your passions/warm network, target small clients, let inbound content pull business; (4) design-craft: typography-critique method (turn off all layers, add back one at a time, one axis/grid, contrast). Debt 7/10 (driver) — synthesis checkpoint ~3 batches out.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 Oct-2017 (Pitch This!, critiques, Rodchenko, design-craft)
Batch 26. Ingested 8 @thefutur videos (2017-10-08 → 2017-10-31) to L2. **Milestone: L2=200.**
- ★ Pitch This! present design work — presenting doctrine: language-is-power, work-doesn't-speak-for-itself, give client a lens/theme, anchor unknown terms to known references; Ben Burns=context (rOGAJwm3n_M).
- ★ Gourmet-brochure typography critique — serif-pairing for food brands, white-space=luxury, break/hug the gutter, rule of thirds, gold sparingly; Molly + designer Eddie=context (ND4VNkb4J3o).
- ★ Rodchenko / Russian Constructivism history — anti-originality thesis ("original = ignorant or arrogant"), timeless-over-trendy, geometric foundations (square/circle/triangle); Chris + Ben co-teach (-MMwGkUioFQ).
- ★ Brainstorm w/ Google + stock — "art of search" ideation method (dictionary def, autocomplete, broad-to-narrow, three-flicks rule, mine stock metatags, collect-without-judging); Emily/Molly=context (Xng-RR0XOWY).
- ★ "Ben Tells All" working w/ clients — ATTRIBUTION CORRECTION: title misleading, Chris is the DOMINANT teaching voice (Ben Burns=interviewee/context). Money-mindset (abundance vs scarcity), call technique (show up empty, unpack loaded questions, non-adversarial selling), imposter-syndrome coaching (UHpjAyAqRd0).
- What Motivates Creatives (2-min cutdown) — take-care-of-your-people culture; Chris solo; likely excerpt of a longer talk (4oGtHgo3OwE).
- CONTEXT: "Be a BETTER Creative Director" — Chris ABSENT (at Adobe MAX); hosted by Matthew Encina + Molly Zrelak. Zero persona data; filed as context per SUBJECT.md instructor-only rule (3jD8i1No1L0).
- Pitch This! talk about design — context-first/story/crescendo pitch structure; Ben+Matthew=context; attribution:uncertain (auto-captions, no speaker labels) (3jBen84xtSM).
Attribution: strong discipline this batch — 1 Chris-absent video correctly quarantined (no persona), 1 title-misleading video correctly RE-attributed to Chris; co-hosts (Molly, Emily), Ben Burns, Matthew Encina, reviewed designers all fenced as context. No family names. Counts: L2 192->200. 5 new L3-candidates.
Synthesis notes: NEW — (1) sales-clients/presenting: "Pitch This!" presenting doctrine — language is power, the work does NOT speak for itself, give the client a lens/theme, anchor unfamiliar design terms to client-known references, describe non-visual senses, surface mood boards to extract feedback; context-first then story then crescendo; (2) design-craft beliefs: anti-originality thesis (chase GOOD not original; "if you think it's original you're ignorant or arrogant") + timeless-over-trendy (never "on trend") + geometric-shape foundations, from the Rodchenko lesson — strong beliefs.md/voice.md material; (3) design-craft method: "art of search" ideation via search-autocomplete + stock-photo metatags; typography/layout principles (white-space=luxury, gutter, serif-pairing); (4) mindset/sales: money-mindset abundance-vs-scarcity + "show up empty" call presence (Ben-Tells-All). Debt 8/10 (driver) — synthesis checkpoint ~2 batches out; ★L3 backlog now large across design-craft + sales-clients + mindset.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 Nov–Dec-2017 (comfort-zone series, logo critiques, imposter syndrome)
Batch 27. Ingested 7 @thefutur videos (2017-11-01 → 2017-12-15) to L2 (1 row, yt-OBCuDSxl_A8, left open on 429 — retry next batch):
- Master the Pen Tool (Illustrator) — Chris teaching; software mechanics, low persona value; rushed-first-pass-then-refine style (Ow6g-kHRR1Y).
- ★ Get Out Of Your Comfort Zone Ep.1/4 — public-commitment/accountability (Adobe MAX "posted my goal" story), conversation difficulty-ladder (strangers → dream client → president); introvert self-disclosure; Melinda/Rebecca=context (fRUYLjkfZKI).
- ★ Stop Overthinking Ep.3 — "too-dumb-to-fail" action model, kayak-vs-ship metaphor, "this is life not a chore"; Melinda/guest=context (yCFGKzFHnOc).
- ★ The Best Logos Are Simple, Not Overworked — restraint=timelessness, judge the mark separately from its application, Dieter Rams/Braun benchmark; co-host Molly (counter-argument)=context (TH-jqZ4xueI).
- ★ Self-Doubt & Imposter Syndrome (w/ unnamed therapist=context) — self-confidence-vs-self-esteem distinction, caregiver-imprint/inner-voice model, Gestalt empty-chair; deep Chris biography (introvert temperament, "don't feel that" upbringing, praise-need) (EIW1Xt5l2T8).
- Learn Typography course trailer (promo) — LIGHT L2, value is VOICE BANK: "If you don't control type, type controls you", "forever intimidated by type", "the key to the design universe", "move at the speed of thought" (gI8fEZvwZyY).
- ★ F1 Formula 1 Logo Critique — "the logo is the tip of a giant beast called the business"; judge the system/business-fit not standalone aesthetics; Beirut diving-vs-swimming long game; Chris solo (y42PI9peurI).
Attribution: co-hosts (Molly, Emily), mentees (Melinda, Rebecca), unnamed therapist, and quoted third parties (Beirut, Rams, Ross Brawn) all fenced as context; only Chris-attributed lines to persona; ASR-inferred speakers flagged uncertain where fuzzy. Chris's young son referenced in pen-tool video → redacted per family-privacy policy. Counts: L2 200->207. 5 new L3-candidates.
Synthesis notes: NEW — (1) mindset: public-commitment/accountability framework + conversation difficulty-ladder + "too-dumb-to-fail" bias-to-action + self-confidence-vs-self-esteem clinical distinction (caregiver imprint, empty-chair) — strong beliefs.md + biography material (childhood conditioning, praise-need); (2) design-craft/branding beliefs: logo simplicity/restraint = timelessness (Dieter Rams), "logo is the tip of the beast" (judge business-fit + whole system, not the standalone mark), judge mark separate from application; (3) voice.md catchphrases: typography-course-trailer voice bank ("if you don't control type, type controls you"). Debt 9/10 (driver) — SYNTHESIS CHECKPOINT DUE NEXT ITERATION (debt hits 10). Large ★L3 backlog across mindset (imposter/confidence/action) + design-craft (logo simplicity, typography critique, ideation) + sales-clients (presenting doctrine) ready to promote.

## [2026-07-17] lint | synthesis pass 3 — P2 mid/late-2017 era (batches 18–27) → persona v4
Stage S synthesis checkpoint (debt hit 10/10). Promoted the accumulated ★L3 backlog from batches 18–27 (~78 L2 pages, L2 129→207) into all 7 topic hubs + persona; recompiled system-prompt v3→v4 (compiled_from 129→207). One agent per file (no write races).
Topic hubs enriched:
- pricing 11→15: price-bracketing (two goal-post numbers), confirm-price-before-proposing/never-free-proposals, "too expensive" objection playbook (anchor/hold-floor/walk-away/one-time-concession), logo-pricing (Embrace-and-Pivot/reputation).
- sales-clients 14→18: first-call doctrine (high-level, float budget, charge for discovery, objection bell-curve), introvert/ambassador BD, "Pitch This!" presenting doctrine (language-is-power, work-doesn't-speak, give-a-lens, anchor-unknown-to-known), show-up-empty call presence.
- design-craft 11→16: logo ideation (draw-don't-think), turn-off-layers critique method, "art of search" ideation, anti-originality + timeless-over-trendy + geometric foundations, logo simplicity/restraint=timelessness (Rams) + "logo is the tip of the beast".
- mindset 13→21: confidence/ego (happiness=think-say-do-harmony, ego=conscious/unconscious gap), introvert power (INTJ→ENTJ), public-commitment + conversation difficulty-ladder, too-dumb-to-fail bias-to-action, goal-setting/overwhelm/motivation cluster, self-confidence-vs-self-esteem (therapist framework kept as context).
- content-strategy 13→16: awareness funnel (profit-chain-backwards, inform-or-inspire), Behance portfolio lead-gen, show-your-work/documentarian.
- branding 23→25: "logo is the tip of the beast" (judge system+business-fit), restraint=timelessness (judge mark separate from application).
- business 12→13: sell-through-curiosity BD + salary≠profit lesson; take-care-of-your-people culture + autonomy/protect-time.
Persona: beliefs ~41→~62 (21 new, all dated/cited); voice +16 catchphrases (typography "if you don't control type, type controls you"; "logo is the tip of the beast"; anti-originality "ignorant or arrogant"; presenting "work does not speak for itself"; mindset "happiness = think/say/do in harmony", "this is life not a chore") + 2 traits (extreme-introvert confession, role-play/demo teaching); biography +12 facts (burnout ~5yrs → sabbatical → Otis teaching → Futur founding mythology; design "gave him an identity"; ~1995 start; INTJ→ENTJ; childhood "don't feel that" conditioning; Kier McLaren ~10yr coach). system-prompt v4.
Contradictions flagged this pass: pricing 2017 one-time-discount vs 2023 no-discount; content-strategy 2017 quality-over-frequency vs 2022 daily-consistency; mindset too-dumb-to-fail vs disprove-your-own-ideas; design-craft judge-mark-alone vs judge-whole-system (context-resolved).
Governance: family names kept out of every file; military/Army background NOT propagated (gaps.md verify item); single-Emmy preserved (no "two Emmys"); coachee/guest/therapist/co-host material fenced as context throughout. High-water mark advanced to batch 27. Resume ingest (Stage B, P2) next iteration.

## [2026-07-17] ingest | yt batch (@thefutur, 5) — P2 2017-12→2018-01 (agency growth, sales, boundaries)
Batch 28 (first ingest after synthesis pass 3). Ingested 5 @thefutur videos (2017-12-26 → 2018-01-23) to L2. 3 rows on 429 rate-limiting left open for retry (yt-OBCuDSxl_A8, yt-ScACW5YgiXs, yt-o5iqEfJxJ7c).
- DIY Packaging Design Assignment — specific packaging-redesign exercise (item under $10, don't change the package); student=context; a recited acting-monologue Chris speaks flagged as NOT his own belief (yg9-bxIf4s4).
- Double Your Revenue / Grow Your Design Agency — 1:1 coaching applying referral + low-hanging-fruit + order-of-the-ask (Sinek) material; coachees=context; $200k→$400k figures self-reported (QPKUN40ZjK8).
- How Do You Learn Soft Skills — short clip; Socratic self-teaching heuristic; cites Cialdini's Influence; student=context (NSgh1UVfKTU).
- ★ Basic Steps To Get More Sales (Edit) — VOICE BANK of canonical sales phrasings: "amateurs give advice, experts diagnose", "we get paid to think versus make", know/trust/like, inbound-vs-outbound (pull vs push); excerpt of a longer live talk (XL1Hb9ffcis).
- ★ How To Say NO To A Toxic Boss (Role Play) — boundary-setting voice: hold-the-line on unpaid overtime, "I'm gonna charge you more to do that" money-boundary; Chris plays the employee (persona), "Greg" the boss (context) (sBNHvx8Vc6M).
Attribution: coachees/students/role-play counterpart all fenced as context; only Chris-attributed lines to persona; a recited monologue explicitly quarantined as not-a-belief; self-reported figures tagged; ASR mis-transcriptions noted. No family names. Counts: L2 207->212. 2 new L3-candidates.
Synthesis notes: NEW — (1) sales-clients voice bank: canonical verbatim phrasings of already-known frameworks ("amateurs advise / experts diagnose", "paid to think vs make", know/trust/like, inbound-vs-outbound) — voice.md quote candidates; (2) sales-clients/mindset: boundary-setting/say-NO voice (hold the line on unpaid overtime, charge-more-to-do-that) — a distinct first-person boundary demonstration. Mostly restatement/coaching of pass-3 material otherwise. Debt 1/10 (driver reset after pass 3).

## [2026-07-17] ingest | yt batch (@thefutur, 4) — P2 2018-01→02 (hiring, career transitions; 2 Chris-absent)
Batch 29. Ingested 4 @thefutur videos (2018-01-01 → 2018-02-03) to L2. 3 rows still on 429 rate-limiting, left open (yt-OBCuDSxl_A8, yt-o5iqEfJxJ7c, yt-D9d56YM1i7U).
- CONTEXT: "Why Being Bad Is Good For Art" — Chris ABSENT; guest Jonah Loeb (Skyrim artist) delivers the make-bad-art growth idea, host Mark Contreras intros. No persona data (ScACW5YgiXs).
- Hire Freelancers / Grow Your Business (Pro Call) — Chris coaching an unnamed caller (context); day-rate vs billable-rate margin logic, delegation; $400-600/day + "20+ yrs" self-reported (MabpAXttXME).
- How To Quit Without Burning Bridges — short clip; graceful off-boarding anecdote (counter-offer story); attribution:uncertain but likely Chris (Blind/Futur employer voice); departing employee=context (xHv5qBbkEZw).
- CONTEXT: "Emily's First Portfolio Review Pt.1" — reviewer is GREG GUNN ("hey everybody Greg here"), NOT Chris; Chris only mentioned. No persona data; Emily=context, surname redacted (13jsuMkJxMY).
Attribution: STRONG discipline — 2 of 4 videos correctly caught as Chris-absent (guest-led / Greg-Gunn-led) and quarantined as CONTEXT with no persona training; coachee/departing-employee fenced; self-reported figures tagged. No family names (Emily surname + "my dad" redacted). Counts: L2 212->216. 0 new L3-candidates (thin long-tail batch: 2 context + 2 short/coaching).
Synthesis notes: none genuinely new — 2 Chris-absent context pages, 1 short off-boarding anecdote, 1 coaching restatement of hiring/margin material already covered. Debt 2/10.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 late-2017 backfill + Feb-2018 (money, typography, influences)
Batch 30. Ingested 7 @thefutur videos (2017-11-11 backfill + 2018-01-26 → 2018-02-26) to L2. Caption 429s cleared for 2 of 3 stuck rows; 1 still open (yt-o5iqEfJxJ7c).
- ★ How To Talk About Money With Clients Ep.2/4 — budget/scope/timeline "pick two of three" constraint, "you can't lose a job you never had" reframe, budget-first qualifying script, "priming the pump" (Darren Hardy); Chris plays both roles; workshop participants=context; $ self-reported (OBCuDSxl_A8).
- CONTEXT: Patrick Seymour woodcut pen-tool tutorial — guest-led; Chris interviewer only; garbled captions (D9d56YM1i7U).
- CONTEXT: Emily Portfolio Review Pt.2 — Chris ABSENT (referred to in 3rd person: "the deck Chris gave me"); reviewer likely Greg Gunn; no persona data (zk2qp_YxYVM).
- CONTEXT: "Inspiration Is For Amateurs" w/ Kyle Cooper — ~80% Kyle Cooper (Chris's INFLUENCE; Se7en title designer); "let the problem tell you what it wants to be"; Chris ~20% interviewer + closing "designers bring baggage so they can't hear the problem"; Chris brought his ArtCenter students to Cooper's studio (documented mentor link). Kyle-Cooper entity-page material captured (l4NRhEp5efU).
- Young Guns Ep.1 — series intro/teaser; narrator confirms Chris coaches, but Chris doesn't speak on-camera in this ep; 5 coachees=context; no persona quotes (b9uU-ZjgiHU).
- ★ Typography — Rules for Graphic Design — DISTINCT legibility rules not yet documented: triadic point-size/measure/leading relationship, word-shape recognition/anti-all-caps, 9-12pt reading size, x-height→more-leading (Helvetica), 65/52 char max-measure by x-height. attribution:uncertain (single narrator, no self-ID; likely Chris) — VERIFY before persona promotion (EozQvV3oQ7c).
- CONTEXT: Kier McLaren MASTERMIND Ep.1 — ~95% Kier bio (Pittsburgh, football, social worker→radio→ad agency→screenwriting→consultant; Harper's Magazine; "everything I teach I learned from someone else"); Chris 15s framing only; corroborates ~10-15yr Chris/Blind coaching relationship. Kier-McLaren entity-page material captured (J_m9-4rgpiE).
Attribution: STRONG — 4 of 7 correctly caught as context (guest/influence/coach-led or Chris-absent); Kyle Cooper + Kier McLaren flagged for future CONTEXT/INFLUENCE entity pages; typography-rules held at attribution:uncertain pending verification. No family names. Counts: L2 216->223. 2 new L3-candidates.
Synthesis notes: NEW — (1) pricing/sales: money-conversation framework — budget/scope/timeline "pick two of three", "you can't lose a job you never had", ask-budget-first qualifying (money series Ep.2/4; promote alongside the other 3 eps when ingested); (2) design-craft: distinct typography LEGIBILITY rules (triadic size/measure/leading, x-height→leading, 65/52 char max-measure) — attribution uncertain, verify before persona; (3) ENTITY-PAGE debt: Kyle Cooper (influence — title design, "let the problem tell you what it wants", documented mentor) + Kier McLaren (context — business coach bio, ~10-15yr relationship) → create at next checkpoint. Debt 3/10.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P2 Feb–Mar-2018 (strategy-selling, Euro tour, masterminds)
Batch 31. Ingested 6 @thefutur videos (2018-02-28 → 2018-03-12) to L2. 2 rows on 429 rate-limiting left open (yt-o5iqEfJxJ7c, yt-v-xKqqXPlDg).
- CONTEXT: "What Does An Executive Producer Do?" — Scott Ross (Blind/Futur EP) explains his own role; Chris absent; no persona data (jOeHZVWAbaw).
- ★ From $0 to $5k For Strategy Ep.9 — strategy-pricing framework: charge for THINKING, strategy>objectives>deliverables hierarchy, current-state/aim/ideal gap diagram, budget-qualify at 5-10% of gross, lead with strategy as the only entry point, refer out deliverables-only work; mentee Melinda Livsey=context, figures self-reported (D2rDvkSfrCI).
- ★ How To Sell Strategy Without Design/Visuals Ep.10 (role-play) — sell thinking-not-making, Tender-Greens/Club-33 intangibles demo (order-taker vs trusted-advisor), qualify-first, decks-are-crutches "your mind is what they're paying for", block-of-marble bite-sized pitching, double-the-rate $5k->$10k->$20k, price as qualifier/filter; Chris=seller/coach, Melinda=client/context (dKIyObgkBVI).
- ★ (thin) Euro Tour London Day 1 VLog — Chris cold-open mission thesis "it's our responsibility as designers to change the world"; rest is travel B-roll + attribution-uncertain collaboration riff; captions sparse (eP5jYUmtiQo).
- CONTEXT: Kier McLaren MASTERMIND Ep.2 (why not to take low-paying work) — ~100% Kier; the anti-lowball thesis is Kier's (Chris endorses but doesn't speak); more Kier entity-page bio (sporting-goods store, film-camera rental business) (x8aMA-kbldo).
- London Event Recap VLOG Day 2 — montage of familiar Futur themes (businesses die from lack of focus, sell-then-figure-it-out, 3-challenges prospect exercise, ignore the client's price anchor); Chris to-camera; mostly logistics (pabF-nu6bMo).
Attribution: Scott Ross + Kier McLaren correctly quarantined as context (Chris absent/endorsing-only); Melinda fenced across both strategy episodes; vlog travel B-roll marked low-value + uncertain lines flagged. No family names. Counts: L2 223->229. 3 new L3-candidates.
Synthesis notes: NEW — (1) pricing/sales-clients STRATEGY-SELLING cluster (Ep.9 + Ep.10, promote together): charge for thinking not making; strategy>objectives>deliverables; budget-qualify at 5-10% of gross; lead with strategy as sole entry point; refer out deliverables-only work; intangibles/order-taker-vs-trusted-advisor demo (Tender Greens/Club 33); decks-are-crutches "your mind is what they pay for"; price-as-qualifier; double-the-rate ladder — strong pricing + sales-clients + beliefs material; (2) mindset/mission: "designers' responsibility to change the world" thesis (Euro tour, attribution-uncertain — verify); (3) ENTITY debt grows: Kier McLaren bio deepened. Debt 4/10. Note: strategy-selling is the strongest ★L3 cluster since the pass-3 material.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P2 Mar-2018 (role-play Ep.11, Young Guns Ep.2; 4 context)
Batch 32. Ingested 6 @thefutur videos (2018-03-06 → 2018-03-26) to L2. 2 rows on 429 rate-limiting left open (yt-o5iqEfJxJ7c, yt-ORNW7oRVF_Q).
- CONTEXT: "Starting Over — Rebuild Your Identity" — guest-dominated interview (Phoenix-protocols/football-injury story = guest); Chris interviewer only, uncertain (v-xKqqXPlDg).
- CONTEXT: Kier McLaren MASTERMIND Ep.3 (Break Rules, Take Risks) — ~100% Kier bio (FCC radio, Job Corps Pittsburgh, Erich Fromm's Escape from Freedom); bio explicitly does NOT match Chris; Chris absent; Kier entity material (v-dQZ7URtVc).
- ★ Dealing With Tough Clients Who Tell You What To Do (Role Play Ep.11) — reassert expertise WITHOUT arguing: disagree-without-being-disagreeable, embrace-then-pivot-to-logic, "double down on their thinking", doctor/self-diagnosis framing, "measure twice cut once", "brand building not logo building"; role INVERSION — Chris plays the designer/seller (persona), Melinda=difficult client/context (fiCVUdEFtqc).
- CONTEXT: "How to Network Through Email/DM" — presenter is MATTHEW ENCINA (self-IDs, signs example emails), NOT Chris; his be-genuine/curious/add-value/ask cold-outreach framework is Encina's; no persona data (2Xs3371FdzA).
- ★ Designer Portfolio Reviews — Young Guns Ep.2 — Chris CONFIRMED reviewer (super-stacking, Eli Altman podcast cite, self-deprecating "four followers"); reusable 4-category portfolio rubric (social-media marketing / presentation & quality / clarity of service / personality, each 1-5) applied across 5 portfolios; engagement-math heuristics (sub-10%=suspicious, boosted-post spikes collapse); Emily + reviewed designers=context (z8BuocNq1Po).
- CONTEXT: "How to Find Clients that Value Design" — Ben Burns interviews guest Ran Segall (Flux/Prospero); Chris absent (only a closing "Christo clap" joke); positioning ideas are the guest's; no persona data; Ran-Segall entity candidate (w_TYQQIagwc).
Attribution: EXCEPTIONAL discipline — 4 of 6 correctly quarantined as context (3 Chris-absent: Matthew Encina, Ben Burns+Ran Segall, guest-interview; + Kier). Only 2 genuinely Chris-led (both ★L3). Melinda fenced in the role-play; role-inversion (Chris=seller) noted. No family names. Counts: L2 229->235. 2 new L3-candidates.
Synthesis notes: NEW — (1) sales-clients/mindset: difficult-client method — reassert expertise WITHOUT arguing (disagree-without-being-disagreeable, embrace-then-pivot-to-logic, doctor/self-diagnosis framing, brand-building-not-logo-building) — strong sales-clients + beliefs material; (2) design-craft/content-strategy: Chris's portfolio-REVIEW rubric (4 categories x 1-5: social-media marketing / presentation-quality / clarity-of-service / personality) + "super stacking" + engagement-math heuristics; (3) ENTITY debt grows: Matthew Encina (instructor-context, already have futur-instructors page) + Ran Segall/Flux (guest-context candidate) + Kier McLaren (deepening). Debt 5/10 (halfway to checkpoint). Note: this era is heavily instructor/guest-led — attribution vigilance paying off.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P2 Jan-backfill + Mar-Apr-2018 (designer value, career, conscious capitalism)
Batch 33. Ingested 6 @thefutur videos (2018-01-18 backfill + 2018-03-21 → 2018-04-14) to L2. 2 new rows on 429 rate-limiting left open (yt-CmqAJ4sILHo, yt-VCvebusD5Fo); prior 429 backlog fully cleared.
- ★ Why Some Designers Are More Valuable Than Others — value-scale-of-questions (low/quantitative -> mid/qualitative -> high/purpose) + Discovery-as-a-paid-question-based-service (symptoms->cause "onion"); Chris solo monologue (o5iqEfJxJ7c).
- CONTEXT: "Thrive As An In-House Designer feat. Charli Marie" — guest Charli Marie (CharliMarieTV) delivers all the in-house tips; Chris interviewer only (4 minor framing items: learner-stance, devil's-advocate, audience-advocacy); bilingual captions, English used (ORNW7oRVF_Q).
- Edinburgh Whitespace event VLOG (humility vs confidence) — scattered fragments (fact-vs-opinion, Jim Rohn major/minor effort, no-victims-just-volunteers, 100%-responsibility); garbled captions; attribution:uncertain; mostly travel (KM0trenddH8).
- Conscious Capitalism & Non-Profits — panel w/ guest Matthew Manos (very nice; "give half your work away" 50% pro-bono model = CONTEXT); Chris's contributions (do-free-to-prove-to-YOURSELF, value isn't real until dollar-quantified, brand-as-filter/stake-in-the-ground, give leveraged services not "dumb money") restate existing positioning -> L2; Manos entity candidate (oAHxZeBUbXM).
- CONTEXT: "Framing Your Shot" — non-Chris Futur motion/3D instructor teaches composition; Chris absent; no persona data (YvK_8G4w25E).
- ★ 4 Tips To Grow As a Designer (career, 5-min edit) — (1) no right/wrong path, just A path (evaluate + switch w/o judgment); (2) "inch wide, mile deep" positioning; (3) traditional graphic design "dead/dying" -> build community around values + monetize audience; (4) use full-time income as runway to raise freelance rates -> AD/CD -> delegate to global network -> entrepreneurship; Chris solo (52WYy8aESFs).
Attribution: 3 of 6 context (Charli Marie guest, Matthew Manos guest panel, non-Chris composition instructor); Chris-solo material cleanly captured in the 2 ★L3s + the panel's Chris-half. No family names (Chris only says "a wife, a dog, two cats" generically). Counts: L2 235->241. 2 new L3-candidates.
Synthesis notes: NEW — (1) sales-clients/pricing: value-scale-of-questions (quantitative->qualitative->purpose) + Discovery-as-paid-service (symptoms->cause onion) — strong pairing with the strategy-selling cluster (Ep.9/10) for the next checkpoint; (2) mindset/career: "4 tips" growth framework — a-path-not-the-right-path, inch-wide-mile-deep positioning, traditional-design-dying/build-community, income-as-runway ladder; (3) business/mission: conscious-capitalism position — do free work to prove it to YOURSELF, value isn't real until dollar-quantified, brand-as-filter (Chris's half of the Manos panel). ENTITY debt: + Matthew Manos (very nice / give-half — guest context). Debt 6/10. Note: designer-VALUE + Discovery material strengthens the pricing/sales checkpoint cluster.

## [2026-07-17] ingest | yt batch (@thefutur, 4) — P2 Apr–May-2018 (self-confidence, Young Guns Ep.3; 2 Kier masterminds)
Batch 34. Ingested 4 @thefutur videos (2018-04-24 → 2018-05-09) to L2. 3 rows on 429 rate-limiting left open (yt-CmqAJ4sILHo, yt-VCvebusD5Fo, yt-zh7gYockjys) — rate-limiting rising, smaller batch this round.
- CONTEXT: Kier McLaren MASTERMIND Ep.4 (Go Your Own Way) — ~100% Kier (distrust-the-system, American-dream-as-nightmare, risk-as-differentiator, country-club upbringing rejected); Chris silent; one indirect trait ("worst thing to say to Chris: 'this is how the other guy does it'"); Kier entity material (gB7WZQNwsdE).
- ★ Believe In Yourself — Power of Self Confidence — DISTINCT confidence mechanism (not a restatement): "be nothing / I'm just a mirror to you" (Zen), decouple self-confidence from credentials (portfolio/school/awards/reputation/looks), recast credentials as "props/crutches", make the interaction about the OTHER person (therapy-style question process), "remove yourself from the equation"; Chris solo; Karen cold-client role-play illustration (0WQVRQ07WtE).
- ★ Pharma Package Design Challenge — Young Guns Ep.3 — Chris-led (confirmed); reusable package/branding critique lens: "me too" design, shelf-presence via shape/color, aesthetic->demographic mapping (clinical vs natural/pastel), house/generic-vs-name-brand as a branding problem ("deliberate design confusion"), constrained brief (keep type, redesign rest, 24h); contestants Connor+Shawn Campbell=context (FDhK1R3GJzs).
- CONTEXT: Kier McLaren MASTERMIND Ep.6 (Look Inside Yourself) — ~100% Kier (inner-child dominant/non-dominant-hand writing exercise, Wizard-of-Oz/Joseph-Campbell hero's-journey, "emotional reaction out of proportion" diagnostic); Chris silent; Kier is an author (entity material) (ktGYhw7gmMY).
Attribution: 2 of 4 are Kier-solo masterminds (context, Chris silent); 2 genuinely Chris-led (both ★L3). Kier entity material now substantial across Eps 1-6. No family names. Counts: L2 241->245. 2 new L3-candidates.
Synthesis notes: NEW — (1) mindset/sales-clients: DISTINCT self-confidence mechanism — be-nothing/be-a-mirror, decouple confidence from credentials (credentials=crutches), remove-yourself-from-the-equation / make-it-about-the-other-person; genuinely different from the existing imposter-syndrome pages, strong beliefs.md material; (2) design-craft/branding: package-design critique lens (me-too design, shelf-presence, aesthetic->demographic mapping, house-vs-name-brand). ENTITY debt: Kier McLaren page now has rich material across 6 mastermind eps (bio + worldview + author + coaching toolkit) — ready to write at checkpoint. Debt 7/10 (checkpoint ~3 batches out). Rate-limiting note: 3 429s this batch; kept batch to 4.

## [2026-07-17] ingest | yt batch (@thefutur, 5) — P2 Apr–May-2018 (Mirrormask, Karin Fong, Young Guns; L2=250)
Batch 35. Ingested 5 @thefutur videos (2018-04-18 → 2018-05-22) to L2. **Milestone: L2=250.** 3 rows on 429 rate-limiting left open (yt-zh7gYockjys, yt-JNTqHJQp1QU, yt-hK_0XPzvpoA).
- Want To Raise Your Value / Solve Bigger Problems — short; reinforces the value-ladder (2018-01-18 page); distinct angle = self-label / "little box" + law-of-the-instrument; Chris solo; not L3 (restatement) (CmqAJ4sILHo).
- ★ Learn Self Acceptance — Letting Go Of Ego — DISTINCT "Mirrormask" metaphor (a mask we mistake for a mirror / idealized self-image that drains energy; the world already sees you as you are) + vivid YouTube-origin discomfort story (first ~10 videos, clenched jaw, hated his own voice, "stop editing within eight feet" rule); Chris solo; strong voice + biography material (VCvebusD5Fo).
- Young Guns Ep.4 (packaging process) — mostly contestant-narrated design process=context; Chris hosts but defers the critique to Ep.5 ("butcher knives out next episode"); contestants (Arun/Sean/Spencer/Connor/Sherif)=context; not L3 (E7vJONz6HKg).
- CONTEXT: Karin Fong interview (main-title-design legend, Imaginary Forces) — Karin=influence/peer/context; process (immerse->distill to one central metaphor), "can it run in front of another show?" uniqueness test, three traits (appropriateness/clever-surprise/craft); Chris interviewer only. BIO NUGGET (persona, promote to biography): fresh out of grad school Chris ran his own studio and was brought into R/GA LA (~late 1990s) to work under Kyle Cooper — incl. Island of Dr. Moreau storyboards — his first exposure to title design; Karin-Fong entity candidate (D-i9yPcEW28).
- Business of Design w/ Rebecca Ep.5 — delegation-margin (2x contractor + ~30% + mark up your AD/CD time), freelancer->owner mindset, hire-people-better-than-you, LinkedIn biz-dev, fundamentals-over-magic-bullets; cites Michael Janda/Blair Enns/Steve Jobs; Rebecca Hyneman=context; restatement, not L3 (SwsivXHY-cU).
Attribution: Karin Fong (guest/influence) + Rebecca (coachee) + Young Guns contestants fenced as context; 2 Chris-solo mindset/value clips cleanly captured. No family names (kids referenced, unnamed). Counts: L2 245->250. 1 new L3-candidate.
Synthesis notes: NEW — (1) mindset/voice: "Mirrormask" self-acceptance metaphor + YouTube-origin discomfort story (hated own voice, first 10 videos) — distinct from existing ego/confidence pages, strong voice.md + biography material; (2) BIOGRAPHY: Chris at R/GA LA under Kyle Cooper (~late-1990s, Island of Dr. Moreau storyboards) = his first title-design exposure — promote to biography.md (deepens the Kyle Cooper influence link); (3) minor: self-label/little-box value angle (restatement). ENTITY debt: + Karin Fong (influence), + confirm Kyle Cooper entity page (Chris & Karin both worked under him at R/GA). Debt 8/10 — checkpoint ~2 batches out; entity-page backlog (Kyle Cooper, Kier McLaren, Karin Fong, Ran Segall, Matthew Manos) to create at checkpoint. Rate-limiting: 3 429s again this batch.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P2 May–Jun-2018 (Young Guns Ep.5 critique; Kier series completes; 5 context)
Batch 36. Ingested 6 @thefutur videos (2018-05-13 → 2018-06-05) to L2. 2 rows on 429 rate-limiting left open (yt-zh7gYockjys, yt-hK_0XPzvpoA).
- ★ Young Guns Ep.5 (Packaging Critique & Winner) — Chris sole judge (the deferred critique); reusable 4-criterion rubric (brand-integrity/positioning, shelf-presence "6ft away/jump off the shelf", improvement-over-original, USP-clarity) + ~11 packaging principles (design package as 3D six-sided sculpture wrapping graphics across edges = "what makes a packaging designer"; establish hierarchy; protect brand equity; premium=less-is-more (Aesop/Clinique); design the product not the parent logo; respect the brief; resolve one idea; design solves a business problem not "design for design's sake"); contestants=context (gx5hEcIwhnY).
- CONTEXT x5 (Chris absent or thin):
  - Kier McLaren MASTERMIND Ep.7 (eliminate negative people) — you-get-the-world-you-see, Calder-mobile metaphor, price-of-change (JNTqHJQp1QU).
  - Kier MASTERMIND Ep.8 (empty pursuit of fame) — external-validation-empty, actor-vs-star; Kier bio (D-I athletics, Harper's, broke-in-40s Burbank curb) (Jbiyh2WbWPs).
  - Kier MASTERMIND Ep.9 (outsiders break rules) — outsiders-break-paradigms (Salk/Bezos); Kier co-wrote a story w/ Chris (ittd4gieExk).
  - Kier MASTERMIND Ep.10 (failure->humility) — COMPLETES the Kier series (Eps 1-10, all Chris-absent context); luck/serendipity, 12-step incremental; Kier bio (2 divorces, ad biz, New Hampshire) (gy5KZlLRl2c).
  - Dr. Samuel Holtzman Pt.1 (objective criteria) — guest expert (criterion-driven discovery, brand-as-shared-filter, big->narrow->drill-out, I-statements); Chris thin (empathy-in-design "know how others feel", externalize/align-a-group); ArtCenter connection; Holtzman entity (FPouel_NEWI).
Attribution: 5 of 6 context (Chris absent/thin) — the Kier mastermind series is now fully cataloged (Eps 1-10) as Chris-absent context with rich Kier bio; Holtzman guest fenced. Only Young Guns Ep.5 is Chris-led (★L3). No family names. Counts: L2 250->256. 1 new L3-candidate.
Synthesis notes: NEW — (1) design-craft/branding: Chris's PACKAGING-critique rubric (4 criteria) + package-as-3D-sculpture principle + premium=less-is-more + design-the-product-not-the-parent-logo — strong design-craft material (pairs with Young Guns Ep.2/3 reviews); (2) minor persona: empathy-in-design + externalize/align-a-group facilitation (Holtzman intro). ENTITY debt now LARGE & ready for checkpoint: **Kier McLaren** (context — full bio across 10 masterminds: Pittsburgh, football/D-I athletics, social worker/Job Corps, radio, ad agency, screenwriting, Harper's, author, ~10-15yr Chris coach, worldview), **Kyle Cooper** (influence — R/GA mentor), **Karin Fong** (influence), **Ran Segall/Flux** (guest), **Matthew Manos** (guest), **Dr. Samuel Holtzman** (guest, ArtCenter). Debt 9/10 — SYNTHESIS CHECKPOINT DUE NEXT ITERATION.

## [2026-07-17] lint | synthesis pass 4 — P2 2018 era (batches 28–36) → persona v5 + 3 entity pages
Stage S synthesis checkpoint (debt 10/10). Promoted the batch 28–36 ★L3 backlog (~50 L2 pages, L2 207→256) into 6 topic hubs + persona; recompiled system-prompt v4→v5 (compiled_from 207→256); CREATED 3 entity pages. 13-agent fan-out (one file each) + system-prompt recompile.
Topic hubs enriched:
- pricing 15→18: budget/scope/timeline "pick two of three" + "you can't lose a job you never had"; value-scale-of-questions (quantitative→qualitative→purpose) + Discovery-as-paid-service; strategy pricing (get-paid-to-think, price-as-qualifier, $5k→$10k→$20k ladder).
- sales-clients 18→22: sell-strategy-without-visuals + intangibles/order-taker-vs-trusted-advisor (Tender Greens/Club 33, decks-are-crutches); dictating-client reassert-without-arguing (disagree-not-disagreeable, brand-not-logo); boundary/say-NO; know-trust-like + inbound-vs-outbound.
- design-craft 16→19: typography legibility rules (triadic size/measure/leading, x-height→leading, 65/52 measure) [attribution uncertain]; portfolio-review rubric (4-cat 1-5 + super-stacking); packaging critique (4-criteria + 3D-sculpture + premium=less-is-more + design-product-not-parent-logo).
- branding 25→27: brand-integrity-in-packaging (protect equity, house-vs-name-brand); brand-as-filter (stake-in-the-ground, value=dollar-quantified).
- mindset 21→24: confidence-without-credentials (be-a-mirror, credentials=crutches); Mirrormask; career 4-tips (a-path-not-the-right-path, inch-wide-mile-deep, design-dying/build-community, income-as-runway).
- business 13→15: conscious-capitalism/pro-bono (do-free-to-prove-yourself, give-leveraged-services); delegation-margin arithmetic (2x contractor+30%+markup, hire-better-than-you).
Persona: beliefs ~62→~85 (+23, sources 38→48); voice +~13 catchphrases (sources 24→32) + traits (YouTube-origin discomfort, "four followers" self-deprecation); biography +2 facts (R/GA under Kyle Cooper ~late-1990s + Island of Dr. Moreau storyboards / first title-design exposure; YouTube-origin discomfort ~2016). system-prompt v5.
NEW ENTITY PAGES (all with CONTEXT banners, wikilink-cited): wiki/entities/kier-mclaren.md (context — Chris's ~10-15yr business consultant; full bio across the 10-ep MASTERMIND series), wiki/entities/kyle-cooper.md (influence — title-design legend, Chris's R/GA mentor), wiki/entities/karin-fong.md (influence — Imaginary Forces, shared R/GA lineage).
Contradictions flagged: confidence be-a-mirror (2018-05) vs see-yourself-through-clients-eyes (2018-01); "amateurs give advice, experts diagnose" date-precedence (2018-01 predates the 2019 instance). Attribution discipline: strategy>objectives>deliverables + 5-10%-of-gross correctly caught as Melinda's COACHEE lines (flagged context, not Chris); "grad school" caption avoided contradicting the established no-master's fact (rendered BFA).
Governance: family names kept out of every file; military/Army NOT propagated; single-Emmy preserved. High-water mark advanced to batch 36. Deferred entity backlog: Ran Segall/Flux, Matthew Manos, Dr. Holtzman (thin guest material — create when they recur). Resume ingest (Stage B, P2 mid-2018) next iteration.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P2 Jun-2018 (fire-clients, creative-block, ArtCenter bio; Danny Yount)
Batch 37 (first ingest after synthesis pass 4). Ingested 6 @thefutur videos (2018-06-06 → 2018-06-26) to L2. 2 rows STILL on 429 (yt-zh7gYockjys, yt-hK_0XPzvpoA — open ~4 batches; if they persist 2 more, mark no-captions/skipped).
- CONTEXT: Danny Yount Pt.1 (Blade Runner 2049 title designer) — ~80% Danny (influence); Chris ~20% interviewer; Danny-Yount entity candidate (Emmy for Six Feet Under; Digital Kitchen->Prologue->Prodigal Pictures; mentor John Van Dyck; friend Ash Thorpe). Chris bio nuggets: same media generation (Ruby lith, DOS typesetting, MacWorld geek), childhood money hustle (~12-13), beliefs "give yourself a no option: die doing this or succeed" + "regret what you did not what you didn't" (vJ7qXaZW-KY).
- ★ Sometimes You Have To Fire Your Clients — resign ("fire") a bad client by refunding + paying them to leave ("here's your money back, good luck"); reject flattering-but-underpaying "ugly clients" who offer exposure/portfolio/experience instead of pay; Chris solo (figures illustrative, not personal) (y-krWqwFDa8).
- CONTEXT: Best Career Advice From 3 Industry Pros — 3 unnamed guests (no speaker labels; not fabricated per rule 5); Chris absent/host only; no persona data; internal contradiction flagged (show-5-best vs show-the-evolution) (_T_qyf9dlKg).
- ★ Get Clear & Avoid Creative Block (Fuzzy Goals = Fuzzy Results) — clarity framework: goal -> compass/direction -> picture -> map/process; rock-to-arch specificity metaphor; "two words -> images -> creative recipe"; Chris teacher, student=context (HdXfCuKu5Lg).
- CONTEXT: Danny Yount Pt.2 — mostly Danny (leadership "lead from the front", emotional-work-noticed, experience>ageism); Chris contributes real positions: creative-team leadership (know strengths, shared ownership, "make it rad is not art direction", Pareto cut-losses, safe-to-fail) + sharp EDUCATION/student-debt critique (schools as "loan officers", $200k reframe, unpayable-debt "tragedy", internet-as-equalizer/hybrid-learning = self-positions The Futur); family redacted (wife/son) (X-IZG-5ccWA).
- ★ Advice for Students: My Life at Design College — RICH BIOGRAPHY: ArtCenter College of Design; deliberately took hardest out-of-major classes; obsessive overachiever (weekly all-nighters, slept on campus); instructor Bruce Hubbard gave him a D (so he wouldn't repeat math); FINANCIAL REALITY debunks "rich kid" myth — upper-middle class, mom paid ~half tuition, Stafford loans + maxed credit cards, entered on 50% scholarship, cleared debt ~1-1.5yrs after graduating, mother kept him "hungry"; turning point age 18-19 (bad relationship, living w/ brother, parents thought him a "loser"); family unnamed (mother/brother relational only) (l-3txt1yNDU).
Attribution: 3 of 6 context (Danny Yount Pt.1/Pt.2 = influence, 3-pros = guests); 3 Chris-led ★L3. Danny Yount = 3rd title-design influence (after Kyle Cooper, Karin Fong). No family names (design-college mother/brother relational; Danny Pt.2 wife/son redacted). Counts: L2 256->262. 3 new L3-candidates.
Synthesis notes: NEW — (1) sales-clients/business: fire-your-clients / client-resignation (refund + pay-to-leave) + reject "ugly clients" (exposure-not-pay) — strong client-selection material; (2) mindset/design-craft: "fuzzy goals = fuzzy results" clarity framework (goal->compass->picture->map, specificity); (3) BIOGRAPHY (rich): ArtCenter years — all-nighters, Bruce Hubbard D-grade, FINANCIAL REALITY (upper-middle, mom-paid-half, Stafford loans, 50% scholarship, debt cleared fast) debunking rich-kid myth, 18-19 turning point → promote to biography.md; (4) mindset/education: student-debt critique (schools=loan officers, $200k reframe) — beliefs material; (5) biography nuggets from Danny Yount Pt.1 (same-media-generation, childhood-hustle, "no option: die or succeed"). ENTITY debt: + Danny Yount (title-design influence, Emmy for Six Feet Under) — 3rd in the title-designer cluster; create alongside a future checkpoint. Debt 1/10.

## [2026-07-17] ingest | yt batch (@thefutur, 5) — P2 Jun–Jul-2018 (don't-convince, internships, networking) + 2 skipped
Batch 38. Ingested 5 @thefutur videos (2018-06-26 → 2018-07-02) to L2. **Marked 2 long-stuck rows SKIPPED** (429/unavailable across 5 batches while peers succeed; both low-value context): yt-zh7gYockjys (Kier mastermind Ep.5) + yt-hK_0XPzvpoA (Blind/Futur intern recruiting) — no-captions, never Whisper w/o approval. 1 new 429 open (yt-rJf_gphvDrY).
- CONTEXT: Domain/Brand Naming Strategies — narrated by Ben Burns (NOT Chris; Chris in 3rd person only); no persona data; bio nugget: Chris had no personal website as of 2018-06 (h1cI9Ti1lG0).
- ★ How To Convince Your Clients — Don't! — reframe: if you have to CONVINCE, you skipped the "meeting of the minds"; instead do discovery, align client wants with consumer wants, advocate for the consumer, help them realize the truth themselves; Chris solo (1DJ4hpWvSBY).
- Work Or Go To School — Choose One & Focus — school-vs-work as two transactions; choose one and focus; prioritize the classes that matter; Chris, student=context; not L3 (f-2oME87pl0).
- ★ Watch This Before Your Next Internship — learning-vs-money sliding scale for evaluating work; write-down-and-prioritize your top-3 criteria as a filter; "you change the target when you love the work"; junior-year timing (resources vaporize post-grad); Chris primary, students=context (5FDRD7vMIHc).
- ★ Why Networking Doesn't Work — attract-your-mentor-by-leveling-up (Brian Tracy: close the gap, become interesting to interesting people, "meeting of the minds"); reframe networking as reciprocity/genuine-helping; ORIGIN STORY (biography): first clients via Epitaph Records → Novacom → Adobe After Effects CD → ArtCenter peers → first car commercial (Buick) via a school favor; Chris confirmed, student=context (MxShKURqbM0).
Attribution: 1 of 5 context (Ben Burns naming); 4 Chris-led (3 ★L3). No family names. Counts: L2 262->267 (+5); 2 rows skipped (no-captions). 3 new L3-candidates.
Synthesis notes: NEW — (1) sales-clients: "don't convince" reframe (convincing = skipped meeting-of-minds → discovery + advocate-for-consumer) — pairs with the difficult-client + Discovery clusters; (2) mindset/career: internship-evaluation (learning-vs-money scale, top-3-criteria filter, junior-year timing) + work-vs-school focus; (3) sales-clients/mindset: networking-as-reciprocity + attract-mentor-by-leveling-up (Brian Tracy); (4) BIOGRAPHY: early-career origin story — Epitaph Records → Novacom → ArtCenter peers → first Buick car commercial (deepens the pre-Blind timeline); + no-personal-website-as-of-2018 nugget. Debt 2/10. Pipeline-note: marked 2 persistent-429 rows skipped (no-captions) to unblock the queue.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 Jul-2018 (expressive-type, CEO-shift, objection-deck, scaling; 2 Kier)
Batch 39. Ingested 7 @thefutur videos (2018-07-03 → 2018-07-19) to L2. 1 row on 429 (yt-rJf_gphvDrY).
- ★ Expressive Typography Critique (cutdown) — DISTINCT expressive-type principles: "be expressive WITH the type" (offset/zigzag letters physically enact the message), unusual letter-spacing as emotion, meaningless-data grid texture + desaturation + gradient-as-implied-lighting + glitch-offset; Chris-probable (unnamed in cutdown), Levi Jones + Emily=context (ZwEMbqZDkXU).
- ★ Why I Don't Work On Design Projects Anymore — CEO/identity-shift framework: "making a difference vs making things", maker-mindset vs entrepreneurial-mindset; BIOGRAPHY: first-year demand exceeded capacity -> brought in friends to execute while he art-directed -> discovered +10% effort makes less-refined work "twice as good" (his scaling mechanism) -> hire-better-than-self -> shift into revenue-responsibility to retain/elevate team; Shane(audience)=context (uVhWhMv6sO4).
- CONTEXT: Instagram Growth Hack — non-Chris instructor (unnamed, UK-accented); Chris absent; no persona data (Qsgl5baPHUs).
- ★ The Worst Things Clients Have Said To Me — prototype "Objection Response Deck": codified common objections + response-move cards (acknowledge / answer-with-a-question / degree / reflect / "I don't know", combinable); "control energy -> bring it to neutral"; grounded in Blair Enns' Win Without Pitching; Chris, Rob(videographer)=context (Blja-ucC5_k).
- ★ How To Scale/Multiply-Time/Delegate — codify your process into <=5 steps (ArtCenter red-blue-dot storyboard-critique origin story = externalizing tacit judgment); "clients can't tell high from super-high quality" threshold (abandon perfectionism); churn-to-superstar team-building; hire-and-still-win margin math ($500/hr target); Chris coaching, coachee=context (OCcbTVbuRIg).
- CONTEXT x2: Kier McLaren MASTERMIND Ep.11 (living a creative life; "you are not what you do", worst-case reframing) + Ep.12 (hard decisions; ego-serving decisions, "10-yr-old strategies run a 40-yr-old life", left/right-hand journaling, neuroplasticity 30-60 days) — series extends past Ep.10; Chris absent both; Kier entity material (uL4Tn0796XI, ADT5g_gxcXI).
Attribution: 3 of 7 context (Instagram instructor + 2 Kier); 4 Chris-led ★L3. No family names (client-objection example "wife" generic). Counts: L2 267->274. 4 new L3-candidates.
Synthesis notes: NEW — (1) design-craft: EXPRESSIVE typography (type-enacts-message, letter-spacing=emotion) — distinct from prior legibility/critique pages; (2) business/mindset: CEO/identity-shift (making-a-difference-vs-making-things, maker-vs-entrepreneur) + BIOGRAPHY scaling mechanism (10%-effort-doubles-quality, friends->hire-better->revenue-responsibility); (3) sales-clients: Objection Response Deck (acknowledge/answer-with-question/degree/reflect + control-energy-to-neutral, Blair Enns) — strong sales-clients + beliefs; (4) business: scaling = codify-process-into-<=5-steps + high-vs-super-high-quality-threshold + churn-to-superstar team. Debt 3/10. Kier mastermind now Eps 1-12 (5 skipped/no-captions), all context.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P2 late-Jul-2018 (diagnostic-value, work-less, 3-things, money-Barcelona; L2=280)
Batch 40. Ingested 6 @thefutur videos (2018-07-20 → 2018-07-31) to L2. **Milestone: L2=280.** 2 rows on 429 (yt-rJf_gphvDrY, yt-zeSIj5GohoI).
- ★ Why Designers Focus On The Wrong Thing — diagnostic-phase / "tell them something they didn't know"; sell business OUTCOMES not deliverables; don't-compete-on-price-by-only-confirming-what-they-know; money-follows-big-problems ($4M foot-traffic reframe, $20M raise example); Chris coach, designer=context (Fm7mjeJpyZ4).
- ★ How To Work Less And Make More — LIVE value-based-pricing sales conversation (not just the principle): scripted question sequence to make the client price their own outcome, "half the time = half the revenue as saved value" $150K anchor, Inputs-vs-Outputs vocab (attributed to "Peter Blair" — UNCERTAIN, verify), "10 chunks" week-budgeting, 2-5yr desired-future-state guardrail, delegation = "parachute in for critical thinking only"; client Ron=context, his $200K/$300K/$4M figures self-reported (eU2neFRbFQc).
- ★ 3 Things You Need To Learn In School — (1) public speaking, (2) learning-how-to-learn (incl. formulating questions), (3) logic & reasoning; + school-as-value-exchange, hiring ignores resume/degree (hires on work quality + attitude/potential), find-passion (free-time / age-6-7); Chris subject, interviewer Elanor Jang=context (W4fhcj5e1wQ).
- CONTEXT: Resume Tips — non-Chris lead instructor + co-host Emily; Chris absent; prescriptive pro-resume-artifact stance (distinct from but consistent with the resume-is-dead page); no persona data (KO6zV5C0COc).
- ★ How To Talk To Clients About Money & Budget (Barcelona workshop) — DISTINCT "train of thought" framework: reverse the idiom, sequence a response feeling->thought->reaction (engine=limbic base emotion at front; caboose=reaction most people wrongly lead with); limbic-vs-neocortex rationale + "feeling chart" to pick a constructive base emotion; emotional SEQUENCING (vs other money pages' WHAT-to-say); Chris lead, role-play partner + host Albert de Ville=context (5r5eQzg11MI).
- CONTEXT: Taking Pressure Off Client Presentations — Ben Burns prepping/debriefing an in-person pitch (channels Chris's philosophy 2nd-hand); Chris ABSENT (referenced 3rd person "we're not Christo"); serve-not-prove pre-pitch mindset, willingness-to-walk-away=calm; no persona data (M2Jls1C9pbE).
Attribution: 2 of 6 context (resume instructor + Ben Burns pressure-off); 4 Chris-led ★L3. No family names ("my wife" generic). Counts: L2 274->280. 4 new L3-candidates.
Synthesis notes: NEW — (1) sales-clients/pricing: diagnostic-phase / tell-them-what-they-didn't-know + outcomes-over-craft (money-follows-big-problems) — pairs with value-scale-of-questions + Discovery; (2) pricing: LIVE value-pricing demo mechanics (price-your-own-outcome question sequence, half-time=half-revenue, 10-chunks week) + Inputs-vs-Outputs (verify Peter Blair attribution); (3) mindset/career: "3 things to learn in school" (public speaking / learn-how-to-learn / logic) + hire-on-work-not-resume; (4) sales-clients/voice: "train of thought" emotional sequencing (feeling->thought->reaction, limbic-vs-neocortex, feeling-chart) — strong voice.md + beliefs material. Debt 4/10. Note: strong pricing/value + emotional-sequencing cluster building.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P2 Aug-2018 (tips videos, mostly instructor-led; 5 YouTube tips ★L3)
Batch 41. Ingested 6 @thefutur videos (2018-08-02 → 2018-08-13) to L2. 2 rows on 429 (yt-rJf_gphvDrY, yt-zeSIj5GohoI).
- CONTEXT: Portfolio Submission / Application Tips — led by Greg Gunn + Scott Rothstein (Blind/Futur EP); Chris absent; no persona data (onvdHlv0p-Q).
- CONTEXT: Supercharge Personal Brand via Instagram — unnamed photographer/instructor (refers to Chris 3rd person); Chris absent; no persona data (A7CnmWIPz7o).
- ★ 5 YouTube Tips (from Casey Neistat / Peter McKinnon / Phil DeFranco) — Chris CONFIRMED; his own YouTube/content playbook: strong thumbnails, cold open, on-camera persona/props, a catchphrase, shareability, broad-topic strategy, and the "their fear is our opportunity" content thesis; named creators = context influences (6GMYDlGtHo8).
- CONTEXT (attribution uncertain): Productivity Tips — single unnamed voice-over; self-description fits Chris OR a Futur producer; standard prioritization/time-audit/shared-workspace advice; no persona data extracted (z9ZBn4n1iD8).
- CONTEXT: Kier McLaren MASTERMIND Ep.13 (Overcome Fear) — Chris absent (Kier refers to "Christo" 3rd person; notes "it doesn't occur to him that he can fail"); Kier entity (rYJ-_76rDIM).
- LLC vs Sole Proprietorship (biz-setup series ep.2) — Chris CONFIRMED leads but explicitly disclaims authority ("I'm not an attorney, talk to an attorney"); generic legal/tax how-to, LOW persona value; not L3; coachees Rebecca/Ashley=context (3wckIG_SQA8).
Attribution: HEAVY context batch — the "tips" videos were mostly instructor-led as suspected (Greg Gunn/Scott Rothstein portfolio, unnamed IG instructor, uncertain productivity narrator); only 5-YouTube-Tips confirmed Chris + ★L3; LLC Chris-led but generic. Kier mastermind now Eps 1-13 (5 skipped), all context. No family names. Counts: L2 280->286. 1 new L3-candidate.
Synthesis notes: NEW — (1) content-strategy: Chris's own YouTube/CONTENT PLAYBOOK (thumbnails, cold-open, persona/props, catchphrase, shareability, broad-topic, "their fear is our opportunity") — strong content-strategy + voice material; explicitly cites Casey Neistat / Peter McKinnon / Phil DeFranco as his creator influences (entity candidates). Otherwise a thin, instructor-heavy batch (5 of 6 context or generic). Debt 5/10 (halfway to checkpoint). Note: many @thefutur "tips/how-to" uploads in this era are instructor-led — attribution vigilance essential.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 Aug-2018 (choose-clients, superpower; Brian Collins; +1 skipped)
Batch 42. Ingested 7 @thefutur videos (2018-06-27 backfill + 2018-08-15 → 2018-08-30) to L2. **Marked 1 long-stuck row SKIPPED**: yt-zeSIj5GohoI "Why Confidence Is More Vital Than Your Work" (429/unavailable 5+ batches; confidence theme well-covered by be-a-mirror/Mirrormask pages).
- CONTEXT: 4 Video Production Hacks — Futur crew Aaron & Mark; Chris absent (rJf_gphvDrY).
- CONTEXT: 3 Minutes of Branding Gold by Brian Collins — ~100% Brian Collins (COLLINS agency, brand-design INFLUENCE); Chris absent; entity material (familiarity/surprise/context model, "poetry as strategy", "provoke love or hate never indifference", anticipation via Ray Eames) (bgStKKE6RUk).
- Futur Office Tour (Casey Neistat 368) — ~70% studio-tour vlog; mission-framing likely-Chris but attribution:uncertain (The Futur = "digital design dojo" disrupting education, ~300%/yr growth, "it's what's inside that counts"); team (Bender/Matthew/Stewart)=context; not L3 (g2xE2wkWIV4).
- ★ Choose Your Clients Wisely — proactive front-end client SELECTION (vs fire-your-clients' removal); strategist reframe: don't wish clients communicated better, BECOME the better communicator/strategist (car-at-mechanic analogy; "the more I reveal to a client what they don't know, the more valuable I become"); guest Henry Kaminsky Jr (brand consultant)=context; good-client-criteria list attribution:uncertain (wzPPi2mX-ho).
- ★ Finding Your Super Power — fullest "superpower" framework: 5-prompt inventory (skill / happiness / opportunity / passion / service to others), ikigai-adjacent Venn diagnosis ("rich but bored", "happy but poor", "just a dream") + build-matrix (educational model / physical product / app-website); Chris subject, Danny Yount panel clip=context; wife's advice redacted (VhztaSc4afE).
- CONTEXT: Dr. Holtzman Pt.2 (Heineken "Beyond the Brief") — guest expert; "decode the brief" (client intent behind literal words; "bottle every 5 sec" = iconic-repetitive spine not literal) + step-out-of-your-own-shoes empathy ("design a pair of shoes for them") = Holtzman's; Chris intro-framing only; Holtzman entity (6GodcTLloaw).
- CONTEXT: Kier McLaren MASTERMIND Ep.18 (Reach Out / get a meeting) — Chris absent (3rd person); get-a-meeting-not-a-job, honest self-assessment, creative human outreach, lead-with-a-solution; Joe Montalbano ice-cream door-opener; Kier entity (XtCWo340xDo).
Attribution: 5 of 7 context (Brian Collins + Holtzman + Kier + video-crew + office-tour-uncertain); 2 Chris-led ★L3. No family names (wife's advice redacted). Counts: L2 286->293 (+7); 1 skipped (no-captions). 2 new L3-candidates.
Synthesis notes: NEW — (1) sales-clients/business: proactive client SELECTION + strategist reframe ("become the better communicator", reveal-what-they-dont-know = more valuable) — distinct from fire-your-clients (removal); pairs with diagnostic-phase + value-scale; (2) mindset/branding: "find your superpower" 5-prompt inventory (skill/happiness/opportunity/passion/service, ikigai-adjacent) + build-matrix — strong beliefs.md material. ENTITY debt grows (influence network): Brian Collins/COLLINS, Danny Yount, Dr. Holtzman (Pt.1+2), Casey Neistat/Peter McKinnon/Phil DeFranco (creator influences), Henry Kaminsky Jr (guest) — plus the existing Kyle Cooper/Karin Fong/Kier. Consider an "influences" cluster at the next checkpoint. Debt 6/10.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 Sep-2018 (chunking-goals, success-leaves-clues, give-away; L2=301)
Batch 43. Ingested 8 @thefutur videos (2018-08-31 → 2018-09-11) to L2. **Milestone: L2 crossed 300 → 301.** Full batch, no 429s.
- CONTEXT: How to Build Websites in Hours — Webflow tutorial by guest Ron Segal (Flux/Prospero); Chris host only; no persona data; Ron-Segal entity reinforced (XsF5YQq7M1A).
- CONTEXT: Kier McLaren MASTERMIND Ep.19 (traits of successful people) — Chris absent; Kier bio: worked at Prologue UNDER KYLE COOPER (connects to kyle-cooper entity); Kier's 3rd-party notes corroborate single Emmy + The Futur took ~3yrs/many failed attempts + Chris was 40+ (AHJcwllsKA4).
- CONTEXT: Kier MASTERMIND Ep.20 (clients who don't know what they want) — Chris absent; Kier ran a New England ad agency; cites Getting-to-Yes / BATNA; Kier entity (dVkyDxbr12I).
- Focus vs Generalist — specialize-as-job-security-insurance, "chasing your tail" warning, strengths-first-then-supplement; restates the specialist/inch-wide-mile-deep stance; a 2nd unnamed host (Sinek why-over-what)=context; not L3 (w5ti6BW8foo).
- What Motivates You — thank-you-economy / reciprocation (Cialdini), #10% work-ethic, the $14.68-check anecdote; Chris solo; not L3 (restatement) but good voice material (mbVjjeH6-tk).
- ★ How To Make Clear Goals You Can Achieve — names "CHUNKING" (chop a big goal into a bite-sized piece + marshal all energy at it) + a live vague-to-specific quantitative drill-down (financial security -> $10k/mo -> $120k/yr -> client-mix math 1x10k vs 2x5k vs 10x1k) + "think/clarity first, tactical work last, don't go squirrel" + SMART trimmed to 3 (specific/measurable/time-bound); Chris coach, guest Ryan=context (4ZnSvCxqTrk).
- Why Do I Give So Much Away (My Content Strategy) — stop-selling (audiences hypersensitive to selling -> credibility/authenticity out the door), "KARMIC EQUITY" label for give-and-reciprocate; self-reported 2018 proof: 300% YoY growth, 4th year, 517 members @ $5/mo; Chris solo; feeds give-first pages (not L3, short) (V-uLjNG73ho).
- ★ Success Leaves Clues — learn-by-modeling / study-successful-people (studied comedians etc.) + his introvert-who-forced-change narrative; Chris solo; foundational recurring trait (Xi3VhHp8llI).
Attribution: 3 of 8 context (Ron Segal + 2 Kier); 2 Chris-led ★L3; 3 Chris-led restatements. No family names. Counts: L2 293->301. 2 new L3-candidates.
Synthesis notes: NEW — (1) mindset: "chunking" goal-setting (chop-to-bite-size + marshal-all-energy, vague-to-specific numeric drill-down, think-first-tactical-last) — pairs with fuzzy-goals + goal-setting; (2) mindset: "success leaves clues" learn-by-modeling framework (foundational trait, ties to existing voice.md learn-by-modeling); (3) content-strategy: "karmic equity" / stop-selling give-first label + 2018 proof-numbers (517 members @$5/mo, 300%/yr) — feeds give-first pages; (4) mindset: specialize-as-job-insurance angle. BIO corroboration (via Kier, context): single Emmy confirmed, Futur format took ~3yrs. ENTITY: Kier<->Kyle Cooper link (both at Prologue) strengthens the influence graph; Ron Segal reappears. Debt 7/10 — checkpoint ~3 batches out.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 Sep-2018 (true-self, getting-to-yes, rapport; sales cluster)
Batch 44. Ingested 8 @thefutur videos (2018-09-13 → 2018-09-25) to L2. Full batch, no 429s.
- ★ Your True Self Is A Full Spectrum — prism/full-spectrum authentic-identity model (true self = white light diffracted into many contextual faces; "I haven't changed, I've shown you more of me"); Chris, DJ Mike (guest question)=context (SAXRxpiJqcE).
- CONTEXT: Wax Seal Logo Mockup (Photoshop) — Emily-led tool tutorial; Chris interviewer only (2 minor conceptual asides); low persona value (3i-jz-6Xu8U).
- How To Make Your Idea Happen — "invert the pyramid" (prototype -> crowdfund -> validate -> then engineer; credited to a Google Labs design director); Chris solo, coachees=context; not L3 (short) (8he7nM4W1vw).
- CONTEXT: Day-in-Life "Presentation FAIL" VLOG — Matthew Encina's SIGGRAPH/MAXON-booth day; Chris absent; no persona data (V1YsOVSSNcE).
- ★ Getting Clients to YES — empathy-first; get the client to state the ask in their own words, then mirror it back; the "three outcomes" model; de-risk via phased engagement / meet-the-owner; Chris coaching a live ~$50k client objection, coachee=context (F7olfui5Igw).
- ★ How To Build Rapport (Lose the Small Talk, Ask Big Questions) — reveal-first reciprocity (share first -> prospect shares goals/finances back), "make big talk"/bigger questions, curiosity + listening posture; Chris, interviewer=context (YKZ1TSZZ5XM).
- How to Pitch to Potential Clients (post-pitch debrief) — contextual framing (pitch each idea against the client's stated challenges/goals), engineer client ownership/collaboration, incubation ("an hour to build but a week of thinking"), pitch objectively so you don't need the client to gush, confidence-vs-desperation; Chris solo; reinforces the Pitch-This doctrine, not L3 (i7O4AtfeM6k).
- CONTEXT: Monoline Logo (Illustrator) — tool tutorial (pen/guides/anchor-averaging); attribution uncertain (a "Molly" addressed); no persona data (59RisFrQZY4).
Attribution: 3 of 8 context (Emily Photoshop, Matthew Encina day-in-life, monoline-uncertain); 3 Chris-led ★L3; 2 Chris restatements. No family names. Counts: L2 301->309. 3 new L3-candidates.
Synthesis notes: NEW — (1) mindset/branding: "full spectrum / prism" authentic-identity model ("I haven't changed, I've shown you more of me") — strong beliefs.md + personal-brand material; (2) sales-clients: getting-to-YES framework (empathy-first, state-then-mirror the ask, three-outcomes, phased de-risking) + build-rapport via reveal-first reciprocity + "make big talk"/bigger-questions — strong sales-clients cluster (pairs with don't-convince, diagnostic-phase, train-of-thought); (3) mindset: "invert the pyramid" idea-validation (prototype-first). ENTITY: Matthew Encina + Emily (Futur instructors, already covered). Debt 8/10 — checkpoint ~2 batches out. Note: the sales-clients ★L3 cluster (getting-to-yes, rapport, choose-clients, don't-convince, diagnostic) is now very strong for the next synthesis pass.

## [2026-07-17] ingest | yt batch (@thefutur, 8) — P2 Sep–Oct-2018 (price-options, personal-projects, imposter-comparison)
Batch 45. Ingested 8 @thefutur videos (2018-09-26 → 2018-10-10) to L2. Full batch, no 429s. P2 open now <800.
- Avoid Clients Who Waste Your Time — earliest red-flags (talking-past-each-other/didn't-read-your-email, "just want to pick your brain"=validation-not-advice, bad-listener-ignores-pushback) + "dinner test" heuristic ("I only work with people I'd like to have dinner with"); Chris solo; refines client-selection, not L3 (15nLfcQxMSQ).
- 1 Simple Tip to Make Logos More Valuable — place logos in real-world context/mockups to raise perceived value; Chris solo; minor (uO8VUYwCmFM).
- CONTEXT: Get More Views / "Define the Gap" — Ricky (Futur videographer, his first solo video); Chris absent; McKee-esque beats/gaps story structure; Casey Neistat example (aBz0fSkCG4Y).
- ★ Pricing Strategies: Give Your Client Price Options — 3 tiers differentiated by CHRIS'S ATTENTION/OWNERSHIP/probability-of-success (NOT labor/deliverable-count); price-first then invent-scope; inverse-client-effort (higher tier = Chris takes more ownership, needs LESS from client); tier ladder bottom=DIY-diagnose/roadmap, middle=collaboration, top=full-ownership; enriches pricing-hub 3-options (M18yO7BYRNE).
- Starting Your Business: Budget vs Profit — deposits, cash-flow, revenue-vs-profit primer; Chris solo; generic, not L3 (Jx9-pOPCv1Y).
- ★ Personal Projects After a Full-Time Job — "what are you willing to give up?" sacrifice/trade model, convert-knowledge/experience-into-equity (Jim Rohn), "growth is the reward not the destination", small-commitments/just-start (Terry Crews gym anecdote), blend-work-and-play; coachees=context. SELF-REPORTED bio to VERIFY (logged in gaps.md): founded Blind by 22, "$2M billings in first two years" (kKLZYk6t7A8).
- CONTEXT: 3 Editing Tips — unnamed Futur editor (recent film grad); Chris absent; no persona data (1m7CVb3LqQw).
- ★ How To Not Feel Like An Imposter When Comparing Yourself — "selective filter" (only admit inputs that help you grow, discard the rest), "knowledge vampire" (extract what successful people do well = compare-to-learn not compare-to-measure-worth), "comparison is the thief of joy" (passed-on quote), Anthony Bourdain curated-lives proof, $30k sales-contract adversity-reframe (take responsibility, extract lesson, move on); Connor(coachee)=context (-yUgbMowG3w).
Attribution: 2 of 8 context (Ricky + editor); 3 Chris-led ★L3; 3 Chris restatements. No family names ("my dad/wife/children" unnamed). Counts: L2 309->317. 3 new L3-candidates. gaps.md: added verify item for self-reported early-Blind financials.
Synthesis notes: NEW — (1) pricing: three-price-options differentiated by ATTENTION/OWNERSHIP (not labor) + price-first-scope-after + inverse-client-effort — distinct enrichment for the pricing-hub 3-options section; (2) mindset: sacrifice/trade "what will you give up" + knowledge-to-equity + just-start (personal-projects) — beliefs.md; (3) mindset: comparison/imposter — "selective filter" + "knowledge vampire" (compare-to-learn) + adversity-reframe — distinct devices beyond the existing imposter pages. BIO: verify early-Blind financials (gaps.md). Debt 9/10 — SYNTHESIS CHECKPOINT DUE NEXT ITERATION. Large sales-clients + mindset + pricing ★L3 backlog (getting-to-yes, rapport, choose-clients, don't-convince, diagnostic, price-options, superpower, chunking, success-leaves-clues, full-spectrum, comparison) ready to promote; + influence-entity cluster (Brian Collins, Danny Yount, Holtzman, creator-influences).

## [2026-07-17] lint | synthesis pass 5 — P2 2018 mid/late era (batches 37–45) → persona v6 + 3 influence entity pages
Stage S synthesis checkpoint (debt 10/10). Promoted the batch 37–45 ★L3 backlog (~66 L2 pages, L2 256→317) into 6 topic hubs + persona; recompiled system-prompt v5→v6 (compiled_from 256→317); CREATED 3 entity pages. 13-agent fan-out (one file each) + system-prompt recompile.
Topic hubs enriched:
- sales-clients 22→30: fire/resign-client (refund+pay-to-leave, reject exposure-pay), don't-convince (skipped meeting-of-minds), Objection Response Deck (acknowledge/answer-with-question/degree/reflect + energy-to-neutral, Blair Enns), diagnostic-phase/outcomes-over-craft, proactive-selection/strategist-reframe (become-better-communicator), getting-to-yes (state-then-mirror, three-outcomes, phased-de-risk), build-rapport (reveal-first reciprocity, make-big-talk), avoid-time-wasters (dinner-test).
- pricing 18→21: live value-pricing demo (price-your-own-outcome, half-time=half-revenue, inputs-vs-outputs [Peter Blair flagged=likely garbled Blair Enns]), "train of thought" emotional sequencing (feeling->thought->reaction, limbic-vs-neocortex), three-options-by-attention/ownership (not labor, price-first-scope-after, inverse-client-effort).
- mindset 24→30: fuzzy-goals + chunking, full-spectrum/prism self, comparison-as-tool (selective-filter/knowledge-vampire), find-your-superpower (5-prompt inventory + ikigai + build-matrix), sacrifice-trade (knowledge->equity), education/internship value-exchange (3-things-in-school); "success leaves clues" folded into existing learn-by-modeling section.
- design-craft 19→21: expressive typography (type-enacts-message, letter-spacing=emotion), logo-value-via-mockups.
- business 15→17: maker-vs-entrepreneur / CEO-shift (making-a-difference-vs-making-things + scaling mechanism), codify-process-into-<=5-steps + quality-threshold, student-debt critique (schools=loan officers).
- content-strategy 16→17: Chris's YouTube playbook (thumbnails/cold-open/persona/catchphrase/shareability + "their fear is our opportunity"), "karmic equity"/stop-selling give-first (2018 proof: 517 members @$5/mo, self-reported).
Persona: beliefs +15 dated (~48->~63 entries, sources 48->69); voice +~11 catchphrases (sources 32->41) + traits (dinner-test, full-spectrum, their-fear-is-our-opportunity, karmic-equity, make-big-talk, success-leaves-clues); biography +4 fact-clusters (18-19 turning point; ArtCenter years all-nighters/Bruce-Hubbard-D-grade/financial-reality-debunks-rich-kid-myth; Epitaph->Novacom->first-Buick-commercial origin; maker->CEO ~1996; sources 22->25). system-prompt v6.
NEW ENTITY PAGES (CONTEXT banners, wikilink-cited): wiki/entities/danny-yount.md (title-design influence, Emmy Six Feet Under, Digital Kitchen->Prologue->Prodigal Pictures), wiki/entities/brian-collins.md (brand-design influence, COLLINS, "poetry as strategy"), wiki/entities/influences.md (INDEX of the whole influence network — title-design mentors, brand authorities, creator influences [Neistat/McKinnon/DeFranco], guest experts [Holtzman/Kaminsky/Manos/Segall], cited thinkers [Rohn/Tracy/Enns/Sinek/Pink/Cialdini], Kier McLaren).
Governance: family names kept out of every file; military/Army NOT propagated; single-Emmy preserved (2018 Kier context corroborates SINGLE Emmy); "$2M billings/founded-by-22" left as gaps.md verify item (NOT asserted). Attribution: guests fenced (Henry Kaminsky Jr, Danny Yount); date-precedence callouts added; "Peter Blair" flagged likely-Blair-Enns. High-water mark advanced to batch 45. Resume ingest (Stage B, P2 late-2018) next iteration.

## [2026-07-17] ingest | yt batch (@thefutur, 6) — P2 Oct-2018 (bracketing-anchoring, charging-too-little; Johnny Cupcakes)
Batch 46 (first ingest after synthesis pass 5). Ingested 6 @thefutur videos (2018-10-12 → 2018-10-25) to L2. 1 row on 429 (yt-EkHAQQjhl90).
- How to Position Yourself as an Expert w/o Experience — age/pedigree invisible online -> "do good work IS the positioning"; internal self-worth conviction; get-known-for-one-thing-then-flip; vulnerability/grow-together for young creators; Chris, coachees=context; not L3 (noted for synthesis) (E4oDHKVYOSk).
- ★ How to Talk About Price Using Price Bracketing — 2018 REFINEMENT of the 2017 bracketing page: LAW OF ANCHORING = say the BIGGER number FIRST (reverse the bracket, "300 and 150"), verbal-upfront-pricing (before you show/build a bid), sonar/echolocation metaphor for reading budget reaction, "address resistance in the moment don't build a bid"; Chris=vendor role-play, Joe=coachee/context (87CPZdh6FIc).
- CONTEXT: Johnny Cupcakes (Johnny Earle) 12 branding tips — ~90% guest; experiential packaging (limited-edition Chinese-takeout box), story-first, "12 things that separate you"; Chris interviewer only (framing + storytelling-experience reflection); Johnny-Cupcakes entity candidate (7UCv0mj8Uc8).
- CONTEXT: Jurassic Park Poster / "The One-Sheet" — hosted by Stuart Schuster (film) + Ben Burns (design); Chris ABSENT (named only as the greenlighter); poster composition, symmetry-as-conflict, meta-branding (0GDdLY4nLuA).
- ★ You're Charging Too Little / Why You're Angry When Clients Call — landmark underpricing-SIGNAL framework: the dread/resentment/irritation you feel when a client calls means you charged too little; Chris explicitly credits Blair Enns / Win Without Pitching (endorsing, not original); Chris solo (yoGvz6lvTfQ).
- Ask More Questions Until Clear — "foreign idea = invader into our brain" psychology (people resist externally-supplied ideas -> reflect questions back), "I don't sell you my idea, I sell you your idea" / hold-a-mirror-up, clarity->pricing bridge ("is it a problem worth solving?" -> "what's that worth?"); Chris solo; restatement, not L3 (-cuy994Fs64).
Attribution: 2 of 6 context (Johnny Cupcakes guest, Jurassic Park = Schuster/Burns Chris-absent); 2 Chris-led ★L3; 2 Chris restatements. No family names. Counts: L2 317->323. 2 new L3-candidates.
Synthesis notes: NEW — (1) pricing: bracketing ANCHORING-REVERSAL (say bigger number first) + verbal-upfront-pricing — distinct refinement of the 2017 bracketing page; (2) pricing/mindset: underpricing-SIGNAL (resentment/dread on client call = charged too little; Blair Enns) — strong pricing + beliefs; (3) sales-clients: "I sell you your idea" / foreign-idea-as-invader (reflect-questions-back psychology) + clarity->pricing bridge; (4) branding/positioning: do-good-work-IS-positioning + get-known-for-one-thing-then-flip (position-as-expert, noted). ENTITY: + Johnny Cupcakes / Johnny Earle (brand founder influence — add to influences index at next checkpoint). Debt 1/10.

## [2026-07-17] ingest | yt batch (@thefutur, 5) — P2 Oct–Nov-2018 (two-budget-approaches, get-more-clients-challenge)
Batch 47. Ingested 5 @thefutur videos (2018-10-26 → 2018-11-02) to L2. 1 row on 429 (yt-EkHAQQjhl90).
- Adobe MAX 2018 recap — sponsored/promo event vlog; Chris's persona-relevant thread = "focus on fundamentals not tools" + creative-tool democratization + "learn to tell your story to stand out"; Ben Burns/Matthew segments=context; not L3 (tkk6yXM2T90).
- Sell Services Without Experience — ranked "what NOT to sell" hierarchy: portfolio (#1 mistake), process (#2); instead sell the PEOPLE, reframe the sale toward identity + confidence; Chris solo; distinct from position-as-expert (no-portfolio starting position); not L3 (short) (RIVGm5E6KsE).
- ★ Two Approaches To Talking About Budget — "two lenses" both rejecting budget-first: (1) emotion/relationship-led (guest Shannon Gabor, CEO of Clever Creative = CONTEXT: "what does success look like," budget-first signals chasing-the-check); (2) logic-led (Chris: rejects transaction frame despite being logical; relationship must be TWO-WAY good-for-client-AND-sustainable-for-team; going transactional early = order-taker not trusted-advisor); + diagnostic: low-ball/bottom-feeder calls = a POSITIONING/marketing problem, not a pricing one (DDBWERuvgFA).
- ★ How To Get More Clients (Challenge) — named lead-gen framework: the "reach out to 30 new people in one week" challenge (Jim Rohn); 2-target outreach taxonomy = "bigger fish" (larger agencies who refer out their misfit/small leads) + "fringe service providers" (adjacent non-competing creatives for network-building); anchors the recurring "Commute Challenge" format; Chris solo (iWDoF1pJfGY).
- Communicate What You Do (1-min tip) — reframe from self-description to CUSTOMER VALUE: profile your customers (ad agencies/entrepreneurs/startups), find the pain-points you solve, build messaging/mission from that; Chris solo; not L3 (qTtEPQP6vSM).
Attribution: 1 interview w/ guest Shannon Gabor (context); Adobe MAX multi-narrator (Ben Burns/Matthew=context); 3 Chris-solo. 2 Chris-led ★L3. No family names. Counts: L2 323->328. 2 new L3-candidates.
Synthesis notes: NEW — (1) pricing/sales-clients: "two approaches to budget" (emotion-led vs logic-led, both reject-budget-first) + relationship-must-be-two-way + low-ball-calls=positioning-problem-not-pricing — enriches money-conversation/discovery; (2) sales-clients/content-strategy: "30-outreach challenge" lead-gen + bigger-fish/fringe-creatives outreach taxonomy (Commute Challenge format); (3) branding/positioning: sell-people-not-portfolio + communicate-via-customer-value/pain-points (2 restatements, feed positioning). ENTITY: + Shannon Gabor / Clever Creative (guest, agency founder). Debt 2/10.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 Nov-2018 (Blind-reinvention BIOGRAPHY, positioning-value, Melinda deep-dive)
Batch 48. Ingested 7 @thefutur videos (2018-11-08 → 2018-11-22) to L2. 1 row on 429 (yt-EkHAQQjhl90).
- Manage Time Better (Commute Challenge) — track 2 days in 15-min increments in a spreadsheet; email = his biggest time-sink (self-reported); Chris solo; not L3 (0IPDtWmYWVg).
- ★ How Strategy Changed My Design Business — **MAJOR BIOGRAPHY SOURCE**: Blind's near-collapse & reinvention, first-person + dated. Blind = motion-design firm founded 1995, run 23 yrs, 1702 Olympic Santa Monica; clients Coldplay/Sting/Xbox; ~$7M peak revenue 2007 [self-reported], decline as audiences left TV for social; 2013 = "big inflection point"; failed pivots (explainer/corporate video couldn't go below $150k; a $5k web project via his older brother); "strategic divide" (seen as vendor not consultant) -> nearly gave up; learned strategy from JOSE CABALLER -> adopted CORE framework; first strategy-led job Trojan Storage (Jose led), first solo CORE = Oles (fishing resort); motion-design -> branding consultancy, "paid for making -> paid to think", reversed a 20-yr decline in ~2 yrs. Co-presenter Matthew (Blind CD)=context (yevZjd-YwUY).
- ★ How Positioning Increases Value — value = the max someone is willing to pay; Rolex-vs-Timex commodity contrast; hourly-billing = self-commoditization; become the go-to person; Chris (speaker-id uncertain but textbook Chris/Futur) (ODcdMUgsxMI).
- NOT SUBJECT: How to Deal With a Client / Direction Changes — scripted role-play, teaching role addressed as "Matthew" + Futur-Freelance-Fridays outro = Matthew Encina (context); re-anchor-on-goals, don't-judge-the-sketch, make-deadline-tradeoff-explicit, convert-to-change-order/overage (~$2-2.5k), "I need time to process"; NO persona data (P7qZd8_gdTI).
- CONTEXT: What is UX Design — unidentified UX instructor (not Chris); no persona data (nV1I_098dzg).
- CONTEXT: Micro-content Videos — Mark Contas (Futur video team); keep-on-topic/feed-metadata/mobile-sound-off (85% Facebook silent-view); Chris absent; no persona data (JZQ_NZJApH8).
- ★ Identity Design -> Brand Strategy Deep Dive w/ Melinda Livsey Ep.12 — Chris COACHES Melinda (context); dense cluster: questionnaire->strategy-workshop, order-taker-vs-consultant, cold-vs-hot leads, symptom-vs-root-cause (rash/carrots), knowledge->capital/equity, Dan Sullivan 3-year question, lifestyle-vs-bigger-mission; CAVEAT: the actual identity->brand-strategy transition is Melinda's story, deferred to another ep; son(12)/wife referenced generically (3el7kOfTPK4).
Attribution: 3 of 7 context (Matthew-Encina role-play NOT-subject, UX instructor, Mark Contas micro-content); 3 Chris-led ★L3; Melinda fenced as coachee. No family names (older-brother/son/wife generic). Counts: L2 328->335. 3 new L3-candidates.
Synthesis notes: NEW — (1) **BIOGRAPHY (major)**: Blind reinvention arc (1995 founding, ~$7M peak 2007, 2013 inflection, motion->branding pivot via CORE learned from Jose Caballer, first jobs Trojan Storage/Oles, 1702 Olympic Santa Monica; financials self-reported) -> promote to biography.md + Blind entity + Jose Caballer entity at next checkpoint; (2) branding/pricing: positioning-increases-value (value=max-willingness-to-pay, Rolex-vs-Timex, hourly=commoditization, become-go-to-person) — strong branding+pricing+beliefs; (3) branding/business: identity-vs-brand-strategy + order-taker-vs-consultant + symptom-vs-root-cause + Dan Sullivan 3-yr question (Melinda deep-dive). ENTITY: + Mark Contas, Shannon Gabor already noted; the CORE framework + Jose Caballer link deepened. Debt 3/10.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 Nov–Dec-2018 (culture, subconscious-ideation, take-responsibility biography)
Batch 49. Ingested 7 @thefutur videos (2018-11-22 → 2018-12-05) to L2. 1 row on 429 (yt-EkHAQQjhl90).
- CONTEXT: UX Design Process (first questions) — non-Chris UX instructor (refers to Ben Burns 3rd person); user-archetypes/senses framework; Chris absent (RjzyZeZo5ZU).
- ★ Company Culture — culture-as-COMPETITIVE-ADVANTAGE: candidates weigh 4 things (pay / work quality / treatment / project-management); a startup can't win on price or work-quality so compete on the two you control (treatment + management); burnout-via-project-selection (accepting under-timed/oversized jobs forces all-nighters -> leader's job is to minimize those); Chris, coachee=context (xefSymuwzzI).
- Monoline M Lettering (Illustrator) — Chris CONFIRMED (not an instructor; drives the tool, off-camera co-host banters); optical-correction-over-mathematical-correctness; live-improv/self-deprecating teaching manner (voice); low persona value (tool); not L3 (SPmqQb7AaME).
- What Would You Do Differently — BIO nuggets: would NOT have a business partner (candid regret; reconcile w/ Blind partnership history), past fear-of-being-on-camera he overcame, The Futur is a real team/studio; "feast with gun turrets, barbed wire, and a moat with man-eating fish" competition metaphor (strong voice); Chris solo; not L3 (short) (MdxqVGLaLYg).
- CONTEXT: Joey Cofone (Baron Fig) Pt.2/2 — ~90% Joey (co-founder, notebook brand, founded 2013 NYC, Kickstarter, employee-owned); "point don't plan", mini-vacations, 5:30-start routine; Chris framing only (praises balance-first as breath-of-fresh-air vs grind; possible Baron Fig collab); Joey-Cofone/Baron-Fig entity (apuUYmUGKP0).
- ★ Unlock Your Subconscious (Better Ideas) — his 20+yr DELIBERATE-INCUBATION ideation framework: reduce problem to 2-3 very specific keywords -> saturate the brain w/ tangential stimuli (art/music/literature/philosophy) filtered through those words -> DELIBERATELY STOP and SLEEP ("subconscious is much smarter than my conscious brain") -> ideas surface in autonomic low-effort states (shower/walk/run) -> capture immediately ("ideas are like cotton candy"); clarity phase DOUBLES as client-onboarding (co-author the answer so they've already bought in); Chris solo (nhUupKOj8I4).
- ★ Take Full Responsibility / Against Parents' Wishes — landmark self-responsibility framework + RICH BIOGRAPHY: parents not fully supportive of him becoming a designer (father opposed, mother shielded him, learned "much later"); attended ArtCenter ("expensive as Stanford"); rejected from UCLA/UC-San-Diego/Cal-Poly (poor grades/lack of focus), art school his only acceptance; self-funded (work-a-semester/odd-jobs); "hundreds of cousins" many high-achievers (Stanford/UCLA/doctors/lawyers), he's the "black sheep" designer they now go to for advice; father of two boys, parenting-mission = design a life so they don't need him; FAMILY NAMES CLEAN (my mom/dad/two boys only) (mruxbUxEUS4).
Attribution: 2 of 7 context (UX instructor, Joey Cofone guest); 3 Chris-led ★L3; 2 Chris solo (biography/tool). No family names. Counts: L2 335->342. 3 new L3-candidates.
Synthesis notes: NEW — (1) business/mindset: culture-as-competitive-advantage (compete on treatment+management) + burnout-via-project-selection — distinct culture framework; (2) design-craft/mindset: DELIBERATE-INCUBATION ideation (2-3 keywords -> saturate -> sleep -> capture; subconscious smarter than conscious) — strong design-craft + beliefs, distinct from art-of-search; (3) BIOGRAPHY (rich): parents-not-supportive/black-sheep origin + ArtCenter-only-acceptance/rejected-from-UC-schools/self-funded (corroborates & deepens the 2018-06-26 ArtCenter source) + would-not-have-a-business-partner regret + camera-fear -> promote to biography.md at next checkpoint. ENTITY: + Joey Cofone / Baron Fig (guest). Debt 4/10. Note: biography backlog growing (Blind-reinvention arc from batch 48 + this parents/ArtCenter material) — strong biography enrichment for the next synthesis pass.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 Dec-2018 (attract-ideal-client, document-delegate-automate, get-a-mentor)
Batch 50 (milestone batch #50). Ingested 7 @thefutur videos (2018-12-10 → 2018-12-20) to L2. 1 row on 429 (yt-EkHAQQjhl90).
- CONTEXT: "Will AI Take MY Job?" — guest interview whose substantive answers are SETH GODIN's (Linchpin, "the work vs the job", competence-is-overrated, school-as-factory / Stop Stealing Dreams; inferred - transcript has no speaker labels); Chris = interviewer only (3 framing questions); Seth-Godin entity candidate; NOT persona (8mzKkbZUnRA).
- ★ Attract Ideal Client via Content Marketing (Melinda Livsey Ep.13) — landmark content-marketing philosophy: write for a PREVIOUS version of yourself, give your best advice away free (rank organically + build trust), creatives-become-champions who carry you up to decision-makers, community-over-competition (that exact phrase = Melinda's), momentum-over-plans, make-small-bets/read-feedback/adapt; Chris coaches Melinda=context; son(12) redacted (37gKuNp-XLw).
- How to Apply What You Learn — consume->convert->share, don't-be-a-learning-hoarder, distill-when-you-teach; Chris solo; not L3 (restatement) (nI5NmyTtyu4).
- Creative Process Documenting Challenge — externally document your tacit process at max granularity = the PRECURSOR to codify-into-steps + better-delegation + explain-to-clients; micro+macro task pairing; "creatives don't perceive their work as systems"; renamed Coffee Challenge (#futurchallenge); Chris solo; not L3 (setup ep) (DxvKsid8trg).
- Pros/Cons Design Business From Home — distributed-teams, remote-hiring, cost-of-living-arbitrage, "fluid model"; Chris solo; generic, not L3 (7bDassY8uP0).
- ★ Document Delegate Automate — process-documentation MECHANICS: 2 audiences (clients vs team), 6-point how-to (start-now/simple/clear/visual/right-tool/shareable), medium-agnostic (typed+screenshots OR video OR public YouTube), Notion-team-wiki + public-YouTube-training stack, real ROI (saved 1-2hrs, avoided remote bottleneck); "2 ways to grow: raise price OR sell more" -> delegation mandatory; Matthew(context: give-them-context/end-result-first recipe)/Jonah=context (I09EDxElu3o).
- ★ How to Get a Mentor — tactical "make the ask": value-exchange (their time for your value), ask SMALL (15min not 1hr, goal=a-yes), scaffolding (start tiny, trade up like a ladder), get-inside-their-head + give 2-5x value, don't-assume-what-they-value (offer+let-them-choose); live role-play; complements the 2018-07-02 "level-up-to-close-the-gap" (this = how-to-make-the-request half); Chris, students=context (3PMB0emL7RY).
Attribution: 1 guest (Seth Godin, correctly quarantined - his ideas NOT Chris's); Melinda + team members (Matthew/Jonah/students) fenced; 5 Chris-led (3 ★L3). No family names (son-12 redacted). Counts: L2 342->349. 3 new L3-candidates.
Synthesis notes: NEW — (1) content-strategy: attract-ideal-client via content (write-for-previous-you, give-best-advice-free, creatives-as-champions, community-over-competition, momentum-over-plans) — landmark, promote to content-strategy + beliefs; (2) business/scaling: document->delegate->automate MECHANICS (2 audiences, 6-point how-to, Notion+YouTube stack) + document-tacit-process precursor — enriches codify-into-steps/delegation cluster; (3) sales-clients/mindset: how-to-get-a-mentor (value-exchange, ask-small, scaffolding, give-2-5x) — pairs with level-up-to-close-gap. ENTITY: + Seth Godin (guest thinker, was the "Will AI" interview subject; author Linchpin/Stop-Stealing-Dreams - candidate for a context page if he recurs) + Joey Cofone (batch 49) + Shannon Gabor (batch 47). Debt 5/10 (halfway to checkpoint). Biography backlog (Blind-reinvention + parents/ArtCenter) still queued.

## [2026-07-17] ingest | yt batch (@thefutur, 7) — P2 Dec-2018→Jan-2019 (long-vs-short-goals, stop-hourly, 5-things-sales-call)
Batch 51 (final batch of this session — user requested stop after this run). Ingested 7 @thefutur videos (2018-10-15 backfill + 2018-12-26 → 2019-01-14) to L2. Crosses into 2019. 1 row on 429 (yt-og6-CKoM5Lk). Prior persistent-429 (EkHAQQjhl90) cleared.
- ★ Mindset Shift: Long vs Short Term Goals — dense signature-mindset cluster (BIO/voice): rock-bottom -> identity-decision, delayed-gratification/long-term focus, "addicted to success", out-hustle-over-talent, internal-only-celebration, emotional-detachment/Spock, daily-gratitude "life hack"; Chris, coachees(Connor/Aaron)=context (EkHAQQjhl90).
- ★ Stop Charging Hourly (roleplay) — Socratic-flip ("why do you want my hourly rate?"), symmetry-of-logic (can't cap AND count hours; fewer-hours=less so more-hours=more), "charging hourly punishes me for being good", value-appreciates-over-time ("$18k today, come back in a year, it'll be 26"); Chris=designer, Jung(coachee)=context (jE53O1PzmNU).
- CONTEXT-mixed: Top 10 Tips 2018 best-of compilation — multiple speakers (Chris + instructors Jonathan Stark/Sagi Haviv?/Brian Collins + guests), captions no speaker labels -> per-clip attribution, uncertain clips kept OUT of persona; 2 strong Chris segments flagged (retreat-and-follow; value=quality-of-questions); not L3 (8HRoeBG6YiE).
- CONTEXT: Johnny Cupcakes unorthodox marketing (~95% Johnny) — limited-drops/reactive-marketing (cupcake-bling within 24h of Drake), experiential scavenger-hunt giveaways, time-gated scarcity, rent-free pop-ups via barter (500+, ~99% free); Chris close only; Johnny-Cupcakes entity (Xxq7c0wGGeA).
- CONTEXT: Seth Godin "Creative Block is a Myth" (100% Seth) — permission-to-write-badly, no-"writing-poorly-block", 50k-words-of-bad-writing threshold, plumber analogy; Chris absent; Seth-Godin entity (VRdFjL_uNoo).
- CONTEXT: Atomic Design (Brad Frost concept) — unattributed Futur instructor (not Chris); design-systems/atoms-molecules-organisms; no persona data (W3A33dmp17E).
- ★ 5 Things You Should NEVER Do on a Sales Call — checklist: (1) don't go in desperate (clients smell it), (2) don't interrupt/cut off, (3) don't assume what they want/value (ask, let them say it), (4) don't go past the sale (once they agree, stop), (5) don't fixate on your script -> LISTEN (~10% you / 90% them, "two ears, one mouth"); Chris solo (eoNH6ol9bmM).
Attribution: 3 of 7 context (Johnny Cupcakes, Seth Godin, Atomic Design instructor) + 1 mixed compilation (guests/instructors fenced); 3 Chris-led ★L3. No family names. Counts: L2 349->356. 3 new L3-candidates.
Synthesis notes: NEW — (1) mindset (BIO/voice): long-vs-short-term signature cluster (rock-bottom-identity, delayed-gratification, out-hustle, Spock-detachment, gratitude) — strong persona/biography material; (2) pricing/voice: stop-charging-hourly roleplay (Socratic-flip, symmetry-of-logic, hourly-punishes-competence, value-appreciates) — negotiation voice-training; (3) sales-clients: "5 things never on a sales call" checklist (desperate/interrupt/assume/past-the-sale/fixate-on-script) — landmark, promote to sales-clients + beliefs. ENTITY: Seth Godin (now 2 appearances - creative-block + AI; author Linchpin/Stop-Stealing-Dreams; strong candidate for a context entity page) + Johnny Cupcakes (deepened). Debt 6/10.
SESSION-END NOTE: user requested stop after this batch. Loop paused at batch 51, L2=356 (through 2019-01-14). Resume with /loop /ingest-loop — next Stage B batch continues @thefutur P2 (Jan 2019+); synthesis checkpoint due at debt 10 (~4 batches out). Open: P2 757 + P3 44 + Academy 72 + shorts 859.

## [2026-07-18] ingest | yt batch (@thefutur, 6) — P2 Jan–Feb-2019 (build-a-bridge, passive-income w/Melinda, 5-rules-sales-call, 4-buyer-types)
Batch 52. Ingested 6 @thefutur videos (2019-01-15 → 2019-02-04) to L2. 2 rows left on 429 (yt-og6-CKoM5Lk, yt-YCGRzMN9gEE — retry later). L2 356->362.
- ★ How to Transition From a Full-Time Job to Freelance? — "build a bridge" method: keep the day job (leverage; quitting first = desperation), build positioned site + price-qualifying intake script in spare hours, win side jobs, then ARBITRAGE by outsourcing the work to a cheaper freelancer (~$400 on a $5k job) and pocketing the spread; quit only once side income beats salary; Chris solo, audience Qs=context (LWqmRvWvXec).
- 2 Minute Brain Training Exercise — NO="Next Opportunity" / FAIL="First Attempt In Learning" reframe (word can't appear in its own acronym). ⚠️ NOT CHRIS: unnamed fill-in host covering for Ben Burns (new baby); whole page attribution:uncertain, does NOT train persona (p4sxZEpi8Kk).
- ★ How to Build a Passive Income Business — w/ Melinda Livsey (Ep.14) — dialogue; Chris-attributed only: passive income = "build once, sell many times" (still needs marketing — "nothing sells itself"); 3 product paths (templates/tools, course, derivative of your framework); digital-over-physical (no capital/logistics/inventory; piratable but scalable); impact-vs-effort facilitation graph + design-sprint prioritization; goal-setting (set high to "jump the curve" [Kawasaki], divide annual by 10, non-linear sales curve); GBO credited to Jose Caballer; Melinda=context. Several caption name-garbles flagged for verify (Svb8fTwX0BE-adjacent) (7b_pEgV86BE).
- ★ Watch This Before Your Next Client Call — "5 rules to rule your sales call" (positive mirror of 5-never-do): (1) talk money EARLY, (2) style>substance/match-mirror [Tony Robbins], (3) educate=EDUCE "to draw out" — show-don't-tell via questions, (4) question quality: why>how>what & "whoever asks more questions is in control", (5) neutral=trust; also "remove yourself from the sale 3x", "how can you lose what you didn't have?"; live role-play w/ participant "Aaron"(uncertain) (lwipfn9znk0).
- When A Client Wants More But Doesn't Want To Pay (Role-play) — Chris plays BOTH vendor & client "Nancy"; scope-creep/free-work playbook: reset the frame, price extras as a SEPARATE service, anchor full package ($1,400) before one modest concession ($1,000), give a pressure-free walk-away + surface real consequences (deadline/rush fees), let the client DE-SCOPE themselves back to the original $800 rather than eat free work; relationship intact; demonstration (no debrief), not L3 (Svb8fTwX0BE).
- ★ 4 Different Buyer Types and How to Respond — taxonomy + per-type tactic: PRICE buyer (qualify fast/MLE, referral-out below minimum), INDECISIVE, KNOW-IT-ALL (agree with everything, hold your price), VALUE buyer (want-vs-need/emotional-vs-features, Porsche analogy, "don't go past the sale"); referral-fee mechanics 10–15% (up to 20–30%) + MLE; Futur pays reps stipend+% for leads; Chris solo (SzW8TUoN01M).
Attribution: 1 do-not-train (fill-in host, NOT Chris) + 1 dialogue (Melinda fenced) + 1 role-play (client lines in-character) + 3 Chris-led; 4 new ★L3-candidates. No family names. Counts: L2 356->362.
Synthesis notes: NEW — (1) business/mindset: "build a bridge" FT→freelance transition + freelance-ARBITRAGE/brokering model (buy-low-sell-high on labor) — new to corpus, promote to business + beliefs; (2) business/content-strategy: passive-income "build once sell many" doctrine (3 product paths, digital-over-physical, nothing-sells-itself, jump-the-curve goal-setting) — Chris's fullest passive-income treatment, promote to business; (3) sales-clients: "5 rules to rule your sales call" (money-early, style>substance, educe=draw-out, why>how>what, whoever-asks-more-questions-controls) — positive mirror of the 5-never-do checklist, promote as paired framework; (4) sales-clients: "4 buyer types" taxonomy + MLE/referral-fee mechanics — landmark qualifying framework, promote to sales-clients; (5) pricing: scope-creep/free-work negotiation playbook (reset-frame, price-extras-separately, anchor-then-one-concession, let-client-de-scope) — promote to pricing. Debt 7/10.

## [2026-07-18] ingest | yt batch (@thefutur, 6) — P2 Feb-2019 (passive-income-promo w/Melinda, cost-estimate, inbound-marketing; 2 non-Chris)
Batch 53. Ingested 6 @thefutur videos (2019-02-06 → 2019-02-27) to L2. 2 rows still on 429 (yt-og6-CKoM5Lk, yt-YCGRzMN9gEE). L2 362->368.
- ★ How to Promote Your Passive Income Business — w/ Melinda Livsey (Ep.15) — sequel to Ep.14 (marketing, not building). Chris-attributed: market-awareness matrix (buyers × aware-of-problem/aware-of-you; worst=neither; validate gut with polls, "separate feelings from facts"); finite-audience reframe (real work = converting people not-yet-aware; if you need ~150 units & have ~150 interested, have conversations not ad-campaigns); freebie/tripwire must align with the ultimate product; expert-positioning ("everything else is garbage"); distill-to-the-essence hook; "blinders on our own stuff" + sounding-board method; landing-page audit heuristics; content-repurposing; humble-delegation voice ("I know enough to be dangerous", hands digital mktg to Ben Burns). Melinda=context; garbles flagged (V6BJxvxUXss).
- ★ How do you Estimate the Cost of a Project? — cost-stack bid build-up: naive $500/day×10=$5k grows to correct $20,400 by layering marked-up labor + producer + prorated art-director + workstation/overhead + explicit 20% profit markup (stated openly as profit); bill every role even if you do it yourself (the "extra" is your margin/risk buffer); mark up artist day rates (artists underestimate). First numbers-driven bottom-up estimating method in corpus. Caption garble caught: "$33,400" markup is really $3,400 (arithmetic + stated total confirm). Chris solo (6BKWq9VJd8w).
- Project Management - How to Break Down Projects — chunking hierarchy: 3 locked waterfall phases → weekly Monday sprints → tasks, "Tetris" task-packing + padded estimates, once-a-week client cadence; 3-phase video breakdown (style-frames → animatic → animation/render); same method scales to solo year/quarter/week. ⚠️ 2 unlabeled speakers, no names — attribution:uncertain, does NOT train persona (zlnVc1nBTto).
- Video Content – 3-steps to Present Your Ideas Clearly — video-structure framework (Overview: cold-open+value-promise+bio+why / 3–5 recipe steps / Outro: recap+action+CTA); YouTube = "just-in-time education", #2 search engine; always make an explicit CTA. ⚠️ NOT CHRIS: Matthew Encina (CCO, self-identified); Futur context only, does NOT train persona (VRecjO0A6Ns).
- How to Build a Passive Income Business For Creatives - Dustin Lee — guest interview; ~95% Dustin Lee (RetroSupply Co. founder): choose-the-right-product, make for a specific "your people" audience, love-marketing; RetroSupply 15-brush $15 Procreate pack, customer-research-driven selection, niche-down, start-now/prepared-to-fail. Chris minimal (only reframes research as rapport-building = echo of existing listen/ask theme). Dustin=context; dustin-lee entity candidate. Nothing new Chris-attributed (RGTUPlf9tAo).
- ★ Inbound Marketing – How to get Clients to Come to You — reframes "better clients?" as inbound/differentiation: if client can't tell you apart they buy on price ("race to zero"), so pick a sharply specific niche + evergreen content, target clients with "more money than time"; metaphors: race-to-top-vs-zero, campfire+magnifying-glass focus, "tip of the spear... pointy, pointy, pointy"; marketing stays narrow, broaden only after landing. Unnamed co-host asks Q + adds "just got funded" prospecting tip (context). (vCn92eifsjM).
Attribution: 2 do-not-train (Matthew Encina solo NOT Chris; PM-chunking 2-uncertain-speakers) + 1 guest-context (Dustin Lee ~95%) + 1 dialogue (Melinda fenced) + 2 Chris-led ★; 3 new ★L3-candidates. dustin-lee flagged as new entity candidate. No family names. Counts: L2 362->368.
Synthesis notes: NEW — (1) content-strategy/branding: passive-income PROMOTION playbook (market-awareness matrix, finite-audience/conversations-over-campaigns, freebie-alignment, expert-positioning, distill-to-essence) — pairs with Ep.14 build; promote to content-strategy; (2) pricing: cost-stack/bottom-up PROJECT ESTIMATING method ($5k→$20.4k build-up, bill-every-role, mark-up-labor, 20%-profit-stated-openly) — first estimating framework in corpus, promote to pricing (complements value-based material with a cost-basis floor); (3) content-strategy/sales-clients: inbound/differentiation set (race-to-top-vs-zero, campfire+magnifying-glass, "more money than time" ideal-client, tip-of-spear niching) — promote to content-strategy + sales-clients. CONTEXT/NON-CHRIS logged, NOT for persona: Matthew Encina video-structure framework (Futur CCO); PM chunking/Tetris framework (uncertain speaker) — hold pending speaker confirmation. ENTITY candidate: Dustin Lee (RetroSupply Co.). Debt 8/10 — synthesis checkpoint due in ~2 batches.

## [2026-07-18] ingest | yt batch (@thefutur, 6) — P2 Mar-2019 (Young Guns EP9/EP10 branding critique, hot/warm/cold leads; guests Gerson/Kunz; 1 non-Chris)
Batch 54. Ingested 6 @thefutur videos (2019-03-04 → 2019-03-25) to L2. 2 rows still on 429 (yt-og6-CKoM5Lk, yt-YCGRzMN9gEE). L2 368->374.
- Stop Losing Money – Break Even Point — guest interview w/ Errol Gerson (Futur "Managing Money" instructor; caption-garbled "Garrison"). Break-even framework = GERSON's (fixed-overhead÷0.5-margin → required revenue ÷ blended-rate → billable hours; keep 6 months' overhead; 10–12% pay-cut over layoffs) — NOT persona. Chris-attributed NEW: runway/cash-flow-vs-sales-cycle insight (as you charge more, close times stretch from a day @$500 to a year @$50k–250k → need cash runway; "sense of peace" at 3 months runway; a ~$250k deal took >1yr to close). errol-gerson entity candidate (dr0ntxYFEWs).
- Project Management - How to Manage Your Clients — client-mgmt tactics ("process is the product", decision-tree logging, versioned email subjects, feedback windows in Gantt, missed-milestone = lose a revision, "bending" slack). ⚠️ NOT CHRIS: 2 unlabeled Futur instructors (both reference "Ben" in 3rd person → neither is Ben/Chris); do-not-train-persona (Futur context); promo for Practical Project Management course (wEvVoXZzkKU).
- ★ Young Guns EP 9 – Airline Branding Challenge — Chris DOMINANT mentor critiquing 5 student WIPs (premium airline sub-brand, JetBlue Mint model). Chris design methodology: sub-brand≠rebrand ("people don't hire you to hit the nuclear button"; constraint is the challenge), understand-problem-before-solution, generate ~100 names + "connective tissue" w/ parent (his "Emerald" for Emirates), presentation discipline (deck not Word doc; Paul Rand million-dollar-logo story; don't "neg yourself"; "mirror to your soul"), marketing rule "aim 10–15 yrs younger" (Scion cautionary tale), color craft ("red & blue can mean a thousand things"; hue/sat/value age a brand), restraint "one flourish not 35"; self-disclosure loves Swiss design (studied in architecture school). Students=context (N0WD9KG7kEY).
- How to Create Engaging Content for Instagram — guest hand-letterer Stefan Kunz (garbled "coun"): growth = make something people talk about + engineer early hype to beat the algorithm (viral "home is where the pants aren't" manufactured intrigue). Tactics = GUEST (context). Chris-attributed NEW (modest): lens that standout social content is designed CONCEPTUALLY like an ad (engineer one "twist" = hype/PR/marketing); maker = fundamentally a marketer w/ a craft skill ("Johnny Cupcakes of hand-lettering"). stefan-kunz entity candidate (2ocGbROfgfQ).
- ★ Convert Cold Leads into Paying Clients — Chris solo: hot/warm/cold lead-TEMPERATURE taxonomy + matched approach (hot→personality/story, "what is the product?"; warm→trusted-endorsement/affiliate bridge, "what is the solution?"; cold→name the problem in their words, "what is the problem?", move up the awareness ladder). Preframing/priming determines lead quality. EXPLICITLY credited to Russell Brunson (DotCom/Traffic Secrets) → promote w/ 3rd-party attribution, not as Chris IP. Self-report: Futur 30k+ subscribers, 700+ videos (2019). russell-brunson entity candidate (7Wsrq0dfYsw).
- ★ Young Guns EP 10 – Presentations & Critique — Chris SOLE critic of 5 airline sub-brand presentations. Design-craft principles: negative-space≠white-space (can be black/gold = low activity), kerning-as-volume (find hardest pairs first, "pouring sand into gaps"), "slap-on logo" anti-pattern (fix via pattern/edge/print integration), brand-extension via parent DNA (related not derivative), print-finishing=premium (hot-foil, vellum, wax seals, metallic edges, subtle embroidery), show-design-in-context, "undesigned design is hard" (simple-that-looks-good is rare; commit to a visual language), "premium economy = jumbo shrimp" rant, Vignelli reference; 3 student archetypes from 15 yrs teaching at Art Center. Students=context (P5cqMtqTNog).
Attribution: 1 do-not-train (client-mgmt, 2 unlabeled instructors) + 2 guest-led (Gerson break-even, Kunz IG — frameworks=guests, only Chris framing kept) + 3 Chris-led ★ (2 Young Guns Chris-dominant + hot/warm/cold); 4 new ★L3-candidates. Entity candidates: errol-gerson, stefan-kunz, russell-brunson (+ dustin-lee from batch 53). No family names. Counts: L2 368->374.
Synthesis notes: NEW — (1) business/mindset: Chris's RUNWAY/cash-flow doctrine (bigger deals close slower → hold cash runway; peace at 3-months) — new business belief + biography datapoint (~$250k deal >1yr), promote to business; (2) design-craft/branding: RICH Chris design methodology from Young Guns EP9+EP10 (sub-brand≠rebrand, ~100-names + parent-DNA, aim-10-15yrs-younger, present-with-a-deck/Paul-Rand, negative-space≠white-space, kerning-as-volume, slap-on-logo anti-pattern, print-finishing=premium, "undesigned design is hard", restraint) — first deep design-CRAFT critique corpus in a while, big promote to design-craft + branding + voice (many quotable lines); (3) sales-clients/content-strategy: hot/warm/cold lead-temperature taxonomy + awareness-ladder (credited Russell Brunson) — promote to sales-clients w/ attribution; (4) content-strategy: "social content = designed like an ad / maker = marketer" lens (modest). ENTITY candidates for synthesis: Errol Gerson (Futur money instructor), Stefan Kunz (hand-letterer guest), Russell Brunson (influence/source), Dustin Lee (RetroSupply, batch 53). CONTEXT/NON-CHRIS: client-mgmt PM tactics (2 unlabeled instructors) — NOT persona. Debt 9/10 — SYNTHESIS CHECKPOINT DUE NEXT ITERATION (Stage S, pass 6 → system-prompt v7).

## [2026-07-18] ingest | yt batch (@thefutur, 4) — P2 Mar–Apr-2019 (Melinda Ep.16/17 marketing, Debbie Millman BIOGRAPHY interview; Adobe trends guest)
Batch 55. Ingested 4 @thefutur videos (2019-03-28 → 2019-04-10) to L2 (4 rows on 429: og6-CKoM5Lk, YCGRzMN9gEE, oyXt5jR6Y1I, aDLmEezhnG0 — retry later; only 4 of 8 fetched, but 4 successes = not a rate-limit stop). L2 374->378.
- Visual Trends 2019 — Adobe 2019 trend forecast (Natural Instincts / Creative Democracy / Disruptive Expression / Brand Stand). ⚠️ ~90% guest Brenda Milis (Adobe Stock, caption-garbled "Brenda Millis"), NOT persona; Chris = host. Chris-attributed NEW (minor): reframe "trendy"=negative (you jumped on something already dated) vs be "visually fluent" + "culturally relevant"; over-production reads inauthentic (show behind-the-scenes); brand-stand must match real culture not "controversy for controversy" (odwoh5kL9dg).
- ★ How do I Market my Product? — w/ Melinda Livsey (Ep.16) — Chris-attributed: SELL THE PROBLEM NOT THE SOLUTION (educate on the pain > the fix; vividly paint the "design slave/sold a dream" pain); people move on LOSS/FOMO > gain (market earlier in the journey, not to the already-convinced); "describe what the status-quo is good for → audience infers what it's not" (Jobs iPhone via Nancy Duarte); "different but better" — force a positioning lane early vs a bigger incumbent; "WRITE YOUR THESIS PAPER" method (one core concept + deep original research + novel packaging → a whole career; Sinek/Start-With-Why, Godin/Icarus); win-with-the-heart-then-logic (Tony Robbins repetition); live preview of his commerce/currency-history research underpinning anti-hourly thesis ("always been about exchanging value, never time"); self-descriptor "weird business person, not really motivated by money". Melinda=context (J0m-fwEQ5TQ).
- ★ How do you find Customers for Your Product? — w/ Melinda Livsey (Ep.17) — Chris-attributed: problem→solution→product cold-lead sequence (attributed Russell Brunson/DotCom Secrets; solution via personal stories); STORY-MINING method (anchor memories on "spaces, places, and things"; build a 5–7-point timeline then find 5 more between each); funnel-attrition math (Casey Neistat 1M→8K→500→5; email subs = hot leads that skip the funnel); audience-platform advice (email doesn't grow reach; use Medium + editorial calendars; "expand the pool" don't compete for the same fish); positioning "four-minute abs" analogy + noun-for-the-avatar ("overwhelmed aspiring designer" not "strategist"); anti-planning (Rework/Fried+Hansson, Bezos framing; Futur self-funded "survival mode"); "give give give" law of reciprocity long-term play (Style Scape launch ~400 seats/~$60K as proof). Garbles flagged: Cialdini/Influence (heard "Robert Kelly"). Melinda=context (apqbrvu2VlE).
- ★ Does Creativity Come From Insecurity? w/ Debbie Millman — guest interview; Debbie (Design Matters) thesis: creativity may stem from a pervasive insecurity/drive to matter (context). BIOGRAPHY GOLD — Chris's richest childhood monologue in corpus: first-gen Vietnamese immigrant, latchkey kid, hardworking absent-weekday parents w/ high expectations, father's "lecture for hours instead of the belt" parenting, total-freedom childhood (creek/caves ~age 11), lifelong identity-struggle/insecurity, outcast w/ racial slurs + fist-fights in a mostly-white neighborhood, discovered typography/graphic-design as the "anchor"/"foundation of the house of my personality", fair-weather-friends lesson, deliberately modeled himself on admired people (classmate Barton Chin, a gentle roommate), self-concept "X-Men Mimic"/"knowledge vampire", "every peak is the base of another mountain" optimism. Paula Scher ref (garbled "Paula share"). Debbie=context, entity candidate (wHhcuix-ir8).
Attribution: 1 do-not-train (Adobe guest ~90%) + 1 guest-interview biography (Debbie=context, Chris-bio kept) + 2 Melinda dialogues (fenced) ; 3 new ★L3-candidates. Entity candidates: Debbie Millman (recurring-caliber), Brenda Milis (one-off, likely skip). No family names (childhood facts self-reported, parents unnamed). Counts: L2 374->378.
Synthesis notes: NEW — (1) BIOGRAPHY (major): Debbie Millman interview = richest childhood/origin material yet (Vietnamese-immigrant/latchkey, outcast/insecurity→drive, typography-as-anchor identity, knowledge-vampire self-concept, "every peak base of next") — big promote to biography.md + voice.md; ties to existing knowledge-vampire/comparison threads; (2) content-strategy/sales-clients: "sell the problem not the solution" + loss/FOMO>gain + "different but better" + "write your thesis paper" differentiation method (Ep.16) — promote to content-strategy + sales-clients; (3) content-strategy: story-mining (spaces/places/things + timeline), funnel-attrition math, "expand the pool", give-give-give reciprocity, problem→solution→product (Brunson) (Ep.17) — promote to content-strategy; (4) business/mindset: anti-planning/Rework + "weird business person not motivated by money" + commerce-history research underpinning anti-hourly thesis — belief + biography datapoints. ENTITY candidates carried: Debbie Millman, + prior (errol-gerson, stefan-kunz, russell-brunson [now 2+ mentions — strong], dustin-lee). Debt 10/10 → SYNTHESIS CHECKPOINT NOW DUE: next iteration is Stage S (synthesis pass 6 → system-prompt v7), draining batches 46–55.

## [2026-07-18] lint | synthesis pass 6 — @thefutur P2 Oct-2018 → Apr-2019 (batches 46–55, L2 317→378) → system-prompt v7
Checkpoint synthesis over ~10 ingest batches. Fanned out one agent per file (concurrency rule). ENRICHED all 7 topic hubs + 3 persona files; recompiled persona/system-prompt.md v6→v7 (compiled_from 317→378).
- **pricing** +6: anchoring-reversal (bigger number first) + verbal-upfront-pricing; resentment/dread=underpricing (Blair Enns); two budget lenses (emotion vs logic, both reject budget-first) + low-ball=positioning-problem; stop-charging-hourly Socratic-flip (value appreciates $18k→$26k); scope-creep/free-work playbook (reset-frame/price-extras-separately/anchor-then-one-concession/let-client-de-scope). Cost-stack estimate FOLDED into existing 2015 build-up (near-dup) w/ 🔄 EVOLUTION note on budget-first sequence.
- **sales-clients** +7: "I sell you your idea" (reflect-question-back); 30-outreach Commute-Challenge (Jim Rohn); get-a-mentor (value-exchange/ask-small/give-2-5x); 5-things-NEVER-on-sales-call + 5-rules-to-rule (paired checklists, 10/90); 4-buyer-types + MLE/referral-fee; hot/warm/cold lead-temperature (⚠️ credited Russell Brunson, borrowed).
- **business** +5: document→delegate→automate; build-a-bridge/freelance-arbitrage; passive-income "build once sell many"; runway/cash-flow doctrine (⚠️ break-even math = guest Errol Gerson, only runway=Chris); culture-as-competitive-advantage.
- **content-strategy** +5: attract-ideal-client-via-content; passive-income promotion/market-awareness-matrix; inbound/race-to-top-vs-zero/campfire/more-money-than-time; sell-the-problem-not-solution/"write your thesis paper"; story-mining + funnel-attrition math + expand-the-pool + give-give-give (⚠️ TENSION callout: pointy-niche vs broad-content-topics, resolved by level).
- **design-craft** +3: deliberate-incubation ideation (saturate→sleep→capture); Young Guns EP9 sub-brand methodology (sub-brand≠rebrand, ~100-names+DNA, aim-10-15yrs-younger, present-with-deck/Paul-Rand, color-craft, restraint); EP10 critique principles (negative-space≠white-space, kerning-as-volume, slap-on-logo anti-pattern, DNA-extension, print-finishing=premium, "undesigned design is hard").
- **branding** +4: do-good-work-IS-positioning + get-known-for-one-thing-then-flip; positioning-increases-value (value=max-willingness-to-pay, Rolex/Timex); identity≠brand-strategy (order-taker-vs-consultant, Dan Sullivan 3-yr Q); premium sub-brand≠rebrand/aim-younger (positioning angle).
- **mindset** +3: long-game maintenance kit (out-hustle-over-talent, "slay the wolf", Spock-detachment, gratitude "life hack"); anti-planning/"survival mode" (Rework, ⚠️ CONTRADICTION callout vs goal-decomposition, resolved by horizon); take-100%-responsibility (stop-using-parents-as-crutch).
- **persona**: beliefs +16 (sources 69→85), voice +~20 verbatim quotes (sources 41→51), biography +8 fact-clusters (sources 25→31) incl. MAJOR childhood/origin (Debbie Millman interview: Vietnamese-immigrant/latchkey/outcast→insecurity→drive, typography-as-"foundation of the house of my personality", X-Men-Mimic/knowledge-vampire, "every peak is the base of another mountain") + Blind reinvention arc (2007 ~$7M → 2013 inflection → motion→brand-strategy via CORE/Jose Caballer; self-reported) + parents-black-sheep nuance + no-partner regret + $250k->1yr deal + commerce-history research.
- **system-prompt v7**: folded new SALES checklists/buyer-types/lead-temperature, build-a-bridge/runway/passive-income, sell-the-problem/race-to-top/thesis-paper, Young Guns design-craft, mindset (out-hustle/anti-planning/responsibility), childhood-origin + Blind-reinvention bio, +14 catchphrases, +influences (Russell Brunson, Debbie Millman, Tony Robbins). compiled_from 317→378.
Attribution (heavy guest/instructor era): fenced Melinda (Ep.14-17), Errol Gerson, Debbie Millman, Stefan Kunz, Dustin Lee, Brenda Milis/Adobe, Russell Brunson (source); do-not-train items (Matthew Encina video-structure, 2 PM-chunking unlabeled-instructor videos) kept OUT of persona. Family names kept out; all Blind financials marked self-reported. Advanced high-water mark to batch 55 (L2=378). ENTITY-PAGE debt deferred to next checkpoint (Russell Brunson, Debbie Millman, Jose Caballer/Blind, Errol Gerson, Dustin Lee, Stefan Kunz). Synthesis debt reset 10→0.

## [2026-07-18] ingest | yt batch (@thefutur, 2) — P2 Apr-2019 (self-acceptance/Spock-compression, Young Guns S1 finale) — RATE-LIMITED
Batch 56. Only 2 of 8 fetched — HEAVY rate-limiting (6 of 8 on 429: og6-CKoM5Lk, YCGRzMN9gEE, oyXt5jR6Y1I, aDLmEezhnG0, UmgtWZfPA4o, __V7mYxg9Mo). Ingested 2 to L2. L2 378->380. Backing off next wakeup to let YouTube cool down.
- How Do You See Yourself? How Do Others? — Chris-attributed: self-acceptance ("I'm the best judge of my own work — criticism only affirms what I already know, praise doesn't inflate me"); Spock/Vulcan emotional-COMPRESSION self-modeling (clip the highs & lows, audio "sound-limiter" metaphor — "maybe that's why I sound funky"); external-validation-doesn't-work (coaching a team member); mention of a therapist; Brené Brown/vulnerability influence (attribution uncertain). 2nd unidentified speaker (refers to Chris in 3rd person) = context. Soft-L3 → voice/biography (aBxl1SBERYw).
- Design Mentorship Reactions & Tips - Young Guns (S1 finale, ep.12) — montage; Chris short per-student appraisals (context) + a few teachable tips: feedback-RESILIENCE lens (does the mentee "fold and collapse" or "rise to the challenge" — maturity/work-ethic signal); global-TALENT/representation thesis (talent exists in overlooked pockets — Egypt, India; people need to "see somebody like themselves in the mirror"; the stated purpose of the series); coaching goal = confidence not just skills. Students + co-host narrator ("Chris told me...") = context. Not L3 (_VrsBh5h8j4).
Attribution: 1 two-speaker (Chris + unidentified 2nd = context) + 1 multi-speaker montage (students/co-host = context); 0 new ★L3 (1 soft-L3 for persona). No family names. Counts: L2 378->380.
Synthesis notes: NEW (minor, debt 1/10) — (1) mindset/voice: Spock/emotional-compression self-modeling + "sound-limiter" metaphor + self-acceptance "best judge of my own work" — distinct voice/biography detail (why his affect is even-keeled), fold at next checkpoint; (2) mindset: feedback-resilience "fold vs rise" mentee lens + global-talent/representation thesis (the Young Guns series purpose). RATE-LIMIT NOTE: 6 persistent-429 rows now queued (og6-CKoM5Lk, YCGRzMN9gEE, oyXt5jR6Y1I, aDLmEezhnG0, UmgtWZfPA4o, __V7mYxg9Mo) — will retry after cool-down.

## [2026-07-18] ingest | yt batch (@thefutur, 4) — P2 Apr-2019 (millennials pep-talk, BOLD 2019 keynote, get-work-in-any-city, Young Guns S2 trailer)
Batch 57. Rate-limiting easing (4 of 8 fetched; 4 still on 429: og6-CKoM5Lk, YCGRzMN9gEE, aDLmEezhnG0, UmgtWZfPA4o). Ingested 4 to L2. L2 380->384.
- Motivating Millennials — after-hours team pep-talk (Chris + 3 team members Ricky/Aaron/Jonah=context). Chris-attributed NEW mindset: motivated-by-LOSS>win (fear-of-being-a-loser drives harder than aspiration); binary "hero or loser" self-image (reject the comfortable middle); motivation-evaporates if not acted on within a day ("advice not acted on is vapor"); empowerment reframe (don't wait for Chris to change — ask what YOU can change); delegation-clarity (concrete tasks easy, high-level idea-requests need their own thinking); "same suit vs new person" reinvention metaphor. Not L3 (oyXt5jR6Y1I).
- Relevance in the Age of Social Media – ArtCenter BOLD 2019 — edited multi-speaker recap of BOLD 2019 (The Futur × ArtCenter's FIRST collaboration; Chris = host/curator; a featured photographer runs IG segments=context). Frameworks Chris teaches are already known (customers-vs-audience, Kevin Kelly 1000-true-fans, Russell Brunson attractive-character, GaryVee "internet won"). BIOGRAPHY (flagged): confirms ArtCenter alum + taught 15+ yrs + spoke at all 3 prior creative symposiums; calls BOLD a "homecoming". Names caption-garbled. Not L3 (__V7mYxg9Mo).
- The Challenges of Being a Creative Professional – Young Guns (S2 TRAILER) — cast-intro reel; 7 students introduce their career problems (impostor syndrome, pricing, business-of-design, niching, audience — all context); Chris only closing lines w/ Melinda Livsey (co-host) teeing up a portfolio review. No new persona material; notes Young Guns S2 format. Not L3 (0kVXDPxRMgk).
- ★ How to Get Work in ANY City — Chris coaches "Alejandro"(=context): cold-DM outreach playbook — resumes & email are "dead", DM the top ~12 companies you want, keep it short/specific, praise-first / don't-ask-right-away then "come back the next day and show up", self-report ~100 DMs/day (replies to each); "trust your struggle" mantra; reframe-to-dissolve ("drop the word 'new' — any city is the same process"); "half an inch from the line to stand out" differentiation. L3-candidate (q_QESEKja3I).
Attribution: 2 multi-speaker (team pep-talk + BOLD recap, non-Chris=context) + 1 trailer (students/Melinda=context) + 1 coaching (coachee=context); 1 new ★L3 (cold-DM playbook). No family names. Counts: L2 380->384.
Synthesis notes: NEW (debt 2/10) — (1) mindset: motivated-by-loss>win + binary hero/loser self-image + motivation-evaporates (team pep-talk) — distinct mindset nuggets, fold at next checkpoint; (2) sales-clients/content-strategy: cold-DM outreach playbook (resumes/email-dead → DM-top-12, praise-first, ~100/day) + "trust your struggle" — tactical lead-gen, promote to sales-clients; (3) BIOGRAPHY corroboration (BOLD 2019): ArtCenter alum + taught 15+yrs + spoke at all 3 prior symposiums + Futur×ArtCenter first collab "homecoming" — minor biography enrichment. Rate-limit: 4 persistent-429 rows remain (og6-CKoM5Lk, YCGRzMN9gEE, aDLmEezhnG0, UmgtWZfPA4o).

## [2026-07-18] ingest | yt batch (@thefutur, 5) — P2 Jan/Apr-May-2019 (New-Year legacy-OS, content-repurposing, Young Guns S2 review+coaching, AIGA belief-systems keynote)
Batch 58. Rate-limiting easing further (5 of 8 fetched incl. long-stuck og6-CKoM5Lk; 3 still on 429: YCGRzMN9gEE, aDLmEezhnG0, UmgtWZfPA4o). Ingested 5 to L2 — strong Chris-heavy batch, 4 ★L3. L2 384->389.
- ★ Live YOUR Life – 2019 is Your Year — New Year talk. NEW mindset: "legacy OS" metaphor (parents run an OS right for THEIR time; world changes too fast to inherit it); Bronnie Ware "Top Five Regrets of the Dying" (top regret: courage to live your OWN dream not someone else's); mortality-as-motivator (birth→death line, midpoint=still time, momentum works against you the longer you wait); immigrant-parents want stability b/c they suffered ("love you but don't have the information"); choose consciously from compassion. Audience("Rebecca")=context (og6-CKoM5Lk).
- How to Make More Content and Reach More People — Chris solo content-repurposing engine: take one long-form piece, "chop it up 7 ways", reformat PER platform (long→transcribe→micro-articles→best line=tweet→tweet+image=IG story), "make it work for its platform" don't cross-post identically; superfan-scraper-turned-hire story; self-report following 1.5k→~60k via repurposing. Not L3 (standard) (zeE7F1498yw).
- ★ Design Portfolio Review – Young Guns 2 Ep2 — Chris+Melinda co-host review 7 under-26 portfolios vs 4 criteria (personality/focus/clarity/quality), secret-score. Chris NEW design-craft/positioning: "3 projects to identify a PATTERN" (AD can then predict your output = easy hire); tell the story INSIDE the visuals not the copy (many won't read; "show less = more curious"); curate ruthlessly (sub-top work sends the wrong signal); "a logo is just an identifier/PUNCTUATION not the communication" (over-expressive marks don't age); neutral "Swiss modern" is more broadly applicable "and gets paid a lot more"; go-with-type-vs-against-type premium framework; personal-vs-professional feed focus. Melinda(context)/students(context) (UJo7a_9IGBM).
- ★ Belief Systems—Unlocking Your Potential — Chris's FIRST AIGA National Design Conference keynote + Q&A. NEW vs existing belief-cycle: input→INTERPRETATION→output model (interpretation = the overlooked middle step; same input → infinite outputs, choose an empowering one); subjective "individual reality" vs objective physical reality; word-reframes (FAIL=first-attempt-in-learning, No=next-opportunity, FEAR=fantasized-experience-appearing-real, Pain=precursor-to-anything-notable, Safe="stay average forever"); internal-vs-external validation → client exploitation; "make stuff without judging it, be prolific, then listen to the market". Debbie Millman guest (insecurity-as-genesis, HER thesis)=context. BIO: first AIGA keynote (mlcovSWlAow).
- ★ These Designers Need HELP – Coaching Young Guns S2 — Chris sole coach of 7 women designers (Ricky Lin co-host=context) + $3k-logo sales role-play. NEW: pricing "DOUBLE your price, don't inch up" + charge-more virtuous loop (higher fees buy world-class collaborators) + "skip value-pricing theory, master hourly→deliverable→project then hold the line" + luxury-no-justification + pre-qualify referral leads/decline old "favor price"; listening "listen to understand not to respond" + verbatim-repeat "human tape recorder" drill; craft "make 3 projects SING vs 35 on Behance" + close-the-gap self-critique + perceived-value-via-photography; mindset worthiness/"European clients won't pay"=limiting-belief, inexperience-as-asset. BIO: dot-com-bust laid off 3-4 people; wife's "do you have the team for the future?" question; "employment is not a marriage"; invest in coaches/CPA when successful not desperate. Students=context (kY7i_JYNQ3Y).
Attribution: 2 Young Guns S2 (Melinda/Ricky Lin/students=context) + 1 keynote (Debbie Millman guest=context) + 2 Chris-solo; 4 new ★L3-candidates. No family names (wife unnamed). Counts: L2 384->389.
Synthesis notes: NEW (debt 3/10) — (1) mindset: "legacy OS"/parents'-outdated-OS + Bronnie-Ware-regrets + mortality-as-motivator (New Year) AND input→interpretation→output belief-layer + word-reframes FAIL/No/FEAR/Pain/Safe (AIGA keynote) — strong mindset promotes, pair at next checkpoint; (2) pricing: "double don't inch up" + charge-more-virtuous-loop + master-fee-ladder-then-hold-line (YG S2 coaching) — promote to pricing; (3) design-craft/branding: "3-projects=a-pattern", story-in-visuals, curate-ruthlessly, "logo=punctuation", Swiss-modern-pays-more (YG S2 review) — promote to design-craft + branding + portfolio-review; (4) sales-clients: "listen to understand not respond"/human-tape-recorder drill + $3k-logo role-play (why-this/why-now/why-me per Jonathan Stark) — promote to sales-clients; (5) content-strategy: "one piece → 7 formats" repurposing engine — promote; (6) BIOGRAPHY: dot-com-bust layoffs (3-4 people) + wife's "team for the future" question + first-AIGA-keynote — biography enrichment. Rate-limit: 3 persistent-429 rows remain (YCGRzMN9gEE, aDLmEezhnG0, UmgtWZfPA4o).

## [2026-07-18] ingest | yt batch (@thefutur, 4) — P2 May-2019 (Young Guns S2 packaging challenge+critique, How-To-Charge-More, How-To-Start-on-YouTube)
Batch 59. 4 of 8 fetched (4 on 429: YCGRzMN9gEE, aDLmEezhnG0, UmgtWZfPA4o + new 2sqUDzorHLU "Why I Don't Have A Business Partner Anymore" [biography-relevant — retry]). Ingested 4 to L2 — Chris-heavy, 3 ★L3. L2 389->393.
- ★ Packaging Design Challenge – Young Guns S2 Ep4 — Chris framing (~25-30%; students introduce picks=context). NEW design-craft: packaging judging-criteria (higher-end AND mainstream appeal, appetite appeal, shelf standout, features/benefits, appropriateness); "perception of value" exercise (read colors/materials → guess price → verify alignment); buyer × brand-attributes overlap = "the sweet spot"; design for values-alignment (Sinek "buy why you do it"); teaching-method meta (withholds coaching on 1st challenge for an uncoached baseline). Caption garble flagged (colors-changeable line contradicts the brief) (fmaiTM-sCW0).
- How To Charge More? — coaching (coachee=context). NEW (mostly reframes existing pricing via MINDSET): charging is gated by a SELF-WORTH limiting belief not a market ceiling; education≠worth (a degree only signals ability-to-pay/get-in/finish; Danny Yount & Doyald Young were self-taught masters); objection-by-INVERSION ("that's not valuable? ok — what IS? maybe I can help with that"); "invent SYSTEMS to resolve any client objection" (burned-by-comms → 24h-response-guarantee + cell#); can't convince a client to switch value-positions (high-vs-low-stakes value the same work differently). Not L3 (7xpuDBMLFs0).
- ★ Package Design Critique Part 1 – Young Guns Ep5 — Chris SOLE critic (Melinda absent this ep); students=context. NEW design-craft: 5-criteria packaging rubric (high-end feel/appetizing/shelf-presence/features/appropriateness); "observe the original WITHOUT judgment or attachment" first; 3 sources of contrast (value [black/white highest], size+complexity, texture/tonal); repositioning = near-free MARGIN leverage on white-label goods (+25¢ moves the bottom line); "don't hide the brand" (Ford-in-the-corner analogy); food must not read clinical/sterile (cold-blue/dot-grid = medicine look); elevate via materials/print-finishes + "billboard effect of the shelf"; packaging-as-rocket-ship storytelling (credits "books are rocket ships" to Brian Collins); cultural-authenticity over Western pastiche (commission real calligraphy). Refs: Warhol, Charles S. Anderson, Designers Republic (vomjcfFKHoE).
- ★ Designers Ask How To Start on YouTube — w/ Melinda Livsey + Raoul — Chris ~70-80% coaching 2 Pro-Group members launching a show (Melinda + Raoul=context). NEW content-strategy YouTube-launch playbook: beginner length 4-9min (10 too long; Futur avg ~9, YT avg ~5); "ask for comments WITH a timestamp" (credits Gary Vee); personality>information (entertainment↔education spectrum, Julia-Child→Gordon-Ramsay); "structure the show BEFORE the content" (show-map-first); on-camera training = actively MIMIC performers (Chris Rock pacing, Graham Norton) as muscle-memory; "the 10% you're scared to show is the 10% that makes it 100%"; expectation-management ("first 10 episodes we're gonna be terrible"; "happiness is inversely proportionate to expectations"). Cites GaryVee/Draplin/MKBHD/DeFranco/Rogan as examples (N3hHRYhQRwo).
Attribution: 3 Young Guns/panel (Melinda/Raoul/Ricky/students=context) + 1 coaching (coachee=context); 3 new ★L3-candidates. No family names. Counts: L2 389->393.
Synthesis notes: NEW (debt 4/10) — (1) design-craft/branding: PACKAGING-design cluster now rich (Ep4 challenge criteria + perception-of-value + buyer×brand-overlap; Ep5 5-criteria rubric + observe-without-judgment + 3-contrasts + don't-hide-brand + materials/finishes + packaging-as-rocket-ship [Brian Collins] + cultural-authenticity) — strong promote to design-craft (packaging section) + branding; (2) content-strategy: YouTube-LAUNCH playbook (4-9min, personality>information, structure-before-content, mimic-creators/muscle-memory, expectation-management, "10% you're scared of") — promote to content-strategy (his own media playbook); pairs with existing YouTube-playbook material; (3) pricing/mindset: charging gated by self-worth + education≠worth + objection-by-inversion + systemize-the-objection-away — promote to pricing + mindset (self-worth link). ENTITY: Brian Collins (already have a page — deepen: "books are rocket ships"); Doyald Young (type-design master, possible entity). Rate-limit: 4 persistent-429 rows (YCGRzMN9gEE, aDLmEezhnG0, UmgtWZfPA4o, 2sqUDzorHLU).

## [2026-07-18] ingest | yt batch (@thefutur, 5) — P2 Apr/Jun-2019 (self-confidence, Young Guns S2 package-critique-2+accountability, build-audience w/Melinda; 1 non-Chris)
Batch 60. 5 of 8 fetched (UmgtWZfPA4o cleared; 3 on 429: YCGRzMN9gEE, aDLmEezhnG0, 2sqUDzorHLU). Ingested 5 to L2 — Chris-heavy, 4 ★L3. L2 393->398.
- ★ Power of Self Confidence & Overcoming Imposter Syndrome — Chris Q&A. NEW vs existing self-confidence corpus: true confidence = accepting BOTH strengths AND flaws (not pretending all of you is good); imposter self-honesty test ("you can't lie to yourself; you know when you're faking"); BINARY serve/not-serve filter for others' opinions; "people buy YOU before they buy your product — always"; signals are audience-RELATIVE (same trait reads square to one tribe, integrity to another); embrace-contradictions as legit identity. audience("Aaron")=context (UmgtWZfPA4o).
- ★ Package Design Critique Part 2 – Young Guns Ep6 — Chris sole critic (Encina brief mango consult; Melinda absent). NEW beyond Ep5: typography OPTICS (horizontals must read optically thinner, stretching a face = "typography violation", flourishes trap negative space, set body RAGGED not force-justified b/c "rivers"); mockup-discipline ("mockups make or break your presentation", X-Acto craft); "appetite appeal" named criterion (imagery must show what product IS); brand-HERITAGE leverage (ownable "est. 1912" story — don't erase 100 yrs, fix hierarchy); contrast-of-volumes (4/5 vs 1/5). NEAR-CONTRADICTION w/ Ep5 flagged: cliche (Greek key) OK "if it communicates". students=context (tS7fF7NKoRQ).
- ★ Build Your Audience and Connect – w/ Melinda Livsey — Chris + Melinda(context). NEW: 3-LEARNING-STYLES framework (high-level / story / kinesthetic) + lesson-design rule (concept → personal story → tactical DIY, "lace your fingers" demo); "teach while you LEARN, not what you know" (experts make bad teachers; Bob Ross vs Van Gogh; self-IDs as high-level learner/"worst kind of teacher"); belief-PRECEDES-results ("body listens to the mind", trigger "could be 100% fabricated" and still work = "your truth"); "heart broken OR mind opened" = 2 drivers of change; compelling-event catalyst; innovation-vs-iteration self-critique; "hold strong beliefs loosely"; "failure & invention are inseparable twins" (Bezos). Melinda=context (2ju9b4SgvoQ).
- ★ Improvement, Accountability, & Focus – Coaching Young Guns S2 — Chris coaches 6 designers (Ricky co-host=context). NEW: "just to the ___" small-steps technique (aim only for the next lamppost); SMART self-brief method (write 5 specific briefs in 1 niche, roll a die, commit w/ deadline); memento-mori accountability ("#1 thing wrong w/ young people: you think you have time... you're gonna die"); remote-client thesis (depth of conversation > physical proximity; demonstrate care via recordings/notes/summaries); royalty pricing (packaging $5-20k; 3 structures — upfront-w/-discount / installments / licensing $5k + 2% of what they MAKE; royalty leverage only when irreplaceable); "designers assume, professionals ask"; "say the price like a fact". BIG BIOGRAPHY: 47yo, company 23 yrs, 4 seasons of UFC "Ultimate Fighter" title sequences, 3 films w/ Stacy Peralta, first-ever Quiksilver commercial, recently lost father-in-law, has a (video-game-playing) son [family unnamed]. students=context (eQo2UPIRxZo).
- 3 Ways to Reclaim your Creativity and Productivity — ⚠️ NOT CHRIS: Matthew Encina (CD, Adobe 99U recap: focus-sprints [Dr. Sahar Yousef] / better-brainstorms [Duncan Wardle] / beautiful-boredom). do-not-train-persona (Futur context). Not L3 (ybaom7OVtIw).
Attribution: 1 do-not-train (Encina) + 2 Young Guns/coaching (Ricky/students=context) + 1 Melinda dialogue (fenced) + 1 Chris Q&A; 4 new ★L3-candidates. No family names (son/father-in-law unnamed). Counts: L2 393->398.
Synthesis notes: NEW (debt 5/10, halfway) — (1) mindset: true-confidence=accept-flaws + binary-serve-filter + embrace-contradictions (self-confidence) AND "just to the ___"/SMART-brief/memento-mori (accountability) AND belief-precedes-results/heart-or-mind/hold-beliefs-loosely (Melinda) — strong mindset cluster; (2) content-strategy/mindset: 3-LEARNING-STYLES + teach-while-you-learn-not-what-you-know — strong teaching-philosophy promote (pairs w/ existing content/teaching material); (3) design-craft: PACKAGING cluster completes (Ep6 typography-optics + mockup-discipline + appetite-appeal + brand-heritage + cliche-if-communicates) — big design-craft promote w/ Ep4/Ep5; (4) pricing: royalty/licensing structures ($5k+2%, packaging $5-20k) — promote; (5) BIOGRAPHY (rich): 47yo/23-yr-company (2019) + 4-seasons-UFC-Ultimate-Fighter + 3-Stacy-Peralta-films + first-Quiksilver-commercial + lost-father-in-law + has-a-son — significant biography/filmography enrichment (Blind client work). Rate-limit: 3 persistent-429 (YCGRzMN9gEE, aDLmEezhnG0, 2sqUDzorHLU).

## [2026-07-18] ingest | yt batch (@thefutur, 5) — P2 Jun-Jul-2019 (Young Guns S2 book-cover challenge+critique; 3 non-Chris: PM series, Building-A-Brand doc, motivation montage)
Batch 61. 5 of 8 fetched (3 persistent 429: YCGRzMN9gEE, aDLmEezhnG0, 2sqUDzorHLU — stuck 3rd+ batch). Ingested 5 to L2 — instructor/produced-heavy era, only 2 Chris ★L3. L2 398->403. Crosses into July 2019.
- Product Management - What is PM — ⚠️ NOT CHRIS: Futur PM interview series (hosts Matthew+Sina; guest Justin Zaccardi/Tonal; editor Mark Contreras). do-not-train-persona (Futur context). MVP/jobs-to-be-done/conductor-metaphor all guest's. Not L3 (YIz774Gjo1E).
- A Better Way to Present to Clients – Building A Brand Ep5 — ⚠️ NOT CHRIS: "Building A Brand" documentary of a real Blind rebrand (Hamilton Family Brewery); Blind employees Ben+Matthew present 4 style-scapes to clients Josh/Kristen. Ideas (style-scapes-as-conversation-starters, descriptor-naming-frames-perception, involve-client-every-step, "I thought I had to have all the answers—wrong") ECHO Chris's teaching but are spoken by EMPLOYEES → context, do-not-train. Not L3 (54o73NXCfTk).
- ★ Book Cover Design Challenge – Young Guns S2 Ep8 — Chris frames+judges (students=context). NEW: 4-criterion book-cover rubric (CONCEPT/"aha moment"/"image within the image" > convey-main-theme > shelf-presence > cohesion); "design's job = draw somebody & get them curious enough to spend money"; reduce any story to a core conflict (man-vs-nature/man/time/himself) then find nuance/"read between the lines"; study the CONCEPTUAL FRAMEWORK behind inspiration (double-exposure/hidden-silhouette) not the execution; "communicator of truth — if you don't understand it you're just making stuff up" (MITy9UGnKt8).
- ★ Book Cover Design Concepts Critique – Young Guns S2 Ep9 — Chris sole critic (students=context). Most concentrated CONCEPTUAL-DESIGN statement yet. NEW: semiotics as the engine ("A+B=C", "1+1=3" — juxtaposition creates new unexpected meaning); "find the idea FIRST, then design the system around it"; layered reads (reward 1st/2nd/3rd read); "the cover is the hero" (don't let the back steal the job); ideas come only from TRUE understanding (read critical analysis → reduce to 2-3 words → "your truth"); "free yourself of physical reality" (a book can be big as a building); hand-crafted humanity > "the digital edge cheapens the design"; photo-ref workflow (shoot/cut/high-contrast then trace, but don't make photography THE solution); "No pressure, no diamonds" / putty→iron→steel / "I'm here to help you not break you"; "the best designers I know are self-taught"; public-critique = career/lead engine. Influences: Olly Moss (negative-space), René Magritte/surrealism (2HY_vl9a6JA).
- Respect The Hustle — Motivation Video — produced spoken-word montage (persistence/resilience for non-traditional creatives). ⚠️ uncredited narrator, attribution:uncertain → do-not-train-persona. Not L3 (SMri3o96ppI).
Attribution: 3 do-not-train (Futur PM series NOT Chris; Building-A-Brand doc = Blind employees; motivation montage uncredited) + 2 Chris-led ★ (both Young Guns book-cover); 2 new ★L3-candidates. Excellent attribution discipline in an instructor-heavy era. No family names. Counts: L2 398->403.
Synthesis notes: NEW (debt 6/10) — (1) design-craft: BOOK-COVER + CONCEPTUAL-DESIGN cluster (Ep8 4-criterion rubric + reduce-to-core-conflict + study-framework-not-execution; Ep9 semiotics A+B=C/1+1=3 + find-idea-first + layered-reads + cover-is-the-hero + your-truth + free-of-physical-reality + hand-crafted-humanity) — strong promote to design-craft (conceptual-design section); pairs w/ the packaging cluster (Ep4/5/6) for a big design-craft pass; (2) design-craft/voice: "no pressure no diamonds", "best designers are self-taught", "design's job = draw curiosity", "communicator of truth" — voice.md candidates; (3) ENTITY: Olly Moss (poster/negative-space designer), René Magritte (surrealist) — influence candidates. CONTEXT/NON-CHRIS logged (NOT persona): Futur PM series (Matthew/Sina/guests), Building-A-Brand Blind doc (Ben/Matthew employees) — but the Building-A-Brand series is useful ENTITY/Blind-process context. Rate-limit: 3 persistent-429 rows STILL stuck (YCGRzMN9gEE 'Taking Risks', aDLmEezhnG0 'Losing A Big Job' photographer, 2sqUDzorHLU 'Why I Don't Have A Business Partner Anymore' — last is biography-relevant).

## [2026-07-18] ingest | yt batch (@thefutur, 5) — P2 Jul-2019 (How-To-Get-A-Promotion, Young Guns book-cover FINAL; 3 non-Chris Building-A-Brand Blind docs)
Batch 62. 5 of 8 fetched (3 persistent 429: YCGRzMN9gEE, aDLmEezhnG0, 2sqUDzorHLU). Ingested 5 to L2 — 2 Chris ★L3 + 3 Blind-doc context. L2 403->408.
- Top 4 Webflow Tips – Building A Brand — ⚠️ NOT CHRIS: unnamed Blind/Futur team member (Webflow tutorial: Flexbox/CMS/symbols/hover). do-not-train (Futur context). Org-note: Futur adopted Webflow, planned WordPress→Webflow migration ~mid-2019. Not L3 (8FMb2DETdgw).
- ★ How To Get A Promotion — recorded internal COACHING of Chris's own Futur team (Ricky + team=context). Chris = coach/boss (all teaching). NEW promotability model (employee-side value, new audience angle for his value philosophy): do-your-homework so guesses are EDUCATED (research/data > feelings); be self-directed; SELF-DIRECTION MUST ALIGN with company goals ("tropical forest in the back room" = unaligned initiative wasted); "anticipate the next steps — the more steps you anticipate, the greater your value" (garbage-can/root-cause analogy); GENERATE the ideas that become directives = BOTTOM-UP management ("best ideas come from you guys"). Results-over-process reinforced (client parallel). team=context (fAkRgRHRRms).
- Designing A Beautiful Beer Can – Building A Brand Ep9 — ⚠️ NOT CHRIS: Blind employees (Ben Burns, Matthew Encina, intern Jun; clients Josh/Kristen). do-not-train. BLIND-process/entity context: "brand strategy design consultancy, Santa Monica, since 1995"; Ben Burns' $100K wrong-barcode war story → QA "check 3 times" culture; packaging-as-sales (alcohol sells on packaging); "show them something bad so they know what's good"; retail hierarchy (flavor above logo). Not L3 (KcnslNdyFI0).
- ★ Book Cover Design Challenge FINAL Critique – Young Guns S2 Ep10 — Chris critic (students=context; a 2nd unnamed co-critic flagged uncertain). NEW beyond Ep8/9: "READ IT LIKE AN IDIOT" (critique by describing ONLY what's literally visible — the shelf/Amazon browser never gets your explanation; "design, like typography, is thought made visual"; don't let designers justify); ONE-WORD ESSENCE (reduce smaller & smaller until you pull the essence); LEAVE CLUES / legible patterns (viewers should predict the next beat; illogical progression breaks it); positive/negative-space "the deeper you go the more you're rewarded" (Absolut bottle silhouette, Beauty-and-Beast rose petals = Beast/Belle); CONTRAST to survive the shelf (add black/white to low-contrast; or add contrast in the presentation background); use the PHYSICAL BOOK FORM as the concept (R&J spread pulls clasped hands apart); judge graphic-power vs conceptual-thinking separately (good idea ≠ good execution) (EQWsDA8D-54).
- Making the Perfect Beer Commercial – Building A Brand Ep10 — ⚠️ NOT CHRIS: Matthew Encina + Ben Burns (clients Josh/Kristen). do-not-train (the "music tells you how to feel / my 3-year-old" line is ENCINA's, not Chris — misfiling trap flagged). BLIND video-process context (3-stage pre/pro/post, overshoot discipline, boom+lav, Epidemic Sound; split-interview Kristen=heart/Josh=business). Not L3 (pRDfov1dbj0).
Attribution: 3 do-not-train (Building-A-Brand Blind docs = Encina/Burns/team, NOT Chris) + 2 Chris-led ★ (promotion coaching + book-cover final); 2 new ★L3-candidates. Strong discipline; the whole Building-A-Brand series is Blind-employee documentary = entity context, not persona. No family names. Counts: L2 403->408.
Synthesis notes: NEW (debt 7/10) — (1) design-craft: BOOK-COVER cluster COMPLETES (Ep10 final adds "read it like an idiot"/thought-made-visual, one-word-essence, leave-clues/legible-patterns, neg-space-rewards, contrast-to-survive-shelf, physical-form-as-concept, graphic-vs-conceptual) — with Ep8/Ep9 + packaging Ep4/5/6 this is a LARGE design-craft promotion for pass 7 (conceptual-design + packaging + critique-method sections); (2) business/mindset: employee-side "how to be more valuable / get promoted" model (educated-guesses, alignment-gates-self-direction, anticipate-steps=value, bottom-up-management) — new audience angle, promote to business + beliefs; (3) design-craft/voice: "read it like an idiot", "design is thought made visual", "the deeper you go the more you're rewarded" — voice candidates. ENTITY debt: Blind (entity page now strongly warranted — Building-A-Brand series gives rich process/employee context: Ben Burns + Matthew Encina as creative directors, QA culture, "since 1995 Santa Monica"), + Hamilton Family Brewery (client, minor). CONTEXT logged, NOT persona: all 3 Building-A-Brand docs. Rate-limit: 3 persistent-429 STILL stuck (YCGRzMN9gEE, aDLmEezhnG0, 2sqUDzorHLU).

## [2026-07-18] ingest | yt batch (@thefutur, 6) — P2 Apr/Jul-Aug-2019 (Yvette-photographer interview, expertise-while-learning, IG-necessary, work-on-yourself; 2 non-Chris)
Batch 63. 6 of 8 fetched (aDLmEezhnG0 cleared; 2 on 429: YCGRzMN9gEE, 2sqUDzorHLU). Ingested 6 to L2. L2 408->414. Crosses into Aug 2019.
- Losing A Big Job Was The Best Thing To Happen To This Photographer — Chris interviews photographer Yvette (lost a camera-brand job for ~1k IG followers vs ~50k wanted; her account doubled after going public). Chris NEW content-strategy: FEED-vs-STORIES doctrine (feed = "precious", curate consistent aesthetic/voice; stories = ephemeral, experiment/find your voice); "gatekeepers are gone" (blessing + threat); EARNED-vs-BOUGHT followers (engagement exposes fakes; ambassadors won't work w/ low engagement); advertising-is-dead → branded-content shift (ad $ TV→influencers); vulnerability-sells (Sinek). BIO: bullied growing up (fueled defending her online). Yvette=context (entity if she recurs) (aDLmEezhnG0).
- Work On Yourself More Than On Your Job (2-Min Motivation) — Chris montage. NEW: Jim Rohn "work on yourself WAY harder than on your job" (uncredited — link influence); "don't live up to the titles you HAVE, live up to the title you WANT"; "what you do in your free time... I'll tell you what you become"; stated emotional-DETACHMENT preference ("no emotions, objectively cut everything; attachment = route to disappointment"); "getting things done > being right"; skip the invisible last 5-10% polish. Not L3 (Uu29Tb2Cilg).
- Be a Better Designer. Learn to Communicate – Young Guns S2 Ep13 — ⚠️ NOT CHRIS: hosted by an unnamed Futur member (refers to "Chris" in 3rd person throughout: "even the way Chris talks... comfortable in silence"; "next episode with Chris"; plausibly Encina but uncertain). do-not-train. "creativity is a rubber band" metaphor is SECONDHAND-Chris (uncertain) — must be sourced from a first-party video, NOT from here. Not L3 (IqxpgnYf1_Y).
- Beer Brewery Makeover – Building A Brand Ep11 (S1 FINALE) — ⚠️ NOT CHRIS: Ben Burns + Matthew Encina (clients Josh/Kristen). do-not-train. RICH BLIND/entity context: brand reveal + retail results (cans into 5 BevMo, ~20% quarterly growth, new hires); series ORIGIN (Ben Burns pitched Chris ~1yr prior to document a rebrand for a couple who "can't afford Blind services"; Chris FUNDED it as a "test experiment"); education-funnel→agency PIPELINE (owner found Futur via YouTube DIY logo → hit "kerning" competence wall → called parent-co Blind); brand-style-guide deliverable model + the "clients warp it" designer fear. Not L3 (pOdBeS43W0A).
- Is Instagram Necessary For Work? – Young Guns S2 Ep12 — Chris coaches Megan+Anastasia (Encina intro/outro + students=context). NEW: IG is OPTIONAL for a design business (long game not instant hiring); "public journaling" feed framing (post for yourself — win/lesson/joy); reverse-engineer successful accounts (even ones you dislike) into abstract frameworks (+ Jim Rohn "success leaves clues"); "LUMPY MAIL" physical outreach (credits Allan Dib/1-Page-Marketing-Plan — cuts through digital clutter now everyone's in DMs); "DON'T give a gift YOU like" (a self-promo piece is a gift to yourself — make it about the recipient; coffee-from-your-country, design-on-a-dollar-bill "not a bribe"); effort-is-rewarded (intern hired off a funny brand-aware application video). Not L3 (restated) (5w9Ld8_X5Bc).
- ★ How To Build Expertise While Learning — Chris solo. NEW: EXPERTISE = life-experience + knowledge + skills (knowledge from "no more than five books"); 10,000-hours REFRAME + dual "expert" definition (strict vs popular: "someone who knows a little more than you" / a coach who helps you reach your optimum); DOMAIN-EXPERT SHORTCUT (interview 2-3 domain experts, learn the QUESTIONS they'd ask, get good at "top-level conversations" not details); imposter-syndrome reframed as THEFT (refusing to share robs others of help); "DON'T EDIT what you give" (share the full thing); "I'm still figuring it out, come along on the ride, we'll grow together" authenticity posture (MKBHD/Logan Paul/Casey Neistat "audience grows up with you"; Chris "the anomaly"/older on YouTube). L3-candidate (Mj1PhPKkERY).
Attribution: 2 do-not-train (Young Guns Ep13 non-Chris host; Building-A-Brand finale = Blind employees) + 1 guest-interview (Yvette=context) + 3 Chris-led (2 coaching w/ students-context + 1 solo); 1 solid ★L3 + 1 partial. No family names. Counts: L2 408->414.
Synthesis notes: NEW (debt 8/10, checkpoint ~2 batches out) — (1) content-strategy: SOCIAL-MEDIA/personal-brand cluster (feed-vs-stories, earned-vs-bought-followers, "public journaling", IG-optional/long-game, reverse-engineer-into-frameworks, lumpy-mail outreach, "don't give a gift you like") — promote to content-strategy (his media playbook); (2) mindset/content-strategy: "teach/share BEFORE you're an expert" thesis + expertise-formula + domain-expert-shortcut + imposter-syndrome-as-THEFT + "don't edit what you give" — strong teaching-philosophy promote (pairs w/ 3-learning-styles + teach-while-you-learn from batch 60); (3) mindset/business: "work on yourself harder than your job" (Jim Rohn), "live up to the title you want", emotional-detachment — promote to mindset/business + beliefs; (4) BIO: bullied-growing-up (corroborates outcast/insecurity origin). ENTITY debt (STRONG now): entities/blind (Building-A-Brand S1 gives origin+process+funnel+team) + Ben Burns + Matthew Encina (recurring Blind CDs) — create at pass 7 checkpoint. Rate-limit: 2 persistent-429 (YCGRzMN9gEE, 2sqUDzorHLU — the latter biography-relevant).

## [2026-07-18] ingest | yt batch (@thefutur, 6) — P2 Aug-Sep-2019 (learn-faster, branding-vs-marketing, good-vs-great-companies; 2 non-Chris PM + 1 montage)
Batch 64. 6 of 8 fetched (2 persistent 429: YCGRzMN9gEE, 2sqUDzorHLU). Ingested 6 to L2. L2 414->420. Crosses into Sep 2019.
- Things I learned as a Young Designer – Young Guns S2 finale — MIXED montage; participants narrate their own stories (one: "each critique we received from Chris" = 3rd-person → context); probable-Chris mentor lines flagged uncertain (restatements: don't-compare-to-highlight-reel, say-most-with-least, conceptual-thinking-is-hard). Low-signal. Not L3 (pO60YfDG6s8).
- (Don't) Question Everything — How to Learn Faster — Chris (+editor Aaron=context). NEW (in TENSION w/ his usual learn-by-modeling/question-asking): "the trait that made me a great student = I did everything my coach told me WITHOUT question"; names the cynical "question everything" voice as Steven Pressfield's RESISTANCE / the obstacle to learning; Aaron's reconciling frame (time to ask when searching for mentors/ideas vs time to stop & absorb) = context. BIO: ~$250k over ~10 yrs on weekly coaching (corroborates Kier McLaren long coaching relationship). Soft-L3 (MtTwqk-0zG4).
- 3 Tips to Get Your Work Done on Time — Project Management — ⚠️ NOT CHRIS: unnamed Futur team member/instructor (assigns tasks to "Ben" 3rd-person; "if I was managing a video team I have no knowledge of how to make videos"). do-not-train. 1-page-brief/expectations+buy-in/padded-internal-deadlines. Not L3 (caS7SxmAbdo).
- No More Revisions! Working With Clients — Project Management — ⚠️ NOT CHRIS: two Futur team members (one "UI designer by trade"; Chris never speaks). do-not-train. 5-sentence-email-rule (>5 sentences → call; reclaimed ~12hrs/wk), decision-tree "breadcrumbs" + round "2 of 3" labeling, reusable email-template arsenal (Futur process context). Not L3 (xoOo1bjYsKs).
- ★ What Is The Difference Between Branding & Marketing? — roundtable reacting to a Donald Miller/StoryBrand clip (Chris HOST + Fabian Geralt/brand-strategist + Melinda/moderator=context). Chris NEW: positioning = "the art/strategy of occupying a space, a position in a person's MIND"; branding & marketing are CONVERGING "blood cousins, maybe twins" ("swap the word branding for marketing and you'll be okay") — explicit ANTI-tribalism; approves Seth Godin's modern marketing def ("generous act of helping others achieve their goals") vs old repetition/control-the-dialogue; Allan Dib marketing-activity taxonomy (promotion/publicity/PR/advertising/sales); Neumeier Brand-Flip 4 brand-strategist skills (visual/verbal/30k-ft/co-create); "what design schools call branding is really identity/design systems; most 'branding people' only do logos, not positioning"; "only client-business impact matters". Fabian Geralt entity candidate (L3-candidate).
- ★ The Difference Between Good & Great Companies — Chris solo (filmed on a Geneva/Milan Digital Design Days speaking trip). NEW landmark: CUSTOMERS vs AUDIENCE thesis (all companies have customers you PAY to reach via ads; great ones have an AUDIENCE / true fans who give attention FREELY) + The Futur's stated success formula = 3 principles: BE CONSISTENT, GIVE GENEROUSLY, SERVE OTHERS; "stop selling, start CELEBRATING" (be a champion for those you serve); Seth Godin smallest-viable-audience + market-first inversion (find market → problem → solution, not reverse); Austin Kleon "documentarian of your own work" (Show Your Work!); Terry Crews "action beats intent", GaryVee "execution is the game". Garble flagged ("$50→$200k/12mo" ambiguous — not asserted). L3-candidate (zSVlMER-zfE).
Attribution: 2 do-not-train (both PM-series team members) + 1 mixed montage (participants=context, mentor-lines-uncertain) + 1 roundtable (Fabian/Melinda=context) + 2 Chris-led (1 solo talk + 1 w/ editor); 3 new ★L3-candidates. No family names. Counts: L2 414->420.
Synthesis notes: NEW (debt 9/10 — SYNTHESIS CHECKPOINT DUE NEXT ITERATION, Stage S pass 7 → system-prompt v8) — (1) content-strategy/branding LANDMARK: customers-vs-AUDIENCE + 3-principles (consistent/generous/serving) = The Futur's success formula ("good vs great companies") + "stop selling start celebrating" — big promote to content-strategy + beliefs; (2) branding: positioning-def "space in the mind" + branding/marketing-convergence "blood cousins" anti-tribalism + Godin-marketing-def + Neumeier-4-skills — promote to branding; (3) mindset: "do what the coach says WITHOUT question" / resistance-as-obstacle (TENSION callout w/ learn-by-modeling/question-asking — reconcile by context: absorb-from-a-chosen-mentor vs question-when-searching) — promote to mindset w/ contradiction flag; (4) content-strategy: social-media cluster from batch 63 (feed-vs-stories etc) + teaching-philosophy (expertise-formula, share-before-expert) still queued. ENTITY debt for pass 7: entities/blind + Ben Burns + Matthew Encina (strong) + Fabian Geralt (brand strategist, recurring w/ Chris). Rate-limit: 2 persistent-429 (YCGRzMN9gEE 'Taking Risks', 2sqUDzorHLU 'Why I Don't Have A Business Partner Anymore' — biography-relevant, stuck many batches).

## [2026-07-18] ingest | yt batch (@thefutur, 6) — P2 Sep-Oct-2019 (innovate-dont-iterate, find-heroes; Design-From-Scratch series + Gerson = context)
Batch 65. 6 of 8 fetched (2 persistent 429: YCGRzMN9gEE, 2sqUDzorHLU). Ingested 6 to L2. L2 420->426. Crosses into Oct 2019.
- ★ Are you Becoming Obsolete? Innovate Don't Iterate – Chris Do — Chris solo keynote (expands the batch-60 innovation-vs-iteration mention). NEW: DEFINE BY PURPOSE not what-you-do (case set: Western Union / Blockbuster / Tower Records / Kodak defined by product → died); EMPATHY EXERCISE (day-in-the-life grid → task / gap / opportunity; "write it as an opportunity not as work"; "gap = a problem everybody ignored"); The Futur's white-space origin (charismatic amateurs vs award designers who won't teach); "12 one-week projects instead of one 12-week project"; "long-term business plans are a fantasy — pick a direction, adjust"; "a thousand wrong decisions beats no decision"; "space to be bored"/unplug for incubation; "run towards your fear" (coach); windshield-vs-rearview. BIO: YouTube start "~2014", ~15yrs teaching ArtCenter. L3-candidate (SKlCnawfQQE).
- Design From Scratch Ep1 (We Can't Agree on a Direction) — ⚠️ Futur documentary (rebuild thefutur.com in Webflow); multi-speaker (narrator=Greg Gunn?/uncertain, Matthew Encina, Ben Burns, freelancer). Chris = CHARACTER (2 short lines, discussed 3rd-person) → do-not-train. "PASSIONATE DETACHMENT" (separate create-mode from critique-mode, athlete-watching-game-tape) = reported-Chris phrase (flagged, promote only if it recurs first-party). CONTEXT: on-record Ben-vs-Chris tension (Ben=money/conversions, Chris=why-story). Not L3 (DGGUB_XlH8k).
- Design From Scratch Ep2 (Responding to Criticism) — ⚠️ Futur website doc; team members (Jamie/Ben), Chris doesn't clearly speak → do-not-train. Futur critique-culture context (separate self-worth from work). Not L3 (R8vbQR9et_Y).
- Design From Scratch Ep3 (Website Ready to Launch?) — ⚠️ Futur website launch finale; team (Greg Gunn self-ID'd narrator + Sayed/Craig/Ben/Jaime); Chris = INTERNAL CLIENT/reviewer only (rejects the build for not matching the approved style-scape, questions ROI on man-hours, gives MVP sign-off) → do-not-train (low-conf context; the "presentation tip" is Greg Gunn's, NOT Chris). Not L3 (KJfB1GLGZPQ).
- Gratitude Changes Everything w/ Errol Gerson — ⚠️ 100% Errol Gerson (thank-your-bed practice → breakthrough w/ girlfriend + reconciled w/ estranged father after 12yrs). Chris ABSENT from this cut → do-not-train (Gerson context). Not L3 (YOq_VPgK6t0).
- ★ Why You Don't Need A Mentor—Find Heroes — MULTI-SPEAKER montage. Chris reframe: mentors DON'T SCALE (~2000 askers per successful person) → find HEROES who don't need to know you exist; "hijack them" without permission, use "what would X do?" as a compass; "you don't need a mentor when you can have many heroes". GaryVee ("35 DMs 'be my mentor'... mentor-thirsty = excuse not to do") + 1 UNIDENTIFIED speaker w/ a mentorship-bio that does NOT match Chris (flagged, kept OUT of biography). ⚠️ SOFT TENSION w/ his batch-50 "how to get a mentor" material — reconcile/date at synthesis. L3-candidate (Chris parts) (cbwSXFNATOY).
Attribution: 4 do-not-train/context (3 Design-From-Scratch team docs + Gerson 100%) + 2 Chris-led ★ (innovate-keynote solo + find-heroes Chris-parts); 2 new ★L3-candidates. STRONG discipline: 2nd Futur documentary series (Design From Scratch, like Building A Brand) correctly fenced. No family names. Counts: L2 420->426.
Synthesis notes: NEW (debt 10/10 — SYNTHESIS CHECKPOINT NOW DUE, Stage S pass 7 → system-prompt v8) — (1) mindset/business: INNOVATE-don't-ITERATE (define-by-purpose, empathy-exercise task/gap/opportunity, 12-one-week-projects, "1000 wrong decisions beats no decision", run-towards-your-fear) — strong promote to business + mindset + beliefs; (2) mindset: FIND-HEROES-not-mentors (mentors-don't-scale, hijack-them/what-would-X-do compass) — promote to mindset w/ TENSION callout vs get-a-mentor (reconcile: heroes=self-directed-modeling-at-scale, mentor=chosen-close-relationship); (3) mindset (reported): "passionate detachment" (create-vs-critique mode) — hold, promote only if first-party recurs. ENTITY debt for pass 7 (LARGE): entities/blind + entities/the-futur (Design-From-Scratch + Building-A-Brand give rich process/culture/team context) + Ben Burns + Matthew Encina + Greg Gunn (recurring Futur team) + Fabian Geralt + Errol Gerson (recurring guests). Rate-limit: 2 persistent-429 STILL stuck (YCGRzMN9gEE, 2sqUDzorHLU).

## [2026-07-18] lint | synthesis pass 7 — @thefutur P2 Apr→Oct-2019 (batches 56–65, L2 378→426) → system-prompt v8
Checkpoint synthesis over ~10 ingest batches. Fanned out 13 agents (one per file, concurrency rule) + 1 system-prompt recompile. ENRICHED all 7 topic hubs + 3 persona files + 3 entity pages; recompiled persona/system-prompt.md v7→v8 (compiled_from 378→426).
- **design-craft** +2 big sections: PACKAGING trilogy (Ep4/5/6 — 5-criteria food rubric, perception-of-value, observe-without-judgment, 3-sources-of-contrast, don't-hide-brand/Ford-in-corner, materials/finishes + shelf-billboard, packaging-as-rocket-ship [Brian Collins], typography-optics; ⚠️ cliché-if-communicates vs anti-cliché callout) + BOOK-COVER/CONCEPTUAL trilogy (Ep8/9/10 — concept-first rubric, semiotics 1+1=3, find-idea-first, cover-is-the-hero, "read it like an idiot"/design-is-thought-made-visual, one-word-essence, neg-space-rewards, physical-form-as-concept; Olly Moss/Magritte).
- **content-strategy** +5: customers-vs-AUDIENCE LANDMARK + 3-principles (consistent/generous/serving), YouTube-launch playbook (4-9min/personality>info/mimic/expectation-mgmt), personal-feed doctrine (feed-vs-stories/public-journaling/lumpy-mail/earned-vs-bought), teach-while-you-learn/3-learning-styles/expertise-formula/imposter-as-theft, one-piece→7-formats; ⚠️ TENSION teach-while-learn(2019) vs teach-what-you've-earned(2025).
- **mindset** +6: innovate-don't-iterate (define-by-purpose/empathy-exercise/12-one-week-projects/1000-wrong-decisions/run-towards-fear), belief-precedes-results/heart-or-mind-opened, heroes-vs-mentors (⚠️ EVOLUTION vs get-a-mentor + ⚠️ TENSION coach-without-question vs question-everything, both reconciled by stage), true-confidence-accepts-flaws, just-to-the-___/SMART-brief/memento-mori, work-on-yourself>job.
- **business** +3: promotability/bottom-up-management (anticipate-steps=value, alignment-gates-initiative), innovate-strategy-angle (define-by-purpose or die), royalty/licensing ($5k+2%).
- **branding** +1: positioning="occupying a space in the mind", branding/marketing "blood cousins" anti-tribalism, Godin-marketing-def, Neumeier Brand-Flip 4-skills.
- **pricing** +3: "double don't inch up" + charge-more virtuous loop, charging-gated-by-self-worth/education≠worth/objection-by-inversion, royalty-structures.
- **sales-clients** +2: cold-DM outreach playbook (resumes/email-dead→DM-top-12, praise-first, "trust your struggle") + lumpy-mail, listen-to-understand/human-tape-recorder-drill/$3k-logo-roleplay (why-this/why-now/why-me per Jonathan Stark).
- **persona**: beliefs +14 (sources 85→98), voice +18 verbatim quotes (sources 51→63), biography (sources 31→37) incl. 47yo/Blind-23yrs-2019 + 4-seasons-UFC-Ultimate-Fighter + 3-Stacy-Peralta-films + first-Quiksilver-commercial (self-reported) + first-AIGA-National-keynote(2019) + Digital-Design-Days-Geneva/Milan + ~$250k-over-10yrs-coaching + bullied-childhood-deepened (name-free son/father-in-law).
- **entities** DEEPENED (already existed, not created): blind (Building-A-Brand + Design-From-Scratch process/culture/origin/education-funnel/Ben-vs-Chris-tension), futur-instructors (Ben Burns/Matthew Encina/Greg Gunn/Ricky Lin/Sina + guest pointers — the ATTRIBUTION GUARD), influences (+11: Russell Brunson, Debbie Millman, Allan Dib, Austin Kleon, Olly Moss, Magritte, Neumeier/Brand-Flip, Pressfield, Bronnie Ware, MKBHD, GaryVee).
- **system-prompt v8**: folded audience-formula/teach-before-expert/YouTube-playbook, innovate-don't-iterate/find-heroes/work-on-yourself/memento-mori, packaging+conceptual design-craft, positioning/blood-cousins, double-don't-inch/self-worth-pricing, promotability, 2019 biography (47/UFC/Peralta/Quiksilver/AIGA); +18 catchphrases, +influences. compiled_from 378→426.
Attribution (heaviest instructor/documentary era): fenced 2 full doc series (Building-A-Brand + Design-From-Scratch = Blind employees Ben Burns/Matthew Encina/Greg Gunn), PM-interview series (Matthew/Sina/guests), Young Guns non-Chris hosts, guests (Melinda, Errol Gerson, Debbie Millman, Stefan Kunz, Yvette, Fabian Geralt, Brenda Milis) — all do-not-train, ledger-flagged. Advanced high-water mark to batch 65 (L2=426). Synthesis debt reset 10→0.
LINT DEBT for next lint pass: (1) "Melinda Livsey" vs "Melinda Livesey" spelling inconsistency across pages; (2) entities/errol-gerson.md + entities/fabian-geralt.md referenced but not yet created (create when they recur). Family names kept out throughout.

## [2026-07-18] ingest | yt batch (@thefutur, 7) — P2 Jan/Oct-Nov-2019 (taking-risks, horse-painter parable, work-alone-wont-get-work; guests Hoodzpah/Bob-Burg + Greg-Gunn promo)
Batch 66. 7 of 8 fetched (YCGRzMN9gEE cleared after many batches; 1 on 429: 2sqUDzorHLU still stuck). Ingested 7 to L2. L2 426->433. Crosses into Nov 2019.
- ★ Taking Risks - Changing Careers — Chris (+audience-Q=context). NEW: relationship-with-RISK / SEEK discomfort (the moment before a breakthrough is filled w/ fear+ambiguity, so seek it); "freedom over security" creed ("I'd rather make a lot less than work for someone else"; "I'm not a guy who works well for other people"); "what got you here won't get you there". BIO (self-reported salary chronology): out of school ~$85k/yr → took a $30k/yr job → quit for no job → freelance → own business. L3-candidate (YCGRzMN9gEE).
- The Most Valuable Thing You Can Do For Your Client — ⚠️ 2-voice unlabeled; primary teaching voice is SOMATIC/therapeutic ("the body has to relax", "feel heard", "abandon all agenda") — NOT Chris's usual sales register → LIKELY A GUEST; attribution:uncertain, do-not-train pending full-video verification. Warmer empathy/presence angle (understanding=the-deliverable) IF later confirmed Chris. Not L3 (AkVX7cJiz7Q).
- ★ 1 Powerful Marketing Tip For Broke Artists — Chris solo. The "HORSE PAINTER" PARABLE: a broke dropping-out illustrator finishes a half-painted horse on-site at the exclusive Paddock Riding Club (LA); by repositioning the SAME work before the right AUDIENCE + coaching her from $100 to $1,000/sitting she booked ~$10K in a day. Lesson = value/price is set by audience + ENVIRONMENT, not the work itself; Wayne Dyer "if you change the way you look at things, the things you look at change". Canonical pricing/positioning story asset. L3-candidate (-JpBRdjffbQ).
- Book As Passive Income Business — Chris INTERVIEWS the Hoodzpah sisters (Amy Hood & Jen Hood)=context (book ~25% income/~75% profit; book→workshops→digital ladder; "too busy = priced too low"). CORRECTION: NOT about Chris's Pocket-Full-of-Do (never mentioned; zero Chris-publishing bio). Chris minor (consistent w/ corpus): self-publish-if-you-have-a-built-in-audience, write-to-discover/clarity-through-articulation, recs Never-Split-the-Difference + Socratic-Selling (labeling-emotion). Not L3 (tjNtQfc7u2A).
- Color for Creatives – NEW Course Promo — ⚠️ NOT CHRIS: presented entirely by GREG GUNN (course creator, "Hi I'm Greg Gunn"). do-not-train. Futur PRODUCT context (color course, Nov-2019 pre-sale, $50 off). Not L3 (FUbuuVJcgMM).
- 4 Reasons Why You Need To Use Empathy In Business – w/ Bob Burg — ⚠️ ~100% GUEST (name title-truncated "Bob B..."; almost certainly BOB BURG / The Go-Giver — Ziglar "help others get what they want" thesis matches). Empathy-as-hard-skill across marketing/spreading-ideas/negotiation/self-reflection; Peter Singer drowning-child paradox. Chris share ~0 (only Pro-Group plug). do-not-train. Bob Burg entity only if confirmed + recurs. Not L3 (AdQQHQdQo8E).
- ★ Your Work [ALONE] Won't Get You More Work – Chris Do & Priscilla — Chris coaches Priscilla (French-born/NY-trained/Utah, Pro-Group, going solo)=context. Core belief stated cleanly: for the ~95% OUTSIDE the top 5%, better WORK ALONE won't get more work → move UPSTREAM to strategic thinking, differentiate via positioning + personal brand, OWN the client relationship, put your face/story forward. NEW illustrations/sourcing: Joshua-Bell-in-the-subway framing/venue argument (via Allan Dib's 1-Page-Marketing-Plan) — "same musician, different venue, different results; you're letting others frame who you are"; explicitly credits Allan Dib for "the mistake creatives make is thinking better work gets more work"; story-and-work-INSEPARABLE (Aaron Draplin, Tibor Kalman); "whoever commands the relationship with the client makes the most money"; "it takes work to get work... a threshold of pain keeps the riffraff out"; beliefs/values-base + mission-top pyramid; Behance search-game (title-for-search + tag-heavily). L3-candidate (sRlJzrDa8Ak).
Attribution: 3 do-not-train/context-led (Greg-Gunn promo NOT Chris; Bob-Burg guest ~100%; uncertain-somatic-voice client video) + 1 guest-interview (Hoodzpah=context, Chris minor) + 3 Chris-led ★ (taking-risks solo, horse-painter solo, work-alone coaching); 3 new ★L3-candidates. No family names. Counts: L2 426->433.
Synthesis notes: NEW (debt 1/10, fresh after pass 7) — (1) pricing/branding: "HORSE PAINTER" parable (price=audience+environment not the work) — canonical story, promote to pricing + a story-bank; pairs w/ positioning-increases-value; (2) branding/content-strategy: "your work ALONE won't get more work" for the 95% (upstream/positioning/personal-brand/own-the-relationship; Joshua-Bell-subway via Allan Dib; story-and-work-inseparable; Behance search-game) — strong promote to branding + content-strategy (personal-brand); (3) mindset: relationship-with-risk/seek-discomfort + "freedom over security" creed — promote to mindset + beliefs; (4) BIO: salary chronology $85k→$30k→freelance→own-business (early-career datapoint). ENTITY: Hoodzpah/Amy+Jen Hood (guest), Bob Burg (guest, if confirmed+recurs), Greg Gunn (Color-course — already on futur-instructors). Attribution-verify item: AkVX7cJiz7Q speaker (somatic voice) — check full video before any promotion. Rate-limit: 1 persistent-429 (2sqUDzorHLU 'Why I Don't Have A Business Partner Anymore' — biography-relevant, stuck ~10 batches).

## [2026-07-18] ingest | yt batch (@thefutur, 4) — P2 Nov-2019→Jan-2020 (work-life-balance, get-more-from-school, perfect-sales-call-script w/Neumeier, self-acceptance)
Batch 67. 4 of 8 fetched (3 auto-marked L1 no-captions: avTemiwR1IA Best-Non-Design-Books, S68b1zbcIg4 Branding-Basics, CbQNwT7FsVg Best-Business-Tip; 1 on 429: 2sqUDzorHLU). Ingested 4 to L2 — all Chris-substantial, 4 ★L3. L2 433->437. Crosses into 2020.
- ★ Find Work-Life Balance – The Struggle — Chris coaches Priscilla (context; Matthew narrator). NEW: COMPARTMENTALIZATION / "walled-off sections" (mommy-work-time vs off-grid family time — thinking about one during the other makes you good at neither); "lifestyle business is a FREEDOM business" reframe (vs "glorified freelancer"); FRONT-LOADED sacrifice (pay systems/protocols upfront → coast later); "increase demand, DECREASE the supply of you" + diminishing-returns ("the work is good enough"); money-buys-freedom (cautionary mid-life friends). BIO: had au pairs from France ~4 yrs while overworking, realized "wasn't present enough" a few years back → changed, happier, works from home, camps/fishes with his boys. "change can happen within 24 hours". L3-candidate (VN_0fy-jXYc).
- ★ How To Get More From School — Chris coaches students (George + others=context; Matthew outro). NEW: 80/20 OF SCHOOL (you learn everything from ~20% of your instructors → concentrate on ~2 of 6 classes); "COLUMN A / COLUMN B" binary instructor-prioritization sort (filters: career-alignment/practicality AND portfolio-worthy-YET-work-you-actually-want); "stop chasing an A in every class — A stands for AVERAGE"; "listen to what you're told but keep only what your own judgment wants". Extends education-is-broken w/ a concrete decision tool. L3-candidate (DK6J9bgj5yc).
- ★ The PERFECT Sales Call Script — Chris × MARTY NEUMEIER (guest=context; branding author, already in influences). Chris asks Marty to re-enact his early cold-call pitch, then dissects it. NEW (vs 5-never/5-rules/SALES/discovery): an actual worked cold-call SCRIPT (disarm → position as CATEGORY SPECIALIST → offer free high-value content [a slideshow] with ZERO pressure → client self-books → over-deliver → own the category); free-slideshow LEAD-MAGNET mechanic; CATEGORY-OWNERSHIP → PRICING POWER (teach clients the questions competitors can't answer); "fish jumps in the boat" + "pushing is a TELL for clients" (desperation signal — reinforces 2019-01-14 don't-go-in-desperate); Marty's price-anchor-HIGH ("quote more than you want, argue down later"). Marty-script/tactics=CONTEXT; Chris commentary=persona. L3-candidate (LEKeZTMp03A).
- ★ My Struggle To Find Self Acceptance — Chris SOLO confessional. BIOGRAPHY (major, deepens childhood-outcast/insecurity): as a kid all he wanted was to be ACCEPTED (not loved/respected) + to stay INVISIBLE so he wouldn't be noticed & bullied at school; years of self-repression/hiding cost him his VOICE + identity; turning point = radical SELF-ACCEPTANCE (lean into quirkiness/crankiness/sardonic humor, be okay w/ haters). Self-descriptors for voice.md: "cantankerous sense of humor", "sardonic", "quirkiness", "crankiness". Stance on haters ("I stand for these people, I don't stand for you") + "come into the light" authenticity framing. L3-candidate (d7V7eJn3-oc).
Attribution: 1 guest-dialogue (Marty Neumeier tactics=context) + 2 coaching (Priscilla/students/Matthew=context) + 1 Chris-solo; 4 new ★L3-candidates. 3 no-caption videos correctly auto-marked L1. No family names (boys/wife unnamed). Counts: L2 433->437.
Synthesis notes: NEW (debt 2/10) — (1) BIOGRAPHY (rich): self-acceptance childhood testimony (wanted-acceptance-not-love, deliberate-invisibility-to-avoid-bullying, repression-cost-his-voice → radical-self-acceptance) — deepen biography.md + voice.md self-descriptors (cantankerous/sardonic/quirky); + work-life-balance life-details (au-pairs-France, works-from-home, camps/fishes-with-boys, "wasn't present enough"→changed); (2) mindset/business: "lifestyle=FREEDOM business" + compartmentalization/walled-off-sections + front-loaded-sacrifice + "increase-demand-decrease-supply-of-you" (work-life) AND 80/20-of-school + Column-A/B + "A=average" (school) — promote to mindset + business; (3) sales-clients: the Marty-Neumeier COLD-CALL SCRIPT + category-ownership→pricing-power + free-content-lead-magnet + "pushing-is-a-tell" — promote to sales-clients (Neumeier attributed) + deepen Neumeier in influences. Rate-limit: 1 persistent-429 (2sqUDzorHLU). Pipeline: 3 rows marked L1 no-captions this batch.

## [2026-07-18] ingest | yt batch (@thefutur, 7) — P2 Jan-Feb-2020 (sales-skills, expertise-vs-mastery, confidence-via-teaching/BURNOUT-origin, hiring-first-employee, 3-pricing-options)
Batch 68. 7 of 8 fetched (1 on 429: 2sqUDzorHLU). Ingested 7 to L2. L2 437->444.
- ★ Most Important Sales Skills To Learn — Chris (Ricky host=context). NEW: the TWIN CONSTRAINT ("it's difficult to think, and it's difficult to make a decision") → the seller's job = help them THINK + remove the FEAR of deciding (the WHY behind ask-questions/listen-more); "the quality of your question determines the quality of knowledge you signal"; Socratic short-leading-questions "excavating information"; epic-vs-intimate naming-the-contradiction example; "clients are MORE afraid of you than you are of them" (Kier McLaren) → create safe space, don't turn discovery into a battle; "don't let the client self-diagnose". L3-candidate (GAxyQ-TzOoc).
- Perfectionism Is A Trap—Quantity Over Quality — ⚠️ multi-speaker panel (host Jonah + ≥2 unnamed guests inc. an IG-growth speaker who went 5-7day→2x/day = ~8-9k followers/wk); CHRIS NOT IDENTIFIABLE anywhere → do-not-train pending verification. Note: the Art&Fear ceramics parable is NOT cited (argued from experience). Not L3 (GEAKZAa1kLI).
- ★ Imposter Syndrome: Expertise Vs. Mastery — "Thinking Critically" debate show (Chris × Alec Miller guest=context). NEW: EXPERT vs MASTER distinction — expert is a BEHOLDER's title you can accept ("knows a little more/can help"); MASTER is a separate HIGHER category that OTHERS bestow and you NEVER claim for yourself; subjective (teacher/coach/helper) vs OBJECTIVE (gold-medal/Clio/Oscar/GPA) measures; David C. Baker "The Business of Expertise" (claim a focus, "fake it while you learn"); imposter-syndrome defined tightly = "inability to recognize what you're good at"; disclosure heuristic (front-load only RELEVANT, over-disclaiming = "lawyers talking to lawyers"); don't design advice around the <20% who fake it. L3-candidate (4tKF7Gp0414).
- ★ How To Build Self Confidence and Discover What You Know — Chris (Ricky+team=context). NEW mechanism: confidence is REBUILT THROUGH TEACHING — "gain clarity through articulation" (explaining surfaces knowledge you didn't know you had); best coaches NEVER reached flow-state mastery (Michael Jordan can't explain how he scores → had to consciously deconstruct). BIOGRAPHY (concrete backstory to the existing "I forgot what I knew" teaching-origin): the ~2000 BURNOUT episode — eclipsed by a young hotshot, "lifespan of a graphic designer is 5 years", downward self-doubt spiral → resolved via ArtCenter/Otis teaching invitation during a 3-month sabbatical → "never doubted himself again". L3-candidate (bBEYQqHqR98).
- Overcoming Struggle, Power Of Vulnerability — Chris INTERVIEWS Katherine "Kathy" Dyer (cancer survivor, guest=context, NOT family). BIOGRAPHY/IDENTITY (rare candid): his WIFE accuses him of not letting her in emotionally ("she wants the robot to feel"; "it is or it isn't, I don't think about that"); repeatedly accused of "NOT being relatable", admits he can recall only "a few" personal-struggle stories → context for why vulnerability is a DELIBERATE personal-brand project; introvert/analytical/"business person" self-ID; Tony Hsieh/Zappos airport-driver + "watch how they treat the usher" character test. Not L3 (Dw4pu71m_Ws).
- ★ Hiring Your First Employee As An Entrepreneur — Chris (Ricky+coachee Ash=context). NEW first-hire playbook: swap Maker/Creator Hat → ENTREPRENEUR Hat; document every function you do; hire a PAID INTERN (over unpaid, "so it's sustainable") from a nearby school for the LEAST-essential functions FIRST; expect to churn many to find fit (personality/skill/drive); MENTORSHIP is part of the compensation (entry pay ↔ teaching they can't get elsewhere); the "KEEPER" self-identifies by mastering tasks & asking for more; use the margin between your rate and their wage to BUY BACK TIME for the 4 "glue" functions (marketing/sales/customer-service/UX) + thought-leadership; scaling makes you CHOOSY ("dibs on the dream project", Calvin Klein/Mos Def) not idle. Reinforces maker→CEO + doc→delegate→automate + hire-on-values. L3-candidate (SduKH5rf850).
- ★ How To Use Pricing Options In Your Bids & Proposals — Chris (Ricky=context; fixes coachee Shia who sent ONE estimate). NEW delivery mechanics (beyond existing good/better/best + bracketing): always present 3 OPTIONS so the client "compares you against YOURSELF" instead of shopping around; BUILD the high anchor by stacking coaching + staff-training + months of oversight so the MIDDLE looks like best value; verbal SCRIPT — "I have three options I've crafted just for you", state the TOP price FIRST then PAUSE to "let the anchor do its work", name the packages (e.g. "White Glove"); worked example \$5K logo/strategy | \$20K "most popular" branding | \$45K White-Glove; wine-list "reset the ladder, buyers still pick the new middle" (credited to Pro member Matthew/alt-MBA). L3-candidate (fVLK9fJoM1g).
Attribution: 1 do-not-train (perfectionism panel, Chris not identifiable) + 2 guest/debate (Alec Miller, Kathy Dyer=context) + 4 coaching (Ricky/Ash/Shia/students=context); 5 new ★L3-candidates. No family names (wife unnamed). Counts: L2 437->444.
Synthesis notes: NEW (debt 3/10) — (1) BIOGRAPHY (rich): the ~2000 BURNOUT→teaching origin story (concrete backstory to "I forgot what I knew"; young-hotshot, "designer lifespan 5yrs", 3mo-sabbatical → ArtCenter/Otis → confidence-restored) — promote to biography.md (deepens the Futur founding mythology); + emotional-guardedness identity (wife "wants the robot to feel", "not relatable", vulnerability-as-deliberate-project) — biography/voice; (2) sales-clients: twin-constraint (hard-to-think + hard-to-decide → help-think + remove-fear) + "clients more afraid of you" + create-safe-space — promote to sales-clients (the WHY behind discovery); (3) mindset: EXPERT-vs-MASTER distinction + confidence-rebuilt-through-teaching / "clarity through articulation" / best-coaches-never-mastered — strong promote to mindset (imposter/expertise cluster); (4) business: INTERN-BRIDGE first-hire playbook (hire-least-essential-first, mentorship-as-comp, keeper-signal, Maker→Entrepreneur-Hat) — promote to business (scaling/hiring); (5) pricing: 3-OPTIONS-in-proposals delivery mechanics ("compare you against yourself", high-anchor-stacking, state-top-first+pause script, wine-list-reset) — promote to pricing (enriches the three-options section). ENTITY: Alec Miller (debate guest), David C. Baker (author — influences), Katherine Dyer (guest). Rate-limit: 1 persistent-429 (2sqUDzorHLU).

## [2026-07-18] ingest | yt batch (@thefutur, 7) — P2 Feb-2020 (teach-while-learn w/Melinda, Pocket-Full-of-Do sold-out, hire-first-freelancer; Paula-Scher + 2 Jonah-hosted = context)
Batch 69. 7 of 8 fetched (1 on 429: 2sqUDzorHLU). Ingested 7 to L2. L2 444->451.
- ★ Teach While You Learn w/ Melinda Livsey Ep.21 — Chris + Melinda (context; her insecurity re "those who can't do, teach"). Chris NEW: "educate = DRAW OUT not put in" (teaching is extraction via questions); the AUDIENCE owns the "expert/teacher" label (extends Neumeier "brand = gut feeling" — you influence but can't control it); the BUYER (not seller) determines price/value (video-game-skins: zero perf advantage yet people pay); let the MARKET decide who's qualified to teach (terminal-degree gatekeeping = "artificial barrier"); being GOOD at doing makes you a WORSE teacher (too intuitive to explain); ITERATE frameworks like software (OS/patches) vs "bank-robbery rigor" for one-shot situations; to teach better, be COACHED yourself; "read the room — when everyone writes it down, hit that harder"; we buy a DESTINATION/change, not a product. L3-candidate (DWBZRZRkEGk).
- Before You Design A Logo Do This One Thing — ~95% PAULA SCHER (Pentagram partner, guest=context): her "book of ~500 trademarks" sticky-note taste-SORTING exercise (learn client taste BEFORE designing), multi-decision-maker consensus test, competitor-envy read, "red belt on a black dress" analogy. Chris = intro + 1 question only. paula-scher ENTITY candidate. Not L3 (guest-led) (5SMxKlH7kZM).
- Fake It Till You Make It Explained — ⚠️ NOT CHRIS: host JONAH (self-ID "I'm Jonah") + Greg Gunn outro. do-not-train. "believe it till you achieve it"/act-as-if/amateur-mindset (Rodney Mullen, Roger Bannister). Useful CONTRAST to Chris's own fake-it-while-you-learn (David C. Baker) — keep separate. Not L3 (vHlLtOzSjks).
- ★ My First Self Published Book Sold Out! — Chris solo (Ricky helps read Kickstarter backers=context). BIOGRAPHY GOLD — POCKET FULL OF DO: his FIRST-EVER + FIRST SELF-PUBLISHED book; KICKSTARTER-funded; a collection of 20+ years of lessons (mindset/business/pricing/creativity/"some family stuff"); the extra print copies SOLD OUT within 48h (as of 2020-02-13); formats rolling out (e-book + Audible audiobook via Futur site, physical later). Structure (caption-derived, verify): Ch.1 "Relationships" (p.29 "To be interesting, be interested"), Ch.2 "Creativity" (p.41 "Fail Forward"), Ch.3 "Beliefs" (p.57 "No victims, just volunteers"). Self-disclosure: introvert, "uncomfortable/awkward in social situations", coping trick = shift attention OFF himself onto the other person. L3-candidate (jgQiX-n7aEE).
- When You Help Others You Also Help Yourself — ⚠️ 2-voice unlabeled, attribution:uncertain (plausibly Chris, unverified); do-not-train pending. Give-first framings: helping as non-monetary "payment" (hearing you helped fuels you), "planting seeds" metaphor (costs nothing, blooms into joy; freezer-section-stranger anecdote), see-yourself-through-loved-ones'-eyes (vs hyper-critical lens = imposter). Both speakers endorse the close so it's Chris-consistent. Not L3 (oH2R_fJOFI0).
- Why Emails Are Bad For Business — ⚠️ NOT CHRIS: host JONAH narrating a Chris PRO-GROUP PROTOCOL in 3RD PERSON ("a cut down from a protocol that Chris did... either Chris or another manager runs them"). do-not-train (same failure mode as the 5-sentence-email PM clip). Push prospects to a live phone/video call (commitment test = power) vs one-directional email; send video if they insist on email; drop if they won't commit to a call. Not L3 (Zgfz97BZwXA).
- ★ Find & Hire Your First Freelancer — Chris (editor=context; cut from a Pro-Group call). NEW (distinct from the employee INTERN-BRIDGE): judge a freelancer by whether their existing portfolio matches EXACTLY the style you want ("they'll do whatever they show you" — loops to consistency-gets-you-hired); "DATABASE OF 12" bench concept (deliberately stock low/mid/high-price freelancers to match cost to job — "big guns" vs "overkill"); short PAID TRIAL de-risk ("pay for a day or two, no harm no foul"); subcontractor traits (responsive/reasonable/level-headed/clear-articulable-process) + "trust your gut"; language reframe "they're the freelancer, not you" (doer→hirer). L3-candidate (kk9kJIg8SXI).
Attribution: 2 do-not-train (both Jonah-hosted Futur clips, Chris 3rd-person/absent) + 1 guest-led (Paula Scher ~95%) + 1 uncertain-2-voice + 1 Melinda dialogue + 2 Chris-led ★; 3 new ★L3-candidates. NOTE: "Jonah" now a recurring short-clip HOST (add to futur-instructors attribution-guard). No family names. Counts: L2 444->451.
Synthesis notes: NEW (debt 4/10) — (1) BIOGRAPHY (landmark): POCKET FULL OF DO details (first/self-published, Kickstarter, sold-out-48h Feb-2020, 3-chapter structure, formats) — promote to biography.md (fills the book milestone) + the 3 book-passage beliefs; (2) mindset/business: TEACH-WHILE-LEARN Ep.21 cluster (educate=draw-out, audience-owns-expert-label, buyer-determines-value, market-decides-who-teaches, being-good-makes-worse-teacher, iterate-frameworks-like-software, we-buy-a-destination) — promote to mindset + business (pairs w/ existing teaching-philosophy); (3) business: FREELANCER-hiring playbook (portfolio-exact-match, database-of-12 bench, paid-trial de-risk) — promote to business (pairs w/ employee intern-bridge from batch 68); (4) voice/bio: introvert-coping-trick (shift-attention-off-self). ENTITY: Paula Scher (Pentagram, design influence — candidate page), "Jonah" (Futur host — add to futur-instructors), David C. Baker (author, from batch 68). Rate-limit: 1 persistent-429 (2sqUDzorHLU).

## [2026-07-18] ingest | yt batch (@thefutur, 7) — P2 Feb-Mar-2020 (accusation-audit, cant-afford-barter-menu, specialize-externally, rock-bottom, double-income-bid-buildup; 2 non-Chris)
Batch 70. 7 of 8 fetched (1 on 429: 2sqUDzorHLU). Ingested 7 to L2 — 5 Chris ★L3. L2 451->458.
- ★ Be The First To Raise Client Objections — Chris (Ricky host=context). NEW: the ACCUSATION AUDIT (credits Chris Voss / Never Split the Difference) — proactively voice the client's likely objections so they're neutralized; the canonical 3 he preempts (too-expensive / not-enough-experience / no-guarantees); the conditional/hypothetical U-TURN ("if X matters to you, you probably shouldn't hire us" → makes prospects turn their own stated criteria against themselves); ~\$700K project "technical-specs vs artistry" reframe + "every project was the first time we did that kind of project" (no-experience reframe). BIO: "19 years in business" (2020). L3-candidate (ba4TH9C4qAU).
- ★ How To Respond When Someone Can't Afford You — Chris live-coaches a freelancer re peers/musicians wanting free/exposure work (Eric Sweet intern narrator=context). NEW pricing axis beyond anchor/discount: CHARITY-vs-CLIENTS cut (genuine cause + truly broke = charity; exploiters "not broke, they're just BROKEN; their cause is capital"); pro-bono RATIO rule ("10 clients before I give one away"); a BARTER/non-cash-value MENU with \$ values (tickets/merch/referrals/lessons/genuine endorsement); exposure & portfolio-pieces DON'T count as payment (you can get those yourself); "exposure as an ACT not a word" (a performed endorsement scaled by audience size has value); a barter trade must EXCEED the cash price (bartering is extra work); equity/% in lieu of a guaranteed fee; bartered goods are re-tradable. L3-candidate (xE1onB5dVI8).
- How To Measure The Effectiveness Of Branding — ⚠️ Jonah host + MARTY NEUMEIER (guest; the BRAND LADDER = satisfaction→delight→engagement→empowerment is HIS IP from The Brand Flip; "you don't buy brands, you join them"; measure via YoY customer-engagement cheaply) + Chris co-articulates the rungs + Apple example. do-not-train (framework=Neumeier — belongs on his influence/entity page, NOT beliefs.md). Not L3 (aT-Z2R4vJSQ).
- ★ Specialize or Generalize - Niche or Broad — Chris solo. NEW reconciliation of the niching tension: SPECIALIZE EXTERNALLY / GENERALIZE INTERNALLY (show the world ONE deep expertise = what earns money/opportunity; privately keep ALL your other passions = what keeps you fulfilled); the HALO BIAS as the payoff mechanism (seen as great at one thing → people assume great at everything → adjacent doors open); portfolio-editing rule (show only 3-4 pieces b/c reviewers judge you by your WORST one); cites Blair Enns (creatives' novelty-addiction sabotages marketing/expertise) + Jordan Peterson (creatives = divergent thinkers, a little convergent discipline pays). BIO: landed his first ad job with 4 conceptual pieces in a FedEx box. L3-candidate (TmPHqX2P3vM).
- The Truth About Your High Expectations and Your Creativity — ⚠️ NOT CHRIS: host MATTHEW ENCINA (creative director) + guest Melanie Whitney (Common Collective). Chris absent. do-not-train. don't-attach-to-outcome/commit-to-journey/"you are enough"; Futur context (case study: Design From Scratch underperformed Building A Brand). Not L3 (bm9BrG5EiNA).
- ★ How To Pick Yourself Up From Rock Bottom — Chris coaches a Pro-Group member out of a confidence collapse after "failing" a practice boss-battle (member=context). NEW framework: everyone falls — the difference is the STORY you tell yourself when you fall; expectations & ATTACHMENT to an idealized future self = "the root of your sadness"; live in the PRESENT self (not future/past self); "a house made of assumptions falls over"; a practice group is the SAFEST/CHEAPEST place to fail vs in front of a paying client; "don't assume, understand the problem first" (bridges his sales-discovery principle into mindset). BIO: worked with his business coach ~13 YEARS, weekly 2hrs "without fail", and only ~year 13 felt "I think I got this" (hard numbers on the long-road-to-mastery theme; corroborates Kier McLaren). No COVID content despite Mar-2020 date. L3-candidate (s5MWPNIBPRQ).
- ★ How To Double Your Income As A Solopreneur — Chris solo. NEW BID-BUILDUP pricing method: research what it costs to hire someone AT/ABOVE your level (3+ data points, averaged), then price every bid AS IF you had to hire that person + a salesperson + production manager + project coordinator, + 20-30% profit + padding → reveals most solopreneurs underprice + gives them the OPTION to hire & scale solo→team; "investor whose money makes money" framing (play the roles by choice not necessity); freelancer→full-time scaling ladder ("don't be quick to hire — creatives find it very hard to fire"); Grant Cardone 200-unit analogy. L3-candidate (082H4FftCY8).
Attribution: 2 do-not-train (Neumeier-framework clip; Encina+Whitney expectations) + 4 coaching/Pro-Group (Ricky/Eric-Sweet/members=context) + 1 Chris-solo; 5 new ★L3-candidates. No family names. Counts: L2 451->458.
Synthesis notes: NEW (debt 5/10) — (1) sales-clients: ACCUSATION-AUDIT / be-first-to-raise-objections (Chris Voss) + conditional-U-turn — promote to sales-clients (objection-handling); (2) pricing: CHARITY-vs-CLIENTS + barter/non-cash-value-menu + "exposure is an act not a word" + barter-must-exceed-cash (can't-afford playbook) AND BID-BUILDUP method (price-as-if-hiring-at/above-your-level + roles + profit) — strong promote to pricing (2 distinct new methods); (3) branding/business: SPECIALIZE-EXTERNALLY/GENERALIZE-INTERNALLY + HALO-BIAS + portfolio-3-4-judged-by-worst — promote to branding (reconciles the niching tension) + design-craft (portfolio rule); (4) mindset: story-you-tell-when-you-fall + attachment=root-of-sadness + present-self + practice-group-safe-to-fail — promote to mindset (resilience); (5) BIO: "19 years in business (2020)" + business-coach-~13-yrs-weekly-2hrs (hard numbers) + first-ad-job-4-pieces-FedEx-box — biography enrichment. ENTITY: Marty Neumeier (deepen w/ brand-ladder/Brand-Flip), Matthew Encina (recurring host — futur-instructors), Chris Voss (author — influences). Rate-limit: 1 persistent-429 (2sqUDzorHLU).

## [2026-07-18] ingest | yt batch (@thefutur, 5) — P2 Apr-2020/COVID (talk-less-listen-more, coping-anxiety, make-a-living+2020-financials; 2 guest-led + WFH team compilation)
Batch 71. 5 of 8 fetched (2 on 429: 2sqUDzorHLU, 0lRXUzwFvHY; 1 no-caption L1: mpOGY4bMoWQ). Ingested 5 to L2. L2 458->463. COVID era begins (Apr 2020).
- ★ The Best Sales Technique—Talk Less Listen More — Chris coaches Pro-Group (members Henry/refs to Priscilla/Melinda=context). NEW frames (beyond 10/90, two-ears-one-mouth): selling as THERAPY (ask super-smart questions, the client already knows the answer, "your own advice is the best advice you'll take"); LION-AND-SHEEP respect frame (client = proven successful owner; understand their lens, don't teach them); "WHAT COMPELS YOU TO OPEN YOUR MOUTH?" self-diagnostic (urge-to-speak = validation-seeking + silence-discomfort + need-to-entertain); "when you stop selling you start closing more"; "if you want to be seen as an expert, be quiet"; count-to-20 restraint; "death eyes" (CDs cutting off clients on 6-figure calls). L3-candidate (01UOEz1Ed4M).
- Coping With Fear & Anxiety In Difficult Times — COVID (2020-04-02); Chris interviews therapist WESLEY LITTLE (guest=context, most clinical content NOT persona). Chris COVID-dated positions: pandemic response = two polar extremes (under-reactors-feel-invincible vs panic-hoarders); NARRATIVE-REFRAME coping (you tell yourself a "story crafted out of thin air" from feelings/opinions not facts → choose a better one; worked: reframe a talk-due-in-a-week from "you'll fail" to "we've been here, a week is plenty"); overwhelm remedy = name "the 3 things you need to do right now", prioritize, "become my own boss"; overwhelm = "a ball of rubber bands twisted & knotted"; resists therapist's word "coping", prefers "a life philosophy". Not L3 (wIzlb_iYZjY).
- Work From Home Setup — multi-speaker Futur-team WFH compilation (Matthew, Ben & Elyse Burns, Greg Gunn, Elle=context). ⚠️ the "introvert-loves-isolation / focus-sprints / Eisenhower-matrix" segment is MATTHEW ("a post that Chris shared on his Instagram"), NOT Chris. Chris appears ONLY in the closing BOOK-READING method: (1) read the table of contents first as a preview; (2) read the book TWICE (fast first-sentence-of-each-paragraph skim, then slow analytical pass in 90-min blocks); (3) personal ANNOTATION LEGEND — highlight keywords, underline cross-refs, box reusable ideas as "building blocks" for future talks; cross-references Voss (say price LAST) vs Blair Enns/Pricing-Creativity (say price FIRST/anchor). Mostly do-not-train. Not L3 (ho3lPg4C6gg).
- ★ Make A Living Doing What You Love—Practical Advice — Chris coaches an LA session drummer "Blair"/Sticks-and-Wires (guest=context) using The Futur's own multi-income model as a template. RARE 2020 FUTUR FINANCIALS (self-reported): $3.1M prior year; YouTube ~$10-12k/mo; coaching group ~$30k/mo recurring; sponsorships up to $10k+/episode; affiliates 10-50%; book Kickstarter raised >$70k (floor $20k); 12 staff. NEW: FAME-vs-PRICE ("the more well-known you are, the less price matters" → get known first); AUDIENCE-as-core / product-as-DISTRACTION ("the course is a vehicle to say thank you"); course-BUNDLING mechanics (mini-courses low-price, bundle below sum-of-parts, try-then-credit); "GARAGE SALE" monetization (from Rework — sell digital assets already on your drive; Futur sells case studies + templatized legal forms); "little buckets that collect rain" multiple-income-stream metaphor; ladder-of-commitment microtransactions; story-driven non-selling newsletter. L3-candidate (tgjSyB7pXb4).
- How to Protect Yourself from Bad Clients — ⚠️ NOT CHRIS: guest EMILY COHEN (design-business consultant; "Brutally Honest w Emily Cohen" livestream) delivers ALL frameworks: "for every RED FLAG raise your fee ~10%", red-flag inventory (too-many-stakeholders/non-decision-makers/hours-long-calls), say-NO discipline, fire ~1 client/yr, diplomatic firing scripts, alcoholic-client story. Chris = HOST/reactor + short "Emily, can you fire me?" role-play. do-not-train (frameworks=Emily). emily-cohen ENTITY candidate. Not L3 (mXi7SGXZYVQ).
Attribution: 2 do-not-train/guest-led (Emily Cohen frameworks; Wesley Little clinical) + 1 team-compilation (WFH, Chris only closing) + 2 Chris-led coaching (Pro-Group/drummer, members=context); 2 new ★L3-candidates. No family names (Ben+Elyse Burns are the Burns's, context). Counts: L2 458->463.
Synthesis notes: NEW (debt 6/10) — (1) sales-clients: talk-less-listen-more DEEPER frames (selling-as-therapy, lion-and-sheep, "what-compels-you-to-open-your-mouth" self-diagnostic, "stop-selling-to-close", count-to-20) — promote to sales-clients (enriches the listen cluster); (2) business/content-strategy: MULTIPLE-INCOME-STREAM model + rare 2020 FINANCIALS ($3.1M, revenue breakdown, 12 staff) + fame-vs-price + audience-as-core + garage-sale/bundling monetization — strong promote to business + content-strategy + biography (financials); (3) mindset: NARRATIVE-REFRAME coping + overwhelm-remedy (3-things-now) + COVID two-extremes (2020-04 dated) — promote to mindset; (4) mindset/content-strategy: Chris's BOOK-READING method (TOC-first, read-twice, annotation-legend/building-blocks) — distinct learning method, promote. ENTITY: Emily Cohen (recurring guest — create page if recurs), Wesley Little (therapist guest), Chris Voss (author — influences, already noted). BIO: 2020 Futur $3.1M/12-staff + book-Kickstarter->$70k. Rate-limit: 2 persistent-429 (2sqUDzorHLU, 0lRXUzwFvHY).
