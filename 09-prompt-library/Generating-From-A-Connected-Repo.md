---
title: "Generating From A Connected Repo"
asset_id: "PROMPT-CONNECTED-REPO"
version: "1.0"
status: "canonical"
---

# Generating From A Connected Repo

> **The machine-readable version of this is [`AGENTS.md`](../AGENTS.md) at the
> repository root.** Point the model at that; this document is the reasoning
> behind it, for humans.

**For when ChatGPT has read access to this repository**, rather than being pasted
into by hand. Added 2026-08-01.

The prompt packs were built to be self-contained so they could be pasted into any
tool with no repository access. That still works and is still the fallback. But a
connected model can read the prompt *and* fetch its own reference plates, which
removes the failure that causes nine faults in ten — the operator forgetting to
attach something.

It introduces one new failure in its place, and it is worse: **a connected model
will summarise the prompt instead of using it.** The instruction below exists
mostly to stop that.

---

## The instruction

Substitute the character and the view. Everything else stays.

```
Read this file from the repo:

  03-characters/shada/prompts/turnarounds/turn-working-front.txt

THAT FILE IS THE PROMPT. Use it verbatim as the image generation
instruction. Do not summarise it, shorten it, paraphrase it, or pull
"key points" out of it. It is long on purpose — every NON-NEGOTIABLE
item in it is there because a previous generation got it wrong.

The file contains lines like:
  [for the operator, not the model: also attach <path>]
You are the operator now. Fetch each of those files from the repo and
use them as reference images.

Also fetch and use as the face and build reference:
  03-characters/shada/reference/actor/dasha-svistunenko-heashot.jpg

Before you generate anything, list the NON-NEGOTIABLE items back to me,
one line each, so I can see you actually have them.

Then generate ONE image at the aspect ratio given in the file header.

After generating, check your own image against each NON-NEGOTIABLE item
and tell me which ones you are confident you hit and which you are not
sure about. Be honest about the ones you are not sure about — that list
is what I use to decide whether to keep it.
```

**Do not** ask it to "read the character document and make an image". The prompt
files exist because `Character.md` is written for humans and is the wrong length
and shape to generate from.

---

## Before you start

**Push first.** A connected model reads what is committed, not what is on your
disk. If the prompts have been regenerated locally and not pushed, it will use
the old ones — which is exactly the stale-copy failure the old workflow had, in a
new place.

```bash
python tools/prompt-splitter/turnarounds.py shada
python tools/prompt-splitter/split.py shada
git add -A && git commit -m "prompts(shada): regenerate" && git push
```

---

## The front view is the special one

**It is the only image generated without a costume reference, because it is the
image that creates the reference.**

The prompt says so itself:

> THIS IS THE FIRST IMAGE OF THIS COSTUME. THERE IS NO REFERENCE YET.
> Build it from the description below, which is the only source.
>
> Once approved, THIS IMAGE BECOMES THE REFERENCE that every other view of this
> costume is matched against. An error here propagates into all of them, so it is
> worth several attempts to get right.

So for the front view, the only images to fetch are the **plate references** named
in the operator lines, and the **actor reference**. There is no approved costume
image to attach yet — that is what you are making.

**Every other view, and every mood image, is different.** Those must also get the
approved front turnaround attached, and their prompts refuse to run without it.

### After it is approved

Record it, or nothing else will match against it:

```yaml
# outfits.yaml
approved:
  date: "YYYY-MM-DD"
  view: front
  reference: 03-characters/<character>/source/artwork/turn-<outfit>-front.png
```

Then regenerate and push, so the connected model can see the new reference.

---

## What will go wrong

**It summarises the prompt.** By far the most likely failure. The Shada front
prompt is 34,000 characters with eight numbered non-negotiables; a model asked to
"use this file" will happily compress it to a paragraph and generate something
plausible and wrong. The read-back step is there to catch it — **if it cannot list
the non-negotiables, it did not use the file.**

**It generates without fetching the reference plates.** The operator lines are
addressed to a human and a model may skip them. Check its read-back mentions the
plates.

**It refuses the actor photograph.** Image generators often will not reproduce a
real person's likeness from a photo. If it refuses, fall back to generating from
the written description and accept that the face is indicative — the costume is
what the turnaround is for. Do not let it substitute a generic face and call it
matched.

**It writes the image to the wrong path.** The filename is in the second line of
every prompt file. If the model has write access, tell it that path explicitly.

---

## Judge the result against the watch-list, not your memory

Every character with a history of failures has one. Shada's is in
[`11-production-tracking/Shada-Image-TODO.md`](../11-production-tracking/Shada-Image-TODO.md)
under *Watch for*, and it is specific: metal on both forearms, caps on both
shoulders, matching patches, a modern coil zip, the blaster on her left.

**Two or more of those in one image almost always means the references were not
used.** Regenerate rather than argue with it.
