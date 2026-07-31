---
title: "Generic Mercenary"
asset_id: "CHAR-GENERIC-MERCENARY"
version: "0.2"
status: "in-development"
faction: "Mercenaries"
source: "Filmanize script breakdown, Mercenaries faction guide, Crew-Roster"
---

# Generic Mercenary

> **Production rule:** Refer to the Production Design Bible before any visual
> development or image generation.

## Art Department Brief

**This is not a character. It is a kit.**

Four background mercenaries have to read as four people who each assembled their
own gear over years — because that is the faction's entire identity. There is no
uniform, nothing is issued, and nothing matches. A costume built once and copied
four times destroys the only idea the faction has.

So the deliverable is a **modular system**: a set of shared component *classes*
with enough variants that four figures can be assembled from them and still look
like four individuals who chose differently.

**The rule is the class of item, not the item itself.** Every mercenary has good
boots. No two pairs match.

## Story Function

Four extras, drawn from this kit. See
[`Crew-Roster.md`](../../04-factions/mercenaries/Crew-Roster.md).

| Scene | Beat |
|---|---|
| 10 | **The Sabacc game.** All ten of the crew in one frame, one night, one campfire |
| 20–23 | The pursuit. The crew splits |
| 23 | **The large one takes hold of Vala.** She pulls a grenade from his belt; he panics and drops her; it detonates |
| 23 | Two die with the grenade |
| 24 | Two are killed by Baylan in the clearing |

**Scene 10 is where these four earn their money.** One frame establishes that
this crew exists, and the audience believes in it for the rest of the film. It is
also the only place all four are seen together, which makes it the test of
whether the kit produced individuals or a set.

**Every mercenary in the film dies except Baylan.**

## The system — component classes

Each class needs enough variants that no two of the four builds share one. Where
two figures must carry the same class of item, the items differ in material, age,
cut and how they are worn.

| Class | Variants | Notes |
|---|---|---|
| **Head** | 4 | Bare, cap or wrap, partial helmet, goggles pushed up. Never a matching helmet |
| **Torso base** | 4 | Work shirt, technical knit, sleeveless, layered tunic |
| **Outer layer** | 4 | Padded jacket, long coat, vest, poncho — or none |
| **Plating** | 4 | Placed differently on each: chest, one shoulder, forearms, thighs. Never a full set on anyone |
| **Harness** | 4 | Chest rig, bandolier, belt-and-braces, shoulder sling |
| **Legs** | 3–4 | Work trousers, reinforced, padded, wrapped |
| **Boots** | 4 | All good, all different — height, lacing, sole, wear pattern |
| **Pack and pouches** | 4 | Every figure carries differently. This is the silhouette |
| **Personal marks** | 4 | Trophies, kept objects, small decoration, paint. **This is what makes them people** |

**At most one figure carries any given silhouette cue.** If two of them read as
"the one with the long coat", one of them is wrong.

## The four builds

Proposed. The classes above are the system; these are one valid assembly of it.

### 1. The Wookiee — `heavy`

**Decided 2026-07-31: a full Wookiee, and an established member of the crew.** He
is at the Sabacc game and on the pursuit, not only in the Vala fight. See
[`Faction.md`](../../04-factions/mercenaries/Faction.md) for the cost and the
reasoning.

He is the only one of the four with a plot requirement. The beat needs a severe
size mismatch against Vala, **a grenade on a bandolier where a held person can
reach it**, and panic. A Wookiee gives the size for free, and the grenade must be
legible **in Scene 10**, ten scenes before Vala takes it, or the payoff plays as
convenient.

**He must not be Chewbacca.** Bandolier plus Wookiee plus forest is a silhouette
the audience already knows by name, and the bandolier is not optional here. So
the distinction has to come from everything else: a different fur colour and
pattern, a different age read, a bandolier of visibly different construction, and
**no bowcaster**. He assembled his own kit like everyone else in this crew and he
can afford good equipment — that is what separates him from a reference.

Beyond the fur he carries the heaviest gear of the four, and the least of it is
clothing.

### 2. The rifle — `ranged`

Long gun, and the kit is built around it. Lightest armour of the four, most
pouches, best boots. A shooter's silhouette: nothing on the shoulder that fouls a
stock, nothing on the chest that stops him going prone.

### 3. The close one — `armoured`

**The most actual armour of the four** — the Wookiee is bigger but mostly fur,
and carries plate only on his forearms and one shoulder. This one has a segmented
chest rig and plates on both arms.

Shortest weapon, built for the clearing rather than the chase, and the only one
wearing anything on the head that could be called a helmet — partial, salvaged,
and clearly not issued.

### 4. The second non-human — `alien`

A second non-human species, and their kit is cut for a body that is not human.
Two different species in four figures is what proves this crew found each other
rather than being recruited: different anatomy, same standard of gear.

Species is an open question, with three constraints now that the Wookiee is
confirmed:

- **Practical make-up and silhouette, not a full creature build.** The Bible
  favours practical solutions, the budget is already carrying one full suit, and
  a background extra cannot carry a second.
- **Not large and not furred.** That read belongs to the Wookiee. This one should
  be closer to human scale and clearly a different *kind* of non-human.
- **Not serpentine and not scaled.** That language is Shada's and duplicating it
  weakens hers.

## Species mix

**Two non-humans among the four**: the Wookiee, and one other species that shares
none of his physical language. The remaining two are human or near-human.

Draw on the established Star Wars alien population — mercenary work in the Outer
Rim is not a human profession, and an all-human crew of ten would be the odd
thing to have to explain.

The crew now reads as genuinely mixed at the fire in Scene 10, which is the
single frame that has to sell the faction.

## Handedness

**All four are right-handed**, and every placement follows from that. See
[`09-prompt-library/Handedness-And-Placement.md`](../../09-prompt-library/Handedness-And-Placement.md).

A left-handed figure would be a nice piece of individuality, but `outfits.yaml`
declares handedness once per character file and the generator cannot vary it per
build. Mixing it by hand is how placements get flipped, which has already cost
this production images. Not worth it for a background figure.

## Quality — the difference from the escapees

This crew is good at the work and the work pays. **That money is on their
bodies.**

- Good leather, sound plating, maintained hardware, boots that work.
- Repairs done properly, with tools and materials — not by hand in poor light.
- Everything fits. Every piece has been adjusted over years.
- Nothing factory fresh. Nothing ruined either.

The escapees wear what they were given and it is being destroyed. These four
chose every piece and look after it. **That contrast has to survive at distance,
in one frame, at night, by firelight.**

## Equipment and Hero Props

Blasters, rifles, a scanner, tents, tarpaulins, crates, ammunition, field-camp
equipment. All maintained, all functional, **none of it issued**.

**The grenade on the large one's belt is a hero prop**, not set dressing. It is
planted in Scene 10 and paid off in Scene 23.

## Performance and Body Language

- Competent and unhurried. They have done this before and expect to be paid.
- No military posture, no formation, no unit discipline. They are not soldiers.
- They are racing a city, not strolling a wilderness — scenes 20 to 23 carry a
  deadline. See the faction guide.
- Around the fire in Scene 10 they are comfortable with each other. That comfort
  is what makes the clearing land.

## Rejections

- **No uniform, no insignia, no faction colour, no matching anything.** If two of
  the four look like they were dressed by the same person, it is wrong.
- No military unit read.
- No Caribbean pirate, medieval, Victorian, Roman or modern tactical/SWAT
  language — per the Design Bible.
- Nothing factory-fresh. Nothing ruined either.
- No full armour set on anyone. Plating is partial and placed differently on each.
- No character-defining silhouette shared between two builds.

## Scene Appearances

Scenes **10, 20–23, 24**. See
[`Scene-Index.md`](../../02-story/script-breakdown/Scene-Index.md).

## Canonical Prompt Framework

1. Production Design Bible
2. Faction guide — [`Mercenaries`](../../04-factions/mercenaries/Faction.md)
3. This document
4. Scene requirements
5. Camera and lighting instructions

## Open Questions

- **What species is the second non-human?** It needs to work in practical
  make-up, read at distance by firelight, and share nothing with either the
  Wookiee (large, furred) or Shada (serpentine, scaled).
- ~~Is the large one a partial Wookiee or a large near-human?~~ **Decided
  2026-07-31: a full Wookiee, established in the crew from Scene 10.**
- **What does the Wookiee carry instead of a bowcaster?** The obvious weapon is
  the one that makes him a reference rather than a character.
- **Does his fur survive the forest schedule?** Hair maintenance scales with
  shooting days, and putting him in Scene 10 and the pursuit added days.
- Do any of the four have a visible relationship in the Sabacc scene? Nyx wins
  the pot off *somebody*.
- Are the two who die with the grenade the two we spent most time on earlier, or
  deliberately not?
- Does any of them carry something that pays off later, the way the grenade does?

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 0.2 | 2026-07-31 | in-development | Written up as a modular kit: component classes, four proposed builds, species mix, handedness, quality rules and rejections. |
| 0.1 | 2026-07-30 | placeholder | Placeholder document created from current production data. |
