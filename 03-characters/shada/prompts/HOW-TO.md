# Generating Shada — the actual procedure

> **If ChatGPT is connected to the repository, use
> [`09-prompt-library/Generating-From-A-Connected-Repo.md`](../../../09-prompt-library/Generating-From-A-Connected-Repo.md)
> instead.** It fetches its own reference plates, which removes the failure this
> document is mostly about. What follows is the paste-by-hand procedure.

The single most common failure is generating **without the reference photographs
attached**. The result looks plausible and is the wrong costume, the wrong face
and often the wrong location. Every prompt now refuses to proceed if nothing is
attached — but only if you paste the whole thing.

## Setup — once per session

1. **Start a new conversation.** Old ones carry earlier costume versions and will
   blend them.
2. **Attach both reference photographs before anything else:**
   - `03-characters/shada/source/artwork/turn-working-front.png` — the approved costume
   - `03-characters/shada/reference/actor/dasha-svistunenko-heashot.jpg` — the actor
3. Say: *"These are the approved costume and actor references for this character.
   Match them exactly in everything that follows."*

## Then, per image

4. Open the prompt file **from `prompts/turnarounds-short/`, not
   `prompts/turnarounds/`**. Image models accept about 4,000 characters and the
   long files are 28,000 — anything past the limit is compressed by the host
   before the generator sees it, which is why identical files gave different
   costumes. The long files are the specification; read them, never paste them.
5. **Select all. Paste.** Do not trim the top — the check lives there.
6. Save the result to `source/artwork/` using the exact filename in the header.

**Do not** say "same again but in the forest." That is how the model starts
working from its own last output instead of your reference.

## If the costume comes back wrong

Check in this order:

1. **Were images actually attached to this conversation?** Not a previous one.
   This is the cause about nine times in ten.
2. **Did you paste the whole prompt**, including the check at the top?
3. **Is it a fresh conversation?** An older one may hold a superseded costume.
4. Re-attach the approved front turnaround and say: *"Match the attached costume exactly.
   The previous image was wrong."*

## What "wrong" looks like

The failure that keeps recurring for this character:

| Wrong | Right |
|---|---|
| Scale armour on both arms and both shoulders | **Three patches only** — her right forearm, her left shoulder, her left thigh |
| All three patches the same metal | **Three different metals** — dull grey steel, brass with verdigris, dark bronze. Three scavenging trips |
| Any metal on the torso | Her chest, sternum and back are plain cloth. No chest patch, no bib, no pendant, no breastplate |
| Bulky or loose | Close-fitting, cut to the figure |
| Ship interior | She is never on a ship. Forest and camp only |

If two or more of those appear, the reference was not attached.
