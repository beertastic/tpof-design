# Mercenary Kit — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Every reference it
needs is listed inside it as a public URL, to be fetched not attached.

All at **2:3**, tall, full figure.

| Outfit | Status | View | Prompt | Output |
|---|---|---|---|---|
| Merc 1 — the Wookiee | in progress | FRONT | `turn-merc-1-front.txt` | `turn-merc-1-front.png` |
| Merc 1 — the Wookiee | in progress | LEFT SIDE | `turn-merc-1-left.txt` | `turn-merc-1-left.png` |
| Merc 1 — the Wookiee | in progress | RIGHT SIDE | `turn-merc-1-right.txt` | `turn-merc-1-right.png` |
| Merc 1 — the Wookiee | in progress | BACK | `turn-merc-1-back.txt` | `turn-merc-1-back.png` |
| Merc 1 — the Wookiee | in progress | NATURAL POSE | `turn-merc-1-natural.txt` | `turn-merc-1-natural.png` |
| Merc 2 — the rifle | in progress | FRONT | `turn-merc-2-front.txt` | `turn-merc-2-front.png` |
| Merc 2 — the rifle | in progress | LEFT SIDE | `turn-merc-2-left.txt` | `turn-merc-2-left.png` |
| Merc 2 — the rifle | in progress | RIGHT SIDE | `turn-merc-2-right.txt` | `turn-merc-2-right.png` |
| Merc 2 — the rifle | in progress | BACK | `turn-merc-2-back.txt` | `turn-merc-2-back.png` |
| Merc 2 — the rifle | in progress | NATURAL POSE | `turn-merc-2-natural.txt` | `turn-merc-2-natural.png` |
| Merc 3 — the close one | in progress | FRONT | `turn-merc-3-front.txt` | `turn-merc-3-front.png` |
| Merc 3 — the close one | in progress | LEFT SIDE | `turn-merc-3-left.txt` | `turn-merc-3-left.png` |
| Merc 3 — the close one | in progress | RIGHT SIDE | `turn-merc-3-right.txt` | `turn-merc-3-right.png` |
| Merc 3 — the close one | in progress | BACK | `turn-merc-3-back.txt` | `turn-merc-3-back.png` |
| Merc 3 — the close one | in progress | NATURAL POSE | `turn-merc-3-natural.txt` | `turn-merc-3-natural.png` |
| Merc 4 — the near-human | in progress | FRONT | `turn-merc-4-front.txt` | `turn-merc-4-front.png` |
| Merc 4 — the near-human | in progress | LEFT SIDE | `turn-merc-4-left.txt` | `turn-merc-4-left.png` |
| Merc 4 — the near-human | in progress | RIGHT SIDE | `turn-merc-4-right.txt` | `turn-merc-4-right.png` |
| Merc 4 — the near-human | in progress | BACK | `turn-merc-4-back.txt` | `turn-merc-4-back.png` |
| Merc 4 — the near-human | in progress | NATURAL POSE | `turn-merc-4-natural.txt` | `turn-merc-4-natural.png` |

## Approved outfits

An outfit marked **APPROVED** has a locked reference image. Every other view
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
