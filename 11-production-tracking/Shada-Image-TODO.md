---
title: "Shada — Finish List"
asset_id: "TRACK-SHADA-IMAGES"
updated: "2026-07-31"
---

# Shada — Finish List

**Status: 20/20 images, 5/5 boards built, validation clean.**

Three images are on the boards but wrong. Replace those and she is done.

---

## Start here

```bash
cd /home/tris/tpof-design
source .venv/bin/activate
python tools/prompt-splitter/split.py shada
python tools/prompt-splitter/turnarounds.py shada
```

**Run this first, every time.** The prompts have changed since the last images
were made, and two images have already been lost to stale copies.

Then open a **fresh** ChatGPT conversation and attach both references *before*
pasting anything:

- `03-characters/shada/source/artwork/turn-working-front.png` — approved costume
- `03-characters/shada/reference/actor/dasha-svistunenko-heashot.jpg` — actor

Say: *"These are the approved costume and actor references. Match them exactly in
everything that follows."*

---

## The three to replace

### 1. `turn-working-back` — mirrored

Prompt: `03-characters/shada/prompts/turnarounds/turn-working-back.txt`

Every asymmetric element is on the wrong side. It is a horizontal flip of the
front view rather than the person turned around.

The prompt has been rewritten with a rotation-not-mirror instruction. **Paste it
whole.** After generating, check against the front view:

| Element | Front view | Back view must be |
|---|---|---|
| Gauntlet | viewer's left | **viewer's left** |
| Shoulder cap | viewer's right | **viewer's right** |
| Thigh patch | viewer's right | **viewer's right** |
| Blaster | viewer's left | **viewer's left** |
| Knife | viewer's right | **viewer's right** |

Both views show the **same side of the frame** for each item, because she turned
around rather than being flipped. If they swap, it is wrong.

### 2. `forest` — interior

Prompt: `03-characters/shada/prompts/04-forest.txt`

Currently an industrial workshop with a figure in the background. It is the
**dusk in-situ reference** — the reality check on whether her charcoal costume
separates from a wet forest at dusk.

The exterior-only rule is now in the prompt. The phrase that was pulling her
indoors — *"even when standing inside a starship"* — has been removed from her
character constants.

### 3. `maintenance` — interior

Prompt: `03-characters/shada/prompts/11-maintenance.txt`

Also an interior workshop. She is never indoors. Same fix: the prompt now states
exterior-only.

Consider a camp setting — cleaning her blaster by firelight, or checking kit
beside a tent.

---

## Optional

`camp_day` is an outdoor forest camp, which is right, but the light is dappled
shade. Its job is to be the **bright, readable daylight reference** — the image
where every patch, layer and fitting is legible. Worth one more attempt asking
for open overcast sky and a standing pose.

---

## Then rebuild

```bash
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
```

`--validate` catches missing images **and overlapping panels**. Both clean before
building.

---

## Do not regenerate

`turn-working-front` (approved), `-left`, `-right`, `-natural`, `hero`,
`scale_figure`, `scale_portrait`, `species_strip`, `expression_strip`, `blaster`,
`knife`, `utility`, and all four `material-*`.

`species_strip` and `expression_strip` are particularly good — leave them alone.

---

## Watch for

The failures that keep recurring:

- **Metal on both forearms.** One gauntlet, her right.
- **Matching scale patches.** Four patches, four different metals.
- **A bulky silhouette.** Close-fitting, cut to the figure.
- **Any interior.** Forest, clearing or camp only. If there is a wall or ceiling, it is wrong.
- **A modern coil zip.** Industrial hardware, or hooks and lacing.

Two or more together almost always means **the references were not attached**.

---

## After Shada

Baylan is next, and one thing must happen before generating any of his twenty
turnarounds:

**Declare `handedness:` in `03-characters/baylan/outfits.yaml`, and add
`must_show:` to each of his four outfits.**

The placement checker is already warning about both — he has a blaster, a holster
and a rifle with no side assigned. One edit now, or twenty regenerations later.
