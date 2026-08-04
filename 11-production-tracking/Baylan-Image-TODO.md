---
title: "Baylan — Finish List"
asset_id: "TRACK-BAYLAN-IMAGES"
updated: "2026-08-04"
status: "open"
---

# Baylan — Finish List

> # PICK UP HERE — 2026-08-04
>
> **Nothing is approved and nothing is generated. Seven front turnarounds have
> been run as tests and none was kept.** The costume moved a long way during
> them and the current rules are the result; the pictures are not.
>
> **THE FRONT IS THE GATE.** Everything downstream — the other views, the
> fourteen slots, the boards, the build guide and the two build sheets — matches
> against one approved image, and there isn't one yet.
>
> **Two prompts, both current, both regenerated 2026-08-04:**
>
>     03-characters/baylan/prompts/turnarounds-short/turn-working-front.txt
>     03-characters/baylan/prompts/turnarounds-short/turn-working-coat-front.txt
>
> Attach all three files from `prompts/attach/working/`. Fresh chat, tier High,
> and the reply must open with `Working from commit …, prompt …`.
>
> **Run both.** They differ by one garment and the coat version is the one the
> Production Designer liked; comparing them like for like is worth the extra pass.

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

---

## Still open

**THE CHEVRON COUNT. Seven generations, never five.** The count leads its rule,
it is in the check block, and it has still come back six, seven or eight every
time. **Words have lost this.** The fix is a cropped reference — see
`03-characters/baylan/reference/concept/README.md`, which carries the brief and
the scoping method. Do not write an eighth rule.

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

1. **A cropped still of the later chest piece** → `reference/concept/chevron-geometry-source.png`. Chest only: no head, no robes, no silhouette. Unblocks the two faults words cannot fix.
2. **A photograph of the printed gauntlets** → `reference/props/gauntlets.jpg`. The repo rule is *"for anything physically built, the reference is a photograph of the build, not a render"*, and it has already bitten twice here.
3. **Approve a front**, either outfit.

---

## Then, in this order

1. **Approve the front** — `03-characters/APPROVAL.md`. Fill `approved:` in `outfits.yaml`, add the locked plates to `references:`, and run `./tools/regen baylan`.
2. **The remaining views** — four for `working`, one for `working-coat`.
3. **The three prop plates** — `08-blaster`, `09-crystal`, `10-utility`. Both prompts are self-sufficient and need no reference; **do not attach a stock kyber crystal image**, the design is deliberately raw, yellow and unglowing against the canonical look.
4. **The eleven remaining slots.**
5. **The make-up board** — the only board he is missing. Its images are already defined: `detail_portrait` + `expression_strip`.
6. **`components:`** — then `./tools/build-guide-pdf baylan` and `./tools/build-lists baylan`. The chevron top is `route: made`; a base kurta or reenactment tunic at £5–15 plus a charity-shop leather garment cut up is the whole shopping side.
7. **Add him to `drive_folder()`** in `tools/publish-to-drive`, then publish. That mapping is manual on purpose — a wrong guess silently creates a second Drive folder.

**Full process:** [`../03-characters/Character-Build-Recipe.md`](../03-characters/Character-Build-Recipe.md), phases 3 to 9.
