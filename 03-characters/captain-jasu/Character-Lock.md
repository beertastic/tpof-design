---
title: "Captain Jasu — Character Lock"
asset_id: "LOCK-CAPTAIN-JASU"
updated: "2026-08-04"
status: "locked"
---

# Captain Jasu Character Lock

**Status:** LOCKED FOR BOARD REVIEW — the horns are SETTLED; two deviations in
the approved reference remain and are not in dispute
**Version:** 2.0
**Date:** 2026-08-04

**One approved reference, and it is scoped to the costume only.**

| Reference | Authoritative for | NOT for |
|---|---|---|
| `source/artwork/turn-field-front.png` | **The costume** — cut, silhouette, palette, placement, hardware | **The horns, the mantle surface and the whistle.** See the three deviations below |
| `reference/actor/ling-jiu-headshot.jpg` | **The face and the build**, and nothing else | The costume. There is none in frame |
| `reference/props/a180.jpg` | **The blaster**, and nothing else | Everything else |
| `reference/headdress/horns-authority-2026-08-04.png` | **The bone horns**, and nothing else | The costume. Cropped above the collar so there is none in frame |

**Do not add a second full-figure costume photograph.** Two references competing
over the same garment is the failure that cost Shada five generations. Her three
plates are safe because their scopes do not overlap — a costume, a face, a
weapon.

**The 2026-08-01 front is superseded** and survives only as
`evolution/00-first-approved-2026-08-01.png`. **It must not be attached to
anything.** It carries ankle boots, a whistle at the belt and swept-up hair.

---

## The costume front — APPROVED v2, 2026-08-03

Every other view and every narrative plate matches against this single image. It
settles the three things that four passes moved: **tall boots with a low heel,
exactly one whistle at the throat, and hair worn down and loose.**

**None of those three was ever a design change.** All three were written in
`outfits.yaml` on 2026-08-01 and none of them reached the generator, because they
sat late inside a 2,166-character rule that was being trimmed before it was sent.
The design was right and the pipeline was losing it. The rewrite of nine prose
rules into twenty-six imperative ones on 2026-08-03 took her from ~13% of the
specification reaching the generator to 100%, with nothing removed.
*See [`../../11-production-tracking/Prompt-Reliability-TODO.md`](../../11-production-tracking/Prompt-Reliability-TODO.md).*

**She is the worked example for that fix**, the way Shada is for everything else.

### Known deviations in the approved front

**All three were found on 2026-08-04 by cropping and magnifying the reference
against the plates generated from it.** The horns were settled the same day and
are no longer in dispute; the mantle and the whistle are not disputed either —
the rule wins on both, as it does on Shada's three. **What remains is scheduling
the re-roll, not deciding anything.**

- **THE HORNS — SETTLED 2026-08-04 BY THE PRODUCTION DESIGNER, and the ruling
  went to neither side of the argument.** The spec is now:

  > **Trophies, and bone. Exactly two, one each side, both curved. Alike in
  > curve, colour and size, and officially different objects. Each a third to a
  > half the height of her head.**

  **The old rule overstated the asymmetry.** It asked for *"long and sweeping on
  one side, shorter points on the other"*, and that is not the design — it is a
  much louder object than what is wanted. **`headdress.png` obeyed that rule and
  is therefore now out of spec**, with three horns on its visible side.
  `expression_strip.png` is out too, at 20% and 47% of head height and ridged
  against a rule that says smooth.

  **`portrait.png` is the only plate compliant on every point** — 46% and 53%,
  both curved, alike in character, one blunt-tipped and one pointed. It is now
  the authority, cropped to
  `reference/headdress/horns-authority-2026-08-04.png` so no costume competes.

  **The approved front remains wrong, but for a narrower reason than before.**
  Its horns are the right size and the right character; they are **a true
  mirrored pair** — flipping one produces the other, verified by test — which is
  exactly the printing trap the component note warns about.

- **THE MANTLE SURFACE — the same fault, milder, same cause.** `must_show` rule
  13 asks for *"fine IRREGULAR crazing and cracking… NO quilting, NO lattice, NO
  regular grid."* The approved front carries **a web of long straight crossing
  lines forming rough diamonds**, which is close enough to a lattice that every
  plate generated from it regularises further. `candid.png` reproduced it
  faithfully; `headdress.png` came back frankly diamond-quilted with stitch lines.

  **Rule 13 does not fail because it is trimmed, and it does not only fail at
  close crop** — it fails at full-figure distance too, because it is arguing with
  a photograph. **Only a dedicated paragraph in the slot's own shot text beats
  it**, which is why `mantle_detail.png` and `portrait.png` are the two that came
  back correct. That paragraph now sits in slots 6, 7 and 8.

  **`mantle_detail.png` is the authority on this surface, not the front.**

- **THE WHISTLE — found 2026-08-04 by crop, and it is the third.** `must_show`
  rule 20 asks for a whistle that is *"cheap, plain and much handled… NOT
  ornamental and NOT jewellery"*, and rule 29 permits **exactly two pale or
  bright things, the bone horns and the blaster barrel.**

  **`whistle_and_leash.png` and `mantle_detail.png` both show the correct
  object** — a dull, dark, tarnished tin whistle. **The approved front carries a
  clean bright unmarked silver bar on a cord**, with no tarnish and no handling
  wear, and it reads as a pendant.

  Inherited by `scale_figure`, `hero`, `camp_day`, `expression_strip` and the
  four other turnarounds. **In `expression_strip` there is no blaster in frame,
  so the whistle is the brightest object in the picture** — her most important
  prop rendered as jewellery, which is the precise failure rule 20 exists to
  stop.

  **`whistle_and_leash.png` is the authority on this object, not the front.**

**All three travel together, and one generation fixes all three.**

| Rule the front breaks | Scoped authority to attach instead |
|---|---|
| The horns — a true mirrored pair | `reference/headdress/horns-authority-2026-08-04.png` |
| The mantle — a lattice, not irregular crazing | `mantle_detail.png` |
| The whistle — bright polished jewellery | `whistle_and_leash.png` |

**Twelve of the nineteen images carry at least one of the three.** That is most
of the pack. It does not get cheaper by waiting, and it is stated plainly in
[`../../11-production-tracking/Jasu-Image-TODO.md`](../../11-production-tracking/Jasu-Image-TODO.md)
rather than softened.

---

## Identity

- **Mercenary captain of an eight-person crew.** Human. Female.
- **Twenty-eight years old.** *A departure from the script, which says "CAPTAIN
  JASU (40s), a powerful woman". Cast 2026-08-01 and recorded, not hidden.*
- **155 cm (5 ft 1 in), and almost certainly the smallest adult in the film.**
  Slight and fine-boned. Baylan stands 43 cm above her. Her own animal outweighs
  her.
- **Right-handed.** Blaster on her right hip; leash, pouches and tools on her
  left, off the drawing side.
- Cold rather than angry. Calm, still, watchful, unsentimental — assessing you
  rather than threatening you. She kills a man mid-sentence and smiles.
- She dies confused, charging Baylan after her own animal refuses her.

## The one idea the design exists to carry

**Her authority is borrowed from an animal.** Not rank, not seniority, not
tactical skill, not the crew's respect. She is in charge because she owns a
monster and everyone knows it.

- **She must not look like a natural leader.** No insignia that commands respect,
  no meaningful rank marking, no bearing of authority. Whatever she projects is
  on loan from the beast at her side.
- **The akk dog is the rank. Where she is, it is.**
- **She raised it** — implied, never stated. The affection in Scene 9 is genuine,
  and the reminder to everyone watching is a by-product. It is what makes the
  finale worse rather than better: she spends something she loves.
- **At 155 cm there is now nothing else her authority could be.** The recast made
  the central idea airtight rather than weakening it.

**An image that makes her physically formidable has destroyed the only idea in
the design.** This is the reason for most of the rejections at the foot of this
document.

## What her share looks like, and why it is never rank

She probably takes the largest cut, so she may be the best-equipped of them.
**Money without authority is a specific and useful look**, and it shows in
exactly three places, none of which is an insignia:

1. **The clothes are made to measure.** In a crew wearing dead men's kit, hers is
   the only outfit in the film that was cut for a person. At 155 cm nothing could
   have been scavenged to fit her anyway, and a garment fitted this close cannot
   read as anything else.
2. **The blaster is modular.** An A180 is a compact pistol built to be
   reconfigured, and a modular weapon is an expensive weapon.
3. **The blaster is clean.** It is the only maintained object in this crew.

## Physical Design

- **Species: human.** The akk dog is the only non-human thing beside her, and
  nothing about her body may compete with it for attention.
- **Build: small and slight**, fine-boned. Never muscular, never broad. Nothing
  about her body may suggest she could win a fight or hold a room by force.
- **Her head is in normal adult proportion to her body.** Never oversized, never a
  caricature. *The Funko headdress references were detached on 2026-08-03: a 1:1
  head-to-body ratio is exactly how a 155 cm woman turns into a caricature.*
- **Long dark hair, worn DOWN and LOOSE** — over the shoulders and down the back,
  swept off the face, field-worn and slightly dishevelled. **Corrected 2026-08-03
  from a superseded swept-up specification.** Never piled up, never a bun, never a
  half-up knot, never scraped back, never styled.
- **The face comes from the actor photograph and the body from this document.**
  A young East Asian woman.
- **No make-up that reads as make-up, no glamour, no styling.** She is not
  presented as attractive; she is presented as a person doing a job.

## Costume

Full specification in [`outfits.yaml`](outfits.yaml); the build list is the
production's first `components:` block and the model for every other character.
*See [`../../11-production-tracking/Costume-Build-Method.md`](../../11-production-tracking/Costume-Build-Method.md).*

**The silhouette is five things**, and it is the shape of authority bought by
somebody who has none of the real thing: **a high closed collar, a hard square
shoulder, a hard-cinched waist, a second-skin body, and tall boots.**

- **THE SHOULDER MANTLE IS THE SIGNATURE.** A stiff yoke of **stiffened cloth**
  over both shoulders, standing proud of the body, reaching past the shoulder
  points before angling down over the upper arm, coming to a **sharp upswept
  point at each shoulder**, and rising at the back into the stand collar. **It is
  the only thing on her wider than she is.**
  - **It holds its shape by construction** — ribbed, quilted or pleated cloth.
    **NOT leather, NOT printed, NOT a bought pauldron.** *A sourcing guide written
    from photographs alone recommended an Etsy leather pauldron; that is the
    single most wrong thing it is possible to buy for this costume.*
  - **Surface: WEAR, never DECORATION.** Fine irregular crazing and cracking,
    heavier where it flexes and rubs, never the same twice. **Looked after, not
    derelict** — no splits, no holes, no rot. The best-kept item in a crew wearing
    salvage, and it still shows a hard few years. See the deviation above.
- **THE BODY IS TEXTILE, NOT LEATHER.** Heavy ribbed knit, quilted panels, dense
  woven canvas — matte and dry. Leather is confined to the belt, the boots, the
  bracers and the holster. **If the costume reads as a leather bodysuit, it is
  wrong.**
- **SKIN-TIGHT FROM COLLAR TO ANKLE — a second skin**, with no bulk over the
  ribs, waist, hips or limbs. No flare, no swing, no volume, no gathered or draped
  fabric anywhere. **Cut for a gymnast, not a soldier** — she is the smallest
  adult in the film and has to keep up with people twice her size, and the costume
  must say so at a glance.
- **THE COLLAR is stiff and stands, closed to the throat.** Never open, never a
  lapel, never a shawl, never a cowl.
- **THE WAIST is pulled in hard by a wide heavy belt** over the second skin. The
  cinch is what makes the silhouette read.
- **BELOW THE WAIST: skin-tight trousers** with quilted outer-thigh panels
  stitched **flat** to the leg, and knee pads. **NOTHING hangs from the belt and
  nothing swings.**
- **THE BOOTS are tall and close to the calf** — the shaft rises well up the calf
  and ends below the knee. **Settled by a generated A/B on 2026-08-03**; the tall
  boot was obviously right on sight and Variant B was never generated. **The heel
  is flat or as near flat as the boot allows** — no more than about 25 mm, never a
  block heel, and never anything that adds height to her.
- **THE BRACERS are forearm only** — wrist to below the elbow, buckled, dark.
  Never continuing up the upper arm.
- **IT IS CUT TO HER AND ONLY TO HER.** Never oversized, never borrowed, never a
  child in adult clothes.
- **The cloth is expensive and it is filthy. The quality is in the cut, never in
  the condition.** Faded across the shoulders, mended at cuff and hem, mud to the
  knee, collar worn shiny.

### Palette

**Muted and dark** — deep brown, dark umber, faded charcoal, oiled hide, the dull
warm grey of old canvas. The bracers, leg panels, knee pads, mantle and boots are
**all dark warm brown**, never bone, cream, ivory or pale.

**TWO PALE OR BRIGHT THINGS AND ONLY TWO: the bone horns and the blaster barrel.**
Nothing else on her is pale and nothing else is bright, and the barrel is never
dulled down to match her.

## The headdress

**Pale curved bone horns set into long dark hair worn down and loose**, projecting
up and outward from both sides, sitting above and behind the ears.

- **They are trophies from what the animal kills.** Worn, matte, yellowed with
  age, tapering to points. **Never polished, never carved, never set in metal.
  A trophy, not jewellery.**
- **EXACTLY TWO, ONE EACH SIDE, each a third to a half the height of her head.**
  Never three, never a cluster, never a row of points.
- **ALIKE IN CURVE, COLOUR AND SIZE, AND NOT THE SAME OBJECT.** Both curve; one
  is blunter and one comes to a point; one runs slightly the longer. **A pair of
  trophies, not a mirrored pair.** *This is a printing trap as much as a drawing
  one — a printer produces a perfect matched pair by default, so they must be
  printed as two separate models. Recorded in `Costume-Build-Method.md`.*
- **Smooth** — never ridged, never banded, never segmented like a ram's horn.
- **Pale against very dark hair, and that contrast is the whole effect.**
- **Nothing covers her face or her brow.** Not a helmet, not a crown, not a
  circlet, not a metal band, not a mask, not a visor.

> **`Character.md` still advertises a "Brow band" in its summary table at line
> 306** — *"low, ornate, asymmetric, a small worn crest to one side… the only
> decorative object on her."* **The band was removed on 2026-08-01**, which the
> same document states at line 481 and treats as moot at line 614. There is no
> component for it, and no approved image shows one. **The table row is stale and
> should be deleted.** Flagged 2026-08-04 while writing this lock.

## Equipment and hero props

- **THE WHISTLE — the cheapest hero prop in the film and the most important
  object she owns.** Small, worn, cheap, much handled, on a cord **at her
  throat, plainly visible**. **It is her entire command structure**: she whistles
  and the beast comes, she whistles and it kills. It is worth nothing to anybody
  else.
  - **THERE IS EXACTLY ONE, AND IT IS AT HER THROAT.** Nothing resembling a
    whistle hangs from her belt. *A generated test on 2026-08-03 came back wearing
    two; two makes it an ornament instead of an instrument.*
  - **DULL, DARK AND TARNISHED, NEVER BRIGHT.** `whistle_and_leash.png` is the
    authority. **The approved front shows a clean bright silver bar that reads as
    a pendant** — see the deviation above. A bright whistle is also a third pale
    object, which rule 29 forbids outright.
  - *A sourcing guide written from the photographs called it a "vintage keychain
    fob".*
- **THE LEASH.** Heavy chain or thick strap, **coiled and hung at her belt on her
  LEFT**, off the drawing side. **She is never holding it and the animal is never
  on it.** Carrying restraint she does not need is a display for the crew — the
  difference between commanding an animal and controlling a weapon. Something to
  physically drop in the finale.
  - **The single exception is `candid.png`**, where she is alone and maintaining
    her own kit. The animal is still not on it.
- **THE A180 BLASTER PISTOL** — *the weapon Jyn Erso carries in Rogue One.*
  Belt-mounted on her **RIGHT hip**, grip up and angled forward for a right-hand
  draw. **She is right-handed and it is never on her left.**
  - **Two-tone: bright polished steel forward, black at the back.** A Luger-pattern
    build with a long bare barrel, **six round vent holes** near the muzzle, fine
    fluting part way back, a stepped muzzle, a black receiver with bright polished
    plates, a **mounting rail** with a knurled knob at the rear, and a black
    chequered grip raked steeply back.
  - **It is clean, serviced and cared for — the only maintained object in this
    crew — and it must stay bright.** Not a generic sidearm, not a revolver, not a
    scratch-built mismatch, not an antique, not ornate, not dark all over.
  - **Recognition risk, stated not hidden:** an audience may read it as Jyn's. An
    in-universe non-issue — BlasTech sells them, and at ~1 BBY it is
    contemporaneous rather than anachronistic — but it sits in the same class as
    the Imperial and samurai reads blocked below.
  - **The reference at `reference/props/a180.jpg` is third-party. Replace it with
    a photograph of our build when the prop is made**, per the rule Shada's
    WESTAR-35 established. **Verify the designation with the armourer** before it
    is engraved anywhere.

## The akk dog

It is not her costume, but it is her rank, so it is locked here too. Full spec in
[`../../08-species/akk-dog/Creature.md`](../../08-species/akk-dog/Creature.md).

- **0.85 m at the shoulder crest — level with the bottom of her belt**, measured
  off the rig. Her resting hand hangs naturally onto it: she does not reach down
  and she does not reach up. **It outweighs her.**
- **A low-slung reptile** — pebbled and plated scale, a spiked dorsal crest, brow
  horns, hide damp and darker where wet, mud up the forelegs, feet *in* the
  ground rather than on it.
- **It is never on a lead**, never harnessed, and nothing runs from her hand to
  it.

> **Two failures on the record, and both were caused by the same omission — the
> slot never said what an akk is and no creature plate was attached.**
> `captaining.png` drew a **generic canid in a harness**, and the size came back
> at **roughly half** twice more before the landmark was promoted out of a
> ~90-word paragraph to the head of its block. **`camp_day.png` got it right by
> luck**, seven minutes earlier. **Any slot containing the animal needs the
> creature plates attached and the size stated early.**

## Design Drift Prevention

**Reject any design that becomes:**

### The three retrievals — these are the whole reason this list exists

- **An Imperial officer.** No flat grey-green uniform, no tunic with a rank
  plaque, no code cylinders at the shoulder, no peaked military cap, no jodhpurs,
  no gleaming jackboots, no insignia of any kind. **She commands eight people and
  a dog. There is no empire behind her and nothing she wears may imply one.**
- **A samurai, and not a Jedi.** No lacquered lamellar plate, no laced armour
  panels, no wide flaring shoulder guards, no horned or winged helmet, no face
  mask, no mempo, no topknot, no robes, no sash-wrapped front, no sword. **The man
  standing beside her in the finale is a Jedi hiding as a mercenary, and his
  entire design depends on nobody in frame reading as one.**
- **Physically imposing.** The word *captain* pulls toward someone tall, broad,
  older and weathered. **Refuse it.** Never taller, never broader, never harder-
  looking to justify the rank. She is obeyed because of the beast at her side and
  for no other reason.

*A high collar plus a hard shoulder plus a crest at the brow sits very close to
two costumes an image model knows extremely well, and both are wrong for opposite
reasons. **What is true instead:** she has bought the shape of authority because
she has none of the real thing.*

### The headdress

- **A MIRRORED PAIR of horns** — two castings of one object. They are alike in
  curve, colour and size and they are **not the same object**: one blunter, one
  pointed, one slightly the longer. *The approved front is a true mirrored pair,
  verified by flipping one onto the other.*
- **Three or more horns, a cluster, or a row of points.** Exactly two, one each
  side. *`headdress.png` has three on its visible side, because it obeyed the
  superseded rule.*
- **Horns outside a third to a half of her head height**, either way.
- **Ridged, banded or segmented horns** like a ram's. They are smooth.
- **Polished, carved, jewelled or metal-set horns.** A worked finish turns them
  into jewellery and collapses the reading.
- **A helmet, crown, circlet, metal band, mask or visor**, or anything covering
  her face or brow.
- **A brow band.** Removed 2026-08-01. If one appears, it is the stale
  `Character.md` table row being read.
- **Hair piled up, in a bun, in a half-up knot, gathered at the crown, scraped
  back tight, or styled.** *Superseded on 2026-08-03, and a slot that still
  carried the old wording duly produced a half-up knot on 2026-08-04.*

### The costume

- **A skirt, tabard, apron, overskirt, coat tail or any hanging panel over the
  trousers.** Nothing hangs from the belt and nothing swings. *The "long skirted
  coat" of the officer reference does not transfer, and the narrow split panels
  that used to be specified were deleted on 2026-08-03 — they existed only in
  `must_show`, had no component, and no image ever showed one. **A skirt over the
  trousers is the exact fault that cost Shada her fifth generation.***
- **Ankle boots, low boots, pale boots or ornamented boots.**
- **A block, shaped or raised heel**, or anything that adds height to her. *The
  component note said "flat" from 2026-08-01 and a build note cannot reach a
  generator; there is now a heel rule. The heel runs slightly high in
  `turn-field-natural.png` — within tolerance, but check it in every frame.*
- **A second whistle, or a whistle at the belt.**
- **A bright, clean, polished or unmarked whistle**, or one that reads as a
  pendant. It is cheap tin, tarnished and much handled. *Currently shown bright
  by the approved front and by five plates matched against it.*
- **The leash in her hand or clipped to the animal.** *`candid.png` is the single
  exception.*
- **A mantle with quilting, lattice, regular cross-hatch, triangular grid,
  tooling, embossing or any repeating texture.** *See the open deviation.*
- **A leather mantle, a printed mantle, or a bought pauldron.** It is stiffened
  cloth holding its shape by construction.
- **A leather bodysuit.** The body is textile.
- **A pauldron, a spiked guard, a winged shape, a cape or a fur collar** in place
  of the mantle.
- **Bulky, loose, oversized or borrowed.** It was cut to her.
- **Fine modern coil zips, neat garment zips or a visible zip of any kind.** The
  closure is concealed.
- **Glamour posing, sexualisation or fashion-editorial lighting.** Close-fitting
  for movement, not for display.

### The rank

- **Any insignia, rank badge, faction mark, medal or braid.** **The animal is the
  rank.**
- **Any faction colour** — no imperial grey, no uniform green, no red, no gold
  braid. *Rank is one of the few sanctioned uses of bright colour in the Bible,
  which is why the rank question below is a palette decision as much as a costume
  one.*
- **A dulled or dark-all-over blaster.** It is the only gleaming object in this
  crew and the palette rule protects it.

### The animal

- **A dog.** Not a canid, not a wolf, not a mastiff — and the akk is **larger**
  than any of them, not merely a different shape. *The three negations were
  themselves pushing the size down: a mastiff is a ~76 cm dog.*
- **An akk at knee height.** The crest is level with the bottom of her belt.
- **A harnessed or leashed animal.**

### General

- **Any part of another character's costume.** *Recorded from the other
  direction on 2026-08-02, when a Shada generation returned Jasu's costume — bone
  horns, a full-width yoke, quilted sleeves and matched bracers — because the two
  sets were generated in the same conversation. **Fresh chat per character.***
- **Too dark to read.** She must separate from a night forest and from firelight;
  do not sink her into the background. *`akk_together.png` runs close to this
  line — its slot specifies no light, and it is a scale plate rather than a
  costume authority.*
- **An empty holster, or a costume record with the weapons absent.**

---

## Open, and it is the highest-leverage item in the production

- [ ] **DOES SHE CARRY A RANK MARKING, AND WHAT IS IT?** Rank is one of the few
      sanctioned uses of bright colour in the Bible, so this is a palette decision
      as much as a costume one — and it sits directly against *"no meaningful rank
      marking"* above.

      **Her design sets the rank language for the entire mercenary faction.** Nyx,
      Yaslo Bis, Reya Fenn and the four-person Mercenary Kit all inherit their
      answer from hers. **Settling it after they are designed means redoing them;
      settling it now costs one decision.** Nyx is already flagged PRIORITY in
      `Production-Status.md`.

- [ ] **THE HORNS.** See the deviation at the top of this document. **Must be
      settled before the boards are built.**

- [ ] **What is her share, and how visibly does she wear it?** Partly answered by
      the three places above — tailoring, modularity, maintenance — but not
      closed.

- [ ] **Does anything on the animal predate her?** Older tack, a mark, a scar she
      did not cause. She raised it, implied and unstated.

---

## See also

- [`Character.md`](Character.md) — cast, backstory, and the departure from the script
- [`outfits.yaml`](outfits.yaml) — the full specification, the 29 `must_show` rules and the `components:` build list
- [`../APPROVAL.md`](../APPROVAL.md) — how a reference is approved and re-approved
- [`../../11-production-tracking/Jasu-Image-TODO.md`](../../11-production-tracking/Jasu-Image-TODO.md) — the finish list and the open horn decision
- [`../../11-production-tracking/Prompt-Reliability-TODO.md`](../../11-production-tracking/Prompt-Reliability-TODO.md) — why specification does not reach the generator
- [`../../11-production-tracking/Costume-Build-Method.md`](../../11-production-tracking/Costume-Build-Method.md) — her `components:` block is the model
- [`../shada/Character-Lock.md`](../shada/Character-Lock.md) — the format this follows
