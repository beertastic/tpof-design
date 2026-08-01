---
title: "Mercenary Kit — Image Prompt Pack"
asset_id: "CHAR-MERCENARY-KIT"
version: "0.2"
status: "ready"
faction: "Mercenaries"
governing_documents:
  - ../../01-production-design/Production-Design-Bible-v1.0.md
  - ../../04-factions/mercenaries/Faction.md
  - Character.md
  - outfits.yaml
---

# Mercenary Kit — Image Prompt Pack

**Faction:** Mercenaries
**Scenes:** 10, 20–23, 24
**Primary environment:** Forest
**Brief:** A modular kit, not a character. Four background mercenaries assembled
from shared component classes, who must read as four people who each chose their
own gear.

---

## Order of work

**The turnarounds come first.** They live in `prompts/turnarounds/`, generated
from `outfits.yaml` by `tools/prompt-splitter/turnarounds.py`, and they carry the
per-build non-negotiables. Nothing in this file can be generated properly until
at least one build has an approved front view to attach as a reference.

1. Generate `turn-heavy-front` and the other three front views.
2. Approve them, and record each as `approved.reference` in `outfits.yaml`.
3. Generate the remaining turnaround views against those references.
4. Then work through the slots below.

**The large one has no turnaround, by decision.** The image generator refuses
him — see Character.md. His specification is written, his bandolier plate is
slot 9 and must be done, and the rest is settled with the performer. Four slots
below put him in frame among the others; try them, and if one refuses, generate
the other three and note his scale in words.

**Slot 1, the line-up, is the important one.** It is the only image that tests
whether the kit produced four individuals or one costume in four colours. Every
"the only X in the crew" rule in `outfits.yaml` exists to be checked against it.

---

## How to use

Each numbered slot is a complete, self-contained prompt. Save the result to the
exact filename given, in `03-characters/mercenary-kit/source/artwork/`.

Everything needed is written out below — no other file has to be read first.

---

## Style — paste with every prompt

Live-action Star Wars production still. Outer Rim frontier realism in the manner
of the original trilogy and *Andor*, with a subtle *Mandalorian* frontier
aesthetic. Photographic, not illustrative.

This is a galaxy built from industrial salvage. Nothing is factory fresh. Every
object has had a previous owner and carries visible history: repairs, scratches,
faded paint, replaced components, grime, evidence of servicing.

Costume is functional workwear first — real, buildable construction with
believable seams and fasteners, no floating armour, nothing purely decorative.
Occupation should be readable from silhouette alone. Materials: ballistic weave,
quilted flight fabric, reinforced synth-leather, flexible armour mesh, woven
technical textiles, plastoid plates, insulated work fabric, industrial rubber,
brushed alloy.

Palette muted, sun-faded, practical — charcoal, ash grey, weathered black, faded
olive, dust brown, sand, bone white. Secondary: rust red, ochre, deep burgundy,
forest green, navy blue. Accents (brass, copper, oxidised bronze, warning
yellow) used sparingly. Bright colour only for rank, warning markings, cultural
identity or a significant personal item.

Lighting motivated by believable sources only: natural sunlight, overcast sky,
work lamps, bulkhead fixtures, warning lights, control panels, firelight.

Camera: naturalistic composition over heroic posing. Restrained colour grade,
subtle atmospheric haze, realistic depth of field, fine film grain, practical
lens behaviour. Subject engaged in meaningful activity rather than looking at
camera unless specified. The world feels larger than the people within it.

---

## Do Not — paste with every prompt

No Caribbean or Earth pirate costume, tricorn silhouettes, pirate coats,
corsets, Renaissance or medieval clothing, medieval leather armour, fantasy
shoulder pads, decorative belts, swashbuckler aesthetics, Victorian fashion,
Roman armour, modern tactical/SWAT gear.

No pristine futuristic minimalism. No factory-fresh or polished surfaces. No
ceremonial or ornamental equipment. No oversized or stylised weapons. No glowing
decorative technology. No gadget overload.

No glamour posing, no sexualisation, no fashion-editorial lighting.

No text, logos, watermarks, captions, labels or lettering in the image.

No crushed blacks — the silhouette must stay separated from the background.

Photographic realism only: no anime, no cel shading, no painterly illustration,
no 3D-render look, no plastic or waxy skin.

---

## Capture — NARRATIVE slots only

> **Paste with slots 2, 3, 13** — in-scene frames.
>
> **Do NOT paste with the line-up, the kit plates or the material plate** (1, 4–12). Those want flat, even
> documentation light and sharpness across the whole frame. Shallow depth of
> field on a materials board is a fault, not a style.

Shot on **anamorphic lenses** in the manner of the original Star Wars trilogy —
Panavision-style anamorphic glass, not modern clinical optics.

**Optical character:** oval, horizontally-stretched bokeh in out-of-focus
highlights. Gentle barrel distortion. Noticeably softer toward the frame edges
while the focal plane stays sharp. Shallow depth of field with smooth falloff.
Faint horizontal streak flare where a bright practical source is in frame —
restrained, never a showpiece. Mild chromatic aberration at high-contrast edges.
Slight vignetting.

**Photochemical character:** the response of 35mm motion picture negative — fine
organic grain, present in shadows and midtones rather than added uniformly.
Gentle halation blooming around bright sources. Highlight rolloff that compresses
rather than clips. Rich shadow that retains detail instead of going black.

**Colour:** restrained, filmic, desaturated toward the muted end. Skin natural
and slightly warm. No digital vibrance, no teal-and-orange grade.

**Focus behaviour:** one plane is sharp and everything else falls away. Detail
resolves where the lens is focused and softens elsewhere — do not render every
surface at equal sharpness.

The image should look like a **frame from a photochemical motion picture**, or a
unit stills photographer's frame from the same set. Not a rendered picture.

---

## Anti-synthetic — any slot containing a FACE

> **Paste with slots 1, 2, 3, 4, 11, 13.** Wider than the Capture block: the line-up and the head plate are lit flat, but
> the skin still has to be real.
> This is the block that defeats the plastic-AI look, and it applies wherever
> there is a person.

**Skin must be real.** Visible pores, fine lines, uneven tone, blemishes, broken
capillaries, stubble, shine where skin is oily and matte where it is not.
Subsurface scattering at the ears and nostrils. **No smoothed, waxy, airbrushed
or plastic skin. No beauty retouching of any kind.**

**Faces are asymmetric.** Eyes differ slightly, the expression is uneven, nothing
is mirrored.

**Lighting has a direction and a cost.** One dominant source with genuine shadow
and real falloff. No omnidirectional fill, no unmotivated rim light, no glow
without a source.

**Framing is imperfect.** Off-centre, unbalanced headroom, something clipped by
the frame edge or slightly in the way. Not a composed poster.

**Detail is not uniform.** Real photographs have areas of mush — motion, focus
falloff, underexposed corners. Do not render every fibre at maximum sharpness.

**Nothing is symmetrical, new or clean** unless the shot says so.

---

## Species rendering — paste if non-human

Alien species must feel biologically plausible and grounded in live-action Star
Wars. Favour practical make-up and prosthetic effects over exaggerated digital
fantasy. Costume adapts to anatomy without sacrificing practicality.

---

## Costume rules — LARGE-ONE PLATES ONLY

> **Applies to slots 9, 10** — the bandolier and the fur study.
>
> **Deliberately narrow, and it must stay that way.** The generator injects the
> non-negotiables of the *first* outfit in `outfits.yaml`, which is `heavy`, the
> large one. That is correct for a plate showing only him and wrong for anything
> showing the other three. Every other slot gets all four builds through the
> Character Constants block instead. Do not widen this list.

The non-negotiable costume rules are injected here automatically from
`outfits.yaml`.

---

## Character Constants — paste with every prompt

**This is a kit, not a person.** Four background mercenaries in the Mercenaries
faction, assembled from one modular system. There is no uniform, nothing is
issued and nothing matches. Every one of them assembled their own gear over
years, and that is the faction's entire identity — a crew of self-assembled
individuals who can afford good equipment looks nothing like a herd of people
wearing what they were handed.

They are good at this work and it pays well. **That money is on their bodies:**
good leather, sound plating, maintained hardware, boots that work, repairs done
properly with tools rather than by hand in poor light. Everything fits, because
everything has been adjusted over years. Nothing is factory fresh. Nothing is
ruined either — that is the difference between this crew and the escapees they
are hunting.

**All four are male and all four are right-handed.** Weapon and armour placement
is stated from the wearer's own left and right, never the viewer's.

**THE FOUR BUILDS.** No two share a silhouette cue. If two of them read as the
same person in different clothes, the image has failed.

1. **THE LARGE ONE** — a towering fur-covered humanoid, over two metres tall and
   massively built, entirely covered in coarse body hair. Broad chest, very long
   powerful arms, a heavy brow over deep-set dark eyes, a projecting muzzle. His
   hair is dark iron-grey shot through with rust brown, mottled and uneven,
   paling almost to white at the muzzle, and he is visibly old. Very little clothing: a broad hand-built ammunition bandolier over one
   shoulder carrying grenades on the front of it, a narrower utility strap
   crossing it the other way, a heavy working belt, and salvaged plate strapped
   over the forearms and one shoulder — oversized, refitted for him. His weapon
   is a human-sized blaster rifle worn on his right hip like a pistol. Metal
   rings and beads braided into the fur at the shoulder and muzzle. **Coarse, uneven, badly
   kept hair, thinning over the shoulders and scarred — never long or glossy.**
2. **THE RIFLE** — lean and quick, built around a salvaged long gun on a shoulder
   sling. The lightest armour of the four: one shoulder pad on his right, the
   trigger side, and nothing on the chest or shoulders that would foul a stock or
   stop him going prone. The most pouches of anyone, carried low on hips and
   thighs. Best boots in the crew. A cap or wrapped head-cloth with goggles
   pushed up on the forehead. Job tallies notched into the rifle stock.
3. **THE CLOSE ONE** — the most actual armour: a segmented chest rig and plates on
   both forearms, the only figure with armour on both arms. A partial salvaged
   helmet covering the crown and one side of the face, jaw and other side open —
   the only headgear in the crew that could be called a helmet. A short weapon on
   his right hip, never a long gun. No coat. Trophies taken from targets fixed to
   the helmet and the rig.
4. **THE NEAR-HUMAN** — human bone structure, human scale, differing from human in
   skin colour and markings only: a distinct muted skin tone that is clearly not
   a human complexion, and geometric inked markings across the face. **Achieved
   in make-up alone — no appliances, no prosthetics, nothing glued on.** Bare
   head so the markings read. The only long coat in the crew, weathered, below
   the knee, worn open. Belt and braces, nothing across the chest. Small kept
   objects from a life before this threaded onto the belt. **Not serpentine, not
   scaled, not furred, not large.**

**Personal marks are the group read.** Each carries a different *kind* of
decoration and no two are alike: braided into the body, notched into a weapon,
trophies off other people's gear, kept objects on a belt. Four figures decorating
themselves the same way would be a uniform by another name.

**Performance:** competent and unhurried, no military posture, no formation, no
unit discipline. They are not soldiers and never were. They are racing a city,
not strolling a wilderness.

---

## Character-specific rejections

The specific wrong directions a generator will drift toward for *this* character.

1. **A uniform.** Any two figures who look dressed by the same person, in
   matching materials, matching plating or a shared colour scheme. This is the
   single most likely failure and it kills the faction's only idea.
2. **Two figures sharing a silhouette cue.** One long coat, one helmet, one long
   gun, one set of crossed straps — each belongs to exactly one build.
3. **A military unit read.** Formation, matching rank markings, insignia,
   anything that looks issued, anything that looks like surplus.
4. **A large fur-covered figure resembling any well-known one.** Warm chestnut
   hair, a long glossy evenly-flowing coat, a single neat woven diagonal strap, a
   crossbow-like weapon. This one is grey, mottled, coarse-coated, scarred, old.
5. **A creature build on the near-human.** Horns, tentacles, head-tails, a
   snout, appliances of any kind. He is make-up only and must hold a close-up.
6. **Serpentine or scaled anything.** That language belongs to Shada.
7. **Ruined gear.** These are not the escapees. Worn and repaired, never
   destroyed, never filthy, never falling apart.
8. **Drifting out of Star Wars.** Building without a uniform means sourcing
   freely, and that freedom is where a costume leaves the franchise. No Earth
   military surplus, no historical costume, no contemporary fashion.

---

# Prompt slots

## 1. `lineup.png` — the four together

**Wide, 2:1.**

**THE KEY IMAGE OF THIS PACK.** The only one that proves the kit produced four
individuals rather than one costume in four variations.

All four builds standing in a single frame, side by side, facing camera, evenly
spaced against a plain neutral studio backdrop. Flat, even documentation
lighting, sharp across the whole frame, no atmosphere and no mood. Full figure,
head to boots, all four standing on the same ground line at true relative scale —
the large one towers over the other three and that size difference must be honest.

Left to right: the large one, the rifle, the close one, the near-human.

Each of the four must be immediately distinguishable from the other three at a
glance, by silhouette alone, before any detail is read. Different heights,
different bulk, different outer layers, different headwear, different weapons
carried differently.

## 2. `sabacc.png` — Scene 10, the ship's hold

**Landscape, 16:9.**

**INTERIOR. Moved inside on 2026-08-01** — the scene plays in the mercenary
ship's main hold, not at a campfire. It is the only interior in the mercenary
pack.

The Sabacc game in a cramped, salvaged cargo hold at night. All four sitting
around a crate with cards and a pile of chips, comfortable with each other,
mid-game. **A single work lamp swings overhead and is the only source** — hard
top light, moving shadows, deep falloff into the corners. Exposed pipework,
tie-downs, mismatched paint, scuffed decking, stacked salvage, service markings.
Lived-in and over-occupied: this crew sleeps in a space too small for them.

This is the frame that establishes the crew exists, and it has to survive being
lit by one lamp — the four silhouettes must still separate from each other and
from the dark hold behind them.

Relaxed, off duty, weapons still on them because they always are.

**Not a clean ship.** No polished surfaces, no glowing consoles, no bridge or
cockpit. This is a hold that has had cargo dragged across it for twenty years.

## 3. `pursuit.png` — moving through the forest

**Landscape, 16:9.**

The four moving through dense wet forest in daylight, spread out, covering
ground with purpose. They are racing a city, not strolling a wilderness — there
is a deadline on this and it shows in the pace. Overcast daylight, mist between
trunks, wet ground.

Not a formation and not a patrol line. Four individuals who work together and
each move their own way.

## 4. `kit-heads.png` — head treatments

**Wide banner, 3:1.**

The four head treatments side by side, shoulders up, flat even documentation
light against a plain neutral ground. Left to right: the large one's bare furred
head with rings and beads braided in; a cap or wrapped head-cloth with goggles
pushed up on the forehead; a partial salvaged helmet covering the crown and one
side of the face; a bare human-proportioned head with geometric inked markings
and a skin tone that is not a human complexion.

Four completely different answers to the same problem. No two share a material.

## 5. `kit-harness.png` — how each one carries

**Wide banner, 3:1.**

The four chest and harness solutions, torso only, flat even documentation light
against a plain neutral ground. Left to right: a broad hand-built ammunition
bandolier with grenades seated on the front, crossed by a narrower utility strap;
a bare chest and shoulders deliberately clear of anything that would foul a rifle
stock, with pouches carried low instead; a segmented armour chest rig; belt and
braces with nothing worn across the chest.

This plate is where the individuality either works or fails — it is the same
problem solved four ways.

## 6. `kit-plating.png` — where the armour sits

**Wide banner, 3:1.**

The four plating solutions laid out flat on a neutral surface, evenly lit, sharp
across the frame. Oversized forearm and single-shoulder plate cut for a limb that size;
a single shoulder pad; a segmented chest rig with both forearm plates; and an
empty space where the fourth would be, because the near-human wears no plate at
all.

All salvaged, all mismatched alloys, all obviously cut and refitted rather than
manufactured as a set. Nothing here matches anything else here.

## 7. `kit-boots.png` — four pairs, none matching

**Wide banner, 3:1.**

Four pairs of boots side by side on a plain neutral surface, flat even light.
Every mercenary has good boots and no two pairs match: different heights,
different lacing, different soles, different wear patterns. One pair is enormous.

All well made, all maintained, all repaired properly. This plate exists to prove
the class-not-item rule.

## 8. `kit-marks.png` — what makes them people

**Wide banner, 3:1.**

Four small studies of personal decoration, flat even light on a plain neutral
ground. Metal rings and beads braided into shaggy fur; job tallies notched into a
worn rifle stock in counted groups, smooth where a hand sits; small hard trophies
obviously cut from other people's gear, fixed to a helmet and a chest rig; and
small worn kept objects, clearly not equipment, threaded onto a belt.

Four different *kinds* of decoration, not four versions of the same one.

## 9. `bandolier.png` — the hero prop

**Square, 1:1.**

The large one's ammunition bandolier laid out on a plain neutral surface,
photographed flat and evenly lit, sharp across the whole frame — the kind of
plate an art department shoots to document what it has built.

Broad, thick, hand-built heavy leather, obviously made for a body far larger than
a human, worn and darkened where it has sat across fur for years. **At least two
grenades seated on the front face of it**, in open cradles rather than closed
pouches, held firmly but reachable in one movement by someone who is not wearing
it. That seating is the point of this plate: Vala takes one of these off him
while he is crushing her, so it must be legible that a grenade can be got at
quickly and by someone else.

Show the crossing utility strap alongside it.

## 10. `heavy-fur.png` — fur colour and texture

**Square, 1:1.**

A close study of the large one's body hair: shoulder, upper arm and the side of the
muzzle, evenly lit and sharp, filling the frame.

**Dark iron-grey shot through with rust brown**, greying and paling at the
muzzle, coarse and long, matted and darkened in places by weather and work.
Visibly an older animal. Metal rings and beads worked into braids close to the
skin.

This plate exists to settle the colour, because the difference between this
character and a famous one is largely this surface. **It is not warm chestnut
brown.**

## 11. `nearhuman-markings.png` — the make-up reference

**Portrait, 3:4.**

Head and shoulders of the near-human against a plain neutral ground, flat even
light, sharp — a make-up department reference plate rather than a portrait.

A distinct muted skin tone that is clearly not a human complexion, even across
the whole face and neck. Geometric inked markings — deliberate, angular, placed
with intent, reading as earned rather than chosen for looks. Human bone
structure, human proportions, ordinary human features underneath.

**Nothing is glued on. No appliance, no prosthetic, no horns, no ridges.** Skin
colour and markings only. This is what a make-up artist will work from, so the
edges of every marking must be legible.

## 12. `materials.png` — materials and palette

**Square, 1:1.**

A flat-lay material board for the mercenary faction on a plain neutral surface,
evenly lit, sharp across the frame. Swatches of the materials this crew is built
from: good worn leather in several different tans and blacks, ballistic weave,
quilted work fabric, salvaged alloy plate in mismatched finishes, brass and
oxidised bronze fittings, heavy webbing, rope, boot leather.

Muted and practical — charcoal, ash grey, weathered black, faded olive, dust
brown, sand, bone white, with rust red and ochre as secondaries and brass used
sparingly.

Every swatch is good quality and well kept. **Nothing here is a matched set:** it
is the material vocabulary four different people drew from independently.

## 13. `tone-collage.png` — the share sheet

**Tall portrait, 2:3.**

**Not a board asset.** This is the one image to send someone on a phone when
they ask what these characters look like. It is a tone and casting reference for
quick sharing, never a costume authority — nothing is ever matched against it.

A single image divided into SIX panels in an irregular contact-sheet layout —
uneven panel sizes, hard white gutters between them, no captions, no text, no
numbering. One large panel carries the sheet; the rest are supporting sizes.

Because this character is four people rather than one, the panels show the crew
rather than an individual:

1. All four together, full figure, open daylight.
2. The large one alone, showing scale against a tree.
3. A tight portrait of the near-human, markings legible.
4. The rifle and the close one working together at distance.
5. The hold at night under one work lamp, figures small.
6. A detail: braided fur, a notched stock, a trophy, a kept object.

The four builds must be identical to their turnaround views in every panel — same
gear, same marks, same sides. Panels that disagree with each other have failed,
however good they look individually.

---

## Output checklist

| Slot | File | Ratio | What it proves |
|---|---|---|---|
| 1 | `lineup.png` | 2:1 | **Four individuals, not one costume** |
| 2 | `sabacc.png` | 16:9 | **Interior — the ship's hold.** They still separate under one work lamp |
| 3 | `pursuit.png` | 16:9 | They work as a crew without being a unit |
| 4 | `kit-heads.png` | 3:1 | Four answers to the head |
| 5 | `kit-harness.png` | 3:1 | Four answers to carrying |
| 6 | `kit-plating.png` | 3:1 | Partial armour, placed differently |
| 7 | `kit-boots.png` | 3:1 | The class-not-item rule |
| 8 | `kit-marks.png` | 3:1 | What makes them people |
| 9 | `bandolier.png` | 1:1 | The grenade can be reached |
| 10 | `heavy-fur.png` | 1:1 | A specific elderly individual |
| 11 | `nearhuman-markings.png` | 3:4 | Make-up only, holds a close-up |
| 12 | `materials.png` | 1:1 | One vocabulary, no matched set |
| 13 | `tone-collage.png` | 2:3 | Shareable, never authoritative |

Plus **20 turnaround plates** — four builds by five views — from
`prompts/turnarounds/`.

---

## Continuity rules across the set

- **The four builds never change between images.** Same gear, same marks, same
  sides, same relative heights.
- **Nothing is mirrored on anyone.** All four are right-handed.
- **No two builds acquire a shared feature.** If a second long coat, a second
  helmet or a second long gun appears, the image is wrong.
- **The large one is always the largest thing in frame**, and the grenades are
  always visible on the front of his bandolier.
- The near-human is **always make-up only** — no appliance appears in any image.

---

## Open questions blocking this character

- No build has an `approved.reference` yet. The front turnarounds have to be
  generated and approved before the slots above can attach a costume reference.
- What does the large one's suit cost across the added Scene 10 and pursuit days?
- Exact skin tone and marking geometry for the near-human — muted green-gold or
  desaturated blue, and what the markings mean.

---

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 0.2 | 2026-07-31 | ready | Rewritten from scaffold: kit constants for all four builds, eight character-specific rejections, thirteen slots built around the line-up. Capture, anti-synthetic and costume-rule applicability set. |
| 0.1 | 2026-07-30 | scaffold | Placeholder pack. |
