# Captain Jasu — costume turnarounds

**The primary deliverable.** Five images per outfit: four technical views
and one natural pose. Generate these in full before any mood image.

Each file is self-contained — open, select all, paste. Every reference it
needs is listed inside it as a public URL, to be fetched not attached.

All at **2:3**, tall, full figure.

| Outfit | Status | View | Prompt | Output |
|---|---|---|---|---|
| Field dress | in progress | FRONT | `turn-field-front.txt` | `turn-field-front.png` |
| Field dress | in progress | LEFT SIDE | `turn-field-left.txt` | `turn-field-left.png` |
| Field dress | in progress | RIGHT SIDE | `turn-field-right.txt` | `turn-field-right.png` |
| Field dress | in progress | BACK | `turn-field-back.txt` | `turn-field-back.png` |
| Field dress | in progress | NATURAL POSE | `turn-field-natural.txt` | `turn-field-natural.png` |

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
