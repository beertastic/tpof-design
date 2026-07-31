# Generating Shada — the actual procedure

The single most common failure is generating **without the reference images
attached**. The result looks plausible and is the wrong costume, the wrong face
and often the wrong location. Every prompt now refuses to proceed if nothing is
attached — but only if you paste the whole thing.

## Setup — once per session

1. **Start a new conversation.** Old ones carry earlier costume versions and will
   blend them.
2. **Attach both reference images before anything else:**
   - `03-characters/shada/source/artwork/turn-working-front.png` — the approved costume
   - `03-characters/shada/reference/actor/dasha-svistunenko-heashot.jpg` — the actor
3. Say: *"These are the approved costume and actor references for this character.
   Match them exactly in everything that follows."*

## Then, per image

4. Open the prompt file. **Select all. Paste.** Do not trim the top — the check
   lives there.
5. Save the result to `source/artwork/` using the exact filename in the header.

**Do not** say "same again but in the forest." That is how the model starts
working from its own last output instead of your reference.

## If the costume comes back wrong

Check in this order:

1. **Were images actually attached to this conversation?** Not a previous one.
   This is the cause about nine times in ten.
2. **Did you paste the whole prompt**, including the check at the top?
3. **Is it a fresh conversation?** An older one may hold a superseded costume.
4. Re-attach the approved reference and say: *"Match the attached costume exactly.
   The previous image was wrong."*

## What "wrong" looks like

The failure that keeps recurring for this character:

| Wrong | Right |
|---|---|
| Scale armour on both arms and both shoulders | **Four patches only** — one gauntlet, one shoulder, sternum, one thigh |
| All four patches the same metal | **Four different metals**, four scavenging trips |
| Full scale breastplate | A patch stitched flat at the sternum |
| Bulky or loose | Close-fitting, cut to the figure |
| Ship interior | She is never on a ship. Forest and camp only |

If two or more of those appear, the reference was not attached.
