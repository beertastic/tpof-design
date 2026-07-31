# Shin — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Attach actor
reference first.

All at **2:3**, tall, full figure.

| Outfit | Status | View | Prompt | Output |
|---|---|---|---|---|
| As we meet her | in progress | FRONT | `turn-early-front.txt` | `turn-early-front.png` |
| As we meet her | in progress | LEFT SIDE | `turn-early-left.txt` | `turn-early-left.png` |
| As we meet her | in progress | RIGHT SIDE | `turn-early-right.txt` | `turn-early-right.png` |
| As we meet her | in progress | BACK | `turn-early-back.txt` | `turn-early-back.png` |
| As we meet her | in progress | NATURAL POSE | `turn-early-natural.txt` | `turn-early-natural.png` |
| Destroyed by the forest | in progress | FRONT | `turn-late-front.txt` | `turn-late-front.png` |
| Destroyed by the forest | in progress | LEFT SIDE | `turn-late-left.txt` | `turn-late-left.png` |
| Destroyed by the forest | in progress | RIGHT SIDE | `turn-late-right.txt` | `turn-late-right.png` |
| Destroyed by the forest | in progress | BACK | `turn-late-back.txt` | `turn-late-back.png` |
| Destroyed by the forest | in progress | NATURAL POSE | `turn-late-natural.txt` | `turn-late-natural.png` |
| The clearing | in progress | FRONT | `turn-final-front.txt` | `turn-final-front.png` |
| The clearing | in progress | LEFT SIDE | `turn-final-left.txt` | `turn-final-left.png` |
| The clearing | in progress | RIGHT SIDE | `turn-final-right.txt` | `turn-final-right.png` |
| The clearing | in progress | BACK | `turn-final-back.txt` | `turn-final-back.png` |
| The clearing | in progress | NATURAL POSE | `turn-final-natural.txt` | `turn-final-natural.png` |

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
