# raw/ — immutable source material (gitignored)

Everything in this folder except this README is **gitignored** — it holds copyrighted
material (video transcripts, book texts, article copies) that must never be published.

Rules (from AGENTS.md):
- Files are date-prefixed: `YYYY-MM-DD-slug.md` (date = publication date).
- **Immutable once filed** — never edited after ingestion.
- Layout: `raw/youtube/<channel-slug>/` for caption transcripts (written by
  `tools/ingest_batch.py`), `raw/books/` for book texts, top level for one-off
  documents.
- Losing this folder is recoverable: the ledger (`pipeline/ledger.csv`) knows every
  source, and captions can be re-fetched.
