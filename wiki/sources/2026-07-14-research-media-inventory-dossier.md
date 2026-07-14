---
type: web-research
source_date: 2026-07-14
ingested: 2026-07-14
tags: [media-inventory, pipeline, enumeration, channels, podcast, socials, courses, guest-appearances]
---

# Media inventory dossier — Chris Do / The Futur (as of 2026-07-14)

Phase-2 consolidation of the full media surface of the SUBJECT (Chris Do). YouTube
numbers come from exact yt-dlp enumeration on 2026-07-14 (Phase-0, authoritative);
everything else was verified or extended via web research on 2026-07-14. Every number
carries its as-of date and source. Follower counts are platform-self-reported unless
noted; nothing here is registry-verified.

## YouTube channels (exact yt-dlp enumeration, 2026-07-14 — authoritative)

| Channel | Channel ID | Subs | Content | Notes |
|---|---|---|---|---|
| @thefutur | `UC-b3c7kxa5vU-bnmaROgvog` | 2,810,000 | 1,177 long-form + 737 shorts + 235 streams | Main corpus. Long-form split: 431 videos ≥20 min, 188 videos 10–20 min, 558 videos <10 min (≈475 h); streams ≈320 h. Oldest uploads Aug/Sep 2014 (first: "How To Ask for the Sale Pt 1", 2014-08-20, with Jose Caballer). Legacy vanity URL `youtube.com/c/thefuturishere` = same channel. |
| @TheFuturAcademy | `UCqHuGF2axS8Yf89r1tUVS_A` | 436,000 | 72 videos + 14 shorts | Started 2019-01-23. Tutorials mostly by other instructors — low persona value. |
| @ChrisDo | `UCWqGiF72rubTwZLNoKT9Y1A` | 67,700 | 2 videos + 8 shorts | Near-dormant personal channel. |

**Host-attribution notes (critical for fidelity rule 6):** Chris Do is primary host of
@thefutur post-2017. The early era (2014–~2017) was co-hosted with Jose Caballer; some
content is fronted by team members Matthew Encina, Ben Burns, Greg Gunn, and Melinda
Livsey (~25 videos explicitly named in titles; more unnamed pre-2019 tutorials).
**Every ingest must attribute speakers before anything flows into persona files.**
@TheFuturAcademy content is mostly NOT Chris — treat as context, not persona training
data, unless Chris is on camera/mic.

No "Futur Photography" channel and no official clips channel exist (Phase-0 check,
2026-07-14).

## Podcast — "The Futur with Chris Do"

- **RSS feed**: `https://feeds.megaphone.fm/TFL6245334029/` — hosted on **Megaphone**;
  feed title "The Futur with Chris Do", author "The Futur", owner
  `podcast@thefutur.com` (feed fetched directly 2026-07-14 via
  [rephonic.com](https://rephonic.com/podcasts/the-futur-with-chris-do), then verified
  against the live feed). Caution: the fetched feed rendered only ~10 recent items —
  full back-catalog enumeration should use the feed with pagination or a directory API.
- **Episode count**: 445 episodes as of 2026-07-14 (Listen Notes,
  [listennotes.com](https://www.listennotes.com/podcasts/the-futur-with-chris-do-the-futur-URywKcNj2TZ/)).
  Latest: "The Pricing Conversation You Keep Avoiding w/ Chris Do | Ep 441",
  2026-07-08. Note: numbered "Ep 441" vs. 445 total — the delta is trailers/bonus
  items; treat the ledger count as feed items, not episode numbers.
- **First episode**: 2016-09-08; weekly cadence since (Listen Notes, 2026-07-14).
- **Directories**: Apple `id1209219220`, Spotify `5K96ryZCjCmxqMzEotvS8h`, iHeart
  (`iheart.com/podcast/269-the-futur-with-chris-do-77346412/`), SoundCloud
  (`soundcloud.com/thefuturishere`), Podcast Addict `6019389`.
- **Ratings**: ~3.1k ratings, ~4.9/5; ranked #39 US Apple Business/Marketing category
  (rephonic.com, 2026-07-14 — third-party estimate).
- **Dedup rule (binding for the ledger)**: 80–90% of podcast episodes are the audio of
  YouTube uploads (Phase-0, 2026-07-14; YouTube playlist
  `PLzKJi2GjpkEE8hyFgMt0pIjnYkGB2YpDt` "The Futur Podcast with Chris Do").
  **YouTube is the primary ingestion source.** Podcast feed items enter the ledger
  only when no matching YouTube upload exists (match on title + publish week); matched
  items stay L1 with `dup-of:<youtube-id>` notes.

## Books

| Title | Date | Details | Source |
|---|---|---|---|
| *Pocket Full of Do* | 2019 (2nd printing 2020) | Self-published, ISBN 9780578551333; designed by Minhye "Min" Cho, edited Bryn Mooth, illustrated Greg Gunn | Phase-0 (thefutur.com/shop/pocket-full-of-do, amazon.com, goodreads.com), 2026-07-14 |
| *Unbland Yourself* | Launched late Dec 2025 | Personal-branding workbook, $99 digital, 119 pp, 900+ preorders (self-reported); Forbes coverage 2026-02-05 | Phase-0 (community.thefutur.com/unbland; forbes.com/sites/jodiecook/2026/02/05/), 2026-07-14 |

NOT his book: *The Five Most Important Things You Don't Learn in School* (2022,
Mathias Omotola) — Chris wrote the foreword only (Phase-0, 2026-07-14).

## Socials

| Platform | Handle | Count | As of | Source | Confidence |
|---|---|---|---|---|---|
| LinkedIn | [linkedin.com/in/thechrisdo](https://www.linkedin.com/in/thechrisdo/) | 628,000 followers | 2026-07-14 | Phase-0 direct profile check | High. Flagship platform, posts daily. Headline 2026: "I'll teach you to charge so much it makes your mom nervous. Hard truths gently told. Content Lab launching Sep." (verified in search result title, 2026-07-14) |
| Instagram | [@thechrisdo](https://www.instagram.com/thechrisdo/) | Profile displays "1M" (rounded); third-party tracker SPEAKRJ reports 837,444 | 2026-07-14 | instagram.com profile snippet; speakrj.com/audit/report/thechrisdo/instagram | Medium. The 1M display and 837K tracker figure conflict; true value likely 0.84–1.0M. Phase-0's "~1M" stands as the display value. |
| X / Twitter | [@theChrisDo](https://x.com/thechrisdo) | ~100,000 | 2023-01-31 (STALE) | Chris's own Jan-2023 LinkedIn post (self-reported); no fresher count fetchable 2026-07-14 (X blocks scraping) | Low. Account also self-reported as low-activity. |
| TikTok | [@thechrisdo](https://www.tiktok.com/@thechrisdo) | 116,100 | 2026-07-14 | web search snippet of tiktok.com profile | Medium. Consistent with Phase-0 "~115K". |
| Threads | @thechrisdo | count not established | 2026-07-14 | Phase-0; LinkedIn cross-post announcing the account (2023) | Low — existence confirmed, count unknown. |
| Behance | [behance.net/chrisdo](https://www.behance.net/chrisdo) | n/a (portfolio) | 2026-07-14 | Phase-0 | Profile lists Santa Monica, CA; self-reported. |

Historical anchor for growth curves: Chris's own Jan-2023 self-report — 2.1M YouTube,
880K Instagram, 420K LinkedIn, 100K Twitter (LinkedIn post, self-reported, 2023-01-31).

## Websites / courses

### thefutur.com (main hub)

Sitemap fetched 2026-07-14 (`thefutur.com/sitemap.xml`): ~800+ URLs. Key structure:

- **`/watch/*`** — free content library, 200+ video pages (essentially YouTube mirrors
  with SEO pages; recent modifications through 2026-06-15). Dedup against YouTube —
  do NOT ledger these separately.
- **`/content/*`** — 300+ blog/article pages (educational articles, guides,
  interviews). Optional long-tail ledger candidates (priority 3); mostly team-written,
  so speaker attribution required before persona use.
- **`/shop`** ("Courses & Tools") — course/product catalog. The course platform itself
  runs on **academy.thefutur.com** (Teachable; visible in lecture URLs, 2026-07-14).
- **Programs**: `/pro-group` (Futur Pro membership/community), `/content-lab` (new
  program, "launching Sep" 2026 per LinkedIn headline), `/unbland` (Unbland Yourself),
  `/retreats/pasadena` (in-person retreat), `/free-resources`, `/events`.
- **`/newsletter`** — newsletter signup exists ([thefutur.com/newsletter](https://www.thefutur.com/newsletter),
  confirmed via search 2026-07-14); collects name+email for "newsletter and
  information about The Futur events and products". Name/frequency not established
  (page is JS-rendered; not fetchable) — low confidence beyond existence.

Notable: the sitemap contains **no `/courses/` or `/course/` paths** as of 2026-07-14,
but `/course/<slug>` URLs (e.g. `/course/perfect-proposal`, `/course/pricing`,
`/course/how-to-negotiate`) resolve and appear in search indexes — catalog pages are
likely excluded from the sitemap or in transition.

### Course catalog shape (named products)

Names verified against thefutur.com URLs 2026-07-14; prices from a third-party roundup
([justcreative.com/top-10-best-futur-courses/](https://justcreative.com/top-10-best-futur-courses/),
undated article, accessed 2026-07-14 — treat prices as indicative, not current):

**Design track**: Typography 01 (Chris Do, $299) · Logo Design 01 (Chris Do, $149) ·
Lettering 01 (Nils Lindstrom, $149) · Stylescapes (Chris Do, $199) · Color for
Creatives (Greg Gunn, $149).

**Business track**: Business Bootcamp (Chris Do; flagship) · Positioning & Lead Gen
(Chris Do, $699) · Brand Strategy Fundamentals (Anneli Hansson, $199) · The Perfect
Proposal (Ben Burns, $59) · Overcoming Sales Objections (Chris Do) · Painless Pricing
(`/course/pricing`) · How To Negotiate (`/course/how-to-negotiate`) · Brand Messaging
Kit · Brand Style Guide Kit · Complete Case Study Toolkit.

**Memberships/programs**: Futur Pro Group · Content Lab (Sep 2026, announced) ·
Unbland Yourself ($99 digital workbook).

Attribution note: several courses are taught by team members (Lindstrom, Gunn,
Hansson, Burns) — course authorship is persona-relevant only for Chris-taught courses.

### Other sites

- **blind.com** — Blind, Chris's brand-strategy consultancy (relaunch post:
  `blind.com/blog/blind-relaunches-as-brand-strategy-design-consultancy/`), Phase-0.
- **academy.thefutur.com** — Teachable-hosted course delivery (2026-07-14).
- **community.thefutur.com** — community platform (hosts `/unbland`), Phase-0.

## External guest appearances (starter ledger candidates)

Chris has 100+ guest appearances (Phase-0 estimate). Starter list of named shows,
verified 2026-07-14 unless noted. Confidence: **C** = episode URL confirmed,
**L** = listed on a curated list ([Feedspot "10 Best Chris Do Podcasts"](https://podcast.feedspot.com/chris_do_podcasts/)),
episode URL still to be pinned.

1. **Creator Science #111** (Jay Clouse) — [podcast.creatorscience.com/chris-do/](https://podcast.creatorscience.com/chris-do/) — C
2. **The Second Studio #188** — [secondstudiopod.com](https://www.secondstudiopod.com/) — C (Phase-0)
3. **Fearless Business** (Robin Waite) — [podcast.fearless.biz/e/chris-do-the-futur-podcast-interview/](https://podcast.fearless.biz/e/chris-do-the-futur-podcast-interview/) — C
4. **Baby Got Backstory (BGBS) #049** — [wildstory.com/podcast/chris-do-the-futur](https://www.wildstory.com/podcast/chris-do-the-futur) — C
5. **Makers of Sport #97** — [makersofsport.com/episodes/97/chris-do](http://makersofsport.com/episodes/97/chris-do) — C
6. **Ukramedia #012** ("The Balance Between Do and Don't") — [ukramedia.com/the-balance-between-do-and-dont-with-chris-do/](https://ukramedia.com/the-balance-between-do-and-dont-with-chris-do/) — C
7. **The Garlic Marketing Show** (Ian Garlic) — [iangarlic.com/2022/06/10/chris-do/](https://iangarlic.com/2022/06/10/chris-do/) — C
8. **School of Motion Podcast** ("The Uncertain Future of Mograph") — [schoolofmotion.com/blog/the-uncertain-future-of-mograph-with-chris-do](https://www.schoolofmotion.com/blog/the-uncertain-future-of-mograph-with-chris-do) — C
9. **PepsiCo Design podcast** — [design.pepsico.com/podcasts/chris-do](https://design.pepsico.com/podcasts/chris-do) — C
10. **Millo / Freelance to Founder** — [millo.co/chris-do-interview](https://millo.co/chris-do-interview) ("From immigrant childhood to millions in revenue & winning an Emmy"); Freelance to Founder is Millo's podcast, episode re-run 2024 — C
11. **The Business of Graphic Design** (multi-part interview) — [thebusinessofgraphicdesign.com/an-interview-with-chris-do-part-1/](https://thebusinessofgraphicdesign.com/an-interview-with-chris-do-part-1/) — C
12. **Finien Podcast Ep004** (Fabian Geyrhalter) — [finien.com/podcasts/ep004-chris-do/](https://www.finien.com/podcasts/ep004-chris-do/) — C
13. **Beyond a Million** ("Building a Brand with The Futur Founder") — [beyondamillion.com/audio/chris-do/](https://beyondamillion.com/audio/chris-do/) — C
14. **Giant Thinkers Podcast #86** — [giantthinkers.podbean.com/e/chris-do-founder-of-the-futur-on-building-and-positioning-a-thriving-creative-business/](https://giantthinkers.podbean.com/e/chris-do-founder-of-the-futur-on-building-and-positioning-a-thriving-creative-business/) — C
15. **ScaleX Insider S14E2** (Brendan McGurgan) — [simplescaling.com/insights/podcast/season-14-episode-2/](https://simplescaling.com/insights/podcast/season-14-episode-2/) — C
16. **"Emmy Award Winner Explains Building a Brand in 2024"** — Apple show `id1604899711`, episode `i=1000658346221`, aired 2024-06-09 — [podcasts.apple.com](https://podcasts.apple.com/us/podcast/emmy-award-winner-explains-building-a-brand-in-2024/id1604899711?i=1000658346221) — C (show name to resolve at ingest)
17. **The MOOD Podcast** — appearance confirmed in search summaries (topics: personal branding, authenticity, algorithm, burnout), 2026-07-14; episode URL to pin — L
18. **The 505 Podcast** — show: [redcircle.com/shows/the-505-podcast](https://redcircle.com/shows/the-505-podcast); episode URL to pin — L
19. **We Have A Meeting** — Feedspot list — L
20. **The Right Questions** — Feedspot list — L
21. **The Profitable Graphic Designer** (Kady Sandel) — Feedspot list — L
22. **Vietcetera** (press interview, identity-focused) — [vietcetera.com/en/chris-do-on-mastering-the-power-of-embracing-identity](https://vietcetera.com/en/chris-do-on-mastering-the-power-of-embracing-identity) — C
23. **"Your Repeatable Story" Ep. 28** (show unidentified) — [youtube.com/watch?v=Ns1teHj2bLk](https://www.youtube.com/watch?v=Ns1teHj2bLk) — C (URL) / show name to resolve

Not verified despite targeted searches (2026-07-14): appearances on Deep Dive (Ali
Abdaal), Chase Jarvis LIVE, Marketing Against the Grain, Smart Passive Income, GaryVee
— do NOT assume these exist.

## Enumeration universe — what feeds pipeline/ledger.csv

Ledger population order and dedup precedence (all counts as of 2026-07-14):

1. **@thefutur YouTube** — 1,177 long-form + 737 shorts + 235 streams = **2,149 items**
   (yt-dlp, authoritative). Primary corpus; shorts dedup against long-form
   (`dup-of:<id>`).
2. **@TheFuturAcademy** — 72 + 14 = **86 items** (mostly L1/skip; low persona value,
   non-Chris instructors).
3. **@ChrisDo personal** — 2 + 8 = **10 items**.
4. **Podcast feed** (Megaphone `TFL6245334029`) — **445 items**; only the ~10–20%
   without a YouTube match get their own ledger rows (est. 45–90 net-new items);
   the rest L1 `dup-of:<youtube-id>`.
5. **Books** — **2 items** (both landmark, priority 1, L3).
6. **External guest appearances** — **23 named** above (starter; ~100+ total
   estimated); each gets a ledger row as pinned. These carry the highest
   biographical-detail yield per item.
7. **thefutur.com/content articles** — **~300+ items**, priority-3 long tail; enter
   the ledger only during a dedicated later phase (attribution burden is high).
8. **thefutur.com/watch pages** — **do not ledger** (YouTube mirrors).

Rough total enumeration universe: ~2,300 primary items + ~400 conditional/long-tail.
