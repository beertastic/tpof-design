# Changelog

All notable production-bible changes are recorded here.

## Unreleased

### Changed
- **Shada's two costume references swapped roles, 2026-08-02**, on the
  Production Designer's call. `flank-panels.png` becomes **the costume** —
  silhouette, vest, collar, placket, the laced panels, the thigh patch, belts,
  trousers and boots — and `costume-front-v2.png` is scoped down to three
  things: the loose scale shoulder cap, the printed gauntlet, and how big a
  plate is. They were the other way round, and the generation that day shows
  why that failed: **two full-figure references competing over the same garment
  is a fight the written rules cannot win.** The vest lost its stand collar to a
  crossover wrap and a full layered skirt appeared over the trousers. Only one
  photograph is the costume now. Where the primary reference is wrong — its
  smooth shoulder plate, its leather forearm, its oversized plates — the rules
  **say so by name**, which is a new kind of rule in this production: an image
  beats a paragraph, so a paragraph that contradicts an image has to point at it.
- **The shoulder cap is restated as a field of small scale plates** in the same
  10–15 mm hexagons as the rest of the costume — not a plate with a scale
  texture, and never one smooth plate. The specification already implied it; the
  new primary reference shows it wrong, so it is now said outright in three
  places. No change to the build, and the gauntlet stays a solid printed shell.

### Fixed
- **Seven of Shada's fourteen `must_show` rules re-ordered, 2026-08-02, so the
  load-bearing sentence leads.** A fifth generation came back with a skirt and
  tabard over the trousers, a crossover V-neck vest, the gauntlet and shoulder
  cap on each other's sides, unlaced flank panels, no thigh patch and the knife
  at her centre front. **Not one of those was a missing rule, and not one was
  the model disobeying.** Every element was the second half of a rule that
  reached the generator: the trousers were the *last* sentence of the boots rule
  and had never once survived the trim; the collar and placket were sentence two
  of the vest rule; the lacing and the cloth gap were sentences four and five of
  the panel rule; the word *knife* had never reached a generator at all, because
  the blaster description ate the whole allowance. `trim()` always keeps the
  opening sentence and then the first hard negation — so **the order of the
  sentences inside a rule matters more than the length of the rule.** All
  fourteen now land whole, with no ellipsis. No rule was shortened or removed.
- **`short.py` was missing from the run instructions.** The finish list named
  `split.py` and `turnarounds.py`, neither of which writes `turnarounds-short/`
  — the directory the pasted prompt actually comes from. Running the documented
  commands left the short prompts stale and reported success. The other
  characters' finish lists have not been checked for the same omission.

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

### Added
- **`Prompt-Reliability-TODO.md`, 2026-08-02** — written after a fourth Shada
  generation came back wrong, to stop patching symptoms. Measuring the pipeline
  rather than guessing at it produced the finding the individual fixes had all
  missed: **most of the specification never reaches the generator, and nothing
  reports it.** Shada's `must_show` rules total 18,061 characters and the pasted
  prompt carries 1,988 of them — **11%**. Captain Jasu 13%, Baylan 20%. Three of
  the four recorded failures were rules that existed, were correct, and were
  trimmed before the generator saw them, including the "NO YOKE" prohibition
  whose absence produced a yoke. The per-rule cap is uniform, so **every fix so
  far — promoting a buried clause to its own rule — has shortened all the
  others.** Also found while measuring: **Shin has no `must_show` rules at all**
  across her three outfits.

### Fixed
- **Costumes from other characters no longer leak in, 2026-08-02.** A Shada
  prompt returned **Captain Jasu's costume on Shada's face** — bone horns, a
  full-width scale yoke across the shoulders, a quilted long-sleeved bodysuit,
  matched wrist bracers, her hanging cord and pendant. Nothing in the prompt
  asked for any of it; Jasu's set had been generated the day before in the same
  conversation, and a model that has just drawn one character in a production
  carries it forward. **The fix is a fresh chat per character**, now stated in
  `Prompts.md` and the finish list. As a backstop the prompt names all four tells
  as hard prohibitions — *no horns, no headdress, no helmet, no yoke, no sleeves,
  no bodysuit, no second bracer* — because "NO YOKE" already existed inside the
  placement rule and the trim had quietly cut it.
- **Shada's non-negotiables cut from sixteen rules to fourteen** so the new
  prohibitions survive the trim. The per-rule cap is uniform and falls as rules
  are added, so a sixteenth rule shortens all the others: the anti-contamination
  rule was itself being truncated to its first two clauses. The vest rule
  absorbed the bare-arms rule (one garment, one coverage statement) and the
  metals rule absorbed plate size (one object), buying roughly 35 characters back
  on every rule in the file. All fourteen now reach the generator intact.
- **Full-figure reference photographs now state what they are NOT for.** A Shada
  generation came back in a perfect costume on the wrong woman: with six images
  attached and one of them a well-lit full-length portrait of a person in exactly
  this costume, the likeness was taken from the costume reference rather than the
  actor. Naming the actor photograph was never enough — the competing photographs
  had to be disqualified by name. Every costume reference label now leads with
  **NOT THE FACE**, a face-precedence rule sits first in `must_show`, and the
  lesson is written up in `Prompts.md` for every character, not just hers.
- **Short-prompt rules restructured so the operative clause survives the trim.**
  Sixteen non-negotiables had driven the per-rule cap low enough to cut the new
  face rule off mid-sentence — the one rule that had to survive. Long opening
  sentences were split into short negation-bearing ones, which is what `trim`
  keeps, and the serpentine-grain rule was folded into the vest rule it describes.
  All fifteen rules now reach the generator intact.

### Changed
- **Shada's flank panels restored, 2026-08-01 — the third revision of the day.**
  They were dropped that afternoon on the argument that a shaped panel each side,
  laced at the centre front, would read as a corset. A generation of exactly that
  shape showed otherwise: it reads as **brigandine**, and what keeps it off a
  corset is the **strip of vest cloth visible in the lacing gap**, with the
  collar, placket and centre-front seam still readable. That gap is now itself a
  rule, because a panel pair that closes up in the middle would fail exactly as
  feared. Five pieces, five metals: dull grey steel, blackened iron, dark bronze,
  pale worn pewter and rust-red oxidised iron — and **one alloy per panel**,
  since a panel speckled with four is decorative mottling.
- **Shada's gauntlet face changed from a hexagon field to plain worn plate**,
  matching the accepted render: a broad flat panel with a shallow border line, a
  scatter of rivets and a serpent swirl worn almost away. It reads more like a
  genuine hull offcut for being plain, and the hexagon field stays with the four
  flexible pieces.
- **Shada's plate count back to ~440**, having gone 440 → 220 → 440 across three
  revisions in a day. The printed gauntlet's ~150 plates are permanently gone —
  that saving survives every revision, because it is a property of the piece
  rather than of the coverage.
- **Shada's costume revised again on 2026-08-01, against a reference photograph
  supplied by the Production Designer** — held at
  `03-characters/shada/reference/approved/costume-direction-front.png` and now
  attached to every generated prompt. It **reverses the morning's revision
  below**: the flank panels are dropped and the torso carries no metal again.
  Three further changes come with it.
  - **The forearm gauntlet becomes a solid one-piece 3D-printed shell** with the
    hexagon field printed into it, plus **two dim amber telltales at the wrist**
    — the only light anywhere on the costume, and kept inside the Bible's
    "bright colour only for a significant personal item" allowance by staying
    grimy and half-dead. It is the single rigid piece she wears, which sharpens
    the flexible-scale rule rather than weakening it.
  - **The shoulder cap is specified as loose** — separate plates on a hand-cut
    backing, hanging off the point of the shoulder with daylight under its lower
    edge. "Shoulder cap" alone kept generating a fitted pauldron, and a cap that
    fits her is a cap somebody made for her.
  - **The vest hide gains a faint serpentine grain**, in the material rather
    than printed on it. This needed an explicit carve-out from the long-standing
    "scale as texture is wrong" prohibition, which governs the **armour** and
    still does. The costume now carries the idea in three registers: soft scale
    on skin, hard plate at three points, serpent grain in the cloth between.
  - **Brass and verdigris are off the costume.** Three metals now: dull grey
    steel, blackened iron, dark bronze.
  - **Belt and boots recorded** for the first time — two unmatched belts, and
    mid-calf boots with long leather straps wound criss-cross up the shaft.
- **Shada's plate count ~440 → ~220, halved.** The printed gauntlet removes ~150
  hand-laced plates on its own and the dropped flank panels take ~220 more. That
  saving is the strongest practical argument for printing the piece; nothing else
  in the build offers one of that size.
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
