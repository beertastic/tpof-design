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
./tools/regen shada
```

**Use `regen`, not the generators individually.** Approval changes what every
*other* view says, and that text has to reach `prompts/turnarounds-short/` — the
directory the pasted prompt comes from — or the match instruction you just added
never gets used. `regen` runs all three generators, commits and pushes.

## What that does

**Every other view now opens with a match instruction** naming the file to
attach. In the short prompts it is the first reference in the attachment block:

>     COSTUME (match exactly): <url of the approved plate>

and in the long prompts:

>     FETCH AND MATCH — the approved costume reference: <url>

**Precedence comes from the scope line, not from a separate sentence.** Every
prompt already says *"Each photograph is an authority WITHIN ITS OWN SCOPE and
nowhere else"* (long prompts: *"THE ATTACHED PHOTOGRAPHS OUTRANK THIS TEXT, EACH
WITHIN ITS OWN SCOPE"*), and the approved plate's scope is **the whole costume**.
So where the text and the photograph disagree about the costume, the photograph
wins — because that is what its label says it is authoritative for.

> **Corrected 2026-08-05.** This section used to quote a sentence — *"Where this
> text and the approved front turnaround disagree, THE PHOTOGRAPH WINS"* — and
> claim every other view ended with it. **No generator has ever emitted that
> string**, for any character, including Shada who has been approved since
> 2026-07-31. The mechanism was real and the quotation was not. Anyone editing
> the generators to "restore" that line should know it was never there.

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
