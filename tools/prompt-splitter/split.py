#!/usr/bin/env python3
"""Split a character's Prompts.md into paste-ready plain-text prompt files.

Prompts.md stays the source of truth and the human-facing reference. This emits
one self-contained .txt per slot — everything needed, no assembly, no markdown.

  python tools/prompt-splitter/split.py baylan
  python tools/prompt-splitter/split.py --all
"""
from __future__ import annotations

import argparse
import re
from urllib.parse import quote
import sys
from pathlib import Path


RAW_BASE_FALLBACK = "https://raw.githubusercontent.com/beertastic/tpof-design/main"


def raw_base() -> str:
    """Public raw-file base URL for this repository.

    Emitted into every prompt so a connected model can fetch a reference by URL
    instead of guessing a path. Derived from the git remote so a fork does not
    silently point at the original.
    """
    import subprocess
    try:
        url = subprocess.run(["git", "remote", "get-url", "origin"],
                             capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return RAW_BASE_FALLBACK
    m = re.search(r"github\.com[:/](.+?)(?:\.git)?$", url)
    return f"https://raw.githubusercontent.com/{m.group(1)}/main" if m else RAW_BASE_FALLBACK


def raw_url(repo_path: str) -> str:
    """Public raw URL for any path in this repository."""
    return f"{raw_base()}/{quote(str(repo_path).lstrip('/'))}"


ACTOR_EXT = (".jpg", ".jpeg", ".png", ".webp")

# Filenames from 03-characters/CAST-REFERENCE.md, so a numbered list can still
# say what each angle actually is.
ACTOR_ANGLES = {
    "headshot-neutral": "front on, neutral",
    "headshot-profile": "full side profile",
    "headshot-three-quarter": "three-quarter — the most useful working angle",
    "full-body": "standing, whole figure — build and proportion",
}


def actor_refs(character: str) -> list[tuple[int, str, str, str]]:
    """Every actor reference for a character, numbered.

    Returns (n, filename, url, what) so prompts can list them 1, 2, 3 with a
    fetchable URL each.
    """
    d = Path("03-characters") / character / "reference" / "actor"
    if not d.is_dir():
        return []
    files = sorted(f for f in d.iterdir() if f.suffix.lower() in ACTOR_EXT)
    out = []
    for i, f in enumerate(files, 1):
        stem = f.stem.lower()
        what = next((v for k, v in ACTOR_ANGLES.items() if stem.startswith(k)), "")
        url = f"{raw_base()}/{quote(f.as_posix())}"
        out.append((i, f.name, url, what))
    return out


def find_repo_root(start: Path) -> Path:
    for candidate in [start.resolve(), *start.resolve().parents]:
        if (candidate / "03-characters").is_dir() and (candidate / "tools").exists():
            return candidate
    raise SystemExit("Could not locate repository root.")


def demarkdown(text: str) -> str:
    """Strip markdown decoration that is noise inside a prompt."""
    text = re.sub(r"^>\s?", "", text, flags=re.M)          # blockquotes
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text, flags=re.S)  # bold
    text = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", text, flags=re.S)  # italic
    text = re.sub(r"`([^`]+)`", r"\1", text)               # inline code
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)   # links
    text = re.sub(r"^---+$", "", text, flags=re.M)         # rules
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse_blocks(md: str) -> dict[str, str]:
    """Pull the named prompt blocks out of Prompts.md."""
    blocks: dict[str, str] = {}
    wanted = {
        "Style": r"^## Style\b.*$",
        "Do Not": r"^## Do Not\b.*$",
        "Realism": r"^## Realism\b.*$",
        "Capture": r"^## Capture\b.*$",
        "Anti-synthetic": r"^## Anti-synthetic\b.*$",
        "Character Constants": r"^## Character Constants\b.*$",
    }
    for name, pattern in wanted.items():
        m = re.search(pattern, md, flags=re.M)
        if not m:
            continue
        start = m.end()
        nxt = re.search(r"^#{1,2} ", md[start:], flags=re.M)
        end = start + nxt.start() if nxt else len(md)
        body = demarkdown(md[start:end])
        # Drop the leading applicability note — it addresses the human, not the model.
        paras = body.split("\n\n")
        while paras and re.match(r"^(Paste with slots?|Do NOT paste|Narrative slots)", paras[0].strip()):
            paras.pop(0)
        blocks[name] = "\n\n".join(paras).strip()
    return blocks


def parse_applicability(md: str) -> tuple[set[int], set[int], set[int]]:
    """Slots taking Capture, Anti-synthetic, and the full-costume rules."""
    def slots_after(header_pattern: str) -> set[int]:
        m = re.search(header_pattern, md, flags=re.M)
        if not m:
            return set()
        window = md[m.end(): m.end() + 600]
        pm = re.search(r"(?:Paste with|Applies to) slots?\s+([0-9,\s–\-and]+)", window)
        if not pm:
            return set()
        out: set[int] = set()
        for part in re.split(r"[,\s]+", pm.group(1).replace("and", " ")):
            part = part.strip()
            if not part:
                continue
            rng = re.match(r"^(\d+)[–-](\d+)$", part)
            if rng:
                out.update(range(int(rng.group(1)), int(rng.group(2)) + 1))
            elif part.isdigit():
                out.add(int(part))
        return out

    return (slots_after(r"^## Capture\b.*$"),
            slots_after(r"^## Anti-synthetic\b.*$"),
            slots_after(r"^## Costume rules\b.*$"))


def parse_slots(md: str) -> list[dict]:
    """Extract the numbered prompt slots."""
    section = md.split("# Prompt slots", 1)
    if len(section) < 2:
        raise SystemExit("No '# Prompt slots' section found.")
    body = section[1].split("## Output checklist", 1)[0]

    slots = []
    pattern = re.compile(r"^## (\d+)\.\s+`([^`]+)`\s+—\s+(.+)$", flags=re.M)
    matches = list(pattern.finditer(body))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        chunk = body[start:end]
        ratio_m = re.search(r"^\*\*(.+?)\.\*\*\s*$", chunk, flags=re.M)
        raw = ratio_m.group(1).strip() if ratio_m else ""
        rm = re.search(r"(\d+\s*:\s*\d+)", raw)
        ratio = rm.group(1).replace(" ", "") if rm else raw
        framing = raw.split(",")[0].strip() if "," in raw else ""
        if ratio_m:
            chunk = chunk[:ratio_m.start()] + chunk[ratio_m.end():]
        slots.append({
            "n": int(m.group(1)),
            "file": m.group(2),
            "title": m.group(3).strip(),
            "ratio": ratio,
            "framing": framing,
            "body": demarkdown(chunk),
        })
    return slots


def _repo_commit() -> str:
    """The commit the SOURCES were at when this prompt was generated.

    Deliberately NOT part of the hashed body. The content hash must change only
    when the prompt itself changes; a commit id changes on every commit. Both are
    inserted after hashing, so the hash stays stable and the commit id moves.

    Note the off-by-one: the generator runs before you commit, so this names the
    PARENT of the commit the file lands in. That is the useful one — it identifies
    the sources that were read.
    """
    import subprocess
    root = Path(__file__).resolve().parents[2]
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%h %cd", "--date=format:%Y-%m-%d %H:%M"],
            capture_output=True, text=True, timeout=5, cwd=root)
        return out.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


ECHO_TEMPLATE = (
    "BEFORE YOU GENERATE, SAY THIS LINE BACK, WORD FOR WORD:\n"
    "    Working from commit {commit}, prompt {h}.\n"
    "That is your proof you read this file. It is provenance for the human, NOT\n"
    "something to check against the repository — this prompt is self-contained and\n"
    "a cached REPO-STATE.md cannot make it stale. Do not go and look. If you\n"
    "cannot quote it, say so and generate nothing. Never put it in the picture."
)


def _stamp_version(body: str) -> str:
    """Short content hash after the header — an exact "did you read THIS version"
    check. Character counts are not: a connected model reported 28,195 for a file
    that has never been that size, because it counts post-processed text.
    """
    import hashlib
    h = hashlib.sha256(body.encode()).hexdigest()[:8]
    lines = body.split("\n")
    commit = _repo_commit()
    stamp = f"Prompt version: {h} \u00b7 repo commit {commit}"
    echo = ECHO_TEMPLATE.format(commit=commit.split()[0], h=h)
    return "\n".join(lines[:3] + [stamp, "", echo] + lines[3:])


def build(character: str, slot: dict, blocks: dict, cap: set[int], anti: set[int],
          approved: dict | None = None, must: list | None = None,
          handed: str | None = None, costume: set[int] | None = None,
          refs: list | None = None, retrieve: str | None = None) -> str:
    narrative = slot["n"] in cap
    # The share sheet is one image made of many frames, so the single-frame
    # language that closes every other prompt would fight its own description.
    sheet = slot["file"].rsplit(".", 1)[0] == "tone-collage"

    # Any slot showing the person must be anchored to the approved costume.
    gate = slot["n"] in anti
    # Some names in this film belong to well-known characters, and the name alone
    # retrieves that depiction. Same block as the turnarounds carry.
    retrieve_block = ("=" * 68 + "\n"
                      "THE NAME ON THIS PROMPT BELONGS TO A CHARACTER YOU ALREADY KNOW.\n"
                      "DO NOT DRAW THAT CHARACTER.\n"
                      + "=" * 68 + "\n\n" + retrieve.strip() + "\n\n"
                      "Everything you already believe about this name is from a different\n"
                      "production. Discard it. The description below is the only source, and\n"
                      "where your memory and this document disagree, THIS DOCUMENT IS RIGHT."
                      if retrieve else "")

    hand_line = (f"This character is {handed.upper()}-HANDED. All positions are given "
                 f"from\nTHEIR OWN left and right, never the viewer's."
                 if handed and gate else "")
    show_costume = (slot["n"] in costume) if costume else gate
    must_block = ""
    if must and show_costume:
        must_block = ("NON-NEGOTIABLE — THIS IMAGE IS WRONG WITHOUT ALL OF THESE:\n"
                      + "\n".join(f"  {i}. {m.strip()}" for i, m in enumerate(must, 1)))
    ref_note = ""
    if approved and approved.get("reference"):
        ref_note = ("FETCH AND MATCH — the approved costume reference:\n    "
                    + raw_url(approved["reference"]))
    # Approved material and prop plates. The figure prompts no longer describe
    # the plate in full — the plate photograph carries it — so these must attach.
    #
    # A plate is never a reference for ITSELF. Once an approved plate lives in
    # source/artwork/ and is also declared under references:, the slot that
    # generates it would otherwise be handed its own previous version and told
    # to match it — which freezes the image at whatever it was and makes
    # regenerating it pointless. scale_portrait was the first to hit this, on
    # 2026-08-03, the day it became the make-up lock.
    for r in (refs or []):
        if Path(r["path"]).name == slot["file"]:
            continue
        ref_note += (("\n" if ref_note else "")
                     + f"USE THE ATTACHED PHOTOGRAPH — {r['what']}. If not attached, fetch:\n    "
                     + raw_url(f"03-characters/{character}/{r['path']}"))
    # Every actor reference, numbered, each with a fetchable public URL.
    for _n, _name, _url, _what in actor_refs(character):
        _label = f" — {_what}" if _what else ""
        ref_note += (("\n" if ref_note else "")
                     + f"LIKENESS ({_n}){_label} — attached, or fetch:"
                     + f"\n    {_url}")
    if narrative:
        demand = (
            "THIS MUST LOOK LIKE A FRAME FROM A REAL MOTION PICTURE.\n"
            "A photograph made on a real film set, on 35mm anamorphic lenses, of real\n"
            "people wearing real costumes under real light. Not a render, not an\n"
            "illustration, not concept art, not AI-looking output."
        )
    else:
        demand = (
            "THIS MUST LOOK LIKE A REAL REFERENCE PHOTOGRAPH.\n"
            "A studio photograph of real physical objects on a real surface under real\n"
            "light — the kind an art department shoots to document what it has built.\n"
            "Flat, even, sharp across the frame. Not a render, not an illustration,\n"
            "not concept art, not AI-looking output."
        )
    if not gate:
        pass
    parts = [
        f"[{character.upper()} — SLOT {slot['n']:02d} — {slot['title'].upper()}]",
        f"Output file: {slot['file']}",
        (f"Aspect ratio: {slot['ratio']}"
         + (f"  ({slot['framing'].lower()})" if slot.get("framing") else "")) if slot["ratio"] else "",
        "",
        demand,
        "",
        "BEFORE YOU GENERATE — GET THE REFERENCES.",
        "",
        "Every reference this image must match is listed above as a public URL.",
        "For each one: DOWNLOAD it, DECODE it, LOOK at it to confirm it opened, and",
        "MAKE IT AVAILABLE AS AN IMAGE INPUT to the generator. A URL that has been",
        "fetched but never handed to the generator is not a reference, and that gap",
        "is exactly what produced a run of wrong faces on 2026-08-01.",
        "",
        "Do NOT ask for a manual attachment when the download and the handoff both",
        "succeed. Ask only if a URL will not download, a file will not decode, or the",
        "generator cannot receive it — and then name the one that failed.",
        "",
        "Do not proceed from the text alone. The written description is not sufficient",
        "on its own and will produce the wrong costume and the wrong face.",
        "",
        # "face" used to be in this list, which made the COSTUME photograph an
        # authority on the face — the 2026-08-01 failure that came back in a
        # perfect costume on the wrong woman, and a direct contradiction of the
        # face-precedence rule further down this same file. Each photograph is
        # an authority on its own scope and nothing else.
        "THE ATTACHED PHOTOGRAPHS OUTRANK THIS TEXT, EACH WITHIN ITS OWN SCOPE.",
        "Take the COSTUME, materials and colours from the costume photograph.",
        "Take the FACE, HEAD and BUILD from the ACTOR photographs ONLY — never",
        "from the costume photograph, however clearly the face reads in it.",
        "Where a photograph is silent, or is labelled NOT an authority on",
        "something, the written text below wins.",
        "Only the setting, pose and lighting change.",
        "" if gate else None,
        ref_note if gate else None,
        "" if gate else None,
        retrieve_block if retrieve_block else None,
        "" if retrieve_block else None,
        hand_line if hand_line else None,
        "" if hand_line else None,
        must_block if must_block else None,
        "" if must_block else None,
        ("Generate one image, divided into panels, to the description below."
         if sheet else "Generate a single image to the description below."),
        "",
        "=== STYLE ===", blocks.get("Style", ""), "",
        "=== DO NOT ===", blocks.get("Do Not", ""), "",
        "=== PHOTOGRAPHIC REALISM ===", blocks.get("Realism", ""), "",
    ]
    if slot["n"] in cap and "Capture" in blocks:
        parts += ["=== CAPTURE ===", blocks["Capture"], ""]
    if slot["n"] in anti and "Anti-synthetic" in blocks:
        parts += ["=== SKIN AND REALISM ===", blocks["Anti-synthetic"], ""]
    parts += [
        "=== CHARACTER ===", blocks.get("Character Constants", ""), "",
        "=== THIS IMAGE ===", slot["body"], "",
        (("=== CHECK BEFORE YOU FINISH ===\n" + must_block + "\n")
         if must_block else ""),
        (f"Deliver ONE image at {slot['ratio']}, containing all six panels. "
         "Every panel must look photographed, not generated."
         if sheet else
         (f"Deliver a single image at {slot['ratio']}. "
          + ("It must look photographed, not generated."
             if not narrative else
             "It must look like a frame from a real film, not a generated image.")))
        if slot["ratio"] else "",
    ]
    return _stamp_version("\n".join(p for p in parts if p is not None).strip() + "\n")


def run(repo: Path, character: str) -> int:
    src = repo / "03-characters" / character / "Prompts.md"
    if not src.is_file():
        print(f"  skip {character}: no Prompts.md", file=sys.stderr)
        return 0
    md = src.read_text(encoding="utf-8")
    if "# Prompt slots" not in md:
        print(f"  skip {character}: no slots yet", file=sys.stderr)
        return 0
    import re as _re
    st = _re.search(r'^status:\s*"?([a-z-]+)"?', md, flags=_re.M)
    if st and st.group(1) != "ready":
        print(f"  skip {character}: status is '{st.group(1)}', not ready", file=sys.stderr)
        return 0

    blocks = parse_blocks(md)
    cap, anti, costume = parse_applicability(md)
    slots = parse_slots(md)

    approved, must, handed, refs = None, [], None, []
    ofile = repo / "03-characters" / character / "outfits.yaml"
    if ofile.is_file():
        import yaml
        cfg = yaml.safe_load(ofile.read_text(encoding="utf-8")) or {}
        outfits = cfg.get("outfits", [])
        sys.path.insert(0, str(Path(__file__).parent))
        from turnarounds import check_placement
        from consistency import check_slot
        for w in check_placement(character, cfg):
            print(f"  ! {w}", file=sys.stderr)
        # A slot body sits between the two copies of the rules in every prompt,
        # and the generator follows the slot when they disagree.
        for slot in slots:
            if must and ((slot["n"] in costume) if costume else True):
                for w in check_slot(character, slot, must):
                    print(f"  ! {w}", file=sys.stderr)
        handed = cfg.get("handedness")
        retrieve = cfg.get("do_not_retrieve")
        chosen = next((o for o in outfits if (o.get("approved") or {}).get("reference")),
                      outfits[0] if outfits else None)
        if chosen:
            approved = chosen.get("approved") or None
            must = chosen.get("must_show") or []
            refs = chosen.get("references") or []

    outdir = repo / "03-characters" / character / "prompts"
    outdir.mkdir(exist_ok=True)
    for old in outdir.glob("*.txt"):
        old.unlink()

    for slot in slots:
        stem = slot["file"].rsplit(".", 1)[0]
        path = outdir / f"{slot['n']:02d}-{stem}.txt"
        path.write_text(build(character, slot, blocks, cap, anti, approved, must,
                              handed, costume, refs, retrieve), encoding="utf-8")

    index = [
        f"# {character} — paste-ready prompts",
        "",
        "One file per image. Each is completely self-contained: open it, select all,",
        "paste into the image generator. Nothing to assemble, nothing to remove.",
        "",
        "Each prompt lists every photograph it needs as a public URL — fetch",
        "them, do not ask for attachments. See 03-characters/CAST-REFERENCE.md.",
        "",
        "Save each result to source/artwork/ using the exact filename stated at the",
        "top of the prompt, then run:",
        "",
        f"    python tools/board-generator/generate.py {character}",
        "",
        "| File | Image | Ratio | Realism | Anamorphic | Skin |",
        "|---|---|---|---|---|---|",
    ]
    for s in slots:
        stem = s["file"].rsplit(".", 1)[0]
        index.append(
            f"| `{s['n']:02d}-{stem}.txt` | `{s['file']}` | {s['ratio']} | yes | "
            f"{'yes' if s['n'] in cap else '—'} | {'yes' if s['n'] in anti else '—'} |"
        )
    index += [
        "",
        "Generated from `Prompts.md` by `tools/prompt-splitter/split.py`.",
        "**Do not edit these files** — edit `Prompts.md` and regenerate.",
        "",
    ]
    (outdir / "README.md").write_text("\n".join(index), encoding="utf-8")

    print(f"  {character}: {len(slots)} prompts -> {outdir.relative_to(repo)}")
    return len(slots)


def main() -> None:
    ap = argparse.ArgumentParser(description="Split Prompts.md into paste-ready prompt files.")
    ap.add_argument("character", nargs="?")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    if args.all == bool(args.character):
        ap.error("Give one character name or use --all.")

    repo = find_repo_root(Path(__file__).parent)
    names = (
        sorted(p.name for p in (repo / "03-characters").iterdir() if p.is_dir())
        if args.all else [args.character]
    )
    total = sum(run(repo, n) for n in names)
    print(f"\n{total} prompt files written.")


if __name__ == "__main__":
    main()
