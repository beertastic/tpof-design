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
- LibreOffice available on `PATH`
- Python packages in `requirements.txt`

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

The generator writes:

- `source/<Character>-Production-Boards.pptx`
- `source/<Character>-Production-Boards.pdf`
- the configured individual PDFs in the character folder
- configured PNG previews under `renders/`

## Recommended workflow

```bash
cp replacement.png 03-characters/shada/source/artwork/forest.png
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada

git acp "design(shada): new forest plate"
```

## Outputs and version control

The PPTX is **generated output, not an editable master** — it is overwritten on
every run, so hand-edits made in PowerPoint are lost. `board-data.yaml` is the
master.

Committed: `board-data.yaml`, `source/artwork/`, and the five board PDFs.

Gitignored: `renders/`, `source/*.pptx`, `source/*-Production-Boards.pdf`. These
are reproducible from one command and run to ~100 MB per character per rebuild.
One current copy is kept on disk; none go into history.
