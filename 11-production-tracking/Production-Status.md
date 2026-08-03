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
| **Akk dog** | **Measured 2026-08-03 from the rig — 0.85 m at the crest, a very large dog.** Nine reference plates filed, dentition and Scene 25 reasoning recorded. Three renders still owed: front, rear and a seated pose. See `08-species/akk-dog/Creature.md` |
| **Prompt library** | **`09-prompt-library/README.md` is the index.** Read `Writing-Rules-A-Generator-Can-Follow.md` before editing any prompt |
| **Cast data** | **NOT IN THIS REPOSITORY, and that is a standing rule — `Cast-Data-Source.md`.** This repo is **public**; measurements, contracts, fees and contacts stay in Google Drive. Character specs live here, performer data does not |
| **Drive publishing** | **LIVE, and verified in sync 2026-08-04 — `Drive-Publishing.md`.** Signed-off images and finished boards go to Drive, one folder per character, three subfolders each: `turnarounds/`, `artwork/`, `boards/`. Jasu 5+3, Shada 5+16+7. The repo is the source of truth and Drive is overwritten. **The superseded v1 turnarounds are gone** — ankle boots and a belt whistle, cleared from the Jasu folder root. Re-publish with `./tools/publish-to-drive --go`; check with `./tools/check-drive`, daily by cron. **Deadline: rclone's shared Google client_id is retired during 2026 and we need our own before then** |
| **Scope, decided 2026-08-03** | **TIERED.** Baylan, Shin and Jasu get the full ~21-image treatment. Nyx, Krellis, Jeyin, Vala and the mercenaries get a reduced ~11-image set — turnarounds, portrait, expressions, scale plate, one materials plate, one narrative frame, tone collage, and three boards |
| **Mercenary Kit boards, decided 2026-08-03** | **ONE SHARED SET, FOUR COLUMNS.** Four turnaround boards as now, plus one costume, weapons and materials board treating all four side by side. They are a group design and the comparison is the point |
| **OPEN — species** | Nyx, Krellis, Vala, Jeyin, Reya, Yaslo all say TBD. **`outfits.yaml` cannot be written for any of them until this is settled.** Nyx may already be decided as baseline human |
| **OPEN — Vala** | Dies Sc.24, never shown. How much design does she need? Turns on how present she is *before* the death, not on the death itself |

## Image priority

**Costume turnarounds are the primary deliverable** — five images per outfit
(front, left, right, back, natural), plain grey studio background, everything
visible. They are what the costume department builds from.

Mood and narrative images are context. Three or four per character is enough.

| Character | Outfits | Turnaround prompts | Generated |
|---|---|---|---|
| Shada | 1 | 5 | **COMPLETE 2026-08-03. 21 of 21 images current, six boards and the promo sheet built.** The design locked 2026-08-02 — vest from hide to **cloth**, palette to **grey / grey-green / khaki**, plate density, tessellation, cap size and wear all fixed. TWO approved references with non-overlapping scopes: `turn-working-front` for the costume, `scale_portrait` for the make-up. **She is the worked example** — every rule in her pack has a documented failure behind it. Run list and reasoning in [`Shada-Image-TODO.md`](Shada-Image-TODO.md). Open, cosmetic only: `species_strip` carries a zip and a shingled cap, and can be re-rolled against the fixed prompt whenever convenient |
| Mercenary Kit | 4 people (Merc 1–4) | 20 | **Ids renamed to the people, 2026-08-01** — files are `turn-merc-1-front` etc, and there is now a board config with one turnaround sheet each. 3/4 fronts were generated but **are not in the repository**. **Merc 1, the Wookiee, has no generated turnaround by decision** — fill his sheet from concept art or build photos |
| Baylan | **1**, in two states | **10** | not started. Collapsed from four outfits to one on 2026-08-01 — the robe is a removable layer and the separate Jedi build is dropped. **The coat gained its own five-view set on 2026-08-01** (`working-coat`): the base five are the build record, the coat five are the silhouette the audience sees. **Chevron geometry fixed against reference the same day** — a centre-front plastron, five broad bands, throat to belt, narrower than his shoulders. `handedness: right`, checker clean. Lock his prop plates before his figures |
| Captain Jasu | 1 | 5 | **5/5 COMPLETE — REBUILT AS v2, 2026-08-03.** Front re-approved and all four views regenerated against it. **The v1 set was wrong and had been since 2026-08-01**: ankle boots, a whistle at the belt, and hair that matched a rule which was itself mistaken — none of it visible until her `must_show` was rewritten and the rules started reaching the generator. Four evolution passes settled it. **Handedness verified by zooming both profiles**: blaster flat against the near thigh on her right, edge-on past the hip on her left, leash mirroring it. The visibility rule added 2026-08-03 held. **16 slot images remain**, all prompts ready. See [`Jasu-Image-TODO.md`](Jasu-Image-TODO.md) |
| Shin | 3 states | 15 | not started — **blocked the same way Baylan was**: no `handedness:`, no `must_show:` on any state |

See `09-prompt-library/Turnaround-Block.md`.

## Characters

| Character | Status | Notes |
|---|---|---|
| Shada | **CLOSED 2026-08-03** | Was closed 2026-07-31 and revised three times on 2026-08-01, each turn settled by looking at a picture. Landed at **five pieces**: a **solid printed gauntlet with a cluster of dim wrist telltales**, a **loose scavenged shoulder cap**, a thigh patch, and a **restored pair of unmatched flank panels** laced across the centre front with vest cloth showing in the gap. The vest hide carries a **faint serpentine grain**. A **face-precedence rule** was added after a generation took its likeness off the costume reference. Documents, outfits.yaml and 21 prompts are current; the images are not. Recorded in `Character-Lock.md` v4.0; build cost in `Costume-Build-Method.md` (~440 plates, with the gauntlet's ~150 permanently removed by printing) |
| Baylan ("Bay") | In development | Locked for board review. Order 66 survivor; 11 scenes. Prompt pack ready. |
| Captain Jasu | **In development. CAST 2026-08-01** | Commands via the akk dog. Kills Krellis mid-sentence and smiles. **Killed by Nyx's deflected bolt, not by Baylan.** Physical design decided and `outfits.yaml` written — five turnaround prompts generate. **Cast against the script:** 28 and 155 cm, not "(40s), a powerful woman" — recorded as a departure in `Character.md`. Costume abstracted from a Japanese-officer reference per Bible §6.5. Backstory pending from the production |
| Nyx | In development | **PRIORITY.** The blade changes colour on him — killed **before** the massacre, not last. His deflected shot kills Jasu. Baseline human — decided. Design still TBD |
| Reya Fenn | Placeholder — **story function written** | Formerly "Freya". The helmet reveal in Sc.10; speaks first in the finale; killed in Baylan's massacre. Pincer group |
| **Yaslo Bis** | Placeholder | **Formerly `Loryl`** — renamed 2026-08-01. Deals the sabacc hand; pincer group; killed in Baylan's massacre |
| Mercenary Kit | In development | **Not a character — a build system.** 4 builds, one each to Merc 1–4. 33 prompts ready. Merc 1 is **the Wookiee**, confirmed in v10 |
| Jeyin | Placeholder | Shin's mother. Killed by the akk dog in the finale. Injury is a continuity track. |
| Shin | In development | **Co-lead.** Locked for board review. 11 scenes (incl. Sc.4 voice); pack ready. |
| Vala | Placeholder | **Survives.** Do not stage a death; show no injury. Killed by Shin in Film 2 |
| Krellis | Placeholder — **death and backstory written** | Escapee medic. **Shot through the head by Jasu mid-plea, Sc.25** — the hardest shot in the film. **Backstory from the production 2026-08-02, partial:** war-torn planet, oldest of many siblings, watched his parents die for want of medical help, captured protecting them, now the arena's medic. It answers the navigator question — his wayfinding is a childhood survival skill, so his death costs the group a *skill*, not a map — and it argues his kit is the wreck of a real professional one rather than improvised. Physical design still entirely TBD |

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
| **Forest Crash Site** | **Written 2026-08-03.** New. The wreck two clicks out — briefed in Sc.9, its smoke is set dressing in Sc.24–25, and no scene goes there. The smoke column is the only part of it the audience sees |

## Creatures

| Asset | Status | Notes |
|---|---|---|
| Akk Dog | Asset built and rigged | Jasu's. Unnamed. Kills Jeyin. **Survives** — left on the planet with Vala |

## Vehicles

| Asset | Status | Notes |
|---|---|---|
| Mercenary ship | **YT-2000.** Digital interior built | **Stolen by Baylan and Shin in the finale** — theirs from Film 2. Unnamed |
| Escapee ship | **Documented 2026-08-03. No visual design** | Crashes in Sc.2. Source of Jeyin's fatal wound. `06-vehicles/escapee-ship/Vehicle.md` records the three scripted lines that are all there is; the wreck now has a location document; **the torn metal still has no prop entry** |
