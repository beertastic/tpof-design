# Production Design Status

## Governing documents

| Asset | Status |
|---|---|
| **Screenplay v9** | **Arrived 2026-08-01, as delivered by the writer. Outranks everything here** |
| **Screenplay v10** | **Working draft. `02-story/scenes/*.fountain` is the editable source; render with `tools/script-convert/render.py`** |
| **Script reconciliation** | **OPEN — see `Script-v9-Reconciliation.md`. Age resolved (48); Vala was a false alarm. Seven items still need decisions** |
| Production Design Bible | v1.0 canonical |
| Filmanize Script Breakdown | imported — **scene numbering now superseded by v9** |
| Character template | available |
| Costume build method | Recorded — see `Costume-Build-Method.md` |

## Image priority

**Costume turnarounds are the primary deliverable** — five images per outfit
(front, left, right, back, natural), plain grey studio background, everything
visible. They are what the costume department builds from.

Mood and narrative images are context. Three or four per character is enough.

| Character | Outfits | Turnaround prompts | Generated |
|---|---|---|---|
| Shada | 1 | 5 | 5/5 — design closed, images indicative |
| Mercenary Kit | 4 builds (Merc 1–4) | 20 | 3/4 fronts done. **Merc 1, the Wookiee, has no turnaround by decision** — generator refuses the species; spec is written, bandolier plate stands in |
| Baylan | **1** | **5** | not started. Collapsed from four outfits to one on 2026-08-01 — the robe is a removable layer and the separate Jedi build is dropped. `handedness: right`, checker clean. Lock his prop plates before his figures |
| Shin | 3 states | 15 | not started — **blocked the same way Baylan was**: no `handedness:`, no `must_show:` on any state |

See `09-prompt-library/Turnaround-Block.md`.

## Characters

| Character | Status | Notes |
|---|---|---|
| Shada | **Design closed** | Documents, outfits.yaml and 21 prompts current and consistent. Images are a guide, not a lock — regenerate as needed. See `Shada-Image-TODO.md` |
| Baylan ("Bay") | In development | Locked for board review. Order 66 survivor; 11 scenes. Prompt pack ready. |
| Captain Jasu | Placeholder | Commands via the akk dog. Killed in the clearing |
| Nyx | In development | **PRIORITY.** The blade changes colour on him — killed **before** the massacre, not last. His deflected shot kills Jasu. Baseline human — decided. Design still TBD |
| Reya Fenn | Placeholder | Formerly "Freya". **Survives the grenade** — speaks first in the finale, killed in Baylan's massacre. Pincer group |
| **Yaslo Bis** | Placeholder | **Formerly `Loryl`** — renamed 2026-08-01. Deals the sabacc hand; pincer group; killed in Baylan's massacre |
| Mercenary Kit | In development | **Not a character — a build system.** 4 builds, one each to Merc 1–4. 33 prompts ready. Merc 1 is **the Wookiee**, confirmed in v10 |
| Jeyin | Placeholder | Shin's mother. Killed by the akk dog in the finale. Injury is a continuity track. |
| Shin | In development | **Co-lead.** Locked for board review. 11 scenes (incl. Sc.4 voice); pack ready. |
| Vala | Placeholder | **Survives.** Do not stage a death; show no injury. Killed by Shin in Film 2 |
| Krellis | Placeholder | Escapee medic |

## Factions

| Faction | Status |
|---|---|
| Mercenaries | **Roster v2.0, derived from script v10.** Ten individuals, three groups, every death assigned. See `Crew-Roster.md` |
| Slaves / Escapees | Placeholder |

## Locations

| Location | Status |
|---|---|
| Forest World | Placeholder |
| Mercenary Ship | Placeholder |
| Forest Mercenary Camp | Placeholder |
| Forest Escapee Camp | Placeholder |
| Force Vision | Placeholder |
| Sand Dunes | Placeholder |
| Forest Ditch | Placeholder |
| Forest Clearing | Placeholder |

## Creatures

| Asset | Status | Notes |
|---|---|---|
| Akk Dog | Asset built and rigged | Jasu's. Unnamed. Kills Jeyin. **Survives** — left on the planet with Vala |

## Vehicles

| Asset | Status | Notes |
|---|---|---|
| Mercenary ship | **YT-2000.** Digital interior built | **Stolen by Baylan and Shin in the finale** — theirs from Film 2. Unnamed |
| Escapee ship | Not started | Crashes in Sc.2. Source of Jeyin's fatal wound. Wreck is a location; the torn metal is a prop |
