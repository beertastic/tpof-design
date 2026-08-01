---
title: "Costume Build Method"
asset_id: "TRACK-BUILD-METHOD"
updated: "2026-08-01"
status: "reference"
---

# Costume Build Method

**Fabric is bought. Hard parts are printed.**

Every costume in this production splits into three build routes, and knowing
which route a component takes changes how it should be designed. This document
records the policy and the design consequences that follow from it.

| Route | What goes this way |
|---|---|
| **Bought** | All fabric and leather: garments, coats, trousers, boots, webbing, straps, wraps |
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

Her whole costume rests on **four pieces of scale in four different metals** —
dull grey steel on her right flank, blackened iron on her left, brass with
verdigris on the shoulder, dark bronze on the thigh. That mismatch is the proof
nobody made the costume for her. Identical pieces quietly recreate the
matched-set problem in four places instead of one.

**The two flank panels are the acute case**, because they are a left-and-right
pair in the same place on the body. If those two match, the costume reads as a
cuirass somebody fitted to her, and the whole scavenger argument collapses.

A printer will produce all four in the same filament. **The difference between
those metals is now entirely a paint and patina job**, not a material one,
and it has to be scheduled and costed as such. If the four pieces come off the
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
| The hexagonal shape | The material |
| The serpent motif | The finish, age and state of wear |
| | The exact form of the serpent |

**Regular shape, irregular material.** One print file is correct and expected;
one finish across all four pieces is not. They came off four different
scavenging trips and must read as four different metals — dull grey steel on her
right flank, blackened iron on her left, brass with verdigris on the shoulder,
dark bronze on the thigh.

**The serpent is raised, not incised**, so it wears from the top down — the ridge
goes flat and pale where the plate has been handled, and nearly disappears on the
oldest patch. If it comes out crisp and identical on every plate it reads as
jewellery, and the costume says somebody made it for her.

**No two serpents should be identical.** The samples already vary, which is
correct and worth preserving: one die used once would produce a matched set, and
the story is four scavenging trips. Different mills, different batches, different
worn dies.

**One piece may be hardened hide rather than metal**, cut to the same hexagon.
Leather plates carry the serpent faintly or not at all — a mill mark belongs in
metal, and its absence is evidence of where that plate came from.

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

| Patch | Approx. area | Plates |
|---|---|---|
| Flank panel — her right | ~150 cm² | ~110 |
| Flank panel — her left | ~150 cm² | ~110 |
| Shoulder cap | ~120 cm² | ~90 |
| Thigh | ~180 cm² | ~130 |
| | | **~440** |

*Revised 2026-07-31: the sternum patch was dropped, taking about 75 plates with
it.*

**Revised 2026-08-01, and the total went UP by about 70.** The forearm gauntlet
became plain leather, releasing ~150 plates; a pair of scale flank panels was
added over the ribs, costing ~220. Net **+19%** on what was already the largest
labour item in the costume.

*Estimated from assumed patch dimensions — confirm against the real patterns
before committing to a print run.* The flank panels are the least certain
figure here, because their area depends on a pattern nobody has cut yet, and
they are now **half the plate count in the costume**. Pattern them first.

**Getting on for four hundred and fifty plates, each needing two holes and hand
lacing.** That is the largest single labour item in this costume and it is easy
to miss, because each plate is trivial on its own.

**The flank panels also add work the other patches never had:** punched eyelets
down both facing edges, a leather thong long enough to lace the full height, and
two strap-and-buckle fixings at the back. The lacing is visible and structural,
so it cannot be faked with a hidden fastening.

Three consequences:

- **The pressure to print pre-linked sheets will be enormous**, and it is exactly
  the shortcut that kills the flex. If assembly time is the problem, reduce the
  patch areas rather than linking the plates.
- **The raised swirl is now a 12 mm detail.** It has to survive at print
  resolution and it will need a wash or dry-brush to read at all — the relief
  alone will not carry it at that size.
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

## The checklist — not built yet

**Requirement, recorded 2026-07-31.** A per-character checklist of every costume
item, showing build route and progress, so the state of the build can be checked
at a glance.

**It should be generated, not hand-maintained.** Everything else in this repo is
generated from a source of truth and this should be no different — a hand-kept
checklist will drift from `outfits.yaml` within a fortnight, and then the
checklist is worse than nothing because it is trusted and wrong.

The gap is that `outfits.yaml` currently describes costumes in prose and rules,
not as itemised components. It would need a structured block per outfit:

```yaml
components:
  - item: Scale gauntlet, right forearm
    route: printed
    qty: 1
    status: not-started      # not-started | in-progress | done
    note: Dull grey steel finish. Must NOT match the other three pieces
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

**Not started.** Raise it when the first costume actually goes into build.

---

## See also

- [`Shada-Image-TODO.md`](Shada-Image-TODO.md) — the prop reference lock
- [`../01-production-design/Production-Design-Bible-v1.0.md`](../01-production-design/Production-Design-Bible-v1.0.md) — sections 5 and 6, materials and weapons
- [`../03-characters/shada/Character.md`](../03-characters/shada/Character.md) — the four-metals rule this document is mostly about
