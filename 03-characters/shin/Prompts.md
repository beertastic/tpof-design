---
title: "Shin — Image Prompt Pack"
asset_id: "CHAR-SHIN"
version: "1.0"
status: "ready"
faction: "Slaves / Escapees"
governing_documents:
  - ../../01-production-design/Production-Design-Bible-v1.0.md
  - ../../04-factions/slaves-escapees/Faction.md
  - Character.md
  - Character-Lock.md
---

# Shin — Image Prompt Pack

**Before you start:** if actor reference images exist, **attach them to the
conversation** — see [`../CAST-REFERENCE.md`](../CAST-REFERENCE.md). A repository
connector may not let the model see images even when it can read this file. The
reference governs face and build; this pack governs everything else.

> **Start with the costume turnarounds — they are the primary deliverable.**
> 15 paste-ready prompts in [`prompts/turnarounds/`](prompts/turnarounds/).
> Generate those in full before any image in this document. Regenerate with
> `python tools/prompt-splitter/turnarounds.py shin`.
>
> **The slots below are plates and mood images.** Three or four mood images is
> enough — they are context, not something anyone builds from.
>
> **Pre-assembled versions of the slots below are in [`prompts/`](prompts/).** One
> plain-text file per image, each fully self-contained — open it, select all,
> paste. No sections to gather, no markdown to strip. Generated from this
> document; if you change anything here, run
> `python tools/prompt-splitter/split.py shin`.

**How to use** (if assembling by hand)**.** Each numbered slot is a complete, self-contained prompt. Paste
**Style**, **Do Not**, **Character Constants**, then the single slot you want.
Do not paste more than one slot at a time. Save the result to the exact filename
given, in `03-characters/shin/source/artwork/`, then run:

```bash
python tools/board-generator/generate.py shin
```

Every rule needed is written out below. Nothing here depends on reading another
file first.

---

## Style — paste with every prompt

Live-action Star Wars production still. Outer Rim frontier realism in the manner
of the original trilogy and *Andor*, with a subtle *Mandalorian* frontier
aesthetic. Photographic, not illustrative.

This is a galaxy built from industrial salvage. Nothing is factory fresh. Every
object has had a previous owner and carries visible history: repairs, patches,
fading, grime, wear.

Costume is functional and real — buildable construction, believable seams and
fastenings, nothing decorative. Coarse woven cloth, undyed or badly dyed,
hand-repaired.

Palette muted, sun-faded, practical — charcoal, ash grey, weathered black, faded
olive, dust brown, sand, bone white.

Lighting motivated by believable sources only: overcast daylight, dawn, dusk,
firelight, a dying fire.

Camera: naturalistic composition over heroic posing. Restrained colour grade,
subtle atmospheric haze, realistic depth of field, fine film grain, practical
lens behaviour. The world feels much larger than the people within it.

---

## Do Not — paste with every prompt

No Caribbean or Earth pirate costume, Renaissance, medieval or Victorian
clothing, fantasy armour, or modern tactical gear.

No pristine surfaces, no clean clothing, no styled or salon hair.

**Absolutely no sexualisation.** The subject is a fifteen-year-old child. No
fitted or shaped costume, no exposed midriff or shoulders as design language, no
artful tearing, no glamour lighting, no adult posing, no makeup. This rule
overrides every other consideration in this pack.

Not a warrior. No weapon, no armour, no fighting stance, no confidence, no
capability. No robes, no lightsaber, nothing Jedi.

No glowing eyes, no visible magic, no energy effects on the character.

No text, logos, watermarks, captions or labels. No crushed blacks.

Photographic realism only: no anime, no cel shading, no painterly illustration,
no 3D-render look, no plastic skin.

---

## Realism — paste with EVERY prompt, without exception

This is a photograph. A real image, made with a real camera, of real physical
objects, under real light. It is not a render, not an illustration, not concept
art, and not a picture that looks like it was generated.

Every surface is a real material behaving like one: weave visible in cloth, grain
in leather, tool marks and micro-scratches in metal, dust settled in crevices,
moisture where it would collect. Nothing is perfectly clean, perfectly even or
perfectly smooth.

Physical imperfection throughout — dust, fingerprints, scuffs, uneven wear,
slight asymmetry, threads out of place, edges that are not quite straight.

Real optics and real capture: genuine lens behaviour, natural highlight rolloff,
fine photographic grain present in the image rather than added on top.

Reject entirely the look of computer-generated imagery — the smooth,
evenly-lit, uniformly-detailed, faintly plastic quality of a render. If the
result looks manufactured rather than photographed, it has failed.

---

## Capture — NARRATIVE slots only

> **Paste with slots 1, 2, 3, 4, 5, 7, 12** — in-scene frames.
>
> **Do NOT paste with reference plates** (8 (expression strip), 9–11, 13). Those want flat, even
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

> **Paste with slots 1, 2, 3, 4, 5, 6, 7, 8, 12.** Wider than the Capture block: a portrait study or
> an expression strip is lit flat and sharp, but the skin still has to be real.
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

## Character Constants — paste with every prompt

Shin. Human girl, **fifteen years old**. An escaped captive fleeing through a
forest world with her mother and a small band of prisoners, hunted by mercenaries.

Slight and underfed — a child who has not had enough food for a long time. Not
athletic, not frail. Pale skin. Young, open face, easily read; she has never had
to hide what she feels from anyone.

**Long red hair — the only strong colour anywhere in this film.** Bound, braided
or wrapped back for practicality, never loose and never styled. It catches what
little light there is. It should be filthy and progressively more damaged as the
story runs. Pretty, never sexy.

Her face and hands are dirt-smeared. Her hands are small and work-marked — she
has been used for labour, never for fighting.

She wears captivity clothing: a coarse, unfitted, badly-dyed tunic and top,
hand-repaired by her mother, wrong-sized and worn to destruction on the run. Her
footwear was never meant for a forest and is failing. Nothing she wears was made
for her or chosen by her.

She carries nothing. She is exhausted, frightened, filthy, and being protected by
people who love her. She is a child in the middle of an adult catastrophe.

---

# Prompt slots

## 1. `portrait.png` — hero portrait
**Tall portrait, 9:16.**

Waist-up portrait of Shin in a dim forest at dusk, three-quarter angle, caught
mid-movement and looking off past camera. Fifteen, slight, pale, dirt-smeared.
Long red hair bound back and dull with grime — the only colour in an otherwise
charcoal and dust-brown frame. Coarse unfitted captivity clothing, hand-patched.
Overcast light through wet canopy. She is frightened and trying not to show it,
and not quite managing. Not posed, not heroic, not composed.

## 2. `forest.png` — the run
**Tall portrait, 9:16.**

Full-figure shot of Shin running through dense wet forest at dusk among other
fleeing figures, mid-stride, hair bound and whipping, one arm up against
branches. Read her as small and young against the scale of the trees. Mud, leaf
litter, mist between trunks. She is not running like a fighter — she is running
like a frightened child who has been running for a long time. Her red hair is
the one thing findable in the murk.

## 3. `sky.png` — marvelling
**Tall portrait, 9:16.**

Shin standing still in a forest clearing at dusk, head tilted right back,
**looking up at the open sky** with unguarded wonder on her filthy face. Around
and behind her, other exhausted escapees have slumped down and are not looking at
anything. She is the only one looking up. Soft dusk light falling on her upturned
face and catching in her red hair. This is the only moment of joy in the film and
it belongs to a child who has almost nothing.

## 4. `camp_night.png` — cannot sleep
**Tall portrait, 9:16.**

Shin at a makeshift forest camp at night, lit only by a dying fire. She is
awake, sitting up, arms around her knees, staring at nothing. Her face is
dirt-smeared and hollow with exhaustion. Beside her, her mother sleeps — pale,
sweaty, brow creased in pain even asleep. Low warm firelight raking across
Shin's face and picking out the red in her bound hair. She is exhausted beyond
description and she is not sleeping, because she is afraid of what happens when
she closes her eyes.

## 5. `mother.png` — carrying Jeyin
**Tall portrait, 9:16.**

Shin at dawn supporting her injured mother through the forest, her mother's arm
across her shoulders, taking weight she is too small to take. Early grey morning
light, mist between the trunks. Both are filthy and exhausted. The composition
must read as the child carrying the parent. Shin's face shows effort and fear;
her mother is concealing how bad it is.

## 6. `detail_portrait.png` — the face
**Portrait, 3:4.**

Close portrait of Shin, head and shoulders, in soft overcast daylight. Fifteen
years old — the face must read unmistakably as a child, not a young adult. Pale
skin under a layer of dirt, freckles if the actor has them, chapped lips,
shadows under the eyes from days without sleep. Long red hair bound back off her
face, dull and matted, a few strands loose and stuck to her skin. Her expression
is open and frightened — she is very bad at hiding things. Practical realism:
every pore, every smear of dirt. No makeup, no styling, nothing softened.

## 7. `vision_shadow.png` — the manifestation
**Wide banner, 21:9.**

Wide shot: Shin running through dark forest with other figures, and **a pulsing
shadow gathers around her** — a darkening of the air itself, light bending away,
the undergrowth around her going dim while the rest of the frame stays lit.
Not smoke, not energy, not a visual-effects glow. An absence. It is leaking out of
her, not being produced by her — nothing about it may look aimed or intended. She does not know
it is happening and her expression shows only terror at being chased. The other
figures do not appear to notice. Her red hair remains the one point of colour
inside the darkening.

## 8. `expression_strip.png` — performance range
**Landscape, 16:9.**

Horizontal strip of four head-and-shoulders expressions of the same
fifteen-year-old face, evenly lit and consistently framed: (1) open wonder,
looking up; (2) horror at something she has just been told; (3) hollow sleepless
exhaustion; (4) grief — total, unguarded, the face of a child who has just lost
everything. Same lighting, angle and scale in every panel. Dirt-smeared
throughout. Nothing performed or restrained: this face shows everything.

## 9. `clasp.png` — the hero prop
**Wide banner, 3:1.**

Product-reference layout on a neutral surface, evenly lit: a small metal clasp —
a functional fastener, not jewellery — shown from two angles with its mechanism
visible. It has been used constantly for years: worn smooth and bright at the
contact points, dulled and slightly tarnished elsewhere, with fine scratching
from handling. Sturdy, plain and well-made in the way of an object that has
outlived several owners. No gems, no engraving, no ornament, no shine. Small
enough to close a hand around. This object has to carry an entire relationship,
so it must be specific and memorable in silhouette.

## 10. `hair_study.png` — the hair
**Square, 1:1.**

Reference study of the character's hair: three or four views on a neutral,
evenly lit background showing how the long red hair is bound, braided and
wrapped back for a forest run — from behind, from the side, and a close crop of
the binding itself. Practical and unglamorous, tied with cord or torn cloth
rather than anything made for the purpose. Dirty, matted, with loose strands
escaping. This is a hair-and-makeup reference, not a beauty shot. The colour must
be consistent and repeatable — it is the only strong colour in the film.

## 11. `utility.png` — what she carries
**Square, 1:1.**

Overhead flat-lay on a worn surface of everything Shin has in the world: her
failing footwear, a strip of cloth used as a hair tie, a scrap of rag, perhaps a
water container that is not hers, and the small metal clasp. Even flat reference
lighting. **The emptiness is the point.** This is not a kit — it is the few
objects that happen to be on a fleeing child, and it should look shockingly
insufficient laid out against a mercenary's equipment.

## 12. `ditch.png` — hiding
**Tall portrait, 9:16.**

Shin pressed into a muddy forest ditch, low, curled small, being physically held
down and shielded by an older woman's arm across her back. Wet earth, tangled
roots, standing water. Morning light above but almost none reaching them. Her
face is turned up and sideways, filthy, wide-eyed, listening. Absolute terror
held completely silent. She is as small as she can make herself.

## 13. `materials.png` — materials and palette
**Landscape, 5:4.**

Materials reference board: physical swatches and close details on a neutral
surface, evenly lit. Coarse undyed woven cloth; badly-dyed fabric gone patchy;
hand-stitched repairs in mismatched thread; frayed hems; failing footwear leather
with a split sole; cord and torn cloth used as ties; mud, damp and staining; the
small metal clasp at one corner; and a lock of the red hair for colour matching.
Palette held to charcoal `#2B2A26`, ash brown `#3A352F`, dust brown `#544E42`,
leather `#6B5A47`, faded tan `#7C6F5B`, faded olive `#4F563F`, weathered black
`#2E2F33`, natural bone `#BDAF95` — **plus the hair, which is the only saturated
colour permitted anywhere in this film.** Matte throughout. The repairs must
read as done by hand, in poor light, by someone who cared.

---

## Output checklist

| # | File | Ratio |
|---|---|---|
| 1 | `portrait.png` | 9:16 |
| 2 | `forest.png` | 9:16 |
| 3 | `sky.png` | 9:16 |
| 4 | `camp_night.png` | 9:16 |
| 5 | `mother.png` | 9:16 |
| 6 | `detail_portrait.png` | 3:4 |
| 7 | `vision_shadow.png` | 21:9 |
| 8 | `expression_strip.png` | 16:9 |
| 9 | `clasp.png` | 3:1 |
| 10 | `hair_study.png` | 1:1 |
| 11 | `utility.png` | 1:1 |
| 12 | `ditch.png` | 9:16 |
| 13 | `materials.png` | 5:4 |

All thirteen land in `03-characters/shin/source/artwork/`. The board generator
places images with a **contain** operation and never crops — the wrong ratio
letterboxes the board. Then:

```bash
python tools/board-generator/generate.py shin --validate
python tools/board-generator/generate.py shin
```

## Continuity rules across the set

- Same face, same age read, in every image. Fifteen, never older.
- **Hair colour must be identical across all thirteen.** It is the film's only
  saturated colour and any drift between images will be obvious.
- Hair is bound in every image. It gets dirtier and more damaged, never cleaner.
- Same single costume throughout, progressively more destroyed.
- The clasp appears only from Scene 22 onward — it must not be visible in slots
  1–5, 7 or 12.
- She carries no weapon in any image, ever.
- She never looks capable, composed or dangerous.

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 1.0 | 2026-07-30 | ready | Initial prompt pack derived from locked character. |
