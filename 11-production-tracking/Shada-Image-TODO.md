---
title: "Shada — Finish List"
asset_id: "TRACK-SHADA-IMAGES"
updated: "2026-07-31"
---

# Shada — Finish List

**Status: 20/20 images, 5/5 boards built, validation clean.**

`turn-working-back`, `maintenance`, `camp_day` and `forest` are all correct and
on the boards. `camp_day` is now the standing bright-daylight plate it was meant
to be, with the blaster on the correct side. The old `forest` was the six-panel
collage; it is kept as `source/artwork/tone-collage.png` under the new share
sheet, slot 16.

Two things are worth a look before she is signed off, neither blocking:

- **`forest` is a daylight camp, not the dusk in-situ.** Slot 4 exists to answer
  one question — does the charcoal costume separate from a wet forest at dusk —
  and a daytime camp does not answer it. It also now covers similar ground to
  `camp_day`.
- **The four metals are converging on brass.** In the newest plates the gauntlet,
  cap, sternum and thigh patches read as much the same alloy. The mismatch is
  what proves nobody made the costume for her; if they match, that is quietly
  lost.

---

## Start here

```bash
cd /home/tris/tpof-design
source .venv/bin/activate
python tools/prompt-splitter/split.py shada
python tools/prompt-splitter/turnarounds.py shada
```

**Run this first, every time.** The prompts have changed since the last images
were made, and two images have already been lost to stale copies.

Then open a **fresh** ChatGPT conversation and attach both references *before*
pasting anything:

- `03-characters/shada/source/artwork/turn-working-front.png` — approved costume
- `03-characters/shada/reference/actor/dasha-svistunenko-heashot.jpg` — actor

Say: *"These are the approved costume and actor references. Match them exactly in
everything that follows."*

---

## The one to generate

### `forest` — the dusk in-situ reference

Prompt: `03-characters/shada/prompts/04-forest.txt`

The reality check on whether her charcoal costume separates from a wet forest at
dusk. Full figure, moving low, overcast dusk, wet rim highlights keeping her off
the background. It is the only image in the set that answers that question, so a
daylight or firelit frame does not substitute for it.

The last attempt returned a six-panel collage instead. If that happens again it
is the prompt length talking — the single-image instruction sits at the top and
bottom with two thousand words of costume-record language in between. Say
*"one frame, not a contact sheet"* when you paste it.

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
| Gauntlet | right forearm | **right** |
| Shoulder cap | left shoulder | **left** |
| Thigh patch | left thigh | **left** |
| Blaster | right thigh | **right** |
| Knife | left hip | **left** |

Note that a horizontal flip of the front view *also* swaps the frame sides, so
frame position cannot catch a mirror. What catches it is anatomy: a real back
view shows shoulder blades, the back seams of the vest, rear pockets and the
back of her head. A mirrored front shows her face and the front closure.

The current `turn-working-back` passes both tests.

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

`turn-working-front` (approved), `-left`, `-right`, `-back`, `-natural`, `hero`,
`scale_figure`, `scale_portrait`, `species_strip`, `expression_strip`, `blaster`,
`knife`, `utility`, `maintenance`, and all four `material-*`.

`species_strip` and `expression_strip` are particularly good — leave them alone.

`tone-collage` is slot 16, the new **share sheet** — one image, six panels, for
sending to people on a phone. It is not on any board and is never used as a
costume reference. Every character now has this slot.

---

## Watch for

The failures that keep recurring:

- **Metal on both forearms.** One gauntlet, her right.
- **Shoulder caps on both shoulders.** One cap, her left — the opposite side to
  the gauntlet. This is the rule doing the most work in the design: symmetry
  quietly turns scavenged mismatch into a costume somebody made for her.
- **Matching scale patches.** Four patches, four different metals.
- **A bulky silhouette.** Close-fitting, cut to the figure.
- **Any interior.** Forest, clearing or camp only. If there is a wall or ceiling, it is wrong.
- **A modern coil zip.** Industrial hardware, or hooks and lacing. Still slipping
  through on nearly every frame — the one recurring fault not yet beaten.
- **The blaster on her left.** It is on her right thigh; only the knife is on her
  left.
- **Four patches in the same metal.** Steel gauntlet, brass cap, dark bronze
  sternum, brighter new thigh patch. They drift toward matching brass.

Two or more together almost always means **the references were not attached**.

---

## The gap this character exposed — props have no lock

**The costume has an approved reference image. The props do not.**

`outfits.yaml` carries `approved.reference`, pointing at the locked front
turnaround, and every prompt tells the operator to attach it. That is why the
costume now holds still across twenty images.

Nothing does that job for the blaster, the knife, the utility kit or the scale
patches. They are described in words and redrawn from scratch every time, so they
drift — a different gun in every plate, scales that change size and colour, kit
that gains and loses items. Words cannot hold a silhouette; only an image can.

The fix mirrors what already works:

```yaml
# outfits.yaml
props:
  blaster:
    reference: 03-characters/shada/source/artwork/blaster.png
    approved: "2026-07-31"
    slots: [1, 2, 3, 4, 9, 11]     # where it must match
  knife:
    reference: 03-characters/shada/source/artwork/knife.png
    approved: "2026-07-31"
    slots: [1, 2, 3, 4, 8, 11]
```

`split.py` then emits an operator line naming the plates to attach for that slot,
exactly as it already does for the costume reference, and the prompt tells the
model those images outrank the text.

**Worth building before Baylan, not after.** He has a blaster, a holster and a
rifle across four outfits — the same drift, multiplied.

---

## After Shada

Baylan is next, and one thing must happen before generating any of his twenty
turnarounds:

**Declare `handedness:` in `03-characters/baylan/outfits.yaml`, and add
`must_show:` to each of his four outfits.**

The placement checker is already warning about both — he has a blaster, a holster
and a rifle with no side assigned. One edit now, or twenty regenerations later.

He will also want a `promo-data.yaml`. Copy Shada's, keep the structure, replace
the copy — see `tools/board-generator/README.md`.
