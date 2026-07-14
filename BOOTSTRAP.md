# BOOTSTRAP — from empty template to initialized clone project

_Harness-neutral procedure. In Claude Code, `/clone-setup <Full Name>` executes
exactly this. In Codex/Pi, paste: "Read AGENTS.md and BOOTSTRAP.md, then bootstrap
this repo for <Full Name>." One bootstrap per repo — one repo per person._

**Input**: the full name of ONE public figure. Nothing else.
**Output**: an initialized repo where the ingest loop can start immediately.

## Phase 0 — Identity verification (STOP-gate: user must confirm)

1. Web-research the name. Build a candidate list if the name is ambiguous.
2. For the (or each) candidate, establish: who they are, birth year, what they're
   known for, and their **main content channels** with rough sizes (YouTube subscriber/
   video counts, podcast, books, socials).
3. **Viability check** — this pattern needs a large public corpus. Rough guide:
   - 500+ long-form videos → excellent (the Hormozi reference build had ~4,000)
   - 100–500 → good
   - < 50 long-form videos/podcasts → warn the user: the clone will be shallow.
4. Present a short dossier (identity + channels + corpus size estimate + expected
   ingest effort) and **WAIT for explicit user confirmation**. Never proceed on a
   guess. If ambiguous, let the user pick the candidate.

## Phase 1 — Subject definition

After confirmation:

1. Fill **`SUBJECT.md`** from its embedded template: identity, content universe
   (every official channel with channel IDs; excluded channels with reasons),
   proposed **domain taxonomy** (5–8 domains derived from what the person actually
   talks about — show the user, adjust on feedback), persona command slug.
2. Create the taxonomy folders + hub pages under `wiki/topics/<domain>/<domain>.md`.
3. Create the persona alias command: copy `.claude/commands/persona.md` to
   `.claude/commands/<slug>.md` (e.g. `patel.md`) so `/patel` works like `/persona`.
4. Add subject-specific priority markers to `tools/merge_staging.py`
   (`P1_EXTRA`: book titles, signature formats; `P3_EXTRA`: "Ask <Name>"-style guest
   formats) — the BOOTSTRAP HOOK comments mark the spot.

## Phase 2 — Biography & master source map (deep web research)

Same as the reference build's Phase 1 (see ROADMAP.md):

1. **Biography dossier** → `wiki/sources/YYYY-MM-DD-research-biography-dossier.md`
   (today's date; type `web-research`): full dated life timeline, family, education,
   companies, controversies — registry-verified vs self-reported marked per claim.
   Then distill `persona/biography.md` v1 from it (dated, cited, confidence markers).
2. **Media inventory dossier** → `wiki/sources/YYYY-MM-DD-research-media-inventory-dossier.md`:
   every channel, podcast, website, social profile with verified IDs and counts.
   This defines the enumeration universe and updates SUBJECT.md's channel list.
3. **Companies/entities dossier** (if the subject is a business figure) → registry
   lookups where reachable; `wiki/entities/` pages for companies, key people
   (context-marked), channels, websites.

Use parallel research agents where the harness supports them; verify claims across
independent sources before they enter `persona/biography.md`.

## Phase 3 — Corpus enumeration (network, mechanical)

For each TARGET channel in SUBJECT.md:

```
# /videos and /shorts tabs separately:
.\tools\fetch_channel.ps1 -Url "https://www.youtube.com/@Handle/videos" -Out "pipeline\staging-handle-videos.csv"
.\tools\fetch_channel.ps1 -Url "https://www.youtube.com/@Handle/shorts" -Out "pipeline\staging-handle-shorts.csv"
python tools/merge_staging.py --channel @Handle --videos pipeline/staging-handle-videos.csv --shorts pipeline/staging-handle-shorts.csv
python tools/backfill_metadata.py --channel @Handle --top 50   # dates+views; top-N by views -> P1
```

Delete the staging CSVs afterwards. If backfill rate-limits (429), log it and move
on — dates backfill lazily during ingest too.

## Phase 4 — Wrap-up

1. Update `index.md` (dossier pages, entity pages, topic hubs) and `ROADMAP.md`
   phase checkboxes; write `BACKLOG.md`'s snapshot line.
2. Append `log.md` entries (`setup | bootstrap: <Name>` + one per research dossier).
3. Commit everything (`bootstrap: <first-last>`), push if a remote exists.
4. Report to the user: corpus size (ledger counts per channel/priority), estimated
   ingest effort (see README's "how long does it take"), and the exact next command
   (`/loop /ingest-loop` or the Codex/Pi session opener in `tools/INGEST.md`).

## Guardrails

- `SUBJECT.md` already `INITIALIZED` → refuse (one repo, one person; start a new repo
  from the template for another person).
- Never skip the Phase-0 user confirmation.
- Everything written is English, cited, and dated (AGENTS.md fidelity rules apply
  from the first file on).
