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
RULE_CHARS = 4000      # per non-negotiable — the CEILING the search starts from, not a target.
                       # It was 200 until 2026-08-03, and `fit()` only ever searched
                       # DOWNWARD from it, so a rule was cut to 200 characters even when
                       # the file had a thousand characters of unused budget. Three of the
                       # four mercenaries were losing 30-40% of their specification to a
                       # cap that no budget required. Measured, before and after:
                       #
                       #     merc-2   70% -> 100%     merc-1         39% -> 80%
                       #     merc-3   69% -> 100%     baylan/coat    39% -> 48%
                       #     merc-4   61% -> 100%
                       #
                       # No budget was raised to get that; the files still fit in 3,800.
                       # Shada, Jasu and baylan/working are unmoved — they are genuinely
                       # budget-bound, and fix 2 (shorter rules) is the only thing left.
MIN_RULE_CHARS = 70    # below this a rule stops naming its own subject


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


# Each view states WHICH OF THEIR SIDES THE CAMERA CANNOT SEE, and forbids moving
# a hidden piece round to the visible side.
#
# Added 2026-08-03, from an A/B where both arms failed identically. Scored by HER
# side, the left-profile results were: shoulder cap (her left) correct, knife
# (her left) correct, thigh patch (her left) correct — gauntlet (her right) on
# the wrong arm, blaster (her right) on the wrong side. Three for three on the
# near side, nought for two on the far side.
#
# That is not left/right confusion, which was the standing diagnosis and which
# would have scattered the errors. It is a VISIBILITY BIAS: nothing that belonged
# on the hidden side survived being hidden. The gauntlet is the most emphatically
# described object in Shada's costume — "THE ONLY RIGID THING SHE WEARS" — and
# emphasis is precisely what drags an occluded piece round into shot.
#
# Raising the budget cannot fix it: the 3,800 and 8,000 prompts failed the same
# way. What was missing was permission for a limb to be EMPTY.
def _label(what: str, limit: int) -> str:
    """A reference's scope line, cut at a sentence or word boundary.

    It used to be `what.upper()[:38]`, a hard character cut, which put
    "THE SCALE PLATES — SIZE AND FINISH. WH:" in front of every Shada prompt —
    a label severed mid-word. A reference label is the one line that tells the
    generator what an attached image may and may not be trusted for, so it has
    to survive whole. Prefer the first sentence; fall back to a word boundary.
    """
    flat = " ".join(str(what).split()).upper()
    first = flat.split(". ")[0].rstrip(".")
    if len(first) <= limit:
        return first
    return flat[:limit].rsplit(" ", 1)[0].rstrip(",;—-")


VIEWS = {
    "front":   "Facing camera square on. Shoulders level, head level, looking down the lens. "
               "BOTH SIDES VISIBLE — THEIR RIGHT IS ON THE VIEWER'S LEFT. Every asymmetric piece must be present.",
    "left":    "Rotated exactly 90° to show their LEFT side in full profile. Head faces the same way as the body. "
               "OCCLUSION — THEIR WHOLE RIGHT SIDE IS BEHIND THEM AND CANNOT BE SEEN: right shoulder, right arm, "
               "right forearm, right hand, right hip and right thigh are all hidden by the body. ANYTHING THE RULES "
               "PLACE ON THEIR RIGHT DOES NOT APPEAR IN THIS IMAGE AT ALL. Do NOT bring it round to the near side to "
               "show it, and do NOT copy it onto the left. A near-side limb carrying nothing is BARE, and bare is CORRECT.",
    "right":   "Rotated exactly 90° the other way to show their RIGHT side in full profile. Head faces the same way as the body. "
               "OCCLUSION — THEIR WHOLE LEFT SIDE IS BEHIND THEM AND CANNOT BE SEEN: left shoulder, left arm, "
               "left forearm, left hand, left hip and left thigh are all hidden by the body. ANYTHING THE RULES "
               "PLACE ON THEIR LEFT DOES NOT APPEAR IN THIS IMAGE AT ALL. Do NOT bring it round to the near side to "
               "show it, and do NOT copy it onto the right. A near-side limb carrying nothing is BARE, and bare is CORRECT.",
    "back":    "Facing directly away. A ROTATION, NOT A MIRROR — because they turned, THEIR RIGHT IS NOW ON THE VIEWER'S "
               "RIGHT, the opposite of the front view. BOTH SIDES VISIBLE, nothing occluded, every asymmetric piece present. "
               "Show shoulder blades, back seams, rear pockets, the back of the head. No face, no front closure.",
    "natural": "Three-quarters to camera, standing as this person actually stands. Weight on one leg, a real posture rather "
               "than a display position. THE FAR SIDE IS PARTLY TURNED AWAY — a piece on it may be partly hidden, and that is "
               "CORRECT. Do not rotate it into view or move it to the near side.",
}


def reference_list(character: str, outfit: dict, view: str) -> list[tuple[str, str, str]]:
    """Every reference this view needs: (label, repo-relative path, url).

    ONE list, used both to write the prompt's attachment block and to stage the
    files on disk. They used to be derived separately — the prompt from here, the
    operator's list from whatever a document happened to say — and by 2026-08-03
    the repository held FIVE different answers to "what do I attach", none of
    which matched the five this function returns. The result was three
    generations run with two of five references attached, including the approved
    costume front, which is the image the whole turnaround method is built on.

    Deriving both from one list is the fix. A list that cannot drift cannot
    disagree with itself.
    """
    out = []
    approved = (outfit.get("approved") or {}).get("reference")
    # A view cannot match itself, so the approved view never gets its own image.
    if approved and view != (outfit.get("approved") or {}).get("view", "front"):
        out.append(("COSTUME (match exactly)", approved, raw_url(approved)))
    for r in (outfit.get("references") or []):
        p = f"03-characters/{character}/{r['path']}"
        out.append((_label(r["what"], 52), p, raw_url(p)))
    for n, name, url, what in actor_refs(character):
        out.append((f"FACE + BUILD ({n})", f"03-characters/{character}/reference/actor/{name}", url))
    return out


def build(character: str, cfg: dict, outfit: dict, view: str, rule_chars: int = RULE_CHARS) -> str:
    refs = [f"{label}: {url}" for label, _, url in reference_list(character, outfit, view)]

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
        # A character with no references at all used to get this block anyway,
        # listing nothing and still ending "if neither worked, stop" — an
        # instruction to abort over a photograph that was never named. Captain
        # Jasu is the first uncast principal to reach this generator.
        *([
            "USE THE ATTACHED PHOTOGRAPHS. They are attached to this message. If nothing",
            "is attached, fetch these URLs instead — and say which route you used:",
            *[f"  {r}" for r in refs],
            "  Take the FACE and BUILD from the actor image only. Hair, beard, age,",
            "  grooming and costume come from the text below and override the photo.",
            "  Do not edit or re-crop that photo — make a new photograph of that person.",
            "  Say whether you used an attached file or a URL. If neither worked, stop.",
            "",
        ] if refs else [
            "NOT YET CAST — THERE IS NO REFERENCE PHOTOGRAPH AND YOU MUST NOT INVENT",
            "A LIKENESS OF A REAL PERSON. Build the face from the written description",
            "alone: an ordinary, unremarkable, plausible human being who could exist,",
            "photographed in a fitting room. Do not resemble any actor or public figure.",
            "",
        ]),
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


def payload(text: str) -> int:
    """Length of the prompt, not counting reference URLs.

    REFERENCE URLS DO NOT COUNT AGAINST THE BUDGET, from 2026-08-01. They are
    fixed overhead rather than prose, and they do not make a prompt "long" in the
    sense this budget exists to prevent — nobody skims a URL.

    Counting them was actively harmful. Captain Jasu reached five reference
    images, whose links came to 1,406 characters of the 4,000, and the cap
    collapsed to the floor of 80: every non-negotiable was truncated mid-clause
    to pay for links to the pictures that prove them. The rules were funding
    their own references out of the same purse.
    """
    links = sum(len(l) + 1 for l in text.split("\n") if "https://" in l)
    return len(text) - links


def fit(character: str, cfg: dict, outfit: dict, view: str,
        budget: int = None) -> tuple[str, int]:
    """Find the LARGEST per-rule cap whose prompt still fits the budget.

    Returns the prompt and the cap it settled on.

    BUDGET used to be declared and never applied: `trim` capped each rule at 200
    characters and nothing capped the total, so every line added anywhere pushed
    files over the limit silently. Ten of forty-five were over 4,000 before this
    existed — the exact failure the short prompts were built to prevent.

    The search used to run downward from 200 and stop at the first cap that fit,
    which quietly made 200 a target rather than a ceiling: an outfit whose whole
    prompt came to 2,458 characters against a 3,800 budget still had every rule
    cut to 200, and lost 30% of its specification to spare capacity. It now
    searches for the largest cap that fits, so a small specification is sent
    whole and only a genuinely oversized one is trimmed.

    Rules are shortened together rather than dropped. A truncated non-negotiable
    still names its subject; a missing one is invisible.
    """
    budget = BUDGET if budget is None else budget

    text = build(character, cfg, outfit, view, RULE_CHARS)
    if payload(text) <= budget:
        return text, RULE_CHARS

    # Largest cap that fits. payload is monotonic in the cap, so bisect.
    lo, hi = MIN_RULE_CHARS, RULE_CHARS
    best, best_cap = build(character, cfg, outfit, view, lo), lo
    while lo <= hi:
        mid = (lo + hi) // 2
        t = build(character, cfg, outfit, view, mid)
        if payload(t) <= budget:
            best, best_cap = t, mid
            lo = mid + 1
        else:
            hi = mid - 1
    return best, best_cap


def losses(outfit: dict, cap: int) -> list[tuple[int, str, list[str]]]:
    """Which sentences of which rules did not survive the trim.

    Fix 1 of `11-production-tracking/Prompt-Reliability-TODO.md`. The run used to
    print "5 short prompts, 4466-4538 chars" and nothing else: `trim()` appends
    an ellipsis only when it cuts mid-sentence, so whole dropped sentences left
    no mark at all. Counting ellipses found 1 truncated rule in 67; measuring
    content found 89% of Shada's specification missing.

    Every one of the five recorded failures was a rule that existed, was correct,
    and was cut before the generator saw it. This is the report that would have
    shown that at the time.
    """
    out = []
    for i, rule in enumerate((outfit.get("must_show") or []), 1):
        kept = trim(rule, cap)
        flat = " ".join(rule.split())
        if kept == flat:
            continue
        gone = []
        for sent in [x.strip() for x in re.split(r"(?<=[.!])\s+", flat) if x.strip()]:
            if sent in kept:
                continue
            # A sentence kept only as its leading clause is cut, not dropped.
            stem = re.split(r" — |; |: |, and |, ", sent)[0].rstrip(",")
            gone.append(("cut   " if stem and stem in kept else "DROPPED", sent))
        if gone:
            subject = flat.split(".")[0][:48]
            out.append((i, subject, gone))
    return out


def _slug(label: str, n: int) -> str:
    """A filename that carries the reference's SCOPE, not just its subject.

    The filename travels with the image into the chat and is part of what the
    model sees, so "2-plate-shape-and-finish-not-size.png" is doing work that
    "material-scale.png" is not. Every reference failure in this production has
    been an image used for something it was not scoped to.
    """
    s = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    return f"{n}-{s}"


def stage_attachments(repo: Path, character: str, outfit: dict) -> tuple[int, list[str]]:
    """Copy every reference this outfit needs into one folder, ready to drag in.

    Written 2026-08-03 because "hunt down five images across three directories,
    every time, for every image" is a description of a step rather than a step —
    the same reasoning that produced tools/regen. The operator was attaching two
    of five, which is not an operator error: the documents told them to.

    The folder holds the SUPERSET across views. The approved view is the one
    exception and MANIFEST.txt names it: a front turnaround must not be given
    the approved front to match, because it cannot match itself.

    Not committed — see .gitignore. It is 8.6 MB of duplicated binaries per
    outfit, regenerated on every run, and reproducible from outfits.yaml and the
    images already in the repository. Same reasoning as renders/.
    """
    outdir = repo / "03-characters" / character / "prompts" / "attach" / str(outfit["id"])
    if outdir.is_dir():
        for f in outdir.iterdir():
            f.unlink()
    outdir.mkdir(parents=True, exist_ok=True)

    # The superset: the non-approved views need everything.
    views = [v for v in VIEWS if v != (outfit.get("approved") or {}).get("view", "front")]
    refs = reference_list(character, outfit, views[0] if views else "left")

    lines, missing, n = [], [], 0
    for i, (label, path, _url) in enumerate(refs, 1):
        src = repo / path
        if not src.is_file():
            missing.append(f"{label} -> {path}")
            continue
        dst = outdir / f"{_slug(label, i)}{src.suffix.lower()}"
        dst.write_bytes(src.read_bytes())
        lines.append(f"{dst.name}\n    scope : {label}\n    source: {path}")
        n += 1

    approved_view = (outfit.get("approved") or {}).get("view", "front")
    note = ""
    if any(l.startswith("COSTUME") for l, _, _ in refs):
        note = (f"\nEXCEPTION — turn-{outfit['id']}-{approved_view}: attach everything EXCEPT\n"
                f"file 1. The approved {approved_view} cannot be given to itself as a match\n"
                f"target. Every other view takes all {n}.\n")

    head = (f"ATTACH ALL {n} OF THESE FILES, and nothing else.\n"
            if n else "NOTHING TO ATTACH — this outfit declares no references.\n")
    body = ("\n".join(lines) + "\n") if n else (
        "\nThis character has no approved costume reference, no reference plates\n"
        "and no actor photograph, so every image of them is generated from the\n"
        "written rules alone. That is not a neutral position: words cannot hold a\n"
        "silhouette across five views, and this is the state every character was\n"
        "in before the approved-front method existed.\n"
        "\nAdd references: to outfits.yaml, or approve a front and let the other\n"
        "four match it. See 03-characters/APPROVAL.md.\n")

    (outdir / "MANIFEST.txt").write_text(
        head
        + f"{character} / {outfit['id']} — generated by short.py, do not edit.\n"
        "\nThe prompt lists these same references in this same order. If the two\n"
        "ever disagree, the prompt is right and this folder is stale — rerun\n"
        "./tools/regen.\n"
        + ("\nThe model should confirm it used the ATTACHMENTS rather than the URLs.\n"
           "If it says it fetched URLs, or says nothing, the references did not\n"
           "arrive and the image is not trustworthy.\n" if n else "")
        + f"{note}\n" + body
        + ("\nMISSING — declared in outfits.yaml, not on disk:\n  "
           + "\n  ".join(missing) + "\n" if missing else ""),
        encoding="utf-8")
    return n, missing


def run(repo: Path, character: str, budget: int = None, dry_run: bool = False) -> int:
    cfg_path = repo / "03-characters" / character / "outfits.yaml"
    if not cfg_path.is_file():
        return 0
    cfg = yaml.safe_load(cfg_path.read_text())
    outdir = repo / "03-characters" / character / "prompts" / "turnarounds-short"
    if not dry_run:
        outdir.mkdir(parents=True, exist_ok=True)
    n = 0
    sizes = []
    reported = set()
    for outfit in cfg.get("outfits", []):
        for view in VIEWS:
            text, cap = fit(character, cfg, outfit, view, budget)
            if not dry_run:
                (outdir / f"turn-{outfit['id']}-{view}.txt").write_text(text, encoding="utf-8")
            sizes.append(len(text))
            n += 1

            # Once per outfit, not once per view — the five views trim alike.
            if outfit["id"] in reported:
                continue
            reported.add(outfit["id"])
            lost = losses(outfit, cap)
            if not lost:
                continue
            rules = outfit.get("must_show") or []
            spec = sum(len(r) for r in rules)
            kept = sum(len(trim(r, cap)) for r in rules)
            share = 100 * kept // spec if spec else 100
            mark = "!" if share < 80 else " "
            print(f"  {mark} {character}/{outfit['id']}: rules trimmed at cap {cap} — "
                  f"{share}% of {spec} spec chars reach the generator")
            for i, subject, gone in lost:
                print(f"      rule {i}. {subject}…")
                for kind, sent in gone:
                    print(f"        {kind} {sent[:96]}")

    if not dry_run:
        for outfit in cfg.get("outfits", []):
            k, missing = stage_attachments(repo, character, outfit)
            rel = f"prompts/attach/{outfit['id']}"
            print(f"    {character}/{outfit['id']}: {k} reference images staged -> {rel}/")
            for m in missing:
                print(f"  ! MISSING reference — declared but not on disk: {m}")

    if n:
        print(f"  {character}: {n} short prompts, {min(sizes)}–{max(sizes)} chars "
              f"-> {outdir.relative_to(repo)}")
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("character", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--budget", type=int, default=BUDGET,
                    help=f"total character budget (default {BUDGET}). Raise it to "
                         "test what the generator actually accepts before "
                         "committing to a new ceiling.")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would be trimmed without writing anything")
    a = ap.parse_args()
    repo = find_repo_root(Path.cwd())
    names = ([p.name for p in sorted((repo / "03-characters").iterdir()) if p.is_dir()]
             if a.all else [a.character])
    if a.budget != BUDGET:
        print(f"  budget {a.budget} (default {BUDGET}) — this is a test, not the "
              f"committed setting\n")
    total = sum(run(repo, c, a.budget, a.dry_run) for c in names if c)
    print(f"\n{total} short prompts written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
