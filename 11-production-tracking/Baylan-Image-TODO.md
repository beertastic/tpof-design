---
title: "Baylan — Finish List"
asset_id: "TRACK-BAYLAN-IMAGES"
updated: "2026-08-05"
status: "open"
---

# Baylan — Finish List

> # PICK UP HERE — 2026-08-05, end of day
>
> ## THE COSTUME IS RIGHT EXCEPT THE SKIRT, WHICH JUST CHANGED
>
> **The front was approved on the fourteenth turnaround and the approval was
> cleared the same afternoon.** The Production Designer changed the skirt, and
> `APPROVAL.md` is unambiguous: editing an approved outfit invalidates the
> artwork made from it.
>
> **THE TWO EXISTING PLATES ARE SUPERSEDED** — `source/artwork/`
> `turn-working-front.png` and `turn-working-back.png`. Keep them as history.
> **They must not be used as a match target or as board source.**
>
> ### What changed
>
> The knee-length split tunic skirt is gone. In its place: **two separate torn
> panels of cloth hung from the belt, one over each hip**, open at the centre
> front AND the centre back so his trousers show up the middle from both sides,
> **upper thigh only** — barely past the seat. *"A hint of a skirt, and perhaps
> worn or torn."*
>
> **This is the fauld silhouette, and it is now safe.** The fauld was refused on
> 2026-08-04, but that refusal was about **overlapping metal plates** — *"the
> shape most likely to read as armour, and armour reads as status, and status is
> what he has spent eighteen years hiding."* Torn cloth reads as damage, not
> defence. **The shape was never the problem; the material was.**
>
> It also retires a whole rule. The old skirt needed *"THE SKIRT MUST NOT TURN
> HIM INTO A JEDI, AND FIVE THINGS WOULD DO IT"* because a knee-length split
> tunic **is** that shape. Two ragged hip panels are not, so the five signals
> keep their own rule and lose the skirt framing.
>
> ### Run this
>
>     prompts/turnarounds-short/turn-working-front.txt
>
> Attach **4 files** from `prompts/attach/working/` — the approved-front
> reference is gone from the folder now that the approval is cleared, so the
> numbering has shifted back:
>
>     1-the-chest-panel-geometry-only-not-the-garment.png
>     2-face-build-1.jpg   3-face-build-2.jpg   4-face-build-3.jpg
>
> **Everything above the belt is settled** — check only the hip panels: two of
> them, open front and back, upper thigh, torn.
>
> ---
>
> ## THE REFERENCE EXISTS NOW, AND IT CHANGED THE COSTUME
>
> `reference/concept/chevron-geometry-source.png` — cut from a costume
> reproduction on a **mannequin**, so there is no head, no face and no bearing
> in frame to leak. Attached to every `working` view.
>
> **Looking at it reversed two rules we had written ourselves in the previous
> forty-eight hours:**
>
> - **Rule 9** forbade a broad plain yoke. **The real garment has one filling
>   the top half.** The rule was raised on 2026-08-04 *because* three
>   generations kept drawing it — the generator was reproducing the source and
>   was corrected away from it, three times.
> - **Rule 11** made the bands quilting and forbade *"separate pieces, hard
>   edges, cast shadows"*. **The real garment is exactly that** — applied
>   panels, overlapping, piped edges, real shadows.
> - **Rule 6** said "never shoulder to shoulder". It is a **broad plastron**
>   almost armhole to armhole.
>
> **THE COUNT IS NO LONGER A NUMBER.** Eleven fronts chased "exactly five" and
> never got it because five is not a countable feature of the object — the
> reference reads as three, four or five depending on whether the yoke edge and
> the piping count. The rule now says **THREE TO FIVE broad bands below the
> yoke**. Previous ruling superseded.
>
> **THE GREEN IS REAL** — confirmed on the screen costume, *very* subtle, and
> the Production Designer had to be told it was there. Target: findable when
> looked for, never announced.
>
> ## RUN THE FRONT AGAIN — IT IS A DIFFERENT COSTUME NOW
>
>     prompts/turnarounds-short/turn-working-front.txt
>
> Attach **4 files** from `prompts/attach/working/`. **The numbering changed** —
> the geometry reference is now file 1 and the face files shifted to 2, 3, 4:
>
>     1-the-chest-panel-geometry-only-not-the-garment.png
>     2-face-build-1.jpg   3-face-build-2.jpg   4-face-build-3.jpg
>
> Then these five, each from its own folder:
>
> | Prompt | Attach from `prompts/attach/working/` |
> |---|---|
> | `prompts/slots-short/15-gauntlets.txt` | `15-gauntlets/` — 5 files |
> | `prompts/slots-short/08-blaster.txt` | `08-blaster/` — 5 files |
> | `prompts/slots-short/10-utility.txt` | `10-utility/` — 5 files |
> | `prompts/slots-short/11-maintenance.txt` | `11-maintenance/` — 5 files |
> | `prompts/slots-short/09-crystal.txt` | 4 files. **NO kyber reference** |
>
> Fresh chat, tier High, and the reply must open with `Working from commit …,
> prompt …`.
>
> ## THE COAT IS DEPRIORITISED
>
> **Confirmed 2026-08-05: get the working dress finished first.** The coat is
> slot 13, a separate removable garment, and it is NOT the gate. Its image is
> missing the harness straps and the ammunition pouches its own rule 8 requires,
> and its belt and boots do not match the working dress. Fix all of that when
> slot 13 comes up, not before.

---

## Where he is

| | |
|---|---|
| `Character.md` · `Character-Lock.md` · `outfits.yaml` · `Prompts.md` | ✅ all present, `status: ready` |
| Turnarounds | **0 of 7** — five `working`, two `working-coat` |
| Numbered slots | **0 of 14** |
| Prop locks | **0 of 3** — `blaster`, `crystal`, `utility` |
| Boards | 5 built, **no make-up board** |
| `components:` | ❌ none, so no build guide and no build sheets |
| Drive | not mapped — he is not in `drive_folder()` in `publish-to-drive` |

---

## What seven generations taught

**This is the part worth keeping.** Every rule below was bought with a wasted
pass, and the generalisations belong in
[`../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md`](../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md)
once they have been seen twice.

**1. Forbidding one direction teaches the generator another.** A wide buckled
strap came back HORIZONTALLY across his sternum. The rule was tightened to forbid
horizontal, and the next pass returned a DIAGONAL bandolier with a buckle
mid-chest — the rule obeyed and the fault intact. It now refuses the class:
nothing crosses his chest at any angle. **Refuse the category, not the instance.**

**2. A specification that contradicts itself is resolved by the generator, in
whichever direction it likes.** The gauntlets were specified as metal in the
rules while the outfit's `description:` still said *"worn leather wraps on both
forearms"*. They came back leather twice. **The prose won, because prose is the
specific instruction and a rule is the general one** — the same shape as the
three defects `consistency.py` was written for. Check the description whenever a
rule changes.

**3. Put the finish first if the finish is what fails.** *"DULL, DIRTY AND
BATTERED"* sat third in the gauntlet rule and was ignored; they came back
polished chrome, the brightest object on a man whose palette rule is near-black.
Moved to the front of the rule and they dulled down. **The trim keeps the opening
sentence — so the sentence that keeps losing should become the opening one.**

**4. "Apex down" is ambiguous and cost a generation.** An apex *is* a point, so
"apex down" reads equally as *the point is at the bottom* and *the shape points
down the page* — and Λ satisfies the second. Now spelled out: *ends HIGH at the
sides, point LOW at the centre, like a downward arrowhead, never a peak.*
**Geometry needs describing twice, in different words.**

**5. A shoulder piece becomes a pauldron whatever the rule says.** Specified soft,
drooping, no structure, no hard edge, NOT a pauldron — and it returned a
structured pauldron standing off the shoulder. Third rejection of shoulder armour
on this character; see `Planted-Elements.md` P5.

**6. Rules can arrive whole and still lose to each other.** The chevron panel was
specified as five appliquéd leather bands while rule 2 says ABSOLUTELY NO
ORNAMENT, no insignia, no badges. **A centred, symmetrical five-band device is the
most insignia-shaped thing it is possible to put on a man**, so the two rules
fought and the picture won every time. Changed to QUILTING on 2026-08-04 — seams
stitched through a padded panel rather than pieces laid on it. Same geometry,
different make, and it is the only change that addressed *why* the costume kept
reading as "off".

**7. Coverage was never the tool's limit, it was somebody else's.** His working
outfit was losing a quarter of its specification to an 8,000-character budget set
to match Shada's approved plates. He has none, so the ceiling cost him nothing but
harm. `prompt_budget: 11000` in his `outfits.yaml`; **100% of his specification
now reaches the generator**, up from 74%.

**That 100% did not last, and nobody noticed.** Hip plates were added to the
spec later the same day. Coverage was back to **88%** by the eighth generation
and the tool had been reporting it in its own output the whole time. **Coverage
is not a milestone, it is a gauge — read it on every regen.** Lesson 8 is what
the missing 12% was doing.

**8. A COUNT CANNOT HOLD A LAYOUT. THE SIZE HOLDS IT, AND THE COUNT FOLLOWS.**
This is the one that broke the seven-generation deadlock, and it is the most
transferable thing on this page.

Rule 8 said FIVE and it said EXACTLY FIVE and it led with it, and the trim was
dropping its last two sentences — *"Each is a BROAD BAND ROUGHLY A HAND'S
WIDTH"* and *"They TOUCH: no cloth shows between them"*. **Width and spacing
were never reaching the generator at all.** It was told five bands and nothing
about how big a band is, so it drew narrow ones, left gaps, and filled the
leftover panel — with seven.

The A/B ran itself. `working-coat` rule 1 carries *"each about a hand's width,
touching"* inline in a rule short enough to survive whole, and **it returned
five on the first pass** — same panel, same generator, same morning. The only
difference was whether the width survived the trim.

Five bands a hand wide, touching, fill a chest panel exactly once. Given the
width and the extent, **five is the only answer available and the number stops
having to be obeyed.** Given the number alone, the generator satisfies it and
then resolves the leftover space however it likes — which is not disobedience,
it is an underspecified layout.

**Corollary, and the reason this was invisible for seven passes: a rule can fail
because of a clause that never arrived.** Six generations were spent tightening
words that were already in the file and already being cut. **Before rewriting a
rule that keeps failing, check the trim report and confirm the rule is actually
reaching the generator whole.**

---

## Still open

**THE CHEVRON COUNT — ELEVEN GENERATIONS, NEVER FIVE. WORDS HAVE LOST IT.**

The trim discovery was real and it bought a great deal: the bands now TOUCH,
have no gaps, are correctly broad, are properly quilted, and the hand-stitching
finally shows as stitching. **Every one of those came from clauses that had
never been arriving.** But the count itself did not follow, and three separate
rewordings after the fix did not move it:

| Wording | Result |
|---|---|
| "EXACTLY FIVE bands" | 7 |
| "…each a BROAD BAND A HAND'S WIDTH, touching" | 6 |
| "…each ONE FIFTH OF THE PANEL'S HEIGHT" | 5 on the chest, then 2 more below the belt |
| "…collar to lower edge, THE BELT CROSSES THE FOURTH" | 6, panel ending at the belt |

**The tell is the panel extent, not the count.** Across three runs on
effectively the same instruction it ended *above* the belt, then ran *through
and below it*, then stopped *at* it. That is not a rule being misread — it is
run-to-run variance on a layout the generator is not computing. It renders a
plausible quilted panel at a plausible band pitch; it does not solve for a
count, a fraction or a landmark.

**So the eleventh front closes the argument the way the 2026-08-04 note opened
it: only an image holds a shape.**

**THE GREEN HAS NEVER APPEARED EITHER, AND THIS WAS MEASURED RATHER THAN
EYEBALLED.** Scanning every row of the eleventh panel, peak green bias is 4.5
and the mean is 1.74, where a genuinely green thread scores 15–40. There is no
green anywhere; the value is JPEG noise.

The rewrite that stopped the rules telling it to hide *did* work — the stitching
is now visible as stitching, which it never was. What is missing is only the
hue, and the likely reason is that **`DARK GREYED-OFF GREEN` puts two
desaturating modifiers in front of the colour** and the generator is applying
the modifiers and dropping the hue. Worth one attempt if a rewording is ever
bundled with something else — but it is a named plant in P5, so **it goes on the
same reference and stops being a wording problem.**

**Cloak or coat. Recommended: coat.** P5 has the coat becoming the cloak, *"same
garment, same silhouette, no ceremony attached to it yet"* — and a cloak carries
ceremony by definition, which rule 1 refuses. The hood-down rule added 2026-08-04
gives the cloak *hint* at the neck on a garment that is still a coat. **Not
settled; the Production Designer liked the coat generation.**

**Watch the accumulation.** He has gained a skirt, metal gauntlets and a hooded
coat in one day, and lost a shoulder pad. Each was justified alone. His defining
rule is *"his plainness is the only odd thing about him — the absence IS the
design"*, and a costume can accumulate its way out of that premise one defensible
addition at a time. **Judge the next generation as a whole silhouette, not feature
by feature.**

---

## Blocked on the Production Designer

1. **A cropped still of the later chest piece** → `reference/concept/chevron-geometry-source.png`. Chest only: no head, no robes, no silhouette. **Downgraded 2026-08-05** — the count now has a words-only fix awaiting test (lesson 8), so this is needed for the green stitching, and for the count only if that test fails.
2. ~~A photograph of the printed gauntlets~~ **DELIVERED 2026-08-05**, along with the blaster. Both are in `reference/props/`. **See item 4 — the gauntlet build contradicts the gauntlet rule and needs a ruling before it can be attached.**
3. **Approve a front**, either outfit.
4. **RULE THE GAUNTLET SCREEN.** The printed build has a **large, bright, near-white screen** with a pale keypad on the outer forearm. The rule says *"a SMALL DARK screen… half dead, with nothing lit on it"*, rule 2 says ABSOLUTELY NO ORNAMENT, and his characterisation is *"the absence IS the design."* **A glowing white rectangle on each forearm is the most conspicuous object on a near-black costume.** Either the print is painted down to near-black, or the rule changes and the characterisation takes the hit. The build also has heavy stepped ribbing where the rule says *"a smooth clamshell"*, and puts the screen on the outer forearm where the rule says the inside of the wrist. **`reference/props/README.md` has the full table.**

---

## Then, in this order

1. **Approve the front** — `03-characters/APPROVAL.md`. Fill `approved:` in `outfits.yaml`, add the locked plates to `references:`, and run `./tools/regen baylan`.
2. **The remaining views** — four for `working`, one for `working-coat`.
3. **The three prop plates** — `08-blaster`, `09-crystal`, `10-utility`. **`08-blaster` and `10-utility` now carry the printed build photograph** (`reference/props/blaster-build-2026-08-05.jpg`, also on `11-maintenance`); staged folders are at `prompts/attach/working/08-blaster/`, `10-utility/` and `11-maintenance/` — four files each, use the slot's own folder. `09-crystal` needs no reference and **do not attach a stock kyber crystal image**: the design is deliberately raw, yellow and unglowing against the canonical look.
4. **The eleven remaining slots.**
5. **The make-up board** — the only board he is missing. Its images are already defined: `detail_portrait` + `expression_strip`.
6. **`components:`** — then `./tools/build-guide-pdf baylan` and `./tools/build-lists baylan`. The chevron top is `route: made`; a base kurta or reenactment tunic at £5–15 plus a charity-shop leather garment cut up is the whole shopping side.
7. **Add him to `drive_folder()`** in `tools/publish-to-drive`, then publish. That mapping is manual on purpose — a wrong guess silently creates a second Drive folder.

**Full process:** [`../03-characters/Character-Build-Recipe.md`](../03-characters/Character-Build-Recipe.md), phases 3 to 9.
