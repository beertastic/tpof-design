---
title: "Akk Dog — Finish List"
asset_id: "TRACK-AKK-IMAGES"
updated: "2026-08-03"
status: "open"
---

# Akk Dog — Finish List

**The rig is canonical.** Nine reference plates were filed 2026-08-03 and the
scale is measured. What remains is three renders and one question, and both are
blocked on the VFX team rather than on us.

## Waiting on VFX — asked 2026-08-03

- [ ] **`turnaround-front.png`** — head-on, orthographic. Chest width and stance,
      which every side view hides.
- [ ] **`turnaround-rear.png`** — hindquarters and tail.
- [ ] **`pose-seated.png`** — seated or lying. **Scene 9 needs this**, and it is
      the pose the animal is actually in on screen. It is also the only thing
      blocking the "Jasu petting it as it sleeps" image.
- [ ] **Is the dorsal crest always on?** The unrendered sculpt captures show a
      smooth back where every rendered plate shows a plated, spiked crest.
      Everything else matches feature for feature — horn count and sweep, eye and
      socket, snout, tooth arrangement, feet and claws — so it is almost certainly
      the same base mesh with the crest carried by displacement or a groom layer
      that an unrendered viewport does not show. **The question is not "same
      model" but "does the crest render every time".** Until answered, the
      rendered plates are canonical for the crest and the sculpt plates for the
      silhouette underneath it.

Render conditions, from `08-species/akk-dog/reference/README.md`: neutral grey,
even lighting, no dramatic key, no depth of field, no motion blur. 2048 px on the
long edge is plenty.

## Ours to do

- [ ] **`outfits.yaml`** — the tooling reads nothing else. `regen` looks for
      `08-species/akk-dog/outfits.yaml` and everything hangs off it.
- [ ] **De-scaffold `Prompts.md`** — `short.py` writes nothing for a scaffold,
      silently. Same trap that left Captain Jasu with five images for two days.
- [ ] **Decide whether it gets its own boards.** It is a creature, not a costume;
      the six-board set may be the wrong shape for it.

## Settled, do not reopen

**Scale: 0.85 m at the highest point of the back, ~1.05 m nose to tail base.**
Measured off the turntable against a 1.8 m figure on the same ground plane, feet
within 4 px of each other. Great Dane height, at the top of that range.

**The landmark is per-person and must be recomputed, never standardised.** Level
with the bottom of Captain Jasu's belt at 155 cm; **mid-thigh on Baylan at 198
cm.** Pegging it to a tall character's waist would make it 1.19 m and a pony.

**The dentition decides Scene 25 and it already works.** Many small conical grip
teeth, no shearing blades — the jaw physically cannot sever. The scene needs
injuries survivable for the length of Jeyin's dialogue and unmistakably fatal,
and the script leads with the claws, not a bite. **Nothing needs re-scaling or
re-modelling.**

**It has no name, deliberately.** She has never named the only thing that has
ever loved her because nobody taught her how.

## Related

- [`../08-species/akk-dog/Creature.md`](../08-species/akk-dog/Creature.md) — the measurements and the landmark table
- [`../08-species/akk-dog/reference/README.md`](../08-species/akk-dog/reference/README.md) — what each plate is good for, and its caveat
- [`Jasu-Image-TODO.md`](Jasu-Image-TODO.md) — `12-akk_together` needs these plates
- [`Deaths-And-Effects.md`](Deaths-And-Effects.md) — Scene 25
