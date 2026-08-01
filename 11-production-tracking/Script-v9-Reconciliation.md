---
title: "Script v9 — Reconciliation"
asset_id: "TRACK-SCRIPT-V9"
updated: "2026-08-01"
status: "open — needs Production Designer decisions"
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

## 1. Baylan's age. The documents say fifty; the script says early thirties

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

**This is the largest open question in the project.** It affects casting, make-up,
the costume's read, the performance notes, the timeline and every prompt in his
pack. His prompts currently carry no age at all — I removed *"FIFTY YEARS OLD"*
from `must_show` rather than bake a contradiction into five turnarounds. They say
*"tall, broad, thickened"* and describe the wear without dating it.

**Needed:** his actual age, and whether the eighteen-year timeline holds.

---

## 2. Vala dies in the script. The documents say she survives

The documents are emphatic:

> Vala | Placeholder | **Survives.** Do not stage a death; show no injury.
> Killed by Shin in Film 2 — *Production-Status.md*

> Where is Vala's post-credit scene set? **Where she fell** — blast crater, dead
> mercs, shot from behind as the stolen ship lifts away — *Open-Questions.md*

The script has her pull the detonator herself in Scene 24, and Nyx confirms it in
Scene 25:

> That slave set off a grenade. Killed my whole squad. *(sneers)* **And herself.**

There is no post-credit scene in v9.

This one runs deep — `02-story/Planted-Elements.md` and the Film 2/3 material are
built on her surviving, and the *"deferred injury"* decision exists specifically
to keep that option open.

**Needed:** is the survival a planned change to the script, or has the plan
changed? Everything about Film 2 hangs on it.

---

## 3. Deaths, generally, do not match

| | Script v9 | Design documents |
|---|---|---|
| Krellis | **Shot through the head by Jasu**, on screen, Sc.25 | No death recorded. "Placeholder — escapee medic" |
| Jasu | Killed by a blaster bolt **Baylan deflects** into her chest | "Baylan kills everyone" |
| Reya Fenn | **Alive in Sc.25**, has dialogue, dies in Baylan's final massacre | "Killed by Vala's grenade, off screen" |
| Loryl | **Does not appear in v9 at all** | "Killed by Vala's grenade, off screen" |
| Nyx | Killed last, blade withdrawn orange ✓ | ✓ matches |
| The akk dog | **Baylan locks eyes with it and sends it away** — "something passes between them" | "Knocked out, left alive and abandoned" |

The akk dog change is an improvement and I would take it: he does not spare it,
he *dismisses* it, and it obeys him rather than Jasu. That is a far better version
of the same beat.

Note also that Nyx's death has no raised hands in the script — he pulls a knife
and advances on Shin. The documents' *"raised hands must read as a Force push, a
deliberate misdirect"* is not in v9.

---

## 4. A named mercenary with no file, and one who has vanished

**`YASLO BIS`** has dialogue in Scene 10 (deals the sabacc hand) and again in
Scene 25. There is no character folder, no entry in the crew roster, and no
mention anywhere in the repository.

**`Loryl`** has a `Character.md` and a folder, and does not appear in v9.

Most likely Loryl was renamed. Worth confirming rather than assuming.

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

## 6. How they leave, and on what

The documents say they steal the mercenary ship and it is theirs from Film 2:

> **They steal the mercenary ship.** It is theirs from Film 2 onward. Archive it.

The script's last line sends them the other way:

> together, they run off into the trees, towards the still-swirling column of
> smoke from **the ship crashing** — *Scene 25*

That is the **escapees'** wreck, not the mercenary ship. Which also means the
escapee ship — still the only asset with no document — may be the one they leave
on.

---

## 7. The scene numbering has changed

The breakdown lists 25 scenes including a **24A**. Script v9 has 25 scenes and
**no 24A** — the clearing fight is Sc.24 and the finale is Sc.25.
`02-story/script-breakdown/Scene-Index.md` is therefore out of date, and so is
every `scenes:` field in every `outfits.yaml`.

Scene 6 has also become a **vision** in v9 (`EXT. FOREST - EVENING (VISION)`) —
Baylan seeing Shin's group, with Nyx's voice cutting in. The breakdown had it as
an ordinary forest scene.

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

## 9. The sabacc scene, if it moves onto the virtual set

Scene 10 is `EXT. FOREST - MERCENARY CAMP - NIGHT` in v9, around a campfire.
There is a plan to shoot it on the virtual set as a **ship interior** instead
(being built and tested the weekend of 2026-08-02).

Two things break if it moves indoors:

- **Shada is in Scene 10**, and her spec says `EXTERIOR ONLY — IN ANY IMAGE THAT
  HAS A LOCATION. She is never indoors`, with *"if there is a wall or ceiling, it
  is wrong"* in her watch-list. That rule would need relaxing for her one interior.
- **The mercenary pack's slot 2 is titled `SCENE 10, THE CAMPFIRE`** and is
  written around firelight. Ship interior lighting is a different image entirely.

Neither is hard to change. Both are wrong until somebody does.

---

## What has already been actioned

- **Baylan collapsed to one costume** with the robe as a removable layer, and the
  separate Scene 12 Jedi build dropped. Decided 2026-08-01 with the producers.
  This is a deliberate departure from the script, which names Jedi robes in Sc.12
  — recorded in `Character.md` and `Character-Lock.md` so it is not rediscovered
  as an error.
- **The empty holster after Sc.15** written into his documents.
- **Age removed from his prompts** rather than assert fifty against the script.
