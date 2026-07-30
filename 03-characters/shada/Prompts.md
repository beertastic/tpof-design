---
title: "Shada — Image Prompt Pack"
asset_id: "CH-006"
version: "1.0"
status: "ready"
faction: "Mercenaries"
governing_documents:
  - ../../01-production-design/Production-Design-Bible-v1.0.md
  - ../../04-factions/mercenaries/Faction.md
  - Character.md
  - Character-Lock.md
---

# Shada — Image Prompt Pack

**How to use.** Each numbered slot below is a complete, self-contained prompt.
Paste **Style**, **Do Not**, **Character Constants**, then the single slot you
want. Do not paste more than one slot at a time. Save the result to the exact
filename given, in `03-characters/shada/source/artwork/`, then run:

```bash
python tools/board-generator/generate.py shada
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
decorative technology. No gadget overload. No datapad.

No glamour posing, no sexualisation, no fashion-editorial lighting.

No text, logos, watermarks, captions, labels or lettering in the image.

No crushed blacks — the silhouette must stay separated from the background.

Photographic realism only: no anime, no cel shading, no painterly illustration,
no 3D-render look, no plastic or waxy skin.

**Shada-specific rejections.** Not a generic human scavenger with no serpentine
ancestry. Not fully reptilian or a full creature design. Not a heavy-armoured
soldier. Not covered head-to-toe in a way that hides the scale language.

---

## Character Constants — paste with every prompt

Shada. Female mercenary assassin, thief, scout and tracker. Compact, agile
build, small beside most of the crew. Mostly human in appearance with subtle
inherited serpentine ancestry.

Fine, subtle scales on face, neck, collarbone, shoulders, arms and hands —
inherited detail, not a costume texture. Eyes carry a reptilian quality while
remaining expressive and recognisably human. Movement stays human, restrained
and economical.

Costume: light, fitted, scavenged armour protecting vital areas only. Layered
technical cloth, worn leather, repaired matte hardware. Practical harness, belt,
sheath, concealed holster. Functional exposed skin at shoulders, upper arms and
selected mobility zones — for movement, heat and sensory function, never
decorative or sexualised, and it is what makes the inherited scales legible.
Nothing polished, ornamental or factory fresh.

Equipment: compact blaster, well-used combat knife that never leaves her side,
small climbing and infiltration kit. Nothing else.

She is dangerous through precision, patience and observation rather than
physical dominance. She should look like someone who belongs in a forest even
when standing inside a starship.

---

# Prompt slots

## 1. `portrait.png` — hero portrait
**Tall portrait, 9:16.**

Waist-up portrait of Shada in an evening forest, three-quarter angle, her
attention caught by something off-frame to the left. Neutral alert expression —
assessing, not posing. Overcast evening light through wet canopy; soft rim light
separates her dark layers from the treeline. Fine inherited scales visible
across cheekbone, jaw, neck and collarbone, catching the light at a grazing
angle. Reptilian quality in the iris, human in the expression. Shoulders and
upper arms bare over a fitted scale-textured undersuit; light scavenged chest
and shoulder plating, worn matte. Knife sheath visible at the hip. Shallow depth
of field, forest falling into soft haze behind her.

## 2. `forest.png` — in-environment
**Tall portrait, 9:16.**

Full-figure shot of Shada moving low through dense wet forest at dusk, weight on
the balls of her feet, one hand steadying against a trunk. Not running —
deliberate, economical, mid-assessment. Read as small against the scale of the
trees. Mist between trunks, wet bark, leaf litter, standing water catching the
last light. Her dark layers stay separated from the background by wet rim
highlights and material contrast, never merging into black. Natural overcast
dusk only.

## 3. `industrial_a.png` — ship corridor
**Tall portrait, 9:16.**

Shada standing in a cramped, lived-in starship corridor — exposed pipework,
access panels, fasteners, mismatched paint, service markings, scuffed decking.
She is still, listening, weight settled, checking the corridor behind her. She
looks out of place in the metal environment in a way that reads as *forest
animal indoors*, not as costume mismatch. Lit by bulkhead fixtures and a warning
light — hard practical sources, no coloured drama. The scales on her arms and
neck pick up the cold industrial light differently from the surrounding metal.

## 4. `industrial_b.png` — crew space
**Tall portrait, 9:16.**

Shada in a cramped mercenary crew compartment, seated slightly apart from the
group, cleaning or checking a piece of kit. Warmer than the corridor — work lamp
and a screen glow, motivated only. Her posture is relaxed but her sightline
covers the hatch. Salvaged fittings, crates, worn webbing, personal repairs
visible on the surrounding surfaces. Costume layers readable: undersuit, harness,
plates, wraps. This is the one image where a trace of warmth shows.

## 5. `industrial_c.png` — cargo / hold
**Tall portrait, 9:16.**

Shada in a dim cargo hold checking an access route — hand on a stanchion,
looking up toward an overhead gap or duct, plotting a way through. Full body
visible, compact silhouette clear. Stacked salvage crates, tie-downs, fuel
staining, repaired plating. Single overhead work lamp with strong falloff, but
blacks stay open and her outline stays legible.

## 6. `scale_portrait.png` — species detail
**Portrait, 3:4.**

Close portrait of Shada, head and shoulders, turned slightly away, lit at a
grazing angle to reveal skin texture. The subject of this image is the
inheritance: fine scales across cheekbone, temple, jaw, neck and collarbone,
blending into human skin rather than stopping at a hard edge. Practical make-up
and prosthetic quality, not digital fantasy. Eyes visible, reptilian in
structure but expressive and human in intent. Soft overcast daylight. No
costume detail competing for attention.

## 7. `species_strip.png` — ancestry study
**Wide banner, 21:9.**

Horizontal study strip, three to four separate views across the frame on a
neutral, evenly lit background: scale detail on the back of the hand and
forearm; scale transition at the collarbone and shoulder; close eye detail
showing the reptilian iris structure; profile of the neck and jawline. Even,
flat reference lighting — this is a make-up and prosthetics reference, not a
dramatic image. Consistent skin tone and scale density across every view.

## 8. `expression_strip.png` — performance range
**Landscape, 16:9.**

Horizontal strip of four head-and-shoulders expressions of the same face,
evenly lit and consistently framed: (1) neutral alertness — the resting state;
(2) suspicion without panic; (3) focused assessment, narrowing in on a target;
(4) cold lethal calm. Restrained throughout — this face does not perform. Same
lighting, same angle, same scale detail in every panel. Reference-sheet
evenness, not four dramatic portraits.

## 9. `knife.png` — hero prop
**Wide banner, 3:1.**

Product-reference layout of a single combat knife on a neutral surface, lit
evenly. An old working blade, repeatedly sharpened — the edge profile visibly
reground and shortened over years. Grip wrapped and repaired with mismatched
cord. Silent, secure sheath shown alongside. This is a survival tool first and a
weapon second: it should read as something used daily for cutting rope, food and
cordage, not a fighting knife on display. Mechanically believable, no ornament,
no engraving, no jewelling.

## 10. `blaster.png` — hero prop
**Square, 1:1.**

Product-reference layout of a compact blaster pistol on a neutral surface, lit
evenly. Modified for reliability rather than power — replacement components,
mismatched finish, a field-repaired grip, worn bluing at the contact points.
Small enough to conceal and draw quickly. Mechanically believable construction
with visible fasteners and access. No oversized silhouette, no scope, no glowing
elements, no ornament.

## 11. `utility.png` — kit layout
**Square, 1:1.**

Overhead flat-lay of Shada's complete infiltration kit on a worn surface, laid
out in the deliberate order of someone who checks it after every mission:
climbing rope, lock picks, small field tools, spare blaster parts, cleaning kit,
wraps, a compact water container. Every item shows use and repair. Explicitly no
datapad and no unnecessary technology. Even, flat reference lighting. The
restraint of the kit is the point — this is a short list, well maintained.

## 12. `maintenance.png` — character at work
**Tall portrait, 9:16.**

Shada seated, cleaning and checking her blaster by work-lamp light, parts laid
out in a fixed habitual arrangement on the cloth beside her. Absorbed in the
task, not looking up. This is the image that says preparation is how she
controls fear. Hands and forearms prominent — scales visible, fingers precise.
Warm practical lamp light against a dim salvaged interior. Unhurried, ordinary,
routine.

## 13. `materials.png` — materials and palette
**Landscape, 5:4.**

Materials reference board: physical swatches and close details arranged on a
neutral surface, evenly lit. Flexible scale-textured mesh; worn reinforced
synth-leather with visible stitching and repair; coarse technical fabric;
weathered matte metal hardware; rope, patches, mud and patina. Palette held to
charcoal `#2B2A26`, ash brown `#3A352F`, dust brown `#544E42`, leather `#6B5A47`,
faded tan `#7C6F5B`, faded olive `#4F563F`, weathered black `#2E2F33`, natural
bone `#BDAF95`. Matte and low-noise throughout — nothing reflective. Dark values
must remain separable from one another by texture and value, never merging.

---

## Output checklist

| # | File | Ratio |
|---|---|---|
| 1 | `portrait.png` | 9:16 |
| 2 | `forest.png` | 9:16 |
| 3 | `industrial_a.png` | 9:16 |
| 4 | `industrial_b.png` | 9:16 |
| 5 | `industrial_c.png` | 9:16 |
| 6 | `scale_portrait.png` | 3:4 |
| 7 | `species_strip.png` | 21:9 |
| 8 | `expression_strip.png` | 16:9 |
| 9 | `knife.png` | 3:1 |
| 10 | `blaster.png` | 1:1 |
| 11 | `utility.png` | 1:1 |
| 12 | `maintenance.png` | 9:16 |
| 13 | `materials.png` | 5:4 |

All thirteen land in `03-characters/shada/source/artwork/`, overwriting the
existing files by the same name. Then:

```bash
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
```

## Continuity rules across the set

- Same face, same scale density and placement, in every image containing her.
- Same costume build in slots 1–5 and 12. Slots 6–8 are reference sheets.
- The knife in slot 9 is the same knife visible at her hip in slots 1–5.
- Nothing gains a decorative element between images.

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 1.0 | 2026-07-30 | ready | Initial prompt pack derived from locked character. |
