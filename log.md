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
