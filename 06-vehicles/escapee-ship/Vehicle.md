---
title: "Escapee Ship"
asset_id: "VEHICLE-ESCAPEE-SHIP"
version: "1.0"
status: "in-development"
class: "TBD — see Open Questions"
owner: "The escapees. Stolen from the slave auction"
---

# Escapee Ship

> **Production rule:** Refer to the Production Design Bible before all visual development.

**The ship that starts the film.** It carries four people off a slave auction,
flies into a dampening field it knew nothing about, and comes down in Scene 2.
Everything that follows — the chase on foot, Jeyin's wound, the column of smoke
on the horizon for the rest of the day — comes out of this vehicle.

> **It had no document until 2026-08-03.** It was named in
> [`README.md`](../README.md) and its consequences were written up under
> [`07-locations/forest-world/`](../../07-locations/forest-world/Location.md) and
> in [`03-characters/jeyin/Character.md`](../../03-characters/jeyin/Character.md),
> but the vehicle itself had no entry. This is that entry. **It records what the
> script fixes and what is still open; it decides no visual design**, because
> none has been decided.

## What the script fixes

Three lines, and they are all there is:

| Scene | The line | What it fixes |
|---|---|---|
| **2** | *"A more rickety ship tumbles through the sky. Smoke billows from its engines as it drops down past the treeline."* | **Rickety.** Tumbling, not gliding. Engine smoke, evening light, and it goes down below the trees |
| **9** | *"The reports say that their ship crashed two clicks from here. The dampening fields used to protect the mines, stop ships flying over."* | **Two kilometres** from the mercenary landing, and the cause: the field, not pursuit |
| **25** | *"…they run off into the trees, towards the still-swirling column of smoke from the ship crashing."* | The smoke is **still up a full day later** — and it is the bearing of the last shot in the film |

**Scene 2 is the only time the audience sees it.** Perhaps three seconds, in the
air, already failing, at distance and against an evening sky. It is never seen
intact, never seen on the ground, and never seen from inside.

## What that means for the build

**The design load is almost entirely silhouette and behaviour.** A shape against
the sky, tumbling, trailing smoke — read in a few seconds by an audience that has
just watched a sharp metal ship fly the other way.

- **It is the contrast pair to the mercenary ship**, and the contrast is the
  point. Theirs is a maintained YT-2000: worn, sound, chosen. This one is
  whatever would fly. Design them against each other — see
  [`../mercenary-ship/Vehicle.md`](../mercenary-ship/Vehicle.md).
- **It must read as rickety in silhouette alone**, because that is all the frame
  gives it. Not derelict-looking-but-elegant. Asymmetric, patched, wrong.
- **It must plausibly hold four.** Dozens fled the auction; these four found each
  other and took a ship. Small, and taken because it was there.
- **Nobody aboard chose it and nobody aboard could maintain it.** They are
  escaped slaves. There is no history of care on this hull.

## It was stolen, and that shows

They escaped a slave auction during a mass revolt and stole whatever would lift.
Two consequences worth designing to:

- **It is not their ship, and it does not fit them.** No personal trace, no
  adaptation, nothing added. They were aboard it for hours, not years.
- **Whoever owned it before had a purpose for it** — and it should read as that
  purpose, badly served. Cargo, transport, a service hull. Not a passenger
  vessel, and certainly not a fighter.

## The crash was an accident of navigation

**Nobody shot them down.** They flew too close to a dampening field protecting a
mine that has nothing to do with anyone in the film, stalled, and fell — the same
shape as the accident that triggered the escape in the first place. The galaxy is
not paying attention to these people.

This is load-bearing for the whole film and is recorded in full under
[`07-locations/forest-world/`](../../07-locations/forest-world/Location.md).

## The three things this asset needs

Restated from [`README.md`](../README.md), now with a home for each:

| | Thing | Where it lives | State |
|---|---|---|---|
| 1 | **The ship** — airborne, tumbling, smoking | This document | Class and design open |
| 2 | **The wreck as a location** | [`07-locations/forest-crash-site/`](../../07-locations/forest-crash-site/Location.md) | Written 2026-08-03 |
| 3 | **The torn metal as a prop** | `05-props/` — **does not exist yet** | See below |

### The torn metal

**The piece of hull that impales Jeyin.** It is the most consequential physical
object in the film: it kills a principal across six scenes of continuity, and it
is the reason the finale happens the way it does.

It is needed **only if the crash is filmed**. The crash is currently intended to
happen off screen for budget — but the *wound* is on screen from Scene 8 onward
and a prosthetic has to match something. **Whoever designs the wound is
implicitly designing this prop**, whether or not it is ever built. See
[`03-characters/jeyin/Character.md`](../../03-characters/jeyin/Character.md) for
the six-scene injury track.

Torn hull metal, not a spar or a blade: the ship came apart around her.

## Appearances

| Scene | Presence |
|---|---|
| **2** | **On screen** — tumbling through the evening sky, smoke from the engines, dropping past the treeline |
| **9** | Referenced — Jasu briefs the crew about the crash and its distance |
| **24, 25** | Set dressing — the still-swirling column of smoke on the horizon. The last shot of the film runs toward it |

Off screen but continuous: the smoke is up all day, which means it is available
as background in **any exterior scene from 3 onward** and should be treated as
part of the sky, not as an effect that comes and goes.

## Open Questions

- **Class and model.** Entirely open. The only constraints are: rickety, holds
  four, stolen from a slave auction, and it must not read as a variant of the
  YT-2000.
- **Is it ever seen intact?** Currently no — Scene 2 is already the crash. A
  brief establishing beat before it stalls would cost a shot and would let the
  audience see what these people escaped in. Not recommended unless the crash is
  filmed anyway.
- **Is the crash filmed?** Currently off screen for budget. This decides whether
  items 1 and 3 above are built or only implied.
- **Name and registry.** Unnamed. **Probably correct** — they stole it hours ago
  and would not know its name. Worth deciding rather than forgetting: a visible
  registry on the hull that belongs to somebody else is a cheap, good detail.
- **Does the wreck appear on screen at all?** See the crash-site location
  document — this is the same question from the other end.
- **The last shot runs toward the smoke, and the working ship is the other way.**
  Already flagged under `forest-world`. Baylan and Shin steal the mercenary ship,
  which is at the landing clearing; the smoke is two kilometres past it. Either
  the last shot is a bearing rather than a destination, or the geography of the
  final run needs a decision. **Not a design question — a blocking one**, but it
  lands on this asset because the smoke is what they are running at.

## See also

- [`README.md`](../README.md) — the two ships as a contrast pair
- [`../mercenary-ship/Vehicle.md`](../mercenary-ship/Vehicle.md) — the maintained half of the pair
- [`07-locations/forest-crash-site/`](../../07-locations/forest-crash-site/Location.md) — the wreck
- [`07-locations/forest-world/`](../../07-locations/forest-world/Location.md) — the dampening field, and why the film happens on foot
- [`03-characters/jeyin/Character.md`](../../03-characters/jeyin/Character.md) — the wound this ship causes

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 1.0 | 2026-08-03 | in-development | First document. The three scripted lines recorded as the only fixed facts; the stolen-ship and accident-of-navigation readings carried across from `Open-Questions.md` and `forest-world`; the torn metal named as a prop that does not exist. No visual design decided. |
