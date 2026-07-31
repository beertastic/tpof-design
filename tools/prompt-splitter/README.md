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

## Reference plates — `references:`

An outfit can name approved plates that get attached alongside the costume
reference:

```yaml
references:
  - path: source/artwork/material-scale.png
    what: the scale plates, their finish and how the panel is assembled
```

Every turnaround view then carries an operator line naming that file. Unlike the
costume reference, these attach to the **front view too** — the material can be
locked before the costume is, and usually should be, because a material plate is
a far easier image to get right than a full figure.

This is the prop lock recorded in `11-production-tracking/Shada-Image-TODO.md`,
in its minimal form. Words cannot hold a silhouette; only an image can.

## Rules

`outfits.yaml` and `Prompts.md` are the sources of truth. **Do not edit the
generated `.txt` files** — change the source and re-run.

Re-run both after any change to a character's costume, the Style block, the
Capture block or the Turnaround block.

### A slot body must never contradict a `must_show:` rule

The non-negotiables from `outfits.yaml` are injected twice — once at the top of
every prompt and once as the closing checklist. The slot's own `=== THIS IMAGE
===` description sits between them.

**Where the two disagree, the generator follows the slot body**, because it is
the specific instruction and the rules are the general one. Shada's `maintenance`
slot asked for "a dim salvaged interior" while her rules said EXTERIOR ONLY in
capitals, twice. It returned an interior every time, and the rule looked broken
when it was being overruled by a sentence forty lines further down.

So: when a `must_show:` rule governs something — location, handedness, what is
on which side, what she is never seen wearing — the slot bodies must not restate
it, qualify it, or describe a scene that needs it broken. Describe only what that
particular image adds.

Symptom to watch for: a rule that is stated emphatically and ignored
consistently. That is almost never the model failing to read it. Search the slot
body for the thing it is being told not to do.

### The checker cannot see inside `must_show`

It compares prose against the rules. It does **not** compare the rules against
each other, and a long `must_show` block can contradict itself.

That happened: the scale rule said TESSELLATED, NOT OVERLAPPED, and four hundred
words later the gauntlet placement rule still said "Overlapping metal scales
wrapping the outer forearm". Both in the same list, both hoisted to the top of
every prompt. The gauntlet came back shingled.

**When you invert a rule, grep the whole `must_show` for the old word**, not just
the paragraph you edited.

### `consistency.py` now checks this automatically

Four defects from this one pattern was enough. Both tools run the checker on
every invocation, so it fires wherever you already look:

```text
! shada/working description: says "…Quiet wraps at the forearms and…" but a
  must_show rule forbids "wrap". The prose wins in the prompt — remove it or
  restate it to agree.
```

It looks for four things, all of which have caused a real defect:

| Check | The defect it came from |
|---|---|
| Prose asserts something the rules forbid | `maintenance` asked for an interior against EXTERIOR ONLY |
| "both X" where the rules make X asymmetric | "caps over both shoulders" against one cap, her left |
| An item placed somewhere the rules do not | "a compact blaster at the hip" against her right thigh |
| An item described generically where the rules name a model | the same line, after the blaster became a WESTAR-35 |

**It is a lint, not a prover.** It reports prose worth looking at rather than
proving a contradiction, and it is tuned to stay quiet — a checker nobody reads
is worse than no checker. The whole repo currently produces zero warnings.

The four defects are encoded as regression cases, along with the phrasings that
tripped earlier versions of the checker:

```bash
python tools/prompt-splitter/consistency.py --selftest
```

If a change stops one of those being caught, the change is wrong. Run it after
touching `consistency.py`.
