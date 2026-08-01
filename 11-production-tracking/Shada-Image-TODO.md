---
title: "Shada — Finish List"
asset_id: "TRACK-SHADA-IMAGES"
updated: "2026-07-31"
---

# Shada — Finish List

**Status: DESIGN CLOSED 2026-07-31. Documents are the deliverable; images are a
guide.**

Her documents, `outfits.yaml` and all 21 prompts are current and internally
consistent. The checker is clean and the boards validate.

**The images are deliberately not "finished", and that is the right call.** Every
generation lands differently, and the build will change again with budget and
what the supplier actually has. The prompts and the character documents are what
holds — an image is a guide to the intent, not the intent itself. Regenerate when
useful, approve what is close enough, and do not chase pixel agreement.

What the build actually needs is settled:

- **Three patches** — right forearm gauntlet, left shoulder cap, left thigh. No
  metal on her torso.
- **Three different metals** — dull grey steel, brass with verdigris, dark
  bronze. The mismatch is the point.
- **Plates 10–15 mm**, regular hexagons, tessellated edge to edge, never
  overlapped, each carrying a raised snake swirl that varies plate to plate.
- **Roughly 370 plates.** See `Costume-Build-Method.md` — this is the largest
  hidden labour item in the costume.
- **WESTAR-35** on her right side; combat knife on her left hip.
- **Skin:** a faint scale pattern like a tattoo, ancestry tens of thousands of
  years back. Reptilian contact lenses are the highest-value make-up item.

Open, non-blocking: photograph the printed WESTAR-35 and add it under
`references:` in `outfits.yaml` — the entry is there, commented. And run a noise
test on the first finished patch; she is an infiltrator and 370 hard plates is
not obviously a quiet garment.

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

## The order to work in

**1. `turn-working-front` first, and nothing else until it is right.**

It is the approved reference in `outfits.yaml` — every other image matches
against it, so a wrong front view propagates into all twenty. Check it against
the new spec before approving: hexagonal plates 10–15 mm across, tessellated
edge to edge and **never overlapped**, the same worn serpent stamp on every
plate, three visibly different metals in three patches with no metal on the
torso, and a WESTAR-35 on her right side.

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

`species_strip`, `expression_strip`, `knife`, `utility`, `scale_portrait`,
`material-leather`, `material-cloth`, `material-hardware`.

**Superseded by the build — these now need regenerating:**

| Image | Why |
|---|---|
| All five `turn-working-*` | Hexagonal plates and the serpent stamp; WESTAR-35 |
| `blaster` | It is a WESTAR-35 now, not a generic sidearm |
| `material-scale` | Hexagons with a pressed stamp, not round coins |
| `hero`, `camp_day`, `forest`, `maintenance`, `scale_figure` | Scale shape and blaster model both visible |

The front turnaround is still the approved reference in `outfits.yaml`. **Redo it
first**, re-approve it, then everything else matches against the new one.

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
- **Matching scale patches.** Three patches, three different metals.
- **A bulky silhouette.** Close-fitting, cut to the figure.
- **Any interior except the Sabacc hold.** Forest, clearing or camp — with the single exception of slot 2, Scene 10, which moved inside the ship on 2026-08-01. Anywhere else, a wall or ceiling is wrong.
- **A modern coil zip.** Industrial hardware, or hooks and lacing. Still slipping
  through on nearly every frame — the one recurring fault not yet beaten.
- **The blaster on her left.** It is on her right thigh; only the knife is on her
  left.
- **Three patches in the same metal.** Steel gauntlet, brass cap, dark bronze
  thigh. They drift toward matching brass.
- **Metal on the torso.** There is none. A chest patch, bib or pendant is wrong.

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
