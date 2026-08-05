# `props/`

Photographs of the physical builds.

**The repo rule: for anything physically built, the reference is a photograph of
the build, not a render.** A render is a proposal; the printed object is the
thing the camera will see, and the two drift. This has already bitten twice on
this character.

---

## `blaster-build-2026-08-05.jpg` — THE CONVERTED LIGHTSABER

**Supplied by the Production Designer, 2026-08-05.** A photograph of the printed
build, unpainted, with the dimensions marked on it by hand.

**Scope line — use this verbatim when it is attached:**

> *Authoritative for the BLASTER'S SHAPE, PROPORTION AND COMPONENT LAYOUT ONLY —
> the silhouette, the parts and where they sit. It is NOT an authority on FINISH
> or COLOUR: it is unpainted print, bare light grey, and the weapon is matte,
> weathered, scratched and dark with eighteen years of handling on the grip.
> THE WRITTEN RULE WINS ON FINISH.*

That caveat is the whole risk with this image. It is bright bare plastic against
a character whose palette rule is near-black, and Baylan has already lost a
generation to exactly this failure — the gauntlets came back polished chrome
because *"DULL, DIRTY AND BATTERED"* sat third in its rule. **An unpainted print
attached without a finish caveat is an instruction to make it shiny.**

### Dimensions, from the photograph

| | |
|---|---|
| Overall length | 340 mm |
| Overall height | 105 mm |
| Upper receiver ⌀ | 40 mm |
| Magazine block | 90 mm tall, 55 mm wide |
| Muzzle to magazine | 100 mm |
| Magazine to rear | 70 mm |

**340 mm is a large pistol** — long-barrelled, front-heavy, unbalanced in the
hand. That is on-spec, not a problem: the rule asks for *"a scratch-built,
unbalanced-looking pistol assembled from mismatched parts"*, and the length is
what sells it. **The height must read too** — it is a deep, blocky object, not a
slim one.

### The conversion is visible in the build, and it must survive to the plate

The lightsaber is still legible in the object, which is the entire point of the
plant:

- **The emitter shroud has become the muzzle** — the slotted, stepped cylinder at
  the front is saber architecture, unmodified.
- **The ribbed body running the full length** is the hilt's grip section, turned
  horizontal and used as the receiver.
- **The magazine below is a second ribbed hilt section**, cut down and hung
  vertically.
- **A machined cylindrical core runs through the middle of it** — this is the
  part that reads as "empty crystal chamber" in the disassembled view at slot 11.

**This is the object, and every later image must match it.** `Prompts.md` sets
the continuity requirement: *"Every component visible in the reconstructing hilt
was visible on the assembled blaster. Same object, different arrangement."*
Without a build photograph the two were being drawn from words twice and had no
reason to agree.

### Where it is attached

`slot_references:` in `outfits.yaml`, scoped to three slots and no others:

| Slot | Why |
|---|---|
| `blaster` (08) | The plate of the object itself |
| `utility` (10) | Kit layout — the blaster is in it |
| `maintenance` (11) | The reconstruction; must match component for component |

**Deliberately NOT on the turnarounds**, though the blaster is holstered on his
right hip in all of them. A 340 mm detail photograph attached to a full-length
costume fitting invites the weapon to grow and to take the frame — the failure
the akk dog scoping exists to prevent. The turnarounds carry it in words until
there is an approved front, and then they match against that.

---

## `gauntlets-build-2026-08-05.jpg` — THE GAUNTLETS

**Supplied by the Production Designer, 2026-08-05**, and it closes the second of
the two outstanding build photographs. Printed as a matched pair, unpainted
black, photographed outdoors on paving.

**Converted from `.avif` on arrival.** AVIF is not safe here — the staging
pipeline reads with PIL, which does not decode it without a plugin, and image
generators are inconsistent about accepting it. **Save build photographs as
`.jpg` or `.png`.** The filename also lost its space, because these get passed
through shell tooling.

### NOT YET ATTACHED TO ANYTHING, AND THAT IS DELIBERATE

It is on disk and it is not in `references:` or `slot_references:`. Two reasons,
both concrete:

**1. There is no slot to scope it to.** The gauntlets appear in the seven
turnarounds and in none of the fourteen numbered slots. So the only way to
attach it is outfit-level — which puts it on the front turnaround, **the one
image currently being used to test the chevron fix.** Adding a second variable
to a single-variable test means the next result cannot be attributed to either
change. It goes on after the front is approved.

**2. The build and the written rule disagree in three ways**, and attaching the
photograph settles all three silently, in the picture's favour. That is Baylan
lesson 6 exactly — *"rules can arrive whole and still lose to each other, and
the picture won every time."* **These need a ruling before the image is wired
in, not after.**

| | The written rule | The build |
|---|---|---|
| **Form** | *"a smooth clamshell shell closing with no visible fastening"* | Not smooth and not a clamshell — a one-piece open-backed tube with **four or five heavy stepped ribs** around the lower half |
| **Screen** | *"a SMALL DARK screen and a few worn buttons… scuffed and half dead, **with nothing lit on it**"* | A **large, bright, near-white** screen with a pale keypad below it. It reads as lit and as the brightest thing on the costume |
| **Position** | *"at the INSIDE of each wrist"* | High on the **broad outer face**, nearer the elbow than the wrist |

**The screen is the one that matters.** Rule 2 is *ABSOLUTELY NO ORNAMENT* and
rule 26 is *"nobody in frame finds them remarkable"*; his entire characterisation
is *"the absence IS the design."* A glowing white rectangle on each forearm is
the most eye-catching object on a near-black costume, and it is the first thing
an audience would look at. **Either the print gets painted down — screen dulled
to near-black, keypad knocked back — or the rule changes to admit a lit screen
and the characterisation takes the hit.**

The palette is otherwise **right, and better than the blaster's**: the print is
black, on-palette, so it does not carry the bare-grey finish risk. What it does
carry is **gloss** — the layer lines catch the light — against rule 24's *"DEAD
DULL, NO shine, NO polish, NOTHING mirror-like."* Matte varnish or a dusting of
matte spray before it is photographed on the actor.

### When it is wired in, it needs this scope line

> *Authoritative for the GAUNTLETS' SHAPE, PROPORTION AND RIBBING ONLY. NOT an
> authority on FINISH: they are DEAD DULL, filthy, scratched and greasy, with the
> finish worn off at every edge. NOTHING on them is glossy, bright or lit.*

**And the label is capped at 52 characters**, so the refusal has to be inside the
first sentence or it will not arrive — see the note on `slot_references:` in
`outfits.yaml`. `THE GAUNTLETS — SHAPE ONLY, NEVER FINISH OR SHINE.` fits.
