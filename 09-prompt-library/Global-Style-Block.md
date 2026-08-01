# Global Style Block

Canonical source for the shared prompt language used by every character's
`Prompts.md`. Derived from **Production Design Bible v1.0**.

These blocks are **inlined** into each `03-characters/<name>/Prompts.md` rather
than referenced. That is deliberate: an image generator reading a single prompt
file in isolation must still receive the full ruleset. If you change a rule
here, propagate it to the character files.

---

## Block A — Style

> Live-action Star Wars production still. Outer Rim frontier realism in the
> manner of the original trilogy and *Andor*, with a subtle *Mandalorian*
> frontier aesthetic. Photographic, not illustrative.
>
> This is a galaxy built from industrial salvage. Nothing is factory fresh.
> Every object has had a previous owner and carries visible history: repairs,
> scratches, faded paint, replaced components, grime, and evidence of servicing.
>
> Costume is functional workwear first and appearance second — flight suits,
> mechanic coveralls, modular armour panels, utility harnesses, padded work
> jackets, weather capes, survival gear, pressure garments, industrial gloves.
> Construction must be real and buildable: believable seams and fasteners, no
> floating armour, nothing purely decorative. Occupation should be readable from
> silhouette alone.
>
> Materials: ballistic weave, quilted flight fabric, reinforced synth-leather,
> flexible armour mesh, woven technical textiles, plastoid armour plates,
> insulated work fabric, industrial rubber, carbon-fibre composite, brushed
> alloy. Surfaces show wear, repair, scratches, grime and fading.
>
> Palette is muted, sun-faded and practical — charcoal, ash grey, weathered
> black, faded olive, dust brown, sand, bone white, cream. Secondary: rust red,
> ochre, deep burgundy, forest green, navy blue. Accents used sparingly: brass,
> copper, oxidised bronze, warning yellow. Bright colour appears only for rank,
> warning markings, cultural identity, or a significant personal item.
>
> Lighting is motivated by believable sources only: natural sunlight, overcast
> sky, planetary atmosphere, work lamps, bulkhead fixtures, warning lights,
> control panels, firelight.
>
> Camera: naturalistic composition over heroic posing. Restrained colour grade,
> subtle atmospheric haze, realistic depth of field, fine film grain, practical
> lens behaviour. The subject is engaged in meaningful activity rather than
> looking at camera unless the shot specifies otherwise. The world should feel
> larger than the people within it.

---

## Block B — Negative / Do Not

> Do not produce: Caribbean or Earth pirate costume, tricorn silhouettes, pirate
> coats, corsets, Renaissance or medieval clothing, medieval leather armour,
> fantasy shoulder pads, decorative belts, swashbuckler aesthetics, Victorian
> fashion, Roman armour, or modern tactical/SWAT gear.
>
> No pristine futuristic minimalism. No factory-fresh or polished surfaces. No
> ceremonial or ornamental equipment. No oversized or highly stylised weapons.
> No glowing decorative technology. No gadget overload.
>
> No glamour posing, no sexualisation, no fashion-editorial lighting, no
> direct-to-camera hero stance unless the shot specifies it.
>
> No text, logos, watermarks, captions, labels, or lettering anywhere in the
> image.
>
> No crushed blacks — the silhouette must stay separated from the background.
>
> Photographic realism only: no anime, no cel shading, no painterly
> illustration, no 3D-render look, no plastic or waxy skin.

---

## Block C — Species rendering

> Alien species must feel biologically plausible and grounded in live-action
> Star Wars. Favour practical make-up and prosthetic effects over exaggerated
> digital fantasy. Costume adapts to anatomy without sacrificing practicality.
> Individuality is expressed through clothing, tools, customs and craftsmanship
> rather than extreme anatomy alone.

---

## Aspect ratios by artwork slot

The board generator places images with a **contain** operation — it never crops.
Supplying the wrong ratio produces letterboxing on the board. Match these.

| Slot | Board frame | Ratio | Ask for |
|---|---|---|---|
| `portrait.png` | 5.15 × 9.70 | 1 : 1.88 | tall portrait, 9:16 |
| `forest.png` | 5.15 × 9.70 | 1 : 1.88 | tall portrait, 9:16 |
| `industrial_a.png` | 5.15 × 9.70 | 1 : 1.88 | tall portrait, 9:16 |
| `industrial_b.png` | 5.30 × 9.70 | 1 : 1.83 | tall portrait, 9:16 |
| `industrial_c.png` | 5.30 × 9.70 | 1 : 1.83 | tall portrait, 9:16 |
| `maintenance.png` | 5.40 × 9.40 | 1 : 1.74 | tall portrait, 9:16 |
| `scale_portrait.png` | 6.20 × 8.00 | 1 : 1.29 | portrait, 3:4 |
| `materials.png` | 7.00 × 5.60 | 1.25 : 1 | landscape, 5:4 |
| `blaster.png` | 5.25 × 5.50 | 1 : 1.05 | square, 1:1 |
| `utility.png` | 5.45 × 5.50 | 1 : 1.01 | square, 1:1 |
| `expression_strip.png` | 6.40 × 3.50 | 1.83 : 1 | landscape, 16:9 |
| `species_strip.png` | 6.40 × 2.45 | 2.61 : 1 | wide banner, 21:9 |
| `knife.png` | 10.90 × 3.70 | 2.95 : 1 | wide banner, 3:1 |

Frame dimensions come from each character's `board-data.yaml`. If you change a
frame there, update the ratio you ask for.

---

## Prompt hierarchy

Per Bible §12, every prompt applies, in order:

1. Style Bible (Block A + Block B above)
2. Faction guide — `04-factions/<faction>/Faction.md`
3. Character documents — `Character.md` + `Character-Lock.md`
4. Scene description — `02-story/Scene-Index.md`
5. Camera direction

The Style Bible always takes precedence unless explicitly overridden.
