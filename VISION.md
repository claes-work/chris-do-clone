# VISION — from one clone to a team of minds

_The direction this template is heading. Nothing here is required to build a single
clone; it explains design decisions that already exist (one repo per person, the data
contract) and sketches the stages ahead._

## The end state

A **decentralized roster of persona clones** — each a self-contained git repository
built from this template — that can be composed into an **agent team**: "Alex Hormozi
and Neil Patel, work out a launch plan for my product." Each agent brings its
subject's actual, cited knowledge and voice; they argue, divide work, and produce an
answer no single generic model would give.

Think: a team of employees, where every employee is a world expert with a documented,
verifiable body of knowledge.

## Design decisions already baked into the template (and why)

1. **One repo = one person.** The hard separation is not bureaucracy — it is what
   makes composition possible. Knowledge provenance stays clean per person; an agent
   can never accidentally answer with another persona's beliefs. Mixing knowledge
   would poison both clones irreversibly.
2. **Decentralized by construction.** A clone is a folder of markdown + a git remote.
   No server, no database, no vendor. Any machine that can clone the repo can run the
   persona. Clones can live on different machines and still form a team.
3. **A uniform data contract.** Every clone built from this template exposes the same
   interface:
   - `SUBJECT.md` — machine-readable identity (who am I, what domains do I cover)
   - `persona/system-prompt.md` — the compiled, versioned persona (load this = be them)
   - `index.md` → `wiki/**` — the cited knowledge base for retrieval during a session
   - `wiki/gaps.md` — honest self-knowledge of what the clone does NOT know
   Because every repo has the same shape, an orchestrator needs zero per-persona code.
4. **Citations all the way down.** In a multi-agent debate, "because I said so" is
   worthless. Every claim a persona-agent makes can be traced to a dated source page —
   so disagreements between two clones are *resolvable* (check the sources), not
   just noise.

## Stages to get there

### Stage 1 — Roster (now)
Build clones one at a time from this template. Each lives in its own repo, maintained
by its own ingest/synthesis loops. Quality bar: the persona session feels like the
person; `gaps.md` shrinks over time.

### Stage 2 — Single clone as a reusable agent
Expose one clone to other projects. Two cheap paths, both already supported by
today's tooling:
- **Subagent definition**: a `.claude/agents/<slug>.md` whose system prompt is the
  clone's `persona/system-prompt.md` and whose tools are read-only access to the
  clone's repo (Read/Grep/Glob). Any project on the machine can then summon the
  persona for a question. (This mirrors how the reference build already exposes a
  read-only "second-brain" research agent.)
- **MCP server** (for remote/decentral use): a thin server per clone exposing
  `ask(question)` + `search(query)` over the repo. The clone stays a git repo; the
  server is stateless glue.

### Stage 3 — The roundtable (multi-clone orchestration)
An orchestrator (a plain Claude Code session, or a small harness) that:
1. Takes a problem + a chosen roster ("Hormozi × Patel").
2. Spawns one persona-agent per clone (each loaded ONLY with its own system prompt +
   its own repo access — the one-repo-one-person rule at runtime).
3. Runs a structured exchange: independent takes → cross-examination (each persona
   critiques the others *in character, citing its sources*) → synthesis by a neutral
   moderator agent (the curator role, not a persona).
4. Outputs a recommendation with per-persona attribution ("Hormozi argues X because
   [cited]; Patel counters Y because [cited]").
Key rule carried over from the repos: personas never read each other's wikis. They
exchange *statements*, not knowledge bases — exactly like real people in a meeting.

### Stage 4 — Living clones
The freshness loop (ROADMAP Phase 5) keeps each repo current on a schedule: new
videos auto-ingest weekly, synthesis checkpoints fire automatically, the system
prompt version ticks up. The roster stays current without manual sessions.

## Non-goals

- **No merged "super-brain".** The value is in distinct, honest perspectives.
- **No impersonation outside the sandbox.** Clones are research/advisory tools over
  public statements; they say what the person has said, dated and cited — they don't
  pretend to BE the person to third parties.
- **No fabrication.** A clone that doesn't know, deflects — in character — and logs
  the gap. That property must survive orchestration.
