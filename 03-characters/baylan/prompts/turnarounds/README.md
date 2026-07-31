# Baylan — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Attach actor
reference first.

All at **2:3**, tall, full figure.

| Outfit | View | Prompt | Output |
|---|---|---|---|
| Working dress | FRONT | `turn-working-front.txt` | `turn-working-front.png` |
| Working dress | LEFT SIDE | `turn-working-left.txt` | `turn-working-left.png` |
| Working dress | RIGHT SIDE | `turn-working-right.txt` | `turn-working-right.png` |
| Working dress | BACK | `turn-working-back.txt` | `turn-working-back.png` |
| Working dress | NATURAL POSE | `turn-working-natural.txt` | `turn-working-natural.png` |
| Working dress with robe | FRONT | `turn-robe-front.txt` | `turn-robe-front.png` |
| Working dress with robe | LEFT SIDE | `turn-robe-left.txt` | `turn-robe-left.png` |
| Working dress with robe | RIGHT SIDE | `turn-robe-right.txt` | `turn-robe-right.png` |
| Working dress with robe | BACK | `turn-robe-back.txt` | `turn-robe-back.png` |
| Working dress with robe | NATURAL POSE | `turn-robe-natural.txt` | `turn-robe-natural.png` |
| Shirtsleeves | FRONT | `turn-shirtsleeves-front.txt` | `turn-shirtsleeves-front.png` |
| Shirtsleeves | LEFT SIDE | `turn-shirtsleeves-left.txt` | `turn-shirtsleeves-left.png` |
| Shirtsleeves | RIGHT SIDE | `turn-shirtsleeves-right.txt` | `turn-shirtsleeves-right.png` |
| Shirtsleeves | BACK | `turn-shirtsleeves-back.txt` | `turn-shirtsleeves-back.png` |
| Shirtsleeves | NATURAL POSE | `turn-shirtsleeves-natural.txt` | `turn-shirtsleeves-natural.png` |
| Jedi Knight robes | FRONT | `turn-jedi-front.txt` | `turn-jedi-front.png` |
| Jedi Knight robes | LEFT SIDE | `turn-jedi-left.txt` | `turn-jedi-left.png` |
| Jedi Knight robes | RIGHT SIDE | `turn-jedi-right.txt` | `turn-jedi-right.png` |
| Jedi Knight robes | BACK | `turn-jedi-back.txt` | `turn-jedi-back.png` |
| Jedi Knight robes | NATURAL POSE | `turn-jedi-natural.txt` | `turn-jedi-natural.png` |

## The consistency rule

The four turnaround views are **the same photograph with the subject
rotated.** Same distance, lens, height, light, background and scale. If the
figure changes size or the light shifts between images, the set is useless.

Generate all five of an outfit in one sitting, in one conversation, before
moving to the next outfit.

Generated from `outfits.yaml` by `tools/prompt-splitter/turnarounds.py`.
**Do not edit these files** — edit `outfits.yaml` and regenerate.
