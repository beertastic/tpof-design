# TPOF Top-Level Board Generator

This tool rebuilds character production boards from existing artwork and a
character-local `board-data.yaml` file.

It follows the repository hierarchy: Production Design Bible first, followed
by faction guidance, the character document and Character Lock, then the board
brief. The generator is a publishing tool; it does not invent design choices.

## Why this exists

Replace an image in `03-characters/<character>/source/artwork/`, keep the same
filename, and rerun one command. The editable PowerPoint master, A2 PDFs and PNG
review renders are rebuilt locally with crisp typography and uncropped images.

## Requirements

- Python 3.10 or later
- Python packages in `requirements.txt`

**No LibreOffice required.** Boards are drawn straight to PDF with `reportlab` —
vector text, no PowerPoint intermediate, no external process. The old
PPTX-then-convert pipeline needed `libreoffice-impress`, which is easy to be
missing and gives an unhelpful *"source file could not be loaded"* when it is.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tools/board-generator/requirements.txt
```

## Commands

```bash
# Validate Shada without generating files
python tools/board-generator/generate.py shada --validate

# Generate all five Shada boards and 300-DPI previews
python tools/board-generator/generate.py shada

# Generate one board
python tools/board-generator/generate.py shada --board weapons

# Generate lighter review previews
python tools/board-generator/generate.py shada --dpi 150

# Generate PDFs but no PNG previews
python tools/board-generator/generate.py shada --pdf-only

# Generate every currently existing configured character
python tools/board-generator/generate.py --all

# Generate the A4 promo sheet instead of the boards
python tools/board-generator/generate.py shada --promo
```

`--all` discovers folders dynamically. It never uses a hard-coded character
list and therefore does not recreate deleted characters.

## Character setup

A character participates only when its existing folder contains:

```text
03-characters/<character>/board-data.yaml
```

Artwork paths in that file are relative to the character directory. Images are
always placed using a contain operation, preserving the full frame rather than
cropping it.

## Outputs

- One PDF per board, in the character folder
- Matching PNG previews under `renders/` (gitignored)

## Boards are defined by the config

Board order and names come from `board-data.yaml`, not from the tool. A character
can have as many boards as the work needs — Baylan has eight, including one
costume turnaround sheet per outfit.

`--board <key>` generates a single board, using the key from the config.

## Recommended workflow

```bash
cp replacement.png 03-characters/shada/source/artwork/forest.png
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada

git acp "design(shada): new forest plate"
```

## The promo sheet — `--promo`

A single A4 portrait page for people **outside** the production: press packs,
festival submissions, funding decks, a link to send someone who asked what the
character looks like.

It is deliberately the inverse of a board. A board is exhaustive and neutral —
flat light, every fitting legible, nothing concealed. The promo sheet is
selective and atmospheric: one hero image carrying the page, sparse type, a
teaser rather than a spec.

```bash
python tools/board-generator/generate.py shada --promo
python tools/board-generator/generate.py shada --promo --validate
python tools/board-generator/generate.py --all --promo
```

Driven by `03-characters/<character>/promo-data.yaml`, styled by
`templates/promo-a4.yaml`. Output is `<Character>-Promo.pdf` in the character
folder.

### The page

```text
┌──────────────────────────────────────────────┐
│ NAME                        project · kicker │
│ role                                         │
├───────────────┬──────────────────────────────┤
│ panels:       │                              │
│  heading      │        hero_image            │
│  text         │        (cover crop,          │
│  items        │         hero_anchor picks    │
│               │         what survives)       │
├───────────────┴──────────────────────────────┤
│ logline          (large)                     │
│ pull             (secondary, italic)         │
├──────────────────────────────────────────────┤
│ WEAPONS & EQUIPMENT                          │
│ [plate] [plate] [plate]   + captions         │
│ notes, in columns                            │
├──────────────────────────────────────────────┤
│ field: optional image strip, pinned          │
│ project · kicker · disclaimer                │
└──────────────────────────────────────────────┘
```

`panels` and `weapons.notes` take as many entries as you give them, so the
length of the page is set by the copy. Weapon plates use a **contain** fit —
they are prop photographs on plain ground and cropping them cuts the prop. The
hero and the optional `field` strip use **cover**, with a per-image `anchor`
between 0 and 1 choosing what survives the crop (low keeps the top, which is
usually where the face is).

**Two rules for the content.**

*It is never a costume authority.* Nothing is ever matched against it, and it
carries no non-negotiables. Only the boards and the approved turnaround do that.

*Keep it spoiler-free unless someone has decided otherwise.* `Character.md` is
full of plot — who dies, when and at whose hand. None of that belongs on a page
you hand to a stranger. Decide it deliberately; do not copy-paste.

The page flows from the title down and the footer is pinned, so overlong copy
collides rather than reflowing onto a second page. The generator **warns and
still writes the file** — check the warnings, not the exit code. The left-column
warning reports the measured height and the `hero_height` that would match it:

```text
! Shada-Promo.pdf: left column runs 4.43in against a 4.05in hero —
  trim a panel, or set `hero_height: 4.43`
```

Setting `hero_height` to that number squares the bottom of the image with the
bottom of the text column, which is what the page wants to look like.

## Outputs and version control

The PPTX is **generated output, not an editable master** — it is overwritten on
every run, so hand-edits made in PowerPoint are lost. `board-data.yaml` is the
master.

Committed: `board-data.yaml`, `source/artwork/`, and the five board PDFs.

Gitignored: `renders/`, `source/*.pptx`, `source/*-Production-Boards.pdf`. These
are reproducible from one command and run to ~100 MB per character per rebuild.
One current copy is kept on disk; none go into history.
