---
title: "Capture Block"
asset_id: "PROMPT-CAPTURE"
version: "1.0"
status: "canonical"
---

# Capture Block

Prompt language for making generated images read as **photographs taken with real
equipment**, in the anamorphic house style.

> **Inlined into each character's `Prompts.md`**, like the Style and Do Not
> blocks. If you change a rule here, propagate it.

---

## Two kinds of image — do not mix them

The two blocks have **different applicability**, and conflating them is the
easiest mistake to make:

| Block | Applies to | Why |
|---|---|---|
| **Capture** (anamorphic) | Narrative frames only — in-scene, environment, character-at-work | These are frames from the film. Reference plates are not |
| **Anti-synthetic** | **Anything containing a face** — including portrait studies and expression strips | A study is lit flat and sharp, but the skin must still be real |

| Type | Slots | Treatment |
|---|---|---|
| **Narrative** | portraits in-scene, environment, character-at-work | Capture **+** Anti-synthetic |
| **Face study** | close portraits, expression strips | Anti-synthetic **only** — flat even light, sharp across frame |
| **Object plate** | materials, props, kit layouts, turnarounds | **Neither.** Flat documentation light |

A materials board shot with shallow depth of field and lens flare is a bad
materials board. Reference plates are documentation, not frames from the film.

## Anamorphic is a look, not a delivery ratio

The film is shot anamorphic; **board slots are layout frames, not film frames.**
Ask for the ratio the slot states and let the optical character do the work.
Requesting 2.39:1 for a 9:16 panel produces letterboxing and wastes the frame.

---

## Block D — Capture (narrative slots only)

> Shot on **anamorphic lenses** in the manner of the original Star Wars trilogy —
> Panavision-style spherical-mount anamorphic glass, not modern clinical optics.
>
> **Optical character:** oval, horizontally-stretched bokeh in out-of-focus
> highlights. Gentle barrel distortion. Noticeably softer toward the frame edges
> while the focal plane stays sharp. Shallow depth of field with smooth, creamy
> falloff. Faint horizontal streak flare where a bright practical source is in
> frame — restrained, never a lens-flare showpiece. Mild chromatic aberration at
> high-contrast edges. Slight vignetting.
>
> **Photochemical character:** the response of 35mm motion picture negative —
> fine organic grain, present in the shadows and midtones rather than added
> uniformly. Gentle halation blooming around bright sources. Highlight rolloff
> that compresses rather than clips. Rich shadow that retains detail instead of
> going black.
>
> **Colour:** restrained, filmic, desaturated toward the muted end. Skin tones
> natural and slightly warm. No digital vibrance, no teal-and-orange grade, no
> saturation boost.
>
> **Focus behaviour:** one plane is sharp and everything else falls away. Detail
> resolves where the lens is focused and softens elsewhere — do not render every
> surface at equal sharpness.
>
> The image should look like a **frame from a photochemical motion picture**, or a
> unit stills photographer's frame from the same set, not a rendered picture.

---

## Block E — Anti-synthetic (narrative slots only)

The recognisable "AI look" comes from a specific set of tells. Name them and they
recede.

> **Skin must be real.** Visible pores, fine lines, uneven tone, blemishes,
> broken capillaries, stubble, shine where skin is oily and matte where it is
> not. Subsurface scattering at the ears and nostrils. **No smoothed, waxy,
> airbrushed or plastic skin.** No beauty retouching of any kind.
>
> **Faces are asymmetric.** Eyes differ slightly, the smile is uneven, the nose
> is not centred. Nothing about a real face is mirrored.
>
> **Lighting has a direction and a cost.** One dominant source with genuine
> shadow and real falloff. No omnidirectional fill, no invisible rim light on
> every subject, no glow with no source.
>
> **Framing is imperfect.** Off-centre, unbalanced headroom, an object clipped by
> the frame edge, something slightly in the way. Not a composed poster.
>
> **Detail is not uniform.** Real photographs have areas of mush — motion, focus
> falloff, underexposed corners. Resist rendering every fibre of every surface at
> maximum sharpness.
>
> **Nothing is symmetrical, new or clean** unless the shot says so.

---

## Optional — naming equipment

Specifying real hardware often improves photographic realism, because models have
learned the associations from photographic metadata. Use sparingly and stay
plausible.

**Useful to name:**

- *Panavision anamorphic* — the original-trilogy lineage; more flare and more
  character than modern glass
- *ARRI ALEXA* — the digital body behind most contemporary Star Wars television
- *Kodak Vision3 500T* — tungsten-balanced motion picture negative; good for
  firelight and interiors
- *85mm / 100mm anamorphic* for portraits; *40mm* for wider environment shots
- Aperture as a number — *f/2.8*, *f/4* — rather than "shallow depth of field"

**Do not** name a director of photography, a specific film title, or a living
artist. Describe the equipment and the physics, not a person's work.

---

## Honest limits

**Prompt language helps. Reference images help far more.**

The single biggest lever on photographic realism is attaching a real photograph
with the look you want, alongside actor reference. Words steer; images anchor.

Expect to reject a lot. Generators drift toward smooth, symmetrical, evenly-lit
and over-detailed output because that is what they are rewarded for, and no
phrasing defeats that reliably. Getting one good frame out of six is a normal
hit rate, and the discipline is throwing the other five away rather than
accepting one that is nearly right.

**The tell to check first is always skin.** If it looks retouched, the image has
failed regardless of what else it gets right.
