---
title: "Shada — Finish List"
asset_id: "TRACK-SHADA-IMAGES"
updated: "2026-08-02"
---

# Shada — Finish List

**Status: DESIGN SETTLED AND LOCKED 2026-08-02.** Seven variant generations in
one session moved the vest from hide to cloth, the palette from brown to grey /
grey-green / khaki, and fixed the plate size, the tessellation, the shoulder cap
size and the wear. The front turnaround is **APPROVED** and is now the single
match target for everything else. Documents, `outfits.yaml` and all 21 prompts
are current; **the other twenty images are not.** Documents are the deliverable;
images are a guide.

**What the lock changed, in one place:**

| | Was | Is |
|---|---|---|
| Vest material | Scavenged hide | **Cloth** — heavy close-woven working fabric |
| Palette | Dark brown, charcoal | **Grey vest, grey-green trousers, taupe leather**; bronze thigh patch the one warm note |
| Plate density | "10–15 mm", nothing countable | **About twelve across a flank panel**, fifteen rows — with a floor: any finer is chain mail |
| Tessellation | "Never overlapped" | Said **positively** — flat in one plane, a thin dark line of backing between neighbours |
| Shoulder cap | "Loose, scavenged" | **A palm's width**, the point of the shoulder only |
| Wear | Not specified | **Plates missing** — 5–10 per flank panel, 3–5 on the cap — bent, chipped, badly repaired |
| Serpentine grain | Pressed into hide | **Woven into the cloth** |

Her documents, `outfits.yaml` and all 21 prompts are current and internally
consistent. The checker is clean and the boards validate.

---

## THE RUN LIST — start here

**17 images to regenerate.** Every one: **fresh chat**, paste the prompt whole,
attach `source/artwork/turn-working-front.png` and the two actor photographs, and
save the result into `source/artwork/` under the exact name on the prompt's
`Output file:` line. The boards look those up by name.

**Keep the files they have — nothing in them changed:** `species_strip`,
`expression_strip` (face and head only) and `knife` (locked as a prop reference).
`turn-working-front` is **done and approved — do not regenerate it.**

### 1. `scale_portrait` — first, and lock it as the MAKEUP reference

- [ ] Generate `scale_portrait.png` against the approved front
- [ ] Check: **reptilian slit pupils, clearly readable** — absent from the
      approved front, and recorded everywhere as the highest-value make-up item
- [ ] Check: **scale on the neck, jaw and collarbone** — nearly clear in the
      approved front
- [ ] Check: the pattern is **tonal, the same colour as her skin** — in the
      approved front it is noticeably warmer than her skin, which is wrong
- [ ] Tell the repo it is approved, so the other sixteen inherit it

**Why first:** the four turnaround views and every narrative frame show her face
and neck. Generate them before the make-up is locked and it drifts across all of
them — the same failure that cost this character her props, recorded below and
fixed in `8c5bea7`. *Lock the plates before the figures.* The face is the plates.

### 2. The four remaining turnarounds

Against the approved front **plus** the makeup portrait. Prompts in
`prompts/turnarounds-short/`.

- [ ] `turn-working-natural.png`
- [ ] `turn-working-left.png`
- [ ] `turn-working-right.png`
- [ ] `turn-working-back.png` — check it with the anatomy test below, not the
      frame-side test

### 3. Prop and material plates

- [ ] `blaster.png` — WESTAR-35, and the taupe leather
- [ ] `material-scale.png` — hexagons, tessellated flat, plates missing
- [ ] `material-cloth.png` — **changes most.** Grey woven cloth with the
      serpentine grain in the weave, not brown hide with it pressed in
- [ ] `material-leather.png` — taupe, not warm brown
- [ ] `material-hardware.png` — palette
- [ ] `utility.png`

### 4. Narrative frames

- [ ] `hero.png`
- [ ] `scale_figure.png`
- [ ] `camp_day.png`
- [ ] `forest.png` — **still owed a dusk frame**, and the palette change makes it
      more urgent. The old risk was a charcoal costume vanishing into shadow; the
      new one is grey-green and khaki vanishing into wet foliage
- [ ] `maintenance.png`
- [ ] `tone-collage.png`

### 5. Rebuild the sheets

```bash
cd /home/tris/tpof-design && source .venv/bin/activate
python tools/board-generator/generate.py shada --validate   # missing images, overlapping panels
python tools/board-generator/generate.py shada              # the 5 board PDFs
python tools/board-generator/generate.py shada --promo      # Shada-Promo.pdf — a SEPARATE command
```

**`--validate` will stay green throughout and that is not reassurance.** It
catches images that are *absent*, never images that are *stale*. Until the
seventeen are done the boards show one current front against sixteen pictures of
a costume that no longer exists, and only your eye catches that.

---

## BLOCKER — sixteen of the twenty-one prompts cannot be pasted

**Found 2026-08-02. Read before starting section 3 or 4 above.**

`short.py` only builds short prompts for the **five turnaround views**. The
sixteen numbered slots exist only as the long files in `prompts/`:

| Slots | Size | Against a ~4,000 character budget |
|---|---|---|
| `hero`, `camp_day`, `forest`, `maintenance`, `tone-collage` | ~65 KB | **16× over** |
| `scale_portrait`, `species_strip`, `expression_strip`, `material-scale` | ~18 KB | 4× over |
| the remaining plates | ~16 KB | 4× over |

So for those sixteen there is no deliberate prompt to paste — you would be
handing over the long file and letting the host compress it, **which is the exact
failure `Prompt-Reliability-TODO.md` exists to document.** The overflow is
discarded silently, from the middle, and nothing reports it.

**The fix is to extend `short.py` to cover the numbered slots.** The trim logic,
the rule handling and the reference block all already exist; what is missing is
the per-slot shot and scene text, which is what `VIEWS` does for turnarounds.
Roughly the same shape of change, one level up.

**Section 1 and section 2 are not blocked** — `scale_portrait` at 18 KB is
borderline but workable, and the five turnaround views have proper short prompts.
Do those first regardless.

**The images are deliberately not "finished", and that is the right call.** Every
generation lands differently, and the build will change again with budget and
what the supplier actually has. The prompts and the character documents are what
holds — an image is a guide to the intent, not the intent itself. Regenerate when
useful, approve what is close enough, and do not chase pixel agreement.

What the build actually needs is settled:

- **Five hard pieces** — right forearm gauntlet, left shoulder cap, left thigh
  patch, and a pair of unmatched flank panels over her ribs. *Revised three
  times on 2026-08-01; the third is current — see `Character-Lock.md` v4.0.*
- **The flank panels lace across her centre front**, worn over the vest, with a
  **strip of vest cloth visible in the gap** — collar, placket and centre-front
  seam still readable. That gap is what makes them brigandine and not a corset,
  and it must not close. No breastplate.
- **The gauntlet is a SOLID 3D-PRINTED SHELL** with a **plain worn plate face,
  not a hexagon field**, and a small cluster of **dim amber telltales at the
  wrist**. It is the only rigid piece on the costume and the only light on it.
- **The shoulder cap HANGS LOOSE** — separate plates on a hand-cut backing,
  sitting away from the body, daylight under its lower edge. Never a moulded
  pauldron.
- **Five different metals** — dull grey steel (gauntlet), blackened iron
  (shoulder cap), dark bronze (thigh), pale worn pewter (right flank), rust-red
  oxidised iron (left flank). **No brass and no verdigris.** The mismatch is the
  point — and it lives *between* the pieces: **within one panel the metal is all
  one metal.**
- **The vest hide carries a faint serpentine grain** — in the material, tonal,
  visible only in raking light. Not the scale armour, and never a printed
  snakeskin.
- **Plates 10–15 mm**, regular hexagons, tessellated edge to edge, never
  overlapped, each carrying a raised snake swirl that varies plate to plate.
- **Roughly 440 loose plates.** The printed gauntlet permanently removed ~150,
  and the restored flank panels put ~220 back. See `Costume-Build-Method.md` —
  still the largest hidden labour item in the costume, and the flank panels are
  half of it. Pattern them first.
- **WESTAR-35** on her right side; combat knife on her left hip.
- **Skin:** a faint scale pattern like a tattoo, ancestry tens of thousands of
  years back. Reptilian contact lenses are the highest-value make-up item.

Open, non-blocking: photograph the printed WESTAR-35 and add it under
`references:` in `outfits.yaml` — the entry is there, commented. And run a noise
test on the first finished patch; she is an infiltrator and 440 hard plates is
not obviously a quiet garment. The loose shoulder cap swings, and the flank
panels sit over her ribs, where she breathes.

---

## Before you run anything, read this

**Only about 11% of Shada's written specification currently reaches the image
generator.** Her `must_show` rules total 18,061 characters; the short prompt that
gets pasted carries 1,988 of them, and the loss is silent. Three of the four
recorded failures were rules that existed and were correct but were trimmed away
before the generator saw them.

**Partly addressed 2026-08-02.** The proportion is unchanged — the rules are the
same length — but seven of the fourteen were re-ordered so the sentence that
does the work comes first. `trim()` always keeps the opening sentence and then
the first hard negation, so what survives is now chosen rather than accidental.
All fourteen rules land whole in the short prompt, with no ellipsis.

The fix list is [`Prompt-Reliability-TODO.md`](Prompt-Reliability-TODO.md).
Until item 2 there is done, expect to check generated images against the
**documents**, not against the prompt — the prompt is a lossy summary of them.

---

## Start here

```bash
cd /home/tris/tpof-design
source .venv/bin/activate
python tools/prompt-splitter/split.py shada
python tools/prompt-splitter/turnarounds.py shada
python tools/prompt-splitter/short.py shada
```

**Run all three, every time.** The prompts have changed since the last images
were made, and two images have already been lost to stale copies.

**The third line is the one that matters and it was missing from this list until
2026-08-02.** `turnarounds.py` writes the long prompts; `short.py` writes
`turnarounds-short/`, which is what you actually paste. Running the first two
alone leaves the short prompts stale, and nothing says so — the header even
carries a version stamp from the run that made the long file.

Then open a **fresh** ChatGPT conversation — genuinely fresh, not a continuation
— and attach the references *before* pasting anything. A chat that has already
drawn another character in this production will carry that costume over; it has
happened once and it cost a full generation.

- `03-characters/shada/reference/actor/dasha-svistunenko-heashot.jpg` — actor
- `03-characters/shada/source/artwork/material-scale.png` — the plates

**There is ONE approved costume reference, as of 2026-08-02:**

| File | Use it for | Ignore in it |
|---|---|---|
| `source/artwork/turn-working-front.png` | **Everything.** The whole costume: the grey cloth vest with its stand collar and centre-front placket, the palette, the plate size, the tessellation, the wear, the shoulder cap size, the flank panels laced across the front, the thigh patch, the belts, the trousers, the boots, and which side every piece is on | **The face**, which comes from the actor photographs |

*Why there is only one.* There were two DIRECTION photographs with different
scopes, and the generation of 2026-08-02 shows why that failed: with two
full-figure references competing over the same garment, the vest lost its stand
collar to a crossover wrap and a full layered skirt appeared over the trousers.
The written rules cannot win that fight. **One costume reference, and it is the
approved front.**

`costume-front-v2.png`, `flank-panels.png` and `costume-direction-front.png` are
kept on disk as history and **must not be attached to anything.** Every fault
they carried has been designed out — the smooth shoulder plate, the leather
forearm wrap, the oversized plates, the brown palette, the hide vest.

**It is not a face reference, and saying so is not optional.** A generation on
2026-08-01 came back in a perfect costume on the wrong woman because the costume
reference carried no scope. Any full-figure photograph attached to a prompt must
state what it is *not* for.

---

## The order to work in

**1. `turn-working-front` is DONE and APPROVED.** Do not regenerate it. It is the
image every other view matches against, and regenerating it would move the target
under twenty images that have not been made yet.

**2. `scale_portrait` next, and lock it as the MAKEUP reference.**

**The costume has a lock. The makeup does not** — and this is the same gap that
cost this character her props, recorded below and fixed in `8c5bea7`. *Lock the
plates before the figures.* The face is the plates, here.

Two things the approved front does not carry, both noticed after it was approved:

- **The reptilian contact lenses.** Her eyes are plain blue in it. No slit pupil.
  This is recorded everywhere as the single highest-value item in her make-up.
- **The scale pattern on her neck**, which is nearly clear, while the pattern on
  her arms is **stronger and warmer in colour than the specification allows** —
  it should be *tonal*, the same colour as her skin, readable only in raking
  light. In the approved front it is a distinctly warmer tone than her skin.

**None of that is a reason to regenerate the front**, and doing so would be a
mistake. A slit pupil is a handful of pixels at full-figure scale and cannot
carry there; the front took seven passes to converge on silhouette, palette,
plate size, cap size, tessellation, wear and sides, and re-rolling it to chase
something that will not read risks all of it.

`scale_portrait` is a close portrait and it is the right instrument. Generate it
against the approved front, get the lenses and the neck right, and **approve it
as a second, scoped reference**:

| Reference | Scoped to | Not for |
|---|---|---|
| `turn-working-front.png` | The costume — everything below the collar | The face, the eyes, the neck |
| `scale_portrait.png` | **The makeup** — the slit pupils, the strength and colour of the scale pattern, and where it sits on the neck, jaw and collarbone | The costume |

Two references with **stated, non-overlapping scopes** is not the failure that
cost five generations. That failure was two references competing over *the same
garment*. Scope is what makes the difference, and it has to be written down.

**3. The other four turnaround views** — `natural`, `left`, `right`, `back` —
matched against the approved front, with the makeup portrait attached. This is
the method Captain Jasu's set proved: generate each view *against the approved
image* rather than from the prompt alone. Her five pass the mirror check; every
character generated view-by-view from prompts alone got five near-misses.

**4. `blaster` and `material-scale`** — the two plates that define the changed
objects. Once approved these become prop references in their own right.

**5. Everything else**, with the approved front and the plate references attached.

**6. `forest` is still owed a dusk frame — and the question has changed.** It came
back as a daylight camp, so the slot's question is still open and it now overlaps
`camp_day`. **The palette change on 2026-08-02 makes this more urgent, not less.**
The old risk was that a charcoal costume would vanish into shadow; the new risk is
that a grey-green and khaki one vanishes into wet foliage. For an infiltrator that
is arguably correct in-world and bad for the camera, and only this frame settles
it. If it returns a six-panel collage again, that is the prompt length talking:
say *"one frame,
not a contact sheet"* when you paste it.

---

## How to check a back view

The old version of this file had a table here demanding that each item stay on
the **same side of the frame** in front and back views. That was wrong, and it
would fail a correct image.

When she turns around, her right side moves from the viewer's left to the
viewer's right. **The frame sides swap. What never changes is which of *her*
sides carries the item.** In a back view:

| Element | Her side | Back view: viewer's |
|---|---|---|
| Printed gauntlet | right forearm | **right** |
| Loose shoulder cap | left shoulder | **left** |
| Flank panels | both sides | **both** — but still unmatched |
| Thigh patch | left thigh | **left** |
| Blaster | right thigh | **right** |
| Knife | left hip | **left** |

Note that a horizontal flip of the front view *also* swaps the frame sides, so
frame position cannot catch a mirror. What catches it is anatomy: a real back
view shows shoulder blades, the back seams of the vest, rear pockets and the
back of her head. A mirrored front shows her face and the front closure.

The `turn-working-back` in the repository passed both tests, but predates the
2026-08-01 revision and shows the superseded build.

---

## Then rebuild

```bash
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
```

`--validate` catches missing images **and overlapping panels**. Both clean before
building.

---

## What still needs regenerating

**The 2026-08-02 lock invalidated more than the previous revisions did**, because
the palette and the vest material are visible in every frame that shows the
costume at all — not just the ones showing armour detail.

**Leave alone — nothing in them changed:**

`species_strip`, `expression_strip`. Both are face and head only, both are
particularly good, and neither shows enough costume to be affected. `knife` is
also unaffected and is already locked as a prop reference.

**Regenerate — the costume in them no longer exists:**

| Image | Why |
|---|---|
| `turn-working-natural`, `left`, `right`, `back` | The front is approved; these four must be matched against it. **Do not regenerate the front** |
| `hero`, `camp_day`, `forest`, `maintenance`, `scale_figure` | Full figure — cloth vest, grey palette, plate size, cap size, wear |
| `scale_portrait` | Shows the collar, the shoulder and the vest cloth |
| `material-cloth` | It is now a grey woven cloth with the serpentine grain in the weave, not a brown hide with it pressed in |
| `material-leather` | Taupe, not warm brown |
| `material-scale` | Hexagons with a pressed stamp, tessellated flat, with plates missing |
| `material-hardware` | Palette |
| `blaster`, `utility` | The WESTAR-35, and the taupe leather |
| `tone-collage` | Everything above |

**The front turnaround is APPROVED in `outfits.yaml`.** Every image above matches
against it.

`tone-collage` is slot 16, the new **share sheet** — one image, six panels, for
sending to people on a phone. It is not on any board and is never used as a
costume reference. Every character now has this slot.

---

## Watch for

The failures that keep recurring:

- **Plates that shingle.** They butt edge to edge in one flat plane with a thin
  dark line of backing between them — no plate rides over another and none casts
  a shadow onto its neighbour. "Never overlapped" was in the spec for days and
  never worked; what works is describing what tessellation *looks like*.
- **Chain mail.** The opposite over-correction, and it arrived within one
  generation of fixing the size. Twelve plates across a flank panel is the
  **floor** as well as the target — any finer and the plates lose their edges.
- **A leather vest.** It is cloth now, and it creases where the hard pieces bear
  on it. If it reads as hide, the base layer has become armour.
- **A brown costume.** The leather especially drifts warm on nearly every
  generation, and warm leather drags the whole palette back to where it started.
- **Armour that looks laid out.** Plates are missing, bent and badly repaired.
- **A shoulder cap creeping down the arm or in toward the collarbone.** It is a
  palm's width, on the point of the shoulder. This is how a yoke returns under
  another name.
- **The thigh patch as a solid patch.** It is a field of the same small plates.
- **A skirt, tabard or apron over the trousers.** New on 2026-08-02, and the
  largest silhouette failure so far. The trousers were the last sentence of the
  boots rule and the trim cut them from every short prompt, so nothing described
  her lower half at all. Now the first sentence of that rule.
- **The gauntlet and the shoulder cap swapped over.** Her right forearm, her
  left shoulder, always. On 2026-08-02 they exchanged sides while the blaster
  stayed correct, so it was not a mirrored image — the two pieces simply read as
  interchangeable. They are on opposite sides on purpose.
- **A crossover or V-neck vest.** Stand collar and a concealed placket straight
  down the centre front. The collar sentence used to be trimmed away.
- **Another character's costume entirely.** Captain Jasu's horns, shoulder yoke,
  quilted sleeves and matched bracers arrived on 2026-08-02 from a shared
  conversation. **Use a fresh chat for every character** — the prohibitions in
  the prompt are a backstop, not the fix.
- **A yoke, or panels that climb onto the chest.** The scale panels are
  lower-torso only: ribs, waist and hip, never above the armpit.
- **The wrong face.** The single most expensive failure so far. The costume
  photographs are not face references; the actor photographs are.
- **A laced or leather gauntlet.** It is a solid printed shell now. One
  gauntlet, her right, and her left forearm is bare.
- **Flank panels that close up in the middle.** The strip of vest cloth in the
  lacing gap is what stops them reading as a corset.
- **A panel speckled with four metals.** One panel, one alloy. The mismatch is
  between the five pieces.
- **A glowing gauntlet.** Two dim amber pinpoints at the wrist. No lit seams, no
  edge lighting, nothing spilling onto skin.
- **A shoulder cap moulded to the shoulder.** It hangs loose and light gets under
  it.
- **Shoulder caps on both shoulders.** One cap, her left — the opposite side to
  the gauntlet. This is the rule doing the most work in the design: symmetry
  quietly turns scavenged mismatch into a costume somebody made for her.
- **A bulky silhouette.** Close-fitting, cut to the figure.
- **Any interior except the Sabacc hold.** Forest, clearing or camp — with the single exception of slot 2, Scene 10, which moved inside the ship on 2026-08-01. Anywhere else, a wall or ceiling is wrong.
- **A modern coil zip.** Industrial hardware, or hooks and lacing. Still slipping
  through on nearly every frame — the one recurring fault not yet beaten.
- **The blaster on her left.** It is on her right thigh; only the knife is on her
  left.
- **Pieces in the same metal.** Steel gauntlet, iron cap, bronze thigh, pewter
  and rust-red flanks. They drift toward matching brass, and there is no brass on
  this costume.
- **Metal on her chest.** The flank panels sit at the SIDES, over the ribs. Her
  sternum, her centre front and the middle of her back stay plain cloth — a chest
  patch, bib, pendant or breastplate is still wrong.
- **Printed snakeskin on the vest.** The grain is in the hide, faint and
  irregular, or it is not there at all.

Two or more together almost always means **the references were not attached**.

---

## The gap this character exposed — props have no lock. **Built 2026-07-31.**

**The costume had an approved reference image. The props did not**, so the
blaster, the knife and the scale patches were described in words and redrawn from
scratch every time. Words cannot hold a silhouette; only an image can.

Fixed in commit `8c5bea7`. `outfits.yaml` now carries a `references:` list
alongside `approved:`, and both `split.py` and `turnarounds.py` emit an operator
line naming every plate to attach. A declared reference that does not exist
raises a warning, since the prompt would otherwise tell the operator to attach a
missing file.

Currently locked: `material-scale.png` and `knife.png`.

**The blaster is deliberately not locked.** `blaster.png` is a decent plate but
it does not match the printed prop — the physical WESTAR-35 has brass panels let
into the slide, a blue panel and a black textured grip. Attaching it would lock
every image to a gun nobody is building. The entry sits commented in
`outfits.yaml`, pointing at `reference/props/westar-35.jpg`, to be uncommented
once the prop is photographed.

**The general rule, which has now come up twice: for anything physically built,
the reference is a photograph of the build, not a render.**

Baylan inherits this for free — but he needs his own plates locked before his
figures, not after. He carries a blaster, a holster and a rifle: the same drift,
multiplied across every view.

---

## After Shada

Baylan is next.

**Done 2026-08-01: he is `handedness: right`, and his costume carries
`must_show:`.** The placement checker is silent on him. Blaster on his right hip,
rifle slung to fall to his right hand, pouches on his left off side. Recorded in
`Character.md`, `Character-Lock.md` and `outfits.yaml`.

**He was also collapsed to ONE costume that day** — the robe is a removable layer,
and the separate Scene 12 Jedi build is dropped. Five turnarounds, not twenty.

Still owed before those five turnarounds:

- **Lock his plates first, then his figures.** This is the order correction from
  `8c5bea7` and it matters more for him than it did for Shada: he carries a
  blaster, a holster and a rifle, and words will not hold three silhouettes
  across eighteen images. Generate `blaster`, `crystal` and `utility`,
  approve them, add them to `references:` in `outfits.yaml`, and only then start
  the figures with all of them attached.
- **A `promo-data.yaml`.** Copy Shada's, keep the structure, replace the copy —
  see `tools/board-generator/README.md`.

**Shin is now the character with the placement checker warning against her** — no
`handedness:`, and no `must_show:` on any of her three states. Same job, same
half hour.
