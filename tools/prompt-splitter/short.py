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

BUDGET = 3800          # hard ceiling for the FINISHED file, header included. The header, the version stamp and
                       # the echo block are added after trimming and cost about
                       # 500 characters, so the budget has to leave room for them
                       # or the fit guarantee is a lie. The real limit out there
                       # is about 4,000.
RULE_CHARS = 200       # per non-negotiable


def trim(text: str, limit: int) -> str:
    """Cut to `limit`, keeping the sentences that actually constrain the image.

    The naive version kept the first N characters at a sentence boundary, which
    assumes the operative clause comes first. It usually does not. The lead
    sentence names the subject and the constraint follows it:

        "THE ROBE IS A SEPARATE REMOVABLE GARMENT AND IT IS A HEAVY OLD WORKING
         COAT, NOT JEDI DRESS. IT IS NOT WORN IN THE TURNAROUND VIEWS — ..."

    Cut at 92 characters that became a rule saying the coat exists, with the
    instruction not to wear it removed. The generated image duly wore it, and so
    did the pouch that another rule said to hide. Both were read as the model
    disobeying; both were the trim.

    So: always keep the first sentence, since it names the subject. Then prefer
    sentences carrying a hard negation or restriction — those are the ones a
    generation gets wrong — before any remaining prose, and stay inside `limit`.
    """
    flat = " ".join(text.split())
    if len(flat) <= limit:
        return flat

    sentences = [x.strip() for x in re.split(r"(?<=[.!])\s+", flat) if x.strip()]
    if not sentences:
        return flat[:limit]

    HARD = re.compile(r"\b(NOT|NEVER|NO|NOTHING|ONLY|ALWAYS|MUST)\b")
    head, rest = sentences[0], sentences[1:]
    if len(head) > limit:
        return head[:limit].rsplit(" ", 1)[0] + "\u2026"

    def clause(sent: str, room: int):
        """The leading clause, for a constraint too long to keep whole.

        "IT IS NOT WORN IN THE TURNAROUND VIEWS — those record the base costume,
        and a long coat over the top hides the harness..." is 163 characters and
        gets skipped entirely for want of room, which loses the instruction. Its
        first clause is 39 and carries all of the meaning.
        """
        for sep in (" \u2014 ", "; ", ": ", ", and ", ", "):
            if sep in sent:
                first = sent.split(sep)[0].rstrip(",") + "."
                if len(first) <= room:
                    return first
        return None

    chosen, used = [], len(head)
    first_hard = next((i for i, x in enumerate(rest) if HARD.search(x)), None)

    # The FIRST constraint after the subject line is the operative one, and it
    # must survive at any cap. Without this it competes on length with whatever
    # follows: at cap 130 "IT IS NOT WORN IN THE TURNAROUND VIEWS." missed by two
    # characters and lost to "Repaired tears. NO ceremonial drape." — so the rule
    # kept its decoration and dropped its instruction, and the coat got worn.
    if first_hard is not None:
        room = limit - used - 1
        sent = rest[first_hard]
        pick = (sent if len(sent) <= room else clause(sent, room))
        if pick is None and room >= 24:
            pick = sent[:room].rsplit(" ", 1)[0] + "\u2026"
        if pick:
            chosen.append((first_hard, pick))
            used += 1 + len(pick)

    for hard in (True, False):
        for i, sent in enumerate(rest):
            if i == first_hard or bool(HARD.search(sent)) is not hard:
                continue
            if used + 1 + len(sent) <= limit:
                chosen.append((i, sent))
                used += 1 + len(sent)
            elif hard:
                c = clause(sent, limit - used - 1)
                if c:
                    chosen.append((i, c))
                    used += 1 + len(c)

    return " ".join([head] + [t for _, t in sorted(chosen)])


VIEWS = {
    "front":   "Facing camera square on. Shoulders level, head level, looking down the lens.",
    "left":    "Rotated exactly 90° to show their LEFT side in full profile. Head faces the same way as the body.",
    "right":   "Rotated exactly 90° the other way to show their RIGHT side in full profile. Head faces the same way as the body.",
    "back":    "Facing directly away. A ROTATION, NOT A MIRROR — their right side is now on the viewer's LEFT. Show shoulder blades, back seams, the back of the head.",
    "natural": "Three-quarters to camera, standing as this person actually stands. Weight on one leg, a real posture rather than a display position.",
}


def build(character: str, cfg: dict, outfit: dict, view: str, rule_chars: int = RULE_CHARS) -> str:
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

    rules = [trim(m, rule_chars) for m in (outfit.get("must_show") or [])]
    hand = cfg.get("handedness")
    height = outfit.get("height") or cfg.get("height")
    # An outfit may override the file-level block. Baylan needs this: the base
    # turnarounds say the coat is not worn, and the coat set says it is.
    retrieve = (outfit.get("do_not_retrieve_short") or outfit.get("do_not_retrieve")
                or cfg.get("do_not_retrieve_short") or cfg.get("do_not_retrieve"))

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
    # The stamp stays; the instruction to recite it back does not. See
    # ECHO_TEMPLATE below for the measurement that removed it.
    return "\n".join(lines[:3] + [stamp] + lines[3:])


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


# THE ECHO BLOCK IS DELIBERATELY ABSENT FROM THE SHORT PROMPTS. Removed
# 2026-08-01. It asked the model to recite the commit and hash before
# generating, and it lives on in turnarounds.py and split.py, where it is still
# doing a job.
#
# It never fired here. Short prompts are pasted by hand into a fresh chat, and
# in that mode the question it answers — "did you actually open the file?" — is
# already answered by the act of pasting. The connected-repo case in AGENTS.md
# is different and keeps the check.
#
# Tested before removing, rather than assumed. Asked to quote line 5, a run
# replied "the literal fifth line is blank" and then gave the fifth NON-EMPTY
# line correctly. Both true, and not guessable: it held the exact text,
# whitespace included. It simply does not recite the line when its task is to
# make an image. (Asked for line 4 it returned line 3 — so "quote line N" is
# not a reliable check either. Ask for content, not position.)
#
# It cost 401 characters of a 4,000 budget. Because `fit` lowers ONE cap across
# all rules until the file fits, that was ~40 characters off EVERY
# non-negotiable:
#
#     Shada   cap 110 -> 150        Baylan  cap 110 -> 140
#
# Four wrong images this week were rules truncated for want of exactly that
# room. A check that cannot fail, competing against rules that decide whether
# the picture is right, is not a check — it is overhead.


def fit(character: str, cfg: dict, outfit: dict, view: str) -> str:
    """Build the prompt, then tighten the per-rule cap until the whole thing fits.

    BUDGET used to be declared and never applied: `trim` capped each rule at 200
    characters and nothing capped the total, so every line added anywhere pushed
    files over the limit silently. Ten of forty-five were over 4,000 before this
    existed — the exact failure the short prompts were built to prevent.

    Rules are shortened together rather than dropped. A truncated non-negotiable
    still names its subject; a missing one is invisible.
    """
    for cap in range(RULE_CHARS, 70, -10):
        text = build(character, cfg, outfit, view, cap)
        if len(text) <= BUDGET:
            return text
    return text


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
            text = fit(character, cfg, outfit, view)
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
