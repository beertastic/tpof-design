---
title: "Shada — Costume Evolution"
asset_id: "EVO-SHADA"
updated: "2026-08-02"
status: "closed"
---

# Shada — Costume Evolution

**How the infiltration dress got from dark brown leather to grey cloth, in seven
passes on 2026-08-02.** Each file is the prompt for one pass; each image is what
that prompt produced. See [`../../README.md`](../../README.md) for the
convention.

**This is history, not specification.** Nothing here is a source of truth. The
costume is specified in `outfits.yaml`, `Character.md` and `Character-Lock.md`,
and the approved reference is `source/artwork/turn-working-front.png`. **Do not
attach these images to a generation prompt** — six of the seven show a costume
that no longer exists.

## The sequence

| # | Pass | What changed | What it cost |
|---|---|---|---|
| 00 | *(starting point)* | The dark brown leather costume the standard prompt produced, already close | — |
| 01 | `cloth-vest` | Hide → **cloth**, for a base layer that creases where the hard pieces bear on it | Clean |
| 02 | `green-khaki` | Brown → **green / grey / khaki** across the whole costume | Skin pattern nearly vanished; five metals collapsed to one; boots lost their wrapping |
| 03 | `plate-size` | Plates from six across a panel toward twelve; thigh patch made scale; cap shrunk | **Overshot** — plates became chain mail |
| 04 | `plate-identity` | Plates back to discrete hexagons, anchored to the thigh patch in the frame | Cap lost its scales; skin pattern went to a rash |
| 05 | `plate-and-cap-size` | Halve the plate width, halve the cap area — expressed as a *change*, with a floor | Clean, but plates still large |
| 06 | `sides-and-wear` | Gauntlet and thigh patch to their correct sides; **missing plates, bent, badly repaired** | Clean |
| 07 | `tessellation-and-grey` | Plates butt edge to edge, not shingled; vest khaki → **grey** | **Approved.** Became `source/artwork/turn-working-front.png` |

## What the seven passes taught

**Absolutes oscillate; changes converge.** Passes 03 and 04 both overshot,
because each specified a target ("10–15 mm", "match the thigh patch") that the
generator hit from the wrong side or that drifted with the image. Pass 05 worked
because it named a *change* with a floor — *halve the width, stop there, twelve
across is the target and the minimum*. Every instruction after that was bounded
at both ends.

**A prohibition does not tell a generator what to draw.** "Tessellated, never
overlapped" had been in the specification for days and the plates shingled
anyway. What fixed it was describing what tessellation *looks like*: flat in one
plane, a thin dark line of backing between neighbours, no shadow falling from one
plate onto the next, a hand run across it would not catch.

**Analogies are instructions.** Pass 03 said the panels should read as "a fine
dense texture, like a mail shirt or a fish's flank." It produced chain mail. The
analogy was doing more work than the measurement.

**Change one variable and declare the rest correct.** Every pass from 02 onward
attached the previous accepted image and listed what to keep. The passes that
drifted were the ones that changed two things at once.

**Two full-figure references competing over one garment is a fight the written
rules cannot win.** That lesson predates this sequence and cost five generations;
it is why there is now exactly one approved costume reference.

## Still open after the lock

**The reptilian contact lenses and the scale pattern on her neck.** Neither reads
in the approved front — the eyes are plain blue, the neck is nearly clear, and
the pattern on her arms is stronger and warmer in colour than the specification
allows (it should be *tonal*, the same colour as her skin). **Deliberately not
fixed here.** A slit pupil is a handful of pixels at full-figure scale and cannot
carry; regenerating the approved front to chase it would risk everything these
seven passes settled. It belongs in `scale_portrait`, which becomes the approved
**makeup** reference — scoped to the face, the eyes and the neck, the way this
image is scoped to the costume. See `11-production-tracking/Shada-Image-TODO.md`.
