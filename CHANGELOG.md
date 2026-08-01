# Changelog

All notable production-bible changes are recorded here.

## Unreleased

### Added
- **Captain Jasu's turnaround set completed, 2026-08-01 — the first in the
  production.** Her front was approved and locked, and the other four views were
  generated *against that image* rather than from the prompt alone. All five pass
  the mirror check. Six reference plates travel with the set: the approved front,
  the concept sketch, two figure shots for the headdress, the A180 and the actor.
  Every character before her had its five views generated independently and got
  five near-misses; this is the method that replaces that.
- **Captain Jasu carries the first `components:` block** in an `outfits.yaml` —
  material, construction, quantity, build route, and the things each item must
  *not* be. It is the durable half of a sourcing guide, kept beside the
  specification it came from so the two cannot silently disagree.

### Changed
- **Shada's armour revised structurally at the team's request, 2026-08-01.** The
  forearm gauntlet becomes **plain leather with no plates**; a pair of **scale
  flank panels** is added over her ribs, laced across the centre front. This
  **reverses "no metal on her torso"**, itself a decision from 2026-07-31. It is
  the better reading of a lock that already asked for *vital-area protection
  only* — panels over the liver and kidneys are that; a forearm gauntlet was not.
  The two panels are deliberately **unmatched** (dull grey steel / blackened
  iron), because a symmetrical pair meeting in the middle would read as a set
  made for her, which the whole costume argues against.
- **Shada's plate count ~370 → ~440** (+19%), the largest labour item in the
  costume. The gauntlet released ~150 plates; the flank pair costs ~220.
- **Shada's approved front turnaround UNLOCKED.** It shows a metal gauntlet and
  no flank panels, and every other view is handed it as "match exactly" — so
  leaving it approved was worse than having no reference. All five turnarounds
  and the narrative plates are superseded.
- **Shada's vest specified as a built garment** from a reference: stand collar,
  concealed placket, princess seams, cut-on shoulder, shaped raw hem. The
  concealed placket is what finally removes the modern coil zip, which repeated
  prohibitions never did.
- Shada gains explicit rules for **reptilian contact lenses** (previously six
  words at the end of the face rule, trimmed from every prompt) and **torso
  coverage** (previously unstated, so a crop top satisfied the brief).
- **Where sourcing lives, decided 2026-08-01.** Supplier links, prices and stock
  go to the production's Drive; they never enter this repository. They rot — a
  shop closes, a listing sells, a price doubles — and a repository full of dead
  links is worse than none, because somebody trusts it. Same rule as
  `10-assets/study/`: write down the derived decision, never the perishable
  source.
- **Captain Jasu cast against the script, 2026-08-01** — 28 and 150 cm, not
  "(40s), a powerful woman". Recorded as a deliberate departure in her
  `Character.md` rather than quietly absorbed.

### Fixed
- **The short prompts were silently dropping the sentences that mattered.** Four
  wrong images this week traced to the same cause, not to the generator: Baylan's
  chevron geometry, Shada's patch placement, her bare-arms exception and her
  plate size were all specified correctly in `outfits.yaml` and trimmed away
  before reaching a model. Rules now lead with the operative fact, because only
  the first sentence is guaranteed to survive.
- **Removed the echo-back block from the short prompts** (`tools/prompt-splitter/short.py`).
  It asked the model to recite the commit and hash and never once did. Tested
  before removing: the model holds the pasted text exactly, it simply does not
  recite provenance when generating. It cost 401 characters — ~40 off *every*
  non-negotiable — which is the budget those four failures were competing for.
  Retained in the long prompts and in `AGENTS.md` for connected-repo runs, where
  the question it asks is real.
- Baylan's long coat gains **its own five-view turnaround set**; the base five
  stay the build record.
- **A sourcing guide written from Jasu's turnaround photographs alone
  contradicted four locked decisions** — a leather pauldron for a mantle
  specified as stiffened cloth, carved hair rings for horns specified as unworked
  trophies, a cardboard tube in leather-look fabric for the one weapon she keeps
  clean and serviced, and secondhand petite-sizing advice for the only
  made-to-measure costume in the film. It also demoted the whistle — her entire
  command structure — to a "vintage keychain fob", and omitted the leash. None of
  that was unreasonable from five photographs: **sourcing written away from the
  specification drifts toward what the pictures look like rather than what the
  design says.** Its one genuinely good idea was kept — equestrian jodhpurs and
  breeches, and searching by *construction* rather than by look.

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
