# Script conversion

Puts the screenplay under version control as plain text, so a draft change is a
diff instead of two PDFs held up to the light.

```bash
source .venv/bin/activate
pip install -r tools/script-convert/requirements.txt

# once per incoming draft
python tools/script-convert/pdf_to_fountain.py \
    "02-story/scenes/The Price of Freedom v9.pdf" \
    02-story/scenes/the-price-of-freedom-v9.fountain

# prove it
python tools/script-convert/pdf_to_fountain.py \
    "02-story/scenes/The Price of Freedom v9.pdf" \
    02-story/scenes/the-price-of-freedom-v9.fountain --verify

# render, any time
python tools/script-convert/render.py                # PDF
python tools/script-convert/render.py --format fdx   # Final Draft
```

## What is authoritative

**The `.fountain` file.** It is committed, it is what gets edited, and it is
what a revision diff is taken against.

The incoming typeset PDF is committed too, because it is what the writer
actually sent and it is the evidence any conversion is checked against. The
rendered `.pdf` and `.fdx` are **gitignored** — regenerable in one command, and
committing them would put a binary in history every time a line changes.

## Fountain, briefly

Plain-text screenplay markup, and deliberately almost invisible:

```
EXT. SAND DUNES - AFTERNOON (VISION)

She sees a hazy vision of a man we can't quite make out in Jedi robes.

PALPATINE (O.S.)
The time has come. Execute Order Sixty-Six.
```

A line beginning `INT.`/`EXT.` is a scene heading. An upper-case line is a
character cue. The line under it is dialogue, brackets are a parenthetical,
`> TEXT` is a transition, `#12#` at the end of a heading is a scene number. A
correctly typed screenplay is already most of the way there.

## How the conversion works

The incoming PDF is typeset in standard US screenplay format, so **every
element is identified by its left margin alone.** Nothing is inferred from
wording, which is what makes it trustworthy.

| x (points) | Element |
|---|---|
| < 80 | Scene number, out in the left margin |
| ~89 | Action, and scene headings |
| ~183 | Dialogue |
| ~226 | Parenthetical |
| ~269 | Character cue |
| > 380 | Transition |

Two things make a naive text extraction wrong, and both are handled:

- **Parentheticals are drawn as three spans** — the text, then the opening
  bracket, then the closing one. Read in document order that gives
  `cuts her off ( )`. Spans are grouped by baseline and sorted by x instead.
- **A scene number shares its baseline with the heading.** Split it off before
  classifying, or the heading is read as a scene number and lost with it.

## The verification, and what it reports

`--verify` re-renders the Fountain through screenplain and compares the words
against the original PDF. Current result:

```
similarity: 99.788%
LOST:   contact, more, bay, cont'd
GAINED: 1 … 25
```

All four differences are understood and intended:

- **`more` / `bay` / `cont'd`** — one `(MORE)` and its matching `BAY (cont'd)`,
  which exist only because the source draft happened to break a page mid-speech.
  They are typesetting, not content, and are merged back into one speech. A
  fresh render generates its own where it needs them.
- **`contact`** — the source title page reads `Contact: <address>`; screenplain
  renders the address under its own heading. The address is preserved.
- **`1`–`25`** — screenplain prints scene numbers in *both* margins, which is
  standard practice. The source printed them only on the left.

A stricter line-by-line check is also worth knowing about: **every body line
matches the source character for character**, with the single exception of the
merged `(MORE)` pair above.

**Page count is not preserved** — the source is 30 pages, a fresh render is 31,
because line-wrap widths differ slightly. That is fine in pre-production and
**wrong the moment anyone issues locked, coloured revision pages to a crew.**
Screenplain has no A-page or revision-mark support. If shooting drafts start
going out, this pipeline stops being the right tool for issuing them.

## Working with the writer

`--format fdx` writes Final Draft XML. That is the answer to "the writer does
not want to learn Fountain": revisions can go out as a `.fdx` she opens
natively, works in, and sends back. Nobody has to change tools.

Record who authored a revision in the commit message. The repository history
should not quietly imply the art department wrote the script.
