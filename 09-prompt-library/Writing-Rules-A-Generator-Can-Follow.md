# Writing Rules A Generator Can Follow

Canonical guidance for anyone writing or editing a `Prompts.md` or a `must_show`
rule. **This is not a block to paste** — it is how to phrase the blocks.

Everything here was paid for. Each rule below cost at least one wasted
generation, and several cost three.

---

## 1. A rule the generator can MEASURE beats a rule it has to INTERPRET

The single most reliable finding in this project. It landed three times in three
unrelated domains on 2026-08-03 alone.

| Interpreted — failed | Measurable — worked |
|---|---|
| "Plates 10–15 mm" | **"TWELVE across a flank panel"** |
| "The crest comes up to her waist" | **"Level with the bottom of her belt"** |
| "A raised snake swirl" | **"A blank plate means the image has failed"** |

**The creature case is the cleanest evidence.** The same prompt produced 0.78 m
twice from "comes up to her waist", and 0.87 m first time from "level with the
bottom of her belt" against a 0.85 m spec. Nothing else changed.

**A belt is in the frame. A waist is an idea.** Millimetres cannot be counted in
an image; plates across a panel can. Anchor to something the generator can see
and count in the picture it is making.

**Corollary: the landmark must be recomputed per subject.** "Level with her belt"
is right for a 155 cm character and wrong for a 198 cm one — the same animal
reaches the tall character's mid-thigh. A landmark works *because* it is specific;
standardising it destroys the mechanism. See
[`08-species/akk-dog/Creature.md`](../08-species/akk-dog/Creature.md).

### 1b. When the note says "10 cm", find the 10 cm object already in the frame

Added 2026-08-05, after **five** failed attempts to shorten one garment.

The Production Designer asked for hip panels "about 10 cm" deep. Everything that
described a *size* or a *position* failed, in a very consistent way:

| Wording | Result |
|---|---|
| "Upper thigh only, barely past the seat" | mid-thigh |
| "One third of the way from the belt to the knee" | two thirds |
| "Level with the bottom of the holstered blaster" | **longer than before** |
| "No deeper than the belt above them is wide" | *under test* |

**Even a landmark fails if the landmark's own size is not fixed.** The holster
is in every frame, which is why it looked like a good answer — but the generator
draws the blaster at whatever size it likes, so "level with the bottom of it"
inherits that variability. A landmark only works if **its size is pinned by
something else.**

**The belt is pinned.** It is specified as *broad salvaged leather*, it is drawn
at a consistent width, it is directly above the thing being measured, and a
broad belt is about 10 cm — so it IS the ruler the note was asking for. The same
belt now fixes three separate measurements on this costume: the panel depth, the
gap between the lowest chevron and the belt, and by extension the "10 cm higher"
the chevron block was asked to move.

**Method: convert the real-world figure into "about as big as X", where X is an
object of known size that is already required to be in the picture.** It turns a
measurement into a comparison, and comparison is the only spatial operation that
has reliably worked on this project.

### 1a. A COUNT cannot hold a layout. The SIZE holds it, and the count follows

Added 2026-08-05, after **nine** attempts at a five-band chevron panel that came
back with seven, then six.

The rule said FIVE, and EXACTLY FIVE, and led with it, and was in the check
block. It never worked. **The count was never the operative instruction.** Five
bands filling a panel is a consequence of how wide a band is — so given the
number alone, the generator satisfies it and then resolves the leftover space
however it likes. That is not disobedience; **it is an underspecified layout.**

**But the size must be expressed IN TERMS OF THE THING IT DIVIDES.** This is
where the first attempt at the fix still failed:

| Attempt | Result |
|---|---|
| "EXACTLY FIVE bands" | seven |
| "EXACTLY FIVE, each a BROAD BAND A HAND'S WIDTH, touching" | **six** — broader, and touching, but still not five |
| "EXACTLY FIVE, each band ONE FIFTH OF THE PANEL'S HEIGHT, so the five fill it exactly" | *under test* |

A hand's width is rule 1's failure in a new costume: **a real-world unit against
a body the generator is inventing.** Measured off the six-band image, the panel
was ~512 px and the bands ~77 px — 512 ÷ 77 ≈ 6.6, so it picked a plausible band
width and filled. Nothing was disobeyed.

**"One fifth of the panel" makes the count and the size the same statement.**
They can no longer disagree, and there is no unit to convert. Where a fixed
number of things must fill a fixed space, **give the fraction, not the tally.**

---

## 2. Say it POSITIVELY. A prohibition alone has never been enough

"Never overlapped" sat in the specification for days and never once worked.

What worked was describing what the correct thing **looks like**:

> Every plate lies FLAT IN THE SAME PLANE as its neighbours, six flat sides
> butted against six flat sides. Between two plates there is a THIN DARK LINE
> showing the backing beneath, and nothing else.

Keep the prohibition — add the description. A generator cannot draw an absence.

---

## 3. Name the failure condition explicitly

Give the generator a test it can apply to its own output before it commits.

- *"A blank plate means the image has failed."*
- *"If the object in frame could be put on, the image is wrong."*
- *"If she could sit on it, the scale is wrong."*
- *"If it reads as black leather, it is wrong in the other direction."*

That last one matters: **bound the fault in BOTH directions.** A rule that only
says "not too warm" gets obeyed by going black. The leather came back at 17%
value against a 24–33% costume range because nothing said it could be too dark.

---

## 4. Uniform in shape, never uniform in condition

Three different assets hit this in one day — a printed hexagon plate, a costume
material, and a living creature. Each time, uniformity that was *correct* in
geometry read as *manufactured* because the finish was uniform too.

> THE SHAPE IS UNIFORM; THE WEAR IS NOT.

Wherever a thing is deliberately regular — printed, stamped, milled, moulded —
the prompt must say in the same breath where the variation lives instead: paint,
chipping, how far a ridge has worn down, which pieces are missing, which were
replaced later in something else.

**This applies to creatures as much as props.** An animal rendered clean and dry
in a wet forest reads as CG for exactly this reason, and the fix is the same
sentence.

---

## 5. Put the load-bearing clause FIRST

`trim()` keeps a rule's opening sentence and then its first hard negation.
Everything else is a candidate for deletion at any cap.

Four documented failures were rules that **existed, were correct, and were cut
before the generator saw them**:

| Lost clause | Where it was |
|---|---|
| The trousers | last sentence of the boots rule |
| The reptilian slit pupil | last clause of the face rule |
| "Salvaged and worn, never machined" | last sentence of the longest rule in the file |
| "Wet forest, forest clearing or the camp among the trees" | middle sentence of the exterior rule — so a whole shoot came back as desert |
| "Each is a BROAD BAND A HAND'S WIDTH" and "They TOUCH: no cloth shows between them" | last two sentences of Baylan's chevron rule — **six generations were spent rewriting a rule whose operative clauses were never arriving** |

**Write the sentence that does the work as the opening sentence.** If a rule has
two load-bearing ideas, it is two rules.

### 5aa. "It keeps doing X" is EVIDENCE. Check the source before you forbid X

Added 2026-08-05, and it is the most expensive lesson in this file.

Baylan's rule 9 was raised because **three generations put a broad plain yoke
above the chevron bands**. It was read as drift and forbidden by name: *"the
plain area above them is SMALL — a shallow yoke just under the throat, NEVER a
broad empty field of cloth."*

**The reference, obtained eight generations later, has a large plain yoke filling
the top half of the panel.** The generator had been reproducing the real garment
three times running and was corrected away from it — after which nothing on that
panel was ever right again. The same day, rule 11 forbade *"separate pieces laid
on top, hard edges, cast shadows"*; the real garment is applied overlapping
panels with piped edges casting real shadows.

**A model repeating itself is not necessarily disobeying. It may know the
subject.** That is the whole reason `do_not_retrieve` exists — retrieval is
strong enough to need refusing when it is wrong, so it is strong enough to be
right when it is right.

**Before writing a rule that forbids a recurring behaviour, get one look at the
source.** Where the subject is a real object that exists, the cost of checking is
minutes and the cost of not checking was eleven generations here.

### 5a. Before rewriting a rule that keeps failing, check that it ARRIVED

Added 2026-08-05. **A rule can fail because of a clause that was never sent.**
Baylan's chevron count was rewritten six times, tightened, promoted and put in
the check block, while the two sentences that actually controlled it were being
cut every single run — and `short.py` had been printing the drop on every
regeneration the whole time.

**Read the trim report before touching the words.** `./tools/regen <character>`
names every dropped sentence and gives the coverage percentage.

### 5b. `trim()` ranks by SHOUTING, and it is case-sensitive

The hard-negation detector is `\b(NOT|NEVER|NO|NOTHING|ONLY|ALWAYS|MUST)\b` with
no `re.I`. **Lowercase negations are invisible to it** and rank as ordinary
prose, so they are dropped first. *"not a thin stripe, not a painted line"* was
cut for exactly this reason.

This is **left as-is deliberately** — fixing the regex would change prompt output
for every character including Shada's and Jasu's approved plates. It suits the
house style anyway. **Shout the negation you cannot afford to lose.**

### 5c. A reference's scope label is cut at 52 characters, first sentence only

`_label()` keeps only the first sentence of a reference's `what:`, capped at 52
characters. Everything after it is for the long prompts and **never reaches the
short ones.**

So the refusal goes in the first sentence, not after it. A photograph of an
unpainted 3D print attached with the label *"THE BLASTER — SHAPE, PROPORTION AND
COMPONENT LAYOUT"* is an instruction to make the weapon bare grey plastic. The
working version is **`THE BLASTER — SHAPE ONLY, NEVER ITS COLOUR OR FINISH.`**

---

## 6. Every attached image needs a stated SCOPE, and scopes must not overlap

Two full-figure references competing over one garment cost five generations. The
fix was not better rules — the written rules cannot win that fight — it was one
reference per question, each labelled with what it may and may not be trusted for.

- `COSTUME (match exactly)` — **not the face**
- `THE MAKE-UP — NOT THE COSTUME`
- `PLATE SHAPE AND FINISH — NOT SIZE`
- `THE WESTAR-35 — ITS SHAPE ONLY, NOT ITS FINISH`

**A reference with no scope teaches everything in it**, including the parts that
are wrong. The stock WESTAR-35 photograph carried a brown grip and no brass —
both recorded faults — and only the scope line stopped it teaching them.

**And check what a reference actually teaches before attaching it.** A macro crop
of fourteen plates teaches "big plates" whatever the caption says. A Funko Pop
teaches a 1:1 head-to-body ratio.

---

## 7. Name what to KEEP, not only what to change

Every correction that named a single fault fixed it and quietly traded away
something else. Roll two of a turnaround fixed the plate size and the boots, and
swapped the blaster and knife onto the wrong sides while doing it.

A correction should read as a diff:

> **KEEP EXACTLY AS IT WAS:** …
> **CHANGE TWO THINGS ONLY:** …

---

## 8. Compose a frame, not a plate

A narrative image described only by its content comes back centred, eye-level,
flat-lit and fully in frame — which is a reference plate with scenery. Films do
not look like that. See [`Cinematic-Framing-Block.md`](Cinematic-Framing-Block.md).

---

## Where this came from

Recorded 2026-08-03, after a day that produced twenty-one finished images for
Shada and the project's first two-subject frame. The failures behind each rule
are logged in
[`11-production-tracking/Prompt-Reliability-TODO.md`](../11-production-tracking/Prompt-Reliability-TODO.md)
and in the per-character image TODOs.
