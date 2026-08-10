# Notebook Export

Flattens the whole repository into **one file**, for tools that cannot read a git
repository — written for Google NotebookLM, useful for any RAG or chat tool that
takes a single upload.

```bash
./tools/notebook-export/build.py                    # TPOF-Complete.md
./tools/notebook-export/build.py --pdf              # ...and TPOF-Complete.pdf, illustrated
./tools/notebook-export/build.py --pdf --include-actor-photos
```

Both outputs are **gitignored**. They are copies of the tree and go stale the
moment anything is committed, so they are rebuilt on demand and never stored.

## The two outputs are not interchangeable

| | `TPOF-Complete.md` | `TPOF-Complete.pdf` |
|---|---|---|
| Text | Everything | Everything |
| **Images** | **None — only an inventory listing them** | **Placed inline** |
| Build time | Seconds | Minutes |

**This split is forced by NotebookLM, not chosen.** An uploaded `.md` is read as
TEXT. Markdown image syntax, relative paths and base64 data URIs are all
discarded — there is no way to get a picture into a notebook through a markdown
file. Images survive only inside a PDF, which NotebookLM does look at.

So: **upload the `.md` if you want the writing, the `.pdf` if you want the
artwork, and both if you want both.** NotebookLM takes multiple sources and they
are the same document, so nothing contradicts.

## What it does that `cat *.md` would not

**Every section prints the file it came from**, as a repo-relative path, in the
body text where retrieval can see it. The one thing genuinely lost in flattening
is provenance — a notebook answer is grounded in "the document", not in
`03-characters/shin/outfits.yaml`. Ask the export where something is written down
and it can answer with a path you can open.

**It refuses to ingest contradictions.** `.claude/worktrees/` holds full copies of
the tree at older commits, and the v9 screenplay differs from v10 in ways the
reconciliation document explains. Feeding a retrieval engine three versions of
Baylan's costume is the worst thing that could be done to it. Both are skipped,
and the skip list with its reasons is printed in the export itself.

**It deduplicates the plates.** 244 image files, 101 distinct — `prompts/attach/`
stages a copy of the same reference into a folder per prompt, so Baylan's three
face-build photographs exist eight times each. The inventory lists all 244 with
the copies marked; the PDF places each picture once.

**It is idempotent, and it does not eat itself.** The export lands in the
repository root as a `.md`, so the first version ingested its own previous
output and the word count doubled from 277k to 554k. Both outputs are excluded
by path.

## Photographs of real people are withheld by default

`reference/actor/` holds photographs of named performers. `vala/reference/fitting/`
is a costume fitting whose subject's permission is a standing open risk in the
delivery plan — see `11-production-tracking/Delivery-Plan-2026-08-14.md`.

**Uploading to NotebookLM is uploading to Google.** That is not the art
department's to do as a side effect of a tooling test, so those 29 files are
listed in the inventory — the export records that they exist and where they
live — and their pixels stay in the repository. `--include-actor-photos` overrides
it, deliberately and per run.

## Size

~277,000 words, ~1.6 MB. NotebookLM's limit is **500,000 words per source**, so
there is roughly 45% headroom. The build prints the count and warns if a future
version of the repository crosses it — at which point the fix is to split by
part, not to trim.

## Rendering

The PDF goes through `tools/build-guide-pdf`'s renderer, imported as a module.
That renderer's markdown subset is small and deliberately so; the export needed
two additions to it, both made there rather than worked around here:

- **fenced code blocks**, so an embedded `outfits.yaml` sets as monospace instead
  of turning every `#` comment into a heading
- **a fix to `inline()`**, which converted code spans before applying italics and
  so let the italic rule reach inside its own output — one `.gitignore` line
  quoted in a README produced crossed tags and reportlab refused the whole
  document

Both were verified against the existing build guides, which render byte-identically.
