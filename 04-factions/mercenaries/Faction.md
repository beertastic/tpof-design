---
title: "Mercenaries"
asset_id: "FACTION-MERCENARIES"
version: "1.0"
status: "in-development"
---

# Mercenaries

> Refer to the Production Design Bible before all visual development.

## Narrative Function

A hunting crew pursuing escaped prisoners across the forest world for a bounty.
Not soldiers, not a unit, not an organisation — a group of individuals who found
each other and stayed together because the work pays.

## Members

| Character | Note |
|---|---|
| [Captain Jasu](../../03-characters/captain-jasu/) | Commands. See below |
| [Baylan](../../03-characters/baylan/) | Eighteen years embedded. Nobody knows what he is |
| [Nyx](../../03-characters/nyx/) | Recurring — patrol, pursuit, dialogue |
| [Reya Fenn](../../03-characters/reya-fenn/) | Sabacc scene, final clearing |
| [Yaslo Bis](../../03-characters/yaslo-bis/) | Sabacc scene, pincer group, final clearing |
| [Shada](../../03-characters/shada/) | Assassin, thief, scout and tracker |
| [Mercenary Kit](../../03-characters/mercenary-kit/) | Reusable background family |

Also present: **an akk dog** belonging to Jasu — see
[`08-species/akk-dog/`](../../08-species/akk-dog/).

## The core rule — no uniform, better kit

**They all found each other.** There is no shared history, no former unit, no
issued equipment and no organisation behind them. Every one of them assembled
their own kit over years.

So the crew is **as mismatched as the escapees are.** The difference is not
uniformity — it is *choice and quality*:

| | Escapees | Mercenaries |
|---|---|---|
| Chose it? | No | Yes, every piece |
| Fits? | No | Yes — adjusted over years |
| Quality | Whatever they were given | Good. They can afford good |
| Decoration | None. They own nothing | Personal marks, trophies, taste |
| Condition | Being destroyed | Maintained, repaired, kept |

They are good at this work and the rewards are high when the targets end up dead.
That money is on their bodies.

**Nothing in this faction is issued. Nothing matches. Everything was picked.**

## Individuality is the faction identity

Each member has visible personality in their kit — and that *is* the group read.
A crew of self-assembled individuals who can afford what they want looks
completely different from a herd of people wearing what they were handed.

In practice:

- Personal marks, trophies, small decorations, kept objects.
- Preference visible in silhouette — how each one carries, layers and arms
  themselves.
- Quality that reads at a distance: good leather, sound plating, maintained
  hardware, boots that work.
- Repairs done properly, with tools and materials — not by hand in poor light.

## Captain Jasu commands because of the akk dog

**Her authority is borrowed from an animal.** She is not in charge through rank,
seniority, tactical skill or the crew's respect. She is in charge because she
owns a monster and everyone knows it.

Design consequences, and they are significant:

- **She must not look like a natural leader.** No insignia that commands respect,
  no rank marking that means anything, no bearing of authority. Whatever
  authority she projects is on loan.
- **The akk dog is the rank.** Where she is, it is. Scene 9 — petting it while
  briefing the squad — is not warmth; it is a reminder, and it should play cold.
- **Scene 19** — the squad kneels or readies gear while Baylan stands at the back
  — reads differently now. Compliance is fear, not discipline.
- The finale is her instrument of power used on an unarmed, injured woman. Then
  Baylan removes the entire structure in under two minutes.
- She may well be the **best-equipped** of them, because she takes the largest
  share. Worth showing.

See [`03-characters/captain-jasu/`](../../03-characters/captain-jasu/).

## Baylan inside this faction

In a crew where every member decorates, personalises and displays taste,
**Baylan's total plainness is conspicuous** — and it reads as a dull man rather
than a hiding one, which is exactly what he needs.

He is the only member with:

- No trophies, no personal marks, no decoration of any kind.
- No preference visible in his silhouette.
- A weapon they mock (Scene 20).
- Kit that is functional and nothing else.

He has been here eighteen years and owns nothing that says anything about him. In
this faction that is not invisible — it is the one odd thing about him, and it is
deliberate.

## Mercenary Kit — a kit of parts

Because there is no uniform, the background family cannot be built as one costume
in multiple copies. It needs a **modular system**: a set of shared component
*types* — jackets, harnesses, plating, boots, headwear — with enough variants that
background figures read as individuals who chose their own gear.

The rule is the class of item, not the item itself. Every mercenary has good
boots; no two pairs match.

See [`03-characters/mercenary-kit/`](../../03-characters/mercenary-kit/).

## The large mercenary — a Wookiee. DECIDED 2026-07-31

**A full Wookiee, and an established member of the crew.** He is in the Sabacc
game in Scene 10 and on the pursuit, not only in the Vala fight.

That second half is what makes the first half affordable to justify. The analysis
below concluded that a full Wookiee is *"only worth it if he appears elsewhere in
the film"* — the decision is to make him appear elsewhere, which satisfies the
condition rather than ignoring it. It also removes the problem the same analysis
flagged: a Wookiee who turns up for one fight in the final act reads as
convenient.

**What it costs.** A full-body suit, a performer with the height, hair
maintenance across every shooting day he is on, and a build that has to survive a
forest. Putting him in Scene 10 and the pursuit **increases his shooting days**,
and the suit and hair maintenance scale with them. That is the price of the beat
working, and it is now a known cost rather than a discovered one.

Build him from the modular kit as
[`mercenary-kit` / `merc-1`](../../03-characters/mercenary-kit/outfits.yaml).

### What the beat still needs

The Vala sequence requires **a severe size mismatch**, **a visible bandolier with
a grenade on it**, and **panic**. A Wookiee delivers the first for free. The
second is now the most natural thing he could be wearing — but see the rejection
below, because it is also the most obvious way to end up with somebody else's
character.

### We are honouring the species, not the character

**Chewbacca is one Wookiee out of millions** — one individual, in the same way
one actor is one human. This is somebody else entirely, and he should read as a
different *person* of the same species, not as a variation on the famous one.
If a viewer's first thought is "that's Chewbacca in different gear", the design
has failed.

The trap is that the bandolier is canonical Wookiee kit and cannot be dropped —
Vala takes a grenade off it. So bandolier plus Wookiee plus forest is a
silhouette the audience already knows by name, and everything else has to do the
separating.

**Wookiee fur varies enormously across the species** — black, grey, cream, rust,
mottled, streaked. The famous one is a single colouring, not the template. This
one is **dark iron-grey shot through with rust brown**, mottled and uneven, and
he is **old**: paling at the muzzle, thinning patches, old scarring, sections
matted and badly healed. Shorter, rougher and worse kept than the long clean fall
of hair the audience pictures.

**No bowcaster** — that weapon belongs to the famous one. A crossed second strap
rather than the single neat diagonal. Rings and beads braided into the fur, which
the famous one does not wear.

He is a working mercenary who assembled his own gear like everyone else in this
crew, and he can afford good equipment. Design him as you would design any other
member of the crew: as an individual.

### The options that were rejected

Kept for the record, in ascending cost.

| Option | Cost | Why not |
|---|---|---|
| A very large human or near-human | Lowest | Casting solves the beat, but gives the crew no non-human presence at the fire |
| Prosthetic face and hands only | Low | Cheaper distinct species, but does not deliver the size mismatch |
| Partial Wookiee — never fully seen | Medium | The honest compromise **if he only appeared in Scene 23.** He does not |
| **Full Wookiee** | Highest | **Chosen.** Justified by his presence across Scene 10 and the pursuit |

## The pursuit is a race

The escapees are heading for **Prodona**, a busy spaceport city. If they reach it
they are gone — into a crowd, onto a ship, untraceable within the hour.

**The forest is the only place the crew can still catch them**, which puts a
deadline on scenes 20 to 23. The mercenaries are not leisurely hunters working a
wilderness; they are racing a city.

## Headcount

**Proposed crew: 10** — six named plus four extras. See
[`Crew-Roster.md`](Crew-Roster.md) for the full breakdown and the scene splits.

The crew operates a **YT-2000 Corellian light freighter**, which cannot house
twenty — ten is already over its nominal capacity. That constraint is useful: a small crew is diegetically correct, matches
the Bible's cramped-and-functional interior rule, and makes Baylan's eighteen
years of hiding considerably worse — there is nowhere on that ship to get away
from anyone.

The crew splits before the finale:

- **Vala pursuit — 5.** Her grenade kills four. Nyx alone survives, dazed.
- **The clearing — 5**, then six when Nyx returns. Baylan kills all of them.
- **Every mercenary in the film dies except Baylan.**

**Scene 10, the Sabacc game, is where the extras earn their money.** One night,
one campfire, the entire crew in a single frame. Establish the crew once and the
audience believes in it for the rest of the film; every other scene can carry two
to four people without reading thin.

## Shared Equipment

Blasters, rifles, a scanner, tarpaulins, crates, ammunition, field-camp
equipment. All maintained, all functional, none of it issued.

## Rejections

- **No uniform, no insignia, no faction colour, no matching anything.** If two
  members look like they were dressed by the same person, it is wrong.
- No military unit read. They are not soldiers and never were.
- No Caribbean pirate, medieval, Victorian, Roman or modern tactical/SWAT
  language — per the Design Bible.
- Nothing factory-fresh, but nothing *ruined* either. This crew maintains its
  gear, and that is the difference from the escapees.
- Jasu must not read as a competent, respected commander.

## Open Questions

- Does the akk dog survive the finale?
- What is Jasu's share, and is her kit visibly the best in the crew?
- The ship is a **YT-2000** but has no name or registry.
- Do any two of them have a prior relationship, or did they genuinely all arrive
  separately?
- **Is the large mercenary in the Vala fight a Wookiee?** See above. Affects
  casting, budget, and whether he needs to appear earlier in the film.

## Revision History

| Version | Date | Status | Notes |
|---|---|---|---|
| 1.0 | 2026-07-30 | in-development | Established as a self-assembled crew with no uniform — distinguished from the escapees by choice and quality rather than uniformity. Jasu's authority recorded as deriving from the akk dog. |
| 0.1 | 2026-07-30 | placeholder | Placeholder document. |
