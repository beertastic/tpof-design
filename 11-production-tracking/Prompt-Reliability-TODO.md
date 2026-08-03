---
title: "Prompt Reliability — Fix List"
asset_id: "TRACK-PROMPT-RELIABILITY"
updated: "2026-08-03"
status: "open"
note: "Fix 2 half-done (Shada re-ordered, Jasu not). Fix 7 added — it gates 26 images and was only recorded in Shada's file. Work the order in 'Which of these to do first', not the numbering."
---

# Prompt Reliability — Fix List

**Why this exists.** Four Shada generations in two days came back wrong in four
different ways. Each was patched individually. This document is the attempt to
stop patching symptoms and name what is actually broken.

---

## The finding

**Most of the specification never reaches the generator, and nothing says so.**

> **Superseded 2026-08-03.** The table below is the original measurement, kept as
> the record. Re-measured a day later, **Shada is at 22,915 spec characters and
> 8%, not 18,061 and 11%** — the specification grew and the share reaching the
> generator fell. Current figures, and the finding that the binding constraint
> was `RULE_CHARS` rather than `BUDGET`, are in
> [*What fix 4 actually found*](#what-fix-4-actually-found-2026-08-03).

Measured 2026-08-02 across every outfit in the production, comparing the
`must_show` rules in `outfits.yaml` against what survives into the short prompt
that actually gets pasted:

| Outfit | Rules | Spec chars | Reaching generator | Kept |
|---|---|---|---|---|
| **shada/working** | 14 | 18,061 | 1,988 | **11%** |
| captain-jasu/field | 9 | 11,665 | 1,601 | **13%** |
| baylan/working | 11 | 7,427 | 1,517 | **20%** |
| mercenary-kit/merc-1 | 7 | 2,598 | 1,034 | 39% |
| baylan/working-coat | 8 | 3,195 | 1,279 | 40% |
| mercenary-kit/merc-4 | 8 | 2,057 | 1,274 | 61% |
| mercenary-kit/merc-3 | 5 | 1,056 | 740 | 70% |
| mercenary-kit/merc-2 | 5 | 1,175 | 835 | 71% |

Worst single losses:

| Dropped | Outfit | Rule |
|---|---|---|
| −3,531 chars | shada/working | A PANELLED SLEEVELESS VEST, BARE ARMS… |
| −2,149 chars | shada/working | EACH PLATE IS 10-15 mm ACROSS… |
| −1,978 chars | captain-jasu/field | SKIN-TIGHT THROUGH THE BODY… |
| −1,853 chars | captain-jasu/field | THE HEADDRESS — PALE CURVED BONE HORNS… |
| −1,832 chars | baylan/working | FIVE BROAD NESTED CHEVRONS… |

**This is the common cause behind three of the four failures.** In every case the
rule existed, was correct, and was cut before the generator saw it:

- The **"NO YOKE"** prohibition was inside the placement rule. Trimmed. A yoke
  came back.
- The **plate size** rule was inside the placement rule until 2026-08-01.
  Trimmed. Plates came back three times too large.
- The **contact lens** rule was the last clause of the face rule. Trimmed. It
  never reached a generator at all until it was promoted.

Each was fixed by promoting the clause to its own rule — which lowers the cap and
quietly shortens every other rule. **The fix has been making the problem worse.**

---

## Why it happens

`tools/prompt-splitter/short.py` has a total budget of 3,800 characters and a
uniform per-rule cap. `fit()` lowers that one cap across *all* rules until the
whole file fits. As written on 2026-08-02:

```python
for cap in range(RULE_CHARS, 70, -10):     # RULE_CHARS was 200
    text = build(character, cfg, outfit, view, cap)
    ...
```

Four consequences, none of them visible when you run it:

1. **Adding any rule shortens every other rule.** Going from 14 to 16 rules on
   Shada cut roughly 35 characters off all sixteen.
2. **All rules are treated as equally important.** "HER EYES ARE REPTILIAN" and
   "EXTERIOR, WITH ONE EXCEPTION" get the same allowance, on a studio plate where
   the second rule explicitly does not apply.
3. **The loss is silent.** The run prints `5 short prompts, 4466–4538 chars` and
   nothing else. `trim()` appends `…` only when it cuts mid-sentence; whole
   dropped sentences leave no mark at all. Counting ellipses finds 1 truncated
   rule out of 67. Measuring content finds 89% of Shada's spec missing.
   **Fixed 2026-08-03 — see fix 1.**
4. **The loop never searches upward, so 200 is a target and not a ceiling.**
   Found 2026-08-03 and not visible in the loop above until you ask what happens
   when the file has room to spare: nothing. The cap stays at 200 and the rules
   stay cut. Four outfits were losing 30–60% of their specification to a limit no
   budget required. **Fixed — see fix 4.** Point 1 above still stands; points 2
   and 3's diagnosis was right and incomplete.

---

## Which of these to do first

**The numbers below are stable identifiers, not a running order.** They are cited
from `Shada-Image-TODO.md`, `Jasu-Image-TODO.md` and the changelog, so they do not
get renumbered when the priority changes. The priority changes here:

| Order | Fix | Status | Why here |
|---|---|---|---|
| — | **1 — report what was dropped** | **DONE 2026-08-03** | `short.py` now prints, per outfit, the settled cap, the share of the spec reaching the generator, and every sentence lost — marked `DROPPED` or `cut`. Warns with `!` under 80% |
| — | **4 — check the budget** | **DONE, and it found a different constant** | See below. `RULE_CHARS` was the binding limit, not `BUDGET`. Fixed; four outfits recovered with no budget change |
| — | **7 — `short.py` covers only turnaround views** | **DONE 2026-08-03** | `prompts/slots-short/` — sixteen slot prompts at 2.2–8.9 KB where the long files ran 16–68 KB. **Unblocked 26 images** |
| 1st | **3 — per-rule priority (`pin:`)** | open | **Promoted from 6th.** Five faults now demonstrably REACH the generator and are overruled anyway: plate density, scale-pattern colour, the boots, the zip, the collar. Not truncation, not budget — priority |
| 2nd | **2 — imperative-only `must_show`** | **half done** | Sentence ordering is done for Shada and **not for Jasu's nine**. The budget raise took Shada from 8% to 26%, so this is less urgent than it was and still the only thing that fixes her properly |
| 3rd | **5 — Shin has no `must_show`** | open | Half an hour, and it unblocks a co-lead entirely |
| 4th | **6 — no verification loop** | open | Last. It checks work the fixes above stop producing |

**Fix 3 changed places with fix 2 on 2026-08-03**, on evidence rather than
theory. Six generations that day established that the remaining failures are not
rules being cut — they are rules arriving intact and losing to something else in
the prompt. Fix 2 shortens rules that already fit; fix 3 decides which rules win.

### What fix 4 actually found, 2026-08-03

**The expensive constant was `RULE_CHARS`, not `BUDGET`, and raising the budget
alone does almost nothing.** `fit()` searched the per-rule cap *downward* from
200 and stopped at the first value that fit — which silently made 200 a target
rather than a ceiling. An outfit whose entire prompt came to 2,458 characters
against a 3,800 budget still had every rule cut to 200, and lost 30% of its
specification to capacity nobody was using.

Measured across every outfit, share of `must_show` reaching the generator:

| Outfit | Spec chars | Before | Cap searches up | At budget 8,000 |
|---|---|---|---|---|
| mercenary-kit/merc-2 | 1,180 | 70% | **100%** | 100% |
| mercenary-kit/merc-3 | 1,061 | 69% | **100%** | 100% |
| mercenary-kit/merc-4 | 2,065 | 61% | **100%** | 100% |
| mercenary-kit/merc-1 | 2,605 | 39% | **80%** | 100% |
| baylan/working-coat | 3,203 | 39% | **48%** | 100% |
| baylan/working | 7,438 | 20% | 20% | 77% |
| captain-jasu/field | 11,674 | 13% | 14% | 50% |
| **shada/working** | **22,915** | **8%** | 8% | **27%** |

**Three outfits went to full specification for free**, and two more improved
sharply — no budget raised, every file still inside 3,800. Merc 2, 3 and 4 are
now sent whole; Merc 1 went 39% → 80% and Baylan's coat 39% → 48%. For those
five it was never a budget problem.

**Three corrections this forces on the rest of this document:**

1. **Shada's numbers here were stale and generous.** This document says 18,061
   spec characters and 11% reaching the generator. Measured 2026-08-03:
   **22,915 and 8%.** The specification grew 27% since it was measured and the
   share reaching the generator got *worse*, not better.
2. **"Most of this problem disappears for the price of one constant" is wrong
   for Shada.** Zero trimming for her would need a budget of **24,760**. No image
   model takes that. Even at 16,000 she is at 61%.
3. **So fix 2 is not optional for her.** Her rules are 3× Jasu's and 7× Baylan's
   coat. She is not budget-bound, she is *prose*-bound, and no ceiling rescues
   her. **The remaining question for fix 4 is narrow**: whether the generator
   accepts ~8,000, which would take Baylan to 77% and Jasu to 50%. Test pending —
   `short.py --budget 8000 --dry-run` reports it without writing anything.

---

## Fixes, in order of value per hour

*Superseded as an ordering by the table above — kept because the numbers are
cited elsewhere. Read this section for what each fix **is**, and the table for
when to do it.*

### 1. Report what was dropped — ~~do this first~~ **DONE 2026-08-03**

`short.py` now prints, per outfit, the cap it settled on, the share of the
specification reaching the generator, and **every sentence that did not survive**
— marked `DROPPED` where the sentence is gone entirely and `cut` where only its
leading clause was kept. An outfit under 80% is flagged `!`.

It earned itself on the first run. Merc 1's rule 6 was silently losing:

```
  ! mercenary-kit/merc-1: rules trimmed at cap 385 — 80% of 2605 spec chars reach the generator
      rule 6. HIS PRIMARY WEAPON IS A HUMAN-SIZED RIFLE WORN A…
        DROPPED HE IS RIGHT-HANDED and nothing is mirrored — no matching item on both sides.
```

That is a handedness rule — the class of loss this whole document exists for —
disappearing with no mark on the file and a success message printed.

`--dry-run` reports without writing, which is how to test a budget change safely.

### 2. Stop writing prose into `must_show`

**This is the real cause and the cheapest fix.** `must_show` currently serves two
masters: it is the build specification *and* the generator's rule list. Those
want opposite things. Shada's placement rule is 1,555 characters; her vest rule
is 3,688. They cannot fit and were never going to.

Rules should be **imperative only** — what must be true, in one or two short
sentences, no explanation. All the reasoning ("the mismatch is what proves nobody
made this for her", "this keeps coming back wrong") is real and worth keeping,
but it belongs in `Character.md` and the long prompt, which humans read. A
generator does not need to be persuaded.

Target: **every rule under the cap, so nothing is trimmed at all.** Fourteen
rules at 140 characters is 1,960 — comfortably inside the budget. The long
prompt keeps the full text unchanged.

### 3. Let rules carry a priority

Add `pin: true` (or an explicit order) so identity-critical rules — face
precedence, character identity, handedness — are never trimmed, and low-priority
rules absorb the cut instead. Requires a change to `fit()` to allocate per-rule
rather than uniformly.

### 4. Check whether the 3,800 budget is still real — **DONE 2026-08-03, and the answer was not the budget**

The premise was that `BUDGET = 3800` was the binding constraint and one constant
would fix it. **Measured, it was the wrong constant.** `RULE_CHARS = 200` was
doing the damage, because `fit()` only ever searched downward from it and never
asked whether there was room for more. Fixed: the search now finds the *largest*
cap that fits. Four outfits went to full specification with no budget change.

Full figures in *What fix 4 actually found* above. What survives of this item is
one narrow question — **does the generator accept ~8,000?** — which is worth
about 77% for Baylan and 50% for Jasu, and does not rescue Shada at any value.

### 5. Shin has no `must_show` rules at all

Three outfits — `early`, `late`, `final` — and zero non-negotiables between them.
Every other character has five to fourteen. Nothing enforces anything on the most
protected character in the production. Not caused by the trim; a separate gap,
found while measuring.

### 6. No verification loop

Nothing checks a generated image against the rules that produced it. Every check
so far has been a person looking at a picture and noticing. A checklist generated
from `must_show`, in the order most-often-wrong first, would at least make the
looking systematic.

### 7. `short.py` covers only the five turnaround views

**Added 2026-08-03. It was recorded in `Shada-Image-TODO.md` as a blocker and
never reached this list, which is why the tooling list did not name the item
gating the most images.**

`short.py` builds short prompts for the views in `VIEWS` and nothing else. The
sixteen numbered slots in `Prompts.md` exist only as the long files in `prompts/`:

| Slots | Size | Against a 3,800 budget |
|---|---|---|
| `hero`, `camp_day`, `forest`, `maintenance`, `tone-collage` | ~65 KB | **16× over** |
| `scale_portrait`, `species_strip`, `expression_strip`, `material-scale` | ~18 KB | 4× over |
| the remaining plates | ~16 KB | 4× over |

So for those sixteen there is **no deliberate prompt to paste.** You hand over the
long file and let the host compress it — which is precisely the failure this
document exists to describe, with the compression moved somewhere nothing can
report on it.

**Cost: 26 images.** Twelve of Shada's seventeen regenerations, and all fourteen
of Captain Jasu's narrative slots the moment her pack stops being a scaffold.

The trim logic, the rule handling and the reference block all already exist. What
is missing is the per-slot shot and scene text — what `VIEWS` does for
turnarounds, one level up.

---

## Process, not tooling

**Use a fresh conversation for every character.** A Shada prompt returned Captain
Jasu's costume on 2026-08-02 — horns, shoulder yoke, quilted sleeves, matched
bracers — because her set had been generated in the same chat the day before. No
prompt change fixes this reliably; the prohibitions now in the prompt are a
backstop, not a solution.

**The specification moved four times in two days**, and each move invalidated all
twenty images. Flank panels were added, dropped and restored inside 24 hours.
Some of that was genuine discovery from looking at pictures, and the design is
better for it. Some of it was churn — including at least one change made by
over-reading a brief, which then had to be undone. **Lock the costume before the
next full generation run**, and treat further changes as costed.

---

## The failure record

| Date | What came back wrong | Root cause | Fixed by |
|---|---|---|---|
| 2026-08-01 | Plates 3–4× too large | Size rule trimmed out | Promoted to its own rule |
| 2026-08-01 | Right costume, wrong woman | Costume reference had no scope; read as a face reference | `NOT THE FACE` in every label + face-precedence rule |
| 2026-08-02 | Captain Jasu's costume on Shada's face | Shared conversation | Fresh chat + four named prohibitions |
| 2026-08-02 (fifth) | Skirt and tabard over the trousers; crossover V-neck vest; gauntlet and shoulder cap on the wrong sides; flank panels not laced and no cloth gap; plates 3× too big and all one metal; no thigh patch; knife at the centre front | **Five separate rules trimmed to their opening sentence.** Every missing element was the *second half* of a rule that reached the generator | Lead sentences rewritten so the load-bearing clause comes first, in seven rules |

**The fifth failure is the strongest evidence in this document**, because it is
the finding above with the individual rules named. Not one of the faults was a
rule that did not exist, and not one was the model disobeying a rule it had been
given. In every case the rule was present, correct, and cut before the
generator saw it:

| What appeared | The rule that would have stopped it | Where that sentence sat |
|---|---|---|
| A layered skirt and tabard | "THE TROUSERS are dark, close-fitting…" | **Last** sentence of the boots rule — cut from every short prompt ever generated |
| A crossover V-neck vest | "STAND COLLAR, CONCEALED PLACKET…" | Second sentence of the vest rule — cut |
| Panels not laced, no cloth gap | "LACED ACROSS THE CENTRE FRONT… A STRIP OF VEST CLOTH SHOWS BETWEEN THEM." | Sentences four and five of the flank-panel rule — both cut |
| Knife at the centre front | "KNIFE: … on HER LEFT HIP" | Fifth sentence of the weapons rule; the blaster description ate the whole allowance — the word *knife* never reached a generator |
| Gauntlet and cap on the wrong sides | "(1) A GAUNTLET ON HER RIGHT FOREARM ONLY… (2) A LOOSE SCALE CAP OVER HER LEFT SHOULDER ONLY" | Sentences three and four of the placement rule — cut, leaving only a list of four body parts with no piece attached to any of them |

**The one fault the trim does not explain is the plate size.** That rule led its
own rule, reached the generator intact, and was disobeyed anyway — because the
attached costume photograph shows plates twice the specified size, and an image
beats a paragraph. This is a different failure mode from the rest of this
document and it needs a different fix: **when a reference is wrong about
something, the rule has to say the reference is wrong**, by name. That is now
done for the plate size and for the shoulder piece.

### What this changes about the fix order

Fix 2 above — "stop writing prose into `must_show`" — is right, but the fifth
failure shows the cheaper half of it does most of the work: **the order of the
sentences inside a rule matters more than the length of the rule.** `trim()`
always keeps the first sentence and then prefers the first hard negation, so a
rule whose first two sentences carry the constraint survives at any cap, however
long the rest of it is. Seven of Shada's fourteen rules were re-ordered on
2026-08-02 on that basis and all fourteen now land whole, with no ellipsis and
nothing silently dropped. **No rule was shortened and no rule was removed.**

That does not retire fix 1 — nothing yet *reports* what was dropped, and this
was all found by reading a generated image and then reading the file. It does
suggest fix 1 should report **which sentences of a rule were dropped**, not just
how many characters were lost.

### The sixth failure, 2026-08-03 — and the cheapest fix in this document

**A design was declared wrong and remade, when the design was right and one
sentence of it had never reached the generator.**

Shada's shoulder cap came back moulded tight to her shoulder in every generation
for four days. It was read as a design problem, and the production was on the
point of redesigning the piece. `must_show` rule 5 already said, since
2026-08-01:

> *"Genuinely SEPARATE plates laced to a HAND-CUT, IRREGULAR backing, sitting
> AWAY FROM THE BODY over the point of her left shoulder. It hangs, it lifts, it
> swings when she turns, and DAYLIGHT SHOWS UNDER ITS LOWER EDGE."*

The rule is 1,555 characters. This is what the pasted prompt carried:

```
5. THE SHOULDER CAP IS A LOOSE FIELD OF SMALL SCALE PLATES ON HER LEFT
   SHOULDER, A PALM'S WIDTH. NEVER A SOLID PAULDRON OR ONE SMOOTH PLATE.
```

**137 characters of 1,555 — 9%.** The lead sentence carried the cap's *size* and
its *side* and said nothing about how it *sits*, so the one observable that
distinguishes a scavenged cap from a pauldron never arrived.

Re-ordering the rule so the drape leads fixed it **in a single generation, with
no new words and no design change.** The cap now hangs correctly and the front
was re-approved as v2.

**Why this one matters more than the five above it.** The earlier failures cost
images. This one nearly cost a *design*: the piece was about to be changed to fix
a fault it did not have. A trim that silently drops the load-bearing half of a
rule does not just produce wrong pictures — **it produces wrong conclusions about
the costume**, and those propagate into documents, build notes and cost.

It is also the strongest possible argument for fix 2. Rule 5 is 1,555 characters
of correct, considered specification, and nine per cent of it is doing any work.

### Also found, 2026-08-02

**`short.py` was missing from the run instructions.** The finish list told the
operator to run `split.py` and `turnarounds.py`, neither of which writes
`turnarounds-short/` — the directory the pasted prompt comes from. A run of the
documented two commands leaves the short prompts stale and reports success,
and the stale file's header still carries a version stamp. Corrected in
`Shada-Image-TODO.md`; **the other characters' finish lists have not been
checked for the same omission.**
