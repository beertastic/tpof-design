# TPOF Board Generator

A reusable publishing tool for character production boards.

The image model supplies artwork only. This generator supplies the layout,
metadata, labels, and all small text as real PDF typography. The result is an
A2 landscape PDF suitable for review and printing, plus a 7016 x 4961 PNG at
300 DPI.

## Important source order

Every board must follow the repository's canonical hierarchy:

1. Production Design Bible
2. Faction guide
3. Character document and Character Lock
4. Scene brief
5. Camera direction

The generator does not invent design decisions. It publishes the approved
content in `board-data.json`.

## Install

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tools/board-generator/requirements.txt
```

## Generate Shada

```bash
python tools/board-generator/generate.py 03-characters/shada
```

Outputs:

- `03-characters/shada/Production-Board.pdf`
- `03-characters/shada/Costume-Board.pdf`
- `03-characters/shada/Weapons-Board.pdf`
- `03-characters/shada/Performance-Board.pdf`
- `03-characters/shada/Materials-Board.pdf`
- matching 7016 x 4961 PNG files under `03-characters/shada/renders/`

## Add another character

Only create a folder for a character that currently exists in the production
repository. Do not restore deleted placeholder characters.

1. Copy `03-characters/shada/board-data.json` into the existing character folder.
2. Replace the character metadata and board text.
3. Add five artwork images under `source/artwork/`.
4. Update each board's `artwork` path.
5. Run the generator against that character folder.

## Artwork rules

Artwork should contain no critical small text. It should leave sufficient
negative space and value contrast for layout. Dark costumes must remain
separable from dark environments through lifted background values, wet edge
highlights, atmospheric separation, or material contrast.

## Review workflow

```bash
git switch -c design/<character>-boards
python tools/board-generator/generate.py 03-characters/<character>
git diff --stat
git add tools/board-generator 03-characters/<character>
git commit -m "tools(design): add reusable production board generator"
git push -u origin design/<character>-boards
```
