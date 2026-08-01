#!/usr/bin/env python3
"""Convert the typeset screenplay PDF into Fountain.

    python tools/script-convert/pdf_to_fountain.py \
        "02-story/scenes/The Price of Freedom v9.pdf" \
        02-story/scenes/the-price-of-freedom-v9.fountain

This exists to run ONCE per incoming draft. The Fountain file is the thing
that gets edited afterwards; the PDF it came from is an artefact of how the
draft arrived, not a source.

Why this works at all: the PDF is typeset in standard US screenplay format,
and every element is identifiable by its left margin alone. Nothing is
guessed from the wording.

    x < 80    scene number in the left margin
    x ~ 89    action, and scene headings
    x ~ 183   dialogue
    x ~ 226   parenthetical
    x ~ 269   character cue
    x > 380   transition

Run `--verify` afterwards. It re-renders the Fountain through screenplain and
compares the words against the original PDF, which is the only thing that
proves the conversion did not drop or reorder anything.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import fitz

ACTION = 89.5
DIALOGUE = 183.1
PAREN = 226.3
CUE = 269.5
TRANSITION_MIN = 380.0
SCENE_NUM_MAX = 80.0
TOL = 3.0

# Lines this far apart belong to different elements. Within a wrapped
# paragraph or speech the spacing is 12pt; between elements it is 24pt.
ELEMENT_GAP = 18.0

SCENE_HEADING = re.compile(r"^(INT\.|EXT\.|INT/EXT|I/E)", re.I)
SCENE_NUMBER = re.compile(r"^\d+[A-Z]?$")


def lines_of(page) -> list[tuple[float, float, str, str | None]]:
    """Group spans into visual lines, ordered left to right.

    Returns (y, x, text, scene_number) per line.

    Two things make this necessary rather than using the plain text stream:

    Parentheticals are drawn as three separate spans — the text, then the
    opening bracket, then the closing one — so reading the stream in document
    order produces "cuts her off ( )". Grouping by baseline and sorting by x
    puts them back together, and fixes every "NYX (cont'd)" cue too.

    And a scene number shares its baseline with the scene heading, sitting out
    in the left margin. It has to be split off before the line is classified,
    or the heading is read as a scene number and lost with it.
    """
    rows: dict[float, list[tuple[float, str]]] = {}
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                # Whitespace-only spans are kept: the gap between a cue and
                # its "(cont'd)" is one, and dropping it silently produced
                # "VALA(cont'd)".
                if not span["text"]:
                    continue
                y = round(span["origin"][1], 1)
                rows.setdefault(y, []).append((span["origin"][0], span["text"]))

    out = []
    for y in sorted(rows):
        if y < 60:  # the page number, in the header
            continue
        spans = sorted(rows[y])
        number = None
        if spans[0][0] < SCENE_NUM_MAX and SCENE_NUMBER.match(spans[0][1].strip()):
            number = spans[0][1].strip()
            spans = spans[1:]
        if not spans:
            continue
        text = "".join(t for _, t in spans).rstrip()
        if text:
            out.append((y, spans[0][0], text, number))
    return out


def classify(x: float, text: str) -> str:
    if x < SCENE_NUM_MAX:
        return "scene_number"
    if x > TRANSITION_MIN:
        return "transition"
    if abs(x - CUE) < TOL:
        return "cue"
    if abs(x - PAREN) < TOL:
        return "parenthetical"
    if abs(x - DIALOGUE) < TOL:
        return "dialogue"
    if abs(x - ACTION) < TOL:
        return "heading" if SCENE_HEADING.match(text) else "action"
    return "action"


def convert(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)

    out: list[str] = []
    pending_scene_number: str | None = None
    after_more = False
    prev_kind: str | None = None

    def emit(block: str) -> None:
        if out and out[-1] != "":
            out.append("")
        out.append(block)

    # Page 1 is the title page. Its layout is centred rather than margined,
    # so it is read as a title block rather than run through the classifier.
    for _, _, text, _ in lines_of(doc[0]):
        out.append(text)
    title_lines = out[:]
    out = []

    for page in doc[1:]:
        prev_y: float | None = None
        for y, x, text, number in lines_of(page):
            kind = classify(x, text)
            new_element = prev_y is None or (y - prev_y) >= ELEMENT_GAP
            prev_y = y

            if number:
                pending_scene_number = number

            if text == "(MORE)":
                after_more = True
                continue

            if kind == "scene_number":
                pending_scene_number = text
                continue

            if kind == "cue":
                # A cue immediately after a (MORE) is the same speech resuming
                # over a page break, not a new one.
                if after_more:
                    after_more = False
                    prev_kind = "dialogue"
                    continue
                # Verbatim. The cue is already upper case on the page, and
                # forcing it turns "(cont'd)" into "(CONT'D)".
                emit(text)
                prev_kind = "cue"
                continue

            after_more = False

            if kind == "heading":
                heading = text
                if pending_scene_number:
                    heading = f"{heading} #{pending_scene_number}#"
                    pending_scene_number = None
                emit(heading)
                prev_kind = "heading"
                continue

            if kind == "transition":
                emit("> " + text)
                prev_kind = "transition"
                continue

            if kind == "parenthetical":
                emit(text) if prev_kind not in ("cue", "dialogue") else out.append(text)
                prev_kind = "parenthetical"
                continue

            if kind == "dialogue":
                if prev_kind in ("cue", "parenthetical", "dialogue") and not new_element:
                    out.append(text)
                elif prev_kind in ("cue", "parenthetical"):
                    out.append(text)
                else:
                    emit(text)
                prev_kind = "dialogue"
                continue

            # action
            if prev_kind == "action" and not new_element:
                out.append(text)
            else:
                emit(text)
            prev_kind = "action"

    body = "\n".join(out).strip() + "\n"
    return build_title_block(title_lines) + "\n" + body


COPYRIGHT = re.compile(r"^(©|\(c\)|C)\s*\d{4}", re.I)


def build_title_block(lines: list[str]) -> str:
    """The title page, as a Fountain title block.

    Everything is kept verbatim — including the copyright line, which is a
    literal capital C in the source rather than © and is not ours to correct.

    Only the keys screenplain actually renders are used. `Notes:` parses fine
    and then silently fails to appear on the page, which is how the "Based on
    'Baylan Skoll'" credit and the writer's contact details went missing from
    the first round-trip.
    """
    title = lines[0] if lines else "Untitled"
    credit = author = ""
    source: list[str] = []
    contact = copyright_line = ""

    i = 1
    while i < len(lines):
        line = lines[i]
        low = line.lower()
        if low.startswith("written by"):
            credit = line
            if i + 1 < len(lines):
                author = lines[i + 1]
                i += 1
        elif low.startswith("story by"):
            source.append(f"{line} {lines[i+1]}" if i + 1 < len(lines) else line)
            if i + 1 < len(lines):
                i += 1
        elif low.startswith("contact"):
            # The line already reads "Contact: ..." on the page; keep the
            # address, not a second copy of the label.
            contact = line.split(":", 1)[1].strip()
        elif COPYRIGHT.match(line):
            copyright_line = line
        else:
            source.append(line)
        i += 1

    def field(key: str, values: list[str]) -> list[str]:
        """One Fountain title-page field.

        A multi-line value has to use the block form — a bare `Key:` followed
        by indented lines. Screenplain's parser only looks for continuation
        lines when the key's own line is empty, so `Source: Story by X`
        followed by indented lines silently fails to parse and the whole title
        page is rendered as body text.
        """
        if not values:
            return []
        if len(values) == 1:
            return [f"{key}: {values[0]}"]
        return [f"{key}:"] + ["\t" + v for v in values]

    out = field("Title", [title])
    out += field("Credit", [credit] if credit else [])
    out += field("Author", [author] if author else [])
    out += field("Source", source)
    out += field("Contact", [contact] if contact else [])
    out += field("Copyright", [copyright_line] if copyright_line else [])
    return "\n".join(out) + "\n\n"


def words(text: str) -> list[str]:
    """Word tokens for comparison.

    A letter/digit boundary is split, because the source PDF sets a scene
    number out in the left margin — "EVENING" and "1" — while screenplain
    renders it hard against the heading. Without this the comparison reports
    a spurious loss on all twenty-five headings.
    """
    text = re.sub(r"(?<=[A-Za-z])(?=\d)", " ", text)
    return re.findall(r"[A-Za-z0-9']+", text.lower())


def verify(pdf_path: Path, fountain_path: Path) -> int:
    """Re-render the Fountain and compare its words against the source PDF."""
    import difflib
    import tempfile

    try:
        from screenplain.main import main as screenplain_main
    except ImportError:
        print("screenplain is not installed. pip install -r "
              "tools/script-convert/requirements.txt", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory() as tmp:
        rendered = Path(tmp) / "rendered.pdf"
        screenplain_main(["--format", "pdf", str(fountain_path), str(rendered)])
        original = "\n".join(
            t for p in fitz.open(pdf_path) for _, _, t, _ in lines_of(p)
        )
        roundtrip = "\n".join(
            t for p in fitz.open(rendered) for _, _, t, _ in lines_of(p)
        )

    a, b = words(original), words(roundtrip)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    lost, gained = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("delete", "replace"):
            lost.extend(a[i1:i2])
        if tag in ("insert", "replace"):
            gained.extend(b[j1:j2])

    print(f"source words:    {len(a)}")
    print(f"round-trip words:{len(b)}")
    print(f"similarity:      {sm.ratio()*100:.3f}%")
    if lost:
        print(f"\nLOST ({len(lost)}): {lost[:60]}")
    if gained:
        print(f"\nGAINED ({len(gained)}): {gained[:60]}")
    if not lost and not gained:
        print("\nNothing lost, nothing invented. Conversion is word-exact.")
        return 0
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("fountain", type=Path)
    ap.add_argument("--verify", action="store_true",
                    help="re-render and compare against the source PDF")
    args = ap.parse_args()

    if args.verify:
        return verify(args.pdf, args.fountain)

    args.fountain.write_text(convert(args.pdf), encoding="utf-8")
    print(f"wrote {args.fountain}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
