# Story and Script Reference

**`scenes/` holds the screenplay. It is the source of truth for this entire
repository** — current draft v9, added 2026-08-01. Where a design document
disagrees with it, the script wins and the document is wrong until somebody
records a deliberate departure.

The authoritative file is **`the-price-of-freedom-v9.fountain`** — plain text,
so a draft change is a diff rather than two PDFs held up to the light. The
typeset PDF the writer sent is kept beside it as the evidence the conversion was
checked against. Render a readable copy any time:

```bash
python tools/script-convert/render.py                # PDF
python tools/script-convert/render.py --format fdx   # Final Draft, for the writer
```

Rendered output is gitignored. See
[`tools/script-convert/README.md`](../tools/script-convert/README.md) for how the
conversion was verified and where it stops being the right tool.

[`Scene-Index.md`](Scene-Index.md) is the scene list, following the screenplay.
[`Scene-Elements.md`](Scene-Elements.md) holds the per-scene props, set dressings
and costumes extracted from the Filmanize breakdown before that export was
deleted on 2026-08-01 — the screenplay lists none of those, so it was worth
keeping.

Open disagreements between the script and the design documents are tracked in
[`11-production-tracking/Script-v9-Reconciliation.md`](../11-production-tracking/Script-v9-Reconciliation.md).

This folder stores script-derived design information and scene indexes. Filmanize remains the production-management source for breakdown and scheduling; this repository stores canonical design documentation and revision history.
