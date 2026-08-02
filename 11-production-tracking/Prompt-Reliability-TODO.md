---
title: "Prompt Reliability — Fix List"
asset_id: "TRACK-PROMPT-RELIABILITY"
updated: "2026-08-02"
status: "open"
note: "Fifth failure recorded and diagnosed. Fixes 1 and 3-6 still open."
---

# Prompt Reliability — Fix List

**Why this exists.** Four Shada generations in two days came back wrong in four
different ways. Each was patched individually. This document is the attempt to
stop patching symptoms and name what is actually broken.

---

## The finding

**Most of the specification never reaches the generator, and nothing says so.**

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
whole file fits:

```python
for cap in range(RULE_CHARS, 70, -10):
    text = build(character, cfg, outfit, view, cap)
    ...
```

Three consequences, none of them visible when you run it:

1. **Adding any rule shortens every other rule.** Going from 14 to 16 rules on
   Shada cut roughly 35 characters off all sixteen.
2. **All rules are treated as equally important.** "HER EYES ARE REPTILIAN" and
   "EXTERIOR, WITH ONE EXCEPTION" get the same allowance, on a studio plate where
   the second rule explicitly does not apply.
3. **The loss is silent.** The run prints `5 short prompts, 4466–4538 chars` and
   nothing else. `trim()` appends `…` only when it cuts mid-sentence; whole
   dropped sentences leave no mark at all. Counting ellipses finds 1 truncated
   rule out of 67. Measuring content finds 89% of Shada's spec missing.

---

## Fixes, in order of value per hour

### 1. Report what was dropped — do this first

`short.py` should print, per outfit, which rules lost text and how much, and
should warn hard when a rule loses more than a set fraction. Roughly twenty
lines, no behaviour change, and it turns an invisible failure into a visible one.

Without this, everything below is guesswork.

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

### 4. Check whether the 3,800 budget is still real

`BUDGET = 3800` with a comment saying "the real limit out there is about 4,000".
That was measured against an older generation of image tools. **If the tool now
accepts 8,000+, most of this problem disappears for the price of one constant.**

*Needs input: what is actually being pasted into, and what does it accept?*

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

### Also found, 2026-08-02

**`short.py` was missing from the run instructions.** The finish list told the
operator to run `split.py` and `turnarounds.py`, neither of which writes
`turnarounds-short/` — the directory the pasted prompt comes from. A run of the
documented two commands leaves the short prompts stale and reports success,
and the stale file's header still carries a version stamp. Corrected in
`Shada-Image-TODO.md`; **the other characters' finish lists have not been
checked for the same omission.**
