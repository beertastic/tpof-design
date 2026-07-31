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

**For anything physically built, the reference is a photograph of the build, not
a render.** Shada's blaster is being 3D printed, and the generated `blaster.png`
does not match the printed prop — no brass panels in the slide, a brown ribbed
grip instead of black. Attaching it would lock every image to a gun nobody is
making. Her scale plates went the right way round: the printed samples drove the
specification, not the other way about.

A declared reference that does not exist is a warning, because the prompt will
otherwise tell the operator to attach a file that is not there.

### Generate the cheap plates first, then the figure

The stated priority is turnarounds first, and as a *deliverable* that is still
right. As an **order of work** it is backwards.

A material or prop plate is a small, flat, evenly-lit object on a plain surface.
It is far easier to get right than a full figure, it converges in two or three
attempts, and once approved it does two things for the figure prompt: it carries
the detail far better than words, and it lets you **delete** the words it
replaces. Shada's front turnaround dropped 8,000 characters the moment her plate
was locked.

Do the plates, lock them into `references:`, then generate the figure with all of
them attached.

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

### A rule that is 75% of the prompt crowds out the other 25%

Shada's front turnaround reached **36,500 characters**, and her `must_show` had
drifted badly out of balance:

| Rule | Words |
|---|---|
| 1 — the scale plate | **1,206** |
| 2 — fitted silhouette | 40 |
| 3 — bare arms | 27 |
| 4 — weapons and sides | 166 |
| 5 — exterior only | 64 |
| 6 — face treatment | 96 |

The generator returned a costume with beautifully correct hexagonal plates, long
sleeves, a scarf, no gauntlet and a full torso panel. It obeyed the rule that was
shouting and invented the rest. Nothing was missing from the prompt — "bare arms
and shoulders" was in there twice, 27 words long, behind a 1,200-word wall.

**Every rule in `must_show` competes with every other rule.** Adding detail to one
is not free; it is taken from the others.

The fix was not to shorten the plate spec but to **move it**. Once an approved
plate image is attached via `references:`, the figure prompts do not need to
describe how a plate is made — the image carries it, far better than words. Rule
1 became 390 words ending in "for what a plate looks like, match the attached
plate reference image", and the full specification lives where it belongs: in the
material-plate slot and in `Character.md`.

**The prompt had grown 38% at exactly the moment it should have shrunk.** When a
reference image gets locked, go and delete the words it replaces.

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
