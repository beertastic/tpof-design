---
title: "Handedness and Placement"
asset_id: "PROMPT-HANDEDNESS"
version: "1.0"
status: "canonical"
---

# Handedness and Placement

**Every asymmetric element on a costume must be assigned a side, and that side
must never move.** This applies to all characters.

---

## Why it matters more than it sounds

**Continuity.** An image generator has no memory of which hip you used last time.
Unspecified, a holster lands on a different side in every frame, and a turnaround
becomes useless.

**Stunt and action design.** An actor draws with one hand. If the holster moves
between the costume boards and the shot list, the fight choreography is built on
a lie and somebody finds out on the day.

**Performance.** Where a weapon sits changes how a person stands, what they can
reach without turning, and which shoulder they lead with.

**Build.** A costume maker sets a holster once. They need to be told which side
before they sew.

---

## The convention

**Always state sides from the wearer's own left and right — never the viewer's.**

Add the note explicitly to every prompt:

> In a front view her right side appears on the viewer's left; in a back view it
> appears on the viewer's right.

Without that, a generator flips the whole rig between the front and back plates
of the same turnaround, and both look correct in isolation.

---

## Checking a back view

**The frame sides swap between front and back. Which of *her* sides carries the
item never changes.**

When she turns around, her right side moves from the viewer's left to the
viewer's right. Everything on it goes with her. So for a right-handed character:

| Element | Her side | Front view: viewer's | Back view: viewer's |
|---|---|---|---|
| Blaster | right thigh | left | **right** |
| Knife | left hip | right | **left** |
| Forearm armour | right | left | **right** |
| Shoulder armour | left | right | **left** |

Do not check a back view by asking whether an item stayed on the same side of
the frame. It should not have, and **the frame side cannot detect the failure
this test is meant to catch** — a horizontal flip of the front plate swaps the
frame sides too, exactly as a real rotation does.

**What catches a mirrored plate is anatomy, not position.** A genuine back view
shows shoulder blades, the back seams and closures of the garment, rear pockets,
the harness crossing the back, and the back of the head. A flipped front view
shows the face and the front closure. Look at what the plate is *of* before
looking at what is on which side of it.

---

## Establish handedness first

**It is the decision every other placement follows from.** Settle it before any
weapon or pouch is positioned.

Once set, the defaults fall out:

| Item | Right-handed default |
|---|---|
| Primary weapon | Right hip or right thigh, grip up and slightly forward |
| Blade | Left hip, grip up, for a cross-draw with the right hand |
| Secondary or backup | Off side, or small of the back |
| Tools and pouches | Off side, so they never foul the draw |
| Bandolier | Over the **left** shoulder down to the **right** hip, so the strap does not sit under the drawing arm |

Defaults are a starting point, not a rule. Deviating from them is fine and often
characterful — but it should be a decision, and it should be written down.

---

## What must be specified

For every character, in `Character.md` and in `outfits.yaml` under `must_show`:

- **Handedness**
- **Primary weapon** — which side, hip or thigh, drop-leg or belt, which way the
  grip points
- **Blade** — which side, angle, grip up or down, draw direction
- **Any second weapon**
- **Bandoliers and slings** — *"over the left shoulder to the right hip"*. State
  both ends; one is not enough
- **Pouches, tools, canteens** — which side
- **Armour** — every plate or patch, by side
- **Anything worn on one wrist, one shoulder or one leg**

---

## The test

> Could a costume maker dress a mannequin from this document without asking a
> single question?

If not, something has been left to chance, and a generator will decide it
differently every time.

---

## The generators check this

Both prompt generators run a placement check on every run and warn on stderr:

```
! baylan: no `handedness:` declared in outfits.yaml
! baylan/working: mentions blaster, holster, pistol but never says which side
```

It fires when:

- `handedness:` is missing from `outfits.yaml`
- an outfit has no `must_show:`, so its critical features will not be hoisted
- an outfit mentions an **asymmetric item** — gauntlet, bracer, holster, blaster,
  knife, sheath, bandolier, sling, pauldron, quiver, scabbard, prosthetic — and
  never says which side

Warnings do not stop generation. They are there so nobody ships a costume spec
with an unassigned holster without having been told.

**Every prompt containing a person now opens with the handedness line**, before
the non-negotiables:

> This character is RIGHT-HANDED. All positions are given from THEIR OWN left and
> right, never the viewer's.

## Required schema

In `outfits.yaml`, at the top level:

```yaml
handedness: right     # or left. Required.
```

And per outfit, every asymmetric element named with a side in `must_show`.

## Recording it

Put the placement in three places, because each is read by different people:

1. **`Character.md`** — the reasoning and the full spec. The build document.
2. **`Character-Lock.md`** — the short non-negotiable list.
3. **`outfits.yaml` → `must_show`** — so it is hoisted to the top of every
   generated prompt and repeated at the bottom.

The third is what actually reaches the image generator. The first two are what
reach the humans.

---

## Worked example — Shada

Right-handed.

| Item | Side | Detail |
|---|---|---|
| WESTAR-35 blaster | **Her right side** | Hip or thigh, either acceptable. Grip up, right-hand draw. Never her left |
| Combat knife | **Her left hip** | On the belt, grip up, cross-draw |
| Scale gauntlet | **Her right forearm** | Left forearm completely bare |
| Scale shoulder cap | **Her left shoulder** | Opposite side to the gauntlet |
| Scale thigh patch | **Her left outer thigh** | Same side as the shoulder cap |

Her torso carries no metal at all — the sternum patch was dropped on 2026-07-31.

Her right side carries the gauntlet and the blaster; her left carries the
shoulder cap, the knife and the thigh patch. **Nothing is mirrored, and no two
elements of the same kind share a side.**
