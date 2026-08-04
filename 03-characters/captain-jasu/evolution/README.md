# Captain Jasu — evolution

How her design converged. **History, never specification** — the design lives in
`Character.md`, `outfits.yaml` and the approved reference. Per
[`../../README.md`](../../README.md), **never attach a SUPERSEDED image from this
folder to a generation prompt** — the latest pass is the exception, and pass 03
below relies on it.

## 05 — THE HORNS GO TO A COMPARISON, 2026-08-04

**Staged, not yet run.** Paste `05-horns-funko.txt`, attach all 5 files in
`attachments/05-horns-funko/`, save the result as `05-horns-funko.png`, then
compare it against `../source/artwork/turn-field-front.png` side by side.

### Why

The Production Designer settled the horn spec on 2026-08-04 — **trophies and
bone, exactly two, one each side, both curved, alike in curve, colour and size
but officially different objects, each a third to a half the height of her
head** — and then said the thing that mattered more: **the horns on the painted
figure in `../reference/build/` are the ones they like**, wanted de-polished so
they read as taken off a real animal.

**Nothing generated has ever looked like that figure.** Its horn is a broad
flattened blade sweeping up and back and tapering to a fine point. Every
generated plate shows a chunky curved loop hugging the ear. Same colour, same
rough size, completely different object — and the difference is only obvious
once the two are put beside each other at the same scale.

**The figure was detached on 2026-08-03 for a good reason and the wrong remedy.**
Its 1:1 head-to-body ratio is exactly how a 155 cm woman becomes a caricature.
But that is a property of the *figure*, not of the *horns*. **The fix was to crop
to the horns, not to throw the plate away** — the method Shada's make-up plate
established, and the one used on `../reference/headdress/horns-authority-2026-08-04.png`
the same afternoon. The crops are now at
`../reference/headdress/funko-horn-side.png` and `-front.png`.

### The scope, and it is the same trick that settled the boots

The pass attaches the approved front — which a front view normally must not be
given — because **the costume has to be held still so the only variable is the
horns.** The prompt then overrules it on the horns alone, in the wording proven
on 2026-08-03:

> *"ON THE HORNS, AND ONLY THE HORNS, THE COSTUME PHOTOGRAPH IS WRONG AND THE
> TWO FIGURE PHOTOGRAPHS OVERRIDE IT."*

**And a second scope on top of it, because the figure is a toy:** take the shape
and placement of the horns and *nothing else* — not the head, the face, the
proportions, the hair, the paint or the scale. Rule 2 governs the head
absolutely.

**Shape from the photograph, surface from the words.** The figure's horns are
painted flat white, which is wrong; the written rule supplies bone, matte,
yellowed, pitted and age-cracked. This is the split the A180 already proved —
a reference photograph fixes a silhouette that four generations could not get
from words, and the words still govern the finish.

### What to judge

**Silhouette, and only silhouette.** Does the blade read as something taken off
an animal, or as an ornament? Put it beside the current front at the same size —
that comparison is the decision, not the documents.

### Two things to watch

- **A photograph beats a paragraph**, which is why this test exists at all. The
  risk is the reverse of the boots test: the costume attachment may simply
  redraw its own looped horns and ignore the figure. **If the horns come back
  unchanged, the test has not run** — re-roll before comparing.
- **The figure appears to carry a smaller secondary point below the main blade
  on at least one side.** The settled rule says exactly two horns, one per side,
  so the prompt asks for the blade only. If the pass comes back with extra
  points, that is the figure winning over rule 16 — and worth a decision rather
  than a re-roll, because it may be what was liked about it.

---

## `attachments/` — one folder per pass, drag it in

Each pass has its files staged under `attachments/<pass>/`, numbered and named by
what each one is FOR, with a `MANIFEST.txt`. Same idea as `prompts/attach/`, which
`short.py` writes for the generated prompts.

```bash
./tools/stage-evolution-attachments captain-jasu
```

**Run that after a fresh clone.** The folders are gitignored — they are copies of
images already in the repository — and unlike `prompts/attach/` nothing else
rebuilds them. The script reads each prompt's own URL block, so the staged folder
cannot drift from the prompt: change the prompt, run it again.

> **It found a fault the first time it ran.** `01a` and `01b` stage only **two**
> files, because their URL block never listed the costume photograph — the
> instruction to attach it was in prose only. The test still worked, because the
> operator attached it by hand from this README, but anyone falling back to the
> URLs would have generated without it and got a drifting costume. `02` and `03`
> list all three properly.

| Pass | Variable | Result |
|---|---|---|
| `00` | *(not a pass)* — the **first approved front**, 2026-08-01, kept as the starting point | Superseded 2026-08-03. **Do not attach it to anything** |
| `01a` / `01b` | **The boots — tall to the calf, or ankle** | **TALL WINS, 2026-08-03.** `01b` was never needed — `01a` settled it on sight. Now the default in `outfits.yaml` |
| `02` | **Correction pass — tall boots, flat heel, one whistle at the throat, hair UP** | **Generated 2026-08-03. Three of three landed and the costume held still.** The hair came back too high — see below |
| `03` | **The hair alone — lower and rougher** | **Generated 2026-08-03. Landed exactly as asked — and the answer was that the whole direction was wrong.** Costume is correct in it |
| `04` | **Hair back DOWN — costume from `03`, hair from the original** | **GENERATED AND APPROVED 2026-08-03.** Now `source/artwork/turn-field-front.png` |

## The result

**`01a-boots-tall.png` — approved as the answer to the boot question, and it
carried three other things with it.**

**The test ran properly, which was the thing at risk.** The prompt attached the
approved front — which shows ankle boots — and told the model to override the
photograph on the footwear alone. It did. Tall boots came back against a
reference showing low ones, which means the scoped-exception wording works and is
reusable the next time a single item has to be changed against an approved image.

**Variant B was not generated.** The tall boot was obviously right in the frame:
she is 155 cm and skin-tight from collar to ankle, so the boot shaft is the only
horizontal break in the leg, and it reads as deliberate rather than as
foreshortening. Recording that `01b` exists and was skipped, so nobody assumes a
comparison was made that was not.

### Two faults the image exposed, both now fixed in `outfits.yaml`

- **TWO WHISTLES.** One correctly at her throat from the new rule, and one still
  at her belt, carried over from the approved photograph. Adding the throat
  whistle did not remove the belt one, because **nothing said there was only ever
  a single whistle.** The rule is now `EXACTLY ONE WHISTLE`, with the belt named
  as carrying no second one.
- **HEELED BOOTS.** The component note has said *"flat"* since 2026-08-01 — and
  **a build note cannot reach a generator.** There is now a heel rule in
  `must_show`, and the component note gives a number and an instruction:
  re-heel a boot that is right in every other way, because that is a cobbler's
  job and cheaper than the boot.

**The hair is still down and loose in this image, and that is correct behaviour
here** — the prompt told the model to match the approved photograph on everything
except the boots, and the approved photograph has her hair down. It is not
evidence about the hair rule either way. That fault is tracked separately.

### What this image is not

**It is not the new approved front.** It has two whistles and heeled boots. The
front has to be re-rolled against the corrected rules and re-approved before
anything else is generated from it.

---

## 01 — the boot test

**Why it exists.** The approved front turnaround shows **ankle boots**. Both
`outfits.yaml` and the `components:` build list say **"Boots — tall, close to the
calf"**. They have disagreed since 2026-08-01 and nobody saw it, because the
boots sentence sat eighth in a 2,166-character rule and **was never sent to a
generator at all** — see
[`../../../11-production-tracking/Jasu-Image-TODO.md`](../../../11-production-tracking/Jasu-Image-TODO.md).

So this is not a case of the generator disobeying. Nobody has ever seen her in
the boots the build list describes. **Generate both and decide from the
pictures.**

### What to do

Two prompts, and **they differ by exactly one line** — rule 8. Everything else is
byte-identical, so anything else that changes between the two images is noise and
should be ignored.

```
01a-boots-tall.txt      tall, shaft well up the calf, ending below the knee
01b-boots-ankle.txt     low, at or just above the ankle
```

1. **A fresh chat for each variant.** Not one chat with two prompts — the second
   will copy the first. This is the rule that cost a full Shada set.
2. Paste one file whole as the first message.
3. **Attach everything in `attachments/01a-boots-tall/`** (or `01b-`), plus the
   approved front — see the note below.

4. Save the results here as `01a-boots-tall.png` and `01b-boots-ankle.png`.

### The one unusual thing about this test

**These prompts attach the approved front, which a front view normally must
not be given.** `MANIFEST.txt` omits it precisely because a plate is never a
reference for itself, and a front view handed the approved front just redraws it.

**Here that is exactly what is wanted.** The costume must be held still so the
only variable is the footwear, and copying the approved image is the cheapest way
to hold it still. So both prompts carry an explicit scope:

> *"On the boots, and ONLY the boots, the photograph is WRONG and the numbered
> rule below OVERRIDES it. Everything else in the photograph outranks this text,
> as usual."*

**Watch for that failing in variant A.** A photograph beats a paragraph — it is
the documented reason Shada's plates came back three times too large — so the
tall-boot variant is the one at risk of quietly returning ankle boots off the
reference. **If A comes back with ankle boots, the test has not run.** Re-roll it
before comparing, and if it fails twice, drop the costume attachment from A and
accept that the rest of the costume will drift.

### What to judge

The question is **silhouette**, not detail. She is 155 cm and the costume is
skin-tight from collar to ankle, so the boot shaft is the only horizontal break
in the whole leg line.

- Does the tall boot shorten her, or does it read as deliberate?
- Does the ankle boot leave the leg reading as a single unbroken tube?
- Which one sits better under a hard mantle that is *"the only thing on her wider
  than she is"*?
- Which reads as **the best boots in a crew wearing dead men's kit** — that is
  the point of the item, and it is the same statement as the made-to-measure cut
  and the serviced blaster.

### After the decision

Whichever wins, **one of the three records is wrong and must be corrected**:

| If | Then |
|---|---|
| **Tall wins** | The approved front is wrong. Clear `approved:` in `outfits.yaml`, re-roll the front, re-approve, then re-roll the four matched views against it — **five images** |
| **Ankle wins** | The documents are wrong. Change the boots rule and the `components:` note to ankle boots, and drop "tall boots" from the officer-proportion list in `Character.md` — **no images** |

The whistle is the same class of problem and is **not** part of this test: the
build list puts it on a cord at her throat and the approved front has it hanging
at her belt. Decide it separately.

---

## 02 — the correction pass: boots, whistle and hair

**`02-boots-and-whistle.txt`.** The prompt that produces the replacement front
turnaround. Same costume, three items corrected.

It is built the same way as `01a`: the previously approved front is attached and
governs everything, **with three named exceptions where the numbered rules
override it** — the boots become tall with a flat heel, the belt whistle is
removed leaving exactly one at the throat, and **the hair goes up**. Everything
else must not move.

> ### The hair exception is the risky one, and it is deliberately fenced
>
> The other two swap one object for another. **The hair changes the head
> silhouette**, and the horns are *set into* the hair — so the moment the hair
> moves, the photograph stops holding the headdress still, and the headdress is
> half her design.
>
> So the exception is scoped twice: the hair changes, and **the horns explicitly
> do not.** Their size, curve, asymmetry, colour and position all come from the
> photograph; the only difference is that they are set into a raised rolled mass
> instead of into loose hair. Without that second sentence this pass would be an
> open invitation to redesign the headdress, and *"more ornamental"* is the
> direction it would go.
>
> **Her hair has come back down before when the rule reached the generator
> intact** — logged against `scale_figure`. So this is the first real test of
> whether the hair rule can win at all, and the answer is worth knowing before
> the sixteen narrative slots are generated.
>
> **If the horns drift, re-roll rather than accept it.** Three simultaneous
> changes is already one more than is comfortable; a fourth, unasked-for change
> to the headdress would make it impossible to tell what caused what.

**Drag in everything in `attachments/02-boots-and-whistle/`** — three files,
staged and named by what each is FOR.

```
1-the-costume.png                 <- source/artwork/turn-field-front.png, SCOPED
2-the-a180-blaster-pistol.jpg     <- reference/props/a180.jpg
3-face-build.jpg                  <- reference/actor/ling-jiu-headshot.jpg
```

Note this is the opposite of `MANIFEST.txt` for a normal front view, which omits
the costume photograph because a plate is never a reference for itself. **Here it
is the point** — the job is to change two items and hold everything else still.

**Fresh chat.** Paste `02-boots-and-whistle.txt` whole as the first message.

### Check before approving

- **Tall boots, and a FLAT heel.** The heel is the one the generator has already
  got wrong once.
- **ONE whistle, at the throat.** Look at the belt as well as the neck — the last
  pass drew both and it is easy to see only the one you asked for.
- **The hair actually up**, and a BUILT shape rather than a tidy everyday
  updo. This is the one most likely to come back unchanged.
- **The horns unchanged** — same size, same curve, same asymmetry, same worn
  bone. If they have grown, become symmetrical, or started to read as a crown or
  a headdress, re-roll.
- **Nothing else moved** — mantle points, collar, bracers, belt, thigh panels,
  knee pads, palette.

If it passes, it replaces `source/artwork/turn-field-front.png` and gets
re-approved in `outfits.yaml`; then the other four views are re-rolled against
it. Until that happens the approved reference still teaches ankle boots and a
belt whistle to every image made from it.

---

## 03 — the hair, lower and rougher

**`03-hair-lower.txt`.** A one-item correction on top of `02`.

**Pass 02 worked.** All three exceptions landed — tall boots, a flat-enough heel,
a single whistle at the throat — and the mantle, collar, bracers, belt, thigh
panels, knee pads, palette and pose all held still against the photograph. **The
horns survived the hair change**, which was the thing the fence was written to
protect.

**What was wrong: the hair went too high and too smooth.** And that is what the
rule asked for — it said *"a large rolled, worked mass HELD HIGH ON THE HEAD"*.
The generator obeyed it exactly. The rule has been rewritten: swept back and
gathered **LOW, ROUGH AND MESSY** at the back of the head, no higher than the
crown, uneven, strands escaping.

> **The wording of that rewrite is itself worth keeping.** The first attempt put
> *"messy and hand-made"* in the third sentence — and `short.py` dropped it. The
> single word the whole correction exists for was being trimmed out of the
> prompt. It now leads the rule, where it always survives, with the `NEVER` list
> second, which also always survives. **A correction that does not reach the
> generator is not a correction.**

### What to attach — note that this one is different

**Drag in everything in `attachments/03-hair-lower/`** — three files, staged for
you and named by what each one is FOR. Read its `MANIFEST.txt` first.

```
1-the-costume.png                 <- evolution/02-boots-and-whistle.png, SCOPED
2-the-a180-blaster-pistol.jpg     <- reference/props/a180.jpg
3-face-build.jpg                  <- reference/actor/ling-jiu-headshot.jpg
```

**This attaches an evolution image, which the folder rules normally forbid.** The
reason for that rule is that *"every one but the last shows a costume that no
longer exists"* — and `02` **is** the last. It is also the only image in the
production showing the tall boots and the single throat whistle; the file in
`source/artwork/` still shows ankle boots and a belt whistle and would undo two
settled decisions if attached instead.

Fresh chat. Paste `03-hair-lower.txt` whole as the first message.

### Check before approving

- **The hair no higher than the crown.** The silhouette above her head should be
  her head, not her hair.
- **Actually messy** — uneven, strands escaping. Not a neater version of the same
  sculpted shape.
- **The horns identical to `02`** — same size, curve, asymmetry and colour. This
  is the second pass in a row that moves the hair around them.
- **Boots, whistle and the rest unchanged from `02`.**

If it passes it becomes `source/artwork/turn-field-front.png`, is re-approved in
`outfits.yaml`, and the other four views are re-rolled against it.

---

## 04 — the final pass: costume from `03`, hair from the original

**`04-hair-down.txt`.**

**Pass 03 did exactly what it was asked** — the hair came down low, rough and
messy, and the costume held. Seen against the original, the answer was that
**the direction was wrong, not the execution.** Her hair is worn **down and
loose**, as it has been in every image from the start, and the rule that said
*"NEVER down"* was the thing that was wrong. It had never once been tested
against a picture.

So `04` combines two images that each hold half of the current design:

| | From | What it governs |
|---|---|---|
| **Image 1** | `evolution/03-hair-lower.png` | **The costume, head to foot.** Tall boots, flat heel, one whistle at the throat, and everything that was already right |
| **Image 2** | `source/artwork/turn-field-front.png` | **The hair and horns ONLY.** Long, dark, down and loose |

### This breaks a standing rule, deliberately, and it is the risk in the pass

> *"Two full-figure references competing over the same garment is a fight the
> written rules cannot win"* — and *"do not add a second full costume
> photograph."* This pass attaches exactly that.

It is done because **no single image in the production now shows the whole
design**: `03` has the costume and the wrong hair, the approved front has the
hair and two superseded items. The alternative — describing the hair in words —
was rejected only because the horns need to match precisely, and a photograph
carries them better than a paragraph.

**Three things fence it:**

1. The staged files are **named by scope** — `1-the-costume.png`,
   `2-the-hair-only.png` — so the split survives the drag-and-drop.
2. The prompt says which item in image 2 is out of date, **by name**: ankle
   boots, and a whistle at the belt.
3. It gives a one-look test: *"if your image has ankle boots, or a whistle
   anywhere below her throat, you have taken the costume from the wrong
   photograph."*

**If it fails that test, do not re-roll it as written.** Drop image 2 entirely
and let the text carry the hair. That is likely to work: the generator's own
default is hair down — it returned hair down twice when the rule said not to —
so this is the one instruction that does not need a photograph to win.

### What to attach

Everything in `attachments/04-hair-down/` — **four files**, named by scope. Read
its `MANIFEST.txt` first.

### Check before approving

- **Tall boots. One whistle, at the throat.** These come from image 1 and they
  are the two that image 2 will try to overwrite.
- **Hair long, dark, down and loose**, swept off the face, slightly dishevelled.
- **Horns as they have always been** — pale, worn, asymmetric, above and behind
  the ears.
- **Nothing else moved** from `03`.

If it passes it becomes `source/artwork/turn-field-front.png`, is re-approved in
`outfits.yaml`, and the four other views are re-rolled against it. **That is the
end of this sequence** — every open item on her front view is then closed.

---

## The sequence closed, 2026-08-03

**`04-hair-down.png` is the approved front.** It is now
`source/artwork/turn-field-front.png`, locked in `outfits.yaml`, and the four
remaining views are generated against it from the standard prompts.

**The two-photograph split worked.** The pass that broke the one-costume-reference
rule did so deliberately, and the check it was given — *"if your image has ankle
boots, or a whistle anywhere below her throat, you have taken the costume from
the wrong photograph"* — passed. The costume came from image 1 and the hair from
image 2, as asked.

### What the four passes actually cost, and why

**Five images to fix three faults that were in the documents from day one.** None
of them was a design that changed its mind:

| Fault | In the documents since | Why no image ever showed it |
|---|---|---|
| Ankle boots, not tall | 2026-08-01 | Sentence 8 of a 2,166-character rule. Never sent |
| Whistle at the belt, not the throat | 2026-08-01 | Sentence 2 of a rule cut at the old cap of 200. Never sent |
| Hair up | 2026-08-01 | **Sent, and wrong.** The rule said "NEVER down" and had never been tested against a picture |

The first two are the trim. The third is the opposite failure and the more
interesting one: **a rule that reached the generator every time, was obeyed, and
was itself the mistake.** It survived four days because the image that
contradicted it was the approved reference, and nobody reads a reference as an
argument.

**The order mattered.** Her `must_show` was rewritten from nine prose rules to
twenty-eight imperative ones *before* any of this was generated. Had these passes
run against the old rules, the boots and whistle corrections would have been
trimmed out of the prompts that were supposed to make them.
