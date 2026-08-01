---
title: "Baylan — Image Prompt Pack"
asset_id: "CHAR-BAYLAN"
version: "1.2"
status: "ready"
faction: "Mercenaries"
governing_documents:
  - ../../01-production-design/Production-Design-Bible-v1.0.md
  - ../../04-factions/mercenaries/Faction.md
  - Character.md
  - Character-Lock.md
---

# Baylan — Image Prompt Pack

**Before you start:** if actor reference images exist, **attach them to the
conversation** — see [`../CAST-REFERENCE.md`](../CAST-REFERENCE.md). A repository
connector may not let the model see images even when it can read this file. The
reference governs face and build; this pack governs everything else.

> **Start with the costume turnarounds — they are the primary deliverable.**
> Twenty paste-ready prompts in
> [`prompts/turnarounds/`](prompts/turnarounds/): **one costume, five views.**
> Generate those in full before any image in this document. Regenerate with
> `python tools/prompt-splitter/turnarounds.py baylan`.
>
> **The slots below are plates and mood images** — props, materials, expression
> range, and a few atmospheric frames. Three or four mood images is enough; they
> are context, not something anyone builds from.
>
> **Pre-assembled versions of the slots below are in [`prompts/`](prompts/).** One
> plain-text file per image, each fully self-contained — open it, select all,
> paste. No sections to gather, no markdown to strip. Generated from this
> document; if you change anything here, run
> `python tools/prompt-splitter/split.py baylan`.

**How to use** (if assembling by hand)**.** Each numbered slot below is a complete, self-contained prompt.
Paste **Style**, **Do Not**, **Character Constants**, then the single slot you
want. For narrative slots, add **Capture** and **Anti-synthetic** as well — see
the note on those blocks for which slots they apply to. Do not paste more than one slot at a time. Save the result to the exact
filename given, in `03-characters/baylan/source/artwork/`, then run:

```bash
python tools/board-generator/generate.py baylan
```

Every rule needed is written out below. Nothing here depends on reading another
file first.

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
Materials: ballistic weave, quilted flight fabric, reinforced synth-leather,
flexible armour mesh, woven technical textiles, plastoid plates, insulated work
fabric, industrial rubber, brushed alloy.

Palette muted, sun-faded, practical — charcoal, ash grey, weathered black, faded
olive, dust brown, sand, bone white. Accents (brass, copper, oxidised bronze)
used sparingly. Bright colour only for rank, warning markings or a significant
personal item.

Lighting motivated by believable sources only: natural sunlight, overcast sky,
work lamps, bulkhead fixtures, warning lights, control panels, firelight,
glowrod.

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

**Baylan-specific rejections.**

- **His dark robe must read as a heavy weathered coat, never as Jedi dress.** No
  wide monastic sleeves, no ceremonial drape, no cowl, no hood-up mystique.
  **There are no Jedi robes anywhere in this pack** — the separate Scene 12 build
  was dropped on 2026-08-01 and he wears his working dress in the vision.
- **No visible lightsaber and no hilt on his belt, in any image.** The blaster is
  the hilt, and it is never ignited in any prompt.
- **Not a wise mentor.** Not serene, not teaching, not at peace.
- **Not a ranking officer.** He is a subordinate who stands at the back.
- **Not athletic or agile.** Late forties, thickened, slow.
- **No ornament** — no trophies, faction colours, insignia or jewellery beyond
  the hidden cord.
- **No distinguished silver mane.** Iron-grey, short, badly cut by his own hand.
- Nothing tailored, clean or authoritative. He is nobody, and he has worked hard
  to be.

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

> **Paste with slots 1, 2, 3, 4, 6, 11, 13** — in-scene frames.
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

> **Paste with slots 1, 2, 3, 4, 5, 6, 7, 11, 13.** Wider than the Capture block: a portrait study or
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

Baylan. Human male, late forties. A Jedi Knight who survived Order 66, tried
and failed to keep being a Jedi on the Outer Rim, gave up, and has spent years
since hiding inside a mercenary crew — where he is, for the first time in his
life, safe. Nobody in the crew knows what he is.

Tall and broad, thickened through the middle and shoulders — he was powerful once
and is merely large now. Iron-grey hair, short, cut by himself or a crewmate
rather than anyone skilled. Full unshaped beard, grown to be left alone. Deep
lines around the eyes from squinting into distances and from eighteen years of
not sleeping properly. Heavy working hands: scarred, thickened knuckles, split
nails, ingrained dirt.

He wears salvaged, repaired mercenary workwear that has genuinely worked —
layered technical cloth and worn synth-leather over a heavy work shirt, a padded
jacket re-shouldered at least once, a functional harness carrying ammunition and
tools, heavy resoled boots. Muted charcoal, ash brown, dust brown, faded olive
throughout. No ornament, no faction marking, no trophies, no personal flourish.
In a crew that decorates itself, his plainness is the only unusual thing about
him — and it reads as a dull man rather than a hiding one.

He often wears a **long, heavy, dark robe** — weathered black or near it — that he
has had since before, and which has been through at least one real fight:
repaired tears, scorching, a burn never properly patched. It reads as an ordinary
weather cape or heavy coat, not as Jedi dress: no wide monastic sleeves, no
ceremonial drape, no hood-up mystique. It is visibly the most comfortable thing
he owns and the only object he keeps because he likes it. He wears it off duty,
at the fire and in the cold; less when working or on patrol.

Under everything he wears one further surviving garment: a dark undertunic of an
older, finer weave, re-dyed years ago and patched so often the original fabric
survives only in panels. Across its chest run four or five nested chevrons with
the apex pointing downward — raised panels of matte suede-like leather appliqued
onto the woven base and stitched at the edges, widest at the shoulders and
narrowing toward the sternum, sitting slightly proud of the cloth. Dark on dark:
the pattern reads through texture and shadow, never through colour contrast. A
standing collar sits above it. This is construction, not decoration — layered
overlapping panels that read as padding. Visible only at the collar and cuff, or
when he is in shirtsleeves.

On a cord around his neck, under the shirt and against the skin, hangs a small
worn leather pouch containing a raw, jagged yellow crystal.

He looks like a man who could still do serious damage and would strongly prefer
not to. He moves heavily and slowly and has spent years practising being
uninteresting — but he can be still in a way nobody else can. Around this crew he
is genuinely at ease, and that ease is not part of the performance.

---

# Prompt slots

## 1. `forest.png` — in the mercenary camp
**Tall portrait, 9:16.**

Full-figure shot of Baylan carrying a crate or coil of cable through the forest
mercenary camp at dusk — manual labour, unglamorous, the work of a man who is
told what to do. Tents, tarpaulins, crates, a campfire further back. His full
silhouette readable: big, heavy, slightly stooped under the load. Boots in wet
leaf litter. He belongs here completely and looks like nobody worth watching.
Natural overcast dusk with firelight spill from behind.

## 2. `industrial_a.png` — standing at the back
**Tall portrait, 9:16.**

Baylan standing motionless at the back of a group, slightly apart, while others
in front kneel or check their gear. He is doing nothing — hands at his sides,
weight settled, watching. Early morning grey light in a forest camp. Everyone
else is in motion and he is completely still, and the stillness is the subject of
the image. Read him as the oldest person present. No authority, no rank, no
insignia — he is simply not participating in the way the others are.

## 3. `industrial_b.png` — the storage area
**Tall portrait, 9:16.**

Baylan alone at night in a makeshift storage area among stacked crates, spare
ammunition boxes and a tarpaulin, lit by a single work lamp. He is standing very
still with one hand slightly raised and open, entirely focused, and a small rock
hangs in the air a short distance from his palm. This is the only image in which
he is not performing — his posture, his shoulders and his face have all changed.
Absolute concentration on a very small thing. No glow, no energy effect, no
visual magic: the rock is simply, impossibly, hanging there.

## 4. `industrial_c.png` — in his bunk
**Tall portrait, 9:16.**

**INTERIOR — the mercenary ship's crew bunks.** Scenes 13 and 15 moved inside on
2026-08-01.

Baylan seated cross-legged on his bunk at night, lit low and warm by a glowrod
set down beside him. He is in shirtsleeves — jacket and harness off, work shirt
open at the collar, the patched dark undertunic visible underneath. His long dark
robe is around his shoulders like a blanket. A cord runs around his neck and
disappears into the shirt. His rifle propped in the corner.

A cramped salvaged berth with **bunks packed in too close together** — exposed
pipework, tie-downs, scuffed decking, someone else's kit within arm's reach.
Other crew asleep nearby, out of focus. Not a cabin, not private: this is a
freighter carrying more people than it was built for.

Quiet and exhausted, and **the point of the image is that he has nowhere to be
unguarded.** He has hidden for eighteen years in a space where you cannot get
away from anyone.

## 5. `detail_portrait.png` — the face
**Portrait, 3:4.**

Close portrait of Baylan, head and shoulders, lit at a grazing angle by overcast
daylight. The subject of this image is eighteen years of not sleeping. Deep
creases at the eyes, weathered skin, iron-grey stubble running into a full
unshaped beard, hair cropped short and unevenly by his own hand. His expression
is neutral and absolutely unreadable — he has spent two decades giving nothing
away. But the eyes are older than the rest of him. Practical make-up realism,
every pore and broken capillary present. No costume detail competing.

## 6. `vision_dune.png` — the dune
**Wide banner, 21:9.**

Wide, hazy vision-image: a lone figure standing atop a sand dune under a hard
afternoon sky, sea visible far beyond, gazing out. **He is in his ordinary
working dress — the same costume as every other slot.** No robes, no tabards, no
Jedi dress of any kind; the separate Knight build was dropped on 2026-08-01. His
long dark coat may be on him, worn open and moving in the wind.

He is turning toward camera, caught mid-movement, as if something behind him has
just made a noise. Blown sand, heat shimmer, a bleached and desaturated palette
utterly unlike the wet forest.

**The script's word is "hazy", and the man is one "we can't quite make out" — so
resist resolving him.** Distance, glare, heat shimmer and grain are all doing
work here. This is the one image in the pack that is allowed to be soft,
over-bright and unreal at the edges, and it should not read as a costume plate.
He is *slightly* less worn than in the forest slots — the script says "a few
years younger and less haunted" — but it is the same man in the same clothes and
nothing should announce a time jump.

## 7. `expression_strip.png` — performance range
**Landscape, 16:9.**

Horizontal strip of four head-and-shoulders expressions of the same
late-forties bearded face, evenly lit and consistently framed: (1) neutral
blankness — the manufactured dull expression he wears in company; (2) waking in
terror, gasping, sweating, eyes wide; (3) quiet grief, entirely private and
contained; (4) the real man underneath — focused, dangerous, absolutely still.
Same lighting, angle and scale in every panel. The strip should show how little
he lets show, and then how much is there.

## 8. `blaster.png` — the converted lightsaber
**Wide banner, 3:1.**

Product-reference layout on a neutral surface, evenly lit: a heavily modified
blaster pistol shown assembled at left and partially disassembled at right, its
components laid out in order.

This weapon was built from a lightsaber. The conversion is genuine, not cosmetic
— the emitter shroud has become the barrel shroud, the activation plate has
become the trigger housing, and a belt clip is still fitted because it was never
removed. In the disassembled view the original hilt architecture is unmistakable:
a machined cylindrical core, control studs blanked over with plate, and an empty
crystal chamber at its heart, now holding a power cell.

Assembled, it should read to a casual eye as an ugly, over-modified sidearm that
someone has bodged together — nothing more. Weathered, scratched, matte, with
eighteen years of handling on the grip. No ornament, no engraving, no glow.

## 9. `crystal.png` — the pouch
**Square, 1:1.**

Close product-reference image on a dark neutral surface, lit low and warm as if
by a single glowrod: a small, worn leather pouch, opened, with a fine cord
threaded through it; beside it a small, jagged, raw yellow crystal resting on the
leather. The crystal is uncut and irregular — a rough natural stone, not a
faceted gem and not a finished component. It has a faint internal warmth rather
than a glow. The pouch is old, soft, darkened by skin contact and repaired at one
seam. These two objects are the only things he owns from before.

## 10. `utility.png` — kit layout
**Square, 1:1.**

Overhead flat-lay of Baylan's carried kit on a worn surface: a battered heavy
rifle, the modified blaster in its holster, a handheld scanner, ammunition, a
folded bed roll, a few field tools, a water container, a repair kit. Everything
plain, worn and functional; nothing decorated, nothing personal, nothing kept for
sentiment. Even flat reference lighting. The point of this image is how
characterless it is — this is the kit of a man who has deliberately owned nothing
that says anything about him. The pouch and cord are not here; they are on his
body.

## 11. `maintenance.png` — the reconstruction
**Tall portrait, 9:16.**

Baylan seated cross-legged on his bunk aboard the ship at night, glowrod set
down beside him, the other crew asleep around him, in shirtsleeves. He holds the small jagged yellow crystal in his open palm. In front
of him, unsupported, the components of his blaster hang separated in mid-air —
and they are **drawing back together into a different shape**: a machined
cylindrical lightsaber hilt, mid-assembly, its parts converging. The crystal has
not gone in yet.

He is not triumphant and not afraid. He is looking at it the way a man looks at
something he could not bear to look at for years — and has just found he can.
There should be hesitation in him, and then decision.

Warm low glowrod light, deep shadow, the cramped berth close around him and
sleeping crew just out of the light. No glow effects,
no energy, no magic — only objects hanging in the air that should not be, and
assembling themselves.

## 12. `materials.png` — materials and palette
**Landscape, 5:4.**

Materials reference board: physical swatches and close details on a neutral
surface, evenly lit. Coarse insulated work fabric; worn reinforced synth-leather
with visible stitching and repair; quilted padding at a re-shouldered seam; a
patched dark undertunic panel showing an older, finer weave with a cross-wrapped
edge and a shaped shoulder; weathered matte metal hardware; harness webbing;
boot leather, resoled; a panel of the heavy dark robe cloth showing a repaired
tear and an unpatched scorch. A short length of worn neck cord and a scrap of
soft old pouch leather at one corner. Palette held to charcoal `#2B2A26`, ash brown
`#3A352F`, dust brown `#544E42`, leather `#6B5A47`, faded tan `#7C6F5B`, faded
olive `#4F563F`, weathered black `#2E2F33`, natural bone `#BDAF95`. Matte
throughout, nothing reflective. The undertunic panel must be visibly a finer,
older cloth than everything surrounding it.

---

## 13. `tone-collage.png` — the share sheet

**Tall portrait, 2:3.**

**Not a board asset.** This is the one image to send someone on a phone when
they ask what this character looks like. It is a tone and casting reference for
quick sharing, never a costume authority — nothing is ever matched against it.

A single image divided into SIX panels in an irregular contact-sheet layout —
uneven panel sizes, hard white gutters between them, no captions, no text, no
numbering. One large panel carries the sheet; the rest are supporting sizes.

The same person in the same costume in all six, photographed across one day.
Vary only setting, light, framing and action:

1. A full-figure standing shot in open daylight — the whole costume legible.
2. A tight portrait, head and shoulders, eyes off camera.
3. A mid shot at work, hands doing something specific.
4. A low-light frame — dusk, firelight or a work lamp — showing how the costume
   reads when it goes dark.
5. A wide frame where the environment dominates and the figure is small.
6. A detail: hands, a weapon, a fitting, a worn edge.

CONTINUITY IS THE POINT OF THIS IMAGE. The costume, the hardware, the hair and
the face must be identical in every panel — same garment, same fastenings, same
metal in the same places on the same sides. Panels that disagree with each other
have failed, however good they look individually. If an asymmetric item sits on
one side in one panel it sits on that same side of the body in all six.

Every panel obeys the costume rules above. The rules do not relax because a
panel is small.

---

## Output checklist

| # | File | Ratio |
|---|---|---|
| 1 | `forest.png` | 9:16 |
| 2 | `industrial_a.png` | 9:16 |
| 3 | `industrial_b.png` | 9:16 |
| 4 | `industrial_c.png` | 9:16 |
| 5 | `detail_portrait.png` | 3:4 |
| 6 | `vision_dune.png` | 21:9 |
| 7 | `expression_strip.png` | 16:9 |
| 8 | `blaster.png` | 3:1 |
| 9 | `crystal.png` | 1:1 |
| 10 | `utility.png` | 1:1 |
| 11 | `maintenance.png` | 9:16 |
| 12 | `materials.png` | 5:4 |

All thirteen land in `03-characters/baylan/source/artwork/`. The board generator
places images with a **contain** operation and never crops — supplying the wrong
ratio produces letterboxing on the board. Then:

```bash
python tools/board-generator/generate.py baylan --validate
python tools/board-generator/generate.py baylan
```

## Continuity rules across the set

- Same face, same build, same beard and haircut in **every** image, slot 6
  included. One costume across the whole pack.
- **There are no Jedi robes in this pack at all.** The only garment that could be
  mistaken for one is his long dark coat, and every slot that shows it says so.
- The blaster on his hip in slots 1–3 is the same object as in slots 9 and 12.
- Every component visible in the reconstructing hilt (slot 12) was visible on the
  assembled blaster (slot 9). Same object, different arrangement.
- The cord at his neck in slots 5 and 12 leads to the pouch in slot 10.
- The undertunic in slots 5, 12 and 13 is the same garment, same patches.
- He gains no ornament, insignia or decoration between images. Ever.
- He is never framed heroically and never looks powerful — until slot 12.

## Scene plates — beyond the board set

Not part of the five-board package; generate as needed for the finale.

### F1. The first ignition
**Any ratio.** Forest clearing, morning. Baylan standing among mercenaries,
igniting a **yellow** lightsaber blade for the first time in eighteen years.
(It ignites yellow and finishes the scene orange — see F2.) He
is not posed heroically and not shouting. His face is almost blank. The mercenary
nearest him has not yet understood what he is looking at. Overcast morning light;
the blade is the only saturated colour besides Shin's hair. Still-swirling smoke
from a crashed ship in the background.

### F2. The blade changes
**Wide banner, 3:1.** Close on a lightsaber blade being drawn slowly out of a
man's chest in a forest clearing. The blade **enters yellow and emerges orange** —
the change happening across the withdrawal, not as a cut. The wounded man is a
mercenary in his forties, dazed, his kit scorched and torn down one side from a
grenade blast, hands still half-raised. Overcast morning light. The only
saturated colour in frame is the blade. Held, slow, quiet — no motion blur, no
heroic angle, no spectacle.

### F3. Leaving
**Tall portrait, 9:16.** Baylan and Shin walking out of the forest clearing
together, seen from behind or in profile at middle distance. He is damaged; his
outer layers are torn or gone and the patched dark undertunic is visible. She is
fifteen, filthy, covered in her mother's blood, hair intact. They are not
touching and not talking. The clearing behind them is out of focus. Grey morning
light. This is the last image of the film and the first image of the next.

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 1.2 | 2026-07-31 | ready | Robe added to Character Constants, slots 1, 5 and 13, and the rejection list. |
| 1.1 | 2026-07-30 | ready | Slot 12 rewritten as reconstruction, not disassembly. Finale scene plates added. |
| 1.0 | 2026-07-30 | ready | Initial prompt pack derived from locked character. |
