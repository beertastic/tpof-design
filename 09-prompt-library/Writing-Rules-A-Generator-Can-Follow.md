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

**Write the sentence that does the work as the opening sentence.** If a rule has
two load-bearing ideas, it is two rules.

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
