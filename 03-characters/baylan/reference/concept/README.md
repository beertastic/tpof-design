# `concept/`

Production drawings and scoped design references.

> **SUPERSEDED 2026-08-05 — the reference exists. Skip to "CUT AND WIRED IN"
> below.** This section is kept because its reasoning about cropping is still
> the method, and because it records what was believed before anyone had looked
> at the garment.

## WANTED: the chevron geometry — 2026-08-04

**Drop a still of the later costume's CHEST here.** The first generation got the
chevron panel wrong in four ways at once — too many bands, too narrow, embossed
rather than built from separate pieces, and no stitching — and words have now
failed at it twice. Only an image holds a shape.

This is legitimate and it is not a contradiction of `do_not_retrieve`. **This
film is the origin of that costume** — `outfits.yaml` says so outright, and
`02-story/Planted-Elements.md` records the echo. The chevron plastron is the
planted element that becomes the later garment, so matching its geometry is the
point.

**IT MUST BE CROPPED BEFORE IT IS ATTACHED, AND CROPPED HARD.** Chest only: no
head, no shoulders-and-up, no full figure, no robes, no hood, no silhouette.
Everything `do_not_retrieve` refuses — the bearing, the silver hair, the monastic
sleeves, the gravitas — arrives with an uncropped still, and it arrives more
strongly than any sentence refuses it.

That is the method this repository already uses twice:

- Jasu's `reference/headdress/horns-authority-2026-08-04.png` — cut above the
  collar so no costume is left in frame to compete with the approved front.
- Shada's `scale_portrait.png` — the make-up lock, with no costume in frame at
  all.

**Both carry a scope line, and this one will too:** *authoritative for the
chevron band geometry ONLY — their count, width, angle and construction. Nothing
about the wearer, the garment around it, the colour or the bearing.*

Save it here as `chevron-geometry-source.png`. It gets cropped, scoped and added
to `references:` in `outfits.yaml`, and from then on it is attached to every
costume slot.

---

## CUT AND WIRED IN — 2026-08-05

**`chevron-geometry-source.png` exists.** It is attached to every `working`
view via `references:` in `outfits.yaml`, and it is the first thing in
`prompts/attach/working/`.

### The source is NOT a screen still, and that is a better answer

Everything above this line worries about cropping a frame from the other
production hard enough to strip the bearing, the silver mane, the hood and the
monastic sleeves — everything `do_not_retrieve` refuses, and which arrives more
strongly than any sentence refuses it.

**The source used instead is a costume-reproduction product photograph on a
MANNEQUIN.** There is no head in it, no face, no posture, no actor and no
performance. The retrieval risk the whole section above is about simply does not
exist in the frame. Cropped to chest and shoulders, there is nothing left to
leak.

**THIRD-PARTY REFERENCE**, same status as Jasu's `reference/props/a180.jpg`: a
reproduction of the later costume, not our build and not our photograph.

### What eleven fronts got wrong, and what the reference settled

Looking at it changed three rules, and **two of them we had written ourselves in
the previous forty-eight hours**:

| Rule | Said | The reference | Now |
|---|---|---|---|
| 6 | panel NARROWER than his shoulders, *"NEVER shoulder to shoulder"* | a BROAD plastron almost armhole to armhole | rewritten |
| 9 | the plain area above is SMALL, *"never a broad empty field of cloth"* | **a large plain yoke fills the top half** | **reversed** |
| 11 | QUILTING — *"NO separate pieces laid on top, NO hard edges, NO cast shadows"* | separate overlapping panels, piped edges, real shadows | **reversed** |

**Rule 9 is the one to remember.** It was raised on 2026-08-04 *because* three
generations had put a broad empty yoke above the bands. **The generator was
reproducing the real garment and was corrected away from it, three times.** Every
other fault on this costume was found by reading the trim report or measuring
the image; this one was found by assuming the rule was right because it kept
losing. **"It keeps doing X" is evidence, not disobedience** — and without a
reference there was no way to tell the two apart.

### The count stopped being a number

Eleven fronts chased "exactly five" and never got it, because **five is not a
countable feature of the object.** Depending on whether the yoke's lower edge
and the piping count as outlines, the reference reads as three, four or five —
and the Production Designer confirms the number varies across published images.
The rule now says **THREE TO FIVE broad bands below the yoke**, which is what is
actually true and cannot be missed.

### The green is real

Confirmed 2026-08-05: it is on the screen costume, it is *very* subtle, and the
Production Designer had to be told it was there. So the target is **findable
when looked for** — not absent, and not announced. The old wording, *"findable
only in close-up"*, was an instruction to be invisible in a full-length view and
was obeyed eleven times: measured on the eleventh, peak green bias 4.5 against
15–40 for a real green thread.

Applied panels help here rather than hindering. The green is now the thread
**sewing the panels down**, which is what P5 asks of it — *"the thread holding
the chevron panels"*.

### Known over-attachment

`references:` attaches to **every** slot, including the object plates —
`blaster`, `crystal`, `utility` and `gauntlets` — which have no chest in frame.
`reference_list()` has no slot filter and adding one would change prompt output
for every character, including Shada's and Jasu's approved plates. **Left as-is
deliberately**, on the same reasoning as the `trim()` case-sensitivity bug. The
scope line carries the mitigation: *NOT the garment*, and those prompts have no
costume rules attached at all.

---

## `costume-best-so-far-2026-08-10.png` — WIRED IN, FIRST ATTACHMENT

**The best front so far**, accepted by the Production Designer on 2026-08-10:
*"the 'skirt' is still too long, but the rest is great."* No coat, no cloak.

It is first in `references:` and therefore attachment 1 in
`prompts/attach/working/`, ahead of `chevron-geometry-source.png` — **and it
outranks that image wherever the two disagree.** This is his garment, eighteen
years old and filthy; that one is a shop-new reproduction on a mannequin. The
chevron source stays because it still holds the band geometry more clearly than
a full-length plate can.

### Why it is a scoped reference and NOT an approval

An `approved:` block's scope is **the whole costume** — that is what gives it the
power to make every other view match it exactly. Approving this plate would
therefore lock in the one thing on it that is wrong, and rule 18 would spend the
rest of the turnaround arguing with a photograph it cannot beat. A scoped
reference is the mechanism for a plate that is right about most of itself.

**The scope names the exception in the label:** *the whole costume EXCEPT the
length of the two hip panels* — they hang near mid-calf in it and must reach a
third of the way from belt to knee.

### What it exposed — a rule that contradicted its own checkline

The panels came back at mid-calf because **the prompt asked for two different
lengths at once.** Rule 18's `text:` said *"hem level with his fingertips"*;
checkline 11 said *"ONE THIRD from belt to knee"*. Those are not the same
measurement — fingertips is roughly mid-thigh, about twice the depth — and
`description:` said fingertips too, making it two to one for the longer one.

The comment above the rule had argued for the belt-to-knee fraction and the
`check:` was rewritten to match. **The `text:` never was, and the `text:` is the
part the generator reads as specification.** Both then shipped in every prompt.

Given two irreconcilable numbers the generator obeyed neither and fell back on
what a hip panel usually looks like, which is longer than both. All three
statements now carry the fraction, and *fingertips* is gone for the same reason
*"upper thigh"* and *"a hand's width"* went before it — an arm length on a body
it is inventing is not something it can measure in the picture it is making.

**Worth checking on any rule with a `check:` line**: the two are written months
apart and nothing verifies they still agree.

---

## `chevron-construction-intent-2026-08-05.png` — ON DISK, NOT ATTACHED

The Production Designer's own reference for the construction he wants: the
chevrons as **overlapping lames**, each band standing proud of the one below
with a thick cut edge throwing a real shadow down onto it. It is a generation
from this pipeline, not a third-party image.

**IT IS DELIBERATELY NOT IN `references:`, AND THE REASON IS THE BRACES.** The
frame shows the shoulder harness that was removed from the costume hours later,
and it runs vertically straight through the chevron panel — there is no crop
that keeps the panel and loses the straps. Attaching it would put back, by
photograph, the exact thing the words now refuse; and a photograph beats words,
which is the whole reason references work.

So the construction is carried by rules 11 and 12 instead — *"like the lames of
a plated coat"*, and the leather/suede alternation. **If a generation misses the
relief, revisit this decision rather than rewording again**: the lesson from the
chevron count is that only an image holds a shape, and the cost of attaching
this one is a costume change we would have to undo.

**Also of record: the material alternation started here.** The Production
Designer asked to *"alternate the chevrons with leather and suede, making the
colours pop and stand out"*, and flagged it as a possible contradiction with the
near-black palette. **It is not one.** Smooth leather catches light and napped
suede eats it, so two pieces of identical tone read strikingly differently side
by side. The contrast is FINISH, not colour — which is what lets the panel come
alive without giving him anything bright to be noticed by.
