---
description: Initialize this template for ONE public figure (bootstrap - identity check, biography research, channel enumeration, taxonomy). Usage - /clone-setup First Last
---

You are the CURATOR (see CLAUDE.md / AGENTS.md — they govern everything). Bootstrap this
repo for the person named in $ARGUMENTS by executing **BOOTSTRAP.md exactly** — read it
now, it is the authoritative procedure. This command only adds the harness-specific
notes below.

## Guards (check before anything else)

1. `SUBJECT.md` contains `STATUS: INITIALIZED` → **refuse**: this repo already clones
   someone. One repo = one person; a new person needs a fresh copy of the template.
2. `$ARGUMENTS` empty or not a plausible person name → ask the user for the person's
   full name; do nothing until given.

## Execution notes (Claude Code specifics)

- **Phase 0 (identity)**: use parallel web-research agents for candidate discovery and
  channel inventory. Present the dossier + corpus-size estimate + effort estimate
  (README "How long does it take") as a compact summary, then use AskUserQuestion to
  get explicit confirmation (or candidate selection). **HARD STOP until confirmed.**
- **Phase 1 (subject definition)**: propose the 5–8 domain taxonomy and confirm it with
  the user in the same interaction if possible (they may know the person's content
  focus better than the initial research does).
- **Phase 2 (research)**: fan out parallel agents — one per dossier (biography, media
  inventory, companies/entities). Each writes only its own files; you (the
  coordinator) wire index.md, log.md, SUBJECT.md updates afterwards.
- **Phase 3 (enumeration)**: run the fetch/merge/backfill commands from BOOTSTRAP.md
  per TARGET channel. yt-dlp 429s are logged, not fatal.
- **Phase 4 (wrap-up)**: commit `bootstrap: <first-last>`; push only if a remote is
  configured. End your final message with the exact next step:
  `/loop /ingest-loop` — and mention `/persona` will only get good after the first
  synthesis pass.

## Quality bar

The bootstrap decides the ceiling of the whole clone. Do not rush Phase 2: the
biography dossier and the media inventory are the backbone every later ingest hangs
off. Fidelity rules (cite, date, verbatim-vs-paraphrase, registry-vs-self-reported)
bind from the very first page.
