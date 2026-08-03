# Character Bible

> **Picking up the next character?** Read
> [`NEXT-CHARACTERS-BRIEF.md`](NEXT-CHARACTERS-BRIEF.md) — where everyone stands,
> what each one is blocked on, and the exact questions to settle before writing
> their files.
>
> **Building a character from scratch? Start with
> [`Character-Build-Recipe.md`](Character-Build-Recipe.md)** — the order of
> operations from documents to six boards, with `shada/` as the worked example.
> Then [`../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md`](../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md).


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
| `evolution/` | How the design got to where it is: one prompt and one image per pass. History, never specification. See below. |
| `*.pdf` | The five A2 review boards. Tracked. |
| `renders/` | 300 DPI PNG previews. **Gitignored** — regenerable, ~87 MB per character. |
| `source/*.pptx` | Intermediate build output. **Gitignored** — overwritten on every run. |

`shada/` is the worked reference for all five.

## Prompt packs

`Prompts.md` inlines the full Production Design Bible ruleset rather than
referencing it. This is deliberate — an image generator reading one file in
isolation must still receive every constraint. The canonical shared blocks live
in `../09-prompt-library/Global-Style-Block.md`; if you change a rule there, propagate
it to the character files.

A pack marked `status: scaffold` has correct shared style rules but incomplete
character content. Every `**NEEDS:**` marker is an unanswered design question.
Fill in `Character.md` before completing the pack.

## `evolution/` — how a design converged

**Established 2026-08-02, from Shada.** When a costume is worked out by
generating variants — change one thing, look at it, change the next — the passes
go in `evolution/`. Shada's is the worked example.

```
evolution/
  README.md                     the sequence, what each pass changed, what it cost
  01-cloth-vest.txt             the prompt for pass 1
  01-cloth-vest.png             what it produced
  02-green-khaki.txt
  02-green-khaki.png
  ...
  attachments/                  staged references, one folder per pass — gitignored
    01-cloth-vest/
      1-the-costume.png
      2-...
      MANIFEST.txt
```

Zero-padded sequence, a short slug naming **the variable that pass changed**, and
the `.txt` and `.png` sharing a stem. The final pass produces the image that gets
approved into `source/artwork/`, so the last `.png` here and the approved
reference are the same picture.

**`attachments/` is staged by `./tools/stage-evolution-attachments <character>`**
— the same service `short.py`'s `prompts/attach/` provides for the generated
prompts, so the operator drags one folder in rather than hunting three files
across three directories. It reads each prompt's own **URL block**, which is
therefore the source of truth: change the prompt and run it again.

**Run it after a fresh clone.** The folders are gitignored — copies of images that
are already in the repository — and unlike `prompts/attach/` there is no other
generator that would rebuild them.

**Three rules, and the first is the one that matters:**

1. **It is history, not specification, and nothing in it is a source of truth.**
   The design lives in `outfits.yaml`, `Character.md` and `Character-Lock.md`.
   **Never attach a SUPERSEDED evolution image to a generation prompt** — all but
   the last show a costume that no longer exists, and a superseded photograph is
   how a settled decision quietly comes undone.

   **The latest pass is the exception, and it is a real one.** Mid-sequence, the
   newest evolution image is often the only picture of the current design —
   `source/artwork/` still holds the last *approved* one, which by definition
   predates every correction since. Captain Jasu's pass 03 attaches pass 02 for
   exactly this reason: `source/artwork/` still showed ankle boots and a belt
   whistle, two decisions already reversed. Attaching it would have undone them.
2. **Variant prompts are hand-written and must never sit in `prompts/`.** That
   directory is generated: `split.py` and `turnarounds.py` delete `*.txt` there on
   every run, and a hand-written file among generated ones will either be lost or
   mistaken for current. `evolution/` is outside their reach.
3. **Write the README as you go, not afterwards.** What a pass *cost* — the thing
   it broke while fixing something else — is the part worth keeping, and it is
   the part nobody remembers a week later.

The folder is created when a character's first variant is run. There is no value
in empty ones.

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
