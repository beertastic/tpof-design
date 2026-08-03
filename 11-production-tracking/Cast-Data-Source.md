---
title: "Cast Data — where it lives, and why it is not here"
asset_id: "TRACK-CAST-DATA"
updated: "2026-08-03"
status: "standing rule"
---

# Cast Data — where it lives, and why it is not here

> ## THIS REPOSITORY IS PUBLIC.
>
> `github.com/beertastic/tpof-design` — verified public 2026-08-03. It is public
> **on purpose**: every generated prompt carries `raw.githubusercontent.com`
> URLs as a fallback for when attachments do not arrive, and those only resolve
> on a public repository. `tools/regen` treats a failed push as a hard error for
> the same reason.
>
> **So everything committed here is published, permanently.** Git history, forks
> and clones survive deletion.

## The rule

**Nothing that identifies a real person goes in this repository.**

Measurements, contracts, fees, contact details, accommodation, availability,
next of kin, chaperone arrangements — none of it, in any file, including
commit messages.

**Google Drive is the source of truth for all of it**, and it stays that way.
This is the one class of production data the repository does *not* own.

| Lives in Drive, never here | Where |
|---|---|
| **Cast Measurements** | `Price of Freedom / Costume / Wardrobe /` |
| Individual measurement forms and returns | same folder |
| Contracts | `Price of Freedom / Contracts /` |
| Budget, fees, day rates, who is owed what | `Price of Freedom / Master org` |
| Crew contacts, phone numbers, emails | `Master org` |
| Accommodation and chaperone arrangements | `Master org` |

**Decided 2026-08-03 by the Production Designer**, when a proposal to import the
Drive data into this repository ran into the fact that the repository is public.

### Why this is a rule and not a preference

The cast includes **at least one performer with a chaperone budgeted** —
accommodation is planned for a parent alongside them. Their full body
measurements are in the Drive sheet. Publishing that is not a thing that can be
undone by a later commit, and no production benefit is worth it.

## What the repository holds instead

**Character specifications, not performer data.** *"Captain Jasu is 155 cm"* is a
design fact about a fictional person and belongs here. The measurement record of
the performer playing her does not, even though one derives from the other.

The costume department needs both, and gets them from two places. That is the
cost of this arrangement and it is worth paying.

**When a build note needs a real measurement** — a collar size, an inseam — take
it from Drive at the time and do not write it down here. `components:` blocks
describe garments, not bodies.

## What was checked into this rule, 2026-08-03

Read from Drive, kept out of the repository, but worth recording that they were
*seen* so nobody has to go looking again:

- **The casting confirms Captain Jasu's height.** The cast record gives her
  performer as 5 ft 1 in, which is 154.9 cm. The repository says **155 cm**, and
  the 2026-08-03 recast was right. *A Drive sheet rounds the same figure to 156;
  they are the same measurement, not a disagreement.*
- **Baylan at 198 cm is confirmed** by the same record.
- **"Charlie" is a cast member, not a character** — confirmed outright. It
  appears in the cast payment schedule alongside other performer names, which
  closes the last of the naming questions in
  [`Open-Questions.md`](Open-Questions.md). It had previously been resolved by
  inference.
- **Merc 1 is cast as the largest performer in the company** at 6 ft 2 in, which
  is consistent with him being the Wookiee and with the large mercenary in the
  Vala fight. See the open question in
  [`../04-factions/mercenaries/Faction.md`](../04-factions/mercenaries/Faction.md)
  — **this does not settle it**, because that question is about cost and
  prosthetics, not casting.

## Two things found while checking, both outside this repository

Recorded because they were noticed, not because this document owns them.

1. **A live webmail password sits in plaintext in `Master org`**, in a sheet
   reachable by more than one account. It should be rotated and moved to a
   password manager. **Do not copy it anywhere, and never into this repository.**
2. **The actor reference photographs already in this repository are public.**
   `03-characters/CAST-REFERENCE.md` warned about exactly this case and the
   condition it warns about is now true. Flagged there as an open decision,
   2026-08-03.

## See also

- [`../03-characters/CAST-REFERENCE.md`](../03-characters/CAST-REFERENCE.md) —
  consent, and the public-repository decision
