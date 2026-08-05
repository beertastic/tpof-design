---
title: "Baylan — Finish List"
asset_id: "TRACK-BAYLAN-IMAGES"
updated: "2026-08-05"
status: "open"
---

# Baylan — Finish List

> # PICK UP HERE — 2026-08-05
>
> **Nothing is approved. Eight front turnarounds have been run and none was
> kept** — but the eighth pair found the chevron bug, and the rule is fixed.
>
> **THE FRONT IS THE GATE.** Everything downstream — the other views, the
> fourteen slots, the boards, the build guide and the two build sheets — matches
> against one approved image, and there isn't one yet.
>
> **RUN THIS, regenerated 2026-08-05 against the rewritten rule 8:**
>
>     03-characters/baylan/prompts/turnarounds-short/turn-working-front.txt
>
> Attach these three, from `prompts/attach/working/`:
>
>     1-face-build-1.jpg   2-face-build-2.jpg   3-face-build-3.jpg
>
> Fresh chat, tier High, and the reply must open with `Working from commit …,
> prompt …`.
>
> **Count the bands before anything else.** If it is five, the width hypothesis
> below is confirmed and the finding goes to
> `09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md` for every other
> character. If it is not five, words have genuinely lost and the cropped
> reference is the answer after all.
>
> **The coat view is NOT the gate** and does not need rerunning to clear it — it
> is slot 13, a separate removable garment. Its 2026-08-05 image is the best of
> the eight but it is missing the harness straps and the ammunition pouches,
> which its own rule 8 requires, and its belt and boots do not match the working
> dress. Fix those when slot 13 comes up, not now.

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

**THE CHEVRON COUNT — diagnosed 2026-08-05, fix untested.** Eight generations,
never five in the working view. **It was never a disobedience problem; it was a
trim problem** — see lesson 8. Rule 8 has been rewritten to put the width in its
FIRST sentence, which `trim()` always keeps, and shortened to 232 characters so
it survives whole at the current cap of 312. Coverage 88% → 91%.

**The next generation tests this and nothing else.** If it comes back five, the
cropped reference is not needed for the count and the finding generalises. If it
does not, fall back to
`03-characters/baylan/reference/concept/README.md`.

**The green stitching has never appeared.** It is a named plant in P5 — *"the
colour he is known for… it was on him the whole time, as thread"* — and the
quilting change should help, because the thread is now structural rather than
trim. If it still does not show, it goes on the same reference.

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
