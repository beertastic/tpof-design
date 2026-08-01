---
title: "Key Art Poster Prompt"
asset_id: "PROMPT-KEYART"
version: "1.0"
status: "in-development"
---

# Key Art Poster Prompt

A single self-contained prompt for generating a **series** of poster concepts for
*The Price of Freedom* — for review and to develop ideas from. Paste the block
below into ChatGPT and follow the conversation it sets up.

## What this is for, and what it is not

These images are **exploration**. They are tone, composition and marketing ideas.
They are **never** costume authority, never a board asset, and nothing is ever
matched against them. Do not put a poster render into any `source/artwork/`
folder and do not point `board-data.yaml` at one.

That distinction matters here more than usual, because poster work deliberately
breaks two standing house rules:

- The mood and turnaround prompts say *"not a composed poster"* and *"framing is
  imperfect"*. Key art is the exception — it is composed, balanced and deliberate.
- The mood prompts demand attached reference and refuse to generate without it.
  This pack runs **without** reference on purpose, so ideas can be explored before
  anyone is cast or a costume is built. The cost is that faces and costumes will
  be wrong. That is accepted, and it is why nothing here is authority.

## How to use it

1. Paste the whole block below into a fresh ChatGPT conversation.
2. It will come back with a written list of poster concepts. **Read them first.**
   Kill the bad ones, ask for more of whatever direction looks right. This is the
   cheap part of the process — spend time here.
3. Then have it generate approved concepts **one image per turn**. Do not ask for
   a grid of eight; you get eight bad thumbnails instead of one good poster.
4. Keep what works in `10-assets/`, with a note saying which concept it came from.

**No text in any image.** Every poster leaves clean, uncluttered space for a title
treatment that gets designed properly, in a layout tool, by a person. Generators
still produce mangled lettering, and a title lockup is a design job, not a
prompting job.

**Do not name existing Star Wars characters, actors or species in follow-up
notes.** The lesson from the mercenary pack holds: naming retrieves that
character. Describe the person you want instead.

---

## The prompt — paste everything below this line

```text
You are an art director producing a series of KEY ART POSTER CONCEPTS for a
Star Wars fan film called THE PRICE OF FREEDOM. I want ideas and directions to
review, not finished deliverables.

=== HOW WE WILL WORK ===

STEP 1 — CONCEPTS FIRST, IN WRITING. Do not generate any image yet.
Read the brief below and reply with TWELVE poster concepts as text. For each:
  - a one-line hook (what the poster is about in plain words)
  - the image described in two or three sentences
  - the aspect ratio
  - where the title treatment would sit
  - what it is selling — dread, scale, a character, a relationship, a threat
Range widely. Some obvious, some strange. Include at least two that a normal
Star Wars poster would never do. Number them. Then stop and wait.

STEP 2 — I will approve, cut and redirect. Expect to be told no.

STEP 3 — GENERATE ONE POSTER PER TURN, only when I name the concept. One
image, full attention, at the stated ratio. Never a grid, never a contact
sheet, never four variations in one frame.

STEP 4 — After each image, tell me in two lines what you would push further and
what you think failed. Then wait.

=== STATUS OF THESE IMAGES ===

These are exploration. They are not costume references and not canon. Faces,
costumes and hardware will be wrong and that is accepted at this stage. Do not
claim accuracy. Do not reproduce any recognisable existing Star Wars character,
creature or actor likeness — everyone here is an original character, and if a
description starts pulling you toward a famous face, go the other way.

=== THE FILM ===

An escaped group of slaves is hunted across a forested world by a mercenary crew
hired to bring them back. It is a chase, on foot, over roughly one day and night.
The escapees are exhausted, injured and under-equipped. The mercenaries are
professionals doing a job — competent, unhurried, not evil, which is worse.
Almost nobody gets away.

Hiding among the mercenaries is a man who was a Jedi eighteen years ago and gave
it up. He is fifty, heavy, slow, and has worked hard to be uninteresting. Nobody
in the crew knows what he is. Choosing to act costs him the only safety he has
had since the purge, and the friend he kills to get it.

The film is the origin of a fifteen-year-old girl. Her mother dies in the last
scene, mid-sentence, in the middle of telling her not to let fear control her.
The girl is frightened in nearly every scene and never masters it. Her fear is
the subject of the film, not a character note.

The world is never named. These people are nowhere, and that suits the story.

Tone: no triumph, no heroism, no rescue. This is a story about people being
hunted through trees, and the price of getting out.

=== THE PEOPLE (describe, never name a lookalike) ===

- THE HIDDEN JEDI. Human man, fifty. Tall and broad, thickened, powerful once
  and merely large now. Iron-grey hair cut badly by his own hand, full unshaped
  beard, deep lines from years of not sleeping. Plain repaired mercenary workwear
  with no ornament at all, in a crew that decorates itself. A long weathered dark
  coat that reads as weather gear, never as robes. No visible lightsaber, ever.
- THE GIRL. Fifteen. Small, exhausted, filthy, visibly afraid. Not a warrior yet
  and nothing about her may suggest she is becoming one.
- HER MOTHER. Injured during the escape, moving badly, still putting herself
  between her daughter and everything else.
- THE ARENA FIGHTER. A woman who was captured and made to fight. Scarred,
  capable, the only escapee who can actually fight back.
- THE MEDIC. Under-supplied and out of his depth, treating serious injuries with
  almost nothing.
- THE MERCENARY CAPTAIN. Field commander, calm, unhurried, keeps a large
  predatory beast on a line — heavy, thick-hided, dog-like but wrong.
- THE INFILTRATOR. Compact woman, a tracker and scout. Dangerous through
  observation and timing rather than size.
- THE FRIEND. A mercenary, decent within the terms of his job, who dies at the
  hidden Jedi's hands.

=== THE WORLD ===

Live-action Star Wars in the manner of the original trilogy and Andor, with a
frontier edge. Photographic, never illustrative.

A galaxy built from industrial salvage. Nothing is factory fresh. Everything has
had a previous owner and carries visible history — repairs, scratches, faded
paint, replaced parts, grime, evidence of servicing. People repair rather than
replace.

Costume is functional workwear first, buildable, with believable seams and
fastenings. No floating armour, nothing purely decorative. Ballistic weave,
quilted flight fabric, worn synth-leather, armour mesh, plastoid plate,
industrial rubber, brushed alloy.

Palette muted, sun-faded, practical — charcoal, ash grey, weathered black, faded
olive, dust brown, sand, bone white. Brass and oxidised bronze sparingly. Bright
colour only for rank, warning markings, or one significant personal object.

Locations: dense wet temperate forest, a mercenary camp of tents and tarpaulins
and crates, a ragged escapee camp with no fire, a ditch, a clearing where it
ends. One sequence elsewhere entirely — pale sand dunes under a hard sky, seen in
a vision. A single mercenary ship, salvaged and repaired, seen coming down
through the sky at the start.

Light is motivated and it costs something: overcast daylight through canopy,
firelight, work lamps, a glowrod, ship landing lights, torch beams in trees.

=== POSTER CRAFT ===

This is the one place the production's usual rules relax. Key art IS composed:
deliberate, balanced, built to read at a distance and survive being shrunk to a
thumbnail. But it is composed from PHOTOGRAPHY, not illustration.

- ONE IDEA PER POSTER. If it needs a sentence to explain, it has failed.
- Read the silhouette first. Squint at it — the shape must still work.
- Depth in clear layers: foreground, subject, and a background that carries scale.
- Negative space is a tool. Empty sky, fog, dark forest, a bare dune. Use it.
- Composition may be strong and unusual — extreme scale contrast, a figure tiny
  against something vast, hard symmetry, a single object dead centre, deep
  negative space, heavy silhouette against light.
- Restrained, filmic grade. Anamorphic character — oval bokeh, gentle barrel
  distortion, soft frame edges, restrained horizontal flare, fine 35mm grain,
  halation around bright sources, highlight rolloff that compresses rather than
  clips, shadow that keeps detail. No teal-and-orange. No digital vibrance.
- Skin is real: pores, uneven tone, lines, blemishes, stubble, shine where skin is
  oily. Faces asymmetric. No smoothing, no beauty retouching, no waxy plastic.

=== TITLE SPACE — MANDATORY ===

NO TEXT ANYWHERE IN THE IMAGE. No title, no tagline, no credit block, no billing,
no logo, no watermark, no signature, no lettering of any kind — not even blurred
or suggested text.

Every poster must leave a clean, quiet band with room for a title treatment to be
added later. State in your reply where you left it. Nothing important — no face,
no hand, no key silhouette edge — may sit in that band.

=== DO NOT ===

No Earth pirate costume, tricorns, pirate coats, corsets, Renaissance, medieval
or fantasy clothing, fantasy shoulder pads, swashbuckler dress, Roman armour, or
modern tactical/SWAT gear.

No pristine futuristic minimalism, no factory-fresh or polished surfaces, no
ceremonial gear, no oversized or stylised weapons, no glowing decorative
technology, no gadget overload.

No visible lightsaber and no lightsaber glow in any poster. If the Force is
present it is present as weather, stillness or dread — never as a lit blade.

No glamour posing, no sexualisation, no fashion-editorial lighting, no
chin-up heroic hero shots, no team line-up standing in a row looking at camera
unless a concept specifically calls for it and subverts it.

No floating-heads montage, no orange-and-blue collage, no radial composition
with a big face in the sky, no Photoshop-comp look. If it resembles a modern
streaming key art template, it has failed.

No anime, cel shading, painterly illustration, 3D-render look, digital-painting
brushwork or concept-art finish. No crushed blacks — silhouettes must stay
separated from the background.

Nothing symmetrical, new or clean unless the concept says so.

=== THE STARTING SLOTS ===

Include these eight among your twelve, then invent four more of your own.

1. THE TEASER. Almost nothing. Forest, fog, scale, dread, and the smallest
   possible human presence. Sells the situation, not the cast. 2:3.
2. THE HUNT. Torch beams through wet trees at night, seen from the position of
   the hunted. The hunters are shapes, not faces. 2:3.
3. THE HIDDEN MAN. The Jedi who is not one, alone, plain, entirely
   uninteresting, in a frame that quietly refuses to let you look away. 2:3.
4. THE GIRL. A fifteen-year-old who is afraid, photographed without pity and
   without heroism. Nothing in it may suggest she is about to become powerful. 2:3.
5. THE BEAST. The captain's animal on its line, and the man holding it. The
   creature carries the frame. 2:3.
6. THE ARRIVAL. The mercenary ship coming down through evening sky over forest,
   with the world at full scale beneath it. Landscape, 16:9.
7. THE CLEARING. The ensemble in the last location, staged so the outcome is
   already legible. Landscape quad format, 4:3.
8. THE VISION. Pale sand dunes under a hard sky, a robed figure at distance,
   the whole thing wrong in a way that is hard to name. No recognisable face —
   the figure is a shape and a shadow. 2:3.

=== DELIVERY ===

Now do STEP 1. Twelve concepts, in writing, no images. Then stop.
```

---

## Notes for whoever runs this

**Twelve concepts is deliberate.** Roughly three will be good. Cutting nine is the
work, and it is much cheaper to cut a sentence than an image.

**Expect the coat to become robes.** Every generation of the hidden Jedi drifts
toward monastic sleeves and a raised hood. Push back with the specific words — a
weathered heavy coat, a working man's weather gear — rather than repeating "not
Jedi robes", which supplies the idea you are trying to remove.

**Expect the title band to fill up.** Generators dislike empty space and will put
a branch, a flare or a shoulder in it. Ask for the band again by name.

**If a concept survives review,** it should end up as a proper prompt slot with
the full Capture and Photographic Realism blocks inlined, following
[`Global-Style-Block.md`](Global-Style-Block.md) and
[`Capture-Block.md`](Capture-Block.md) — not left as a paste from this
exploration.
