---
title: "Script v9 — Reconciliation"
asset_id: "TRACK-SCRIPT-V9"
updated: "2026-08-01"
status: "open — 7 of 9 resolved or actioned"
---

# Script v9 — Reconciliation

**The screenplay arrived in the repository on 2026-08-01**:
`02-story/scenes/The Price of Freedom v9.pdf` — 30 pages, written by Grace
Taylor, story by Tristan Pretty.

**This is now the source of truth and it outranks everything in this repository.**

Until today the design documents were built from two things: the Filmanize scene
breakdown (a 13-page export carrying scene descriptions and extracted elements)
and a Production Designer interview on 2026-07-30. Character.md's own revision
history records this — *"built from breakdown + Production Designer interview"*.
Nobody in the art department had read the script.

Most of the design work survives contact with it. The costume language, the
salvage aesthetic, the handedness rules, the prop specifications and the whole
Shada build are unaffected. **What follows is only where the documents and the
script disagree**, ranked by how much work depends on the answer.

Nothing below has been changed in the design documents. These are decisions.

---

## 1. Baylan's age — **RESOLVED 2026-08-01. Late forties, 48. Script changed.**

> **BAY (late 40s)**, a haunted yet strong-willed man — *v10, Scene 3*

Settled as a compromise, and it is a better number than either side had. The
Production Designer plays the part and is fifty; the script said early thirties.
Late forties splits it and reads on camera.

**It also rescues the timeline rather than breaking it.** At 48 in ~1 BBY he was
**30 at Order 66** — an established Knight, comfortably. The documents' original
*"~32 and established"* barely moves, and the eighteen-year gap that everything
else hangs on survives untouched. Early thirties would have made him a child at
the purge and taken the whole backstory with it.

Changed in the script (v10) and propagated through `Character.md`,
`Character-Lock.md`, `board-data.yaml`, `Prompts.md` and the prompt pack.

The original disagreement, for the record:

> **BAY (early 30s)**, a haunted yet strong-willed man — *Scene 3*

`Character.md` and `Character-Lock.md` both open with **"Human male, 50 years
old"**, and the age is load-bearing across the entire design:

- *"Tall and broad, thickened with age and labour. Powerful once, merely large now."*
- *"Iron-grey hair"*, *"going iron, badly cut"*, the grey-haired-warrior rejection
- *"Not athletic or agile. Fifty, thickened, slow."*
- *"eighteen years of not sleeping"*, *"two decades giving nothing away"*
- The timeline: *"Set ~1 BBY, eighteen years after Order 66. Baylan 50, Shin 15"*
  and *"~32 and established at the time of the purge"*

If he is in his early thirties, he was a **child or a young teenager** at Order 66,
not an established Knight — which changes his backstory, not just his hair.

The script supports the younger reading elsewhere. Scene 12 dates the vision at
*"a few years younger and less haunted"*, not eighteen years. And Scene 25 has
him say *"I had my life ripped from me. Twice"* and *"It was instilled in me. But
then it died"* — the language of someone raised into it young and cut off early.

It was the largest open question in the project — it reaches casting, make-up,
the costume's read, the performance notes, the timeline and every prompt in his
pack. Hence changing the script rather than quietly designing against it.

---

## 2. Vala — **NOT a conflict. The script never stages her death.**

**This entry was wrong when first written on 2026-08-01 and is corrected here.**
It reported that the script kills Vala. It does not. Nyx's dialogue was read as
narration, and it is not.

Scene 24 **cuts away before the detonation**:

> She opens her hand. Nyx looks down and sees the red blinking light.
>
> **NYX**
> Oh shi-
>
> **> CUT TO:**

The last frame of Vala has her alive, held off her feet, with a live detonator in
her open hand. The explosion is heard in Scene 25 by Krellis, Jeyin and Shin, who
are somewhere else entirely.

Her death exists only as **two pieces of reported speech**, and neither is
reliable:

- **Krellis** — *"It was Vala giving us a chance."* A grieving man drawing the
  obvious conclusion from a bang in the trees. He saw nothing.
- **Nyx** — *"That slave set off a grenade. Killed my whole squad. (sneers) And
  herself."* A hostile witness asserting something he cannot know, since **he
  survived that same blast** — *"His clothes are tattered and singed. Blood runs
  down the side of his face."* He was close enough to be burned and far enough to
  live. So was she, potentially.

**Consequence: the standing rule is already satisfied.** *"Do not stage a death;
show no injury"* is exactly what the script does. `Planted-Elements.md`, the
deferred-injury decision and the Film 2 material all hold with no script change.

If her survival needs to be airtight rather than merely available, the single
line to revisit is Nyx's *"And herself"* — and even that plays honestly as a
character being wrong about what he did not see.

---

## 3. Deaths, generally, do not match — **ACTIONED 2026-08-01**

All of these are now written into the character documents, and the full picture —
who dies, whether the camera sees it, and what each costs to build — is in
[`Deaths-And-Effects.md`](Deaths-And-Effects.md).

**The cost finding is worth repeating here: only two deaths in the film are
expensive.** Krellis needs one hard VFX shot and Jeyin needs the most demanding
prosthetic in the production. Seven of the eleven cost almost nothing, because
the script cuts away from the grenade and plays the massacre on Shin's face.

| | Script v9 | Design documents |
|---|---|---|
| Krellis | **Shot through the head by Jasu**, on screen, Sc.25 | No death recorded. "Placeholder — escapee medic" |
| Jasu | Killed by a blaster bolt **Baylan deflects** into her chest | "Baylan kills everyone" |
| Reya Fenn | **Alive in Sc.25**, has dialogue, dies in Baylan's final massacre | ~~"Killed by Vala's grenade"~~ **corrected in roster v2.0** |
| Loryl | **Does not appear in v10 at all** — he is `Yaslo Bis`, renamed | ~~"Killed by Vala's grenade"~~ **folder deleted, references repointed** |
| Nyx | Blade withdrawn orange ✓ — but **killed BEFORE the massacre, not last.** Baylan stabs him, talks to Shin, then *"I have to take care of this first"* and cuts down the rest | ~~"Nyx is killed last"~~ **corrected in roster v2.0** |
| The akk dog | **Baylan locks eyes with it and sends it away** — "something passes between them" | "Knocked out, left alive and abandoned" |

The akk dog change is an improvement and I would take it: he does not spare it,
he *dismisses* it, and it obeys him rather than Jasu. That is a far better version
of the same beat.

Note also that Nyx's death has no raised hands in the script — he pulls a knife
and advances on Shin. The documents' *"raised hands must read as a Force push, a
deliberate misdirect"* is not in v9.

---

## 4. A named mercenary with no file, and one who has vanished — **ACTIONED 2026-08-01**

**`YASLO BIS`** has dialogue in Scene 10 (deals the sabacc hand) and again in
Scene 25. There was no character folder, no entry in the crew roster, and no
mention anywhere in the repository.

**`Loryl`** had a `Character.md` and a folder, and does not appear in v10.

**Done:** `03-characters/yaslo-bis/` created with his scene beats and the two
lines that make him matter.

**RESOLVED 2026-08-01: Loryl is Yaslo Bis, renamed.** Production Designer
confirmed. `03-characters/loryl/` is deleted; his prompt-pack scaffold and
artwork folder were moved to `yaslo-bis/` rather than rebuilt, and every
reference across the repository now points at the real name.

**The headcount is unaffected** — the v2.0 roster never counted Loryl. Yaslo Bis
was already the sixth named mercenary, so the crew is still ten.

### And the whole roster was rebuilt on the back of it

`Crew-Roster.md` v2.0 replaces the "four generic extras" idea with **Merc 1 to
Merc 4** — four specific people, one per kit build, each in a named group from the
Sc.23 split, each with a death. `03-characters/generic-mercenary/` is now
`03-characters/mercenary-kit/`, which is what its own first line always called it.

Three further v1.0 errors were corrected in the process: Reya Fenn survives the
grenade and dies in the finale, Nyx dies **before** the massacre rather than last,
and **Jasu is not killed by Baylan** — Nyx fires at him, he deflects without
looking, and the bolt hits her in the chest.

**One script change:** Sc.23's *"You three — pincer movement"* became **"You
four"**, so Baylan's massacre is four bodies rather than three. Production
Designer's call — it is the film's only demonstration that he can take several
opponents at once and it has to read as easy.

**Also:** Scene 10 refers to Shada as **"him"** — *"as Shada knuckles Nyx's hair.
Nyx pushes him off."* Shada is designed and cast as a woman, with an actor
reference on file. Probably a script slip, but it is the one character whose
design is closed, so it should be settled rather than quietly ignored.

**And:** Nyx has already lost an eye — *"Gotta finish my route or Jasu will have
my other eye."* Nothing in his notes records this.

---

## 5. The Wookiee is in the script

> **The wookie** hauls her off of her feet. — *Scene 24*

`Open-Questions.md` still carries this as undecided: *"Is the large mercenary in
the Vala fight a Wookiee? Wanted, but likely too expensive."* The script has
already decided. Vala takes the detonator from his chest exactly as the documents
predicted.

This resolves the open question and validates the faction work. It does not
resolve the cost.

---

## 6. How they leave — **RESOLVED 2026-08-01. No script change.**

**They leave on the mercenary ship, and Scene 25 stays exactly as written.**

The apparent conflict dissolves once the post-credit scene is counted. That was
decided on 2026-07-30 and is already specified in
[`02-story/Planted-Elements.md`](../02-story/Planted-Elements.md):

> Where she fell, a blast crater, dead mercenaries. **Shot from behind — head and
> shoulders only — as the stolen ship lifts away.** She does not know Shin is
> aboard.

*"The stolen ship"* is the mercenaries'. So the exit is settled, the Film 2 plant
holds, and the three scenes now set inside that ship pay off when it is taken.

**The smoke is a landmark, not a destination.** The script's last line —
*"they run off into the trees, towards the still-swirling column of smoke"* — is
the only thing on the horizon and reads as *away*. Nothing says they are going to
the wreck, and nothing needs to.

**The ending is not to be touched.** It was briefly proposed that the film should
end on Baylan's extended hand, cutting before Shin takes it. The Production
Designer withdrew it the same day. As written, the hand is fourth from the end and
the script explicitly has her take it, with *"hope in her eyes, as if she's seeing
the future she can finally have — the one her mother had hoped for her."* That is
the payoff of Jeyin's dying line, and *"Ready?" / "Ready."* is the beat the whole
film has been walking toward. Both stay.

### Still outstanding: the post-credit is decided but not written

It exists in the design documents in full detail and **appears nowhere in the
screenplay**, which currently ends at `FADE TO BLACK`. Somebody has to write it,
and it is the shot that carries Vala into Film 2.

---

## 7. Scene 24A never existed — **RESOLVED 2026-08-01**

**Confirmed by the Production Designer: there is no Scene 24A and there never
was.** It is an artefact of the Filmanize breakdown, which was the first thing
uploaded to this repository and which does not match the screenplay. The design
documents inherited it and carried it into nine files.

The screenplay has **25 scenes**: the clearing fight with Vala is Sc.24 and the
finale is Sc.25.

Every reference is repointed. `Scene-Index.md` now carries the screenplay's
numbering rather than the breakdown's.

**This was never a draft change.** Nothing was renumbered by the writer — the art
department was working from a bad index for two days.

The breakdown is wrong about Scene 6 in the same way. It lists an ordinary forest
scene; the screenplay has `EXT. FOREST - EVENING (VISION)` — Baylan seeing Shin's
group, with Nyx's voice cutting into it.

---

## 8. Things the script says that the documents missed, and should have

- **The holster is empty from Scene 15, and the script makes it a plot point.**
  Sc.20: *"Bay, where's your blaster?"* He covers with the heavy rifle. This is a
  costume continuity track across the last third of the film and no image shows
  it. **Now recorded in `Character.md` and `Character-Lock.md`.**
- **Baylan is Jasu's second.** Nyx, Sc.10: *"We all know Bay's her right hand."*
  The documents say the opposite — *"Not a ranking officer. He is a subordinate
  who stands at the back."* Sc.19 does put him at the back, so both can be true,
  but the design was built on the weaker reading.
- **He names himself.** *"My name. Is Baylan Skoll."* — Sc.25, over Nyx's body.
- **He offers to train her.** *"I can teach you, train you. We can bring this
  cycle of — of hurt to end."* Not in any document.
- **Shin takes a second keepsake** — she rips a piece of armour from Jasu's body
  in the last beat. The documents record only Vala's clasp.
- **Scene 15 is written as disassembly** — *"He starts to take apart the blaster,
  piece by piece..."* The documents were corrected on 2026-07-30 to insist it is a
  **reconstruction** and that parts must converge. The script trails off before
  saying. Worth confirming, because the doc's version is the better scene.
- **Jeyin's wound has no stated cause in v9.** The documents have her impaled by
  torn hull metal in the Sc.2 crash; the script simply shows blood spreading
  through her top from Sc.16. Not contradicted — just unsupported.

---

## 9. The sabacc scene on the virtual set — **DONE 2026-08-01**

**Three scenes moved inside the ship** in v10, onto the virtual set being built
and tested the weekend of 2026-08-02:

| Scene | Was | Now |
|---|---|---|
| 10 — the Sabacc game | `EXT. FOREST - MERCENARY CAMP - NIGHT`, round a campfire | `INT. MERCENARY SHIP - MAIN HOLD - NIGHT`, one work lamp over a crate |
| 13 — Baylan wakes | `EXT. FOREST - MERCENARY CAMP - NIGHT` | `INT. MERCENARY SHIP - CREW BUNKS - NIGHT` |
| 15 — the crystal | `EXT. FOREST - MERCENARY CAMP - LATER` (while describing a tent) | `INT. MERCENARY SHIP - CREW BUNKS - LATER` |

**Scenes 9, 14 and 19 stay outside**, by decision. Jasu and the akk dog under a
tarpaulin against a tree, the storage area among the unloaded crates, and the
morning muster before they move out — none of them gain anything indoors, and 14
is the Nyx patrol conversation, which is explicitly an exterior.

Two things broke and both were fixed rather than left:

- **Shada is in Scene 10**, and her spec said `EXTERIOR ONLY — she is never
  indoors`, with *"if there is a wall or ceiling, it is wrong"* in her watch-list.
  Now carved out precisely: slot 2 is her only interior, it is a cramped salvaged
  hold under one swinging work lamp, and everywhere else the old rule stands.
- **The kit's slot 2 was titled `SCENE 10, THE CAMPFIRE`** and written around
  firelight. Rewritten for the hold.

Baylan's slot 4 and his `tone-collage` panel both had him in a canvas tent, and
his `must_show` said the undertunic shows *"in the tent, at night"*. All three now
say his bunk.

**The tents are gone entirely — decided 2026-08-01, superseding an earlier note
here that argued for keeping them.** Nobody sleeps outside. Sc.7's *"begins to set
up a makeshift tent"* became *"starts dragging a crate clear of the ramp"*, and
the camp is now a working area rather than a sleeping one: unloaded stores, a
fire, and a tarp rigged as a windbreak.

It is the better version. With the whole crew bunking aboard, the ship reads as
over capacity without anyone saying so — and **Baylan has nowhere to be alone**.
When he wants to be unobserved in Sc.14 he cannot step into his own tent; he has
to walk out into the trees, which is exactly how Nyx nearly catches him.

**What the move buys beyond the money:** the audience now spends three scenes
inside this ship before the finale, so when Baylan and Shin leave on it they are
leaving on somewhere they know rather than a prop. And Scene 15 — the most
private thing he does in the film — now happens in a room with other people
asleep in it.

---

## What has already been actioned

- **Baylan collapsed to one costume** with the robe as a removable layer, and the
  separate Scene 12 Jedi build dropped. Decided 2026-08-01 with the producers.
  This is a deliberate departure from the script, which names Jedi robes in Sc.12
  — recorded in `Character.md` and `Character-Lock.md` so it is not rediscovered
  as an error.
- **The empty holster after Sc.15** written into his documents.
- **Age settled at 48** and propagated everywhere, including back into his
  prompts.
