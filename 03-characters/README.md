# Character Bible

Each character has an individual folder and a canonical Markdown file. Status values are:

- `placeholder`
- `in-development`
- `review`
- `approved`
- `locked`

All visual development must begin with the Production Design Bible in `../01-production-design/`.

## Folder contents

| File | Purpose |
|---|---|
| `Character.md` | The canonical character document. |
| `Character-Lock.md` | Non-negotiable traits and the design-drift rejection list. Added at lock. |
| `Prompts.md` | Self-contained image prompt pack — one prompt per artwork slot. |
| `board-data.yaml` | Board layout and content. **This is the board master.** |
| `source/artwork/` | Generated images, named to match `board-data.yaml`. Tracked — not reproducible. |
| `*.pdf` | The five A2 review boards. Tracked. |
| `renders/` | 300 DPI PNG previews. **Gitignored** — regenerable, ~87 MB per character. |
| `source/*.pptx` | Intermediate build output. **Gitignored** — overwritten on every run. |

`shada/` is the worked reference for all five.

## Prompt packs

`Prompts.md` inlines the full Production Design Bible ruleset rather than
referencing it. This is deliberate — an image generator reading one file in
isolation must still receive every constraint. The canonical shared blocks live
in `../09-prompts/Global-Style-Block.md`; if you change a rule there, propagate
it to the character files.

A pack marked `status: scaffold` has correct shared style rules but incomplete
character content. Every `**NEEDS:**` marker is an unanswered design question.
Fill in `Character.md` before completing the pack.

## Workflow

1. Author `Character.md`, then `Character-Lock.md`.
2. Complete `Prompts.md` from the lock.
3. Generate images, saving to `source/artwork/` at the ratios the pack specifies.
4. Create `board-data.yaml` modelled on Shada's.
5. `python tools/board-generator/generate.py <character>`

## What is committed

Source documents, `board-data.yaml`, `source/artwork/` and the five board PDFs.

Everything else the generator produces — `renders/`, the PPTX and the multi-page
master PDF — is gitignored. It is all reproducible from one command, and at
~100 MB per character per rebuild it would otherwise dominate the repository.
Git keeps every version of a binary forever, so a re-render is not a replacement,
it is an addition.
