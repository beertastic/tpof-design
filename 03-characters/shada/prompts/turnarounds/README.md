# Shada — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Attach actor
reference first.

All at **2:3**, tall, full figure.

| Outfit | View | Prompt | Output |
|---|---|---|---|
| Infiltration dress | FRONT | `turn-working-front.txt` | `turn-working-front.png` |
| Infiltration dress | LEFT SIDE | `turn-working-left.txt` | `turn-working-left.png` |
| Infiltration dress | RIGHT SIDE | `turn-working-right.txt` | `turn-working-right.png` |
| Infiltration dress | BACK | `turn-working-back.txt` | `turn-working-back.png` |
| Infiltration dress | NATURAL POSE | `turn-working-natural.txt` | `turn-working-natural.png` |

## The consistency rule

The four turnaround views are **the same photograph with the subject
rotated.** Same distance, lens, height, light, background and scale. If the
figure changes size or the light shifts between images, the set is useless.

Generate all five of an outfit in one sitting, in one conversation, before
moving to the next outfit.

Generated from `outfits.yaml` by `tools/prompt-splitter/turnarounds.py`.
**Do not edit these files** — edit `outfits.yaml` and regenerate.
