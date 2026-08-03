# Shada Character Lock

**Status:** LOCKED FOR BOARD REVIEW  
**Version:** 6.0  
**Date:** 2026-08-03

**There are now TWO approved references, with stated, non-overlapping scopes.**

| Reference | Authoritative for | NOT for |
|---|---|---|
| `source/artwork/turn-working-front.png` | **The costume** — everything below the collar | The face, the eyes, the make-up |
| `source/artwork/scale_portrait.png` | **The make-up** — the slit pupils, and the relief, placement and extent of the scale pattern | The costume. There is none in frame |

Two references with **stated, non-overlapping scopes** is not the failure that
cost five generations. That failure was two references competing over the *same
garment*. The make-up plate is cropped to head and neck **precisely so there is
no costume left in it to compete with anything** — the collar and the shoulder
plates were cropped out rather than described away.

## The costume front — APPROVED 2026-08-03 (v2)

Every other view and every narrative plate matches against this single image. It
settles the five things that seven variant generations moved: a **cloth** vest
rather than hide, a **grey / grey-green / khaki** palette rather than brown,
plates **tessellated edge to edge**, a shoulder cap **the size of a palm**, and
**visible wear with plates missing** from the panels.

**v2 changed exactly one piece: the shoulder cap now HANGS LOOSE**, standing off
her shoulder by a few centimetres with daylight under its ragged lower edge,
instead of gripping the shoulder front to back like a fitted pauldron. The
superseded 2026-08-02 front is at
`reference/alternates/turn-working-front-superseded-2026-08-02.png` and **must
not be attached to anything.**

**That was never a design change.** `must_show` rule 5 had described the drape in
detail — *"sitting AWAY FROM THE BODY… it hangs, it lifts, it swings when she
turns, and DAYLIGHT SHOWS UNDER ITS LOWER EDGE"* — since 2026-08-01. **137 of its
1,555 characters were reaching the generator**, and the drape was not among them.
For four days the cap came back moulded, and it read as a design fault when it
was a trim fault. Re-ordering the rule so the drape leads fixed it in one pass,
with no new words. *This is the clearest single instance of the failure
[`Prompt-Reliability-TODO.md`](../../11-production-tracking/Prompt-Reliability-TODO.md)
exists to describe.*

### Known deviations in the approved front — the written rule wins on all three

Tolerated rather than chased, because each costs a re-roll that risks the cap:

- **The scale pattern on her arms runs WARMER** than the tonal rule allows. The
  make-up plate is the authority, and it too runs slightly warm; **the rule wins
  on colour — tonal, the same colour as her skin.**
- **The boots are strapped and buckled** against a rule that says never.
- **The plates run about six or seven across a flank panel** against a spec of
  twelve.

**Her eyes are human in the front, and that is CORRECT for this plate.** A
vertical slit pupil is two or three pixels at full-figure scale and cannot
render there; chasing it in a full-length view risks everything that took seven
passes to win. **The eyes are locked in `scale_portrait.png`**, at a scale where
they read, and that plate is attached to every prompt.

**It is not a face reference.** The face comes from the actor photographs. This
has already cost one generation, which came back in the right costume on the
wrong person; the failure was that the reference carried no scope, not that the
model misbehaved. Any full-figure photograph attached to a prompt must say what
it is *for* and what it is *not*.

**The two direction photographs are retired.** `costume-front-v2.png`,
`flank-panels.png` and `costume-direction-front.png` are kept on disk as history
and are no longer attached to anything. Every fault they carried has been
designed out — the smooth shoulder plate, the leather forearm wrap, the oversized
plates, the brown palette, the hide vest. **Two full-figure references competing
over one garment is a fight the written rules cannot win**, and that lesson cost
five generations before it was learned.

These traits are non-negotiable unless the Production Designer approves a
recorded revision.

## Identity

- Female mercenary assassin and thief.
- Compact, agile build; small beside most of the crew.
- Mostly human appearance with subtle serpentine ancestry.
- Dangerous through precision, patience and observation.
- Quietly dependable toward her crew.

## Species Traits

- Fine scales on neck, collarbone, shoulders, arms and hands.
- **On the face: edges only** — temples, outer cheekbone, jawline, side of the
  neck, behind the ear. Never the nose, forehead, cheeks or mouth. Tonal, readable
  only in raking light, missable in flat light.
- **Achieved in makeup, not prosthetics.** A human actor; no budget for a full
  facial appliance, and a full-face treatment would read as creature anyway.
- **Reptilian contact lenses** are the single highest-value element.
- Reptilian quality to the eyes without becoming a full creature design.
- Uses scent and environmental observation instinctively.
- Movement remains human, restrained and economical.

## Costume

- Light, fitted, scavenged armour.
- Vital-area protection only.
- **Flexible metallic scale in place of rigid plate — with exactly one
  exception, the printed forearm gauntlet.** See Coverage below.
  - Individual **six-sided metal plates** — hexagons with six straight sides, each
    10 to 15 mm across, about a thumbnail — laced and riveted to a flexible backing and
    **tessellated edge to edge with a narrow visible gap, never overlapped or
    shingled**. No frame or bezel around any plate.
    Never round, never a fish-scale shape.
    **Individually visible and countable** — never a texture or a printed pattern.
  - **The density, fixed 2026-08-02: about twelve plates across the width of a
    flank panel and fifteen rows down** — well over a hundred in one panel. This
    is the single most persistent error in the costume; it has come back wrong in
    five generations, both too coarse and, once corrected too hard, too fine.
    There is a floor as well as a ceiling: **at twelve across, a plate is still an
    individually visible hexagon you could put a fingertip on. Any finer and the
    panel becomes chain mail**, which is as wrong as a dozen big tiles.
  - **What tessellation looks like, said positively** — added 2026-08-02, because
    the prohibition on its own has never been enough. Every plate lies **flat in
    the same plane** as its neighbours, six flat sides butted against six flat
    sides. Between two plates there is **a thin dark line** showing the backing
    beneath, and nothing else: no plate edge riding over another, no shadow of an
    upper plate falling on a lower one, no stepped or layered surface. A hand run
    flat across the panel would not catch. Not shingled, not lamellar, not roof
    tiles, not fish scales.
  - **The wear is part of the specification** — added 2026-08-02. **Five to ten
    plates are missing from each flank panel and three to five from the shoulder
    cap**, leaving scattered dark gaps where the hand-cut backing shows through —
    along the edges, at the waist, over the hip, at the top edge of the cap, the
    places that catch and flex. Bent corners, chipped and cracked plates, rows
    drifting out of line, an eyelet torn out and re-punched beside the old hole, a
    different cord spliced into the lacing where it broke. **Survived in, never
    laid out — and never ruined:** she is alive because this works, and she
    maintains it badly, with what she has.
  - **Every plate carries the same shallow serpent stamp** — a manufacturer's
    mark on cheap hull plate, industrial and meaningless, worn soft and grimed.
    Never crisp, never ornamental. She did not choose it.
  - **Cut from salvaged hull plate, not forged as armour.** Mismatched alloys
    oxidising at different rates — brass, bronze, dull steel, verdigris, rust.
    Sections visibly replaced. **The shape and stamp repeat; the metal never
    does.**
  - **Metallic but never bright.** Dulled and scratched, catching light in small
    dull glints across many facets. It must read as *metal*.
  - **Coverage — five hard pieces, five different materials, all asymmetric.**
    **REVISED 2026-08-01 (third revision of the day)** by the Production
    Designer, against two reference photographs since retired. It keeps
    everything from the second revision and **restores the pair of flank panels
    the second revision had dropped.** The coverage has not moved since; what
    changed on 2026-08-02 was the material, the palette and the sizes, not which
    pieces exist or where they sit.

    *Why the flank panels come back:* the second revision dropped them on the
    argument that a shaped panel each side, laced at the centre front, would read
    as a corset. A generation of exactly that shape showed otherwise. It reads as
    **brigandine**, and what keeps it off a corset is the **strip of vest cloth
    visible in the lacing gap** — the collar, the placket and the centre-front
    seam stay readable between the panels. The concern was real and the picture
    answered it; the answer is now a rule, because a panel pair that closes up in
    the middle would fail exactly as feared.

    *A note on how this design has moved.* The flank panels were added, dropped
    and restored inside one day. That is not indecision worth hiding — each turn
    was settled by looking at a picture rather than by re-reading the argument,
    and the version that survived is the one nobody could fault on sight.

    **Sides are fixed, and given from her own left and right.**
    - **Gauntlet — her RIGHT forearm — a SOLID 3D-PRINTED SHELL.** Wrist to just
      below the elbow, wrapping the outer forearm, on a worn taupe leather cuff
      that shows above and below it. **One rigid surface** — not individual
      plates, no lacing, and it does not flex. Its face is **plain worn plate,
      not a hexagon field**: a broad flat panel with a shallow border line at the
      edge, a scatter of small rivets, and a faint raised serpent swirl worn
      almost away. **Dull grey steel**, pitted, pale worn silver on the raised
      edges. **A small cluster of four to six telltales near the wrist** — dim
      amber, the size of a match head, grimy and half-dead, no glow spilling onto
      skin or cuff. **Her left forearm is completely bare, and there is exactly
      one gauntlet.**
    - **Cap — her LEFT shoulder — LOOSE SCALE.** The opposite side to the
      gauntlet; her right shoulder is bare. Genuinely separate plates laced to a
      hand-cut backing, sitting **away from the body** — it lifts, hangs and
      swings, and daylight shows under its lower edge. Never moulded or shrunk to
      the deltoid, never a solid pauldron. Held by a thin strap under the arm and
      a tie to the vest shoulder, both visibly improvised. **Blackened iron**,
      near-black and matte, rust in the pitting. The plates are **the same
      10–15 mm hexagons as the rest of the costume** — the cap is a scale field,
      not a plate with a scale texture on it, and **three to five of its plates
      are missing.**
      **SIZE — a palm's width, settled 2026-08-02 after three passes.** It covers
      the point of her left shoulder and nothing else. Its outer edge stops where
      the shoulder becomes the arm; it does not run down her upper arm. Its inner
      edge stays well clear of her collarbone and never crosses toward the centre
      front. Its lower edge stops well above the armpit. About twenty-five to
      thirty-five plates. **An oversized cap is how a yoke gets back into this
      costume under another name**, and the yoke is this character's most
      persistent failure.
    - **Patch — her LEFT outer thigh** — the same side as the shoulder cap; her
      right thigh has no metal. A **field of the same small hexagonal plates**
      laced onto the outer trouser leg from hip to above the knee — never a solid
      patch, never leather, never a pocket. **Dark bronze**, almost brown and the
      warmest thing on the costume, and the newest piece: cleaner, less worn,
      clearly added later. Against the grey palette it is now the **only warm
      thing in the whole costume**, which is deliberate.
    - **Flank panels — BOTH sides, LOWER TORSO ONLY.** Shaped scale panels
      covering ribs, waist and hip: from below the armpit — **never above it** —
      down to the hem of the vest, following the ribs, drawing in at the waist
      and flaring slightly over the hip. The top edge sits at about the bottom of
      the shoulder blade, and **everything above that line is plain cloth.**
      Nothing crosses her shoulders, her collarbone or her upper chest. **Laced together across the
      centre front** with a leather thong zig-zagging through punched eyelets and
      tied off at the bottom; two salvaged straps and buckles at the back.
      **Nothing goes over the shoulder** — they hang on the lacing and the
      straps, so her arms stay clear. Worn **over** the vest.
      **A strip of vest cloth must stay visible between them**, with the collar,
      the concealed placket and the centre-front seam readable in the gap. That
      gap is the difference between brigandine and corset and it must not close.
      **Her RIGHT panel is pale worn pewter** — cold, almost white-grey, thin and
      scratched right through in places, the oldest thing she owns. **Her LEFT is
      rust-red oxidised iron**, brown-red and heavily corroded, obviously later
      salvage. **The two must not match** — a pair in what they do, never in how
      they look.
    **No breastplate, no solid chest plate, no sternum panel, no bib, no pendant
    and no yoke.** Her chest and sternum stay plain cloth between the panels, and
    the flank panels are the only metal on her torso. Stating this is what stops
    a full yoke reappearing; omitting it is not enough.
    **Within any ONE piece the metal is all one metal.** A panel speckled with
    four alloys is decorative mottling: one panel is one piece of salvage from one
    trip. It is the **five pieces** that differ from each other, not the plates
    inside a piece.
    **Nothing matches anything.** Five scavenging trips, five scraps, five states
    of wear. **No full yoke, and no matching pair of anything — including the two
    flank panels.**
    At most a quarter of the costume carries metal.
  - **Fastenings:** buckles, hooks, lacing, toggles, straps. Any zip must be heavy
    industrial hardware — large chunky exposed metal teeth, weathered, oversized
    metal pull. **Never a fine modern coil zip.** If in doubt, use hooks or lacing.
  - **Weapons are worn, not implied, and their sides are fixed. Right-handed.**
    - **Blaster — her RIGHT SIDE**, hip or thigh, either acceptable. Grip up and
      angled forward, right-hand draw. Never her left. The drop-leg rig is one
      option, not a requirement.
    - **Knife — her left hip**, on the belt, grip up. Cross-draw.
    - Both visible in every costume view. Nothing is mirrored.
  - **Moves like heavy cloth, not plate.** That is why she wears it.
  - **It reads as serpentine: she wears her own ancestry as armour.**
- **The vest is CLOTH, and it is GREY. Changed 2026-08-02.** A heavy,
  close-woven working fabric — matte, dry, sun-faded, with the softness and the
  give of cloth. It is her **base layer**: the flexible thing the hard pieces are
  strapped over, and it compresses and wrinkles wherever a plate, a strap or a
  buckle bears on it. Never leather, never stiff, never moulded. Still
  close-fitting and cut to her figure — flexible is not slack.
  - **The colour is a dusty, sun-bleached stone grey with a hint of khaki-green.**
    The green is a *cast*, not a colour: enough that it does not read as neutral
    concrete, not enough that anyone would call it olive. Not blue-grey, not
    slate, not charcoal, not a clean neutral grey. It is the lightest thing she
    wears.
  - *Until 2026-08-02 this was scavenged hide in dark brown.* The hide was never
    wrong, but cloth reads as the layer the armour is strapped over, and the grey
    lets the five metals separate from the garment instead of sinking into it.
- **The vest carries a serpentine grain.** Added 2026-08-01, and it survived the
  change of material on purpose. The grain is now **woven into the cloth** rather
  than pressed into a hide: a **faint, fine, irregular snake-skin texture** in the
  weave itself, tonal, the same colour as the rest of the vest, readable only
  where light rakes across it. She did not choose it any more than she chose the
  mill mark on the plates. It is the quietest thing in the costume carrying her
  ancestry, which is why it was worth keeping.
  - **This does not reopen "scale as texture".** That prohibition governs the
    **armour**, where every plate must stay a discrete, countable, physically
    separate piece, and it stands unchanged. A grained cloth is cloth, not armour,
    and the two must never be confused: if the grain starts to read as plates, or
    the plates start to read as grain, both are wrong.
  - **It must never become a pattern.** No printed snakeskin, no reptile print,
    no repeating motif, nothing decorative. At two paces it is a plain worn grey
    vest; the grain is something you find on the third look.
- Functional exposed skin for mobility, heat and sensory function.
- Layered technical cloth, worn leather and repaired matte hardware.
- Practical harness, belt, sheath and concealed holster.
- **All the leather is GREY-BROWN TAUPE. Changed 2026-08-02.** Belts, holster,
  thigh strap, boots and the cuff under the gauntlet: desaturated and
  sun-bleached, with a greenish-grey cast. Never chestnut, never tan, never
  saddle brown. It drifts warm on almost every generation, and warm leather pulls
  the whole costume back toward the brown this design left behind.
- **Trousers — grey-green.** Darker and colder than the vest, close-fitting,
  matte and heavily worn, creased behind the knee and rubbed pale at the thigh
  and seat. Nothing is ever worn over them.
- **Belt — two tiers.** Recorded 2026-08-01 from the reference. A worn taupe
  leather waist belt with a plain squared metal buckle, sitting level; and a
  second belt slung diagonally below it, dropping to her right to carry the
  holster, with a strap and buckle round the thigh.
- **Boots — mid-calf, wrapped.** Recorded 2026-08-01 from the reference.
  Weathered grey-brown taupe leather, flat soled, round toed, trouser legs tucked
  in. Long leather straps wound criss-cross up the shaft and buckled off at the
  top — visibly wrapped by hand every morning, not a fastening the boot came with.
- Nothing polished, ornamental or factory fresh.

## Weapons

- **WESTAR-35 blaster pistol** — the specific in-universe model. Slab-sided,
  dull silver-steel, brass panels in the slide, worn black grip. Mandalorian
  manufacture carried by a non-Mandalorian. Her right thigh, drop-leg holster.
- Well-used combat knife that never leaves her side.
- Small climbing and infiltration kit.
- No datapad.
- No oversized firearm or unnecessary gadget load.

## Design Drift Prevention

Reject any design that becomes:

- Caribbean pirate.
- Medieval fantasy.
- Modern tactical/SWAT.
- Heavy-armoured soldier.
- Generic human scavenger with no serpentine ancestry.
- Fully reptilian, or any full-face prosthetic treatment.
- A chest patch, sternum panel, bib, pendant, breastplate or solid chest plate.
  Dropped 2026-07-31: it kept rendering as hanging jewellery and it was the shape
  most likely to grow into a chest plate. **The flank panels are the exception
  and the only metal permitted on her torso** — they sit at the sides, over the
  ribs, and the centre front stays cloth.
- **Flank panels that meet in the middle.** The strip of vest cloth visible in
  the lacing gap is what makes them brigandine rather than a corset. If the two
  panels close up, or the lacing is hidden, or the gap fills with metal, the
  fear that got them dropped on 2026-08-01 has come true.
- **A panel speckled with several alloys.** One panel is one piece of salvage:
  all one metal. The mismatch is between the five pieces, never inside one.
- **Any part of another character's costume.** Recorded 2026-08-02 after a
  generation returned Captain Jasu's costume wearing Shada's face: bone horns, a
  full-width scale yoke across the shoulders, a quilted long-sleeved bodysuit and
  a matched pair of wrist bracers. **No horns, no headdress, no helmet, no yoke,
  no sleeves, no bodysuit, no second bracer, no hanging cord or pendant.** The
  cause was a shared conversation rather than a bad prompt, but the prompt now
  names all four tells as hard prohibitions so it survives the mistake.
- **A yoke, collar piece or shoulder-to-shoulder panel.** The flank panels are
  **lower-torso only** — ribs, waist and hip. Nothing crosses her shoulders,
  collarbone or upper chest, and the top edge of a panel never rises above the
  armpit.
- **A second gauntlet.** There is exactly one, on her right forearm, and her
  left is bare. A pair means somebody made her a set.
- **A shoulder cap moulded to the shoulder**, or a solid pauldron. It hangs
  loose, off the point of the shoulder, and light gets under it. **Nor one
  smooth plate** — it is a field of small scale plates, and the costume
  photograph shows this wrong.
- **The gauntlet and the cap swapped over.** They sit on opposite sides — the
  gauntlet on her right forearm, the cap on her left shoulder — and on
  2026-08-02 a generation exchanged them while leaving the blaster correct, so
  it was not a mirrored image. That diagonal is the design; a gauntlet and a cap
  on the same side is a matching set, which is the one thing this costume is not.
- **A skirt, tabard, apron, overskirt or hanging panel over the trousers.** Her
  legs read as legs from hip to boot. Nothing drapes and nothing hangs below the
  hem of the vest.
- **A wrap front, a V-neck or a crossover vest.** It fastens on a concealed
  placket behind a stand collar, straight down the centre front.
- **A leather vest.** It is cloth, and it creases where the hard pieces bear on
  it. If it reads as hide, the base layer has become armour.
- **A brown costume.** The palette is grey, grey-green and khaki. The leather in
  particular drifts warm on nearly every generation.
- **Plates that shingle.** They butt edge to edge in one flat plane, with a thin
  dark line of backing between them. No plate rides over another.
- **Chain mail.** Plates so fine they lose their edges and become an allover
  metallic fabric. Twelve across a flank panel is the floor as well as the target.
- **Armour that looks laid out.** Plates are missing, bent and badly repaired.
- **A lit gauntlet.** A small cluster of dim recessed telltales at the wrist, and nothing more.
  No glowing seams, no edge lighting, no light spilling onto skin or leather, no
  illuminated hexagons. If the gauntlet lights the shot, it has become a prop
  from a different film.
- Fine modern coil zips or neat garment zips.
- Three matching patches. They came from three different scavenging trips.
- An empty holster, or a costume record with the weapons absent.
- A matched or symmetrical set of scale armour. It was added piecemeal; a matched
  set means somebody made it for her, and nobody did.
- Bulky, loose or oversized. Her costume is close-fitting and follows her figure —
  waist defined, cut to the body. (Revised 2026-07-31: the original blanket
  restriction on a glamorised reading is lifted **for Shada only**. She is an
  adult character. It does not transfer to anyone else, and Shin's protection is
  absolute and unchanged.)
- Covered head-to-toe in a way that hides the scale language.
- **Rigid armour plates anywhere except the printed forearm gauntlet**, or an
  all-leather costume with no metal on it. The shoulder cap and the thigh patch
  are flexible fields of separate plates; if either reads as hard plate — or as
  leather panels — the design has failed. The connection to her ancestry is lost
  and she becomes a generic scavenger. **The gauntlet is the single exception,
  and it is one object, not a precedent.**
- **Forged, matched or ceremonial scale.** The scales are cut from scrap by hand.
  If they look manufactured as armour, it drifts into the medieval and Roman
  reference the Bible forbids.
- **Scale as texture, in the armour.** Embossed, printed or moulded scale
  pattern standing in for the shoulder cap or the thigh patch is not the same
  thing and is wrong — those are separate pieces of metal. The vest's serpentine
  grain is a different object and is permitted; see Costume above.
- **Printed snakeskin.** A reptile-print leather, a repeating scale motif or any
  decorative pattern on the vest. The grain is in the hide, faint, irregular and
  tonal, or it is not there at all.
- Loaded with gadgets unrelated to infiltration.
- Too dark to separate from the background.
