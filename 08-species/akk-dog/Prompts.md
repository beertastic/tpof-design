---
title: "Akk Dog — Image Prompt Pack"
asset_id: "CREATURE-AKK-DOG"
version: "0.1"
status: "scaffold"
category: "creature"
governing_documents:
  - ../../01-production-design/Production-Design-Bible-v1.0.md
  - Creature.md
---

# Akk Dog — Image Prompt Pack

> **SCAFFOLD.** The shared style rules below are complete and correct. The
> **Creature Constants** block is not — it must be filled from the built rig
> before this pack will hold the animal consistent. Every `**NEEDS:**` marker is
> a value to read off the asset.

This pack has two jobs, and they are different:

1. **Placement** — putting the akk dog into a scene alongside characters. This is
   the common case. Use the Creature Constants block plus a scene prompt.
2. **Board plates** — reference imagery for a creature production board.

**Always attach the reference plates from `reference/` to the conversation.**
Text alone will not hold an animal's shape across images, and a model with
repository access may be able to read this file without being able to see those
PNGs.

---

## Style — paste with every prompt

Live-action Star Wars production still. Outer Rim frontier realism in the manner
of the original trilogy and *Andor*, with a subtle *Mandalorian* frontier
aesthetic. Photographic, not illustrative.

This is a galaxy built from industrial salvage. Nothing is factory fresh. Every
object has had a previous owner and carries visible history: repairs, scratches,
faded paint, replaced components, grime.

Palette muted, sun-faded, practical — charcoal, ash grey, weathered black, faded
olive, dust brown, sand, bone white. Bright colour only for rank, warning
markings or a significant personal item.

Lighting motivated by believable sources only: natural sunlight, overcast sky,
work lamps, bulkhead fixtures, warning lights, firelight.

Camera: naturalistic composition over heroic posing. Restrained colour grade,
subtle atmospheric haze, realistic depth of field, fine film grain, practical
lens behaviour. The world feels larger than the people within it.

**Creature rendering.** Practical creature-effects quality — an animatronic or
suit performer photographed on set, not a digital fantasy creature. Real weight,
real breath, real body language. Skin and hide respond to light like actual
material.

---

## Do Not — paste with every prompt

No glowing eyes. No fantasy horns, ornamental spikes, or decorative frills. No
dragon, demon or monster-movie design language. Not a wolf, not a lion, not a
recognisable Earth animal with details added.

No exaggerated musculature, no impossible anatomy, no hero-monster posing, no
snarling-at-camera. It is an animal, not a threat display.

No weightlessness — a heavy animal displaces leaf litter, compresses ground and
moves earth. If it is standing on soft ground, that shows.

No pristine or ornamental tack. Any harness or collar is worn, repaired,
functional salvage like everything else in this world.

No text, logos, watermarks, captions or labels. No crushed blacks.

Photographic realism only: no anime, no cel shading, no painterly illustration,
no 3D-render look, no video-game creature.

---

## Creature Constants — paste with every prompt

> **INCOMPLETE — fill from the built asset before use.**

An akk dog: a large, heavy-bodied quadruped predator with an armoured hide,
kept as a guard and war beast. This one belongs to Captain Jasu, commander of the
mercenary crew.

**NEEDS — read these off the rig:**

- **Height at the shoulder, in metres.** State it in every prompt. This is the
  single value generators get wrong most often.
- **Body length**, nose to tail base
- **Hide** — armoured plating, scale, or hair; its colour range and how it
  catches light
- **Head and jaw** structure; ears or none; eye placement, size and colour
- **Stance** — how it holds its weight, head height relative to shoulder
- **Tail** — length, thickness, how it is carried
- **Distinguishing marks** unique to this individual animal
- **Tack** — harness, collar, or nothing

Once filled, this block should be specific enough that someone who has never seen
the rig could pick the right animal out of a line-up.

---

# Placement prompts

## P1. Scene 9 — Jasu and the akk dog
**The one scene the script requires.**

Evening in a forest mercenary camp. Captain Jasu stands among her mercenaries
delivering a briefing, one hand resting on or absently scratching her akk dog,
which is settled calmly beside her. Tents, tarpaulins, crates and a campfire
behind. She is giving orders and fussing over the animal at the same time — this
is routine for both of them.

The animal is relaxed and entirely at ease with her. It is not performing threat
and not looking at camera. Its size against the standing figures is the point of
the composition: this is a war beast being treated as a pet.

Overcast evening light with firelight spill. Mercenaries in the mid-ground
listening.

## P2. At rest in camp
Akk dog lying in the mercenary camp at night near the fire, head down, awake but
settled. Firelight raking across its hide showing the real texture. Crates and
tarpaulins around it. Utterly ordinary — this animal lives here.

## P3. Alert
Akk dog standing, head raised, weight shifted forward, attention locked on
something outside frame. Not snarling and not reared up — the stillness before
an animal moves. Wet forest, overcast light.

## P4. Scale plate with figures
Akk dog standing beside two standing human figures in the camp, side-on to
camera, full body of all three visible and unobstructed. Even overcast light, no
dramatic angle. **The purpose of this image is to establish size** — nothing may
be cropped and no foreshortening.

## P5. Working — tracking
*Only if the production decides the akk dog joins the pursuit (see Open Questions
in `Creature.md`).*

Akk dog moving through wet forest at early morning ahead of mercenaries, head
low, following ground scent. Working animal, purposeful, unhurried. Mist between
trunks.

---

# Board plates

For a creature production board, rendered from the rig where possible rather than
generated. Use the same slot geometry as a character board.

| # | File | Ratio | Content |
|---|---|---|---|
| 1 | `portrait.png` | 9:16 | The animal standing, full body, in the camp |
| 2 | `scale_plate.png` | 5:4 | Beside human figures, side-on, even light |
| 3 | `head_detail.png` | 3:4 | Head 3/4, jaw and eye structure |
| 4 | `hide_detail.png` | 1:1 | Hide texture at real scale |
| 5 | `poses_strip.png` | 21:9 | Standing, seated, alert, moving |
| 6 | `in_scene.png` | 9:16 | Scene 9 — with Jasu |
| 7 | `materials.png` | 5:4 | Hide, tack, palette swatches |

The board generator places images with a **contain** operation and never crops,
so supplying the wrong ratio letterboxes the board.

There is no `board-data.yaml` for this creature yet — create one modelled on
`03-characters/shada/board-data.yaml` if a creature board is wanted.

## Continuity rules

- Same animal in every image: same hide, same markings, same proportions.
- **Same shoulder height relative to humans in every image.** Check this first,
  every time.
- It gains no tack, scarring or ornament between images.
- It is never posed as a monster.

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 0.1 | 2026-07-30 | scaffold | Style rules complete; creature constants pending measurement from the built rig. |
