# Baylan — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Attach actor
reference first.

All at **2:3**, tall, full figure.

| Outfit | Status | View | Prompt | Output |
|---|---|---|---|---|
| Working dress | in progress | FRONT | `turn-working-front.txt` | `turn-working-front.png` |
| Working dress | in progress | LEFT SIDE | `turn-working-left.txt` | `turn-working-left.png` |
| Working dress | in progress | RIGHT SIDE | `turn-working-right.txt` | `turn-working-right.png` |
| Working dress | in progress | BACK | `turn-working-back.txt` | `turn-working-back.png` |
| Working dress | in progress | NATURAL POSE | `turn-working-natural.txt` | `turn-working-natural.png` |

## Approved outfits

An outfit marked **APPROVED** has a locked reference image. Every other view
of that costume carries a `MATCH THE APPROVED REFERENCE` instruction naming
the file to attach — and states that where the text and the image disagree,
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
