# SUBJECT — who this repo clones

```
STATUS: UNINITIALIZED
```

> ⚠️ **This template has no subject yet.** Run `/clone-setup <Full Name>` in Claude
> Code (or follow [`BOOTSTRAP.md`](BOOTSTRAP.md) in another harness) to initialize.
> Until then, every other operation (ingest, synthesis, persona mode) must refuse.

The bootstrap replaces this file with the filled-in version below. This file is the
**single source of truth for who is being cloned** — every loop reads it first, and no
other fundamental file (AGENTS.md, tools) hardcodes the subject's name.

---

## Template (filled by /clone-setup)

```markdown
# SUBJECT — who this repo clones

STATUS: INITIALIZED (YYYY-MM-DD)

## Identity (user-confirmed YYYY-MM-DD)
- **Name**: <First Last>
- **Born**: <year, place — cite the source page>
- **Known for**: <one paragraph: companies, books, content>
- **Disambiguation**: <how this person was distinguished from same-named people, if relevant>
- **Persona command**: /<slug>  (alias of /persona, created at bootstrap)

## Content universe (feeds pipeline/ledger.csv)
### YouTube channels (TARGET = enumerated into the ledger)
1. @MainHandle <channel-id> — <n> videos, <role: main/clips/company> — TARGET
2. @ClipsHandle <channel-id> — … — TARGET
- Excluded: <dubbed channels, fan channels, spouse's channel, …> (reason each)

### Other platforms (Phase 4)
- X/Twitter: @… · Instagram: @… · LinkedIn: … · Podcast feeds: … · Books: …
- Websites: …

## Domain taxonomy (user-confirmed; folders under wiki/topics/)
- <domain-1>/ — <what goes in it>
- <domain-2>/ — …
(5–8 domains; each gets a hub page at creation)

## Subject-specific rules (grown during ingest; loops must re-read this section)
- <e.g. "channel X is ~75% not the subject — light-triage">
- <e.g. "guest format 'Ask <Name>' → P3">
- <recurring people → wiki/entities/ context pages: spouse, co-hosts, …>
```
