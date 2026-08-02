---
title: "Captain Jasu — Finish List"
asset_id: "TRACK-JASU-IMAGES"
updated: "2026-08-02"
status: "open"
---

# Captain Jasu — Finish List

**Status: TURNAROUNDS COMPLETE, EVERYTHING ELSE NOT STARTED.**

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
formidable when she is 28, 150 cm and the smallest adult in the film. Those
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
cd /home/tris/tpof-design && source .venv/bin/activate
python tools/prompt-splitter/split.py captain-jasu
python tools/prompt-splitter/turnarounds.py captain-jasu
python tools/prompt-splitter/short.py captain-jasu
python tools/board-generator/generate.py captain-jasu --validate
python tools/board-generator/generate.py captain-jasu
python tools/board-generator/generate.py captain-jasu --promo
```

**Run all three splitter commands, every time.** `turnarounds.py` writes the long
prompts; **`short.py` writes what you actually paste.** Running the first two
alone leaves the short prompts stale and reports success. This omission cost
Shada two images.

---

## Inherited from Shada — do not relearn these

Everything in `Prompt-Reliability-TODO.md` applies to her. The two that will bite
first:

- **Sixteen of Shada's twenty-one prompts cannot be pasted** because `short.py`
  only handles turnaround views. **Jasu's fourteen narrative slots will have the
  same problem the moment they generate.** Fixing `short.py` once fixes it for
  every character; see `Shada-Image-TODO.md`.
- **Only ~13% of her `must_show` specification reaches the generator.** Her rules
  total 11,665 characters and the pasted prompt carries 1,601. The fix that works
  is ordering, not length: `trim()` always keeps the first sentence and then the
  first hard negation, so **the load-bearing clause must lead each rule.** Shada's
  fourteen rules were re-ordered on that basis and all now land whole. **Jasu's
  nine have not been.** Worth doing before her narrative run, not after.

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
