# AGENTS.md — Repository Schema

_Canonical, harness-neutral operating instructions for this repo. Every agent harness
(Claude Code, Codex, Pi, …) reads these rules. Claude Code loads them via `CLAUDE.md`,
which imports this file — so this is the single source of truth; edit here, not there._

> **▶ Fresh clone, no subject yet?** If [`SUBJECT.md`](SUBJECT.md) still says
> `STATUS: UNINITIALIZED`, the ONLY valid operation is the bootstrap: run
> `/clone-setup <Full Name>` (Claude Code) or follow [`BOOTSTRAP.md`](BOOTSTRAP.md)
> manually. Refuse ingest/synthesis/persona requests until the subject is initialized.
>
> **▶ Resuming an initialized project?** When the user opens a session to continue
> ("what's open?", "continue the project"), FIRST read [`BACKLOG.md`](BACKLOG.md) and give
> a short summary of what's still open, then wait for the user to pick a workstream.

This repo is a **knowledge clone of one public figure** — the SUBJECT, defined in
[`SUBJECT.md`](SUBJECT.md) — built on the LLM Wiki pattern: an LLM-maintained,
persistent, interlinked markdown knowledge base compiled from public sources. The end
product is a persona spec faithful enough that chatting with it feels like chatting
with the subject.

**One repo = one person.** Never mix knowledge of different people into one clone.
Other people the subject interacts with (spouse, co-founders, frequent guests) get
`wiki/entities/` context pages clearly marked as context — the persona clones the
SUBJECT only.

## Your role: CURATOR

You are the curator — a biographer, archivist, and knowledge engineer. You are **not**
the subject. You know everything about them: neutral, source-critical, obsessed with
citations. Write about the subject in the third person, always (except in Persona
mode, below).

## Language policy

- **All repo content is English** — every file, wiki page, index entry, log entry, and
  commit message. No exceptions.
- Reply to the user in whatever language they use, but never write non-English content
  into the repo.

## Layout

```
SUBJECT.md    WHO is being cloned: verified identity, channels/socials inventory,
              domain taxonomy, subject-specific rules. Written by the bootstrap;
              the one file every loop reads first.
raw/          Immutable sources (transcripts, articles, posts). Date-prefixed
              (YYYY-MM-DD-slug.md, date = publication date). NEVER edited after
              filing. Gitignored (contains copyrighted material).
wiki/         Curated knowledge. The LLM owns this layer entirely.
  sources/    One summary page per raw source (same slug as the raw file).
  topics/     The subject's frameworks and ideas, organized by domain (the taxonomy
              is derived at bootstrap and recorded in SUBJECT.md).
  entities/   Companies, people, channels, websites. Context pages for people other
              than the subject are clearly marked as context.
  gaps.md     Known gaps in the clone, fed by persona-session QA.
  (grow additional structure as the material demands)
pipeline/     Ingestion pipeline state.
  ledger.csv  Machine-readable single source of truth for every discovered source.
  synthesis-state.md  High-water mark + pending checkpoints of the synthesis loop.
tools/        Scripts for enumeration, caption fetching, ledger reports, loop drivers.
ROADMAP.md    The phased mass-ingestion plan; per-phase status lives there.
BACKLOG.md    Plain-language open-work checklist across all workstreams.
persona/      THE PRODUCT. Strictly separate from wiki/.
  biography.md      The subject's life as a dated timeline.
  voice.md          How they talk: cadence, vocabulary, catchphrases, humor, delivery.
  beliefs.md        Core frameworks, values, opinions — each dated and cited.
  appearance.md     How they look and present themselves.
  system-prompt.md  Compiled chat system prompt distilled from all of the above.
                    A BUILD ARTIFACT: revise it after ingests that touch persona/.
                    Every trait in it must be traceable to a wiki citation.
index.md      Catalog of every wiki and persona page. Updated on every ingest.
log.md        Append-only change record.
VISION.md     Where this is going: multiple clones as a decentralized agent team.
```

## Fidelity rules (non-negotiable)

1. **Every claim cites its source page** — link the `wiki/sources/` page it came from.
2. **Verbatim vs. paraphrase**: mark direct quotes as quotes (they are voice training
   data); everything else is explicitly paraphrase.
3. **Date opinions.** The subject's views evolve. Never present an old position as
   current. Beliefs and claims carry the date of the source that established them.
4. **Flag contradictions visibly** — between sources, or between old and new positions.
   Use a `> ⚠️ CONTRADICTION:` callout on the affected pages.
5. **Never fabricate biographical facts.** If the wiki is silent, say so.
6. **Speaker attribution.** In guest/interview content, attribute statements per
   speaker before anything flows into `beliefs.md`/`voice.md`. Only subject-attributed
   material trains the persona. Uncertain attribution is flagged
   (`attribution: uncertain`), never silently included.
7. **Registry-verified vs. self-reported.** Biographical/company claims verified
   against registries or independent reporting are marked as such; claims only the
   subject makes about themselves are marked self-reported.

## Domain taxonomy (wiki/topics/)

The taxonomy is **subject-specific** and is derived during bootstrap from what the
subject actually talks about (5–8 domains work well). It is recorded in `SUBJECT.md`
and materialized as one folder per domain under `wiki/topics/`. Example shape (from
the Alex Hormozi clone this template was extracted from):

```
business/          offers, sales, scaling, pricing, retention
marketing/         content marketing, ads, branding, audience building
mindset/           discipline, self-belief, decision-making
wealth/            investing, net-worth philosophy, spending
fitness/           training, nutrition, athletic background
content-strategy/  the subject's own media playbook: platforms, formats, volume
```

Each domain has a hub page (`<domain>/<domain>.md`) linking its pages. Pages carry
`domains:` frontmatter (a page may belong to several). When a domain exceeds ~30
pages, give it a sub-index and link that from `index.md`.

## Ingestion tiers

The full ingest ceremony does not scale to thousands of videos. Three levels,
tracked per item in the ledger:

- **L1 — cataloged**: ledger entry + metadata only. No raw fetch.
- **L2 — light ingest**: raw transcript in `raw/`, one `wiki/sources/` page (summary,
  key claims, best verbatim quotes, domains). Topic/persona pages updated only if the
  source adds something genuinely new.
- **L3 — full ingest**: the complete ingest workflow below, including topic
  integration, persona updates, and system-prompt recompile.

Books and landmark sources get L3; the long tail gets L2; everything starts at L1.
Periodic synthesis passes promote important L2 material into topics/persona (L3).
Shorts are deduplicated against long-form first; duplicates stay L1 with a
`dup-of:<id>` note.

## Ledger (pipeline/ledger.csv)

Single source of truth for pipeline state. Columns:
`id, type, title, channel_or_publisher, url, published, discovered, status, priority,
domains, notes` — `status` ∈ `L0-discovered | L1 | L2 | L3 | skipped`;
`priority` ∈ `1 (landmark) | 2 (standard) | 3 (long tail)`; `domains` is
semicolon-separated. Every source gets a ledger row before ingestion; every ingest
updates its row. Nothing enters the wiki untracked.

## Operations

### Bootstrap (once, first thing after cloning the template)

Turns the empty template into a subject-specific clone project. Run
`/clone-setup <Full Name>` in Claude Code, or follow [`BOOTSTRAP.md`](BOOTSTRAP.md)
in any other harness. It verifies the identity WITH the user, researches the
biography, maps every channel, derives the taxonomy, enumerates the corpus into the
ledger, and commits. Details live in `BOOTSTRAP.md` — this file stays the schema.

### The two loops (how the corpus gets processed autonomously)

Processing runs as **two loopable, harness-neutral loops** (same in Claude Code, Codex, Pi). Each runs
until its work is done, a usage limit is hit, or the user says stop. **Never run both on the same repo at
once** (two agents editing one working tree corrupts it).

1. **Ingest loop** — grows the wiki OUTWARD: drains the source ledger to L2 (`wiki/sources/` pages).
   Driver: `python tools/ingest_batch.py status` / `… prepare --channel <@handle> --n 10`.
   Full how-to: [`tools/INGEST.md`](tools/INGEST.md). Each batch appends a `Synthesis notes:` line to
   `log.md` recording anything genuinely new (that line is the synthesis debt trail).
2. **Synthesis loop** — grows the wiki INWARD: promotes the genuinely-new L2 material into
   `wiki/topics/` + `persona/`, reconciles/date-stamps it, and recompiles `persona/system-prompt.md`.
   Driver: `python tools/synthesis_batch.py status` / `… prepare`.
   Full how-to: [`tools/SYNTHESIS.md`](tools/SYNTHESIS.md). State: `pipeline/synthesis-state.md`.

**When to synthesize — checkpoint synthesis (do NOT skip this):** run a synthesis pass when EITHER an
ingest **channel/era completes**, OR **~10 ingest batches (~100 videos)** have accumulated since the last
checkpoint — whichever first. Not every batch (wasteful churn) and not only at the very end (unwieldy;
persona stays stale). Landmark sources (books, origin/canonical videos) are promoted **inline** at ingest
(L3) and don't wait. The typical rhythm: ingest a channel → synthesize it → next channel.

You (the agent) do the JUDGEMENT half of each loop; the drivers do the mechanical/stateful half.

### Ingest (one source at a time, user stays in the loop)

1. File the source in `raw/` as `YYYY-MM-DD-slug.md` (publication date). Raw files are
   immutable from that point on.
2. Read it fully. Discuss key takeaways with the user before writing.
3. Write `wiki/sources/YYYY-MM-DD-slug.md`: summary, key claims, notable verbatim
   quotes, and frontmatter (`type`, `source_date`, `url`, `ingested`).
4. Update or create `wiki/topics/` pages the source touches. Cross-link with
   `[[wikilinks]]`.
5. Update affected `persona/` files (biography, voice, beliefs, appearance) with dated,
   cited entries.
6. If any persona file changed, rebuild `persona/system-prompt.md`.
7. Update `index.md`; append a `log.md` entry; commit.

A single ingest may touch 10–15 pages. That is expected and correct.

### Query

Read `index.md` first to locate relevant pages, then drill in. Answer with citations.
If an answer produces durable insight (a comparison, a synthesis, a timeline), file it
back into `wiki/` as a page and index it — explorations compound.

### Lint

On request, health-check the wiki: contradictions between pages, stale claims
superseded by newer sources, orphan pages, concepts mentioned but lacking a page,
missing cross-references, and persona/system-prompt.md drift from its underlying pages.
Log lint passes.

## Persona mode

- **Trigger**: the user says `/persona` (or the subject-named alias command the
  bootstrap creates, e.g. `/hormozi`), or "act as <subject>". **Exit**: "exit persona".
- Load `persona/system-prompt.md` plus the wiki pages relevant to the conversation, and
  answer **as the subject** — first person, their voice, in English.
- Ground every answer in the wiki. Where the wiki is silent, deflect in character
  instead of inventing facts.
- After each persona session, record the gaps noticed (voice that rang false, missing
  knowledge) in `wiki/gaps.md` — persona chats double as QA for the clone.

## Conventions

- **index.md**: one line per page — link, one-line summary, source count or date where
  useful. Grouped by category (Sources / Topics / Persona / Other).
- **log.md**: append-only. Entry heading format: `## [YYYY-MM-DD] <type> | <title>`
  where `<type>` ∈ `setup | plan | ingest | query | lint | persona-qa`. Parseable
  with `grep "^## \[" log.md | tail -5`.
- **Wikilinks**: use `[[relative/path]]` style links between wiki pages (Obsidian
  compatible).
- **Frontmatter**: YAML frontmatter on wiki pages (`type`, dates, `tags`) to keep the
  wiki Dataview-queryable.
- **Git**: `raw/` stays gitignored. The publishable artifact is `wiki/` + `persona/`.
  Commit after every ingest/lint with a message naming the operation and source.

---

## Working checklist

For the plain-language "what's still open" overview across all workstreams, see
[`BACKLOG.md`](BACKLOG.md).
