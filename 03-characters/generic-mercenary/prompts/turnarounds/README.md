# Generic Mercenary — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Attach actor
reference first.

All at **2:3**, tall, full figure.

| Outfit | Status | View | Prompt | Output |
|---|---|---|---|---|
| The large one | in progress | FRONT | `turn-heavy-front.txt` | `turn-heavy-front.png` |
| The large one | in progress | LEFT SIDE | `turn-heavy-left.txt` | `turn-heavy-left.png` |
| The large one | in progress | RIGHT SIDE | `turn-heavy-right.txt` | `turn-heavy-right.png` |
| The large one | in progress | BACK | `turn-heavy-back.txt` | `turn-heavy-back.png` |
| The large one | in progress | NATURAL POSE | `turn-heavy-natural.txt` | `turn-heavy-natural.png` |
| The rifle | in progress | FRONT | `turn-ranged-front.txt` | `turn-ranged-front.png` |
| The rifle | in progress | LEFT SIDE | `turn-ranged-left.txt` | `turn-ranged-left.png` |
| The rifle | in progress | RIGHT SIDE | `turn-ranged-right.txt` | `turn-ranged-right.png` |
| The rifle | in progress | BACK | `turn-ranged-back.txt` | `turn-ranged-back.png` |
| The rifle | in progress | NATURAL POSE | `turn-ranged-natural.txt` | `turn-ranged-natural.png` |
| The close one | in progress | FRONT | `turn-armoured-front.txt` | `turn-armoured-front.png` |
| The close one | in progress | LEFT SIDE | `turn-armoured-left.txt` | `turn-armoured-left.png` |
| The close one | in progress | RIGHT SIDE | `turn-armoured-right.txt` | `turn-armoured-right.png` |
| The close one | in progress | BACK | `turn-armoured-back.txt` | `turn-armoured-back.png` |
| The close one | in progress | NATURAL POSE | `turn-armoured-natural.txt` | `turn-armoured-natural.png` |
| The non-human | in progress | FRONT | `turn-alien-front.txt` | `turn-alien-front.png` |
| The non-human | in progress | LEFT SIDE | `turn-alien-left.txt` | `turn-alien-left.png` |
| The non-human | in progress | RIGHT SIDE | `turn-alien-right.txt` | `turn-alien-right.png` |
| The non-human | in progress | BACK | `turn-alien-back.txt` | `turn-alien-back.png` |
| The non-human | in progress | NATURAL POSE | `turn-alien-natural.txt` | `turn-alien-natural.png` |

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
