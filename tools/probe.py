#!/usr/bin/env python3
"""Corpus probe that survives hard-wrapping and markdown emphasis.

WHY THIS EXISTS
---------------
`grep` is LINE-BASED. This corpus is hard-wrapped at ~100 characters and written with heavy
inline markdown. So a two-word probe silently returns zero whenever the corpus happens to
wrap between the words, or bolds one of them:

    corpus text:  "…mutual connection Diane\n  Gibbs and a relevant story…"
    grep -ril "Diane Gibbs"  ->  0        # WRONG — it is right there
    corpus text:  "**Diane** Gibbs"
    grep -ril "Diane Gibbs"  ->  0        # WRONG — emphasis between the tokens

Found 2026-07-31 after two false "0 corpus-wide" claims were written into source pages in
one session (`Jose Caballero`/`Caballer`, and `Diane Gibbs`). Both would have entered the
wiki as new entities; the second is already documented as a real connection of his.

This probe normalises whitespace and strips markdown emphasis before matching, so a phrase
is found regardless of how the file happens to be wrapped or styled.

⚠️ IT DOES NOT FIX MIS-HEARD NAMES. A whisper transcript that writes "Caballero" for
"Caballer" still probes to zero. For proper nouns, probe a TRUNCATED STEM as well —
`--stem` does this automatically. See the probe rules in SUBJECT.md.

USAGE
    python3 tools/probe.py "third truth"
    python3 tools/probe.py --stem "Diane Gibbs" "Andrea Stern"
    python3 tools/probe.py --files "reverse sale"      # list matching files, not just count
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOTS = [REPO / "wiki", REPO / "persona"]

EMPHASIS = re.compile(r"[*_`~\[\]]+")
WS = re.compile(r"\s+")


def normalise(text: str) -> str:
    """Collapse wrapping and drop markdown emphasis so phrases match across both."""
    return WS.sub(" ", EMPHASIS.sub("", text)).lower()


def corpus() -> dict[Path, str]:
    out: dict[Path, str] = {}
    for root in ROOTS:
        if not root.is_dir():
            continue
        for p in root.rglob("*.md"):
            try:
                out[p] = normalise(p.read_text(errors="replace"))
            except OSError:
                continue
    return out


def stems(term: str) -> list[str]:
    """For a multi-word proper noun, also try each word truncated by one or two chars.

    Machine transcripts add and drop trailing vowels ("Caballer" -> "Caballero"), so the
    surviving prefix is the reliable part.
    """
    words = [w for w in term.split() if len(w) >= 5]
    out = []
    for w in words:
        out.append(w)
        if len(w) >= 7:
            out.append(w[:-2])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("terms", nargs="+")
    ap.add_argument("--stem", action="store_true", help="also probe truncated word stems (proper nouns)")
    ap.add_argument("--files", action="store_true", help="list matching files")
    a = ap.parse_args()

    docs = corpus()
    print(f"{len(docs)} corpus pages (whitespace- and markdown-normalised)\n")
    for term in a.terms:
        t = normalise(term)
        hits = [p for p, txt in docs.items() if t in txt]
        print(f"  {term!r:34} {len(hits):4}")
        if a.files:
            for p in hits[:8]:
                print(f"      {p.relative_to(REPO)}")
        if a.stem:
            for s in stems(term):
                sh = [p for p, txt in docs.items() if normalise(s) in txt]
                flag = "  <== phrase said 0, stem does not" if not hits and sh else ""
                print(f"      stem {s!r:28} {len(sh):4}{flag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
