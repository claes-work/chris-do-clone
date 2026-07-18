---
type: youtube-video
source_date: 2021-09-04
url: https://www.youtube.com/watch?v=BpTMsCL_9Bs
channel: "@thefutur"
ingested: 2026-07-18
tier: L2
domains: [design-craft]
tags: [built-by-hand, ben-burns, webflow, animation, dark-mode, lottie, after-effects, web-design, context, do-not-train]
attribution: not-subject
---

# Animations & Interactions: Dark Mode

## Summary

**Speaker: Ben Burns** (Futur designer / creative director), NOT Chris Do — this is an
episode of the **"Built By Hand"** series in which Ben rebuilds his personal website in
Webflow. **Chris Do does not appear in this video.** Guests: **Greg Gunn** (illustrator /
animator, helps with After Effects + Lottie) and **Timothy Ricks** ("Trixx," a Webflow
expert, helps with custom code). This episode covers adding animations, micro-interactions,
and a light/dark-mode toggle to the site. Because none of the material is Chris-attributed,
the **entire page is CONTEXT / DO-NOT-TRAIN** — nothing here feeds `persona/` (voice, beliefs,
biography). It is retained only as web-design-craft reference and to document the Futur team's
own media output.

## Key claims (2021-09-04, paraphrased; Ben Burns unless noted — all context, not persona)

- A genuinely good website does not *need* fancy animations or visual effects; the point is
  stated twice for emphasis (context: design principle, per Ben).
- Micro-interactions and animation can make a site more delightful, but pushing past user
  expectations can also make a site harder to use — it's a balance that depends on the project.
- Business-critical or life-critical sites should prioritize usability over flashy effects;
  a passion/portfolio project can "roll the dice" a bit on usability for the sake of coolness.
- Invokes the **Ira Glass "the gap"** idea: there is always a gap between the level of your
  taste and the level of your skill/output; this project narrowed Ben's animation-skill gap
  slightly toward his taste. (The Futur teaches this framing broadly; here it's Ben citing it.)
- Webflow animation basics: an interaction has a **trigger** (hover, click, scroll-into-view,
  or scroll position) → an **action/animation** on a timeline (top = start, bottom = end);
  Ben prefers custom animations over Webflow's presets, and uses **easing** to make motion
  feel natural. Multiple actions can share one timeline so one click fires many changes.
- For a complex toggle (sun→moon), hand-animating ~40–50 Webflow actions per direction would
  be heavy and fragile; better to animate it externally and import a **Lottie** file — a
  vector-based, lightweight, resizable web-animation format (Ben likens it to a GIF).
- Lottie animations are typically made in **After Effects**; Ben had never opened After Effects
  before this episode and brought in Greg Gunn to help; he plans to take the Futur's
  "Animation for Designers" course.
- The hard bug: a Webflow-only dark-mode toggle reverts to light mode on page reload / link
  navigation because the state isn't persisted. **Tim Ricks'** fix: custom code that adds a
  class to the page `<body>` on click and writes a **cookie** so the browser remembers the
  user's mode across pages.
- Follow-on Lottie problem: on each new page the Lottie rewinds to frame 0, so a dark-mode
  user's toggle appeared wrong/invisible. Solution: keep **two Lottie switches** — one
  starting at the beginning playing forward, one starting at the end playing backward — and
  show/hide the correct one based on the active mode class.
- Meta-lesson (the episode's takeaway, per Ben): "do it yourself" doesn't have to mean "do it
  alone." Knowledge is abundant online; the real challenge is knowing *what* to learn, and
  having knowledgeable friends/community to lean on when stuck. (Note: general self-help
  framing, delivered by Ben, not Chris.)

## Notable verbatim quotes (attributed per speaker — all context, not persona)

> "Really good sites do not need fancy animations or visual effects. We'll say it again: in
> order for your site to be a good website, it does not need to have fancy animations or
> visual effects." — Ben Burns

> "There's always a gap between the level of your taste and what you're able to create, and
> that's that level of skill that you have. And for this super extra animation stuff, there's
> a pretty big gap for me." — Ben Burns

> "Two designers try and pretend to be developers and end up smashing their head against
> something… emerge victorious but bloodied. That felt so good. For me there's no better
> feeling than cracking a difficult problem." — Ben Burns

> "Knowledge is everywhere… but knowing what to learn, knowing what to look for, that's the
> new challenge — like looking for a needle in a haystack without knowing what a needle looks
> like." — Ben Burns

> "Do it yourself doesn't need to mean do it alone. So get out there, make friends, contribute
> to a community in a meaningful way, and those relationships will help you a lot in the long
> run." — Ben Burns

> "When you click the switch the Lottie played from the beginning to the end and then paused,
> and then a little piece of custom code added a class name to the page body which switched
> all the colors… and that same piece of code added a cookie to the user's browser which
> helped the browser remember if the user was on light mode or dark mode." — Ben Burns
> (describing Tim Ricks' solution)

> "I like this low-key intro a lot better; it sets the bar where it should be." — Greg Gunn

## Cross-links

- [[wiki/topics/design-craft/design-craft]] — web-design / animation craft reference (context only)
- Series sibling episodes: other **"Built By Hand"** (Ben Burns) episodes on the @thefutur
  channel — same do-not-train attribution applies.
- NOTE: **No L3 candidate.** This is not Chris-taught material; nothing here is promoted to
  `persona/`. Web animation/dark-mode UI is outside Chris Do's teaching domain and the speaker
  is Ben Burns, so the entire page stays context / do-not-train.
