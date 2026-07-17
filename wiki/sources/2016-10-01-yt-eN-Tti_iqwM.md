---
type: youtube-video
source_date: 2016-10-01
url: https://www.youtube.com/watch?v=eN-Tti_iqwM
channel: "@thefutur"
ingested: 2026-07-17
tier: L2
domains: [design-craft]
tags: [responsive, web-design]
---

# How To: Responsive Web Design for Mobile and Tablet

## Summary

An episode of **"The Process"** (thefutur's fly-on-the-wall series showing real client
work) covering the responsive conversion of the "O's Fishing Lodge" website from a
desktop design to tablet/mobile, plus a first-pass review of the developer's staging
build.

**Who leads:** This is a **two-hander**. Chris Do **hosts and moderates** — he frames the
episode, interviews the presenter, and delivers the higher-level design principles
(legibility vs. originality, "sizzle vs. steak," mobile-first thinking, how to work with
developers). The **hands-on technical walkthrough is led by a Futur team member** — a
Korean designer whose name is garbled in the auto-transcript (rendered variously as
"Say"/"Shene"; a separate designer "Charlene" is credited with the original desktop
comps). That designer did the actual responsive artboards and makes the concrete
layout/technical calls (grid widths, image cropping, break points). A colleague "Jose"
(Hosea) and "Andrew" appear briefly on camera.

> attribution: uncertain — presenter/designer names are unreliable in the auto-caption.
> The technical/responsive-conversion material is **CONTEXT** (team member, not the
> subject). Only Chris-Do-attributed principle statements are treated as persona voice.

## Key claims

**Chris Do (2016-10-01, paraphrase — persona-relevant):**
- Designing one layout to serve both desktop and mobile produces a "watered-down" result
  with weak typography; better to design a purpose-optimized mobile experience (cites
  Apple as building a distinct mobile site/experience).
- On mobile you don't include all content — only the *most important* content (text and
  buttons); everything else is a creative decision.
- **"Sizzle vs. steak"** framework: the *steak* is the meaty content (the substance);
  the *sizzle* is the sexiness — typography, graphics, photography, treatments. Different
  pages need different ratios; a job-application page is "steak, not a lot of sizzle."
- On a functional/utility page (e.g. job application), **legibility and usability are
  paramount** — strip decoration so people can complete the task quickly.
- More than half of web traffic in 2016 comes from mobile, so mobile must be a first-order
  concern ("one of these days we're going to design the mobile experience first").
- The creative person must balance two poles: **uniqueness/originality/personality/brand**
  vs. **usability/legibility.** Too far left = boring and generic; too far right =
  frustrated users. The right answer varies per page.
- **Working with developers/specialists:** don't prescribe solutions — ask questions
  ("how would you do this?"). They may know technologies beyond your knowledge. "You don't
  need to be the guy who pretends to know everything… and if you do you need to hire
  smarter people."
- **Project management:** use one shared platform (Trello, Basecamp, or whatever the dev
  team prefers) for transparency and bug tracking; adapt to the team doing the heavy
  lifting rather than forcing them onto your tool.
- Fancy/organic designs "get punished" in build: images without hard top/bottom edges
  can't be cleanly scaled for oversized screens, creating engineering problems.
- Design at least 4K/5K width in mind for backgrounds — HD (1920) is no longer a safe
  ceiling as displays grow.
- Developers promise pixel-perfect alignment with the Photoshop files; a static design and
  a dynamic build differ, so stay flexible.

**Futur designer / presenter ("Say"/"Shene", 2016-10-01, paraphrase — CONTEXT):**
- Used a 960-pixel-wide grid (12 columns) so content stays visible on small laptops, not
  just 27" 5K iMacs.
- Started the mobile artboard at 640px (2× the 320px base) for retina density to avoid
  pixelation; later widened toward 620/640 to give devs room as phones grew ("plus"
  sizes).
- Mobile is "completely different design," not a 1:1 translation — must decide which
  images/elements to drop and how to resize.
- Chose backgrounds by legibility: kept the textural paper background, dropped a
  high-contrast photo that made white type hard to read.
- **Hot tip:** export the mobile design as JPEG/PNG and open it on your actual phone (via
  Dropbox or emailing it to yourself) to check real legibility before locking the design —
  designers tend to make type too small.
- Point-size rule: never smaller than 12pt; doubles resolution for retina (screen mobile
  ~150 DPI vs. 72 DPI desktop referenced loosely).
- Communicates with the dev team daily via their in-house system; designer and developer
  "work a different brain," so always ask and defer to the devs as the web pros.

**Developer-review notes (both, CONTEXT):** first staging pass showed parallax + a
scroll-triggered fade animation (timing judged too fast); open questions about
backend-swappable images, over-1920 width behaviour (proposed: fit browser width,
center-crop, keep height), and tablet break point revealing a hamburger menu.

## Notable verbatim quotes

Chris Do (persona voice):

> "My name is Chris Doe and I talk about the business of design."

> "If we're talking about steak and sizzle, this is steak and not a lot of sizzle… the
> meaty part, it's the content, that's the steak. The sizzle is the sexiness — the
> typography, the graphics and the photography and all the treatments."

> "We know that more than half the traffic these days is coming from mobile, so we have to
> really think about mobile. One of these days we're going to design the mobile experience
> first."

> "If you want to work with anybody with a degree of respect to get the most out of them,
> don't prescribe to them solutions — ask questions… You don't need to be the guy who
> pretends to know everything, 'cause you don't. And if you do, you need to hire smarter
> people."

> "When we do fancy designs we get punished for it… because it's not designed to do all
> that stuff."

Futur presenter (CONTEXT — not persona voice):

> "When you design for mobile it looks nice but you don't know the actual size how it's
> going to look on your phone. So what I do is I actually export this on a JPEG or PNG file
> and then open it on your phone."
