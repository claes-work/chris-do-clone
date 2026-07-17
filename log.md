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
