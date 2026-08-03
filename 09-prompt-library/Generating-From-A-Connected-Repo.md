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

**Superseded twice on 2026-08-01. Read the section above first — the headline is that a connected model can fetch the images, and still cannot deliver the prompt.**

**It fetches the images.** This document previously
said a connector reads only text and that photographs had to be attached by hand.
That was wrong, and the reason the earlier attempts failed was much more boring —
the actor file was called `Tristan Pretty.jpg`, and a space makes a raw URL fail
as a connection error rather than a 404, which looks exactly like having no access.

Renamed, it opens. A model fetched it from its public URL and described the hair,
the beard, the shirt and the background blur accurately.

So every reference in every prompt now carries a full public URL and the model is
told to fetch it. **Attaching by hand still works and remains the fallback**, but
it is no longer the expected route.

It also introduces a new failure, and a worse one: **a connected model will
summarise the prompt instead of using it.** The instruction below exists mostly to
stop that.

---

## The one thing to understand before anything else

**A connected model cannot hand your prompt to the image generator.** Everything
else on this page is downstream of that, and not knowing it cost a full day on
2026-08-01.

The image generator is a separate system with its own short input field. It has
no repository access. Whatever reaches it, ChatGPT typed.

So there are two routes, and they are not variations on a theme — they are
different pipelines with different inputs:

**You paste the prompt.** The text is in the conversation. ChatGPT forwards it to
the generator more or less intact, because it is right there and relaying costs
nothing. This works.

**ChatGPT fetches the prompt.** Your file arrives as a *tool result* — as source
material. ChatGPT reads it, forms an impression, and writes a new brief for the
generator. **Your document never arrives.** The generator sees a paraphrase.

### Why this is so hard to believe

Because the failures do not look like failures. They look like work.

Asked for Baylan's front turnaround, a connected run read the repo — the sources
badge proved it — spent two minutes, and returned a handsome design board headed
**THE PATHS OF FATE**. This film is called *The Price of Freedom*. The board also
carried "Former Jedi", "pensive wanderer", "No rank insignia" and "Stands with
quiet confidence". **None of those five phrases exists anywhere in this
repository.**

It was not defying the prompt. It had never seen the prompt. It read the
character documents, understood the assignment, and wrote its own brief — which
is exactly what a helpful assistant does when handed background reading and asked
for a picture.

**The maddening part is real and worth naming:** the same file, publicly readable,
produces a good plate when pasted and an invention when fetched. That is not
inconsistency. It is two different documents reaching the generator, one of which
is yours.

### The consequence

**Split the work by what each side is actually able to do.**

| Do this with the connector | Do this by hand |
|---|---|
| Read the repo, check the approval gate | **Paste the prompt for every image** |
| Quote the commit id and prompt hash | |
| Fetch reference photographs | |
| Commit accepted images, edit `outfits.yaml` | |
| Answer design questions | |

That is not a workaround pending a fix. It is the correct shape, because the
constraint is architectural.

**How to tell instantly which route a run took.** Every prompt file's line 4
carries a commit id and a content hash, and the file instructs the model to say
them back before generating:

> Working from commit `ddc2d15`, prompt `5e85b186`.

Neither is guessable. **No line, no image** — if a reply starts generating without
it, it is working from its own brief and the result will be invention.

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

I have ATTACHED the reference images by hand — the actor, and the
plates the prompt names in its operator lines. Do not try to fetch
those from the repo: a repo connector reads text and will not put an
image in front of the generator. Use the attached ones.

Tell me which attached images you can actually see before you start.

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
./tools/regen shada
```

That is the whole step: all three generators, then commit and push. It exists
because "regenerate, commit, push" is a description of a step rather than a step,
and because a hand-typed list of generators tends to omit `short.py` — which is
the one that writes what you paste.

---

## Never ask for a "reference image"

**Added 2026-08-01.** The phrase names a genre — a multi-panel character design
board with a name banner, a portrait strip and colour swatches. Ask for one and
you will get one, however long the prompt arguing otherwise. It happened, and it
captioned itself `REFERENCE IMAGE`.

Ask for a **front turnaround**, or a **costume fitting photograph**. Both are
what a costume department actually calls the thing, and neither retrieves a
layout. `reference` is fine for an input you fetch and match against; it is never
the name of what you are making. See [`AGENTS.md`](../AGENTS.md).

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

## Why access is inconsistent

**Diagnosed 2026-08-01, partly by the connected model itself when asked.** There
is not one access mechanism, there are several, and they fail differently:

| Route | Behaviour |
|---|---|
| **Public raw fetch** — `raw.githubusercontent.com` | The most predictable for a known path, and **measured current within seconds** on 2026-08-01: a commit pushed at 17:20 local was being served by raw immediately after. Do not blame this layer first |
| **GitHub connector** | Subject to auth expiry, branch and permission scope, and whether the connector was selected for that particular operation. Its index can lag `main` |
| **Ordinary web search** | Does not reliably index raw files or recent commits. A failed search is not proof the repo is unreachable |
| **Conversation cache** | **The one that actually bites.** A previous turn's fetch is reused for the rest of the chat. A read earlier in the conversation is not evidence of current state |

**Measured 2026-08-01, and it corrected a wrong guess of mine.** A model reported
`REPO-STATE.md` stamped 15:28 UTC while `raw.githubusercontent.com` was serving
16:20 UTC — checked by hand, at the same moment, with `curl`. GitHub was current.
The 52-minute-old copy was the conversation's own.

So *"wait for the CDN to catch up"* is bad advice and I gave it. **The fix is a
fresh chat, immediately** — there is nothing to wait for, and waiting in the same
conversation changes nothing however long you leave it.

Two more that look like access failures and are not:

- **Case.** `03-characters/Shada/` fails where `03-characters/shada/` succeeds.
  A capitalised path returns nothing, which is indistinguishable from having no
  access.
- **Unpushed work.** The model sees `origin/main`. Local commits are invisible,
  and both parties can honestly believe they are looking at "the repo".

### The test that settles it

**Every image-related reply must show the `REPO-STATE.md` stamp, and — whenever a
prompt is used — that file's exact path and character count.** Missing either is
evidence the live file was not demonstrably read.

This works. On 2026-08-01 a model reported `AGENTS.md` at 11,969 characters when
the file on `main` was 12,031, and the stamp it quoted was half an hour old. The
count exposed a stale read that the prose around it did not.

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
