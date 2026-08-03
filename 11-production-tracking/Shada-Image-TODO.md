---
title: "Shada — Finish List"
asset_id: "TRACK-SHADA-IMAGES"
updated: "2026-08-03"
---

# Shada — Finish List

**Status: FRONT v2 APPROVED 2026-08-03, MAKE-UP LOCKED.** There are now TWO
approved references with stated, non-overlapping scopes: `turn-working-front.png`
for the costume, `scale_portrait.png` for the make-up. Every remaining image is
generated against both.

**Twelve images to make.** The run list below is the only place that carries
the order. Documents are the deliverable; images are a guide.

**What the lock changed, in one place:**

| | Was | Is |
|---|---|---|
| Vest material | Scavenged hide | **Cloth** — heavy close-woven working fabric |
| Palette | Dark brown, charcoal | **Grey vest, grey-green trousers, taupe leather**; bronze thigh patch the one warm note |
| Plate density | "10–15 mm", nothing countable | **About twelve across a flank panel**, fifteen rows — with a floor: any finer is chain mail |
| Tessellation | "Never overlapped" | Said **positively** — flat in one plane, a thin dark line of backing between neighbours |
| Shoulder cap | "Loose, scavenged" | **A palm's width**, the point of the shoulder only |
| Wear | Not specified | **Plates missing** — 5–10 per flank panel, 3–5 on the cap — bent, chipped, badly repaired |
| Serpentine grain | Pressed into hide | **Woven into the cloth** |

Her documents, `outfits.yaml` and all 21 prompts are current and internally
consistent. The checker is clean and the boards validate.

---

## THE RUN LIST — start here

**Eight done. One kept. Twelve to make.**

| | |
|---|---|
| **DONE — do not regenerate** | `turn-working-front` (v2, approved 2026-08-03) · `scale_portrait` (the make-up lock) · **the four remaining turnaround views — `natural`, `left`, `right`, `back`, completed 2026-08-03** · **`material-scale` (v2, 2026-08-03 — the locked plate reference)** · **`material-hardware` (2026-08-03)** |
| **KEEP** | `knife.png` — locked prop reference, unaffected |
| **TO MAKE** | 12 numbered slots |

`species_strip` and `expression_strip` were on the KEEP list until 2026-08-03 and
are **not** any more. Both contradict the make-up lock — round pupils, and the
old heavy all-over scale. `expression_strip` also carries a visible ZIP, BRASS
shoulder plates and a BRASS CHEST BIB, all three of which are forbidden. The
2026-08-02 note kept them because they "do not show enough costume to be
affected"; they show collar, zip, vest, shoulder and chest.

---

### THE RULE FOR EVERY SINGLE IMAGE

1. **A genuinely fresh chat.** Not a continuation. A chat that has drawn another
   character carries that costume over — it has happened, and it cost a full
   generation.
2. **Attach the images FIRST, before pasting anything.**
3. **Paste the whole prompt file as the first message.** Nothing before it,
   nothing after it, no "here is a prompt for you". Do not trim the top.
4. **Check the reply says it used the ATTACHMENTS.** The prompt asks. If it says
   it fetched URLs, or says nothing, the references did not arrive — discard it
   and start again.
5. **Save into `03-characters/shada/source/artwork/`** under the exact name on
   the prompt's `Output file:` line. The boards look them up by name.

**What to attach: every image in `03-characters/shada/prompts/attach/working/`.**
SEVEN files as of 2026-08-03, when the WESTAR-35 reference was added — it was
six before, so any count written down elsewhere is stale. Do not curate the
list and do not type your own; that folder is
generated from the same list the prompt declares, so it cannot drift. Five
different hand-written attachment lists existed in this repository on
2026-08-03 and none of them matched the prompt.

---

### STEP 1 — the four turnaround views  *(DONE 2026-08-03)*

Paste from `03-characters/shada/prompts/turnarounds-short/`:

- [x] `turn-working-natural.txt`
- [x] `turn-working-left.txt` — took three rolls; see the note below
- [x] `turn-working-right.txt`
- [x] `turn-working-back.txt`

**All five views checked as a set on 2026-08-03.** Sides correct in all five,
including the back, which is a true rotation — shoulder blades, back seams, rear
pockets — with all six placements landing on the right side of the frame. Vest
cloth measures RGB 132–149 with a warm bias of +11 to +19 across the set, so the
palette holds; `natural` is the warmest and darkest, `front` the lightest.

Accepted deviations, consistent across all five and **not** worth a roll: plates
~6–7 across a flank panel, arm scale running warm and reticulated rather than
tonal, flank panels reading pewter rather than rust-red. `natural` also carries a
visible zip at the throat — the one recurring fault still unbeaten, and the only
view with it.

**What the three rolls of `left` taught, because it generalises.** Roll one
shingled the shoulder cap and made it a yoke, collar to deltoid. Roll two fixed
the plate size and the boots but *swapped the props* — the blaster appeared on
her visible left side and the knife vanished — because the CHECK block names
which side each piece is **on** and says nothing about a profile view **hiding**
the far side. Roll three fixed both, and only because the correction line named
both faults at once. **Each roll fixes what the correction names and quietly
trades away something it does not.** Name every open fault, every time.

Attach everything in the folder. Check each one for:

- **The far side stays hidden.** In `left`, her right forearm and right thigh are
  behind her — so **no gauntlet and no blaster**, and her near forearm is BARE.
  In `right`, the mirror: no shoulder cap and no knife on the visible side. An
  empty limb is the rule being obeyed, not a detail forgotten.
- **`back` is a rotation, not a mirror.** Her right is on the VIEWER'S RIGHT.
  Judge it by anatomy — shoulder blades, back seams, the back of her head. If you
  can see her face or the front closure, it is a mirror. Frame position cannot
  catch this; a flip swaps the sides too.
- **The shoulder cap HANGS**, standing off her shoulder with daylight under a
  ragged lower edge. Never moulded to the shoulder.

### STEP 2 — `material-scale`, on its own, before anything else  *(DONE 2026-08-03)*

- [x] `prompts/slots-short/12-material-scale.txt` — took three rolls, and the
      third is the locked plate. Restaged; the staged copy is byte-identical to
      `source/artwork/material-scale.png`, so steps 3–5 inherit it.

**Still open on this plate, deliberately not chased.** The serpent is one mark
rotated rather than three or four distinct ones — the written rule carries that,
the build needs 3–4 STLs regardless, and nothing downstream inherits the count
from this image. And it still shows ~16 plates at macro scale rather than the
denser field asked for below. **Watch the first figure image of step 5:** if the
plates come back oversized again, that is the trigger to re-roll this plate with
more in frame. The mitigations that did not exist before are the attachment
label — *"PLATE SHAPE AND FINISH — NOT SIZE... proves nothing about scale"* — and
CHECK line 2, *"Plates SMALL: TWELVE across a flank panel, not six big ones."*

**Do this one before the other plates and before every narrative frame**, because
it is an attached reference for all of them. Getting it right first means the
rest inherit a corrected plate.

**Attach everything EXCEPT** `2-plate-shape-and-finish-not-size.png`, which *is*
the image being made. The prompt's own URL block declares the rest. `MANIFEST.txt`
derives every such exception; there are four in total, and until 2026-08-03 it
named only one.

**When you regenerate it, put MORE and SMALLER plates in frame.** The current one
shows about fourteen at macro scale, which teaches "big plates" to every
generation it is attached to — and the plates have come back two to three times
oversized in every figure so far. Its label already says it proves shape and not
size; the image should stop arguing otherwise.

**THEN RERUN `./tools/regen shada` BEFORE STEP 3.** The staged file
`2-plate-shape-and-finish-not-size.png` is a *copy* of `material-scale.png`, made
at regen time. Save the new plate and the copy is still the old one — so every
prompt in steps 3, 4 and 5 would attach the oversized plate and teach "big
plates" all over again. "The rest inherit a corrected plate" is only true after
this command runs.

### STEP 3 — the remaining plates

- [ ] `09-blaster.txt` — the WESTAR-35. **Brass is CORRECT here and only here**;
      do not reject it as palette drift. Stays out of `references:` afterwards
      until the printed prop is photographed
- [ ] `10-utility.txt` — **re-roll, fresh chat.** The first came back as a costume
      knolling sheet with two gauntlets. Prompt rescoped 2026-08-03
- [ ] `13-material-leather.txt` — **re-roll.** Prompt named no colour at all and
      it came back at 17% value against a costume range of 24–33%. Aim at the
      leather visible in `material-hardware.png`, which measures 36% / sat 23%
      against the approved belt's 32% / sat 19%
- [ ] `14-material-cloth.txt` — **re-roll.** Prompt named neither the colour nor
      the serpentine grain. Came back 27% against the vest's 58%. Should return
      roughly double the value of the swatch it replaces
- [x] `15-material-hardware.txt` — **DONE 2026-08-03.** Two buckles, a hook, a
      strap end, two rivets, three distinguishable metals. Rivets measured at
      sat 24–27%: worn bronze, not brass, so on-spec

**Why all three failed, corrected 2026-08-03 after a wrong first answer.** These
were first recorded as "the prompt did not ask". That was true of the SHORT
prompts, which is what got checked — but the LONG files were the ones being
pasted, and they are a different question.

| | Was it in the long file? | Real cause |
|---|---|---|
| Leather colour | **Yes** — "all leather in grey-brown taupe, never chestnut or tan" | **Truncation.** 17 KB against a ~4 KB budget |
| Cloth grain | **Yes** — "its weave carries a faint serpentine grain" | **Truncation** |
| Cloth colour | No — absent from both | Genuine omission |
| Utility wording | Same in both | Genuine wording fault |

**Two of the four were written, reached the file, and never reached the
generator.** That is the failure `slots-short/` exists to prevent, and the fix
was never more words — it was pasting from `prompts/slots-short/`. The long files
now carry a DO-NOT-PASTE banner across the top, added the same day.

The prompt edits still stand: they close the two genuine gaps and front-load the
rest. But do not read this list as evidence that the generator obeys and the
documents fail. **Check which file was pasted before diagnosing anything.**

### STEP 4 — the two strips, remade against the make-up lock

- [ ] `06-species_strip.txt`
- [ ] `07-expression_strip.txt`

Both must now carry the **vertical slit pupil**, and a scale pattern that is
FLAT, TONAL and at the EDGES only. No zip, no brass, nothing on her chest.

### STEP 5 — the narrative frames

- [ ] `01-hero.txt`
- [ ] `02-scale_figure.txt`
- [ ] `03-camp_day.txt`
- [ ] `04-forest.txt` — **still owed a DUSK frame.** It came back as a daylight
      camp, which makes it a duplicate of `camp_day`. The palette change makes it
      more urgent: the old risk was charcoal vanishing into shadow, the new one is
      grey-green and khaki vanishing into wet foliage.
- [ ] `11-maintenance.txt`
- [ ] `16-tone-collage.txt` — the share sheet. One image, six panels. **The only
      slot where a multi-panel result is correct.** Never used as a reference.

### STEP 6 — build the sheets

```bash
source .venv/bin/activate
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
python tools/board-generator/generate.py shada --promo
```

`--promo` is a **separate command** and is easy to forget.

**`--validate` will stay green throughout and that is not reassurance.** It
catches images that are *absent*, never images that are *stale*.

---

### DO NOT re-roll for these three

All three are recorded as known deviations against the approved front. Each costs
a generation, and a generation risks the things that are finally right.

| | |
|---|---|
| **Boots strapped and buckled** | Rule says never. `pin:` work |
| **Plates ~6–7 across a flank panel** | Spec says twelve. `pin:` work |
| **Arm scale runs warm** | Should be tonal. The written rule wins on colour |

**And do not chase slit pupils in any full-length frame.** Her eyes are about
twenty pixels there and a slit pupil is two or three — it cannot render, and
re-rolling for it risks everything that took seven passes to win. That is
precisely what `scale_portrait.png` is for, and it is attached to every prompt.

---

### If you have to correct a generation

**Re-paste the WHOLE file with a correction line on top.** Never "same again
but…" — that works from its own last output and compounds the error.

## ~~BLOCKER — sixteen of the twenty-one prompts cannot be pasted~~ **CLEARED 2026-08-03**

`short.py` now writes `prompts/slots-short/` — sixteen paste-ready slot prompts,
**2,204 to 8,870 characters** where the long files run 16 KB to 68 KB. Same trim,
same rules, same reference block as the turnaround prompts, with the per-slot
shot text that was the only missing piece.

The 67 KB was never the slot. Measured: the sixteen slot bodies run 421 to 3,199
characters and total 13.5 KB between them. **The rest was shared boilerplate,
repeated in full sixteen times.**

Also fixed: a plate is no longer a reference for itself, so
`12-material-scale.txt` is not handed the previous `material-scale.png` and told
to match it.

**This unblocked 26 images** — twelve here and all fourteen of Captain Jasu's,
the moment her pack stops being a scaffold. Recorded as fix 7 in
[`Prompt-Reliability-TODO.md`](Prompt-Reliability-TODO.md).

The original finding is kept below, because the reasoning is why the fix looks
the way it does.

---

**Found 2026-08-02. Read before starting section 3 or 4 above.**

`short.py` only builds short prompts for the **five turnaround views**. The
sixteen numbered slots exist only as the long files in `prompts/`:

| Slots | Size | Against a ~4,000 character budget |
|---|---|---|
| `hero`, `camp_day`, `forest`, `maintenance`, `tone-collage` | ~65 KB | **16× over** |
| `scale_portrait`, `species_strip`, `expression_strip`, `material-scale` | ~18 KB | 4× over |
| the remaining plates | ~16 KB | 4× over |

So for those sixteen there is no deliberate prompt to paste — you would be
handing over the long file and letting the host compress it, **which is the exact
failure `Prompt-Reliability-TODO.md` exists to document.** The overflow is
discarded silently, from the middle, and nothing reports it.

**The fix is to extend `short.py` to cover the numbered slots.** The trim logic,
the rule handling and the reference block all already exist; what is missing is
the per-slot shot and scene text, which is what `VIEWS` does for turnarounds.
Roughly the same shape of change, one level up.

**This is now fix 7 in [`Prompt-Reliability-TODO.md`](Prompt-Reliability-TODO.md)**,
where it belongs — it blocks twelve images here and all fourteen of Captain
Jasu's, and until 2026-08-03 it was recorded only in this file, so the tooling
list did not name the item gating the most images.

**Section 1 and section 2 are not blocked** — `scale_portrait` at 18 KB is
borderline but workable, and the five turnaround views have proper short prompts.
Do those first regardless.

**The images are deliberately not "finished", and that is the right call.** Every
generation lands differently, and the build will change again with budget and
what the supplier actually has. The prompts and the character documents are what
holds — an image is a guide to the intent, not the intent itself. Regenerate when
useful, approve what is close enough, and do not chase pixel agreement.

What the build actually needs is settled:

- **Five hard pieces** — right forearm gauntlet, left shoulder cap, left thigh
  patch, and a pair of unmatched flank panels over her ribs. *Revised three
  times on 2026-08-01; the third is current — see `Character-Lock.md` v4.0.*
- **The flank panels lace across her centre front**, worn over the vest, with a
  **strip of vest cloth visible in the gap** — collar, placket and centre-front
  seam still readable. That gap is what makes them brigandine and not a corset,
  and it must not close. No breastplate.
- **The gauntlet is a SOLID 3D-PRINTED SHELL** with a **plain worn plate face,
  not a hexagon field**, and a small cluster of **dim amber telltales at the
  wrist**. It is the only rigid piece on the costume and the only light on it.
- **The shoulder cap HANGS LOOSE** — separate plates on a hand-cut backing,
  sitting away from the body, daylight under its lower edge. Never a moulded
  pauldron.
- **Five different metals** — dull grey steel (gauntlet), blackened iron
  (shoulder cap), dark bronze (thigh), pale worn pewter (right flank), rust-red
  oxidised iron (left flank). **No brass and no verdigris.** The mismatch is the
  point — and it lives *between* the pieces: **within one panel the metal is all
  one metal.**
- **The vest hide carries a faint serpentine grain** — in the material, tonal,
  visible only in raking light. Not the scale armour, and never a printed
  snakeskin.
- **Plates 10–15 mm**, regular hexagons, tessellated edge to edge, never
  overlapped, each carrying a raised snake swirl — **three or four variants
  repeating, not one per plate.** *Changed 2026-08-03 when the plates became a
  printed part: identical outline from one master, three or four swirl STLs in
  rotation, and all remaining variation comes from wear.*
- **Roughly 440 loose plates.** The printed gauntlet permanently removed ~150,
  and the restored flank panels put ~220 back. See `Costume-Build-Method.md` —
  still the largest hidden labour item in the costume, and the flank panels are
  half of it. Pattern them first.
- **WESTAR-35** on her right side; combat knife on her left hip.
- **Skin:** a faint scale pattern like a tattoo, ancestry tens of thousands of
  years back. Reptilian contact lenses are the highest-value make-up item.

Open, non-blocking: photograph the printed WESTAR-35 and add it under
`references:` in `outfits.yaml` — the entry is there, commented. And run a noise
test on the first finished patch; she is an infiltrator and 440 hard plates is
not obviously a quiet garment. The loose shoulder cap swings, and the flank
panels sit over her ribs, where she breathes.

---

## Before you run anything, read this

**Only about 8% of Shada's written specification currently reaches the image
generator.** Her `must_show` rules total **22,915** characters and the pasted
prompt carries roughly 1,800 of them.

*Re-measured 2026-08-03. This file said 11% of 18,061 — that was 2026-08-02, and
both numbers moved the wrong way: the specification grew 27% while the share
reaching the generator fell.* **The loss is no longer silent** — `short.py` now
names every dropped sentence on every run — but it is still a loss, and she is
the one character no plausible budget rescues. Zero trimming for her would need a
budget of 24,760 characters; nothing accepts that. **She needs fix 2: shorter
rules, with the prose moved to `Character.md`.** Three of the four
recorded failures were rules that existed and were correct but were trimmed away
before the generator saw them.

**Partly addressed 2026-08-02.** The proportion is unchanged — the rules are the
same length — but seven of the fourteen were re-ordered so the sentence that
does the work comes first. `trim()` always keeps the opening sentence and then
the first hard negation, so what survives is now chosen rather than accidental.
All fourteen rules land whole in the short prompt, with no ellipsis.

The fix list is [`Prompt-Reliability-TODO.md`](Prompt-Reliability-TODO.md).
Until item 2 there is done, expect to check generated images against the
**documents**, not against the prompt — the prompt is a lossy summary of them.

---

## Start here

```bash
cd /home/tris/tpof-design && ./tools/regen shada
```

**One command, not three.** `regen` runs all three generators, activates the
venv, commits, pushes, and prints the front prompt's path with the version line
its reply must open with.

This list used to name the generators individually, and it named only two of
them. `turnarounds.py` writes the long prompts; **`short.py` writes
`turnarounds-short/`, which is what you actually paste.** A run of the documented
two left the short prompts stale and reported success — the header even carried a
version stamp from the run that made the long file. That cost two images. The
fix is to stop typing the list.

Then open a **fresh** ChatGPT conversation — genuinely fresh, not a continuation
— and attach the references *before* pasting anything. A chat that has already
drawn another character in this production will carry that costume over; it has
happened once and it cost a full generation.

**The references are staged for you** in `03-characters/shada/prompts/attach/working/`.
Attach all of them. The list that used to sit here named two files and was wrong;
the folder is generated from the same list the prompt is, so it cannot drift.

**There is ONE approved costume reference, as of 2026-08-02:**

| File | Use it for | Ignore in it |
|---|---|---|
| `source/artwork/turn-working-front.png` | **Everything.** The whole costume: the grey cloth vest with its stand collar and centre-front placket, the palette, the plate size, the tessellation, the wear, the shoulder cap size, the flank panels laced across the front, the thigh patch, the belts, the trousers, the boots, and which side every piece is on | **The face**, which comes from the actor photographs |

*Why there is only one.* There were two DIRECTION photographs with different
scopes, and the generation of 2026-08-02 shows why that failed: with two
full-figure references competing over the same garment, the vest lost its stand
collar to a crossover wrap and a full layered skirt appeared over the trousers.
The written rules cannot win that fight. **One costume reference, and it is the
approved front.**

`costume-front-v2.png`, `flank-panels.png` and `costume-direction-front.png` are
kept on disk as history and **must not be attached to anything.** Every fault
they carried has been designed out — the smooth shoulder plate, the leather
forearm wrap, the oversized plates, the brown palette, the hide vest.

**It is not a face reference, and saying so is not optional.** A generation on
2026-08-01 came back in a perfect costume on the wrong woman because the costume
reference carried no scope. Any full-figure photograph attached to a prompt must
state what it is *not* for.

---

## Why the order is what it is

**The order itself lives in one place — [THE RUN LIST](#the-run-list--start-here),
above.** This section is the reasoning, and deliberately does not restate the
sequence; there were two numbered lists here until 2026-08-03 and keeping them in
step was a standing invitation to drift.

### Why the front is not regenerated

`turn-working-front` is DONE and APPROVED. It is the image every other view
matches against, and regenerating it would move the target under twenty images
that have not been made yet.

### Why `scale_portrait` is the makeup lock

**The costume has a lock. The makeup does not** — and this is the same gap that
cost this character her props, recorded below and fixed in `8c5bea7`. *Lock the
plates before the figures.* The face is the plates, here.

Two things the approved front does not carry, both noticed after it was approved:

- **The reptilian contact lenses.** Her eyes are plain blue in it. No slit pupil.
  This is recorded everywhere as the single highest-value item in her make-up.
- **The scale pattern on her neck**, which is nearly clear, while the pattern on
  her arms is **stronger and warmer in colour than the specification allows** —
  it should be *tonal*, the same colour as her skin, readable only in raking
  light. In the approved front it is a distinctly warmer tone than her skin.

**None of that is a reason to regenerate the front**, and doing so would be a
mistake. A slit pupil is a handful of pixels at full-figure scale and cannot
carry there; the front took seven passes to converge on silhouette, palette,
plate size, cap size, tessellation, wear and sides, and re-rolling it to chase
something that will not read risks all of it.

`scale_portrait` is a close portrait and it is the right instrument. Generate it
against the approved front, get the lenses and the neck right, and **approve it
as a second, scoped reference**:

| Reference | Scoped to | Not for |
|---|---|---|
| `turn-working-front.png` | The costume — everything below the collar | The face, the eyes, the neck |
| `scale_portrait.png` | **The makeup** — the slit pupils, the strength and colour of the scale pattern, and where it sits on the neck, jaw and collarbone | The costume |

Two references with **stated, non-overlapping scopes** is not the failure that
cost five generations. That failure was two references competing over *the same
garment*. Scope is what makes the difference, and it has to be written down.

### Why the four views are matched, not re-derived

Generate each view *against the approved image* rather than from the prompt
alone. This is the method Captain Jasu's set proved: her five pass the mirror
check, and every character generated view-by-view from prompts alone got five
near-misses.

### Why the plates come before the rest

`blaster` and `material-scale` define the two changed objects. Once approved they
become prop references in their own right, and everything after them is generated
with those plates attached as well as the front. *Lock the plates before the
figures* — the order correction from `8c5bea7`.

### `forest` is still owed a dusk frame, and the question has changed

It came back as a daylight camp, so the slot's question is still open and it now
overlaps `camp_day`. **The palette change on 2026-08-02 makes this more urgent,
not less.** The old risk was that a charcoal costume would vanish into shadow;
the new risk is that a grey-green and khaki one vanishes into wet foliage. For an
infiltrator that is arguably correct in-world and bad for the camera, and only
this frame settles it. If it returns a six-panel collage again, that is the
prompt length talking: say *"one frame, not a contact sheet"* when you paste it.

---

## How to check a back view

The old version of this file had a table here demanding that each item stay on
the **same side of the frame** in front and back views. That was wrong, and it
would fail a correct image.

When she turns around, her right side moves from the viewer's left to the
viewer's right. **The frame sides swap. What never changes is which of *her*
sides carries the item.** In a back view:

| Element | Her side | Back view: viewer's |
|---|---|---|
| Printed gauntlet | right forearm | **right** |
| Loose shoulder cap | left shoulder | **left** |
| Flank panels | both sides | **both** — but still unmatched |
| Thigh patch | left thigh | **left** |
| Blaster | right thigh | **right** |
| Knife | left hip | **left** |

Note that a horizontal flip of the front view *also* swaps the frame sides, so
frame position cannot catch a mirror. What catches it is anatomy: a real back
view shows shoulder blades, the back seams of the vest, rear pockets and the
back of her head. A mirrored front shows her face and the front closure.

The `turn-working-back` in the repository passed both tests, but predates the
2026-08-01 revision and shows the superseded build.

---

## Then rebuild

```bash
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
```

`--validate` catches missing images **and overlapping panels**. Both clean before
building.

---

## What still needs regenerating

**The 2026-08-02 lock invalidated more than the previous revisions did**, because
the palette and the vest material are visible in every frame that shows the
costume at all — not just the ones showing armour detail.

**Leave alone — nothing in them changed:**

`knife` only. It is unaffected and is already locked as a prop reference.

*`species_strip` and `expression_strip` were listed here until 2026-08-03 and are
not any more — both contradict the make-up lock. They are STEP 4 of the run list.*

**Regenerate — the costume in them no longer exists:**

| Image | Why |
|---|---|
| ~~`turn-working-natural`, `left`, `right`, `back`~~ | **DONE 2026-08-03.** Matched against the approved front. Do not regenerate any of the five |
| `hero`, `camp_day`, `forest`, `maintenance`, `scale_figure` | Full figure — cloth vest, grey palette, plate size, cap size, wear |
| `scale_portrait` | Shows the collar, the shoulder and the vest cloth |
| `material-cloth` | It is now a grey woven cloth with the serpentine grain in the weave, not a brown hide with it pressed in |
| `material-leather` | Taupe, not warm brown |
| `material-scale` | Hexagons with a pressed stamp, tessellated flat, with plates missing |
| `material-hardware` | Palette |
| `blaster`, `utility` | The WESTAR-35, and the taupe leather |
| `tone-collage` | Everything above |

**The front turnaround is APPROVED in `outfits.yaml`.** Every image above matches
against it.

`tone-collage` is slot 16, the new **share sheet** — one image, six panels, for
sending to people on a phone. It is not on any board and is never used as a
costume reference. Every character now has this slot.

---

## Watch for

The failures that keep recurring:

- **Plates that shingle.** They butt edge to edge in one flat plane with a thin
  dark line of backing between them — no plate rides over another and none casts
  a shadow onto its neighbour. "Never overlapped" was in the spec for days and
  never worked; what works is describing what tessellation *looks like*.
- **Chain mail.** The opposite over-correction, and it arrived within one
  generation of fixing the size. Twelve plates across a flank panel is the
  **floor** as well as the target — any finer and the plates lose their edges.
- **A leather vest.** It is cloth now, and it creases where the hard pieces bear
  on it. If it reads as hide, the base layer has become armour.
- **A brown costume.** The leather especially drifts warm on nearly every
  generation, and warm leather drags the whole palette back to where it started.
- **Armour that looks laid out.** Plates are missing, bent and badly repaired.
- **A shoulder cap creeping down the arm or in toward the collarbone.** It is a
  palm's width, on the point of the shoulder. This is how a yoke returns under
  another name.
- **The thigh patch as a solid patch.** It is a field of the same small plates.
- **A skirt, tabard or apron over the trousers.** New on 2026-08-02, and the
  largest silhouette failure so far. The trousers were the last sentence of the
  boots rule and the trim cut them from every short prompt, so nothing described
  her lower half at all. Now the first sentence of that rule.
- **The gauntlet and the shoulder cap swapped over.** Her right forearm, her
  left shoulder, always. On 2026-08-02 they exchanged sides while the blaster
  stayed correct, so it was not a mirrored image — the two pieces simply read as
  interchangeable. They are on opposite sides on purpose.
- **A crossover or V-neck vest.** Stand collar and a concealed placket straight
  down the centre front. The collar sentence used to be trimmed away.
- **Another character's costume entirely.** Captain Jasu's horns, shoulder yoke,
  quilted sleeves and matched bracers arrived on 2026-08-02 from a shared
  conversation. **Use a fresh chat for every character** — the prohibitions in
  the prompt are a backstop, not the fix.
- **A yoke, or panels that climb onto the chest.** The scale panels are
  lower-torso only: ribs, waist and hip, never above the armpit.
- **The wrong face.** The single most expensive failure so far. The costume
  photographs are not face references; the actor photographs are.
- **A laced or leather gauntlet.** It is a solid printed shell now. One
  gauntlet, her right, and her left forearm is bare.
- **Flank panels that close up in the middle.** The strip of vest cloth in the
  lacing gap is what stops them reading as a corset.
- **A panel speckled with four metals.** One panel, one alloy. The mismatch is
  between the five pieces.
- **A glowing gauntlet.** Two dim amber pinpoints at the wrist. No lit seams, no
  edge lighting, nothing spilling onto skin.
- **A shoulder cap moulded to the shoulder.** It hangs loose and light gets under
  it.
- **Shoulder caps on both shoulders.** One cap, her left — the opposite side to
  the gauntlet. This is the rule doing the most work in the design: symmetry
  quietly turns scavenged mismatch into a costume somebody made for her.
- **A bulky silhouette.** Close-fitting, cut to the figure.
- **Any interior except the Sabacc hold.** Forest, clearing or camp — with the single exception of slot 2, Scene 10, which moved inside the ship on 2026-08-01. Anywhere else, a wall or ceiling is wrong.
- **A modern coil zip.** Industrial hardware, or hooks and lacing. Still slipping
  through on nearly every frame — the one recurring fault not yet beaten.
- **The blaster on her left.** It is on her right thigh; only the knife is on her
  left.
- **Pieces in the same metal.** Steel gauntlet, iron cap, bronze thigh, pewter
  and rust-red flanks. They drift toward matching brass, and there is no brass on
  this costume.
- **Metal on her chest.** The flank panels sit at the SIDES, over the ribs. Her
  sternum, her centre front and the middle of her back stay plain cloth — a chest
  patch, bib, pendant or breastplate is still wrong.
- **Printed snakeskin on the vest.** The grain is in the hide, faint and
  irregular, or it is not there at all.

Two or more together almost always means **the references were not attached**.

---

## The gap this character exposed — props have no lock. **Built 2026-07-31.**

**The costume had an approved reference image. The props did not**, so the
blaster, the knife and the scale patches were described in words and redrawn from
scratch every time. Words cannot hold a silhouette; only an image can.

Fixed in commit `8c5bea7`. `outfits.yaml` now carries a `references:` list
alongside `approved:`, and both `split.py` and `turnarounds.py` emit an operator
line naming every plate to attach. A declared reference that does not exist
raises a warning, since the prompt would otherwise tell the operator to attach a
missing file.

Currently locked: `material-scale.png` and `knife.png`.

**The blaster is deliberately not locked.** `blaster.png` is a decent plate but
it does not match the printed prop — the physical WESTAR-35 has brass panels let
into the slide, a blue panel and a black textured grip. Attaching it would lock
every image to a gun nobody is building. The entry sits commented in
`outfits.yaml`, pointing at `reference/props/westar-35.jpg`, to be uncommented
once the prop is photographed.

**The general rule, which has now come up twice: for anything physically built,
the reference is a photograph of the build, not a render.**

Baylan inherits this for free — but he needs his own plates locked before his
figures, not after. He carries a blaster, a holster and a rifle: the same drift,
multiplied across every view.

---

## After Shada

Baylan is next.

**Done 2026-08-01: he is `handedness: right`, and his costume carries
`must_show:`.** The placement checker is silent on him. Blaster on his right hip,
rifle slung to fall to his right hand, pouches on his left off side. Recorded in
`Character.md`, `Character-Lock.md` and `outfits.yaml`.

**He was also collapsed to ONE costume that day** — the robe is a removable layer,
and the separate Scene 12 Jedi build is dropped. Five turnarounds, not twenty.

Still owed before those five turnarounds:

- **Lock his plates first, then his figures.** This is the order correction from
  `8c5bea7` and it matters more for him than it did for Shada: he carries a
  blaster, a holster and a rifle, and words will not hold three silhouettes
  across eighteen images. Generate `blaster`, `crystal` and `utility`,
  approve them, add them to `references:` in `outfits.yaml`, and only then start
  the figures with all of them attached.
- **A `promo-data.yaml`.** Copy Shada's, keep the structure, replace the copy —
  see `tools/board-generator/README.md`.

**Shin is now the character with the placement checker warning against her** — no
`handedness:`, and no `must_show:` on any of her three states. Same job, same
half hour.
