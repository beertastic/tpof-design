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

### 1. The large one — `heavy`

The Wookiee candidate, and the only one of the four with a plot requirement.

**What the beat needs:** a severe size mismatch against Vala, **a visible
bandolier or belt with a grenade on it**, and panic. It does not need a Wookiee —
see the faction guide for the cost ladder.

Built here as a **very large human or near-human**: the cheapest option that
delivers all three, and the one that survives a forest shoot. Heaviest plating of
the four, most physical presence, least agility. The grenade must be legible on
his belt **in the Sabacc scene**, ten scenes before Vala reaches for it, or the
moment plays as convenient.

### 2. The rifle — `ranged`

Long gun, and the kit is built around it. Lightest armour of the four, most
pouches, best boots. A shooter's silhouette: nothing on the shoulder that fouls a
stock, nothing on the chest that stops him going prone.

### 3. The close one — `armoured`

Most plating, shortest weapon, built for the clearing rather than the chase.
Heavy at the chest and forearms, and the only one wearing anything on the head
that could be called a helmet — partial, salvaged, and clearly not issued.

### 4. The non-human — `alien`

**One of the four is a distinctly non-human species**, and their kit is cut for a
body that is not human. That is what proves this crew found each other rather
than being recruited: different anatomy, same standard of gear.

Species is an open question. Whatever is chosen it must work as **practical
make-up and silhouette rather than a full creature build** — the Bible favours
practical solutions, and a background extra cannot carry a prosthetic budget.

## Species mix

Human and near-human baseline, with **one distinctly non-human** among the four.
Draw on the established Star Wars alien population: mercenary work in the Outer
Rim is not a human profession, and an all-human crew of ten would be the odd
thing to have to explain.

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

- **What species is the non-human?** It needs to work in practical make-up, read
  at distance by firelight, and not duplicate Shada's serpentine language.
- **Is the large one a partial Wookiee or a large near-human?** Decision needed
  before casting. If a Wookiee is in the crew he must appear in Scene 10, or his
  arrival in the final act reads as convenient.
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
