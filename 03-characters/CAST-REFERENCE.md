# Cast Reference Convention

Where actor reference images live, and how to use them.

## Location

```
03-characters/<character>/reference/actor/
```

One folder per character. Committed to the repository — these are irreplaceable
production inputs, like `source/artwork/`, not regenerable output.

## Before you put anything here

**These are real people's likenesses.**

- **Get written consent** from the performer covering use as design reference,
  including use with image-generation tools. Say so explicitly — "reference" and
  "training an AI on my face" are not the same permission, and performers are
  increasingly and reasonably careful about the difference.
- Record that consent somewhere durable. A line in this repository is not a
  release form.
- If this repository is ever made public or shared beyond the production, **these
  images are the first thing to reconsider.** Everything else here is text about
  fictional people; this is photographs of real ones.

If consent for AI use is not given, the character can still be designed — the
prompt packs are written to work from description alone, as Shada's did.

## Filenames

**No spaces.** A space makes the raw URL fail as a connection error rather than a
404, which is indistinguishable from having no repository access at all. It cost
an afternoon on 2026-08-01, and the generators now warn about it on every run.

The names below are preferred because the prompt can then say *what angle each
reference is* rather than just numbering it. Anything else still works — the
prompts number every file they find, in sorted order, and emit a fetchable public
URL for each.

## What to put here

| Filename | What |
|---|---|
| `headshot-neutral.jpg` | Front on, neutral expression, even light |
| `headshot-profile.jpg` | Full side profile |
| `headshot-three-quarter.jpg` | The most useful working angle |
| `full-body.jpg` | Standing, whole figure, for build and proportion |
| `expression-*.jpg` | Range, if available |
| `in-costume-*.jpg` | Once costume exists |

Even light, plain background, no heavy styling or makeup. These are references,
not publicity shots — a well-lit neutral headshot is worth more than a good
photograph.

## Using them with an image generator

**Attach them to the conversation.** Do not assume a repository connector lets the
model *see* images — many expose file contents as text, which makes a JPEG
useless. If generated faces come back generic or inconsistent, that is the first
thing to check.

Practical order for each prompt:

1. Attach the actor reference images.
2. Paste **Style** + **Do Not** + **Character Constants** from the character's
   `Prompts.md`.
3. Paste **one** numbered slot.
4. State the aspect ratio the slot specifies.

The reference governs the face and build. The prompt pack governs everything
else — costume, lighting, behaviour, framing, and what to avoid.

## Where they must not end up

Actor reference is an **input**. It does not go into `source/artwork/`, it is
never placed on a production board, and it is not a design document. Nothing in
`board-data.yaml` should ever point at this folder.
