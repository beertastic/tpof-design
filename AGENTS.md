# Instructions for AI agents with access to this repository

**Read this before generating anything.**

## Step 0 — always, before anything else

**Read [`REPO-STATE.md`](REPO-STATE.md) and tell the user the stamp date it
carries.** One line, at the top of your reply, every time:

> Repo state: stamped `<date>`.

That file is rewritten automatically on every commit, so its date is the date of
the most recent change. **If the user says it is older than they expect, you are
reading cached content.** Say so and stop — do not generate from stale files.
Nothing in this repository can force you to refetch; only the user starting a
fresh conversation reliably clears it.

**Also state what you actually read.** When you open a prompt file, say its path
and its length. A model that has silently fallen back on memory cannot do that,
and the user needs to be able to tell the difference.

This file defines the commands a connected model should understand and the checks
it must run before acting. Human background is in
[`09-prompt-library/Generating-From-A-Connected-Repo.md`](09-prompt-library/Generating-From-A-Connected-Repo.md).

---

## If you cannot read this repository

**Say so immediately and offer the fallback. Do not refuse and stop.**

Everything here is designed to work without repository access — the prompt files
are deliberately self-contained, and that is the fallback. If your file reads are
failing or unavailable, say:

> I can't read the repository from here. Paste the contents of
> `03-characters/<character>/prompts/turnarounds/turn-<outfit>-front.txt` and
> attach the reference images named in its operator lines, and I'll work from
> that.

Then follow every other rule below exactly as written. The only thing lost is
that the user has to fetch the files by hand.

**Paths in this repository are lower-case and hyphenated, and GitHub is
case-sensitive.** `03-characters/shada/`, never `03-characters/Shada/`. A
capitalised path returns nothing, which is easily mistaken for having no access
at all.

---

## The rules that apply to everything

**1. The prompt files ARE the prompts. Use them verbatim.**
Never summarise, shorten, paraphrase or extract "key points" from a prompt file.
They run to 30,000+ characters on purpose — every `NON-NEGOTIABLE` item exists
because a previous generation got that thing wrong. A compressed version produces
a plausible, wrong image.

**2. Never generate from `Character.md`.**
Those are written for humans and are the wrong shape to generate from. Only files
under `prompts/` are prompts.

**3. You are the operator.**
Prompt files contain lines like
`[for the operator, not the model: also attach <path>]`.
Fetch every one of those from the repo and use it as a reference image.

**4. Read the non-negotiables back before generating.**
List them, one line each. If you cannot, you did not read the file properly —
stop and read it again.

**5. Self-check after generating.**
Go through each `NON-NEGOTIABLE` item against the image you produced and say which
you are confident about and which you are not. Be honest about the doubtful ones;
that list is what the Production Designer uses to decide whether to keep it.

**6. Never save an image until the user approves it.**
You may have write access. Do not use it on a generation the user has not accepted.
Rejected images must not reach `source/artwork/`.

**7. One image per turn.**
Never a grid, a contact sheet, or four variations in one frame.

**8. The output filename is on line 2 of every prompt file.** Use it exactly.

---

## Command — "make the reference picture for `<character>`"

Also: *"make `<character>`'s reference"*, *"generate the front turnaround"*.

This produces the **front turnaround**, which is the image every other image of
that costume is matched against.

### Step 1 — the reference gate. Run this FIRST, every time.

Read `03-characters/<character>/outfits.yaml`. **That file is the only authority
on how many outfits a character has.** Do not answer from `README.md`, from
`Character.md`, from the status board or from anything you remember — those are
prose and they go stale. If `outfits.yaml` lists one outfit, there is one
outfit.

- If `outfits.yaml` lists more than one and the user did not say which, **ask**.
- Look for `approved.reference` on that outfit, and check whether the file exists.

**If an approved reference EXISTS — stop and ask before doing anything else.**
Show the image and say, filling in the real numbers:

> **`<character>` already has an approved reference for the `<outfit>` costume**,
> approved `<date>`.
>
> *[show `<approved.reference>`]*
>
> **`<N>` other images are matched against this one.** Replacing it means
> re-approving it in `outfits.yaml` and then regenerating all `<N>` so they match
> the new one.
>
> Do you want to preview a replacement?

`<N>` is the number of `.txt` files under `prompts/` and `prompts/turnarounds/`
for that character, minus the front view itself.

**Only continue if the user says yes.** If they do, treat the result as a
*preview* — do not overwrite the existing approved image, and do not touch
`outfits.yaml`.

**If no approved reference exists**, say so briefly and continue.

### Step 2 — generate

1. Read `03-characters/<character>/prompts/turnarounds/turn-<outfit>-front.txt`.
2. Fetch every file named in an operator line.
3. Fetch the actor reference from `03-characters/<character>/reference/actor/`
   if one exists, and use it for face and build.
4. Read the non-negotiables back.
5. Generate one image at the aspect ratio in the file header.
6. Self-check.

**The front view is the only image generated without a costume reference**,
because it is the one that creates it. The prompt says so itself. Do not go
looking for a costume reference to attach — the plates and the actor photo are
all there is.

### Step 3 — after the user approves

Save to `03-characters/<character>/source/artwork/<filename from line 2>`, then
tell the user to record it:

```yaml
# outfits.yaml, on that outfit
approved:
  date: "<today>"
  view: front
  reference: 03-characters/<character>/source/artwork/turn-<outfit>-front.png
```

You may make that edit if asked. **Say clearly that the prompt files must then be
regenerated and pushed** — you cannot run the generators yourself:

```bash
python tools/prompt-splitter/turnarounds.py <character>
python tools/prompt-splitter/split.py <character>
```

---

## Command — "make all `<character>` images from the reference"

### Step 1 — require a reference

Read `outfits.yaml`. **If there is no `approved.reference`, or the file is
missing, stop.** Say:

> `<character>` has no approved reference image yet. Everything else is matched
> against it, so that has to come first. Shall I make the reference picture?

Do not offer to generate the other images anyway.

### Step 2 — assemble the reference set, once

- The approved costume reference — `approved.reference`
- Every plate under `references:` in `outfits.yaml`
- The actor reference from `reference/actor/`

State which ones you have fetched before starting.

### Step 3 — work through the list, one image per turn

In this order:

1. The remaining turnaround views — left, right, back, natural.
2. The numbered slots in `prompts/`, in order.

For each: read the file verbatim, read back its non-negotiables, generate,
self-check, and wait for the user to accept or reject before moving on.

**Do not batch. Do not say "same again but…"** — that makes the model work from
its own last output instead of the reference, and the costume drifts.

---

## Before generating anything, check the prompts are current

The prompt files are **generated** from `outfits.yaml` and `Prompts.md`. If those
sources have been edited since, the prompts are stale and you will produce the
previous version of the costume.

You cannot run the generators. If the sources look newer, say so and ask the user
to run the two commands above and push.

**You read what is committed, not what is on their disk.** Unpushed work is
invisible to you — say so rather than assuming you have the latest.

---

## Judge against the watch-list

Characters with a history of specific failures have one recorded. Shada's is in
[`11-production-tracking/Shada-Image-TODO.md`](11-production-tracking/Shada-Image-TODO.md)
under *Watch for*: metal on both forearms, caps on both shoulders, matching
patches, a modern coil zip, the blaster on her left.

**Two or more of those in one image almost always means the references were not
used.** Say so and regenerate rather than defending the image.

---

## What not to do

- Do not invent design detail that is not in the prompt. If something is
  unspecified, say it is unspecified.
- Do not name real Star Wars characters, actors or species in follow-ups —
  naming retrieves that character. Describe instead. This is a recorded lesson;
  see the mercenary pack's history.
- Do not edit anything under `prompts/` by hand. It is all generated, and hand
  edits are silently destroyed on the next run.
- Do not commit rendered screenplay PDFs, board renders, or rejected images.
  See `.gitignore`.
