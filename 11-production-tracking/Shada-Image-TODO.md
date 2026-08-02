---
title: "Shada — Finish List"
asset_id: "TRACK-SHADA-IMAGES"
updated: "2026-08-01"
---

# Shada — Finish List

**Status: DESIGN REOPENED 2026-08-01** by a costume reference supplied by the
Production Designer. Documents, `outfits.yaml` and all 21 prompts are current
with the revision; **the images are not.** Documents are the deliverable; images
are a guide.

Her documents, `outfits.yaml` and all 21 prompts are current and internally
consistent. The checker is clean and the boards validate.

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

**There is no APPROVED costume reference yet, but there are two accepted
DIRECTION references**, both attached automatically by every generated prompt.
**They swapped roles on 2026-08-02** — check you are reading the current table:

| File | Use it for | Ignore in it |
|---|---|---|
| `reference/approved/flank-panels.png` | **The costume.** Silhouette, the vest with its stand collar and centre-front placket, the flank panels laced across the front with vest cloth in the gap, the thigh patch, the two belts, the close-fitting trousers with nothing over them, the boots | **The face.** Its shoulder piece (a smooth solid plate — should be scale), its forearm (a leather wrap — should be the printed gauntlet), and its plate size (twice too big, and it mixes metals inside one panel) |
| `reference/approved/costume-front-v2.png` | **Three things only** — the loose scale shoulder cap, the printed gauntlet with its amber wrist telltales, and how big a plate is | **The face.** Its vest, its boots, and the fact that it has no flank panels |

*Why they swapped.* They were the other way round, and the generation of
2026-08-02 shows why that failed. With the fuller photograph named as "the
costume" and the better one scoped to one thing, the vest lost its stand collar
to a crossover wrap and a full layered skirt appeared over the trousers. Two
full-figure references competing over the same garment is a fight the written
rules cannot win, so **only one of them is the costume now** and the other is
scoped to the pieces it holds better.

**Neither is a face reference, and saying so is not optional.** A generation on
2026-08-01 came back in a perfect costume on the wrong woman because the costume
reference carried no scope. Any full-figure photograph attached to a prompt must
state what it is *not* for.

Do not attach `turn-working-front.png` or `costume-direction-front.png`: both are
pictures of costumes that no longer exist.

---

## The order to work in

**1. `turn-working-front` first, and nothing else until it is right.**

It becomes the approved reference in `outfits.yaml` — every other image matches
against it, so a wrong front view propagates into all twenty. Check it against
the revised spec before approving: hexagonal plates 10–15 mm across, tessellated
edge to edge and **never overlapped**, the same worn serpent stamp on every
plate, a **solid printed** gauntlet on her right forearm with a cluster of dim
wrist telltales, a **loose** cap on her left shoulder, **flank panels laced
across the centre front with vest cloth showing in the gap**, five visibly
different metals, and a WESTAR-35 on her right side.

Re-approve it in `outfits.yaml` once it is right.

**2. The other four turnaround views**, matched against it.

**3. `blaster` and `material-scale`** — the two plates that define the changed
objects. Once approved these become prop references in their own right.

**4. Everything else**, with all three references attached.

**5. `forest` is still owed a dusk frame.** It came back as a daylight camp, so
the question the slot exists to answer — does the charcoal costume separate from
wet forest at dusk — is still open, and it now overlaps `camp_day`. If it returns
a six-panel collage again, that is the prompt length talking: say *"one frame,
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

## Do not regenerate

`species_strip`, `expression_strip`, `knife`, `utility`, `scale_portrait`,
`material-leather`, `material-cloth`, `material-hardware`.

**Superseded by the build — these now need regenerating:**

| Image | Why |
|---|---|
| All five `turn-working-*` | **Superseded four times.** Hexagonal plates and WESTAR-35; then the flank panels and leather gauntlet; then the 2026-08-01 reference revision — printed gauntlet, loose shoulder cap, no torso metal, vest grain |
| `blaster` | It is a WESTAR-35 now, not a generic sidearm |
| `material-scale` | Hexagons with a pressed stamp, not round coins |
| `hero`, `camp_day`, `forest`, `maintenance`, `scale_figure` | Scale shape and blaster model both visible |

**The front turnaround is no longer approved** — the block is commented out in
`outfits.yaml`. **Redo it first**, re-approve it there, then everything else
matches against the new one.

`species_strip` and `expression_strip` are particularly good — leave them alone.

`tone-collage` is slot 16, the new **share sheet** — one image, six panels, for
sending to people on a phone. It is not on any board and is never used as a
costume reference. Every character now has this slot.

---

## Watch for

The failures that keep recurring:

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
