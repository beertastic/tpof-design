---
title: "Captain Jasu — Finish List"
asset_id: "TRACK-JASU-IMAGES"
updated: "2026-08-03"
status: "open"
---

# Captain Jasu — Finish List

> ## THE FRONT IS APPROVED, v2 — 2026-08-03. Everything below runs against it.
>
> `source/artwork/turn-field-front.png` carries **tall boots with a low heel,
> exactly one whistle at the throat, and hair worn down** — the three things the
> first approved front never showed, because the rules carrying them were being
> trimmed out of every prompt before it was sent.
>
> **Four passes to get there**, all recorded in
> [`../03-characters/captain-jasu/evolution/README.md`](../03-characters/captain-jasu/evolution/README.md).
> The 2026-08-01 front is kept as `00-first-approved-2026-08-01.png` and **must
> not be attached to anything.**
>
> **`./tools/regen captain-jasu` has been run, so every prompt and the staged
> attachment folder already point at the new front.** Verified by checksum.
>
> ### RUN THIS NEXT — the four remaining views
>
> They are the primary deliverable and they are ready now. **Fresh chat each.**
>
> | Order | Paste | Attach |
> |---|---|---|
> | 1 | `prompts/turnarounds-short/turn-field-left.txt` | everything in `prompts/attach/field/` — **all 3** |
> | 2 | `prompts/turnarounds-short/turn-field-right.txt` | the same 3 |
> | 3 | `prompts/turnarounds-short/turn-field-back.txt` | the same 3 |
> | 4 | `prompts/turnarounds-short/turn-field-natural.txt` | the same 3 |
>
> Save each as `source/artwork/<Output file>` exactly as the prompt names it.
> Unlike the front, these views **do** take the costume photograph — a plate is
> only excluded from being its own reference.
>
> **Check each against the front:** boots tall, one whistle at the throat, hair
> down, horns unchanged, and every asymmetric piece on the correct side — blaster
> on her RIGHT, leash on her LEFT. **The profile views are where side errors
> appear**, and the prompts now carry a visibility rule telling the model which
> side the camera cannot see and forbidding it from moving a hidden piece round
> into shot.
>
> > **Known and accepted:** on the left and right prompts the budget settles
> > lower, and five tail sentences are dropped — articulation, the yoke rising
> > into the collar, the leather-minority list, the grip angle. All construction
> > detail; none of it silhouette or placement. Recorded as item 11 in
> > [`Prompt-Reliability-TODO.md`](Prompt-Reliability-TODO.md).
>
> ### THEN the sixteen slots, in this order
>
> Following
> [`../03-characters/Character-Build-Recipe.md`](../03-characters/Character-Build-Recipe.md).
> Paste from `prompts/slots-short/`, never from `prompts/`.
>
> | | Slots | Why this order |
> |---|---|---|
> | 1 | `02-scale_figure` | **Attempted 2026-08-03 and needs a re-roll — see below** |
> | 2 | `09-blaster` · `10-whistle_and_leash` · `11-mantle_detail` | Lock the plates before the figures |
> | 3 | `13/14/15-material_*` | Cloth, leather, hardware |
> | 4 | `06-portrait` · `07-headdress` · `08-expression_strip` | Close work, and the make-up board |
> | 5 | `01-hero` · `03-camp_day` · `04-captaining` · `05-candid` · `12-akk_together` | The frames |
> | 6 | `16-tone_collage`, then the boards | `--promo` is a separate command |
>
> **`09-blaster` now carries the barrel, receiver and grip detail** that used to
> sit in `must_show` — it moved there on 2026-08-03 because no full-length figure
> can resolve it.
>
> ### Then the boards
>
> ```bash
> source .venv/bin/activate
> python tools/board-generator/generate.py captain-jasu --validate
> python tools/board-generator/generate.py captain-jasu
> python tools/board-generator/generate.py captain-jasu --promo
> ```
>
> `--validate` should report only the images that genuinely do not exist yet.
> **She still has no `Character-Lock.md` and no `promo-data.yaml`** — see below.
>
> **Read [`../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md`](../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md) first.**
> Eight lessons from Shada, each paid for by a wasted generation.
>
> **Two things specific to her.** The Funko headdress references were detached on
> 2026-08-03 — a 1:1 head-to-body ratio is exactly how a 155 cm woman turns into a
> caricature, and the approved turnarounds carry the horns better anyway. And the
> akk dog goes wherever she is: it is 0.85 m at the crest, **level with the bottom
> of her belt**, measured off the rig.

> ### HOW THIS STARTED — the FIRST approved front failed three rules that never reached the generator
>
> *Historical, and the reason for the four passes above. The front described
> here was replaced on 2026-08-03; it survives as
> `evolution/00-first-approved-2026-08-01.png`.*
>
> Checked after the `must_show` rewrite, because the regeneration warned that
> `field` is approved and its artwork may no longer match. **It does not match,
> and it never did.** All five rules below were present in `outfits.yaml` at
> commit `2fb594f`, the commit that added and approved the front — verified
> against the file as it stood that day, not assumed.
>
> | Rule, as written on 2026-08-01 | In `turn-field-front` and `-left` | Why |
> |---|---|---|
> | **"THE BOOTS are tall and close to the calf"** | **Ankle boots**, in both views | Sentence 8 of the 2,166-character rule 2. Never sent |
> | **"BELOW THE WAIST, NARROW SPLIT PANELS hang straight and free"** | **Absent.** Skin-tight trousers with quilted outer-thigh panels applied flat to the leg | Sentences 7–9 of rule 2. Never sent |
> | **"A small worn WHISTLE on a cord at her throat, plainly visible"** | A whistle **at her belt**, on a chain | Sentence 2 of rule 6, cut at the old cap of 200. Never sent |
> | "THE COLLAR is stiff and STANDS, closed to the throat" | **Correct** | "collar to ankle" survived in the protected lead sentence |
> | "HER HAIR … swept UP AND BACK … a BUILT shape" | **Down and loose** | **Not the trim.** "SWEPT-UP HAIR" was in the lead sentence and reached the generator intact. This one was disobeyed — same fault already logged against `scale_figure` below |
>
> **This is the sixth failure again, with a costume instead of a shoulder cap.**
> The design was right, the rules were right, and three of them were cut before
> the generator saw them — so the image came back missing two of the five
> proportions the whole costume was derived from. `Character.md` names those
> proportions as *"high closed collar, hard square shoulder, long skirted coat,
> hard-cinched waist, tall boots"*. **The long skirted coat and the tall boots
> are the two that are missing.**
>
> The approval was not careless. It says what it was approving — *"the mantle,
> the palette, the bracers, the leg panels and the horns all landed"* — and all
> five of those are correct in the image. It simply never covered the three
> nobody had been shown.
>
> - [x] ~~**DECISION NEEDED: are the split panels part of this costume?**~~
>       **NO — deleted 2026-08-03 by the Production Designer.** They existed only
>       in `must_show`; there was never a component and the approved front never
>       showed one. **The rule is now the opposite** — nothing hangs from the
>       belt, no skirt, no tabard, no coat tail — which also blocks the drift it
>       was inviting. `Character.md` records that the "long skirted coat" of the
>       officer reference does not transfer. **The approved front was right about
>       this all along**, and one of its three mismatches was the document being
>       wrong rather than the image.
> ### THE BOOTS ARE DECIDED — TALL, 2026-08-03
>
> `evolution/01a-boots-tall.png`. **Tall wins and is now the default rule**, in
> the wording that actually produced it. Variant B was not generated — the tall
> boot was obviously right on sight.
>
> **The test also proved the scoped-exception wording works**: it attached the
> approved front, which shows ankle boots, and overrode the photograph on the
> footwear alone. That is reusable whenever one item has to change against an
> approved image.
>
> Two faults it exposed, both fixed:
>
> - **Two whistles** — the new throat rule added one and nothing removed the belt
>   one inherited from the photograph. Now `EXACTLY ONE WHISTLE`.
> - **Heeled boots** — the component note has said "flat" since 2026-08-01, and a
>   build note cannot reach a generator. There is now a heel rule, and the
>   component note says to re-heel a boot rather than accept the heel.
>
> - [ ] **NEXT, AND IT BLOCKS EVERYTHING: re-roll and re-approve the front.**
>       The approved reference now contradicts the rules on the boots and the
>       whistle, and **it is the reference for the four matched views and all
>       sixteen narrative slots** — so every image generated from it inherits
>       ankle boots and a belt whistle. Per `APPROVAL.md`, clear `approved:` in
>       `outfits.yaml`, re-roll the front, approve it by eye, then re-roll the
>       other four against it.
>
> ### ~~THE BOOTS GO TO AN A/B TEST~~ — staged and run 2026-08-03
>
> - [x] ~~**A/B the boots.** Generate both styles and choose from the pictures
>       rather than from the documents.~~ **Done.** The prompts and the full
>       write-up are in
>       [`../03-characters/captain-jasu/evolution/`](../03-characters/captain-jasu/evolution/README.md).
>       Nobody had ever seen her in the boots the build list describes, because
>       the sentence never reached a generator — so it was the first look at it,
>       not a re-roll.
> - [x] ~~**The whistle — belt or throat?**~~ **Throat, and exactly one.**
>       Settled 2026-08-03 by the same image, which came back wearing both.
>
> ### Open on her, 2026-08-03
>
> - [ ] **`02-scale_figure` — re-roll.** First attempt measured **133 cm** against
>       a 180 cm reference, and the landmark in the prompt was wrong: it said
>       "roughly the figure's eyebrows", which describes a 168 cm woman.
>       **Corrected to "the top of her head is level with his chin"**, now bounded
>       in both directions. At 155 cm the landmark is near-exact.
> - [ ] **Her hair came back down and loose.** The rule says swept UP AND BACK
>       into a large rolled, worked mass held high on the head, with the horns set
>       into it — *"a BUILT shape, not a hairstyle anyone maintains daily"*. Name
>       it in the correction; the headdress is half her design.
> - [ ] **RE-CAST to 155 cm (5 ft 1 in) on 2026-08-03.** Fifty-four references
>       updated. The five turnarounds are unaffected — they contain no scale
>       comparison — and the akk landmark is unchanged. `scale_figure` is the only
>       image the change invalidates.

**Status: FRONT APPROVED v2 (2026-08-03). FOUR VIEWS AND SIXTEEN SLOTS READY TO RUN. SIX BOARDS CONFIGURED.**

> The four other views were generated on 2026-08-01 against the *previous* front and **are now superseded** — they show ankle boots, a belt whistle and hair that no longer matches. They must be re-rolled against the new front, which is why they are the next thing in the run list above.

She is the first character in the production with a **full five-view turnaround
set built off an approved reference** — front approved and locked in
`outfits.yaml`, the other four generated against that image rather than from the
prompt alone, all five passing the mirror check. That method is now the standard
and it came from her.

**Her problem is the opposite of Shada's.** Shada's design churned and her
documents had to keep up. Jasu's design is settled and her *documents are
missing*: she has no `Character-Lock.md`, no `board-data.yaml`, no boards, no
promo sheet, and **her prompt pack is still a scaffold**, which means fourteen of
her nineteen images cannot be generated at all yet.

## What exists

| | |
|---|---|
| `Character.md` | Written. Cast, backstory, the departure from the script |
| `outfits.yaml` | One outfit, `field`. Approved front, `must_show:`, `handedness: right`, and the production's **first `components:` block** |
| `source/artwork/` | **5/5 turnarounds** — `turn-field-front` (approved), `-natural`, `-left`, `-right`, `-back` |
| `reference/` | 6 plates: actor headshot, concept sketch, two figure shots for the headdress, the A180 |
| `Prompts.md` | **Scaffold.** See the blocker below |

## What does not exist

| Missing | Consequence |
|---|---|
| `Character-Lock.md` | Her design is locked in practice and nowhere in writing. No drift-rejection list, so nothing catches the Imperial-officer and samurai retrievals except `outfits.yaml` |
| `board-data.yaml` | **She has no boards and no PDFs at all.** This is the board master; without it `generate.py` has nothing to lay out |
| `promo-data.yaml` | No promo sheet |
| 14 narrative prompts | Blocked by the scaffold, below |

---

## BLOCKER 1 — the prompt pack is a scaffold, and `split.py` refuses it

```
$ python tools/prompt-splitter/split.py captain-jasu
  skip captain-jasu: status is 'scaffold', not ready
  0 prompt files written.
```

`Prompts.md` carries `status: scaffold` and **16 `**NEEDS:**` markers**. Per
`03-characters/README.md` each one is an unanswered design question, and the pack
is deliberately not generatable until they are answered. **Fill in `Character.md`
first, then complete the pack** — that is the documented order and it exists
because a pack written ahead of the character invents its content.

The fourteen slots waiting on it:

- [ ] `portrait` — face, age, build, hair, upper layers, what she is reacting to
- [ ] `environment` — silhouette, posture, gait, what she is doing here
- [ ] `industrial_a` — ship corridor: does she belong in an interior or not?
- [ ] `industrial_b` — crew space: her standing in the group, who she sits near
- [ ] `industrial_c` — working interior: what task brings her here
- [ ] `detail_portrait` — the single distinguishing physical trait
- [ ] `species_strip` — **probably delete this slot.** It is for non-baseline
      species and the pack says to omit it if the character is baseline human
- [ ] `expression_strip` — the four emotional states that define her range
- [ ] `weapon_primary` — the A180. Reference plate already in `reference/props/`
- [ ] `weapon_secondary` — **or delete the slot** if she carries one thing
- [ ] `utility` — the kit list, and explicitly what she does *not* carry
- [ ] `maintenance` — the one habitual task that says who she is
- [ ] `materials` — her material list and palette subset, with hex values
- [ ] `tone-collage` — the share sheet

Two of those are decisions to *delete* a slot, not fill it. Nineteen images is
the current count; seventeen is the likely real one.

## BLOCKER 2 — two open design questions, and they block four other characters

Recorded in `Prompts.md` under *Open questions blocking this character*:

- [ ] **Does she carry a rank marking, and what is it?** Rank is one of the few
      sanctioned uses of bright colour in the Bible, so this is a palette
      decision as much as a costume one.
- [ ] **Her design sets the rank language for the entire mercenary faction.**

**This is the highest-leverage open item in the production, not just in her
folder.** Nyx, Yaslo Bis, Reya Fenn and the four-person Mercenary Kit all inherit
their rank language from her answer. Settling it after they are designed means
redoing them; settling it now costs one decision. Nyx is already flagged
**PRIORITY** in `Production-Status.md`.

---

## The order to work in

**1. Settle the two rank questions.** Everything else in this file, and four
other characters, sits behind them.

**2. Write `Character-Lock.md`.** Model it on Shada's. It must carry the
**drift-rejection list**, and hers is unusually load-bearing: the `do_not_retrieve`
block in `outfits.yaml` already names the two costumes an image model will try to
substitute — an **Imperial officer** and a **samurai** — and a third failure that
the *word* "captain" causes on its own, which is making her tall, broad and
formidable when she is 28, 155 cm and the smallest adult in the film. Those
belong in the lock, not only in the YAML.

**3. Complete `Prompts.md`** — answer the 16 `NEEDS:` markers, delete the slots
that do not apply, then set `status:` past `scaffold` so `split.py` will run.

**4. Generate the narrative images** against the approved front
(`turn-field-front.png`) plus the six reference plates. Fresh chat per image.
Save into `source/artwork/` under the exact `Output file:` name.

**5. Write `board-data.yaml`**, modelled on Shada's — she is the worked reference
for all five characters — then `promo-data.yaml`.

**6. Build the sheets:**

```bash
cd /home/tris/tpof-design && ./tools/regen captain-jasu

source .venv/bin/activate
python tools/board-generator/generate.py captain-jasu --validate
python tools/board-generator/generate.py captain-jasu
python tools/board-generator/generate.py captain-jasu --promo
```

**`regen` is the prompt half — one command, all three generators, commit and
push.** It exists because a hand-typed list omits `short.py`, which is the
generator that writes what you actually paste. That omission cost Shada two
images.

The board generator is a separate step and `--promo` is a separate command
again; neither is part of `regen`.

---

## Inherited from Shada — do not relearn these

Everything in `Prompt-Reliability-TODO.md` applies to her. The two that will bite
first:

- **Sixteen of Shada's twenty-one prompts cannot be pasted** because `short.py`
  only handles turnaround views. **Jasu's fourteen narrative slots will have the
  same problem the moment they generate.** Fixing `short.py` once fixes it for
  every character; see `Shada-Image-TODO.md`.
- ~~**Only ~13% of her `must_show` specification reaches the generator.**~~
  **FIXED 2026-08-03 — she is at 100%, and nothing is trimmed at all.** The 13%
  became 50% when the budget went to 8,000, and 100% when her **nine prose rules
  were rewritten as twenty-six imperative ones** on 2026-08-03. Total spec
  11,559 → 5,662 characters with no specification removed; `fit()` now settles at
  the 4,000 ceiling rather than a cap. Verified sentence by sentence against the
  rebuilt prompt.

  **What she was losing, and it was not small:** the stand collar, the boots, and
  *"they never gather, never flare, and never close into a skirt"* — all buried
  inside a single 2,166-character rule that also carried the body garment, the
  belt, the split panels and the made-to-measure line. **A skirt over the
  trousers is exactly the fault that cost Shada her fifth generation.**

  **Two rules are pinned:** her height and her head proportion — the two things
  the word "captain" breaks on its own.

  **She is now the worked example for fix 2**, the way Shada is for everything
  else. Shada is the remaining case and the hard one — 23,807 characters, and no
  budget rescues her.

- **Fresh chat per character.** A Shada prompt returned Jasu's costume — horns,
  yoke, quilted sleeves, matched bracers — because her set had been generated in
  the same conversation the day before.

- **One approved costume reference, scoped.** Two full-figure references
  competing over the same garment is a fight the written rules cannot win. Her
  six plates are safe because they are scoped to different things — the A180, the
  headdress, the actor — but do not add a second full costume photograph.

---

## See also

- [`Shada-Image-TODO.md`](Shada-Image-TODO.md) — the worked example, and the
  `short.py` blocker
- [`Prompt-Reliability-TODO.md`](Prompt-Reliability-TODO.md) — why the
  specification does not reach the generator
- [`Costume-Build-Method.md`](Costume-Build-Method.md) — her `components:` block
  is the model for every other character
- [`../03-characters/README.md`](../03-characters/README.md) — folder contents,
  the workflow, and the `evolution/` convention
