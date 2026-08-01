# Instructions for AI agents with access to this repository

**Read this before generating anything.**

## Step 0 — always, before anything else

**Read [`REPO-STATE.md`](REPO-STATE.md) and tell the user the stamp date it
carries.** One line, **in your reply text**, every time:

> Repo state: stamped `<date>`.

**In the TEXT of your message. Never inside an image.** A run on 2026-08-01 read
this instruction and rendered `REPO-STATE STAMP 2025-08-01` as a caption on the
artwork. Nothing you are asked to confirm here ever belongs in a generated
image — see the plate rules below.

That file is rewritten automatically on every commit, so its date is the date of
the most recent change. **If the user says it is older than they expect, you are
reading cached content.** Say so and stop — do not generate from stale files.
Nothing in this repository can force you to refetch; only the user starting a
fresh conversation reliably clears it.

**Also state what you actually read.** When you open a prompt file, quote its
`Prompt version:` line — the eight-character hash on line 4. That is the exact
check: it changes whenever the prompt changes and never otherwise.

**Do not rely on character counts.** A model reported 28,195 characters for a file
that has never been that size at any commit, because it counts its own
post-processed text rather than raw bytes. The hash has no such ambiguity.

This file defines the commands a connected model should understand and the checks
it must run before acting. Human background is in
[`09-prompt-library/Generating-From-A-Connected-Repo.md`](09-prompt-library/Generating-From-A-Connected-Repo.md).

---

## The sequence that actually works

**Established 2026-08-01 after a long afternoon of failures.** Three things have
to be true at once, and any one of them missing produced a confident, wrong,
handsome character sheet:

1. **A reasoning tier.** `High` has read this repository reliably. `Instant`
   failed to, twice, then succeeded once — so treat the tier as *strongly
   correlated* with success rather than as a hard rule. If a run cannot fetch,
   raising the tier is the first thing to try.
2. **The instruction present.** In project instructions, or pasted as the first
   message. A fresh chat inherits the connector and none of the rules.
3. **The prompt text in the conversation.** Reading it from the repo works;
   pasting the file whole also works and never fails. Both are fine.

**Attaching an image on the same turn appeared to suppress repo reading.** With
references now fetched by URL this should not arise — nothing needs attaching.

The successful run: `High`, project instructions set, prompt text pasted, actor
headshot attached — full-length figure on seamless grey, correct face, correct
costume language, no retrieved character. It took just under four minutes.

## If you cannot read this repository

**Reply with exactly `CANNOT READ REPO`, generate nothing, and then say how to
proceed.** All three, in that order.

This supersedes an earlier version of this section that told you to offer the
fallback *instead of* stopping. A connected model correctly flagged the two as
contradictory on 2026-08-01 — the project-level instruction said stop, this file
said do not stop. They now agree.

> **CANNOT READ REPO**
>
> I can't fetch the repository, so I won't generate anything — an invented
> character sheet is worse than no answer. To proceed, paste the contents of
> `03-characters/<character>/prompts/turnarounds-short/turn-<outfit>-front.txt` and
> attach the reference images it names.

The stop is not optional and the fallback is not a substitute for it. Failing
visibly is the point; the paste route is what the user does next.

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
Every `NON-NEGOTIABLE` item exists because a previous generation got that thing
wrong. A compressed version produces a plausible, wrong image.

**Use the SHORT prompt. `prompts/turnarounds-short/`, not `prompts/turnarounds/`.**

Established 2026-08-01, and it is the single most important line in this file.
Image models accept roughly 4,000 characters. The long prompts run to 28,000 —
seven times over. Everything past the limit is compressed by the host before it
reaches the generator, lossily and differently each run, which is why the same
file produced a usable costume plate one run and a Jedi character sheet the next.
It is the cause of nearly every failure recorded in this document.

The short files hold the same non-negotiables, trimmed to fit. **They are the
prompt.** The long ones under `prompts/turnarounds/` are the specification — read
them if you need to settle a detail, never paste them into a generator.

That is also why rule 1 is not a licence to shorten things yourself: the trimming
is done by a tool, deterministically, with the critical clause of each rule kept.
Your own compression is not the same thing.

**2. Never generate from `Character.md`.**
Those are written for humans and are the wrong shape to generate from. Only files
under `prompts/` are prompts.

**3. FETCH the reference images yourself. Every one has a public URL.**

Prompt files carry lines like:

```
FETCH AND USE AS THE LIKENESS REFERENCE (1 of 2) — front on, neutral:
    https://raw.githubusercontent.com/.../headshot-neutral.jpg
```

**Open every one of them before generating.** They are public raw files with no
authentication, and they open — verified 2026-08-01, when a model fetched an actor
headshot from one of these URLs and described it accurately down to the shirt and
the background blur.

Three kinds appear, and all three are fetchable:

- **The likeness reference** — the actor. There may be several, numbered; they are
  the same person from different angles and all of them should be used.
- **The approved costume reference** — on every view except the one that creates
  it.
- **Plate references** — a material, a weapon, a piece of kit already locked.

**Fetching is not enough on its own.** For each URL: download it, decode it,
look at it to confirm it opened, and **make the downloaded file available as an
image input to the generator.** A file retrieved by a repository tool but never
handed to the generator is not a reference — that gap, not the URLs, is what
produced a run of wrong faces on 2026-08-01.

**Do not ask for a manual attachment when the download and the handoff both
succeed.** Ask only when a URL will not download, a file will not decode, or the
generator cannot receive it — and then name the one that failed and stop. Never
invent a face.

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

**9. Some of these names belong to characters you already know.**
`Baylan` and `Shin` are real characters from another production, and the name
alone will retrieve that depiction — robes, lightsabers, poise, a backstory about
a mysterious order. **None of it applies here.** This film is set eighteen years
earlier and both are in hiding or in chains. Their prompts carry an explicit
`DO NOT DRAW THAT CHARACTER` block; read it and obey it. If you are adding
something because it feels right for the name rather than because the document
says so, that is the retrieval.

---

## Command — "make the reference picture for `<character>`"

Accepted phrasings, all meaning the same thing:
*"make the reference image for: baylan"*, *"make the reference picture for
baylan"*, *"make baylan's reference"*, *"generate the front turnaround"*.
The character name is the folder name, **lower case**.

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

`<N>` is the number of `.txt` files under `prompts/` and `prompts/turnarounds-short/`
for that character, minus the front view itself.

**Only continue if the user says yes.** If they do, treat the result as a
*preview* — do not overwrite the existing approved image, and do not touch
`outfits.yaml`.

**If no approved reference exists**, say so briefly and continue.

### Step 2 — generate

1. Read `03-characters/<character>/prompts/turnarounds-short/turn-<outfit>-front.txt`.
   **The short one.** See rule 1 — the long file will not fit in the generator.
2. Fetch every file named in an operator line.
3. **Actor references are listed in the prompt itself, numbered, each with a
   full public URL.** There may be several — they are the same person from
   different angles and all of them should be used. **Fetch them yourself**,
   decode them, and hand them to the generator as image inputs.
4. Read the non-negotiables back.
5. Generate one image at the aspect ratio in the file header.
6. Self-check.

**The front view is the only image generated without a costume reference**,
because it is the one that creates it. The prompt says so itself. Do not go
looking for a costume reference — the plates and the actor references are all
there is, and both are fetchable.

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

### Step 4 — commit each accepted image, one at a time

When the user accepts an image, commit it to
`03-characters/<character>/source/artwork/<filename from line 2 of the prompt>`.

**Only accepted images.** A rejected generation must never reach the repository.

**Say the exact path you committed to**, so the user can check it against the
board configuration.

### What you cannot do, and must hand back

**You cannot run the generators.** The prompt files are built from `outfits.yaml`
and `Prompts.md` by `tools/prompt-splitter/`, and after an approval those sources
change — recording an approved reference switches on the gate that makes every
other view fetch and match it.

So after the FRONT view is approved and committed, stop and say:

> The front view is committed. Before the other views can match against it,
> `outfits.yaml` needs its `approved:` block and the prompts need regenerating and
> pushing — I can't run the generators. Once that's done I'll continue.

Generating the other views before that happens produces four images matched
against nothing.

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
