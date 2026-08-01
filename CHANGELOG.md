# Changelog

All notable production-bible changes are recorded here.

## Unreleased

## [0.3.0] - 2026-08-01

**The screenplay arrived, and the design documents had drifted from it.**

### Added
- **The screenplay**, as Fountain under `02-story/scenes/` — plain text, so a draft
  change is a diff. `tools/script-convert/` converts and renders it, with a
  round-trip check proving the conversion is word-exact.
- `AGENTS.md` — commands and mandatory checks for AI agents with repo access,
  including a gate that refuses to overwrite an approved reference image.
- `11-production-tracking/Deaths-And-Effects.md` — every death, who does it,
  whether the camera sees it, and what it costs.
- `11-production-tracking/Script-v9-Reconciliation.md` — where the documents and
  the script disagree. 7 of 9 closed.
- `02-story/Scene-Elements.md` — per-scene props, set dressings and costumes,
  extracted from the Filmanize export before it was deleted.
- `02-story/scenes/Baylan-Blocking-Act-One.md`, `Sc10-Sabacc-Showcase.md`.
- `03-characters/yaslo-bis/`, and a costume build note for Merc 1–4 as people.
- Screenplay v10: Baylan late 40s, the pincer group raised to four, Scenes 10, 13
  and 15 moved inside the ship, no tents, Shada corrected to "her".

### Changed
- **Baylan collapsed from four outfits to one** with a removable robe; the
  separate Scene 12 Jedi build dropped. `handedness: right`, aged 48.
- **`generic-mercenary` → `mercenary-kit`**, and its four builds renamed after the
  four people: `merc-1` … `merc-4`.
- **Crew roster rebuilt from the script** — ten individuals, three groups, every
  death assigned.
- **`07-vehicles/` folded into `06-vehicles/`**; `07-locations/mercenary-ship/`
  removed as a duplicate.
- Forest world and mercenary camp geography settled — the dampening field
  recorded as the reason the film happens on foot.
- Shada: sternum patch drop propagated to the lock, which had never received it.

### Removed
- **The Filmanize breakdown PDF.** It never matched the screenplay, invented a
  Scene 24A that has never existed, and had propagated that into nine files.
- `03-characters/loryl/` — the same part as Yaslo Bis, under a stale name.

### Fixed
- Scene 24A removed from every design document.
- Vala's death: the script never stages it. Reported as a conflict in error.
- Nyx dies **before** the massacre, and the misdirect is on Shin, not him.
- Jasu is killed by Nyx's deflected bolt, not by Baylan.
- Reya Fenn survives the grenade and dies in the finale.
- The akk dog is dismissed by Baylan, not knocked out.
- Placement checker: negation- and word-boundary-aware, so a removed weapon is no
  longer reported as unplaced.


## [0.2.0] - 2026-07-30

### Added
- Filmanize scene breakdown PDF and scene index.
- Placeholder character documents for the current cast and breakdown-derived roles.
- Initial Mercenaries and Slaves/Escapees faction documents.
- Initial location documents for the forest world, mercenary ship and script-specific environments.
- Production status and open-questions trackers.
