# `fitting/` — Vala costume test, 2026-08-05

Twenty-three photographs from a **real costume fitting** — an actor in a built
costume against a white brick wall, shot on a phone. Not generations.

**These are the first physical build reference this character has, and they
outrank the written specification wherever the two disagree.** The repo rule:
for anything physically built, the reference is a photograph of the build, not a
render.

## What was done to them

Rotated upright and **filed under `reference/fitting/`, not the character root**,
where they arrived as `IMG_23xx.jpeg`.

**The rotation was not cosmetic.** Every landscape frame carried EXIF orientation
6 — the pixels are sideways and a tag tells the viewer to turn them. Photo apps
honour that tag; PIL, the staging pipeline and most image generators do not, so
every one of these would have reached a generator lying on its side. The
rotation is now baked into the pixels and the tag is gone, so they are upright
everywhere.

Re-encoded at quality 88 — 67 MB to 38 MB — because they are going into a git
repository and full-quality re-saves were larger than the phone originals.
Filenames keep the original frame number so any shot can be traced back.

## What is in them

| Frames | What |
|---|---|
| 2308–2315, 2317–2319 | Standing, front and three-quarter, hood down |
| **2316** | Three-quarter upright — **the best view of the shawl and the clasp** |
| 2320–2322 | A longer pale over-robe, different configuration |
| 2323, 2329–2333 | Hood up, some with a staff |
| 2327–2328 | With a pack, hood up |

## The costume, as built

- Grey-brown distressed waxed canvas or suede **jacket**, belted at the waist,
  hip length, with a longer under-tunic showing below it
- Brown **leather chest rig** with several small pouches and one larger flapped
  bag
- A heavy olive knitted **shawl-cowl**, deliberately frayed, with long yarn
  tassels, worn over one shoulder and sometimes up as a hood
- **The clasp** pinning it — see `../props/clasp-fitting-2026-08-05.jpg`
- Laced brown **leather bracer** on her right forearm
- Olive **fingerless gloves**
- Olive **cargo trousers**, tapered
- Sand-coloured **wraps wound round both calves**
- Cream lace-up **work boots**

## Against the written specification

**The structure matches better than expected.** `04-factions/slaves-escapees/Faction.md`
specifies for the arena *"strapping, wraps, a belt or harness, reinforcement at
the forearms and shins"* — and all four are present: the bracer, the calf wraps,
the belt, the chest rig.

**THE PALETTE DOES NOT MATCH AND IT IS UNRESOLVED.** The faction rule for the
escapees is *"no colour — undyed, badly dyed, or dye long since gone. Bone-white,
dust-brown and ash."* This build carries a definite olive green through the
trousers, the gloves and the cowl, and the boots are near-cream and read clean.

Either the rule bends for Vala or the build is overdyed. **It is not only her
problem** — the escapees are supposed to read as one group by condition, and she
is already the one who looks different by design.

**Not yet ruled on. See `../../outfits.yaml`, which describes the build as it
stands and flags the conflict at the point it matters.**

## HER FACE HAS BEEN REMOVED FROM EVERY FRAME — 2026-08-05

**All 23 photographs are cropped below the chin.** She is the cast Vala, she has
not given permission, and the Production Designer's instruction was to settle it
immediately rather than wait: *"I think the actor would prefer to be left off
and I'd like to nip that now."*

**CROPPED, NOT BLURRED.** The likeness is not in the file at all, rather than
obscured inside it — a blur is a filter over data that is still there, and a
crop is not. Two frames needed a deeper cut than the rest, where a sliver of jaw
survived the first pass; every frame was checked by eye afterwards.

**The costume loses nothing.** The scope line already said the face was never an
authority. The shawl, the clasp, the chest rig, the bracer, the calf wraps, the
boots and every garment are all still in frame, and the clasp still reads
clearly in 2316 and 2317.

**The prompt now refuses the likeness on its own account**, rather than relying
on the reference simply not showing one — `outfits.yaml` rule 1 is *"BUILD THE
FACE FROM THIS TEXT ALONE… do NOT reconstruct or infer the person it came
from."* A rule that depends on an attachment staying cropped is a rule waiting
to break.

## THE ORIGINAL FRAMES REMAIN IN GIT HISTORY — 2026-08-05

**This is her, and consent has not been obtained.** Recorded by the Production
Designer on the day the photographs were filed.

**THE REPOSITORY WAS PUBLIC WHEN THESE WERE PUSHED, AND IS NOW PRIVATE.** For a
short window every frame — including her face — was reachable at a
`raw.githubusercontent.com` URL by anybody. It was closed the same afternoon by
changing the repository's visibility.

**Two things that follow, and neither is obvious:**

1. **They remain in git history.** Making the repository private stops anonymous
   access; it does not remove anything. If this repository is ever made public
   again, **the history must be rewritten first** — removing the files from the
   working tree is not enough, and a force-push after the fact does not recall
   what has already been cloned or cached.
2. **Nothing here may be published, shared or attached outside this repository
   until permission exists.** That includes Drive publishing, board PDFs, promo
   sheets and anything sent to a third party. The costume may be discussed; her
   face may not be circulated.

**Until permission is confirmed, `outfits.yaml` scopes the costume reference to
the garments and explicitly excludes the face and hair.** That scoping was
written for a different reason — the casting was unconfirmed — and it now does
double duty. Do not relax it on the strength of the casting being settled; the
question is consent, not identity.

## Also unresolved

- **Is this the cast Vala?** If so these double as actor reference — face and
  build — and she is the first escapee to have one. Until that is confirmed,
  nothing here is scoped as a face authority.
- Several frames still show a **sample tag** attached at the hip. It is a
  fitting, not a finished costume.
