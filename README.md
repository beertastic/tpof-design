# TPOF Production Bible

Version-controlled pre-production design for **The Price of Freedom**, a Star
Wars fan film — and the first of three planned.

Everything here is text and images under Git. The documents are the source of
truth; images and boards are generated from them.

---

## The pipeline

```
Production Design Bible          the rules, for everything
        │
Faction guide                    what a group looks like
        │
Character.md + Character-Lock.md the character, and what may not change
        │
outfits.yaml                     each costume, and its non-negotiables
        │
   [ tools/prompt-splitter ]     ─────────────────────────────►  prompts/
        │                                                        paste-ready .txt
        │                                                        one per image
        │
   image generation              you + an image generator
        │
   source/artwork/*.png          the accepted images
        │
board-data.yaml                  which image goes where on which board
        │
   [ tools/board-generator ]     ─────────────────────────────►  A2 board PDFs
```

Two rules hold it together:

**Documents are the master.** Everything in `prompts/` is generated. Never edit a
generated file — change the source and re-run.

**Prompt files are self-contained.** Every rule needed is inlined, so a prompt
works when pasted into any tool, with no repository access. The cost is that
editing the Bible does **not** update existing packs — the canonical blocks live
in `09-prompt-library/` and must be propagated.

---

## Repository structure

| Path | Contents |
|---|---|
| `01-production-design/` | The Production Design Bible. Governs everything |
| `02-story/` | Script breakdown, scene index, planted elements for Films 2–3 |
| `03-characters/` | One directory per character |
| `04-factions/` | Shared group visual language, crew roster |
| `05-props/` | Hero and background props |
| `06-vehicles/` | Vehicles and craft |
| `07-locations/` | Sets, planets, environments |
| `08-species/` | Species and creatures |
| `09-prompt-library/` | Canonical prompt blocks and conventions |
| `10-assets/` | Reference images and exported sheets |
| `11-production-tracking/` | Status board and open questions |
| `tools/` | The two generators |

Each number is used exactly once.

### Inside a character folder

| File | Purpose |
|---|---|
| `Character.md` | The character. The build document |
| `Character-Lock.md` | Non-negotiables and the design-drift rejection list |
| `outfits.yaml` | Each costume, its `must_show` rules, handedness, approval state |
| `Prompts.md` | Image prompt pack — human-readable, the source for `prompts/` |
| `board-data.yaml` | Which images go where on which boards |
| `prompts/` | **Generated.** Paste-ready prompts, one per image |
| `prompts/turnarounds/` | **Generated.** Five per outfit |
| `source/artwork/` | Accepted images. Not reproducible — treat as precious |
| `reference/actor/` | Actor photographs. See `03-characters/CAST-REFERENCE.md` |
| `renders/` | **Gitignored.** 300 DPI board previews |

`03-characters/shada/` is the worked reference for all of it.

---

## Tools

```bash
source .venv/bin/activate

python tools/prompt-splitter/turnarounds.py shada   # costume turnarounds
python tools/prompt-splitter/split.py shada         # plates and mood images
python tools/board-generator/generate.py shada      # A2 board PDFs
```

All three accept `--all`. The board generator takes `--validate` (check without
building) and `--board <key>` (one board).

**No LibreOffice required.** Boards render straight to PDF with `reportlab`.

**Board count comes from the config**, not the tool. Shada has five; Baylan has
eight, including one turnaround sheet per outfit.

**The prompt generators check placement** on every run and warn if handedness is
undeclared or an asymmetric item has no side.

---

## Conventions worth reading before contributing

| Document | Covers |
|---|---|
| [`09-prompt-library/Capture-Block.md`](09-prompt-library/Capture-Block.md) | Anamorphic house style, photographic realism, defeating the synthetic look |
| [`09-prompt-library/Turnaround-Block.md`](09-prompt-library/Turnaround-Block.md) | Costume turnarounds — the primary deliverable |
| [`09-prompt-library/Handedness-And-Placement.md`](09-prompt-library/Handedness-And-Placement.md) | Which side everything sits on, and why it matters |
| [`03-characters/CAST-REFERENCE.md`](03-characters/CAST-REFERENCE.md) | Actor reference, and consent |
| [`03-characters/APPROVAL.md`](03-characters/APPROVAL.md) | Locking a costume and matching against it |
| [`02-story/Planted-Elements.md`](02-story/Planted-Elements.md) | What this film sets up for Films 2–3 |

---

## Priorities

**Costume turnarounds first.** Five images per outfit — front, left, right, back,
and a natural pose. They are what a costume department builds from. Mood images
are context; three or four per character is enough.

**Attach references, always.** Every prompt containing a person refuses to
generate without the approved costume and actor reference attached. Text alone
produces the wrong costume and the wrong face.

---

## What is committed

**Committed:** source documents, `outfits.yaml`, `board-data.yaml`,
`source/artwork/`, actor reference, and the board PDFs.

**Gitignored:** `renders/`, `.venv/`, generated previews. All reproducible in one
command; at ~100 MB per character per rebuild they would otherwise dominate the
repository, and Git keeps every version of a binary forever.

---

## Working method

Small commits straight to `main`, pushed as you go. There is a `git acp` alias
that adds, commits and pushes in one line:

```bash
git acp "design(shada): revise armour language"
```

Quote any message containing `()`, `!`, `"` or `&`.

Commit style: `docs(character):`, `design(costume):`, `prop(shada):`,
`chore(repo):`, `tools:`.

---

## Status

**The screenplay is the source of truth** — `02-story/scenes/`, currently v10 as a
Fountain file. The Filmanize breakdown that preceded it has been deleted; its
per-scene props, set dressings and costumes are preserved in
[`02-story/Scene-Elements.md`](02-story/Scene-Elements.md).

| | |
|---|---|
| **Shada** | Costume approved. **20/20 images, 5/5 boards.** Three images need replacing — see [`Shada-Image-TODO.md`](11-production-tracking/Shada-Image-TODO.md) |
| **Baylan** | Documented and locked. Four outfits, 32 images planned |
| **Shin** | Documented and locked. Three costume states |
| **Akk dog** | Asset built and rigged; documented |
| Everyone else | Placeholder |

Open questions live in
[`11-production-tracking/Open-Questions.md`](11-production-tracking/Open-Questions.md).
