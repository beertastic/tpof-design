# Shada Production Package

This rebuild removes blurred AI-generated labels from the board artwork.

- All production text is real PowerPoint text and vector PDF typography.
- Artwork is placed without cropping.
- The five review PDFs are A2 landscape.
- PNG renders are 7016 x 4961 pixels at 300 DPI.

## The master is `board-data.yaml` — not the PowerPoint

`source/Shada-Production-Boards.pptx` is **generated output, not an editable
master.** `tools/board-generator/generate.py` overwrites it on every run, so any
hand-edit made in PowerPoint is silently destroyed the next time the boards are
built.

To change a board, edit `board-data.yaml` and regenerate. To change an image,
replace the file in `source/artwork/` keeping the same filename, and regenerate.

```bash
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
```

## What is committed

| Path | Tracked | Why |
|---|---|---|
| `Character.md`, `Character-Lock.md`, `Prompts.md` | Yes | Source of truth |
| `board-data.yaml` | Yes | The board master |
| `source/artwork/*.png` | Yes | **Not reproducible** — the generated artwork itself |
| `references/` | Yes | Approved reference photographs |
| `*.pdf` (five board PDFs) | Yes | The review deliverable |
| `renders/*.png` | No | ~87 MB per character, fully regenerable |
| `source/*.pptx`, `source/*-Production-Boards.pdf` | No | Intermediate build output |

Regenerable output is kept on disk as one current copy and is gitignored, so the
repository does not accumulate a new 87 MB copy on every rebuild.
