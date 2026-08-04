---
title: "Character Build Recipe"
asset_id: "PROC-CHARACTER-BUILD"
updated: "2026-08-03"
---

# Character Build Recipe

**From a paragraph of backstory to a costume somebody can actually build, in the
order that works.** [`shada/`](shada/) is the worked example of every step —
twenty-one images, six boards, a promo sheet, a build guide and two build sheets,
with a documented failure behind every rule in her pack. When something here is
unclear, go and look at what she actually has.

**Nine phases. You supply three things and phase 0 turns them into files; the
rest is procedure.** Jasu and Shada have been through all nine and are the
templates — every other character follows them.

**Read [`../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md`](../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md)
before writing a single rule.** It is eight lessons that each cost at least one
wasted generation.

---

## The order matters, and this is the order

Doing these out of sequence is how days get spent. Each phase produces the input
the next one needs.

### Phase 0 — The intake. Three things, and nothing else is needed to start

**This is the whole ask of whoever is commissioning the character.** Everything
downstream is derived from it.

| | What to give | Why it is load-bearing |
|---|---|---|
| **1** | **Description and backstory** — who they are, what they do in the story, what they are afraid of | Becomes `Character.md`. Story function is what stops a costume becoming decoration |
| **2** | **Casting facts** — age, **height in cm**, build, species, and **handedness** | Height sets every scale landmark and comparison. Handedness places *every* weapon, pouch and tool. Both are cheap to state now and expensive to change later |
| **3** | **General clothing ideas** — materials, silhouette, palette, what they must NOT look like | Becomes the costume language. Vague is fine; the negations matter more than the positives |

```bash
./tools/new-character <slug> --name "Full Name" --height 172 --hand right
```

That scaffolds the folder, both templates, a stub `outfits.yaml` carrying the
full schema, and the per-character TODO. **It writes no design** — every field
that needs a decision is left as a `NEEDS:` marker, because a plausible
auto-filled answer is worse than a blank one.

> **HEIGHT AND HANDEDNESS ARE NOT ADMIN.** Captain Jasu was re-cast by 5 cm and
> it took a sweep of fifty-four references, one of which was missed and reached
> Drive twice inside a printed build guide. State them once, correctly, in
> `outfits.yaml` — which is the only file the tooling reads.

### Phase 1 — Documents

| File | What it is |
|---|---|
| `Character.md` | Who they are, story function, design reasoning. Start from [`Character-Template.md`](Character-Template.md) |
| `Character-Lock.md` | The locked design, versioned. Created when the design stops moving |
| `outfits.yaml` | **The master.** Height, handedness, `must_show` rules, `references:`, `approved:` |
| `Prompts.md` | The image prompt pack. Starts `status: scaffold` — **`short.py` writes nothing until this is `ready`** |

**`outfits.yaml` is the only file the tooling reads.** Prose in `Character.md`
reaches no generator. If a rule matters to an image, it lives in `must_show`.

### Phase 2 — The face and the props, before any figure

Put real photographs in `reference/` first:

```
reference/actor/      the performer — the ONLY source for a likeness
reference/props/      photographs of anything physically built
reference/concept/    production drawings
reference/approved/   approved references
reference/alternates/ superseded, kept as history, NEVER attached
```

**Lock the plates before the figures.** A character carrying a blaster, a holster
and a rifle has three silhouettes that words will not hold across eighteen
images. Generate those plates, approve them, add them to `references:` in
`outfits.yaml`, and only then start the figures with all of them attached.

**For anything physically built, the reference is a photograph of the build, not
a render.** A stock reference is an acceptable interim if it is scoped hard — see
Shada's WESTAR-35, which carried two known faults and only the scope line stopped
it teaching them.

### Phase 3 — The approved front

Generate the front turnaround, iterate until it is right, then **approve it** —
see [`APPROVAL.md`](APPROVAL.md). Everything after this matches against one
image instead of being re-derived from a paragraph.

**One costume reference. Never two.** Two full-figure references competing over
one garment cost five generations; the written rules cannot win that fight.

If the design moves while you converge, record the passes in `evolution/` — see
[`README.md`](README.md#evolution--how-a-design-converged). History, never
specification.

### Phase 4 — The remaining four turnarounds

`natural`, `left`, `right`, `back`, matched against the approved front. Check:

- **The far side stays hidden.** In `left`, anything on their right is behind
  them and must not appear. An empty limb is the rule being obeyed.
- **`back` is a rotation, not a mirror.** Judge by anatomy — shoulder blades,
  back seams, rear pockets. A mirrored front shows the face and the closure.

### Phase 5 — A make-up lock, if the face carries anything

If the character has make-up, prosthetics, scarring or a species treatment, the
approved front will not carry it — a slit pupil is two or three pixels at
full-figure scale. **Generate a close portrait as a second, scoped reference**
(`THE MAKE-UP — NOT THE COSTUME`), and then do not chase that detail in any
full-length frame.

### Phase 6 — The plates, then the strips, then the frames

In this order, because each is a reference for what follows:

1. **Material and prop plates** — scale, leather, cloth, hardware, weapons, kit
2. **Study strips** — species, expressions
3. **Narrative frames** — hero, environment, at-work, tone collage

**Re-stage after any plate that is an attached reference.** The staged copies in
`prompts/attach/` are made at regen time; a new plate on disk does not reach the
prompts until `./tools/regen <character>` runs again.

### Phase 7 — Boards

| File | Produces |
|---|---|
| `board-data.yaml` | The six A2 boards |
| `promo-data.yaml` | The A4 share sheet |

```bash
source .venv/bin/activate
python tools/board-generator/generate.py <character> --validate
python tools/board-generator/generate.py <character>
python tools/board-generator/generate.py <character> --promo
```

**`--promo` is a separate command** and is the one that gets forgotten.
**`--validate` going green proves only that files exist** — it cannot see a stale
image. Check timestamps.

### Phase 8 — The build guide and the two build sheets

**Boards are not the end. A costume nobody can shop for is not finished,
however good the plates are** — and the image manifest counts pictures, which
makes that easy to miss.

**Fill in `components:` in `outfits.yaml` first.** Every piece of the costume,
each with a `route:` of `printed`, `made` or `bought`. The full schema — including
the `build:`, `shop:` and `images:` blocks the sheets are made of — is in
[`../11-production-tracking/Costume-Build-Method.md`](../11-production-tracking/Costume-Build-Method.md#the-components-schema).

Then three files, in this order, and **nothing is written from the pictures at
any stage:**

```bash
./tools/build-guide-pdf <character>     # _build_guide.md  ->  _build_guide.pdf
./tools/build-lists     <character>     # _print_list.pdf and _shopping_list.pdf
```

| Sheet | Covers | Read at |
|---|---|---|
| `_build_guide.pdf` | the whole costume in prose | the desk, first |
| `_print_list.pdf` | `route: printed` and `route: made` | the bench |
| `_shopping_list.pdf` | `route: bought` | in the shop, on paper |

**Both sheets carry cropped pictures**, named per component in `images:`, so the
shopping list is enough on its own on a charity-shop rail. **Where a plate is
authoritative for one thing and wrong about others, give it a `scope:`** — it
prints in red under the picture. A picture with no caveat teaches everything in
it equally, which is how a department builds from a superseded image.

**Budget is a cap on bought items only** — filament, paint, leather, dye and any
contact lenses are materials and are counted separately. Jasu came to £36–87 and
Shada to £35–83 against £100.

**No supplier links, ever.** Search terms, filters and refusals go in `shop:`;
listings rot and live in Drive. Decided 2026-08-01 and upheld since.

### Phase 9 — Publish

```bash
./tools/publish-to-drive              # dry run — always do this first
./tools/publish-to-drive --check      # what differs, by filename
./tools/publish-to-drive --go         # the repository wins
```

**One flat folder per character**, no subfolders, because the costume department
browses by arrowing through images. The `_` prefix sorts the guide and the two
sheets above the plates.

**Add the character to `drive_folder()` in the script.** The Drive folder names
are hand-made and are *not* the repo slugs — a character missing from that
mapping is an error, deliberately, because a wrong guess silently creates a
second folder for the same person.

**`--check` after `--go`.** It is the only proof Drive matches, and it costs
seconds.

---

## The twenty-one images

Five turnarounds plus sixteen numbered slots. Shada's set is the reference.

| | Slot | Notes |
|---|---|---|
| **Turnarounds** | `front` `natural` `left` `right` `back` | `front` is approved and never regenerated |
| **Narrative** | `01-hero` `02-scale_figure` `03-camp_day` `04-forest` `11-maintenance` | Take the CHECK block and the Capture and Cinematic Framing blocks |
| **Study** | `05-scale_portrait` `06-species_strip` `07-expression_strip` | Close work. **Take no costume rules — see the warning below** |
| **Props** | `08-knife` `09-blaster` `10-utility` | Flat documentation light |
| **Materials** | `12-material-scale` `13-material-leather` `14-material-cloth` `15-material-hardware` | Name a VALUE, not just a hue |
| **Share** | `16-tone-collage` | The only slot where six panels is correct. On no board |

Not every character needs all sixteen. A character with no species treatment does
not need `species_strip`; one with two props does not need three prop plates.
**The turnarounds and the make-up board are not optional.**

## The six boards

| Board | Carries |
|---|---|
| 01 Turnaround | The five views |
| 02 Costume construction | Front, back, natural, materials, scale figure |
| 03 Weapons & equipment | Prop plates and an at-work frame |
| 04 Performance & movement | Narrative frames |
| 05 **Make-up & continuity** | Portrait, study strips, and the make-up rules |
| 06 Materials & colour | Material plates and the palette |

**Every character needs board 05**, not only the ones with a species. A human
face still needs hair, dirt state per scene, scarring and continuity across a
shoot. Copy the commented block from Shada's `board-data.yaml`.

---

## The six things that will bite you

**1. `Prompts.md` left as `scaffold`.** `short.py` writes no slot prompts for a
scaffold, silently. This is the single most common reason a character produces
nothing.

**2. Pasting the long prompt.** Files in `prompts/` are the specification, 5–8×
over any working budget, and the overflow is dropped silently from the middle.
**Paste from `prompts/slots-short/`.** The version line says `(short)`. Every
long file now opens with a banner.

**3. `pin:` does not reach a slot that takes no rules.** `must_show` is emitted
only for costume slots. A pinned rule — the strongest protection in the file —
never reaches the study strips or the material plates. If a rule matters to those
slots, write it into their shot text as well. See fixes 8 and 9 in
[`../11-production-tracking/Prompt-Reliability-TODO.md`](../11-production-tracking/Prompt-Reliability-TODO.md).

**4. The trim keeps the opening sentence and the first hard negation.** Everything
else can vanish at any cap. Four documented failures were correct rules cut before
the generator saw them. **Put the load-bearing clause first.**

**5. Hand-written attachment lists.** Five different lists existed in this
repository on one day and none matched the prompt. **Attach everything in
`prompts/attach/<outfit>/` except `MANIFEST.txt`** — that folder is generated
from the same list the prompt declares, so it cannot drift. The manifest names
every exception.

**6. An `outfits.yaml` with no `components:` block.** `build-lists` skips the
character and says so in one line that is easy to scroll past, and you get boards
with no build sheets — a character that looks finished and cannot be built.
Baylan, Shin and the mercenary kit are all in this state today.

---

## Operator procedure, every single image

Full version in
[`../09-prompt-library/Character-Image-Checklist.md`](../09-prompt-library/Character-Image-Checklist.md).

1. **A genuinely fresh chat.** A chat that has drawn another character carries
   that costume over.
2. **Reasoning tier High.** It does not persist — check it every time.
3. **Attach the images FIRST**, before pasting anything.
4. **Paste the whole short prompt** as the first message. Nothing before it.
5. **Check the reply says it used the ATTACHMENTS.** URLs, or silence, means the
   references did not arrive — discard it.
6. **Save under the exact `Output file:` name.** The boards look images up by
   name.

**To correct a generation: re-paste the WHOLE file with a correction on top, and
name what to KEEP as well as what to change.** Never "same again but…" — that
works from its own last output and compounds. Every correction that named a
single fault fixed it and traded away something else.

---

## Keep a per-character TODO

`11-production-tracking/<Name>-Image-TODO.md`, following
[`Shada-Image-TODO.md`](../11-production-tracking/Shada-Image-TODO.md).

**One run list, and it is the only place that carries the order.** Shada's had
two numbered lists until they drifted apart. Record what each failed generation
taught, not just that it failed — that record is what made the rules in the
prompt library, and it is worth more than the images.
