# Instructions for AI agents with access to this repository

**Read this before generating anything.**

---

## Read this first: you probably cannot generate from these prompts

**Established 2026-08-01, after an entire day lost to it.** It is the single most
important thing on this page, and everything below is shaped by it.

**You are not the image generator. You are a relay.** The image model is a
separate system with its own short input field, and it never sees this
repository. Whatever reaches it, you typed.

That produces two completely different pipelines, and only one of them works:

| Route | What the image model actually receives |
|---|---|
| The user **pastes** the prompt into the chat | The prompt text, near enough intact — it is already in the conversation, so relaying it costs nothing |
| **You fetch** the prompt from this repository | **Your paraphrase of it.** The file arrives as a tool result — as source material — and you compose a fresh brief from your impression of it |

**The second route has never once produced a usable image.** Not because of
disobedience. Because a file you read is *input to you*, and the generator's
input is a string *you write*. The document never arrives.

Here is what that looks like from the outside. Asked for Baylan's front
turnaround, a run read the repository — the sources badge confirmed it — and
returned a design board headed **THE PATHS OF FATE**. This film is called *The
Price of Freedom*. Also on it: "Former Jedi", "pensive wanderer", "No rank
insignia", "Stands with quiet confidence". **Not one of those five phrases exists
anywhere in this repository.** The run was not ignoring the prompt. It had read
the character documents, understood the job, and written its own brief — helpfully,
fluently, and from nothing.

### What this means for you

**Do not offer to generate an image from a prompt file you fetched.** You will
produce something plausible and invented, and it will cost the Production
Designer an hour to work out why.

Say this instead:

> I can read the prompt but I cannot hand it to the image generator — anything I
> fetch, I have to retype, and what I retype is my summary rather than your file.
> Paste `03-characters/<character>/prompts/turnarounds-short/turn-<outfit>-front.txt`
> as your next message and I will generate from that.

**Then generate from the pasted text.** That route works and has worked every
time.

The human procedure this fits into is
[`09-prompt-library/Character-Image-Checklist.md`](09-prompt-library/Character-Image-Checklist.md).

**What you ARE good for**, and it is most of the job: reading the repository,
checking the approval gate, quoting the commit and prompt hash, fetching
reference photographs, answering questions about the design, committing accepted
images, and editing `outfits.yaml`. Do all of that. Just do not pretend the
generator can see what you can see.

## Step 0a — was this prompt PASTED to you? Then skip the repo entirely.

**If the user has pasted a prompt into the conversation, generate from it. Do not
read `REPO-STATE.md`. Do not compare anything. Do not check whether the repository
is current.**

A pasted prompt is self-contained by design — every rule it needs is inlined, and
it carries its own commit id and content hash on line 4. **Nothing about the
repository can make a pasted prompt stale.** The text in front of you is the text
the Production Designer chose to send.

**Recorded 2026-08-01, because the rule below blocked the only workflow that
works.** A run correctly noticed that the `REPO-STATE.md` it could fetch was
stamped older than the commit named in a pasted prompt, correctly applied the
stale-content rule, and correctly refused to generate. Every step was right and
the outcome was wrong: the repository was irrelevant to the request. The cached
copy was behind; the pasted prompt was current; and comparing the two was a
category error I had written into this file.

**So the scope is now explicit.** The staleness check below governs reading FROM
the repository. It does not govern text handed to you directly.

The commit id and hash on line 4 are **provenance for the human**, not a gate for
you to satisfy. Quote them back — that is the proof you read the file — and then
generate. If they happen to disagree with anything you can fetch, say so in one
line and generate anyway.

---

## Step 0 — when you are READING from the repository, always, before anything else

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

**Also state what you actually read.** Line 4 of every prompt file now carries
both a content hash and the repository commit:

```
Prompt version: 5e85b186 (short) · repo commit ddc2d15 2026-08-01 15:56
```

and the file tells you, in its own words, to say this back before generating:

> Working from commit `ddc2d15`, prompt `5e85b186`.

**That line is not a formality — it is the whole check.** Neither value can be
guessed or remembered. The hash changes when the prompt changes and never
otherwise; the commit id changes on every commit. Quoting both proves you opened
the current file. **No line, no image.** If you cannot produce it, say so plainly
and generate nothing.

The Production Designer can verify any hash you quote:

```bash
grep -rl "Prompt version: <hash>" 03-characters/*/prompts/
git log --oneline -1 <commit>
```

**Added 2026-08-01, after a run that spent three and a half minutes and returned a
character design board with an orange blade, a row of hilts and a data panel of
invented fields — having reported no stamp at all.** It had read nothing. Silence
about provenance turned out to be the reliable early warning, so it is now
forbidden: every reply says where its information came from, or there is no reply.

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
3. **The prompt text PASTED into the conversation.** This is not optional and
   the two routes are not equivalent — *"reading it from the repo works"* stood
   here until 2026-08-01 and was simply wrong. A fetched prompt is retyped from
   memory before the generator sees it. A pasted one is not. See the top of this
   file.

**Attaching an image on the same turn appeared to suppress repo reading.** With
references now fetched by URL this should not arise — nothing needs attaching.

The successful run: `High`, project instructions set, prompt text pasted, actor
headshot attached — full-length figure on seamless grey, correct face, correct
costume language, no retrieved character. It took just under four minutes.

## If you cannot read this repository

**This section does not apply to a pasted prompt.** If the prompt is in the
conversation, generate from it — see Step 0a. Replying `CANNOT READ REPO` to a
self-contained prompt happened on 2026-08-01 and was wrong.

The rule that produced it lives in ChatGPT's project instructions, not here, so
fixing this file alone changed nothing. The master copy of that block is
[`09-prompt-library/ChatGPT-Project-Instructions.md`](09-prompt-library/ChatGPT-Project-Instructions.md)
— if a rule must hold, it has to be there.


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
> attach the photographs it names.

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

**1. The prompt files ARE the prompts. Use them verbatim — and if you cannot,
say so rather than approximating.**

Never summarise, shorten, paraphrase or extract "key points" from a prompt file.
Every `NON-NEGOTIABLE` item exists because a previous generation got that thing
wrong. A compressed version produces a plausible, wrong image.

**Note what this rule is really asking.** If you fetched the file, "verbatim" is
not something you can deliver — you have to retype it into the generator, and
retyping is paraphrase however careful you are. That is not a failure of effort;
it is the shape of the tools. See the section at the top of this file. The honest
response is to ask for a paste, not to do your best from memory.

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

**3. FETCH the reference photographs yourself. Every one has a public URL.**

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

## Command — "make the front turnaround for: `<character>`"

Accepted phrasings, all meaning the same thing:
*"make the front turnaround for: baylan"*, *"make baylan's front turnaround"*,
*"make the front costume photo for baylan"*.
The character name is the folder name, **lower case**.

This produces the **front turnaround** — a single costume fitting photograph of
one person, which every other photograph of that costume is then matched against.

### Never call this a "reference image", and never draw one

**Recorded 2026-08-01, after it cost a full day.** The command used to be phrased
*"make the reference image for `<character>`"*. Asked that, a model produced a
multi-panel character design board: name banner, front/side/back row, portrait
strip, colour swatches, detail crops, an invented data panel with ALIGNMENT and
FACTION fields that exist nowhere in this repository — and it captioned the whole
thing **REFERENCE IMAGE**.

It was not disobeying. *Reference image*, *character sheet* and *reference sheet*
are the names of a **genre of picture**, and naming a genre summons its layout.
The prompt forbade every element of that board and lost, because two words in the
request outweighed three thousand characters of instruction.

So the word is gone from the command, from the prompts, and from the generators.
Say what the picture **is**, in the words a camera department would use:

| Say this | Never this |
|---|---|
| front turnaround | reference image |
| costume fitting photograph | character sheet |
| plate photograph | reference sheet |
| the approved front turnaround | the reference |

**"Reference" is still correct for an INPUT** — a photograph you fetch and match
against. It is never correct for the thing you are making.

### Step 1 — the approval gate. Run this FIRST, every time.

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

## Command — "make all `<character>` photographs from the front turnaround"

### Step 1 — require a reference

Read `outfits.yaml`. **If there is no `approved.reference`, or the file is
missing, stop.** Say:

> `<character>` has no approved front turnaround yet. Everything else is matched
> against it, so that has to come first. Shall I make the front turnaround?

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
