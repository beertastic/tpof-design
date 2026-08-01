# Production Design Status

## Governing documents

| Asset | Status |
|---|---|
| **Screenplay v9** | **Arrived 2026-08-01, as delivered by the writer. Outranks everything here** |
| **Screenplay v10** | **Working draft. `02-story/scenes/*.fountain` is the editable source; render with `tools/script-convert/render.py`** |
| **Script reconciliation** | **7 of 9 closed** — see `Script-v9-Reconciliation.md`. Age, Vala, the roster, the sabacc set, the deaths, the renumbering and the exit are all done |
| **Deaths and effects** | **New.** Every death, who does it, on or off camera, and what it costs — `Deaths-And-Effects.md` |
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
| Mercenary Kit | 4 people (Merc 1–4) | 20 | **Ids renamed to the people, 2026-08-01** — files are `turn-merc-1-front` etc, and there is now a board config with one turnaround sheet each. 3/4 fronts were generated but **are not in the repository**. **Merc 1, the Wookiee, has no generated turnaround by decision** — fill his sheet from concept art or build photos |
| Baylan | **1**, in two states | **10** | not started. Collapsed from four outfits to one on 2026-08-01 — the robe is a removable layer and the separate Jedi build is dropped. **The coat gained its own five-view set on 2026-08-01** (`working-coat`): the base five are the build record, the coat five are the silhouette the audience sees. **Chevron geometry fixed against reference the same day** — a centre-front plastron, five broad bands, throat to belt, narrower than his shoulders. `handedness: right`, checker clean. Lock his prop plates before his figures |
| Shin | 3 states | 15 | not started — **blocked the same way Baylan was**: no `handedness:`, no `must_show:` on any state |

See `09-prompt-library/Turnaround-Block.md`.

## Characters

| Character | Status | Notes |
|---|---|---|
| Shada | **Design closed** | Documents, outfits.yaml and 21 prompts current and consistent. Images are a guide, not a lock — regenerate as needed. See `Shada-Image-TODO.md` |
| Baylan ("Bay") | In development | Locked for board review. Order 66 survivor; 11 scenes. Prompt pack ready. |
| Captain Jasu | Placeholder — **death and finale written** | Commands via the akk dog. Kills Krellis mid-sentence and smiles. **Killed by Nyx's deflected bolt, not by Baylan** |
| Nyx | In development | **PRIORITY.** The blade changes colour on him — killed **before** the massacre, not last. His deflected shot kills Jasu. Baseline human — decided. Design still TBD |
| Reya Fenn | Placeholder — **story function written** | Formerly "Freya". The helmet reveal in Sc.10; speaks first in the finale; killed in Baylan's massacre. Pincer group |
| **Yaslo Bis** | Placeholder | **Formerly `Loryl`** — renamed 2026-08-01. Deals the sabacc hand; pincer group; killed in Baylan's massacre |
| Mercenary Kit | In development | **Not a character — a build system.** 4 builds, one each to Merc 1–4. 33 prompts ready. Merc 1 is **the Wookiee**, confirmed in v10 |
| Jeyin | Placeholder | Shin's mother. Killed by the akk dog in the finale. Injury is a continuity track. |
| Shin | In development | **Co-lead.** Locked for board review. 11 scenes (incl. Sc.4 voice); pack ready. |
| Vala | Placeholder | **Survives.** Do not stage a death; show no injury. Killed by Shin in Film 2 |
| Krellis | Placeholder — **death written** | Escapee medic. **Shot through the head by Jasu mid-plea, Sc.25** — the hardest shot in the film |

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
