#!/usr/bin/env python3
"""Assemble the whole repository into ONE file, for Google NotebookLM.

    ./tools/notebook-export/build.py              # markdown only
    ./tools/notebook-export/build.py --pdf        # markdown + illustrated PDF
    ./tools/notebook-export/build.py --pdf --include-actor-photos

WHY THIS EXISTS. NotebookLM is a retrieval tool over a fixed set of sources. It
cannot walk a git repository, so the repository has to be flattened into it —
and the moment that happens the repository stops being the thing being read.
This script exists so that flattening is REPRODUCIBLE: the export is a build
artefact, regenerated from the tree, never edited by hand. If NotebookLM and the
repository disagree, the repository is right and the export is stale, and the
stamp at the top of the export is how you tell.

WHY EVERY SECTION PRINTS ITS SOURCE PATH. The one thing genuinely lost in the
move is provenance — a notebook answer is grounded in "the document", not in
`03-characters/shin/outfits.yaml`. So every included file is introduced by its
repo-relative path, in the body text where retrieval can actually see it. Ask
the notebook where something came from and it can answer with a path you can
open. That is the whole reason this is not a `cat *.md > out.md`.

WHY TWO OUTPUTS. NotebookLM reads an uploaded `.md` as TEXT ONLY. Markdown image
syntax, relative paths and base64 data URIs are all discarded — there is no way
to get a picture into a notebook through a markdown file. Images survive only
inside a PDF, which NotebookLM does look at. So `--pdf` re-renders the same
content through `tools/build-guide-pdf`'s renderer with the plates placed inline.
The markdown is the complete text; the PDF is the same text plus the artwork.

WHY ACTOR PHOTOGRAPHS ARE OUT BY DEFAULT. Uploading to NotebookLM is uploading
to Google. `reference/actor/` holds photographs of named, real performers, and
`vala/reference/fitting/` is a costume fitting whose subject's permission is
recorded as a standing open risk in the delivery plan. Neither is the art
department's to hand to a third party as a side effect of a tooling test. They
are still LISTED in the image inventory — the export records that they exist and
where they live — but the pixels stay in the repository unless someone passes
`--include-actor-photos` on purpose.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.machinery
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
OUT_MD = REPO / "TPOF-Complete.md"
OUT_PDF = REPO / "TPOF-Complete.pdf"

DOC_EXT = {".md", ".yaml", ".fountain"}
IMG_EXT = {".png", ".jpg", ".jpeg"}

# Directories that are not the project: git internals, the virtualenv, and the
# agent worktrees under .claude/, which are FULL COPIES of the tree at older
# commits. Including those would put three contradictory versions of Baylan's
# costume in front of a retrieval engine, which is the single worst thing that
# could be done to it.
SKIP_DIRS = {".git", ".venv", ".claude", ".idea", "__pycache__", "node_modules",
             "tools"}

# Files excluded from the text export, each for a stated reason. Anything not
# listed here is INCLUDED — the default is comprehensiveness, because the ask
# was "the entire project", and a silent omission is worse than a redundant page.
EXCLUDE = [
    # Superseded. v9 and v10 differ in ways the reconciliation document explains;
    # shipping both gives the notebook two answers to every plot question and no
    # way to prefer one. The reconciliation is included, the old script is not.
    ("02-story/scenes/the-price-of-freedom-v9.fountain", "superseded by v10"),
    # A 62 KB commit-by-commit history of the repository. It is about the work,
    # not the film, and it is the largest single source of stale statements in
    # the tree — every superseded decision appears in it as though it were live.
    ("CHANGELOG.md", "repository history, full of superseded decisions"),
    # Print queues. Pure process — which plate goes to which printer.
    ("_print_list.md", "print queue, not project content"),
]

# Where each top-level directory lands, and in what order. A directory not named
# here still gets exported, at the end, under its own name — so a new `12-`
# folder appears in the next build without anyone editing this list.
PARTS = [
    ("", "Part 1 — Orientation and method"),
    ("01-production-design", "Part 2 — The production design bible"),
    ("02-story", "Part 3 — The screenplay and the story"),
    ("03-characters", "Part 4 — Characters"),
    ("04-factions", "Part 5 — Factions"),
    ("05-props", "Part 6 — Props"),
    ("06-vehicles", "Part 7 — Vehicles"),
    ("07-locations", "Part 8 — Locations"),
    ("08-species", "Part 9 — Species and creatures"),
    ("09-prompt-library", "Part 10 — The prompt library"),
    ("10-assets", "Part 11 — Shared assets"),
    ("11-production-tracking", "Part 12 — Production tracking, TODO lists and open questions"),
]

# Read these first within their part. Everything else follows alphabetically.
# The point is that a reader — human or model — meets the orienting document
# before the detail, and the delivery plan before the eleven TODO lists it ranks.
ORDER = {
    "": ["README.md", "REPO-STATE.md", "AGENTS.md", "CONTRIBUTING.md"],
    "02-story": ["README.md", "Scene-Index.md",
                 "scenes/the-price-of-freedom-v10.fountain",
                 "Scene-Elements.md", "Planted-Elements.md"],
    "03-characters": ["README.md", "CAST-REFERENCE.md", "APPROVAL.md",
                      "Character-Build-Recipe.md", "Character-Template.md",
                      "NEXT-CHARACTERS-BRIEF.md"],
    "11-production-tracking": ["Production-Status.md",
                               "Delivery-Plan-2026-08-14.md",
                               "Open-Questions.md", "Image-Manifest.md"],
}

# Characters in story order rather than alphabetical, so the notebook meets the
# two leads before the background crew. Anyone not listed follows, alphabetically.
CHARACTER_ORDER = ["baylan", "shin", "vala", "jeyin", "krellis", "captain-jasu",
                   "shada", "nyx", "reya-fenn", "yaslo-bis", "mercenary-kit",
                   "palpatine"]

# Real people. See the module docstring.
PRIVATE_IMG = ["/reference/actor/", "/reference/fitting/"]

# Staged copies. `prompts/attach/` and `evolution/attachments/` are populated by
# the prompt tooling, which copies the SAME reference plate into a folder per
# prompt so a generation can be run by dragging one directory in. 84 of the 244
# images in the tree are copies of this kind — Baylan's three face-build
# photographs appear eight times each. They are listed in the inventory, because
# an inventory that hides copies is how a plate gets edited in one place and not
# the other, but they are never PLACED in the PDF: printing one picture eight
# times teaches nothing and costs eight pages.
STAGED_IMG = ["/prompts/attach/", "/evolution/attachments/"]


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(REPO), *args],
                              capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return "unknown"


def excluded(rel: str) -> str | None:
    for pat, why in EXCLUDE:
        if rel == pat or rel.endswith("/" + pat) or rel.endswith(pat):
            return why
    return None


def docs() -> list[Path]:
    out = []
    for p in sorted(REPO.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in DOC_EXT:
            continue
        if set(p.relative_to(REPO).parts) & SKIP_DIRS:
            continue
        # The export lands in the repository root as a `.md`, so a second run
        # would otherwise ingest the first run's output — the word count doubled
        # from 277k to 554k the first time this happened, and the second copy is
        # the one that goes stale.
        if p in {OUT_MD, OUT_PDF}:
            continue
        out.append(p)
    return out


def images(include_private: bool) -> list[Path]:
    out = []
    for p in sorted(REPO.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in IMG_EXT:
            continue
        rel = p.relative_to(REPO)
        if set(rel.parts) & SKIP_DIRS:
            continue
        if not include_private and any(k in "/" + str(rel) for k in PRIVATE_IMG):
            continue
        out.append(p)
    return out


def is_private(p: Path) -> bool:
    return any(k in "/" + str(p.relative_to(REPO)) for k in PRIVATE_IMG)


def is_staged(p: Path) -> bool:
    return any(k in "/" + str(p.relative_to(REPO)) for k in STAGED_IMG)


def plates(all_imgs: list[Path], include_private: bool) -> list[Path]:
    """The images actually worth placing in the PDF: one copy of each.

    Deduplicated by CONTENT, not by name — the staged copies keep their original
    filenames but several canonical plates are also byte-identical to each other
    across folders, and only a hash catches those.
    """
    seen: set[str] = set()
    out = []
    for p in all_imgs:
        if is_staged(p):
            continue
        if not include_private and is_private(p):
            continue
        h = hashlib.md5(p.read_bytes()).hexdigest()
        if h in seen:
            continue
        seen.add(h)
        out.append(p)
    return out


def part_of(rel: Path) -> str:
    top = rel.parts[0] if len(rel.parts) > 1 else ""
    return top if any(top == k for k, _ in PARTS) else (
        "" if len(rel.parts) == 1 else top)


def sort_key(rel: Path, part: str):
    r = str(rel.relative_to(part)) if part else str(rel)
    hints = ORDER.get(part, [])
    rank = hints.index(r) if r in hints else len(hints)
    if part == "03-characters" and len(rel.parts) > 2:
        who = rel.parts[1]
        crank = (CHARACTER_ORDER.index(who) if who in CHARACTER_ORDER
                 else len(CHARACTER_ORDER))
        # Character.md, then the lock, then the costume spec, then the rest.
        fname = rel.name
        frank = {"Character.md": 0, "Character-Lock.md": 1,
                 "outfits.yaml": 2}.get(fname, 3)
        return (len(hints) + 1, crank, who, frank, r)
    return (rank, 0, "", 0, r)


HEADING = re.compile(r"^(#{1,6})(\s)")


def demote(text: str, by: int = 2) -> str:
    """Push every heading down `by` levels so the export has one hierarchy.

    Without this, forty files each starting at `#` produce forty documents in a
    trenchcoat and no table of contents worth having.
    """
    out = []
    fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence:
            m = HEADING.match(line)
            if m:
                level = min(len(m.group(1)) + by, 6)
                line = "#" * level + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)


def strip_frontmatter(text: str) -> tuple[str, str]:
    """Return (body, one-line summary of the frontmatter)."""
    if not text.startswith("---"):
        return text, ""
    end = text.find("\n---", 3)
    if end == -1:
        return text, ""
    fm = text[3:end]
    body = text[text.find("\n", end + 1) + 1:]
    bits = []
    for line in fm.splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, v = line.split(":", 1)
            if k.strip() in {"title", "asset_id", "version", "status"}:
                bits.append(f"{k.strip()}: {v.strip().strip('\"')}")
    return body, " · ".join(bits)


SRC_FIGURE_RE = re.compile(r"^@figure\s+(\{.*\})\s*$", re.M)


def humanise_figures(text: str) -> str:
    """Rewrite source `@figure {json}` directives as a readable sentence.

    Shopping lists carry these for `build-guide-pdf`, which turns them into
    pictures. The PDF export keeps them for exactly that reason. The MARKDOWN
    export cannot show a picture, and leaving the raw JSON in place gives a
    retrieval tool a line of punctuation to index instead of the caption and the
    path — which is the one part of a figure that survives as text.
    """
    def one(m: re.Match) -> str:
        try:
            cols = json.loads(m.group(1)).get("cols") or []
        except ValueError:
            return m.group(0)
        bits = []
        for c in cols:
            cap = c.get("caption") or Path(c.get("src", "")).stem
            scope = f" — {c['scope']}" if c.get("scope") else ""
            bits.append(f"{cap}{scope} (`{c.get('src', '')}`)")
        if not bits:
            return ""
        return "*Figure — " + "; ".join(bits) + ".*"

    return SRC_FIGURE_RE.sub(one, text)


def redact_figures(text: str) -> str:
    """Drop withheld images from source `@figure` directives, for the PDF.

    THE PRIVACY EXCLUSION HAS TWO DOORS AND THIS IS THE SECOND ONE. Plates this
    script places itself are filtered by `plates()`. But shopping lists carry
    their OWN `@figure` directives, written by `tools/build-lists`, and two of
    them point straight at `vala/reference/fitting/` — so the first PDF build
    rendered a costume fitting the exclusion was supposed to hold back. Filtering
    only what this script chooses to place is not the same as filtering what ends
    up on the page.
    """
    def one(m: re.Match) -> str:
        try:
            spec = json.loads(m.group(1))
        except ValueError:
            return m.group(0)
        cols = spec.get("cols") or []
        keep = [c for c in cols
                if not any(k in "/" + c.get("src", "") for k in PRIVATE_IMG)]
        if len(keep) == len(cols):
            return m.group(0)
        note = ("*A figure here is withheld: it is a photograph of a real "
                "person. See the image inventory for what it is and where it "
                "lives.*")
        if not keep:
            return note
        spec["cols"] = keep
        return "@figure " + json.dumps(spec) + "\n\n" + note

    return SRC_FIGURE_RE.sub(one, text)


def describe(p: Path) -> str:
    """A human sentence for an image, from its path and any staged manifest."""
    rel = p.relative_to(REPO)
    man = p.parent / "MANIFEST.txt"
    if man.is_file():
        txt = man.read_text(encoding="utf-8", errors="replace")
        block = re.search(re.escape(p.name) + r"\n((?:\s{2,}.*\n)+)", txt)
        if block:
            scope = re.search(r"scope\s*:\s*(.+)", block.group(1))
            if scope:
                return scope.group(1).strip()
    stem = re.sub(r"^\d+[-_]", "", p.stem).replace("-", " ").replace("_", " ")
    return stem.strip().capitalize() or rel.name


def image_section(placed: list[Path], all_paths: list[Path]) -> str:
    """The inventory. Every image in the repository, listed with its path.

    Includes the withheld and the duplicated ones, both marked — an inventory
    that quietly omits rows is how someone later concludes a photograph was
    never taken, or edits one copy of a plate and not the other seven.
    """
    n_staged = sum(1 for p in all_paths if is_staged(p))
    n_private = sum(1 for p in all_paths if is_private(p))
    lines = [
        "",
        f"The repository holds **{len(all_paths)} image files**, of which "
        f"**{len(placed)} are distinct plates** — the remainder are staged "
        "copies, deduplicated here by content. This table is the complete "
        "index, copies included. Paths are repo-relative and are the "
        "authoritative location of each image: this document carries the "
        "record, the repository carries the file, and the illustrated PDF "
        "build carries the picture.",
        "",
        "| | |",
        "|---|---|",
        f"| Distinct plates | **{len(placed)}** |",
        f"| Staged copies — `prompts/attach/`, `evolution/attachments/` | {n_staged} |",
        f"| Photographs of real people, withheld from the PDF | {n_private} |",
        f"| Total image files | **{len(all_paths)}** |",
        "",
        "| Image | Where it lives | What it is |", "|---|---|---|"]
    for p in all_paths:
        rel = p.relative_to(REPO)
        mark = ""
        if is_private(p):
            mark = " *(withheld from the PDF — photograph of a real person)*"
        elif is_staged(p):
            mark = " *(staged copy)*"
        lines.append(f"| `{rel.name}` | `{rel.parent}` | {describe(p)}{mark} |")
    return "\n".join(lines)


def figures_for(prefix: str, imgs: list[Path], used: set[Path],
                per_row: int = 3) -> str:
    """`@figure` directives for the PDF build; invisible in the markdown.

    `used` is carried across calls so no plate is placed twice — the per-part
    pass and the catch-all at the end would otherwise both claim the same file.
    """
    sel = [p for p in imgs
           if p not in used and str(p.relative_to(REPO)).startswith(prefix)]
    if not sel:
        return ""
    used.update(sel)
    out = []
    for i in range(0, len(sel), per_row):
        cols = [{"src": str(p.relative_to(REPO)), "caption": describe(p)}
                for p in sel[i:i + per_row]]
        out.append("@figure " + json.dumps({"cols": cols}))
    return "\n\n".join(out)


def build_markdown(imgs: list[Path], all_imgs: list[Path],
                   for_pdf: bool, include_private: bool = False) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    sha, subject = git("rev-parse", "--short", "HEAD"), git("log", "-1", "--format=%s")
    files = docs()
    kept = [p for p in files if not excluded(str(p.relative_to(REPO)))]
    dropped = [(str(p.relative_to(REPO)), excluded(str(p.relative_to(REPO))))
               for p in files if excluded(str(p.relative_to(REPO)))]

    L: list[str] = []
    w = L.append

    w("# The Price of Freedom — complete project export")
    w("")
    w(f"**Generated {stamp}** from commit `{sha}` — *{subject}* — by "
      "`tools/notebook-export/build.py`.")
    w("")
    w("## What this document is, and what it is not")
    w("")
    w("This is the entire art-department repository for *The Price of Freedom*, "
      "flattened into one file so it can be read by a retrieval tool that "
      "cannot walk a git repository. It contains the shooting script, every "
      "character document and costume specification, the production design "
      "bible, the factions, locations, vehicles and creatures, the prompt "
      "library the artwork is generated from, and every production tracking "
      "and TODO document including the open questions that are still unanswered.")
    w("")
    w("> **The repository is the source of truth. This file is a copy, and a "
      "copy goes stale.** It was generated at the stamp above. If this document "
      "and the repository disagree, the repository is right. Nothing in here "
      "should be edited — regenerate it instead.")
    w("")
    w("**Every section below names the file it came from**, as a repo-relative "
      "path, immediately under its heading. When you ask this document a "
      "question, that path is the answer to *\"where is this actually written "
      "down?\"* — it is how provenance survives the trip out of the repository.")
    w("")
    w("### A note on how to read the tracking documents")
    w("")
    w("This is a live production, nine days from a delivery date, and the "
      "repository records arguments as well as conclusions. Two conventions "
      "matter when reading it:")
    w("")
    w("- A **`NEEDS:`** marker is an unanswered design question, not a "
      "description. There are dozens, and they are deliberate — they mark the "
      "places where nothing has been decided yet.")
    w("- A **struck-through line in `Open-Questions.md`** is a question that has "
      "been *answered*; the answer follows it. An unstruck line is still open.")
    w("")
    if dropped:
        w("### What was deliberately left out")
        w("")
        w("| File | Why |")
        w("|---|---|")
        for rel, why in sorted(dropped):
            w(f"| `{rel}` | {why} |")
        w("")
    w("---")
    w("")

    # Contents
    w("## Contents")
    w("")
    grouped: dict[str, list[Path]] = {}
    for p in kept:
        rel = p.relative_to(REPO)
        grouped.setdefault(part_of(rel), []).append(p)
    # Empty parts are listed too. `05-props/` holds nothing, and that absence is
    # itself a tracked production problem — the torn metal that kills Jeyin has
    # no entry. A contents page that silently skipped it would hide the gap.
    ordered_parts = list(PARTS)
    ordered_parts += [(k, k) for k in sorted(grouped) if
                      k not in {a for a, _ in PARTS}]
    for key, title in ordered_parts:
        n_docs = len(grouped.get(key, []))
        w(f"- **{title}** — "
          + (f"{n_docs} documents" if n_docs else "*empty — see below*"))
    w("- **Part 13 — Complete image inventory** — "
      f"{len(all_imgs)} images")
    w("")
    w("---")
    w("")

    used: set[Path] = set()
    for key, title in ordered_parts:
        w(f"# {title}")
        w("")
        # Characters place their plates per character, further down. Every other
        # part places its whole set here, under the part heading.
        #
        # THE ROOT PART IS SKIPPED, and that is not a detail. Its key is the
        # empty string, so `startswith("")` matched every path in the tree and
        # the first build placed all 101 plates in the opening pages of Part 1,
        # before the reader had met a single character. Root-level images are
        # picked up by the catch-all at the end instead.
        if for_pdf and key not in {"03-characters", ""}:
            figs = figures_for(f"{key}/", imgs, used)
            if figs:
                w(figs)
                w("")
        if not grouped.get(key):
            w(f"**`{key}/` contains no documents.** This is a real gap in the "
              "production, not an omission by this export. For props "
              "specifically: the torn metal that impaled Jeyin in the Scene 2 "
              "crash has no entry, and it is the one prop that kills a "
              "principal — her wound is on screen from Scene 8 and a prosthetic "
              "has to match something. See `Open-Questions.md`.")
            w("")
            w("---")
            w("")
            continue
        group = sorted(grouped[key], key=lambda p: sort_key(p.relative_to(REPO), key))
        last_char = None
        for p in group:
            rel = p.relative_to(REPO)

            # Characters get a divider so eleven costume packs do not run
            # together into one undifferentiated wall.
            if key == "03-characters" and len(rel.parts) > 2:
                who = rel.parts[1]
                if who != last_char:
                    last_char = who
                    w(f"## {who.replace('-', ' ').title()}")
                    w("")
                    w(f"*All documents below are from `03-characters/{who}/`.*")
                    w("")
                    if for_pdf:
                        figs = figures_for(f"03-characters/{who}/", imgs, used)
                        if figs:
                            w(figs)
                            w("")

            raw = p.read_text(encoding="utf-8", errors="replace")
            body, fm = strip_frontmatter(raw)
            if not for_pdf:
                body = humanise_figures(body)
            elif not include_private:
                body = redact_figures(body)
            depth = 3 if (key == "03-characters" and len(rel.parts) > 2) else 2
            w("#" * depth + f" {rel.name}")
            w("")
            w(f"> **Source file:** `{rel}`" + (f"  \n> {fm}" if fm else ""))
            w("")

            if p.suffix == ".yaml":
                w("*The costume specification, verbatim. This is the file the "
                  "image prompts are generated from — where it and any prose "
                  "description disagree, this wins.*")
                w("")
                w("```yaml")
                w(body.rstrip())
                w("```")
            elif p.suffix == ".fountain":
                w("*Screenplay in Fountain format. Scene headings begin `INT.` "
                  "or `EXT.`; a line in capitals before dialogue is the "
                  "character speaking.*")
                w("")
                w(demote(body.rstrip(), by=depth))
            else:
                w(demote(body.rstrip(), by=depth - 1))
            w("")
            w("---")
            w("")

    w("# Part 13 — Complete image inventory")
    w("")
    # Anything the per-part pass did not claim — a plate at the repository root,
    # or in a directory added since PARTS was last edited. Placing it here is
    # ugly; dropping it silently is worse.
    if for_pdf:
        figs = figures_for("", imgs, used)
        if figs:
            w("**Plates not filed under any part above.**")
            w("")
            w(figs)
            w("")
    w(image_section(imgs, all_imgs))
    w("")
    w("---")
    w("")
    w(f"*End of export. Generated {stamp} from commit `{sha}`. "
      "Regenerate with `./tools/notebook-export/build.py`.*")
    return "\n".join(L)


def render_pdf(md: str) -> None:
    spec = importlib.util.spec_from_loader(
        "bgpdf", importlib.machinery.SourceFileLoader(
            "bgpdf", str(REPO / "tools" / "build-guide-pdf")))
    bg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bg)

    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate

    st = bg.styles()
    margin = 17 * mm
    width = A4[0] - 2 * margin

    def furniture(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(bg.MUTED)
        canvas.drawString(margin, 11 * mm, "The Price of Freedom — complete export")
        canvas.drawRightString(A4[0] - margin, 11 * mm, f"page {doc.page}")
        canvas.drawCentredString(A4[0] / 2, 11 * mm,
                                 "generated from the repository — do not annotate this copy")
        canvas.setStrokeColor(bg.RULE)
        canvas.line(margin, 15 * mm, A4[0] - margin, 15 * mm)
        canvas.restoreState()

    doc = BaseDocTemplate(
        str(OUT_PDF), pagesize=A4, leftMargin=margin, rightMargin=margin,
        topMargin=margin, bottomMargin=22 * mm,
        title="The Price of Freedom — complete project export",
        author="TPOF Art Department")
    doc.addPageTemplates([PageTemplate(
        id="p", frames=[Frame(margin, 22 * mm, width,
                              A4[1] - margin - 22 * mm, id="f")],
        onPage=furniture)])
    with tempfile.TemporaryDirectory(prefix="tpof-nb-") as td:
        doc.build(bg.build_flowables(md, st, width, Path(td), REPO))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true",
                    help="also render an illustrated PDF with the plates inline")
    ap.add_argument("--include-actor-photos", action="store_true",
                    help="include photographs of real performers (off by default)")
    a = ap.parse_args()

    all_imgs = images(include_private=True)
    imgs = plates(all_imgs, include_private=a.include_actor_photos)

    md = build_markdown(imgs, all_imgs, for_pdf=False,
                        include_private=a.include_actor_photos)
    OUT_MD.write_text(md, encoding="utf-8")
    words = len(md.split())
    print(f"{OUT_MD.relative_to(REPO)}  "
          f"{OUT_MD.stat().st_size/1_048_576:.2f} MB  {words:,} words")
    if words > 500_000:
        print("  WARNING: over NotebookLM's 500,000-word per-source limit.")
    print(f"  {len(all_imgs)} image files, {len(imgs)} distinct plates")

    held = sum(1 for p in all_imgs if is_private(p))
    if held and not a.include_actor_photos:
        print(f"  {held} withheld (photographs of real people); "
              "listed in the inventory, pixels not exported")

    if a.pdf:
        print("  rendering PDF, this takes a few minutes ...")
        render_pdf(build_markdown(imgs, all_imgs, for_pdf=True,
                                  include_private=a.include_actor_photos))
        print(f"{OUT_PDF.relative_to(REPO)}  "
              f"{OUT_PDF.stat().st_size/1_048_576:.2f} MB  "
              f"{len(imgs)} plates inline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
