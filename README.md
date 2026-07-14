# Persona Clone Template

**Clone the mind of any public figure into a chat persona — from just their name.**

This is a GitHub template for building a *knowledge clone*: an LLM-maintained,
interlinked markdown knowledge base (an "LLM Wiki") compiled from everything a public
figure has ever said in public — YouTube videos, books, podcasts, posts — distilled
into a persona spec faithful enough that chatting with it feels like chatting with
them. It is extracted from a real build: the
**[alex-hormozi-clone](https://github.com/claes-work/alex-hormozi-clone)** — a clone of Alex
Hormozi compiled from ~1,700+ ingested videos and 2 books, with a versioned, fully-cited system
prompt. That repo is a **ready-to-go instance** of this template — look there to see what a finished
clone actually contains.

**One repo = one person.** Knowledge of different people is never mixed. That is a
hard rule, and it is what later lets multiple clones act as independent agents in a
team (see [`VISION.md`](VISION.md)).

## How it works

```
            you type: /clone-setup <Full Name>
                          │
   ┌──────────────────────▼───────────────────────┐
   │ BOOTSTRAP  identity check (you confirm!) →   │
   │            biography research → channel map → │
   │            domain taxonomy → corpus ledger    │
   └──────────────────────┬───────────────────────┘
                          │  you type: /loop /ingest-loop
   ┌──────────────────────▼───────────────────────┐
   │ INGEST LOOP    drains the ledger, batch by    │──┐ every ~10 batches:
   │ (autonomous)   batch: transcript → cited      │  │ SYNTHESIS pass promotes
   │                wiki/sources/ page (L2)        │◄─┘ what's new into topics/
   └──────────────────────┬───────────────────────┘    + persona/, recompiles
                          │                             the system prompt
                          ▼
        persona/system-prompt.md  (THE PRODUCT, versioned, every trait cited)
                          │  you type: /persona   (or /<name> …)
                          ▼
                 💬 chat with the clone
```

Two layers, strictly separated:
- **`wiki/`** — the curated knowledge library: one cited summary page per source,
  topic pages per domain, entity pages for companies/people around the subject.
- **`persona/`** — the product: biography, voice, beliefs, appearance, and the
  compiled `system-prompt.md`. Every trait traceable to a wiki citation.

The operating rules live in [`AGENTS.md`](AGENTS.md) (harness-neutral — Claude Code,
Codex, and Pi all follow the same file). The quality bar is set by its **fidelity
rules**: every claim cited, quotes verbatim-marked, opinions dated, contradictions
flagged, speaker attribution enforced, nothing fabricated.

## Requirements

| What | Why | Get it |
|---|---|---|
| [Claude Code](https://claude.com/claude-code) (recommended) or Codex/Pi | the agent that does all the work | `npm install -g @anthropic-ai/claude-code` |
| Python 3.10+ | pipeline drivers in `tools/` | [python.org](https://www.python.org/downloads/) |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) on PATH | channel enumeration + caption download | `pip install yt-dlp` |
| Git | every batch ends in a commit; the ledger makes resume exact | [git-scm.com](https://git-scm.com) |
| [Obsidian](https://obsidian.md) (optional, recommended) | browse the wiki as a graph | free download |

> A **Claude subscription with generous usage** (Max recommended) matters more than
> hardware — see "How long does it take" below.

## Quickstart

1. **Create your repo from this template** — on GitHub: *Use this template →*, name it
   after the person (e.g. `<first-last>-clone`). Or locally:
   ```
   git clone <this-template> <first-last>-clone && cd <first-last>-clone
   rm -rf .git && git init && git add -A && git commit -m "template"
   ```
2. **Open the folder in Claude Code** and run:
   ```
   /clone-setup <Full Name>
   ```
   The agent researches the name, shows you an identity dossier (who it found, their
   channels, corpus size, effort estimate) and **waits for your confirmation** — then
   researches the biography, maps every channel, builds the domain taxonomy, and
   enumerates the entire corpus into `pipeline/ledger.csv`. (~30–60 min, mostly
   autonomous after your confirmation.)
3. **Start the ingest loop**:
   ```
   /loop /ingest-loop
   ```
   It runs batch after batch autonomously — ingesting, committing, pushing, and
   switching to synthesis at every checkpoint — until the corpus is drained or you
   stop it. In Codex/Pi use the session opener in [`tools/INGEST.md`](tools/INGEST.md)
   instead.
4. **Talk to the clone** (after the first synthesis pass exists):
   ```
   /persona How would you grow a SaaS from 0 to 10k MRR?
   ```
   Exit with "exit persona". Gaps you notice feed `wiki/gaps.md` — persona chats
   double as QA.

That's it. Steps 2–3 are the only two prompts the system needs.

## How long does it take (and what does it cost)

Real numbers from the reference build (Alex Hormozi, ~2,500 long-form videos +
~8,700 shorts across 5 channels + 2 books):

- **Bootstrap**: under an hour.
- **Ingest**: ~10 videos per batch, a batch takes ~10–20 min in Claude Code (parallel
  subagents). The full long-form corpus took **well over 24 hours of cumulative agent
  runtime**, spread over ~2 weeks of looping sessions. This is a marathon, not a
  sprint — and it is token-hungry (a Max plan, or an API budget in the hundreds of
  dollars, is realistic for a corpus this size).
- **A smaller subject** (say 300 long-form videos) is a weekend, not a fortnight.
- The loop is **interruption-safe**: every batch ends in a pushed commit; the ledger
  knows exactly where to resume. Stop and restart whenever you like.
- The persona gets good long before the corpus drains — landmark (P1) sources are
  ingested first, so after the first few synthesis passes the clone is already usable.

## Browsing the wiki with Obsidian

1. Download [Obsidian](https://obsidian.md) (free).
2. *Open folder as vault* → select your repo folder. A minimal `.obsidian/` config
   ships with the template.
3. The wiki uses `[[wikilinks]]` throughout — the graph view shows the knowledge web
   growing as you ingest; `index.md` is the human entry point.

## Repository layout

See the full schema in [`AGENTS.md`](AGENTS.md). The short version:

```
SUBJECT.md      who is being cloned (written by /clone-setup; read by every loop)
raw/            immutable transcripts/texts — gitignored (copyright)
wiki/           the knowledge library (sources/ · topics/ · entities/ · gaps.md)
persona/        THE PRODUCT (biography · voice · beliefs · appearance · system-prompt)
pipeline/       ledger.csv (every source, its status L0→L3) + synthesis-state.md
tools/          drivers: ingest_batch.py, synthesis_batch.py, enumeration scripts
.claude/commands/   /clone-setup · /ingest-loop · /synthesis-loop · /persona
```

## FAQ

**Who is this for?** People with a *large public footprint* — hundreds of videos or
podcasts. Below ~50 long-form sources the clone stays shallow (the bootstrap warns
you).

**Can I run it outside Claude Code?** Yes — the whole pipeline is harness-neutral.
`tools/INGEST.md` and `tools/SYNTHESIS.md` contain paste-ready session openers for
Codex/Pi. You lose self-scheduling loops and parallel subagents, nothing else.

**Why is `raw/` gitignored?** Transcripts and book texts are copyrighted. The
publishable artifact is `wiki/` + `persona/` (your own cited summaries and analysis).
Keep private clones private if you ingest purchased material.

**Two loops? Why not one?** Ingest grows the library outward (fast, parallel, per
source); synthesis grows the clone inward (careful, cross-source reconciliation).
Separating them is what keeps quality high at thousand-video scale. Never run both in
two sessions on the same repo at once.

**What about non-YouTube sources?** Books and documents get filed in `raw/` and
ingested at L3 (highest value per page — do them early if they exist). Websites,
social posts, and press are Phase 4 in [`ROADMAP.md`](ROADMAP.md).

**Where is this going?** Multiple clones, each in its own repo, cooperating as an
agent team — your personal board of advisors. The plan: [`VISION.md`](VISION.md).

## Related

- **[alex-hormozi-clone](https://github.com/claes-work/alex-hormozi-clone)** — the reference build
  this template was extracted from: a live, ready-to-go clone of Alex Hormozi (~1,700+ videos + 2
  books). See it for a worked example of everything this template produces.
