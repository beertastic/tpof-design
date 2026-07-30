---
title: "Akk Dog"
asset_id: "CREATURE-AKK-DOG"
version: "0.1"
status: "asset-built"
category: "creature"
owner: "Captain Jasu"
scenes: "9"
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

Jasu's animal. It tells you what she is before she says anything: she keeps a war
beast as a pet and is comfortable enough to fuss over it while giving orders. It
is the only warmth she shows on camera.

It also sets the danger level of her camp. A crew that keeps an akk dog is not a
crew you walk away from — which matters, because Baylan has been living beside it
for years, and the escapees are being hunted by it.

### Scene 9 beat

> *Captain Jasu pets a dog-like beast and briefs her mercenaries about a crashed
> ship nearby. She orders the camp to bed down with patrols. Bay worries and
> recalls past missions.*

Evening, forest mercenary camp. The animal is calm and being handled
affectionately in the middle of a military briefing.

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
- TBD: is it calm with the rest of the crew, or only with her?
- TBD: is it working equipment — does it track, hunt, or guard — or purely hers?
- TBD: does it appear in the pursuit scenes (19–24) or only in camp?
- TBD: harness, collar, muzzle, or nothing?

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

- Does the akk dog appear in any scene other than 9? The breakdown does not list
  it as a character or set dressing anywhere else, but a tracking beast would
  plausibly be used in the pursuit.
- Does it have a name? Jasu petting a named animal plays differently from Jasu
  petting an animal.
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
