#!/usr/bin/env python3
"""Generate SHORT paste-ready prompts, sized for an image model's real input.

    python tools/prompt-splitter/short.py baylan
    python tools/prompt-splitter/short.py --all

The long prompts under prompts/ are ~28,000 characters. Image models accept
around 4,000, so everything we send is compressed by the host before it reaches
the generator — lossily, and differently every time. That is why the same prompt
produced a usable costume plate one run and a Jedi character sheet the next: the
top of the file survives compression and the middle does not.

These are written to fit. The long files remain the specification; this is the
thing you actually paste.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
import textwrap
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from split import find_repo_root, actor_refs, raw_url  # noqa: E402

BUDGET = 3600          # target; the hard limit out there is about 4,000
RULE_CHARS = 200       # per non-negotiable


def trim(text: str, limit: int) -> str:
    """Cut to a sentence boundary under `limit`, never mid-word."""
    flat = " ".join(text.split())
    if len(flat) <= limit:
        return flat
    cut = flat[:limit]
    stop = max(cut.rfind(". "), cut.rfind("! "))
    return (cut[:stop + 1] if stop > limit * 0.5 else cut.rsplit(" ", 1)[0] + "…")


VIEWS = {
    "front":   "Facing camera square on. Shoulders level, head level, looking down the lens.",
    "left":    "Rotated exactly 90° to show their LEFT side in full profile. Head faces the same way as the body.",
    "right":   "Rotated exactly 90° the other way to show their RIGHT side in full profile. Head faces the same way as the body.",
    "back":    "Facing directly away. A ROTATION, NOT A MIRROR — their right side is now on the viewer's LEFT. Show shoulder blades, back seams, the back of the head.",
    "natural": "Three-quarters to camera, standing as this person actually stands. Weight on one leg, a real posture rather than a display position.",
}


def build(character: str, cfg: dict, outfit: dict, view: str) -> str:
    approved = (outfit.get("approved") or {}).get("reference")
    gate = approved and view != (outfit.get("approved") or {}).get("view", "front")

    refs = []
    if gate:
        refs.append(f"COSTUME (match exactly): {raw_url(approved)}")
    for r in (outfit.get("references") or []):
        refs.append(f"{r['what'].upper()[:38]}: "
                    f"{raw_url(f"03-characters/{character}/{r['path']}")}")
    for n, name, url, what in actor_refs(character):
        refs.append(f"FACE + BUILD ({n}): {url}")

    rules = [trim(m, RULE_CHARS) for m in (outfit.get("must_show") or [])]
    hand = cfg.get("handedness")
    height = outfit.get("height") or cfg.get("height")
    retrieve = cfg.get("do_not_retrieve_short") or cfg.get("do_not_retrieve")

    parts = [
        f"[{character.upper()} — {outfit['name'].upper()} — {view.upper()}]",
        f"Output file: turn-{outfit['id']}-{view}.png",
        f"Aspect ratio: {cfg.get('ratio', '2:3')} — TALL. Generate at 1024x1536. Never square.",
        "",
        "THIS IS A COSTUME FITTING PHOTOGRAPH — the plain record a costume supervisor takes in a fitting room so the build can be checked. ONE person, alone, standing still, photographed straight on. It is NOT a character sheet and NOT a design board.",
        "NO text, labels, captions, titles, logos, borders or layout. NO second view,",
        "no inset heads, no detail crops, no swatches, no colour palette.",
        "FULL LENGTH — head to below the feet. Not a portrait.",
        "",
        "USE THE ATTACHED PHOTOGRAPHS. They are attached to this message. If nothing",
        "is attached, fetch these URLs instead — and say which route you used:",
        *[f"  {r}" for r in refs],
        "  Take the FACE and BUILD from the actor image only. Hair, beard, age,",
        "  grooming and costume come from the text below and override the photo.",
        "  Do not edit or re-crop that photo — make a new photograph of that person.",
        "  Say whether you used an attached file or a URL. If neither worked, stop.",
        "",
    ]
    if retrieve:
        parts += [trim(retrieve, 420), ""]
    if hand or height:
        bits = []
        if hand:
            bits.append(f"{hand.upper()}-HANDED — sides are given from THEIR own left/right.")
        if height:
            bits.append(trim(height, 90))
        parts += [" ".join(bits), ""]
    parts += ["MUST BE TRUE OF THIS IMAGE:"]
    parts += [f"{i}. {r}" for i, r in enumerate(rules, 1)]
    parts += [
        "",
        f"SHOT: {VIEWS.get(view, '')}",
        "Plain seamless mid-grey studio backdrop. Even, flat, soft frontal light.",
        "Arms ~30° out from the body so nothing overlaps. Sharp throughout, deep",
        "focus, no bokeh, no flare, no vignette. Every strap, seam, buckle and",
        "fastening clearly readable.",
        "",
        "LOOK: a real photograph of a real performer in a real, built costume.",
        "Used-future Star Wars — industrial salvage, nothing factory fresh, muted",
        "and sun-faded. Real skin with pores and lines. Not a render, not concept",
        "art, not AI-looking.",
    ]
    body = "\n".join(parts).strip() + "\n"
    h = hashlib.sha256(body.encode()).hexdigest()[:8]
    lines = body.split("\n")
    commit = _repo_commit()
    stamp = f"Prompt version: {h} (short) \u00b7 repo commit {commit}"
    echo = ECHO_TEMPLATE.format(commit=commit.split()[0], h=h)
    return "\n".join(lines[:3] + [stamp, "", echo] + lines[3:])


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
    "BEFORE YOU GENERATE, SAY THIS LINE BACK TO THE USER, WORD FOR WORD:\n"
    "    Working from commit {commit}, prompt {h}.\n"
    "You cannot know either unless you have read this file, so quoting them is\n"
    "the proof that you did. If you cannot, say so and generate nothing.\n"
    "Never put them in the picture \u2014 they belong in your reply text."
)


def run(repo: Path, character: str) -> int:
    cfg_path = repo / "03-characters" / character / "outfits.yaml"
    if not cfg_path.is_file():
        return 0
    cfg = yaml.safe_load(cfg_path.read_text())
    outdir = repo / "03-characters" / character / "prompts" / "turnarounds-short"
    outdir.mkdir(parents=True, exist_ok=True)
    n = 0
    sizes = []
    for outfit in cfg.get("outfits", []):
        for view in VIEWS:
            text = build(character, cfg, outfit, view)
            (outdir / f"turn-{outfit['id']}-{view}.txt").write_text(text, encoding="utf-8")
            sizes.append(len(text))
            n += 1
    if n:
        print(f"  {character}: {n} short prompts, {min(sizes)}–{max(sizes)} chars "
              f"-> {outdir.relative_to(repo)}")
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("character", nargs="?")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    repo = find_repo_root(Path.cwd())
    names = ([p.name for p in sorted((repo / "03-characters").iterdir()) if p.is_dir()]
             if a.all else [a.character])
    total = sum(run(repo, c) for c in names if c)
    print(f"\n{total} short prompts written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
