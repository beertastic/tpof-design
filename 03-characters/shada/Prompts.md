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

> **Start with the costume turnarounds — they are the primary deliverable.**
> 5 paste-ready prompts in [`prompts/turnarounds/`](prompts/turnarounds/).
> Generate those in full before any image in this document. Regenerate with
> `python tools/prompt-splitter/turnarounds.py shada`.
>
> **The slots below are plates and mood images.** Three or four mood images is
> enough — they are context, not something anyone builds from.
>
> **Pre-assembled versions of the slots below are in [`prompts/`](prompts/).** One
> plain-text file per image, each fully self-contained — open it, select all,
> paste. No sections to gather, no markdown to strip. Generated from this
> document; if you change anything here, run
> `python tools/prompt-splitter/split.py shada`.

**How to use** (if assembling by hand)**.** Each numbered slot below is a complete, self-contained prompt.
Paste **Style**, **Do Not**, **Character Constants**, then the single slot you
want. For narrative slots, add **Capture** and **Anti-synthetic** as well — see
the note on those blocks for which slots they apply to. Do not paste more than one slot at a time. Save the result to the exact
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
dusk, mist, campfire and firelight, and hand-carried work lamps.

SHADA IS NEVER INDOORS AND NEVER ON A SHIP. Every environment she appears in is
exterior: wet forest, forest clearing, or the mercenary camp among the trees. No
corridors, no bulkheads, no control panels, no warning lights, no market stalls,
no buildings, no crowds.

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

No fashion-editorial lighting.

No text, logos, watermarks, captions, labels or lettering in the image.

No crushed blacks — the silhouette must stay separated from the background.

Photographic realism only: no anime, no cel shading, no painterly illustration,
no 3D-render look, no plastic or waxy skin.

**Shada — costume cut.** Unlike other characters in this project, her costume is
deliberately **close-fitting and follows her figure**: waist defined, cut to the
body, feminine. She is compact, agile and quick and the clothes must say so.
Nothing bulky, nothing loose, no oversized jacket or coat swallowing her
silhouette. It remains a working infiltration costume — everything on it does a
job — but it is fitted, not concealing.

**Shada-specific rejections.** Not a generic human scavenger with no serpentine
ancestry. Not fully reptilian or a full creature design. Not a heavy-armoured
soldier. Not covered head-to-toe in a way that hides the scale language.

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

> **Paste with slots 1, 3, 4, 11, 16** — in-scene frames.
>
> **Do NOT paste with reference plates** (6–8 (studies), 9–11, 13). Those want flat, even
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

> **Paste with slots 1, 2, 3, 4, 5, 6, 7, 11, 16.** Wider than the Capture block: a portrait study or
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

## Costume rules — FULL-FIGURE slots only

> **Applies to slots 1, 2, 3, 4, 11, 16** — images showing the whole costume.
>
> **Do NOT apply to face and skin references** (5, 6, 7). Those are close studies
> where the costume is deliberately not the subject, and demanding a thigh patch
> in a head-and-shoulders portrait forces the shot wider and ruins it.

The non-negotiable costume rules are injected here automatically from
`outfits.yaml`.

---

## Attachments — read this before attaching anything

**Any full-figure photograph you attach must say what it is NOT for.**

Learned the hard way on 2026-08-01. A costume reference was attached with the
label *"match its silhouette, cut, palette…"* and the generation came back in a
perfect costume on the wrong woman: with six images attached and one of them a
well-lit full-length portrait of a person in exactly this costume, the most
face-like image wins the likeness unless it is explicitly disqualified. Naming
the actor photograph is not enough — the competing photographs have to be ruled
out by name.

Every costume reference in `outfits.yaml` therefore leads with **NOT THE FACE**,
and the first non-negotiable rule says the same thing again. This applies to
every character, not only Shada.

**And use a fresh conversation for every character.**

Learned the next day, 2026-08-02, when a Shada prompt returned **Captain Jasu's
costume on Shada's face** — bone horns, a scale yoke across the shoulders, a
quilted long-sleeved bodysuit, matched wrist bracers. Nothing in the prompt asked
for any of it. Her turnaround set had been generated the day before, and a model
that has just drawn one character in this production carries that costume
forward unless the conversation is cleared.

The prompts now name the specific tells as prohibitions so they survive the
mistake, but that is a backstop. **The fix is a new chat per character**, and it
costs nothing.

---

## Character Constants — paste with every prompt

Shada. Female mercenary assassin, thief, scout and tracker. Compact, agile
build, small beside most of the crew. Mostly human in appearance with subtle
inherited serpentine ancestry.

Her snake ancestry is **tens of thousands of years back** — so distant that
almost nothing of it survives, and she is human to look at. Fine, subtle scales
on her neck, collarbone, shoulders, arms and hands are the one trace left:
**read them as a faint tattoo lying flat on the skin**, not as a texture applied
over it and never as armour. On her face the same texture appears only
at the edges: the temples, the outer edge of the cheekbone, along the jawline,
down the side of the neck and behind the ear. Tonal, the same colour as her skin,
readable only where light rakes across it and easy to miss in flat light. Never
across the nose, forehead, cheeks or mouth — she is a human actor in makeup, not
a creature in prosthetics. Eyes carry a reptilian quality while
remaining expressive and recognisably human. Movement stays human, restrained
and economical.

Costume: light, fitted, scavenged armour in **five pieces** — a SOLID
3D-PRINTED gauntlet on her right forearm, a LOOSE scale cap hanging off her left
shoulder, a scale patch on her left outer thigh, and a pair of **unmatched scale
flank panels** over her ribs, laced together across the centre front and worn
over the vest. **No breastplate** — her chest and sternum stay plain cloth in the
lacing gap between the panels, with the collar, the placket and the centre-front
seam still readable. Layered technical cloth, worn leather, repaired matte
hardware.

The vest is **cloth, not hide** — a heavy close-woven working fabric in a dusty
sun-bleached **grey with a hint of khaki-green**, soft enough to crease where the
hard pieces bear on it. It is the flexible base layer the armour is strapped
over. Its weave carries a **faint serpentine grain** — fine, irregular, tonal, in
the material rather than printed on it, readable only in raking light. It is not
the scale armour and must never be confused with it.

**The palette is grey, grey-green and khaki.** Trousers colder and darker than
the vest; all leather in **grey-brown taupe**, never chestnut or tan. The dark
bronze thigh patch is the one warm thing in the costume.

Two belts: a worn taupe leather waist belt, and a second slung diagonally below
it to carry the drop-leg holster on her right. Mid-calf taupe boots with long
leather straps wound criss-cross up the shaft.

SCALE ARMOUR — THE DEFINING FEATURE OF THIS COSTUME.

**THE PLATE — THIS IS THE BUILT OBJECT. MATCH IT.**

A flat six-sided plate, **10 to 15 mm across — about the size of a
thumbnail.** These are **fine scale, not large plates**: one flank panel
alone carries well over a hundred, and a patch reads as a dense field of many
small pieces rather than a dozen big ones. The gauntlet is outside this rule —
it is a plain shell, not a field of plates. A **regular equilateral
hexagon** with six straight sides and slightly soft, rounded edges. **EVERY PLATE
IS THE SAME HEXAGON — identical in size and outline, one master repeated.** The
outlines never vary plate to plate, are never wonky or hand-cut, and are never
five-, seven- or eight-sided. Not round, not a coin, not a teardrop, not a fish
scale.

*Said positively 2026-08-03. This read "uneven edges — cut and cast by hand,
never machine-crisp", and the generator obeyed it: the plates came back as
irregular polygons at varying sizes. The plates are a printed part. It is the
FINISH that is hand-worn, never the outline.*

**Surface:** rough and pitted, like sand-cast or corroded metal. A shallow raised
lip runs around the rim of each plate. Dark iron-grey, almost black, going to
pale worn silver on the raised edges where it has been handled. Matte, never
bright, never polished.

**EVERY SINGLE PLATE CARRIES A RAISED SNAKE SWIRL.** This is not optional and
not a detail that can be dropped — **a plate without one is not this costume. If
the plates in the image are blank, the image has failed.**

**The swirl:** a single continuous line curling and winding across the face of
the plate in the shape of a small snake — coiling back on itself, loosely S-shaped
or spiralling, with a slightly thicker head at one end tapering to a fine tail at
the other. It fills most of the plate face.

**It is RAISED, not stamped into the surface.** The swirl stands **proud of the
face** as a soft, worn, rounded ridge, catching light along its top edge and
casting a faint shadow beside it. Not engraved, not incised, not a recessed
stamp, not a printed or etched line.

**The swirl varies from plate to plate.** Every plate carries one, but no two are
identical — the curl sits differently, the line runs thicker or
thinner, some are nearly worn away. It is a common manufacturer's mark from cheap
Outer Rim plate, and every mill, batch and worn die renders it a little
differently. She did not choose it, and nobody remarks on it.

**Two small lacing holes** per plate, punched near opposite edges, for the cord
or wire that fixes it to the backing. The holes are visible.

**Five pieces, five different materials.** Mismatched salvaged alloys — **dull
grey steel** in the gauntlet, **blackened iron** in the shoulder cap, **dark
bronze** in the thigh patch, **pale worn pewter** in her right flank panel and
**rust-red oxidised iron** in her left. **No brass and no verdigris anywhere on
this costume.** On the four flexible pieces, **every plate is a discrete,
countable, physically separate piece** — never an embossed or printed pattern on
a continuous leather panel, never a texture, never a pattern on cloth.

**Within any one piece the metal is all one metal.** A panel speckled with
several alloys reads as decorative mottling: one panel is one piece of salvage
from one trip. The mismatch is between the five pieces, never inside one.

**The gauntlet is the exception and only the gauntlet.** It is a single rigid
printed shell, and its face is **plain worn plate rather than a hexagon field** —
a broad flat panel with a shallow border line at the edge, a scatter of rivets
and a faint raised serpent swirl worn almost away. It must read as a hull offcut,
never as a manufactured tech panel.

**TESSELLATED, NOT OVERLAPPED.** The plates sit edge to edge in a single flat
plane. They do not lap over one another — no layering, no shingling.

**They almost touch.** The gap between neighbours is a **thin dark seam no wider
than the plate is thick** — a line, not a space. Laid close and tight in a
continuous field. **Never spaced apart, never scattered, never floating on a web
of connectors** with the backing showing through in wide gaps between them.

**The lacing is thin and mostly hidden.** Fine waxed cord or thin wire through
the two holes, passing behind the plates to the backing. **No chunky toggles, no
rubber knots, no beads, no visible web of connectors sitting proud of the
plates.** The fixing is barely noticeable; the metal is what you see.

**The backing is not manufactured.** Worn leather or heavy cloth, **hand cut with
an irregular uneven edge**, stitched by hand with uneven stitches, visibly
repurposed from something else. **No neat scalloped outline, no even machine
topstitching, no symmetrical shape, no finished product edge.** If the backing
looks like it came off a production line, the costume says somebody made this for
her, and it is wrong.

**Within one patch the metal is broadly consistent** — one trip, one source —
with only two or three plates obviously replaced later in a different alloy. It
is the **four pieces** that differ from each other, not every plate within a
patch. A panel where every single plate is a different metal reads as decorative
mottling and loses the four-trips story.

The flex comes from the seams and the lacing.

**IT MUST NOT READ AS TECHNOLOGY.** Regular hexagons meeting edge to edge is also
the shape of carbon fibre, machined hex panelling and energy shielding, and that
is this design's failure mode. **No frames, no bezels, no channels around the
plates, no carbon weave, no composite, no polished surfaces, no two plates
finished alike.** This is scrap cut into hexagons by hand and laced on, and the
**worn salvaged finish** is the only thing separating it from a tech panel.

**The only light on this costume is a small cluster of dim recessed telltales at
the gauntlet wrist** — amber, dirty, half-dead, no spill onto skin or leather. Nothing else
glows: no lit seams, no illuminated hexagons, no edge lighting, no blue.

**The shape and the motif repeat. The material and the finish do not.**

 Practical harness, belt,
sheath, concealed holster. Functional exposed skin at shoulders, upper arms and
selected mobility zones — for movement, heat and sensory function, never
decorative or sexualised, and it is what makes the inherited scales legible.
Nothing polished, ornamental or factory fresh.

Equipment: a **WESTAR-35 blaster pistol** on her right thigh, a well-used combat
knife that never leaves her side, and a small climbing and infiltration kit.
Nothing else. The blaster is Mandalorian manufacture carried by somebody who is
not Mandalorian — slab-sided and angular, dull silver-steel with brass panels let
into the slide and a worn black grip. It has had a previous owner and nobody
explains it.

She is dangerous through precision, patience and observation rather than
physical dominance. Everything about how she moves, dresses and watches has been
shaped by wet forest — she belongs in it, and it shows.

---

# Prompt slots

## 1. `hero.png` — the hero portrait
**Tall portrait, 9:16.**

The single image that is this character. Waist-up, in a dim wet forest at dusk,
three-quarter angle. She has stopped and turned her head toward something
off-frame — caught mid-assessment, not posing, not looking at camera. Utterly
still. Overcast evening light through wet canopy, with a soft rim separating her
from the treeline.

Close enough to read the fine inherited scales at her collarbone, neck and the
edge of her face, and to see the metal scale patch at her shoulder catching a
little light. Her expression is neutral alertness — the resting face of someone
who has already worked out three ways out of here.

Shallow depth of field, forest falling into haze behind her. This is the image
that goes on the front of the deck: it must make someone want to know who she is.

## 2. `scale_figure.png` — scale reference
**Portrait, 3:4.**

Two figures standing side by side against a plain seamless neutral mid-grey
studio background, evenly lit, both full length from head to below the feet,
both sharp, shot from chest height on a long lens.

On the left, an average-height human man of about 1.8 metres in plain dark
working clothes, standing straight and neutral — a scale reference, not a
character. On the right, Shada in her full costume, standing the same way.

**She is visibly smaller and lighter than he is** — compact, agile, noticeably
short beside him. That size difference is the entire purpose of this image and
must be unmistakable at a glance.

Even flat documentation lighting, no atmosphere, no environment. A reference
photograph, not a composition.

## 3. `camp_day.png` — the camp, in daylight
**Tall portrait, 9:16.**

**The daylight in-situ reference.** The costume in a real environment, under
light good enough to read every part of it.

Shada standing in the forest mercenary camp in bright overcast morning light —
open sky, no deep shadow, no atmosphere obscuring anything. Tarpaulins,
crates and a dead campfire behind her. She is doing something ordinary: coiling a
line, checking a strap, about to move off.

Full or three-quarter figure, close enough that **the five armour pieces, both
weapons and the material of every layer are clearly legible**. This is the image
someone looks at to answer "what does it actually look like out there" — so the
costume must be readable, not atmospheric.

Bright but not harsh. Soft overcast daylight, the kind that shows texture without
crushing anything into shadow.

## 4. `forest.png` — in-environment
**Tall portrait, 9:16.**

**The dusk in-situ reference — the companion to slot 3.** The same costume in
low light, where it will actually be shot.

Full-figure shot of Shada moving low through dense wet forest at dusk, weight on
the balls of her feet, one hand steadying against a trunk. Not running —
deliberate, economical, mid-assessment. Read as small against the scale of the
trees. Mist between trunks, wet bark, leaf litter, standing water catching the
last light. Her dark layers stay separated from the background by wet rim
highlights and material contrast, never merging into black. Natural overcast
dusk only.

## 5. `scale_portrait.png` — species detail
**Portrait, 3:4.**

Close portrait of Shada, head and shoulders, turned slightly away, lit at a
grazing angle to reveal skin texture. The subject of this image is the
inheritance: fine scales across cheekbone, temple, jaw, neck and collarbone,
blending into human skin rather than stopping at a hard edge. Practical make-up
and prosthetic quality, not digital fantasy. Eyes visible, reptilian in
structure but expressive and human in intent. Soft overcast daylight. No
costume detail competing for attention.

## 6. `species_strip.png` — ancestry study
**Wide banner, 21:9.**

Horizontal study strip, three to four separate views across the frame on a
neutral, evenly lit background: scale detail on the back of the hand and
forearm; scale transition at the collarbone and shoulder; close eye detail
showing the reptilian iris structure; profile of the neck and jawline. Even,
flat reference lighting — this is a make-up and prosthetics reference, not a
dramatic image. Consistent skin tone and scale density across every view.

## 7. `expression_strip.png` — performance range
**Landscape, 16:9.**

Horizontal strip of four head-and-shoulders expressions of the same face,
evenly lit and consistently framed: (1) neutral alertness — the resting state;
(2) suspicion without panic; (3) focused assessment, narrowing in on a target;
(4) cold lethal calm. Restrained throughout — this face does not perform. Same
lighting, same angle, same scale detail in every panel. Reference-sheet
evenness, not four dramatic portraits.

## 8. `knife.png` — hero prop
**Wide banner, 3:1.**

Product-reference layout of a single combat knife on a neutral surface, lit
evenly. An old working blade, repeatedly sharpened — the edge profile visibly
reground and shortened over years. Grip wrapped and repaired with mismatched
cord. Silent, secure sheath shown alongside. This is a survival tool first and a
weapon second: it should read as something used daily for cutting rope, food and
cordage, not a fighting knife on display. Mechanically believable, no ornament,
no engraving, no jewelling.

## 9. `blaster.png` — hero prop
**Square, 1:1.**

Product-reference layout of **a WESTAR-35 blaster pistol** on a neutral surface,
lit evenly, side-on and filling the frame — the specific in-universe model, not a
generic sidearm.

Slab-sided and angular. A brushed bare-metal body in **dull silver-steel**, with
**brass panels** let into the top of the slide and at the rear. Squared trigger
guard, prominent front sight post, a circular vented port through the mid-body,
and a **black textured grip** worn through and chipped where a hand sits.

Modified for reliability rather than power — replacement components, mismatched
finish, a field-repaired grip, worn bluing at the contact points. Mechanically
believable construction with visible fasteners and access.

**Weathered, never factory fresh.** Scratched finish, grime settled in the
recesses, at least one component plainly newer than the rest. No scope, no
glowing elements, no ornament.

## 10. `utility.png` — kit layout
**Square, 1:1.**

Overhead flat-lay of everything Shada carries, laid out on a worn surface in the
deliberate order of someone who checks it after every job: a coiled length of
thin climbing line, a cloth tool roll opened flat to show a row of slender steel
probes and fine hand tools, a small repair kit, spare parts, a cleaning kit,
cloth wraps, and a compact dented water flask. Every item shows use and repair. Explicitly no
datapad and no unnecessary technology. Even, flat reference lighting. The
restraint of the kit is the point — this is a short list, well maintained.

## 11. `maintenance.png` — character at work
**Tall portrait, 9:16.**

Shada seated at the mercenary camp among the trees, cleaning and checking her
blaster, parts laid out in a fixed habitual arrangement on the cloth beside her.
Absorbed in the task, not looking up. This is the image that says preparation is
how she controls fear. Hands and forearms prominent — scales visible, fingers
precise. Warm practical light from a campfire or a hand-carried work lamp,
against wet forest going dark behind her. Open ground under trees — no walls, no
ceiling, no structure enclosing her. Unhurried, ordinary, routine.

## 12. `material-scale.png` — the salvaged metal scales
**Square, 1:1.**

Extreme close-up macro photograph of a section of the scale armour, lying flat on
a plain neutral surface, filling the frame.

Flat six-sided plates **10 to 15 mm across, about the size of a thumbnail** — **regular equilateral
hexagons** with slightly soft, rounded, uneven edges and a shallow raised lip
around each rim. The surface is rough and pitted, like sand-cast or corroded
metal: dark iron-grey going almost black, with pale worn silver on the raised
edges. **Two small lacing holes** punched near opposite edges of each plate, cord
or wire running through them to the leather backing beneath.

Laid edge to edge and **almost touching** — the gap between neighbours is a thin
dark seam, a line rather than a space. The lacing is fine and mostly hidden
behind the plates: no chunky toggles, no rubber knots, no web of connectors. No
frame or bezel around any plate.

The backing beneath is **hand-cut worn leather with an irregular edge and uneven
hand stitching** — never a neat manufactured panel.

**THIS IS A FRAGMENT, NOT A GARMENT.** A torn-off scrap of the material, roughly
the size of a hand, with **only twelve to twenty plates visible** and cut or torn
edges on every side. One edge runs out of frame. Not symmetrical, not centred,
not a finished piece.

**IT IS NOT CLOTHING AND MUST NOT BECOME ANY.** Not a vest, not a plate carrier,
not body armour, not a chest panel, not a bib, not anything wearable or complete.
**No shoulder straps, no webbing, no buckles, no velcro, no closures, no armholes,
no neckline.** If the object in frame could be put on, the image is wrong.

**No modern body-armour silhouette of any kind.** This material appears on her
costume only as four small patches — one forearm, one shoulder, the centre of the
and one thigh. **There is no breastplate and no full torso panel anywhere
in this production.**

**SIX STRAIGHT SIDES ON EVERY PLATE.** Never round, never a coin, never a
teardrop, never a fish-scale shape, and **never seven or eight sides**.
**EVERY PLATE IS THE SAME HEXAGON** — one printed master, identical in size and
outline across the whole patch. The outlines do not vary and are not hand-cut.
**Tessellated, not overlapped** — the plates meet edge to edge in a single flat
plane and never lap over one another.

**EVERY PLATE CARRIES A RAISED SNAKE SWIRL, AND THIS IS THE POINT OF THE IMAGE.**
A single continuous line curling and winding across the plate face in the shape of
a small snake — coiling back on itself, loosely S-shaped or spiralling, a slightly
thicker head at one end tapering to a fine tail at the other, filling most of the
face.

**It stands proud of the surface** as a soft, worn, rounded ridge, catching light
along its top edge and casting a faint shadow beside it. Not engraved, not
incised, not a recessed stamp, not etched or printed.

**THREE OR FOUR DIFFERENT SWIRLS, REPEATING:** the same few marks recur across
the patch — never a unique curl on every plate. Neighbouring plates may well
carry the same mark. What differs between them is the **wear**: how far the ridge
has worn down, where the paint has chipped, which are nearly smooth. **A blank
plate means the image has failed** — at this magnification every swirl must be
clearly legible.

**This is one patch, so the metal is broadly consistent** — one salvage source,
one alloy, with only two or three plates obviously replaced later in something
else. Scratched, dulled, weathered to a low sheen. The lacing and the backing are
visible at the edge of the piece. Even flat lighting, sharp across the frame. A
single material sample photographed for reference — no styling, no arrangement,
no other objects.

## 13. `material-leather.png` — worn synth-leather
**Square, 1:1.**

Extreme close-up macro photograph of a piece of worn reinforced synth-leather,
lying flat on a plain neutral surface and filling the frame. Years of use: the
surface cracked and softened, colour worn away at the high points, a repaired
tear with visible hand stitching in mismatched thread, and one edge showing a
stitched seam and a rivet. Dust worked into the grain. Even flat lighting, sharp
across the frame. A single material sample photographed for reference — no
styling, no arrangement, no other objects.


**A material sample, not an object.** A flat swatch or offcut with cut edges,
roughly the size of a hand. Not a garment, not a bag, not anything wearable
or finished. If the thing in frame could be put on or carried, it is wrong.
## 14. `material-cloth.png` — coarse technical fabric
**Square, 1:1.**

Extreme close-up macro photograph of coarse woven technical fabric, lying flat on
a plain neutral surface and filling the frame. The weave clearly visible at
thread level. Muted and desaturated, dye faded unevenly by sun and washing. A
frayed cut edge, a patch stitched over it by hand, and staining worked into the
fibres. Even flat lighting, sharp across the frame. A single material sample
photographed for reference — no styling, no arrangement, no other objects.


**A material sample, not an object.** A flat swatch or offcut with cut edges,
roughly the size of a hand. Not a garment, not a bag, not anything wearable
or finished. If the thing in frame could be put on or carried, it is wrong.
## 15. `material-hardware.png` — buckles and fittings
**Square, 1:1.**

Extreme close-up macro photograph of a small group of weathered metal fittings on
a plain neutral surface: two or three buckles, a hook, a strap end, a rivet.
Salvaged and mismatched — different metals, different ages, one plainly newer
than the rest. Matte and tarnished, scratched from use, nothing polished or
reflective. Even flat lighting, sharp across the frame. Photographed for
reference — no styling, no arrangement, nothing else in frame.

---


**A material sample, not an object.** A flat swatch or offcut with cut edges,
roughly the size of a hand. Not a garment, not a bag, not anything wearable
or finished. If the thing in frame could be put on or carried, it is wrong.
## 16. `tone-collage.png` — the share sheet

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
| 1 | `hero.png` | 9:16 |
| 2 | `scale_figure.png` | 3:4 |
| 3 | `camp_day.png` | 9:16 |
| 4 | `forest.png` | 9:16 |
| 5 | `scale_portrait.png` | 3:4 |
| 6 | `species_strip.png` | 21:9 |
| 7 | `expression_strip.png` | 16:9 |
| 8 | `knife.png` | 3:1 |
| 9 | `blaster.png` | 1:1 |
| 10 | `utility.png` | 1:1 |
| 11 | `maintenance.png` | 9:16 |
| 12 | `material-scale.png` | 1:1 |
| 13 | `material-leather.png` | 1:1 |
| 14 | `material-cloth.png` | 1:1 |
| 15 | `material-hardware.png` | 1:1 |

All thirteen land in `03-characters/shada/source/artwork/`, overwriting the
existing files by the same name. Then:

```bash
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
```

## Continuity rules across the set

- Same face, same scale density and placement, in every image containing her.
- Same costume build in slots 1–5 and 12. Slots 6–8 are study plates.
- The knife in slot 9 is the same knife visible at her hip in slots 1–5.
- Nothing gains a decorative element between images.

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 1.0 | 2026-07-30 | ready | Initial prompt pack derived from locked character. |
