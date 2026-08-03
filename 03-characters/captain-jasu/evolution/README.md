# Captain Jasu — evolution

How her design converged. **History, never specification** — the design lives in
`Character.md`, `outfits.yaml` and the approved reference. Per
[`../../README.md`](../../README.md), **never attach an image from this folder to
a generation prompt.**

| Pass | Variable | Result |
|---|---|---|
| `01a` / `01b` | **The boots — tall to the calf, or ankle** | **TALL WINS, 2026-08-03.** `01b` was never needed — `01a` settled it on sight. Now the default in `outfits.yaml` |
| `02` | **Correction pass — tall boots, flat heel, one whistle at the throat, hair UP** | **Prompt written 2026-08-03, not yet generated.** Produces the replacement approved front |

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
3. **Attach all three of these:**

   ```
   source/artwork/turn-field-front.png            the costume — SCOPED, see below
   reference/props/a180.jpg                       the blaster
   reference/actor/ling-jiu-headshot.jpg          face and build
   ```

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

**Attach these three, and nothing else:**

```
source/artwork/turn-field-front.png            the costume — SCOPED, three exceptions
reference/props/a180.jpg                       the blaster
reference/actor/ling-jiu-headshot.jpg          face and build
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
