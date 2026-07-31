# Approving a Costume

How a costume goes from *in progress* to *locked*, and what that protects.

## The problem it solves

Turnarounds only work if the five views are the same photograph rotated. Words
cannot hold that — **an approved image can.** Once one view is right, every other
view should be matched against it rather than re-derived from a paragraph.

And once artwork exists, the prompt that made it must stop moving. Otherwise you
have four views built from one description and a fifth built from another.

## How to approve

When a view is right, add an `approved` block to that outfit in
`outfits.yaml`:

```yaml
outfits:
  - id: working
    name: Infiltration dress
    approved:
      date: "2026-07-31"
      view: front
      reference: 03-characters/shada/source/artwork/turn-working-front.png
      note: "Front view locked. Match this for all other views."
```

Then regenerate:

```bash
python tools/prompt-splitter/turnarounds.py shada
```

## What that does

**Every other view now opens with a match instruction** naming the file to
attach, and ending:

> Where this text and the reference image disagree, **THE IMAGE WINS.**

That last line matters. A long prompt will always contain something the approved
image contradicts — a phrase that reads differently, a detail described loosely.
Without the precedence rule the generator has to guess.

**The approved view itself does not get the instruction**, since it cannot match
itself.

**The index marks the outfit APPROVED** with its date.

**The generator warns you** if you regenerate an approved outfit's prompts.

## Where files live

| Path | What | Reproducible |
|---|---|---|
| `reference/actor/` | Actor photographs — **input** | No. Irreplaceable |
| `source/artwork/` | Accepted generated images — **output**, and the board source | No. Cannot be regenerated identically |
| `reference/approved/` | Optional. A copy of a match target if it is not itself final artwork | — |
| `prompts/` | Generated prompt text | Yes, from `Prompts.md` |
| `prompts/turnarounds/` | Generated turnaround prompts | Yes, from `outfits.yaml` |

The approved reference normally lives in `source/artwork/` and is pointed at, not
duplicated. Use `reference/approved/` only when the match target is not itself a
final asset — an early generation you want to match but not use.

## Changing an approved outfit

**Editing it invalidates artwork already made from it.**

If a change is genuinely needed:

1. Clear the `approved` block.
2. Make the change and regenerate.
3. Generate a new reference view.
4. Re-approve from it.
5. **Regenerate every other view of that outfit.** They no longer match.

The generator's warning exists so this is a decision rather than an accident.

## Save accepted images immediately

The prompt is reproducible. The chat is disposable. **A good generation you did
not save is gone.**

Save to `source/artwork/` using the exact filename in the prompt header, the
moment you accept it.
