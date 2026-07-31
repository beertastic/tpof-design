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
import sys
from pathlib import Path


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


def parse_applicability(md: str) -> tuple[set[int], set[int]]:
    """Which slot numbers take Capture, and which take Anti-synthetic."""
    def slots_after(header_pattern: str) -> set[int]:
        m = re.search(header_pattern, md, flags=re.M)
        if not m:
            return set()
        window = md[m.end(): m.end() + 600]
        pm = re.search(r"Paste with slots?\s+([0-9,\s–\-and]+)", window)
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

    return slots_after(r"^## Capture\b.*$"), slots_after(r"^## Anti-synthetic\b.*$")


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


def build(character: str, slot: dict, blocks: dict, cap: set[int], anti: set[int]) -> str:
    parts = [
        f"[{character.upper()} — SLOT {slot['n']:02d} — {slot['title'].upper()}]",
        f"Output file: {slot['file']}",
        (f"Aspect ratio: {slot['ratio']}"
         + (f"  ({slot['framing'].lower()})" if slot.get("framing") else "")) if slot["ratio"] else "",
        "",
        "Generate a single image to the description below.",
        "Attach actor reference images to this conversation before generating.",
        "",
        "=== STYLE ===", blocks.get("Style", ""), "",
        "=== DO NOT ===", blocks.get("Do Not", ""), "",
    ]
    if slot["n"] in cap and "Capture" in blocks:
        parts += ["=== CAPTURE ===", blocks["Capture"], ""]
    if slot["n"] in anti and "Anti-synthetic" in blocks:
        parts += ["=== SKIN AND REALISM ===", blocks["Anti-synthetic"], ""]
    parts += [
        "=== CHARACTER ===", blocks.get("Character Constants", ""), "",
        "=== THIS IMAGE ===", slot["body"], "",
        f"Deliver a single image at {slot['ratio']}." if slot["ratio"] else "",
    ]
    return "\n".join(p for p in parts if p is not None).strip() + "\n"


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
    cap, anti = parse_applicability(md)
    slots = parse_slots(md)

    outdir = repo / "03-characters" / character / "prompts"
    outdir.mkdir(exist_ok=True)
    for old in outdir.glob("*.txt"):
        old.unlink()

    for slot in slots:
        stem = slot["file"].rsplit(".", 1)[0]
        path = outdir / f"{slot['n']:02d}-{stem}.txt"
        path.write_text(build(character, slot, blocks, cap, anti), encoding="utf-8")

    index = [
        f"# {character} — paste-ready prompts",
        "",
        "One file per image. Each is completely self-contained: open it, select all,",
        "paste into the image generator. Nothing to assemble, nothing to remove.",
        "",
        "Attach actor reference images to the conversation first — see",
        "03-characters/CAST-REFERENCE.md.",
        "",
        "Save each result to source/artwork/ using the exact filename stated at the",
        "top of the prompt, then run:",
        "",
        f"    python tools/board-generator/generate.py {character}",
        "",
        "| File | Image | Ratio | Capture | Skin |",
        "|---|---|---|---|---|",
    ]
    for s in slots:
        stem = s["file"].rsplit(".", 1)[0]
        index.append(
            f"| `{s['n']:02d}-{stem}.txt` | `{s['file']}` | {s['ratio']} | "
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
