# TPOF Production Bible

Version-controlled pre-production design for **The Price of Freedom**, a Star
Wars fan film — and the first of three planned.

Everything here is text and images under Git. The documents are the source of
truth; images and boards are generated from them.

---

## The pipeline

```
The screenplay                   02-story/scenes/*.fountain — SOURCE OF TRUTH
        │                        where a document disagrees, the script wins
        │
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
| `02-story/` | **The screenplay**, scene index, scene elements, blocking, planted elements for Films 2–3 |
| `03-characters/` | One directory per character |
| `04-factions/` | Shared group visual language, crew roster |
| `05-props/` | Hero and background props |
| `06-vehicles/` | Vehicles and craft |
| `07-locations/` | Sets, planets, environments |
| `08-species/` | Species and creatures |
| `09-prompt-library/` | Canonical prompt blocks and conventions |
| `10-assets/` | Reference images and exported sheets |
| `11-production-tracking/` | Status board and open questions |
| `tools/` | The three generators — prompts, boards, screenplay |

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
| `prompts/turnarounds/` | **Generated.** Five per outfit. The full specification — too long to generate from |
| `prompts/turnarounds-short/` | **Generated.** The same five, under 4,000 characters. **These are what you paste** |
| `source/artwork/` | Accepted images. Not reproducible — treat as precious |
| `reference/actor/` | Actor photographs. See `03-characters/CAST-REFERENCE.md` |
| `renders/` | **Gitignored.** 300 DPI board previews |

`03-characters/shada/` is the worked reference for all of it.

---

## Tools

```bash
source .venv/bin/activate

python tools/prompt-splitter/turnarounds.py shada   # costume turnarounds — the spec
python tools/prompt-splitter/short.py shada         # the same, cut to fit a generator
python tools/prompt-splitter/split.py shada         # plates and mood images
python tools/board-generator/generate.py shada      # A2 board PDFs
python tools/script-convert/render.py               # screenplay -> PDF
python tools/script-convert/render.py --format fdx  # screenplay -> Final Draft
```

The first four accept `--all`.

**Paste the short ones.** Image models accept about 4,000 characters; the full
turnaround prompts are 28,000. Anything past the limit is compressed by the host
before the generator sees it — which is why identical files gave different
costumes. `short.py` keeps every non-negotiable, trimmed at a sentence boundary,
and fits. The long files remain the specification and the thing humans read. The board generator takes `--validate` (check
without building) and `--board <key>` (one board).

**The screenplay is plain text.** It lives as Fountain under `02-story/scenes/`
and renders on demand — see [`tools/script-convert/README.md`](tools/script-convert/README.md).
Rendered PDFs and FDX are gitignored.

**No LibreOffice required.** Boards render straight to PDF with `reportlab`.

**Board count comes from the config**, not the tool. Shada 5, Baylan 5, Shin 7,
Mercenary Kit 4 — one turnaround sheet per costume, plus the supporting boards.

**The prompt generators check placement** on every run and warn if handedness is
undeclared or an asymmetric item has no side.

---

## Conventions worth reading before contributing

| Document | Covers |
|---|---|
| [`AGENTS.md`](AGENTS.md) | **Instructions for AI agents with repo access.** The commands, and the checks they must run first |
| [`09-prompt-library/Generating-From-A-Connected-Repo.md`](09-prompt-library/Generating-From-A-Connected-Repo.md) | The reasoning behind `AGENTS.md`, for humans |
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

**One exception: the front turnaround.** It is generated without a costume
reference because it is the image that *creates* the reference. Get it right
before anything else — an error there propagates into every other view.

---

## What is committed

**Committed:** source documents, `outfits.yaml`, `board-data.yaml`,
`source/artwork/`, actor reference, and the board PDFs.

**Gitignored:** `renders/`, `.venv/`, generated previews. All reproducible in one
command; at ~100 MB per character per rebuild they would otherwise dominate the
repository, and Git keeps every version of a binary forever.

---

## Working method

**Install the hooks once, per clone:**

```bash
git config core.hooksPath tools/hooks
```

That stamps [`REPO-STATE.md`](REPO-STATE.md) on every commit, which is how a
connected AI agent can tell whether it is reading current files or cached ones.
See [`AGENTS.md`](AGENTS.md).

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

| Character | State |
|---|---|
| **Shada** | **Design closed.** 21 images, 5 boards. Several superseded by the hexagonal-plate and WESTAR-35 revisions — see [`Shada-Image-TODO.md`](11-production-tracking/Shada-Image-TODO.md) |
| **Baylan** | Locked. **One costume**, removable robe. `handedness: right`, checker clean. 5 turnarounds + 13 plates, **none generated** |
| **Mercenary Kit** | **Four people — Merc 1 to 4**, one build each. 20 turnarounds + 13 plates, none generated. Merc 1 is the Wookiee and gets no generated turnaround by decision |
| **Shin** | Locked, three costume states. **BLOCKED** — no `handedness:` or `must_show:`, the last checker warning in the project |
| **Akk dog** | Asset built and rigged; documented |
| Nyx, Captain Jasu, Krellis, Reya Fenn, Yaslo Bis, Jeyin, Vala | Documented to varying depth. **Every death is now written** — see [`Deaths-And-Effects.md`](11-production-tracking/Deaths-And-Effects.md) |
| Palpatine | Glimpsed only. Reference note, by decision |

**The mercenary crew is ten people**, each with a costume build, a group and a
scene they die in — [`Crew-Roster.md`](04-factions/mercenaries/Crew-Roster.md).

Where the design documents and the screenplay disagree is tracked in
[`Script-v9-Reconciliation.md`](11-production-tracking/Script-v9-Reconciliation.md)
— 7 of 9 closed.

Open questions live in
[`11-production-tracking/Open-Questions.md`](11-production-tracking/Open-Questions.md).
