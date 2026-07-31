# Shin — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Attach actor
reference first.

All at **2:3**, tall, full figure.

| Outfit | View | Prompt | Output |
|---|---|---|---|
| As we meet her | FRONT | `turn-early-front.txt` | `turn-early-front.png` |
| As we meet her | LEFT SIDE | `turn-early-left.txt` | `turn-early-left.png` |
| As we meet her | RIGHT SIDE | `turn-early-right.txt` | `turn-early-right.png` |
| As we meet her | BACK | `turn-early-back.txt` | `turn-early-back.png` |
| As we meet her | NATURAL POSE | `turn-early-natural.txt` | `turn-early-natural.png` |
| Destroyed by the forest | FRONT | `turn-late-front.txt` | `turn-late-front.png` |
| Destroyed by the forest | LEFT SIDE | `turn-late-left.txt` | `turn-late-left.png` |
| Destroyed by the forest | RIGHT SIDE | `turn-late-right.txt` | `turn-late-right.png` |
| Destroyed by the forest | BACK | `turn-late-back.txt` | `turn-late-back.png` |
| Destroyed by the forest | NATURAL POSE | `turn-late-natural.txt` | `turn-late-natural.png` |
| The clearing | FRONT | `turn-final-front.txt` | `turn-final-front.png` |
| The clearing | LEFT SIDE | `turn-final-left.txt` | `turn-final-left.png` |
| The clearing | RIGHT SIDE | `turn-final-right.txt` | `turn-final-right.png` |
| The clearing | BACK | `turn-final-back.txt` | `turn-final-back.png` |
| The clearing | NATURAL POSE | `turn-final-natural.txt` | `turn-final-natural.png` |

## The consistency rule

The four turnaround views are **the same photograph with the subject
rotated.** Same distance, lens, height, light, background and scale. If the
figure changes size or the light shifts between images, the set is useless.

Generate all five of an outfit in one sitting, in one conversation, before
moving to the next outfit.

Generated from `outfits.yaml` by `tools/prompt-splitter/turnarounds.py`.
**Do not edit these files** — edit `outfits.yaml` and regenerate.
