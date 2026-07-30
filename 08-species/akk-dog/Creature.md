---
title: "Akk Dog"
asset_id: "CREATURE-AKK-DOG"
version: "0.1"
status: "asset-built"
named: false
category: "creature"
owner: "Captain Jasu"
scenes: "9, and others — full list pending"
source: "Filmanize script breakdown; existing production 3D asset"
---

# Akk Dog

> **Production rule:** Refer to the Production Design Bible before any visual development or image generation.

> **The built asset is canonical.** A 3D akk dog has been modelled and rigged for
> this production. That asset — not this document, not any reference image, and
> not any generated picture — defines the creature. Everything here exists to
> keep generated imagery consistent *with the rig*.

## Art Department Brief

Captain Jasu's akk dog. Appears in Scene 9, where she pets it while briefing her
mercenaries about the crashed ship. Described in the breakdown only as a
"dog-like beast."

An akk dog is a large, heavy-bodied quadruped predator with an armoured hide —
established Star Wars fauna, traditionally kept as a guard and war beast. The
production has built and rigged its own version; the specifics below must be
filled in from that asset rather than from outside reference.

## Story Function

**The akk dog kills Jeyin in the final scene.** Jeyin is Shin's mother. This
animal is not a background detail or a piece of camp colour — it is the
instrument of the film's central loss, and the reason Shin ends the story with
nothing left.

That gives Scene 9 a job. Jasu petting the animal affectionately while briefing
her squad is not characterisation for Jasu; it is setup. The audience must find
the akk dog genuinely likeable — a big calm animal enjoying being scratched —
because the finale depends on that affection being turned against them.

It also sets the danger level of the camp. A crew that keeps an akk dog is not a
crew you walk away from, which matters because Baylan has been living beside it
for years and the escapees are being hunted by it.

**It has no name.** Jasu keeps a war animal she has never named. That is a
deliberate and cold detail: she is fond of it the way you are fond of a good
weapon.

## The core design rule

**The animal does not change.**

It is exactly as affectionate in Scene 9 as it is lethal in the finale. It does
not transform, snarl, redden, bulk up, or acquire monster-design language for the
kill. It does what a war beast was always going to do, with the same body and the
same behaviour, and that is what makes it frightening.

What changes across the film is the audience's reading of the animal — never the
animal itself. Any drift toward creature-feature design in the final scene
destroys the effect the whole structure was built for.

### Scene 9 — the setup

> *Captain Jasu pets a dog-like beast and briefs her mercenaries about a crashed
> ship nearby. She orders the camp to bed down with patrols. Bay worries and
> recalls past missions.*

Evening, forest mercenary camp. The animal is calm and being handled
affectionately in the middle of a military briefing. It must be warm, heavy,
unthreatening and slightly comic — an enormous animal enjoying a scratch.

### Scene 24 / 24A — the kill

The akk dog kills Jeyin in the forest clearing during the final confrontation.

Design and production consequences:

- **Stunt and VFX beat.** The breakdown already flags a `Krellis head shot`
  visual effect in Scene 24. Jeyin's death needs equivalent planning, and it is
  a creature interaction rather than a weapon hit — considerably harder.
- The animal's **jaw, bite mechanism and neck mass** now carry real weight in the
  design. Whatever the rig does in that shot has to be believable at the scale
  established in Scene 9.
- **Blood and aftermath** must be decided as a production standard, not
  improvised in one shot.
- Jeyin is already injured and limping from Scene 16 onward. She is not killed
  while fighting; she is killed while unable to run.

### Other scenes

The akk dog appears in **several scenes beyond 9**. The Filmanize breakdown does
not track it — it is named only inside the Scene 9 description as a "dog-like
beast" and appears in no character or set-dressing list anywhere.

**This means the scene breakdown under-reports the creature, and any schedule
built from that export will miss it.** The full scene list needs to be recorded
here and reflected in `Scene-Index.md`.

## Physical Design

**To be completed from the built asset.** Record what the rig actually is, not
what reference says it should be.

- Overall length / height at shoulder: TBD
- Mass and silhouette: TBD
- Hide: armoured plating, scale, or hair — and its colour range: TBD
- Head and jaw structure: TBD
- Number of limbs and stance: TBD
- Eyes: TBD
- Tail: TBD
- Distinguishing marks unique to *this* animal: TBD

**Scale reference is the critical value.** Every generated image containing the
akk dog needs it correct relative to a human, and it is the single thing image
generators get wrong most often. Record its height at the shoulder against a
1.8 m figure and state it in every prompt.

## Handling and Behaviour

- Calm and affectionate with Jasu specifically (Scene 9).
- Lethal on command, or off it — it kills Jeyin in the finale.
- It has no name.
- TBD: is it calm with the rest of the crew, or only with her?
- TBD: is the kill ordered by Jasu, or does the animal act on its own? This is
  the difference between Jasu being a murderer and the akk dog being a loose
  weapon, and it changes how the animal is handled in every earlier scene.
- TBD: is it worked as a tracker in the pursuit, or only released at the end?
- TBD: harness, collar, muzzle, or nothing? A working animal that is sometimes
  released needs something to release it *from*.

If it wears any tack, that tack is a prop and belongs in `05-props/`.

## Design Rules for Generated Imagery

Per the Production Design Bible §11, creature design must feel biologically
plausible and grounded in live-action Star Wars — practical creature-effects
quality rather than exaggerated digital fantasy.

- It is an animal, not a monster. It has weight, breath and body language.
- No glowing eyes, no fantasy horns, no ornamental spikes.
- Any harness or collar follows the same industrial-salvage rules as everything
  else: worn, repaired, functional, previously owned.
- It must sit in the same muted palette as the rest of the film.
- Weight must read on the ground — a heavy animal displaces leaf litter, sinks
  slightly, and moves earth.

## Reference

Drop production renders into [`reference/`](reference/). See that folder's
README for what is needed and why.

## Open Questions

- **Which scenes exactly?** Confirmed to appear in several beyond Scene 9, but
  the breakdown tracks none of them. Needed for the creature's own shot list, for
  `Scene-Index.md`, and for any schedule built from the breakdown export.
- **Is the kill ordered?** Jasu commanding it and the animal acting alone are
  different films, and the answer changes how the akk dog is staged throughout.
- Is the production treating akk dogs as established fauna with fixed
  characteristics, or as a loose starting point for an original design? This
  determines how much the generated imagery may deviate from the built rig.
- Should creatures move out of `08-species/` into their own category? Species and
  animals are different design problems. One creature does not justify a folder;
  three would.

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 0.1 | 2026-07-30 | asset-built | Folder created. 3D asset exists and is rigged; document awaiting specifics from it. |
