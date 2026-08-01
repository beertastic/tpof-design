---
title: "Turnaround Block"
asset_id: "PROMPT-TURNAROUND"
version: "1.0"
status: "canonical"
---

# Turnaround Block

Costume turnarounds — **the primary deliverable.** Five images per outfit, per
character.

> Mood and narrative images are context. **Turnarounds are what a costume
> department builds from**, and they should be generated first and in full before
> any atmospheric image is attempted.

---

## A plate is not a board

**Added 2026-08-01, after the first connected-model run came back with two
beautifully composed character sheets and neither was usable.**

A turnaround view is **raw material**. One photograph, one figure, seamless grey,
nothing else. The production boards are assembled from plates like it by
`tools/board-generator/`, and every element a generator adds — a title, a name
plate, material swatches, inset head studies, a scale silhouette, a multi-view
strip — has to be removed before the plate can be used.

Image generators reach for the composed sheet unprompted, because that is what
"character reference" looks like in their training data. **Saying "plain grey
background" is not enough** — the first Baylan attempt had a plain background and
still arrived with a title, a faction block, a height figure, six swatches and a
production logo.

Every turnaround prompt now carries an explicit block forbidding text, layout,
logos, second views, inset heads, detail crops, swatches, palettes and scale
silhouettes by name, high up, before the costume description.

## The face

**If an actor reference exists it is attached and named**, and the prompt says the
face and build are theirs.

**If one does not, the prompt says so** and instructs the model to cast the face
from the written description alone — ordinary, unremarkable, believable, and
explicitly *not* handsome or striking, and not drifting toward any actor it has
seen play a similar part.

The absence has to be stated rather than left silent. A model given no
instruction about the face invents a striking one, and a striking face is the
wrong answer for every character in this film.


## The five images

| # | View | Purpose |
|---|---|---|
| 1 | **Front** | Silhouette, layering, closures, what the eye reads first |
| 2 | **Left side** | Profile, depth, how layers stack |
| 3 | **Right side** | Asymmetry — most real costumes differ side to side |
| 4 | **Back** | The half nobody designs and everybody films |
| 5 | **Natural** | The same costume worn by a person rather than displayed |

Four technical views and one human one. The fifth exists because a turnaround
shows you the garment and tells you nothing about how it moves or sits on a body.

---

## Block F — Turnaround (views 1–4)

> **Full-length costume reference photograph.** The subject stands against a
> plain, seamless, neutral mid-grey studio background, lit evenly and flatly from
> the front with soft even light. No atmosphere, no haze, no mood, no
> environmental context.
>
> **Pose: arms held clearly away from the body**, roughly thirty degrees out, so
> that nothing overlaps and the full silhouette reads. Legs slightly apart. Weight
> even on both feet. Standing straight, facing squarely, head level and looking
> straight ahead. Neutral expression. **This is a costume record, not a
> performance** — no attitude, no character, no acting.
>
> **Framing: the entire figure from the top of the head to below the feet**, with
> a small even margin above and below. Shot from chest height with a long lens so
> there is minimal perspective distortion. The figure is centred and fills the
> frame vertically.
>
> **Every garment, fastening, strap, pocket, seam, buckle and item of equipment
> must be clearly visible and readable.** Nothing obscured by shadow, by pose, or
> by another layer.
>
> **Sharp across the entire frame.** Deep depth of field. No shallow focus, no
> bokeh, no lens flare, no vignetting, no anamorphic character. This is
> documentation, not cinematography.

### Consistency is the whole point

The four views are **the same photograph with the subject rotated.** Everything
else must be identical:

- Same distance, same lens, same camera height, same lighting setup
- Same background, same tone, same exposure
- **Same scale** — the figure occupies exactly the same height in all four frames
- Same costume state — nothing added, removed, opened or adjusted between views

If the figure changes size or the light changes direction between images, the
turnaround is useless. State the view explicitly and change nothing else.

---

## Block G — Natural pose (view 5)

> **Same plain neutral mid-grey background, same even studio lighting, same full
> figure framing** as the turnaround views.
>
> **But the subject now stands as this person actually stands.** Weight on one
> leg, shoulders settled, hands where this character would rest them, head at the
> angle they hold it. A real posture rather than a display position.
>
> Expression is the character's default — the face they wear when nobody is
> asking anything of them.
>
> Still sharp across the frame, still evenly lit, still no environment. **The only
> thing that changes from the turnaround is the human being inside the clothes.**

This image answers what the four technical views cannot: how the costume hangs
when it is not being presented, where it creases, what it does under a real body.

---

## Aspect ratio

**2:3 or 9:16** — tall, full figure. Never square, never landscape.

All five views of an outfit must share the same ratio.

---

## Which blocks apply

| Block | Turnaround views | Why |
|---|---|---|
| **Realism** | **Yes** | It must be a real photograph of real cloth |
| **Anti-synthetic** | **Yes** | There is a face and a body in every frame |
| **Capture** (anamorphic) | **No** | These are documentation, not film frames |
| Style | **Yes** | The costume rules still apply |
| Do Not | **Yes** | The rejections still apply |

The Do Not block's *"framing is imperfect, off-centre, unbalanced headroom"* line
comes from the Anti-synthetic block and **conflicts with turnaround framing.** The
turnaround instruction overrides it: these are centred, square-on and deliberate.
Keep the skin and material realism; drop the compositional looseness.

---

## Naming convention

```
source/artwork/turn-<outfit>-front.png
source/artwork/turn-<outfit>-left.png
source/artwork/turn-<outfit>-right.png
source/artwork/turn-<outfit>-back.png
source/artwork/turn-<outfit>-natural.png
```

Where `<outfit>` is a short lowercase label — `working`, `robe`, `shirtsleeves`,
`jedi`.

---

## Two in-situ images, in two lights

Turnarounds are shot flat and even so the garment is legible. They tell you
nothing about how it behaves in the light the film is actually made in.

**Every character needs at least two in-situ images:**

| | Light | Purpose |
|---|---|---|
| **Daylight** | Bright overcast, open sky, no deep shadow | The costume **readable** in a real environment. Every layer, patch and fitting legible |
| **Low light** | Dusk, night, firelight | The costume as it will actually be **shot**. Silhouette, separation from background, what survives darkness |

They answer different questions and neither substitutes for the other.

A costume that reads beautifully flat-lit can vanish into a night forest, and one
that works in firelight can look flat and characterless in daylight. **You only
find out by looking at both**, and it is much cheaper to find out now.

The daylight image is the reference. The low-light image is the reality check.

## Order of work

1. **All turnarounds, all outfits.** These are the deliverable.
2. **Reference plates** — props, materials, expression range.
3. **Mood images last, and few.** Three or four per character is enough to
   establish tone. They are not what anyone builds from.
