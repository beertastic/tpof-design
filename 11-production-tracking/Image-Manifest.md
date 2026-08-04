# Image Manifest

**Every image this film needs, per character, with the arithmetic shown.**

Built 2026-08-04 to make the shape of the project visible before the remaining
design work starts. It supersedes nothing — `Production-Status.md` is still where
status lives. This answers a different question: *how much is there, in total, and
where is it concentrated?*

**Some of this is dummy data, and it is marked.** Rows carrying a ⚠ are
placeholders standing in for a decision nobody has made yet. They are here so the
structure is complete and countable, not because they are right.

## How a character's count is built

There is no flat "21-image treatment", and quoting one has been misleading. The
real formula is:

```text
total = (5 turnaround views × number of costume states) + slot images
```

Slot lists are **bespoke per character** — Jasu has an akk dog and bone horns,
Baylan has a converted lightsaber and a crystal pouch, Shin has a hair study and
a clasp. They are not a template with the names swapped, and the count varies
from 6 to 16.

| Tier | Slots | Which |
|---|---|---|
| **Full** | 13–16, bespoke | The character's own props, materials and narrative beats |
| **Reduced** | **6**, fixed | `portrait`, `environment`, `scale_figure`, `expression_strip`, `materials`, `tone-collage` |

The reduced six are the 2026-08-03 decision written out: *turnarounds, portrait,
expressions, scale plate, one materials plate, one narrative frame, tone collage.*

## The manifest

| Character | Tier | States | Turnarounds | Slots | **Total** | Done | Status |
|---|---|---|---|---|---|---|---|
| **Shada** | Full | 1 | 5 | 16 | **21** | 21 | **COMPLETE.** The worked example |
| **Captain Jasu** | Full | 1 | 5 | 16 | **21** | 14 | 5/5 turnarounds; 9/16 slots. **7 remain** |
| **Baylan** | Full | 2 — base + coat | 10 | 14 | **24** | 0 | Prompts ready, `handedness: right`, checker clean |
| **Shin** | Full | 3 — clean, forest, blood | 15 | 14 | **29** | 0 | **Blocked** — no `handedness:`, no `must_show:` |
| **Vala** | **Full** | 3 ⚠ — clean, forest, blast | 15 | 16 ⚠ | **31** | 0 | **Human.** No sheet — needs `outfits.yaml` |
| **Jeyin** | **Full** | 3 ⚠ — clean, forest, mauled | 15 | 15 ⚠ | **30** | 0 | **Human.** No sheet — needs `outfits.yaml` |
| **Krellis** | **Full** | 2 ⚠ — clean, forest | 10 | 15 ⚠ | **25** | 0 | **Human.** No sheet — needs `outfits.yaml` |
| **Nyx** | Reduced | 1 — mercenary | 5 | 6 | **11** | 0 | **PRIORITY.** Baseline human; design TBD |
| **Reya Fenn** | Reduced | 1 — mercenary | 5 | 6 | **11** | 0 | **Human.** Costume must work fully sealed |
| **Yaslo Bis** | Reduced | 1 — mercenary | 5 | 7 ⚠ | **12** | 0 | **Human + cybernetics ⚠ provisional.** +1 slot for the cyber detail plate |
| **Mercenary Kit** | Special | 4 builds | 20 | 13 shared | **33** | 0 | 33 prompts ready. Merc 1 (Wookiee) has no turnaround by decision |
| ~~Palpatine~~ | — | — | — | — | **0** | — | Reference only. `Reference.md`, no costume to build |

| | |
|---|---|
| **Total images** | **248** |
| **Done** | **35** — Shada 21, Jasu 14 |
| **Remaining** | **213** |

## Vala, Krellis and Jeyin — full sheets, 2026-08-04

**Decided: all three get a complete character sheet and a full image set, with
variations appropriate to the character and the archetype.** Krellis and Jeyin
are promoted from the reduced tier; Vala was promoted on 2026-08-04 already. This
is the largest single scoping change since the tiering decision — **+30 images**.

### What "complete character sheet" means in files

All three currently hold only `Character.md`, `Prompts.md` and `source/`. Measured
against Shada, who is the finished example, each is missing:

| File | What it does | Vala | Krellis | Jeyin |
|---|---|---|---|---|
| `Character-Lock.md` | The non-negotiables. What `must_show` is built from | missing | missing | missing |
| `outfits.yaml` | Costume states, `handedness:`, `must_show:`. **Nothing generates without it** | missing | missing | missing |
| `board-data.yaml` | Board layout config | missing | missing | missing |
| `reference/` | Approved reference plates | missing | missing | missing |
| `Prompts.md` | Present, but the **generic 14-slot scaffold** — not a bespoke list | rewrite | rewrite | rewrite |

### The variations, and why each one exists

The archetype shows up more in **slots** than in states. All three run the same
forest, so they share the clean → destroyed spine; what differs is what their
lives put in front of the camera.

**Vala — the arena fighter. 3 states, ~16 slots.**
Captured and forced to fight in the arena (Sc.17), protects the group throughout,
takes a squad with her own grenade in Sc.24, and **survives** — the post-credit
scene shows her in the blast crater with dead mercenaries around her. The third
state is **blast damage**, not forest damage, and it is what Film 2 inherits.
Her archetype earns: the **grenade and bandolier** as hero props, a **weapons**
plate, and a **scars and old injuries** study — `Character.md` notes the breaks
and scars she carries out of the arena, and Krellis is the one who treated them.

**Jeyin — Shin's mother. 3 states, ~15 slots.**
Her arc mirrors Shin's exactly, so her states do too: captivity, forest-destroyed,
and then the mauling. `Deaths-And-Effects.md` rates her **"Fully staged, extended
— Highest cost: prosthetics plus creature interaction"** and calls the appliance
**the most demanding build in the film**: survivable-looking for the length of her
dialogue, unmistakably fatal. Her archetype earns **injury and appliance plates**
and a **blood-continuity** study, because the blood has to hold across several
minutes of screen time, her death, and Shin's Force blast.

**Krellis — the medic. 2 states, ~15 slots.**
Two states, not three: he is shot through the head mid-sentence in Sc.25, so there
is no injury progression to track — the death is instant and the costume never
changes after the forest. His archetype earns the extra slots instead:
`Character.md` argues his kit is **"the wreck of a real working kit"** rather than
a bag of improvisations, because he was the arena's medic and that is a post. That
wants **two kit slots** — proper instruments, and the bag they live in — plus the
wayfinding detail that makes his death cost the group a *skill* rather than a map.

**⚠ The state counts and slot counts above are proposals, not decisions.** They
follow from the script and the existing documents, but each bespoke slot list has
to be written before the numbers are real.

## Where the work actually is

**Six characters carry 172 of the 213 outstanding images:** Mercenary Kit (33),
Vala (31), Jeyin (30), Shin (29), Krellis (25) and Baylan (24). Nyx, Reya Fenn and
Yaslo Bis are 11 apiece, and Jasu's 7 are the only ones with prompts already
current.

**Costume states are the multiplier, not slot count.** A third state costs five
images; a whole reduced-tier character costs eleven. Giving the escapees their
forest-destroyed state added 15 images across Krellis, Jeyin and Vala, and
promoting the three of them to full sheets added 30 more.

**The "~21-image treatment" figure understates the full tier.** It was derived
from Shada and Jasu, who each wear one costume. Applied to multi-state characters
it is 24–31, and Vala is now the worst case.

## Decisions this manifest records

Taken 2026-08-04, and new here rather than inherited:

- **Vala, Krellis and Jeyin all get complete character sheets and full image
  sets**, with variations appropriate to the character and archetype. Krellis and
  Jeyin promoted from the reduced tier.
- **Reya Fenn and Yaslo Bis get the reduced 11-image set each.** Both have "own
  costume" in `Crew-Roster.md`, both speak, both die in Baylan's massacre. They
  fell through the 2026-08-03 tiering decision, which named neither.
- **Escapees get two costume states minimum, mercenaries get one.** The escapees
  cross the same forest as Shin and arrive in the same condition. Mercenaries
  arrive by ship and stay pristine. Vala and Jeyin earn a third state on top.
- **Palpatine is excluded.** Lore, not a costume.

## Species and gender — settled 2026-08-04

**The whole cast is now decided on both.** This cleared the single largest
blocker on the project: 108 images were waiting on it.

| Character | Gender | Species |
|---|---|---|
| Shada | she/her | Human, with inherited serpentine ancestry |
| Captain Jasu | she/her | Human — decided 2026-08-01 |
| Baylan | he/him | Human |
| Shin | she/her | Human |
| Vala | she/her | **Human** |
| Jeyin | she/her | **Human** — forced; Shin's mother, and Shin is human |
| Krellis | he/him | **Human** |
| Nyx | he/him | **Human, baseline** — stale `TBD` corrected |
| Reya Fenn | she/her | **Human** |
| Yaslo Bis | he/him | **Human, with cybernetics over the face and possibly the arms** ⚠ |
| Merc 1 | he/him | Wookiee — decided 2026-07-31 |
| Merc 2, Merc 3 | — | Human |
| Merc 4 | — | Near-human, make-up alone — decided 2026-07-31 |

**Gender was never actually open.** Every document was already internally
consistent; it had simply never been stated in the `Physical Design` block. It is
recorded now so nobody re-derives it from pronouns.

**⚠ Yaslo's cybernetics are provisional and flagged for checking at his design
pass.** *Face* is the decision, *arms* is a maybe. They earn him a **seventh
slot** — a detail plate — which is the one image this decision added. The
constraint they must survive: he is the warm one in the Sabacc scene, and the
facework cannot cost him expression or make him read as a thug.

**One consequence, accepted knowingly.** Every escapee is human, and all species
presence in the film sits with the mercenaries — the Wookiee, Merc 4's near-human
and Shada's ancestry. The captives are uniformly human and their captors are not.
Recorded here because it is a visible pattern, not because it needs revisiting.

## What is still dummy, and what it blocks

**No character has an `outfits.yaml` outside the four that are built.** Vala,
Krellis, Jeyin, Nyx, Reya Fenn and Yaslo Bis have none, and **nothing generates
without one** — it carries the costume states, `handedness:` and `must_show:`.
Now that species is settled, this is the only thing standing in front of the
whole remaining slate.

**⚠ Every state and slot count carrying a mark is a proposal.** They follow from
the script and the existing documents, but the bespoke slot lists have to be
written before the numbers are real.

**Shin's block is tracked but not scheduled.** She cannot start until
`handedness:` and three `must_show:` blocks exist — the same shape of block that
applies to Vala, Krellis and Jeyin.

## Revision History

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-08-04 | **Species and gender settled for the whole cast** — the 108-image blocker cleared. All five open characters are human; Yaslo Bis gains provisional cybernetics and a seventh slot. Total 247 → 248 |
| 1.1 | 2026-08-04 | **Vala, Krellis and Jeyin promoted to full sheets and full image sets**, with archetype-appropriate variations proposed per character. Total 217 → 247 |
| 1.0 | 2026-08-04 | Created. Tiering completed for Reya Fenn, Yaslo Bis and Vala; escapee costume states decided; Palpatine excluded |
