# Changelog

All notable production-bible changes are recorded here.

- **Captain Jasu re-cast to 155 cm, 2026-08-03** — 5 ft 1 in, not 4 ft 11 in.
  Fifty-four references updated across eleven files: `outfits.yaml`,
  `Character.md`, `Prompts.md`, `board-data.yaml`, the akk dog's landmark table,
  the faction document, the script reconciliation and the status board. Derived
  numbers recomputed, not merely substituted — Baylan is now **43 cm** taller
  rather than 48, she is **86%** of a 1.8 m figure rather than 83%, and her waist
  sits at **93 cm** rather than 90.

  **Nothing about the design moves.** She is still the smallest adult in the film,
  the animal is still her rank, and her own animal still outweighs her. Two things
  are unaffected and were checked rather than assumed: the **five turnarounds**
  contain no scale comparison, and the **akk dog's landmark is unchanged** — its
  crest sits just under her belt at either height, because 5 cm on her is less
  than the gap between belt and crest. **`scale_figure` is the only image the
  change invalidates**, and it needed re-rolling anyway.

  The scale landmark got *better*: at 150 cm her head top sat just under a 1.8 m
  figure's chin, at 155 cm it is level with it.

## Unreleased

### Added

- **Signed-off turnarounds now publish to Google Drive, 2026-08-03** —
  `tools/publish-to-drive` and `11-production-tracking/Drive-Publishing.md`. One
  folder per character under Costume / Wardrobe, so the costume department builds
  from the current images.

  **The repository is the source of truth and Drive is overwritten**, including
  deleting anything in the character's `turnarounds/` folder that the repo does
  not have. That is deliberate: the failure being prevented is somebody building
  from a superseded plate, and a stale file beside a current one is exactly how
  that happens — a duplicate is worse than an absence, because an absence gets
  noticed. Only `turn-*.png` is synced, into a `turnarounds/` subfolder, so a
  sync can never delete build guides or sketches sharing the folder.

  **Sign-off is an `approved:` block in `outfits.yaml`** — already the gate for
  the board generator, the turnaround prompts and `APPROVAL.md`, so it is the
  gate here too.

  **It found live drift immediately.** Captain Jasu's Drive folder holds the
  **superseded v1 turnarounds** from 2026-08-01: `turn-field-front.png` there is
  2,207,890 bytes, byte-for-byte the v1 front archived tonight as
  `evolution/00-first-approved-2026-08-01.png`. **The costume department is
  currently looking at ankle boots and a whistle at the belt.**

  **Why rclone and not the Drive connector**, both checked rather than assumed:
  the connector **cannot update or delete**, only create — so re-publishing
  through it leaves two files with the same name and different contents, which is
  the exact failure the process exists to prevent. And it carries images inline,
  about 2.7 million characters for a 2 MB plate. So the connector does the
  **checking**, which needs only listings, and rclone does the moving.

  **Not yet runnable — rclone is not installed.** The script says so and prints
  the setup. Publishing Jasu is the first job once it is.

- **Drive publishing widened to every image and every board, 2026-08-03** — it
  was turnarounds only. Each approved character now gets three subfolders:
  `turnarounds/` for the build plates, `artwork/` for every other generated
  `.png`, and `boards/` for the finished PDFs. That is 8 images for Jasu and 21
  images plus 7 boards for Shada. `evolution/` and `renders/` deliberately do
  **not** publish — the first is superseded by definition, and the second is the
  same content as the PDFs at twenty times the bytes.

  **Two real faults were found by checking the live folder rather than assuming
  it, and both would have caused the exact duplicate this tool exists to
  prevent.**

  **The Drive folder names are not the repo slugs.** `captain-jasu` lives in a
  folder called **`Jasu`**, named by hand long before any of this. The old
  script would have created a *second* folder called `captain-jasu` beside it.
  The mapping is now explicit in `drive_folder()`, an unmapped character is an
  error rather than a new folder, and every run prints the folder names actually
  on Drive so a mismatch is visible before anything is written.

  **The superseded v1 plates are loose at the folder root, not in a
  `turnarounds/` subfolder.** Publishing into subfolders would have left all
  five sitting one level up, still called `turn-field-front.png` — two files,
  same name, different boots. The sync cannot reach the folder root by design,
  because a hand-written build guide lives there, so the script now **reports**
  shadowed files and removes them only on `--purge-shadows`, and only those
  whose names exactly match something being published.

- **Drive published for the first time, 2026-08-04** — Jasu (5 turnarounds,
  3 artwork) and Shada (5 turnarounds, 16 artwork, 7 boards). Shada's folder was
  created by the run. **Drive now matches the repository**, verified by
  `--check` byte for byte and again through the Drive connector, which is a
  different account path entirely.

  **The superseded v1 turnarounds are gone.** The costume department was looking
  at ankle boots, a whistle at the belt and the superseded hair, from five files
  loose at the root of Jasu's folder. `--purge-shadows` removed exactly those
  five; the hand-written `Jasu_outfit_build_guide.md` beside them was untouched.

  **The setup failure was `client_id = scope1`** — the answer to the scope
  question, typed one prompt too early into a field whose help says "Leave blank
  normally". It cost an evening because rclone 1.60 could only report it as
  `No code returned by remote server` followed by a browser showing
  `ERR_CONNECTION_REFUSED`, which reads as a firewall problem. Upgrading to 1.75
  did not fix it; it made it legible — `401 invalid_client`.

  **Dated warning, now recorded:** rclone's shared Google client_id **is retired
  during 2026**. A client id of our own is needed before then, and the steps are
  in `Drive-Publishing.md`.

- **The daily Drive check is now a script, 2026-08-03** — `tools/check-drive`,
  read-only, exit 1 on drift, with a `crontab` line in `Drive-Publishing.md`. It
  reports four states per set: stale on Drive (the dangerous one), not yet
  published, same name but different bytes, and shadowed at the folder root.

  It never writes, because the fix always needs a person to have decided the
  repository is right. It logs to `~/.local/state/tpof/drive-check.log` and
  raises a desktop notification on drift, so a cron job nobody reads still
  reaches somebody on the day it matters.

  **`PUBLISHED-FROM-REPO.txt` lost its wall-clock timestamp** and gained the
  commit that last touched those exact files, plus their sizes. It is now a pure
  function of repository content, which is what makes a daily byte-for-byte
  check possible — a timestamp would have reported drift on every single run.

  A daily drift check is logged in `Drive-Publishing.md`, with what counts as
  drift and the note that a scheduled agent is the right shape for it — reporting
  only, because the fix needs a person to have decided the repo is right.

### Added

- **Captain Jasu's turnaround set is complete and correct — v2, 2026-08-03.**
  Front re-approved and all four remaining views regenerated against it. The v1
  set, generated 2026-08-01, is superseded in full: it carried ankle boots, a
  whistle at the belt and hair matching a rule that was itself wrong, and none of
  that was visible until her `must_show` was rewritten and the rules began
  reaching the generator.

  **Handedness was verified rather than eyeballed** — both profiles cropped and
  magnified at the hip. In the right profile the holster lies flat against the
  near thigh at full width with no leash visible; in the left it appears edge-on,
  protruding past the front of the hip only, with the leash on the near side.
  That is exactly how a far-side holster reads from the opposite profile.

  **So the visibility rule added on 2026-08-03 works.** It was written against an
  A/B in which *nothing that belonged on the hidden side survived being hidden* —
  the most emphatically described object in the costume was dragged round into
  shot. This time everything stayed where it belongs.

  Also correct in all four: tall boots with a low heel, exactly one whistle at
  the throat, hair down and loose, asymmetric pale horns, forearm-only bracers,
  and the blaster barrel's six vent holes legible in the back view.

  **Two watch items, neither a defect.** The heel sits slightly higher in
  `natural` than the rest — the one detail already got wrong once. And the mantle
  reads smoother in the two profiles than in front and back, which is *predicted*:
  `Ribbed, quilted or pleated.` is one of the five tail sentences the profile
  views drop, because their longer shot text settles the budget lower. Item 11 in
  `Prompt-Reliability-TODO.md`.

### Fixed

- **Captain Jasu's board governing-document paths were both broken, 2026-08-03.**
  `--validate` reported *"missing governing document"* for the Production Design
  Bible and the akk dog creature document — the only two failures in her entire
  board set that were not simply an image not generated yet. They were written as
  a bare title (`Production Design Bible v1.0`) and a repo-root path
  (`08-species/akk-dog/Creature.md`), where the validator resolves relative to the
  character folder. Rewritten in Shada's style, and the faction document added
  while there. **Validation now reports only genuinely missing images.**

### Added

- **A standing rule on cast data, 2026-08-03 — it stays in Google Drive and
  never enters this repository.** `11-production-tracking/Cast-Data-Source.md`.

  A proposal to import the production's Drive data — measurements and hundreds of
  other points — ran into the fact that **this repository is public**, and public
  deliberately: every prompt's `raw.githubusercontent.com` fallback resolves only
  on a public repo, and `regen` treats a failed push as a hard error for that
  reason.

  **The decisive detail:** the cast includes at least one performer with a
  chaperone budgeted, and their full body measurements are in the Drive sheet.
  A git push is not reversible by a later commit.

  So the split is: **character specifications here, performer data in Drive.**
  *"Captain Jasu is 155 cm"* is a design fact about a fictional person. The
  measurement record of the performer playing her is not, even though one derives
  from the other. The costume department uses both and gets them from two places.

  **What the Drive check gave back, without importing anything:**
  - **"Charlie" is confirmed a cast member and never a character** — it appears
    in the cast payment schedule. `Open-Questions.md` had resolved this by
    inference on 2026-07-30; it is now settled outright.
  - **Jasu's 155 cm is confirmed by casting** — her performer is 5 ft 1 in, which
    is 154.9 cm. A Drive sheet rounds the same figure to 156; that is a rounding,
    not a disagreement, and the 2026-08-03 recast was right.
  - **Baylan at 198 cm confirmed.**
  - **Merc 1 is cast as the largest performer in the company**, consistent with
    the Wookiee and with the large mercenary in the Vala fight — though it does
    not settle that open question, which is about cost and prosthetics.

  **Two things flagged that this repository does not own:** a live webmail
  password sitting in plaintext in a shared Drive sheet, and the fact that the
  named actor headshots already committed here are public — the exact case
  `CAST-REFERENCE.md` warned about, now recorded there as an open decision with
  the consent question stated and the point that removal would need a history
  rewrite rather than a `git rm`.

### Changed

- **Captain Jasu's boots are TALL, decided 2026-08-03 from an A/B** —
  `03-characters/captain-jasu/evolution/01a-boots-tall.png`. The approved front
  showed ankle boots; `outfits.yaml` and the build list said tall. They had
  contradicted each other since 2026-08-01 because the boots sentence sat eighth
  in a 2,166-character rule and was never sent to a generator, so **nobody had
  ever seen the design the build list describes.** Tall won on sight and variant
  B was never generated.

  **The test's method is the reusable part.** The prompt attached the approved
  front — which a front view is normally never given — scoped so the photograph
  governed everything except the footwear. It held: tall boots came back against
  a reference showing low ones. That is the wording to use whenever one item has
  to change against an approved image.

  **Two faults the image exposed, both now fixed:**
  - **Two whistles.** The new throat rule added one; the belt one stayed,
    inherited from the photograph. Nothing had ever said there was only one.
    Now `EXACTLY ONE WHISTLE`, with the belt named as carrying no second.
  - **Heeled boots.** The component note has said "flat" since 2026-08-01, and
    **a build note cannot reach a generator.** There is now a heel rule in
    `must_show` — flat or as near flat as the boot allows, ~25 mm — and the
    component note says to re-heel a boot that is otherwise right, a cobbler's
    job and cheaper than the boot.

  **The approved front is now wrong and blocks everything downstream.** It is the
  reference for the four matched views and all sixteen narrative slots, so every
  image made from it inherits ankle boots and a belt whistle. It must be cleared,
  re-rolled and re-approved before anything else generates.
  *(Done the same day — see the v2 turnaround entry at the top of Unreleased.)*

### Fixed

- **Two general traps in `short.py`, found while checking Jasu's rewrite.**
  Neither is fixed in the tool; both are written up in
  `Prompt-Reliability-TODO.md` as items 10 and 11.
  - **`"NONE"` is not a hard token.** `trim()` protects the first sentence
    matching `NOT|NEVER|NO|NOTHING|ONLY|ALWAYS|MUST`, and `\bNO\b` does not match
    `NONE`. Jasu's anti-pale-drift clause — the rule that exists *because* her
    costume drifted pale — began with "NONE of them is bone, cream, ivory or pale
    grey" and was therefore unprotected, so on two views it was dropped while the
    bracer geometry was kept. Rewritten with `NEVER`. Every other character was
    scanned and none has the same shape, but `NEITHER`, `NOR`, `AVOID`, `EXCEPT`
    and `WITHOUT` are the same trap waiting.
  - **The dropped-sentence report is per outfit; the cap is per view.** The
    profile views carry longer shot text and settle far lower. On Jasu the front
    reached the 4,000 ceiling with nothing trimmed while **left and right were
    each dropping five sentences, with no warning printed at all.** The profiles
    are exactly where placement and handedness faults appear.

- **Captain Jasu's `must_show` rewritten, 2026-08-03 — nine prose rules became
  twenty-six imperative ones, and her specification went from 50% reaching the
  generator to 100%.** Total 11,559 → 5,662 characters with **nothing removed
  from the design**. `fit()` now settles at the 4,000 per-rule ceiling instead of
  a cap of 664, which means no rule is trimmed at all. Verified by rebuilding the
  prompt and checking every sentence of every rule survives into it — zero
  missing.

  **What the 50% was hiding was not padding.** Her rule 2 was a single
  2,166-character block carrying eight separate garments — the body garment, the
  collar, the agility, the belt, the split panels, the boots, the made-to-measure
  line and the not-for-display line. `trim()` keeps the first sentence and the
  first negation, so the rest never reached a generator. **The stand collar, the
  boots and *"they never gather, never flare, and never close into a skirt"* were
  being dropped every single time.** A skirt over the trousers is precisely the
  fault that cost Shada her fifth generation, and Jasu was set up to repeat it.

  **The method, which is mechanical and should be reused.** `trim()` protects
  sentence one and the first sentence containing
  `NOT|NEVER|NO|NOTHING|ONLY|ALWAYS|MUST`, then competes on length. So: lead with
  the constraint rather than the subject, make sentence two a prohibition, keep
  each rule under the cap, and **give every enforceable thing its own rule** — a
  rule covering two objects only ever protects one of them. Her height and her
  head proportion are `pin: true`; both are the failures the word "captain"
  causes on its own.

  **No reasoning was lost.** Every cut sentence was checked against
  `Character.md` first, and the one line not already there — that the garment is
  what a very small person wears to keep up with people twice her size — was
  added to it. The A180's barrel, receiver and grip detail moved to slot 9 of
  `Prompts.md`: ~700 characters that no full-length figure can resolve, which
  were being carried in all 21 prompts to be legible in one. That is fix 9's
  argument, applied by hand because per-rule slot applicability does not exist
  yet.

### Added

- **The escapees' ship and its crash site have documents, 2026-08-03** — two
  assets that the script names in three scenes and the repository had never
  filed. `06-vehicles/escapee-ship/Vehicle.md` and
  `07-locations/forest-crash-site/Location.md`.

  **Neither decides any visual design**, because none has been decided. They
  record what the three scripted lines fix — *rickety*, tumbling, engine smoke,
  dropping past the treeline (Sc.2); **two clicks** from the mercenary landing
  and the dampening field as the cause (Sc.9); the column of smoke **still up a
  full day later** and the bearing of the last shot in the film (Sc.25) — and
  everything else is written down as open.

  Three things came out of writing them:
  - **Scene 2 is the ship's only appearance**, perhaps three seconds, in the air,
    at distance. So the entire design load is **silhouette and behaviour**, and
    the contrast with the maintained YT-2000 has to survive being read in a few
    seconds against an evening sky.
  - **The smoke column is the only part of the crash site any audience sees**,
    and it is up across evening, night and morning — lit four ways, in every
    exterior scene from 3 onward. It should be planned once and treated as part
    of the sky, not added where it happens to be scripted.
  - **The torn metal that impaled Jeyin still has no entry under `05-props/`.**
    It is needed only if the crash is filmed, but the *wound* is on screen from
    Sc.8 and a prosthetic has to match something — so whoever designs the wound
    is implicitly designing the prop. Now named as outstanding in three places
    rather than none.

  `Open-Questions.md` closed accordingly; `forest-world`, `06-vehicles/README.md`
  and the status board updated.
- **Krellis has a backstory, 2026-08-02** — partial, from the production, and
  recorded as given with the interpretation flags marked. War-torn planet, oldest
  of many siblings, watched his parents die for want of medical support and vowed
  to become a medic, learned to navigate danger to keep the family safe, captured
  protecting his siblings, and is now the arena's medic. It settles three things
  the documents were carrying open:
  - **The navigator question.** His wayfinding is a **childhood survival skill**,
    not knowledge of Prodona — so when he is shot in the clearing the group loses
    a *skill*, not a map, and a skill cannot be handed over in the seconds he has.
  - **The size and the gentleness, which had not reconciled.** His body has spent
    its whole life **interposing** — oldest of many, the man of the family from
    childhood, captured protecting his siblings. Stepping in front of Shin and
    Jeyin in Sc.25 is the last instance of a lifelong habit, not courage arriving
    from nowhere. And his death repeats his origin exactly: he became a medic
    because he watched people he loved die for want of help, and he dies trying to
    save two more with the only instrument he has left.
  - **What his kit probably is.** He held the *post* of arena medic, with
    sanctioned access to supplies, so his gear is likelier **the wreck of a real
    working kit** than a bag of improvisations. **The poverty is the arena's, not
    his** — and a professional stripped of supply reads as loss where an amateur
    with scraps reads only as poor. Propagated to
    `04-factions/slaves-escapees/Faction.md`, which had assumed the latter.

  It also partly answers a question in **Vala's** file: he was her medic, so
  whatever she carries from twenty years in the arena, he set it. **Their shared
  history is on her body, not in their gear.**
- **`Jasu-Image-TODO.md`, 2026-08-02**, and a run list at the top of
  `Shada-Image-TODO.md`. Two characters, two opposite problems. Shada's design
  churned and her documents kept up: she has 21 current prompts and 17 images to
  regenerate, in a fixed order starting with `scale_portrait` as a scoped
  **makeup** lock. Jasu's design is settled and her *documents are missing*: no
  `Character-Lock.md`, no `board-data.yaml`, no boards, and a `Prompts.md` still
  marked `scaffold` with **16 `NEEDS:` markers**, so `split.py` refuses it and
  fourteen of her images cannot be generated at all. Writing hers surfaced the
  item with the widest blast radius in the production: **her rank language is
  undecided, and Nyx, Yaslo Bis, Reya Fenn and the four-person Mercenary Kit all
  inherit it** — settling it after they are designed means redoing them.
- **A blocker found while writing the run list: sixteen of Shada's twenty-one
  prompts cannot be pasted.** `short.py` only builds short prompts for the five
  turnaround views. The numbered slots exist only as their long files — ~16–18 KB
  for the plates and **~65 KB** for `hero`, `camp_day`, `forest`, `maintenance`
  and `tone-collage`, against a real budget near 4,000 characters. Generating
  from them means handing the host a file to compress, which is exactly the
  silent-truncation failure `Prompt-Reliability-TODO.md` documents. Recorded, not
  yet fixed; the fix is to extend `short.py` one level up from `VIEWS`, and it
  would fix every character at once.
- **`evolution/` — a per-character convention for recording how a design
  converged, 2026-08-02.** One prompt and one image per pass, zero-padded, the
  slug naming the variable that pass changed, with a README saying what each pass
  changed *and what it broke while doing it*. Shada's seven passes are the worked
  example. Three rules: it is history and never specification, evolution images
  are never attached to a generation prompt, and variant prompts never sit in
  `prompts/` — that directory is generated and `split.py` deletes `*.txt` there on
  every run. The folder is created when a character's first variant is run; there
  is no value in empty ones.
- **Shada's costume is LOCKED, 2026-08-02, and has its first approved reference.**
  `turn-working-front.png` is now the single match target for every other view
  and every narrative plate. Seven variant generations in one session settled it,
  each testing one variable against the last accepted image rather than against
  the prompt — the method Captain Jasu's turnaround set proved, applied to design
  rather than to views.

### Changed
- **The vest is CLOTH, not scavenged hide, and the palette is GREY.** Both on the
  Production Designer's call, both tested as variants first. A heavy close-woven
  working fabric in a dusty sun-bleached grey with a hint of khaki-green; trousers
  a colder grey-green; **all leather in grey-brown taupe**, which it resists — it
  drifts warm on nearly every generation and warm leather pulls the whole costume
  back toward the brown it left behind. The **bronze thigh patch is now the only
  warm thing in the costume**, which makes it read harder than it ever did against
  brown. The hide was never wrong; cloth reads as the flexible base layer the hard
  pieces are strapped over, and grey lets the five metals separate from the
  garment instead of sinking into it.
- **The serpentine grain survived the material change** — it is woven into the
  cloth now rather than pressed into a hide. It could have gone with the leather;
  it was kept because it is the quietest thing in the costume carrying her
  ancestry and nothing else does that job. For the build this is a **sourcing**
  requirement, not a finishing one: the texture has to be found in the cloth at
  purchase, and the thing the market will offer instead is a reptile print.
- **Plate density fixed at about twelve across a flank panel**, fifteen rows down.
  Millimetres had failed five times. What worked was a count, with **a floor as
  well as a ceiling** — one pass shrank the plates until the panels became chain
  mail, which is as wrong as a dozen big tiles. Both failure modes are now named.
- **Tessellation is described positively for the first time** — every plate flat
  in the same plane, six flat sides butted against six, a thin dark line of
  backing between neighbours and nothing else, no plate riding over another and no
  shadow falling from one onto the next. "Never overlapped" had been in the
  specification for days and the plates shingled anyway. **A prohibition does not
  tell a generator what to draw.**
- **The shoulder cap is a palm's width** — the point of the shoulder and nothing
  else, after three passes each of which overshot the last. Recorded with the
  reason: an oversized cap is how a **yoke** gets back into this costume under
  another name, and the yoke is this character's most persistent failure.
- **Wear is now part of the specification, not a finishing note.** Five to ten
  plates missing from each flank panel and three to five from the shoulder cap,
  leaving the hand-cut backing showing through at the edges, the waist and the
  hip — the places that catch and flex — with bent corners, cracked plates, rows
  out of line and lacing spliced with a different cord. For the build this is an
  instruction about **where** the gaps fall, not a licence to make fewer plates:
  scattered absence reads as wear, regular absence reads as a pattern. It takes
  about 15 plates off the ~440 count, which is noise, and the labour is unchanged.
- **The two direction photographs are retired.** `costume-front-v2.png` and
  `flank-panels.png` are kept on disk as history and attached to nothing. Every
  fault they carried has been designed out.

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
- **Three prompt packs were pointing the operator at the long files, 2026-08-03.**
  A follow-up to the note left open on 2026-08-02, which said the other
  characters' run instructions had not been checked for the missing-`short.py`
  omission. They had it — and something worse.

  Shada's, Baylan's and Shin's `Prompts.md` headers offered
  `prompts/turnarounds/` and `prompts/` as *"paste-ready"*. Those are the
  specification files, 5–8× over any generator's budget; pasting one hands the
  compression to the host, where nothing can report on what was dropped. That is
  the precise failure `Prompt-Reliability-TODO.md` exists to describe, and the
  packs were recommending it. `slots-short/` and `turnarounds-short/` have
  existed for all five characters since fix 7 and none of the three mentioned
  either.

  All three now lead with **paste from the short directories, never from
  `prompts/`**, and name `./tools/regen <character>` instead of the two-command
  list that leaves the short prompts stale. `mercenary-kit/Prompts.md` and
  `tools/prompt-splitter/README.md` had the same omission — the tools README
  said **"Two generators"** and did not mention `short.py` at all, which is the
  generator that writes what you actually paste. `captain-jasu/Prompts.md` was
  already correct, having been written after the lesson.

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
