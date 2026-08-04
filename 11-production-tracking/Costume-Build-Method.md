---
title: "Costume Build Method"
asset_id: "TRACK-BUILD-METHOD"
updated: "2026-08-02"
status: "reference"
---

# Costume Build Method

**Fabric is bought. Hard parts are printed.**

Every costume in this production splits into three build routes, and knowing
which route a component takes changes how it should be designed. This document
records the policy and the design consequences that follow from it.

| Route | What goes this way |
|---|---|
| **Bought** | All fabric and leather: garments, coats, trousers, boots, webbing, straps, wraps — including Shada's vest, cloth since 2026-08-02 |
| **Printed** | Weapons, buckles and fittings, armour plate, helmets, Shada's scales, prop hardware |
| **Made** | Assembly, distressing, paint and patina, lacing printed parts onto bought backing |

The third route is where most of the labour actually sits, and it is the one
easiest to forget when estimating.

**We have a 3D printing studio on the team** — confirmed 2026-08-01. All armour,
weapons, scales, knives and prop hardware are built in house, which is why the
printed route is the default for anything hard rather than a last resort. It also
means the constraints below are OURS to manage rather than a supplier's, and the
"printed parts come out identical" problem is a paint-shop scheduling decision we
control.

It changes sourcing advice in one specific way worth stating: **do not buy
cosplay armour.** Any guide written without knowing about the studio will
recommend Etsy pauldrons, bought bracers and AliExpress arm guards, and those are
both worse and slower than printing them. What still gets bought is cloth,
leather goods and boots.

---

## What 3D printing changes about the design

Printing is not a neutral substitute for fabrication. It is good at some things
and bad at others, and several design rules already written into this production
depend on which.

### Printed parts come out identical. Mismatch has to be painted on.

**This is the single most important consequence, and it lands hardest on Shada.**

Her whole costume rests on **five pieces of scale in five different metals** —
dull grey steel on the right forearm gauntlet, blackened iron on the left
shoulder cap, dark bronze on the left thigh, pale worn pewter on her right flank
panel and rust-red oxidised iron on her left. That mismatch is the proof nobody
made the costume for her. Identical pieces quietly recreate the matched-set
problem in five places instead of one.

**The two flank panels are the acute case for matching**, because they are a
left-and-right pair in the same place on the body. If those two come off the
same print run and get the same finish, the costume reads as a cuirass somebody
fitted to her.

**The gauntlet is the acute case now**, because from 2026-08-01 it is the one
piece printed as a solid shell rather than assembled from separate plates. It
comes off the printer as a finished object, which means every scrap of its
salvaged history is paint. A clean print reads as a manufactured tech panel, and
that is the failure mode the whole scale specification exists to prevent.

A printer will produce all five in the same filament. **The difference between
those metals is now entirely a paint and patina job**, not a material one,
and it has to be scheduled and costed as such. If the five pieces come off the
same print run and get the same finish pass, the design fails and it fails
invisibly — it will look fine in isolation and wrong in the turnaround.

The same applies to the mercenaries' plating, which is specified as *mismatched
alloys sitting side by side, oxidising at different rates*.

**And to Captain Jasu's horns, which is the sharpest case of all.** They are two
bone trophies taken off two different kills, and the design says so explicitly:
*long and sweeping on one side, shorter points on the other.* **A printer
produces a perfect matched pair by default.** A matched pair is a manufactured
ornament — jewellery — and the whole reading of that headdress is that it is
*taken*, not made. Print them as two different objects, or print one twice and
cut the second down. Finish them matte and yellowed, never polished and never
carved.

### Two kinds of sameness — get them the right way round

**Updated 2026-07-31, from the first physical scale samples.**

Shada's plates are **hexagonal and carry a repeating serpent relief**. Both of
those are deliberately uniform, and that uniformity is doing useful work: it is
what proves the material was stamped out in a mill for something else. The
serpent is a manufacturer's mark on cheap Outer Rim hull plate, not a motif
anyone chose for her.

So the rule for the paint shop is precise:

| Must repeat | Must never repeat |
|---|---|
| The hexagonal shape — **one master, identical everywhere** | The material |
| The serpent motif — **three or four variants, in rotation** | The finish, age and state of wear |
| | **How far each serpent has worn down** |

**Bounded to three or four serpents, 2026-08-03.** The row above read *"the exact
form of the serpent — must never repeat"* until then, and `Character.md` said "no
two are identical". That is unbuildable as a printed part: at ~440 plates it means
sculpting 440 faces, or printing one master and then hand-finishing every plate —
which lands squarely on the largest hidden labour item in this costume and
doubles it. **Three or four STLs in rotation reads the same at arm's length.**
The story survives intact, because three scavenging trips is three or four mills,
batches and worn dies — and never four hundred. What differs between neighbouring
plates is now the wear, not the mark.

**Regular shape, irregular material.** Three or four print files are correct and
expected; one finish across all five pieces is not. They came off five different
scavenging trips and must read as five different metals — dull grey steel on
the right forearm gauntlet, blackened iron on the left shoulder cap, dark bronze
on the left thigh, pale worn pewter on her right flank panel, rust-red oxidised
iron on her left. **No brass and no verdigris**, dropped 2026-08-01.

**And one finish per piece, not one finish per plate.** A panel speckled with
four alloys is decorative mottling: one panel is one piece of salvage from one
trip. The variation belongs between the five pieces, never inside one.

**The serpent is raised, not incised**, so it wears from the top down — the ridge
goes flat and pale where the plate has been handled, and nearly disappears on the
oldest patch. If it comes out crisp and identical on every plate it reads as
jewellery, and the costume says somebody made it for her.

**Three or four serpents, and the paint shop supplies the rest.** *This read "no
two serpents should be identical" until 2026-08-03 — see the bound above.* One
die used once would produce a matched set, and the story is four scavenging
trips, so a single serpent across the whole costume is wrong. Three or four
carries that. Beyond four, the difference stops being visible at any distance a
camera will see and becomes labour spent on nothing.

**Two neighbouring plates carrying the same mark is correct**, and it is the
finishing that must stop them reading as a matched pair: one worn flatter, one
chipped, one with the paint gone off the ridge.

**One piece may be hardened hide rather than metal**, cut to the same hexagon.
Leather plates carry the serpent faintly or not at all — a mill mark belongs in
metal, and its absence is evidence of where that plate came from.

### The vest is bought cloth, not hide — changed 2026-08-02

Shada's vest was specified as scavenged hide until the design locked. **It is now
a heavy close-woven cloth in a dusty grey**, which moves it firmly into the
*bought* route and simplifies it: a garment to source and distress rather than a
hide to find. The palette moved with it — grey, grey-green and khaki throughout,
**all leather in grey-brown taupe**, with the bronze thigh patch the one warm
thing in the costume.

Two consequences for the build:

- **The serpentine grain is now a weave, not a pressing.** It has to be found in
  the cloth at purchase or it does not exist — there is no equivalent of
  embossing a hide. Look for a fine, close, irregular texture woven in, tonal and
  readable only in raking light. **Not a reptile print**, which is the thing the
  market will offer.
- **Taupe leather is a dyeing and distressing job.** Belts, holster, thigh strap,
  boots and the gauntlet cuff all read warm brown as bought. The costume drifts
  back toward brown on almost every image, and it will do the same on the bench.

### Plates are missing on purpose — recorded 2026-08-02

**Five to ten plates are absent from each flank panel and three to five from the
shoulder cap**, leaving the hand-cut backing showing through. Bent corners,
cracked plates, rows out of line, an eyelet re-punched beside a torn one, a
different cord spliced into the lacing.

This is a **finishing instruction, not a licence to make fewer plates.** The gaps
have to fall along the edges, at the waist and over the hip — the places that
catch and flex — which means the panel is patterned and laced complete and then
plates are removed, or specific positions are left empty by design. Scattered
absence reads as wear; regular absence reads as a pattern.

It takes roughly 15 plates off the ~440 count, which is noise. **The labour is
unchanged**, and the backing behind the gaps now has to be worth looking at.

### Printed scale must not fight the backing

Shada's scale armour has to **move like heavy cloth, not like plate** — that is
the entire reason she wears it, and it is what stops it reading as fantasy
armour.

**Revised 2026-07-31: the plates tessellate, they do not overlap.** They sit edge
to edge with a narrow visible gap between neighbours, so **all of the
flex now lives in those gaps and in the lacing.** An overlapped panel can be
stiff and still drape, because the plates slide over each other. A tessellated
one cannot — if the gaps close up or the lacing is tight, the panel becomes a
sheet of armour and the design is lost.

Two things follow for the build:

- **The gap is a functional dimension, not a cosmetic one.** It has to be big
  enough to let the panel curve around a forearm and a shoulder. Worth
  prototyping one patch before committing to a print run.
- **Printing plates in pre-linked sheets defeats the point.** Individual plates
  laced to the backing is what flexes.

### The plate count is the hidden cost

**Plate size confirmed 2026-07-31: 10 to 15 mm across. Re-confirmed 2026-08-01**
against a generation that came back three to four times too coarse.

The size had never reached the generator — it sat inside the placement rule in
`outfits.yaml` and the short prompts trimmed it away, so every image invented its
own plate size. It is now its own non-negotiable. **If a new image shows plates
you can count at a glance, the plates are wrong, not the figure**, and the ~440
count below stands.

That is much finer than it sounds, and it multiplies. A hexagon 12.5 mm across
covers roughly 1.35 cm², so a rough estimate from patch area:

| Patch | Approx. area | Loose plates |
|---|---|---|
| Flank panel — her right | ~150 cm² | ~110 |
| Flank panel — her left | ~150 cm² | ~110 |
| Shoulder cap — her left | ~120 cm² | ~90 |
| Thigh — her left | ~180 cm² | ~130 |
| Gauntlet — her right forearm | ~200 cm² | **0 — printed as one shell** |
| | | **~440** |

*Revised 2026-07-31: the sternum patch was dropped, taking about 75 plates with
it.*

**Revised three times on 2026-08-01, and it has landed back at ~440.** The
morning made the gauntlet plain leather and added the flank panels (~440). The
second change dropped the panels and printed the gauntlet (~220). The third
restored the panels while keeping the printed gauntlet — so **~440 again, but
with the gauntlet's ~150 hand-laced plates permanently gone.**

**Printing the gauntlet is still worth ~150 plates**, each of which would have
needed two punched holes and hand lacing. Nothing else in this build offers a
saving of that size, and it survives every revision because it is a property of
the piece, not of the coverage.

**Pattern the flank panels first.** They are now half the plate count in the
costume and their area depends on a pattern nobody has cut yet, so they are both
the biggest number here and the least certain one.

*Estimated from assumed patch dimensions — confirm against the real patterns
before committing to a print run.*

**Getting on for four hundred and fifty plates, each needing two holes and hand
lacing.** Still the largest single labour item in this costume, and still easy to
miss, because each plate is trivial on its own.

**The flank panels also add work the other pieces never had:** punched eyelets
down both facing edges, a leather thong long enough to lace the full height, and
two strap-and-buckle fixings at the back. The lacing is visible and structural,
so it cannot be faked with a hidden fastening.

Three consequences:

- **The pressure to print pre-linked sheets will be enormous**, and it is exactly
  the shortcut that kills the flex. **On the shoulder cap and the thigh patch
  this is forbidden** — and on the flank panels too. All four must move like
  heavy cloth; the shoulder cap has to hang loose and swing, and the panels sit
  over her ribs, where she breathes. If assembly time is the problem, reduce
  the patch areas rather than linking the plates.
- **The raised swirl is now a 12 mm detail.** It has to survive at print
  resolution and it will need a wash or dry-brush to read at all — the relief
  alone will not carry it at that size. **On the printed gauntlet this is the
  whole job**, since nothing else distinguishes it from a moulded tech panel.
- **Print and finish a full patch before committing.** Several hundred plates is not
  something to discover a problem in halfway through.

### Load-bearing buckles should be real hardware

Printed buckles fail at the layer lines, and they fail under exactly the loads a
costume puts on them.

**Anything actually carrying weight should be bought hardware:** harness
buckles, drop-leg holster straps, belt closures, the Wookiee's bandolier
fittings. Printing is for buckles that are seen but not loaded.

This does not compromise the look. The Design Bible already calls for industrial
salvage over fine modern hardware, and real load-rated buckles read more
correctly than printed ones anyway.

### One printed weapon can serve two characters

The Wookiee's primary weapon is specified as **a human-sized blaster rifle worn
on his hip like a pistol** — the scale is what sells it. That is the same class
of weapon the `merc-2` build carries in two hands.

**One printed rifle model, two uses.** The saving was a design decision before it
was a production one, and it should survive into the build.

---

## The grenade is a stunt prop, not a dress prop

**Flagging this early because it is the one printed item with a physical
performance requirement.**

Vala pulls a grenade off the Wookiee's bandolier while he is crushing her. The
design already specifies open cradles rather than closed pouches, seated on the
front of the strap at mid-chest height, reachable in one movement by somebody who
is not wearing it.

What that means for the build:

- **A printed grenade is brittle at the layer lines.** The hero version can be
  printed; the one that gets pulled in a take should be cast in something soft,
  or printed in a flexible filament.
- **The mounting has to release predictably.** It cannot be so secure that it
  needs a real yank, and it cannot be so loose that it falls off between setups.
- **Multiples are needed.** Several takes, and a stunt performer inside a full
  Wookiee suit who cannot easily reset it themselves.
- It must also be **recognisable in Scene 10**, ten scenes earlier, which means
  the hero and stunt versions have to match on camera.

---

## Where sourcing links live — **decided 2026-08-01**

**Supplier links, prices and stock live in the production's Drive. They do not
live in this repository.**

They rot. A shop closes, a listing sells, a price doubles — and a repository full
of dead links is worse than none, because somebody trusts it. It is the same rule
as [`10-assets/study/`](../10-assets/study/): *write down the derived decision,
never the perishable source.*

**What is durable goes into `components:` in the character's `outfits.yaml`** —
the material, the construction, the quantity, the build route, and the things it
must not be. That keeps it beside the specification it came from, so the two
cannot silently disagree. Captain Jasu is the first character to carry one.

**A worked example of why this matters.** A sourcing guide for Jasu was generated
from her turnaround photographs alone, without the repository. It was competent,
and four of its recommendations contradicted locked decisions: a **leather
pauldron** for a mantle specified as stiffened cloth; **carved Viking hair rings**
for horns specified as unworked trophies; **a cardboard tube in leather-look
fabric** for the one weapon she keeps clean and serviced; and secondhand
petite-sizing advice for the only **made-to-measure** costume in the film. It also
demoted the whistle — her entire command structure — to a "vintage keychain fob",
and omitted the leash.

None of that was unreasonable from five photographs. It is only wrong if you know
the mantle is cloth, and a photograph cannot tell you that. **Sourcing written
away from the specification will always drift toward what the pictures look like
rather than what the design says**, and the fix is to keep the durable half here.

Its genuinely good idea has been kept: **equestrian jodhpurs and breeches** for
trousers with contrast knee patches, and searching by *construction* — ribbed,
quilted, mock-neck — rather than by the look.

---

## The checklist — BUILT 2026-08-04

**Requirement, recorded 2026-07-31.** A per-character checklist of every costume
item, showing build route and progress, so the state of the build can be checked
at a glance.

**Built on 2026-08-04 as `tools/build-lists`, and it went further than a
checklist.** The `components:` schema sketched below is now real on Captain Jasu
and Shada, so the generator this section was waiting for exists:

    ./tools/build-lists shada          # or --all

It writes two sheets per character and renders both to PDF through the same
renderer as the build guide, so they publish to Drive with everything else:

| Sheet | Covers | For |
|---|---|---|
| `_print_list.pdf` | `route: printed` and `route: made` | the bench — approximate sizes, colour swatches, finish and method |
| `_shopping_list.pdf` | `route: bought` | the shop — search terms, filters, what to refuse, target price |

**Both sheets carry pictures, added 2026-08-04**, so a printed shopping list is
enough on its own in a charity shop. *"Heavy ribbed knit, dark warm brown"* is
unambiguous at a desk and useless on a rail, where the job is to recognise the
thing in three seconds. Each component names its plates in `images:`, with an
optional `crop:` in fractions of the frame, and the generator cuts and places
them. **Nothing new is drawn** — every picture is a crop of a plate already in
the repository, which is why the crops are not committed.

**A figure may carry a `scope:`, and it prints in red under the picture.** This
matters more than it looks. Several plates here are authoritative for one thing
and actively wrong about others: the A180 image is third-party, Shada's WESTAR is
**deliberately not locked** because the prop has never been photographed, the
horn authority is right above the collar and nothing below it, and her make-up
plate has no costume in frame at all. **A picture with no caveat teaches
everything in it equally** — that is exactly how a department ends up building
from a superseded image, which is the failure `do-not-publish.txt` and the
`references:` lock both exist to prevent. Where the repository records a scope,
the sheet prints it.

**Two sheets and not three, because three routes are two days of work** — a day
at the bench and a day shopping. `printed` and `made` share a sheet but never a
section: printing a piece that must move like cloth is the failure this document
keeps writing warnings about, and the sheet repeats them.

**Every component lands on exactly one sheet, and the generator fails loudly on
a route it does not recognise.** A component silently missing from both lists is
precisely the bug these sheets exist to prevent.

**The colour swatches are brand-agnostic on purpose** — a name and a hex chip,
never a Vallejo or Citadel code. Paint ranges are reformulated and discontinued;
"pale worn pewter" is not. It is the same rule as the sourcing links below.

**The budget is a cap on bought items only.** Filament, paint, leather, dye and
Shada's contact lens are materials, tracked separately — shopping well does not
control them. Against a £100 cap: **Jasu £36–87, Shada £35–83.**

**Still open.** `status:` is carried through to the sheets but nothing updates
it yet, so progress is still read off the page rather than off the repository.
Baylan, Shin and the mercenary kit have `outfits.yaml` files with no
`components:` block; the generator skips them and says so.

What the requirement originally asked for, kept for the record:

**It should be generated, not hand-maintained.** Everything else in this repo is
generated from a source of truth and this should be no different — a hand-kept
checklist will drift from `outfits.yaml` within a fortnight, and then the
checklist is worse than nothing because it is trusted and wrong.

The gap is that `outfits.yaml` currently describes costumes in prose and rules,
not as itemised components. It would need a structured block per outfit:

```yaml
components:
  - item: Gauntlet, right forearm — solid printed shell
    route: printed
    qty: 1
    status: not-started      # not-started | in-progress | done
    note: >-
      Dull grey steel finish, a cluster of dim amber telltales at the wrist.
      Must NOT match the other four pieces
  - item: Work vest
    route: bought
    qty: 1
    status: sourced
  - item: Harness buckles
    route: bought
    qty: 6
    note: Load-bearing. Not printed
```

From that, a generator produces a per-character build sheet and a
production-wide roll-up — bought versus printed versus made, and how much of each
is done. It would also close the **prop reference gap** recorded in
[`Shada-Image-TODO.md`](Shada-Image-TODO.md), since a component list is most of
what a prop lock needs.

*The per-character sheets are done. The production-wide roll-up is not — the
generator reports per character and there is no combined view yet.*

---

## See also

- [`Shada-Image-TODO.md`](Shada-Image-TODO.md) — the prop reference lock
- [`../01-production-design/Production-Design-Bible-v1.0.md`](../01-production-design/Production-Design-Bible-v1.0.md) — sections 5 and 6, materials and weapons
- [`../03-characters/shada/Character.md`](../03-characters/shada/Character.md) — the four-metals rule this document is mostly about
