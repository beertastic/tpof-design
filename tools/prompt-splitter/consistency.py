"""Catch prose that contradicts a `must_show` rule.

The failure this exists to prevent has now caused three real defects:

  1. Shada's `maintenance` slot asked for "a dim salvaged interior" while her
     rules said EXTERIOR ONLY, in capitals, twice. It returned an interior every
     time and the rule looked broken when it was being overruled.
  2. Her outfit description said the scale covers "caps over both shoulders, and
     the outer forearms" against a rule specifying one cap and one gauntlet on
     opposite sides. Generated images kept coming back symmetrical.
  3. The same description ended "A compact blaster at the hip" after the model
     was changed to a WESTAR-35 on her right thigh.

All three share a shape: `must_show` establishes authority over something, and
prose elsewhere in the same prompt describes it differently. The generator
follows the prose, because it is the specific instruction and the rule is the
general one.

This is a LINT, not a prover. It reports prose worth looking at rather than
proving a contradiction, and it is tuned to stay quiet — a checker nobody reads
is worse than no checker.
"""
from __future__ import annotations

import re

# Things that sit somewhere on a body and can therefore sit in the wrong place.
ITEMS = [
    "blaster", "pistol", "rifle", "carbine", "bowcaster", "knife", "blade",
    "sword", "holster", "sheath", "gauntlet", "bracer", "vambrace", "cap",
    "pauldron", "patch", "plate", "helmet", "coat", "cape", "cloak", "robe",
    "bandolier", "harness", "rig", "sling", "goggles", "pouch", "grenade",
]

# Different words for the same object, so "blaster pistol" is not read as two
# items and "the blaster" in prose is compared against "the pistol" in a rule.
SYNONYMS = {
    "pistol": "blaster", "carbine": "blaster", "sidearm": "blaster",
    "blade": "knife", "sword": "knife",
    "bracer": "gauntlet", "vambrace": "gauntlet",
    "pauldron": "cap",
    "cloak": "coat", "cape": "coat", "robe": "coat",
    "sheath": "holster",
}

# Where those things sit.
PLACES = [
    "hip", "thigh", "shoulder", "forearm", "arm", "wrist", "chest", "sternum",
    "back", "waist", "belt", "head", "leg", "knee", "ankle", "boot", "collar",
]

# Body parts that come in pairs, so "both X" is a meaningful claim about them.
PAIRED = ["shoulder", "forearm", "arm", "wrist", "hand", "thigh", "leg",
          "knee", "hip", "boot", "eye", "ear"]

# Phrases asserting there is only one of something.
SINGULAR = ["only", "exactly one", "not a pair", "no matching pair", "single",
            "is bare", "completely bare", "no metal", "never a pair"]

# Words that negate a mention, so prose saying "no interior" is not a conflict.
NEGATORS = ["no ", "not ", "never ", "without ", "avoid ", "nothing "]

STOP = {"the", "a", "an", "of", "any", "kind", "all", "and", "or", "in", "on",
        "at", "it", "is", "are", "that", "this", "with", "for", "to", "her",
        "his", "their", "its", "them", "he", "she", "they", "other", "same"}


def _stem(word: str) -> str:
    return word[:-1] if len(word) > 3 and word.endswith("s") else word


def _norm(phrase: str) -> str:
    """Reduce a captured phrase to its first meaningful word or two."""
    words = [w for w in re.findall(r"[a-z\-]+", phrase.lower()) if w not in STOP]
    return " ".join(_stem(w) for w in words[:2])


def _prohibitions(rules: str) -> set[str]:
    """Phrases the rules explicitly forbid."""
    out: set[str] = set()
    # Captures stop at punctuation. Running past a comma swallows the next
    # clause — "no wrap, no metal of any kind" would otherwise ban "wrap no".
    patterns = [
        r"\bno ([a-z][a-z\- ]{2,28}?)(?=[,.;:]|$)",
        r"\bnever ([a-z][a-z\- ]{2,28}?)(?=[,.;:]|$)",
        r"\bdo not make (?:this|it) ([a-z][a-z\- ]{2,28}?)(?=[,.;:]|$)",
        r"\bif (?:there is |there are )?(?:a |an )?([a-z][a-z\- ]{2,28}?) "
        r"(?:in the image[, ]*)?(?:it |the image )?is wrong",
    ]
    for pattern in patterns:
        for match in re.findall(pattern, rules, flags=re.M):
            phrase = _norm(match)
            # Keep the whole phrase. "no high collar" bans a high collar, not
            # everything high — matching on the head word alone flags boots.
            if len(phrase.replace(" ", "")) >= 4:
                out.add(phrase)

    # A word the rules also use affirmatively is not banned outright — it was
    # banned in one place. "no metal of any kind" applies to her left forearm;
    # the rest of the rules are about metal. Scoped bans are the caller's job to
    # read, and flagging them buries the real conflicts.
    return {b for b in out if not _used_affirmatively(rules, b)}


def _used_affirmatively(rules: str, term: str) -> bool:
    pattern = r"\b" + r"\s+".join(
        re.escape(w) + r"s?" for w in term.split()) + r"\b"
    hits = list(re.finditer(pattern, rules))
    return any(not _is_negated(rules, m.start()) for m in hits)


def _is_negated(text: str, at: int) -> bool:
    """Is the mention at `at` inside a negative clause?

    The window stops at the nearest sentence break, which is what actually
    bounds it — an earlier version split on commas too and read "nothing
    polished, ornamental or factory fresh" as negating only the first item.
    """
    # Sentence enders only, not commas: "nothing polished, ornamental or
    # factory fresh" negates the whole list, not just its first item.
    window = re.split(r"[.;:—]", text[max(0, at - 60):at])[-1]
    return any(n in window for n in NEGATORS)


def _placements(text: str) -> dict[str, set[str]]:
    """item -> the places the text puts it.

    The window stops at the next item, or a listing comma, so that "a blaster on
    her right thigh, and a knife on her left hip" does not read as putting the
    blaster on the hip as well.
    """
    item_re = re.compile(rf"\b({'|'.join(ITEMS)})s?\b")
    found: dict[str, set[str]] = {}
    for m in item_re.finditer(text):
        item = SYNONYMS.get(m.group(1), m.group(1))
        # A placement claim does not survive a full stop — nor a listing comma.
        # "hides the harness, the belt and the holster" is three items in a row,
        # not a harness worn at the belt. `belt` is both an item and a place,
        # which is what made that read the wrong way.
        rest = re.split(r"\.|;|,\s+(?:the|and|a|an)\b",
                        text[m.end():m.end() + 90])[0]
        # Stop at the next *different* item — "blaster pistol" is one thing,
        # but "blaster ... and a knife" is two.
        for nxt in item_re.finditer(rest):
            if SYNONYMS.get(nxt.group(1), nxt.group(1)) != item:
                rest = rest[:nxt.start()]
                break
        for place in PLACES:
            if re.search(rf"\b{place}s?\b", rest):
                found.setdefault(item, set()).add(place)
                break
    return found


def check_prose(label: str, rules: list[str], prose: str) -> list[str]:
    """Compare a block of prose against the must_show rules governing it."""
    if not rules or not prose:
        return []
    rule_text = " ".join(rules).lower()
    text = prose.lower()
    warnings: list[str] = []

    # 1. Prose asserts something the rules forbid.
    for banned in sorted(_prohibitions(rule_text)):
        pattern = r"\b" + r"\s+".join(
            re.escape(w) + r"s?" for w in banned.split()) + r"\b"
        for m in re.finditer(pattern, text):
            if _is_negated(text, m.start()):
                continue
            warnings.append(
                f"{label}: says \"{_excerpt(prose, m.start())}\" but a must_show "
                f"rule forbids \"{banned}\". The prose wins in the prompt — "
                f"remove it or restate it to agree.")
            break

    # 2. Prose says "both X" where the rules say there is only one.
    for m in re.finditer(r"\bboth ([a-z]+)\b", text):
        part = _stem(m.group(1))
        if part not in PAIRED:
            continue
        near = [r for r in rule_text.split(".") if part in r]
        if any(s in seg for seg in near for s in SINGULAR):
            warnings.append(
                f"{label}: says \"both {m.group(1)}\" but a must_show rule makes "
                f"the {part} asymmetric — one side only. This is the error that "
                f"keeps producing matched pairs.")

    # 3. Prose puts an item somewhere the rules do not.
    ruled, written = _placements(rule_text), _placements(text)
    for item, places in written.items():
        expected = ruled.get(item)
        if expected and not (places & expected):
            warnings.append(
                f"{label}: puts the {item} at the "
                f"{'/'.join(sorted(places))} but must_show says the "
                f"{'/'.join(sorted(expected))}.")

    # 4. Rules name a specific model; prose describes the same item generically.
    for model in set(re.findall(r"\b[a-z]{3,}-\d+\b", rule_text)):
        if model in text:
            continue
        idx = rule_text.find(model)
        # Only the item named beside the model — not every item in every rule.
        window = rule_text[max(0, idx - 60):idx + 60]
        for item in ITEMS:
            if re.search(rf"\b{item}s?\b", window) and re.search(rf"\b{item}s?\b", text):
                warnings.append(
                    f"{label}: describes the {item} generically, but must_show "
                    f"names a specific model ({model.upper()}). Say the model "
                    f"here too, or drop the mention.")
                break
    return warnings


def _excerpt(prose: str, at: int, width: int = 38) -> str:
    start = max(0, at - width // 3)
    text = " ".join(prose[start:start + width].split())
    return ("…" if start else "") + text + "…"


def check_outfit(character: str, outfit: dict) -> list[str]:
    """An outfit's own description against its must_show rules."""
    return check_prose(f"{character}/{outfit['id']} description",
                       outfit.get("must_show") or [],
                       outfit.get("description") or "")


def check_slot(character: str, slot: dict, must: list[str]) -> list[str]:
    """A Prompts.md slot body against the rules injected into the same prompt."""
    return check_prose(f"{character} slot {slot['n']:02d} ({slot['file']})",
                       must, slot.get("body") or "")


# --- Regression cases ------------------------------------------------------
# Each is a defect that reached generated prompts and cost images. If a change
# to this module stops catching one of them, the change is wrong.
#
#   python tools/prompt-splitter/consistency.py --selftest

KNOWN_DEFECTS = [
    ("interior vs EXTERIOR ONLY",
     ["EXTERIOR ONLY. She is never indoors. NO buildings, NO interiors of any "
      "kind. If there is a wall or a ceiling in the image, it is wrong."],
     "Warm practical lamp light against a dim salvaged interior."),
    ("both shoulders vs one cap",
     ["A CAP OVER HER LEFT SHOULDER ONLY, the OPPOSITE side to the gauntlet. "
      "Her right shoulder is bare."],
     "It covers a panel across the torso, caps over both shoulders."),
    ("blaster at the hip vs right thigh",
     ["BLASTER: a WESTAR-35 blaster pistol on HER RIGHT THIGH, in a worn "
      "drop-leg holster. KNIFE: a combat knife on HER LEFT HIP."],
     "A compact blaster at the hip and a well-used combat knife."),
    ("wraps at the forearms vs left forearm bare",
     ["HER LEFT FOREARM IS COMPLETELY BARE — no gauntlet, no bracer, no wrap, "
      "no metal of any kind."],
     "Quiet wraps at the forearms and lightweight boots."),
]

# Prose that must NOT warn. These are phrasings that tripped earlier versions.
MUST_STAY_QUIET = [
    ("scoped ban is not a global ban",
     ["HER LEFT FOREARM IS COMPLETELY BARE — no metal of any kind. The four "
      "patches are metal scales."],
     "She wears individual six-sided metal plates laced onto a backing."),
    ("banned phrase, not the banned word",
     ["Nothing on the chest that would foul a rifle stock — no high collar."],
     "Best boots in the crew, high and properly laced."),
    ("prose repeats the ban rather than breaking it",
     ["NO interiors of any kind."],
     "Never an interior; forest and clearing only."),
]


def _selftest() -> int:
    failures = 0
    for name, rules, prose in KNOWN_DEFECTS:
        hits = check_prose("t", rules, prose)
        print(f"  {'ok  ' if hits else 'FAIL'}  catches: {name}")
        failures += not hits
    for name, rules, prose in MUST_STAY_QUIET:
        hits = check_prose("t", rules, prose)
        print(f"  {'ok  ' if not hits else 'FAIL'}  quiet on: {name}")
        if hits:
            failures += 1
            for h in hits:
                print(f"          unexpected: {h}")
    print("\nall passed" if not failures else f"\n{failures} FAILED")
    return 1 if failures else 0


if __name__ == "__main__":
    import sys
    raise SystemExit(_selftest() if "--selftest" in sys.argv else
                     print(__doc__) or 0)
