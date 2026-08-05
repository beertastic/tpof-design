# Vala — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Every reference it
needs is listed inside it as a public URL, to be fetched not attached.

All at **2:3**, tall, full figure.

| Outfit | Status | View | Prompt | Output |
|---|---|---|---|---|
| The remnants of a fighting rig, layered for the forest | in progress | FRONT | `turn-rig-front.txt` | `turn-rig-front.png` |
| The remnants of a fighting rig, layered for the forest | in progress | LEFT SIDE | `turn-rig-left.txt` | `turn-rig-left.png` |
| The remnants of a fighting rig, layered for the forest | in progress | RIGHT SIDE | `turn-rig-right.txt` | `turn-rig-right.png` |
| The remnants of a fighting rig, layered for the forest | in progress | BACK | `turn-rig-back.txt` | `turn-rig-back.png` |
| The remnants of a fighting rig, layered for the forest | in progress | NATURAL POSE | `turn-rig-natural.txt` | `turn-rig-natural.png` |

## Approved outfits

An outfit marked **APPROVED** has a locked front turnaround. Every other view
of that costume carries a `MATCH THE APPROVED REFERENCE` instruction naming
the URL to fetch — and states that where the text and the image disagree,
**the image wins**.

**Editing an approved outfit invalidates artwork already made from it.** The
generator prints a warning when you do. If a change is genuinely needed,
clear the `approved` block, regenerate, and re-approve from a new reference.

## The consistency rule

The four turnaround views are **the same photograph with the subject
rotated.** Same distance, lens, height, light, background and scale. If the
figure changes size or the light shifts between images, the set is useless.

Generate all five of an outfit in one sitting, in one conversation, before
moving to the next outfit.

Generated from `outfits.yaml` by `tools/prompt-splitter/turnarounds.py`.
**Do not edit these files** — edit `outfits.yaml` and regenerate.
