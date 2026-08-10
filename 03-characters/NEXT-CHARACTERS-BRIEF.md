---
title: "Next Characters — Interview Brief"
asset_id: "PROC-NEXT-CHARACTERS"
updated: "2026-08-10"
---

# Next Characters — Interview Brief

**What each remaining character already has, what is missing, and the exact
decisions needed before their files can be written.**

Written 2026-08-03 so that a design session can be a conversation rather than an
archaeology exercise. **Nothing here invents design.** Where a decision is
outstanding it is written as a question, not filled in with a plausible answer.

**Process:** [`Character-Build-Recipe.md`](Character-Build-Recipe.md) ·
**Rules:** [`../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md`](../09-prompt-library/Writing-Rules-A-Generator-Can-Follow.md)

---

> ## WHO IS STILL OURS — 2026-08-10
>
> **Handed to the costume department:** Captain Jasu, Shada, Vala, Nyx.
> **Handed to the 3D prop master:** Reya Fenn *(handed off under her old name,
> Freya)* and Yaslo Bis — **all costume elements, not just the hard parts.**
>
> **That leaves five for the art department to prep:** Baylan, Shin, Mercenary
> Kit, Krellis, Jeyin. Palpatine is `reference-only` and needs nothing.
>
> **Baylan's working-dress front is APPROVED as of 2026-08-10.** Six views and
> fifteen slots follow from it, and `references:` on that outfit is now empty by
> design — the approved plate is the only costume authority. See
> [`baylan/reference/concept/README.md`](baylan/reference/concept/README.md).
>
> **Krellis had his design session on 2026-08-10** — cast, sized, aged, and the
> carry settled as a satchel. His twenty-year arena clock was broken by the
> casting and has been rewritten; Vala's twenty years survives unchanged.
>
> **The table below is otherwise as written on 2026-08-03** and its `Prompts.md`
> and boards columns have not been re-audited.

---

## Where everyone is

| | `Character.md` | `outfits.yaml` | `Prompts.md` | Boards | Images | `components:` | Build sheets |
|---|---|---|---|---|---|---|---|
| **Shada** | ✅ | ✅ | ✅ ready | ✅ 6 | **✅ 21/21 — done** | ✅ 13 | **✅ guide + 2** |
| **Captain Jasu** | ✅ | ✅ | ✅ ready | ✅ 6 | 19/19 generated — **front re-roll open** | ✅ 12 | **✅ guide + 2** |
| **Baylan** | ✅ 38 KB | ✅ | ✅ ready, 15 slots | 5 — **no make-up board** | **front APPROVED 2026-08-10** | ❌ | ❌ |
| **Shin** | ✅ 23 KB | ✅ | ✅ ready, 14 slots | 7 — **no make-up board** | none | ❌ | ❌ |
| **Mercenary Kit** | ✅ 22 KB | ✅ | ✅ ready, 13 slots | 4 turnarounds only | none | ❌ | ❌ |
| **Nyx** | 9 KB | ✅ | scaffold, 16 `NEEDS:` | ❌ | none | ❌ | ❌ |
| **Krellis** | ✅ 0.3 | ✅ **design session done** | scaffold, 16 `NEEDS:` | ❌ | none — turnarounds ready | ❌ | ❌ |
| **Vala** | 9 KB | ✅ | scaffold, 16 `NEEDS:` | ❌ | 1 | ✅ | ✅ 2 sheets |
| **Jeyin** | 11 KB | ✅ | scaffold, 16 `NEEDS:` | ❌ | none | ❌ | ❌ |
| **Reya Fenn** | 3 KB | ✅ | scaffold | ❌ | none | ❌ | **HANDED OFF** |
| **Yaslo Bis** | 4 KB | ✅ | scaffold | ❌ | none | ❌ | **HANDED OFF** |

**Shada and Captain Jasu are the templates. Both have been through all nine
phases** — documents, references, approved front, turnarounds, slots, boards,
build guide, both build sheets, published to Drive. Every other character follows
them, and nothing about the *process* needs re-deciding.

**That is not the same as saying Jasu is finished.** Her approved front is
carrying three open contradictions against her own rules — the mantle surface
reads as a regular lattice, and the whistle reads as bright jewellery — and the
front is due a re-roll. See [`../11-production-tracking/Jasu-Image-TODO.md`](../11-production-tracking/Jasu-Image-TODO.md).
**The pipeline being complete and a character being complete are different
claims**, and the manifest counts images, which makes that easy to blur.

**The last two columns are the newest gap.** `components:` in `outfits.yaml` is
what `tools/build-lists` reads, and a character without it gets boards and no
build sheets — finished-looking and unbuildable. Baylan, Shin and the mercenary
kit are closest: they have real prompt packs and just need the costume itemised.

**A brand-new character starts with `./tools/new-character`**, which scaffolds
phase 0 from the three intake facts. See
[`Character-Build-Recipe.md`](Character-Build-Recipe.md).

---

## Group 1 — ready to generate, three gaps each

**Baylan, Shin and Mercenary Kit have real, character-specific prompt packs.**
Not templates — Baylan has `crystal.png` and `vision_dune.png`, Shin has
`hair_study.png` and `vision_shadow.png`, the kit has `kit-boots.png` and
`bandolier.png`. Somebody did that work properly.

**They need no interview to start.** Three things bring them to the current
template, and only the third needs any input:

1. ✅ **Cinematic Framing block** — added 2026-08-03 to all three.
2. **A make-up board.** All five other boards exist. Each has the images for it
   already defined — Baylan `detail_portrait` + `expression_strip`, Shin those
   plus `hair_study`, the kit `kit-heads` + `nearhuman-markings`. **The board
   needs its text written**, which is a short conversation per character: what
   the make-up department actually has to do.
3. **A `scale_figure` slot.** None of the three has one, and Baylan needs it most
   — at **198 cm** he is the tallest person in the film, and the akk dog reaches
   his mid-thigh. The Jasu plate proved this is where scale gets fixed.

**Mercenary Kit also has no costume, weapons, performance or materials board** —
only four turnarounds. Four people on one board set is a different layout problem
and worth thinking about rather than copying Shada's.

### Baylan — the one thing to do first

His own notes already say it: **lock his plates before his figures.** He carries
a blaster, a holster and a rifle — three silhouettes, and words will not hold
them across fourteen images. Generate `blaster`, `crystal` and `utility`, approve
them, add them to `references:`, and only then start the figures.

---

## Group 2 — designed as people, not as costumes

**Nyx, Krellis, Vala and Jeyin have real character documents** — story function,
relationships, deaths, backstory. What none of them has is a **physical design**,
and that is what `outfits.yaml` needs before anything can be generated.

Each is blocked on the same short list of questions. Answer these and the files
follow mechanically.

### The questions, for each of the four

1. **Species.** All four say `TBD`. Vala's document explicitly notes nothing in
   her story requires a species; Yaslo's asks whether there is room for a
   near-human. **This decides make-up, prosthetics and half the costume.**
2. **Age, height, build.** Height is not vanity — it is the number that stops
   generators drifting, and it needs a *landmark* not just a figure. Jasu is the
   worked example.
3. **Handedness.** Required. Every weapon and hard-piece placement follows from
   it, and the placement checker warns without it.
4. **The costume in one paragraph** — what it is, what it is made of, and what it
   must never be mistaken for. The "never" list is the most useful part.
5. **Their one hero prop.**
6. **The five to eight specific wrong directions** a generator will drift toward
   for this character. Shada's list is the single most useful part of her pack.

### What is already decided, per character

**Nyx** — *"Baylan's closest thing to a friend, and Baylan kills him in the
finale."* Killed **before** the massacre, not last. His deflected shot kills
Jasu. `Production-Status.md` marks him **PRIORITY** and says baseline human is
decided — so question 1 may already be answered.

**Krellis** — the escapees' medic, poor and badly under-supplied, met Vala in the
arena. **Backstory arrived from the production 2026-08-02:** war-torn planet,
oldest of many siblings, watched his parents die for want of medical help,
captured protecting them. That argues his kit is **the wreck of a real
professional one**, not improvised — a strong costume lead already. Shot through
the head by Jasu mid-plea, Sc.25.

**Vala** — former arena fighter, protects the group. Met Krellis in the arena,
Scene 17. Dies Sc.24, **never shown on screen**, which is a real question for how
much design she needs.

**Jeyin** — Shin's mother, and **the loss the film is built around.** Injured
early and conceals it. Bleeding through her top from Sc.16 — a **six-scene
continuity track**, which means her costume needs a damage-state plan more than
it needs a silhouette. Killed by the akk dog on Jasu's command, Sc.25.

---

## Group 3 — too thin to prep

**Reya Fenn** (3 KB) and **Yaslo Bis** (4 KB) have a paragraph each. Reya has
*"the best entrance in the film"* and is one of the four mercenaries; Yaslo has a
speaking part in two scenes and needs his own costume.

**Both are part of the Mercenary Kit**, so the sensible order is to settle the
kit's four-person design first and let these two inherit from it. Writing them
standalone risks designing the same costume twice.

---

## Suggested order

| | Who | Why |
|---|---|---|
| 1 | **Jasu** finishes | 16 images and 6 boards, everything in place |
| 2 | **Baylan** | Best-developed document in the project, pack ready, plates first |
| 3 | **Shin** | Pack ready, three costume states, and she carries the ending |
| 4 | **Jeyin** | The damage continuity is the design, and it touches Shin's scenes |
| 5 | **Nyx** | Marked PRIORITY, species may already be settled |
| 6 | **Mercenary Kit** | Then Reya and Yaslo inherit from it |
| 7 | **Krellis, Vala** | Both die; Vala is never shown |

---

## What an interview needs from you, in one line each

- **Nyx** — confirm baseline human, then age/height/build and the costume paragraph.
- **Krellis** — is the medical kit the costume? What does under-supplied look like?
- **Vala** — how much design does someone who dies off-screen actually need?
- **Jeyin** — the damage states across six scenes, before the costume itself.
- **Mercenary Kit** — four people, one board set: how do we lay that out?
- **Baylan / Shin** — the make-up board text, and a scale landmark each.
