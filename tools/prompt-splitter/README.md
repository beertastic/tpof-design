# Prompt Tools

Two generators. Both read from the character's documents and emit **paste-ready
plain-text prompts** — open one, select all, paste.

```bash
python tools/prompt-splitter/turnarounds.py baylan   # costume turnarounds
python tools/prompt-splitter/split.py baylan         # plates and mood images
```

Both accept `--all`.

## Priority

**Turnarounds first, and in full.** They are the primary deliverable — what a
costume department actually builds from. Plates and mood images are context, and
three or four mood images per character is enough.

## turnarounds.py

Reads `03-characters/<character>/outfits.yaml` and produces **five prompts per
outfit**: front, left, right, back, and a natural pose.

Output: `03-characters/<character>/prompts/turnarounds/`

Four technical views on a plain grey studio background, arms out, flat even
light, sharp across frame, everything visible. Plus a fifth showing the same
costume on a person standing the way that person actually stands — because a
turnaround tells you what the garment *is* and nothing about how it *sits*.

**Consistency is the point.** The four views are one photograph with the subject
rotated: same distance, lens, height, light, background, scale. Generate all five
of an outfit in one sitting, in one conversation.

Add or change outfits by editing `outfits.yaml` and re-running.

## split.py

Reads `Prompts.md` and produces one prompt per numbered slot — props, materials,
expression range, and the remaining mood images.

Output: `03-characters/<character>/prompts/`

Assembles only the blocks each slot needs:

| Block | Applies to |
|---|---|
| Realism | Every slot, no exceptions |
| Capture (anamorphic) | Narrative frames only |
| Anti-synthetic (skin) | Anything with a face |

Only characters with `status: ready` are processed.

## Rules

`outfits.yaml` and `Prompts.md` are the sources of truth. **Do not edit the
generated `.txt` files** — change the source and re-run.

Re-run both after any change to a character's costume, the Style block, the
Capture block or the Turnaround block.
