---
title: "Shada — Image Generation TODO"
asset_id: "TRACK-SHADA-IMAGES"
updated: "2026-07-31"
---

# Shada — Image Generation TODO

**18 of 20 delivered.** Four boards built; the Performance board is blocked.

Before each session:

```bash
source .venv/bin/activate
python tools/prompt-splitter/split.py shada
python tools/prompt-splitter/turnarounds.py shada
```

Then, in a **fresh conversation**, attach both references before anything else:

- `03-characters/shada/source/artwork/turn-working-front.png` — approved costume
- `03-characters/shada/reference/actor/dasha-svistunenko-heashot.jpg` — actor

---

## 1. Regenerate — wrong, already delivered

| Prompt | Problem | What to add |
|---|---|---|
| `prompts/turnarounds/turn-working-back.txt` | **Mirrored.** Gauntlet on her left, shoulder cap on her right — both flipped | *"This is the same person rotated 180°, not a mirror image. Her RIGHT side is now on the viewer's LEFT. The gauntlet must appear on the viewer's LEFT."* |
| `prompts/05-scale_portrait.txt` | Full-body crouch in a dark interior. Brief asks for a close head-and-shoulders makeup reference in soft overcast daylight | Nothing — the prompt is now fixed. The costume rules were forcing the shot wide and no longer apply to this slot |
| `prompts/01-hero.txt` | Set in a busy settlement with market stalls. Brief says dim wet forest at dusk | *"WET FOREST AT DUSK. No buildings, no market, no crowd, no interior, no other people."* |

---

## 2. Generate — outstanding

| Prompt | Output | Notes |
|---|---|---|
| `prompts/03-camp_day.txt` | `camp_day.png` | **New.** The daylight in-situ reference. Bright overcast, costume fully legible |
| `prompts/04-forest.txt` | `forest.png` | The dusk in-situ reference — companion to the above |
| `prompts/06-species_strip.txt` | `species_strip.png` | Makeup reference: scale detail at hand, forearm, collarbone, eye |
| `prompts/07-expression_strip.txt` | `expression_strip.png` | Four expressions, evenly lit, consistent framing |

Also delete the superseded `source/artwork/camp_night.png` once `camp_day.png`
exists — nothing references it any more.

---

## 3. Then build

```bash
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
```

`--validate` reports missing images **and overlapping panels**. Both must be
clean before building.

---

## Known-good — do not regenerate

`turn-working-front` (approved), `turn-working-left`, `turn-working-right`,
`turn-working-natural`, `scale_figure`, `maintenance`, `blaster`, `knife`,
`utility`, and all four `material-*` macros.

---

## Watch for

The failures that keep recurring:

- **Both forearms with metal.** She has one gauntlet, on her right.
- **Matching scale patches.** Four patches, four different metals.
- **A bulky silhouette.** Close-fitting, cut to the figure.
- **A ship or settlement interior.** She is only ever in forest or camp.
- **A modern coil zip.** Industrial hardware, or hooks and lacing.

Two or more together almost always means **the reference images were not
attached**.
