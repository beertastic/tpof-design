# Prompt Library

Shared prompt language and the rules for writing it. Everything here is
**canonical** — if a character's `Prompts.md` disagrees with a block in this
folder, this folder is right and the character file is stale.

## The one rule about this folder

**Blocks are INLINED into each `03-characters/<name>/Prompts.md`, never
referenced.** An image generator reading a single prompt file in isolation must
receive the full ruleset with no other file open. **If you change a block here,
propagate it to every character file that carries it**, then re-run
`./tools/regen <character>`.

## What is here

| File | What it is | Paste it? |
|---|---|---|
| [`Writing-Rules-A-Generator-Can-Follow.md`](Writing-Rules-A-Generator-Can-Follow.md) | **Read this first.** How to phrase a rule so it survives the trim and lands in the image | No — guidance for authors |
| [`Global-Style-Block.md`](Global-Style-Block.md) | Style, Do Not, Realism — the shared voice of the production | Yes, every prompt |
| [`Capture-Block.md`](Capture-Block.md) | Anamorphic glass and 35 mm negative response | Narrative slots only |
| [`Cinematic-Framing-Block.md`](Cinematic-Framing-Block.md) | Camera position, motivated light, three layers of depth | Narrative slots only |
| [`Turnaround-Block.md`](Turnaround-Block.md) | The five-view costume turnaround | Turnarounds only |
| [`Handedness-And-Placement.md`](Handedness-And-Placement.md) | Which side every weapon and hard piece sits on, and how to check a back view | No — the source for `must_show` rules |
| [`Character-Image-Checklist.md`](Character-Image-Checklist.md) | The operator procedure: fresh chat, attachments first, tier High | No — follow it |
| [`Generating-From-A-Connected-Repo.md`](Generating-From-A-Connected-Repo.md) | Why repository access is not the same as the model seeing an image | No |
| [`ChatGPT-Project-Instructions.md`](ChatGPT-Project-Instructions.md) | Standing instructions for a connected project | No |
| [`Key-Art-Poster-Prompt.md`](Key-Art-Poster-Prompt.md) | The poster, which follows different rules from everything else | Yes, on its own |

## Two things that are easy to get wrong

**Not every block goes on every prompt.** Capture and Cinematic Framing belong to
narrative slots only — roughly six of sixteen. On a materials board or a prop
plate, shallow depth of field and an off-centre crop are faults. Each
`Prompts.md` records applicability with an `Applies to slots …` line.

**The long prompt files in `03-characters/<name>/prompts/` are NOT for pasting.**
They are the specification, 5–8× over any working budget, and the overflow is
discarded silently from the middle. Paste from `prompts/slots-short/` and
`prompts/turnarounds-short/`, which say `(short)` on their version line. Every
long file now opens with a banner saying so.

## Where the failures are logged

- [`11-production-tracking/Prompt-Reliability-TODO.md`](../11-production-tracking/Prompt-Reliability-TODO.md)
  — tooling faults and the fix list
- `11-production-tracking/<Character>-Image-TODO.md` — per-character run lists and
  what each failed generation taught

`03-characters/shada/` is the worked example for all of it: twenty-one images,
six boards, and a documented reason behind every rule in her pack.
