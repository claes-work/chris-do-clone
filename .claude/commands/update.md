---
description: Update THIS clone repo — git pull --ff-only (idempotent, safe). Local command; only updates this one clone.
---

Fast-forward this clone repo to its remote. Safe and mechanical — ff-only never clobbers
local work.

1. **Check state**: `git status --porcelain` — note if there are uncommitted changes.
2. **Pull**: `git pull --ff-only`.
3. **Report**:
   - Advanced → say what came in (new commits / files).
   - `Already up to date.` → nothing to do.
   - Fails (diverged branch, or would overwrite local edits) → report it and STOP; do not
     force, reset, or stash without asking. Let the user resolve, then re-run.
4. **No wiki write, no done-gate.** This only syncs git state — it produces no artifact,
   so skip persistence entirely.

To update every clone plus the orchestration layer at once, use `/update` from the
persona-roster repo instead.
