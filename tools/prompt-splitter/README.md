# Prompt Splitter

Turns a character's `Prompts.md` into **paste-ready plain-text prompt files** —
one per image, each completely self-contained.

```bash
python tools/prompt-splitter/split.py baylan
python tools/prompt-splitter/split.py --all
```

## Why

`Prompts.md` is written for a human: it explains which blocks apply where, keeps
the continuity rules together, and carries the checklist. That makes it a bad
thing to copy out of — you have to select four separate sections, skip the
instructions, and strip the markdown.

The generated files have none of that. **Open one, select all, paste.**

## What it does

- Assembles Style, Do Not, Character Constants and the slot description into one file
- Adds **Capture** (anamorphic) only to narrative slots
- Adds **Skin and realism** to any slot containing a face
- Strips markdown — bold, backticks, links, blockquotes
- Removes the applicability notes, which address you and not the model
- Writes a `README.md` index showing which blocks each slot received

## Output

```
03-characters/<character>/prompts/
    01-portrait.txt
    02-forest.txt
    ...
    README.md
```

## Rules

**`Prompts.md` is the source of truth.** These files are generated output — do
not edit them. Change `Prompts.md` and re-run.

**Only characters with `status: ready` are processed.** Scaffolds are skipped,
because a paste-ready prompt full of `NEEDS:` markers is worse than no file.

Re-run after any change to a character's prompts, the Style block, or the
Capture block.
