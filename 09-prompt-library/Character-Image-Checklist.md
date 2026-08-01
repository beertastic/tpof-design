---
title: "Character Image Checklist"
asset_id: "PROMPT-CHECKLIST"
version: "1.0"
status: "canonical"
---

# Generating a character, start to finish

**The complete procedure for one character, from documents to finished boards.**
Written 2026-08-01, after a day spent discovering the two things that make it work:
the prompt must be **pasted, never fetched**, and it must be the **short** one.

Follow it in order. Every step is here because skipping it cost an afternoon.

---

## The two rules everything else hangs off

**1. Paste the prompt. Never ask ChatGPT to read it from the repo.**

A connected model cannot hand your file to the image generator — the generator is
a separate system and whatever reaches it, ChatGPT retyped. A fetched prompt
arrives as a paraphrase. This is architectural and no wording fixes it. Full
explanation: [`Generating-From-A-Connected-Repo.md`](Generating-From-A-Connected-Repo.md).

**2. Paste from `prompts/turnarounds-short/`, never `prompts/turnarounds/`.**

Image models accept about 4,000 characters. The long files are 28,000 and get
silently compressed by the host. The long files are the specification, for humans
and for settling arguments. The short files are the prompt.

---

## Phase 0 — is this character ready?

**Do not start generating until all five are true.** Each missing item produces a
specific, repeatable failure.

| # | Requirement | Where | Fails as |
|---|---|---|---|
| 1 | `handedness:` set | `outfits.yaml`, top level | Holster swaps sides between views |
| 2 | `height:` as a phrase | `outfits.yaml`, top level | A lone figure on grey has no scale; the model invents one |
| 3 | `must_show:` on every outfit | `outfits.yaml` | Critical features never reach the top of the prompt |
| 4 | At least one actor photograph | `reference/actor/` | Generic face, and no way to match later views |
| 5 | `do_not_retrieve:` **if the name belongs to a known character** | `outfits.yaml` | The name alone retrieves the wrong person |

**You do not have to check by hand.** Run this and read what it says:

```bash
./tools/regen baylan
```

It prints every warning and refuses to go further if anything blocking is missing.

### Current state — checked 2026-08-01

| Character | Ready? | Missing |
|---|---|---|
| **Baylan** | **Yes** | — |
| **Shada** | Nearly | `height:` |
| **Mercenary Kit** | Nearly | `height:` per merc (Merc 1 is a Wookiee — his differs) |
| **Shin** | **No** | `handedness:`, `must_show:` on all three outfits, `height:` |

### Actor photograph rules

- **No spaces in the filename.** `Tristan Pretty.jpg` breaks the raw URL as a
  connection error rather than a 404, which looks exactly like having no repo
  access. Cost half a day. Use `headshot-neutral.jpg`.
- **Lower case, hyphenated.** GitHub is case-sensitive.
- **Several are better than one.** They get numbered automatically — front-on
  neutral first, then any others. All of them go into the prompt as URLs.
- Consent and sourcing: [`03-characters/CAST-REFERENCE.md`](../03-characters/CAST-REFERENCE.md).

---

## Phase 1 — regenerate and push

**Every time you change `outfits.yaml`, `Prompts.md`, or an actor photograph.**

Open a terminal in the project folder and type exactly this:

```bash
./tools/regen baylan
```

That is the whole step. It runs all three generators, shows any warnings, commits,
pushes, and then prints the full path of the file to paste, which photograph to
attach, and the exact line ChatGPT must say back to you.

Substitute the character's folder name — `baylan`, `shada`, `shin`,
`mercenary-kit`. Run it with no name to list them:

```bash
./tools/regen
```

**Pass a commit message when the change deserves one:**

```bash
./tools/regen baylan "design(baylan): scorch moves to the left shoulder"
```

Without one it commits as `prompts(<character>): regenerate`, which is right for a
plain regeneration and wrong when the run also carries a decision worth recording.

**It stops you if the character is not ready.** Missing `handedness:` or
`must_show:` and it refuses to print the next steps, because without them every
weapon and armour placement is decided by the generator, differently each time.

**It stops you if the push fails.** The reference photograph URLs inside the
prompt point at the pushed branch, so unpushed work is invisible to ChatGPT and
you would generate from stale files without knowing.

### First time only, per clone

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install pyyaml reportlab
git config core.hooksPath tools/hooks
```

---

## Phase 2 — the front turnaround

**This is the image that creates the reference. Every other image of the costume
is matched against it, so an error here propagates into all of them. It is worth
several attempts.**

### Step by step

1. **Open a fresh ChatGPT conversation.** Not a continued one — old chats hold
   superseded costumes and blend them.
2. **Set the reasoning tier to `High`.** Check it every time; it does not persist.
3. **Open the file:**
   `03-characters/<character>/prompts/turnarounds-short/turn-<outfit>-front.txt`
4. **Select all. Copy. Paste as your entire first message.** Nothing before it,
   nothing after it, no "here's a prompt for you". Do not trim the top.
5. **Attach the actor photograph** from `reference/actor/`. The URLs are in the
   prompt, but attaching is more reliable and costs nothing.
6. **Send. Wait.** Two to four minutes is normal at `High`.

### Before you look at the picture, check the reply

It must open with a line like:

> Working from commit `ddc2d15`, prompt `5e85b186`.

**No line, no image.** Neither value is guessable, so quoting them is proof it
read the file you pasted. If the line is absent, the model wrote its own brief —
discard the result whatever it looks like, and start a fresh chat.

It should then list the non-negotiables back, and self-check afterwards.

### What a correct front turnaround looks like

- **One person, alone**, full length, head to below the feet
- **Plain seamless backdrop.** No location, no set, no props on the floor
- **Arms about 30° out from the body** so the silhouette reads and nothing overlaps
- **Portrait, 2:3** — 1024×1536
- **No text of any kind.** No name, no palette, no swatches, no height scale, no
  panels, no borders, no second view, no inset heads, no detail crops

**If it has a name banner or a colour palette, it is a design board and it is
wrong**, however good it looks. Reject it.

---

## Phase 3 — when it is close but not right

**This is where the costume quietly drifts, so there is one rule.**

> **Never say "same again but…", "make the arms lower", or "try that with the coat
> off".**

Any of those makes the model work from **its own last output** instead of your
document. Two rounds of that and you are refining a picture that was already wrong.

### Do this instead

**Re-paste the whole prompt, with one correction line at the top.** Same fresh
chat is fine for a retry of the same view.

```
The last attempt got these wrong — fix them and keep everything else:
  - the arms were tight to the body; they must be ~30° out
  - the coat was worn; the turnaround views record the base costume

[then the entire prompt file, pasted below]
```

The file stays the source of truth and the correction is an overlay on it, rather
than the other way round.

### If two or more of these appear, the references were not used

Do not argue with the image. Start a fresh chat and paste again.

| Symptom | What it means |
|---|---|
| A design board, palette, or any text | It wrote its own brief; the prompt never arrived |
| The wrong face | The actor photograph was not fetched or not attached |
| A retrieved character — robes, hood, a lightsaber | The `do_not_retrieve:` block lost to the name |
| Wrong height or proportions | Scale was invented; check `height:` is in `outfits.yaml` |
| Character-specific failures | Watch-list, e.g. [`Shada-Image-TODO.md`](../11-production-tracking/Shada-Image-TODO.md) |

---

## Phase 4 — accepting the front turnaround

**Only when you are genuinely happy.** Everything downstream inherits it.

1. **Download the image.**
2. **Save it to** `03-characters/<character>/source/artwork/` **using the exact
   filename on line 2 of the prompt** — e.g. `turn-working-front.png`.
3. **Commit and push it.**

```bash
git add 03-characters/<character>/source/artwork/turn-<outfit>-front.png
git commit -m "art(<character>): approved front turnaround"
git push
```

**Rejected images must never reach the repository.**

---

## Phase 5 — tell me, and I switch the gate on

**Say:**

> Baylan's front turnaround is approved and pushed. Record it and regenerate.

**What I do, and why it cannot be skipped:**

1. Write the `approved:` block into `outfits.yaml`:

```yaml
approved:
  date: "2026-08-01"
  view: front
  reference: 03-characters/baylan/source/artwork/turn-working-front.png
```

2. Re-run all three generators. **This is the important part.** Recording the
   approval switches on a gate: every other prompt for that costume now carries
   the approved photograph's URL and an instruction to match it. Before this, the
   other four views are matched against nothing.
3. Commit and push, and tell you the new commit id.

**Do not generate the other views before this happens.** You will get four
handsome images of four different costumes.

---

## Phase 6 — the other four turnaround views

**One at a time. Left, right, back, natural.**

Same procedure as Phase 2, with two differences:

- **Attach the approved front turnaround as well as the actor photograph.** This
  is the costume reference, and these prompts refuse to run without it.
- **A fresh chat per view** is safest. Continuing a chat invites the model to
  work from its own previous image.

### Checking the back view

**Do not check it by asking whether things stayed on the same side of the frame.**
They should not have — when he turns around, his right side moves from the
viewer's left to the viewer's right, and a mirrored front plate does exactly the
same thing. Frame position cannot tell them apart.

**Check the anatomy instead.** A real back view shows shoulder blades, back seams,
rear pockets, the harness crossing the back, and the back of the head. A flipped
front view shows the face. See
[`Handedness-And-Placement.md`](Handedness-And-Placement.md).

---

## Phase 7 — the plates and mood images

The numbered files in `prompts/` — portraits, environments, props, detail shots.

- **Turnarounds first, always.** They are what a costume department builds from;
  mood images are context. Three or four per character is plenty.
- Same paste-and-attach procedure.
- **Attach whatever the prompt's operator lines name** — the approved front
  turnaround, and any locked prop plates listed under `references:`.
- Accept, save to `source/artwork/` under the filename on line 2, commit.

---

## Phase 8 — boards

Once the artwork exists:

```bash
python tools/board-generator/generate.py <character> --validate   # check first
python tools/board-generator/generate.py <character>              # build the PDFs
```

Board contents come from `board-data.yaml`, not from the tool. If an image is
missing, `--validate` names it.

---

## The whole thing, on one card

**Type this:**

```bash
./tools/regen baylan
```

**Then do what it tells you**, which is:

```
1.  Fresh ChatGPT chat. Tier set to High.
2.  Paste the whole file it named. Nothing before it, nothing after it.
3.  Attach the actor photograph it named.
4.  Its reply must open with:  Working from commit <id>, prompt <hash>.
    NO LINE, NO IMAGE. Discard it and start a fresh chat.
5.  Wrong? Re-paste the WHOLE file with a correction line on top.
    Never "same again but…" — that works from its own last output.
6.  Right? Save it into 03-characters/baylan/source/artwork/
    under the exact filename on line 2 of the prompt. Then:
        git add -A && git commit -m "art(baylan): approved front turnaround" && git push
7.  Tell Claude: "Baylan's front is approved and pushed. Record it and regenerate."
8.  The other four views — one fresh chat each, approved front attached too.
9.  The numbered plates in prompts/.
10. Boards:  python tools/board-generator/generate.py baylan
```

---

## Why each rule exists

Every one of these was learned the expensive way on 2026-08-01.

| Rule | What happened without it |
|---|---|
| Paste, never fetch | A board headed **THE PATHS OF FATE** — not this film's title — with four other phrases that exist nowhere in the repository |
| Short prompts | 28,220 characters against a ~4,000 limit; the host compressed them differently every run |
| Quote the commit and hash | A run reported no provenance at all, having read nothing, and nothing in the reply said so |
| Never say "reference image" | It names a genre. Ask for one and you get a design board with swatches, whatever the prompt says |
| Never "same again but…" | The model works from its own last output and the costume drifts |
| Height in `outfits.yaml` | A figure on a plain backdrop has nothing to measure against, so the model picks a height |
| No spaces in filenames | A raw URL fails as a connection error, indistinguishable from having no access |
