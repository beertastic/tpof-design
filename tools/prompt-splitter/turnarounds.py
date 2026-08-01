#!/usr/bin/env python3
"""Generate costume turnaround prompts from a character's outfits.yaml.

Five paste-ready prompts per outfit: front, left, right, back, natural.

  python tools/prompt-splitter/turnarounds.py baylan
  python tools/prompt-splitter/turnarounds.py --all
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from split import find_repo_root, parse_blocks, actor_refs, raw_url  # noqa: E402

SIDE_WORDS = ("her right", "her left", "his right", "his left",
              "their right", "their left")

# Things that exist on one side of a body and must be told which.
ASYMMETRIC = ("gauntlet", "bracer", "vambrace", "holster", "blaster", "pistol",
              "knife", "sheath", "sword", "bandolier", "bandoleer", "sling",
              "pauldron", "shoulder cap", "shoulder plate", "satchel", "quiver",
              "scabbard", "eyepatch", "prosthetic")

# An outfit that TAKES an item off does not owe it a side. Baylan's
# shirtsleeves says "no blaster, no holster, no rifle" — the whole point of the
# costume — and was being told to assign them a side it does not have.
NEG_BEFORE = ("no ", "not ", "never ", "nor ", "without ")
NEG_AFTER = re.compile(
    r"[\s,]*(?:(?:is|are|was|were|all|both|now|has|have|been)\s+)*"
    r"(?:removed|gone\b|gone\.|off\b)")


def _unsided(text: str, word: str) -> bool:
    """True if `word` appears at least once as something actually worn.

    Matched on word boundaries, so "swordsman" is not a sword, and negated
    mentions are ignored so a removed item is not reported as unplaced.
    """
    for m in re.finditer(rf"\b{re.escape(word)}\b", text):
        before = text[max(0, m.start() - 12):m.start()]
        if any(before.endswith(n) for n in NEG_BEFORE):
            continue
        if NEG_AFTER.match(text, m.end()):
            continue
        return True
    return False


from consistency import check_outfit


def check_placement(character: str, cfg: dict) -> list[str]:
    """Warn about asymmetric items that have not been assigned a side."""
    warnings: list[str] = []
    hand = str(cfg.get("handedness", "")).strip().lower()
    if hand not in ("left", "right"):
        warnings.append(
            f"{character}: no `handedness:` declared in outfits.yaml. "
            "Set it to left or right — every weapon and armour placement "
            "follows from it. See 09-prompt-library/Handedness-And-Placement.md")

    for o in cfg.get("outfits", []):
        text = " ".join([o.get("description", "")] + list(o.get("must_show") or [])).lower()
        if not (o.get("must_show") or []):
            warnings.append(f"{character}/{o['id']}: no `must_show:` — critical "
                            "features will not be hoisted to the top of prompts.")
        found = [w for w in ASYMMETRIC if _unsided(text, w)]
        if found and not any(sw in text for sw in SIDE_WORDS):
            warnings.append(
                f"{character}/{o['id']}: mentions {', '.join(sorted(set(found))[:4])} "
                "but never says which side. State it from the wearer's own left "
                "and right, e.g. \"her right thigh\".")

        # A space in a filename breaks the raw URL a connected model builds, and
        # it fails as a 000 rather than a 404 — indistinguishable from having no
        # access at all. Cost an afternoon on 2026-08-01.
        actor_dir = Path("03-characters") / character / "reference" / "actor"
        if actor_dir.is_dir():
            for f in actor_dir.iterdir():
                if " " in f.name and f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"):
                    warnings.append(
                        f"{character}: actor reference `{f.name}` has a space in "
                        f"its filename. Rename it — see 03-characters/CAST-REFERENCE.md "
                        f"for the expected names.")

        for r in (o.get("references") or []):
            if not (Path("03-characters") / character / r["path"]).is_file():
                warnings.append(
                    f"{character}/{o['id']}: reference plate {r['path']} does "
                    f"not exist, but every prompt tells the model to fetch "
                    f"it. Create it or remove the entry.")

        # The description is injected into the same prompt as the rules above,
        # and where they disagree the description wins. See consistency.py.
        warnings.extend(check_outfit(character, o))
    return warnings


VIEWS = [
    ("front", "FRONT",
     "The subject faces the camera squarely, straight on. Shoulders level and "
     "parallel to the frame. Head level, looking directly at the lens."),
    ("left", "LEFT SIDE",
     "The subject is rotated exactly ninety degrees to show their LEFT side in "
     "full profile. Head faces the same direction as the body — not turned "
     "toward camera. A clean side-on profile of the whole figure."),
    ("right", "RIGHT SIDE",
     "The subject is rotated exactly ninety degrees the other way to show their "
     "RIGHT side in full profile. Head faces the same direction as the body — "
     "not turned toward camera. A clean side-on profile of the whole figure."),
    ("back", "BACK",
     "The subject faces directly away from the camera, showing the whole of the "
     "back. Shoulders level and parallel to the frame. Head level, facing away.\n"
     "\n"
     "CRITICAL — THIS IS A ROTATION, NOT A MIRROR.\n"
     "The person has turned around. They have NOT been flipped horizontally.\n"
     "Because she has turned, HER RIGHT SIDE IS NOW ON THE VIEWER'S LEFT and her\n"
     "left side is on the viewer's RIGHT — the opposite of the front view.\n"
     "\n"
     "So in THIS image specifically:\n"
     "  - anything worn on HER RIGHT appears on the VIEWER'S LEFT\n"
     "  - anything worn on HER LEFT appears on the VIEWER'S RIGHT\n"
     "\n"
     "If this image looks like a horizontally flipped copy of the front view, it\n"
     "is wrong. Check every asymmetric item — the forearm piece, the shoulder\n"
     "piece, the thigh piece, the holster and the blade — and confirm each one\n"
     "has swapped which side of the FRAME it appears on, compared with the front."),
]

TURN_POSE = """FULL-LENGTH COSTUME REFERENCE PHOTOGRAPH.

Plain, seamless, neutral mid-grey studio background. Even, flat, soft frontal
lighting. No atmosphere, no haze, no mood, no environment, no set.

Pose: arms held clearly away from the body, roughly thirty degrees out, so
nothing overlaps and the full silhouette reads. Legs slightly apart, weight even
on both feet. Standing straight. Neutral expression. This is a costume record,
not a performance — no attitude, no character, no acting.

Framing: the entire figure from the top of the head to below the feet, with a
small even margin above and below. Shot from chest height on a long lens so
there is minimal perspective distortion. Figure centred, filling the frame
vertically.

Every garment, fastening, strap, pocket, seam, buckle and item of equipment must
be clearly visible and readable. Nothing obscured by shadow, by pose, or by
another layer.

Sharp across the entire frame. Deep depth of field. No shallow focus, no bokeh,
no lens flare, no vignetting. This is documentation, not cinematography."""

NATURAL_POSE = """FULL-LENGTH COSTUME REFERENCE PHOTOGRAPH — NATURAL POSE.

Same plain seamless neutral mid-grey studio background, same even soft frontal
lighting, same full-figure framing and same scale as the four turnaround views.

But the subject now stands as this person actually stands. Weight settled on one
leg, shoulders as they naturally sit, hands where this character would rest them,
head at the angle they hold it. A real posture, not a display position.

Expression is the character's default — the face they wear when nobody is asking
anything of them.

Still sharp across the frame, still evenly lit, still no environment. The only
thing that changes from the turnaround views is the human being inside the
clothes: how the costume hangs when it is not being presented, where it creases,
what it does under a real body.

Facing the camera, three-quarters on."""

CONSISTENCY = """CONSISTENCY REQUIREMENT — this is one of five images of the same costume.

All five share the same distance, same lens, same camera height, same lighting
setup, same background, same exposure and the same scale: the figure occupies
exactly the same height in every frame. The costume is identical in all five —
nothing added, removed, opened or adjusted between views.

The only thing that changes between the four turnaround views is the direction
the subject is facing."""


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
    """Insert a short content hash after the header.

    A model can be asked to quote it, which is an exact check that it read THIS
    version of the prompt. Character counts are not — a connected model reported
    28,195 for a file that has never been that size at any commit, because it
    counts its own post-processed text rather than raw bytes.

    Hashed from the body, so it changes only when the prompt actually changes.
    """
    import hashlib
    h = hashlib.sha256(body.encode()).hexdigest()[:8]
    lines = body.split("\n")
    commit = _repo_commit()
    stamp = f"Prompt version: {h} \u00b7 repo commit {commit}"
    echo = ECHO_TEMPLATE.format(commit=commit.split()[0], h=h)
    return "\n".join(lines[:3] + [stamp, "", echo] + lines[3:])


def build(character: str, outfit: dict, view_id: str, view_name: str,
          view_desc: str, blocks: dict, ratio: str) -> str:
    natural = view_id == "natural"

    approved = outfit.get("approved") or {}
    ref_path = approved.get("reference")
    ref_view = approved.get("view", "front")
    gate = bool(ref_path) and view_id != ref_view
    # Approved material and prop plates attach to EVERY view, including the one
    # that creates the costume reference — the material is already locked even
    # when the costume is not.
    cdir = outfit.get("_dir", character)
    extra = [f"USE THE ATTACHED PHOTOGRAPH — {r['what']}. If not attached, fetch:\n    "
             f"{raw_url(f'03-characters/{cdir}/{r[chr(39)+chr(39)] if False else r["path"]}')}"
             for r in (outfit.get("references") or [])]

    # The actor reference is named if one exists, and its absence is stated
    # explicitly rather than left silent — a model given no instruction about
    # the face invents a striking one, and a striking face is the wrong answer
    # for every character in this film.
    actors = actor_refs(cdir)
    if actors:
        for _n, _name, _url, _what in actors:
            _label = f" — {_what}" if _what else ""
            extra.append(f"LIKENESS ({_n} of {len(actors)}){_label} — attached to "
                         f"this message.\n    If it is NOT attached, fetch: {_url}")
        _many = (f"THERE ARE {len(actors)} ACTOR REFERENCES, numbered 1 to "
                 f"{len(actors)}. They are all the SAME PERSON seen from"
                 f" different\nangles. Use every one of them.\n\n"
                 if len(actors) > 1 else "")
        actor_line = (_many +
            "USE THE ATTACHED ACTOR PHOTOGRAPH — TAKE THE FACE AND THE BUILD\n"
            "FROM IT. It is normally attached to this message. If nothing is\n"
            "attached, fetch the URL above instead — it is a public raw file and it\n"
            "opens. Say which of the two you used.\n"
            "\n"
            "If neither works, say so and stop. Never invent a face.\n"
            "\n"
            "Bone structure, features, proportions, skin, the shape of the head. The\n"
            "person in your image must be recognisably the SAME HUMAN BEING as the\n"
            "person in the photograph.\n"
            "\n"
            "DO NOT TAKE THE HAIR OR THE BEARD FROM THE PHOTOGRAPH, and do not take\n"
            "the age or the condition. Where the written description below differs\n"
            "from the reference — colour, length, grooming, weight, wear, years —\n"
            "THE DESCRIPTION WINS EVERY TIME.\n"
            "\n"
            "The actor is being aged, greyed, roughened or otherwise made up to play\n"
            "this part. That is normal and it is the whole job. The photograph is a\n"
            "LIKENESS reference, not a grooming reference and not a costume one.\n"
            "\n"
            "If you find yourself unable to satisfy both, keep the FACE and follow the\n"
            "description for everything else. Do not resolve it by inventing a new\n"
            "person who fits the description — that is the failure this note exists to\n"
            "prevent.\n"
            "\n"
            "THE ACTOR PHOTOGRAPH IS NOT THE BASE IMAGE. DO NOT EDIT IT.\n"
            "Do not retouch it, extend it, outpaint it, crop it or produce a variation\n"
            "of it. You are making a COMPLETELY NEW PHOTOGRAPH of the same person.\n"
            "\n"
            "Take NOTHING from it except the face and the build. In particular do not\n"
            "copy its FRAMING, its CROP, its POSE, its LIGHTING, its BACKGROUND or the\n"
            "CLOTHES the person is wearing in it. The reference is almost certainly a\n"
            "head-and-shoulders portrait on a dark background; what you are making is a\n"
            "full-length figure on plain seamless grey under flat even light. If your\n"
            "output resembles that photograph in anything but the face, you\n"
            "have edited it instead of using it.")
    else:
        actor_line = ("NO ACTOR HAS BEEN CAST. There is no actor reference for this "
                      "character,\nso cast the face yourself — build it from the written "
                      "description and\nnothing else. An ordinary, unremarkable, "
                      "believable face. DO NOT reach for\na handsome or striking one, and "
                      "do not drift toward any actor you have seen\nplay a similar part.")
    ref_note = "\n".join(
        ([f"FETCH AND MATCH — the approved costume reference:\n    "
           f"{raw_url(ref_path)}"] if gate else [])
        + extra)
    must = outfit.get("must_show") or []
    must_block = ""
    if must:
        must_block = ("NON-NEGOTIABLE — THIS IMAGE IS WRONG WITHOUT ALL OF THESE:\n"
                      + "\n".join(f"  {i}. {m.strip()}" for i, m in enumerate(must, 1)))

    hand = outfit.get("_handedness")
    hand_line = (f"This character is {hand.upper()}-HANDED. All positions below are "
                 f"given from\nTHEIR OWN left and right, never the viewer's."
                 if hand else "")

    # Scale is the single thing image generators get wrong most often, and a lone
    # figure on a seamless backdrop offers nothing to measure against.
    # Some characters in this film share a name with a well-known one. The name
    # alone retrieves that depiction, and the model then draws it confidently and
    # in detail. Lesson learned on the mercenary pack in July; it applies harder
    # here, because these names ARE the famous ones.
    retrieve = outfit.get("_do_not_retrieve")
    retrieve_block = ("=" * 68 + "\n"
                      "THE NAME ON THIS PROMPT BELONGS TO A CHARACTER YOU ALREADY KNOW.\n"
                      "DO NOT DRAW THAT CHARACTER.\n"
                      + "=" * 68 + "\n\n" + retrieve.strip() + "\n\n"
                      "Everything you already believe about this name is from a different\n"
                      "production. Discard it. The description below is the only source, and\n"
                      "where your memory and this document disagree, THIS DOCUMENT IS RIGHT.\n"
                      "\n"
                      "If you find yourself adding something because it feels correct for the\n"
                      "name rather than because it is written below, that is the retrieval and\n"
                      "it is exactly what has to be resisted."
                      if retrieve else "")

    height = outfit.get("_height")
    height_line = (f"HEIGHT: {height}. Build the proportions to it — head size against "
                   f"body\nlength, limb length, how heavily the figure stands. A figure "
                   f"alone on a plain\nbackdrop gives the eye nothing to measure "
                   f"against, so it has to be in the body."
                   if height else "")
    scale_block = "\n\n".join(x for x in (hand_line, height_line) if x)
    parts = [
        f"[{character.upper()} — TURNAROUND — {outfit['name'].upper()} — {view_name}]",
        f"Output file: turn-{outfit['id']}-{view_id}.png",
        f"Aspect ratio: {ratio}  (tall, full figure)",
        "",
        f"ASPECT RATIO IS {ratio} — A TALL PORTRAIT. Generate at 1024 x 1536 pixels, or",
        "the nearest TALL size your tool offers. DO NOT DELIVER A SQUARE IMAGE.",
        "A square frame cannot hold a standing figure with headroom and floor, and the",
        "board generator fits plates without cropping — a square one letterboxes on the",
        "sheet and wastes half the panel.",
        "",
        "THIS MUST LOOK LIKE A REAL COSTUME REFERENCE PHOTOGRAPH.",
        "A photograph of a real performer wearing a real, physically built costume,",
        "standing in a real studio under real light. Not a render, not an",
        "illustration, not concept art, not AI-looking output.",
        "",
        "=" * 68,
        "THIS IS A PLATE, NOT A BOARD. ONE PHOTOGRAPH, ONE FIGURE, NOTHING ELSE.",
        "FULL LENGTH — THE WHOLE BODY, HEAD TO BELOW THE FEET.",
        "=" * 68,
        "",
        "NOT a portrait. NOT head-and-shoulders. NOT a bust, a half-length or a",
        "waist-up. If the feet are not in the frame, the image is unusable — this is",
        "a COSTUME record and the boots, the hem and the whole silhouette are the",
        "point. The head should occupy a small part of the frame.",
        "",
        "Deliver a single, plain, full-figure photograph on a seamless studio",
        "backdrop. It is raw material. The production boards are assembled from",
        "plates like this one by a separate tool, and anything you add here has",
        "to be removed before it can be used.",
        "",
        "ABSOLUTELY NOT, IN ANY FORM:",
        "  - NO text of any kind. No name, no title, no caption, no labels, no",
        "    headings, no annotation, no measurements, no height marks.",
        "  - NO logo, no watermark, no signature, no production branding.",
        "  - NO layout, no frame, no border, no vignette panel, no title bar.",
        "  - NO second view. One figure, one angle. No front-and-back pair, no",
        "    multi-view sheet, no turnaround strip, no contact sheet, no montage.",
        "  - NO inset head shots, no profile studies, no detail crops.",
        "  - NO material swatches, NO colour palette chips, NO prop call-outs.",
        "  - NO scale silhouette, no ruler, no grid.",
        "",
        "If the result looks like a designed page rather than a photograph taken",
        "in a costume fitting, it is wrong and cannot be used.",
        "",
        actor_line,
        "",
        # The gate protects every view that has something to match against. The
        # first image of a costume has nothing, so demanding a reference there
        # would refuse the one prompt that has to work from text alone.
        "BEFORE YOU GENERATE — GET THE REFERENCES." if gate else None,
        "" if gate else None,
        "Every reference this image must match is listed above as a public URL." if gate else None,
        "For each one: DOWNLOAD it, DECODE it, LOOK at it to confirm it opened, and" if gate else None,
        "MAKE IT AVAILABLE AS AN IMAGE INPUT to the generator. A URL that has been" if gate else None,
        "fetched but never handed to the generator is not a reference, and that gap" if gate else None,
        "is exactly what produced a run of wrong faces on 2026-08-01." if gate else None,
        "" if gate else None,
        "Do NOT ask for a manual attachment when the download and the handoff both" if gate else None,
        "succeed. Ask only if a URL will not download, a file will not decode, or the" if gate else None,
        "generator cannot receive it — and then name the one that failed." if gate else None,
        "" if gate else None,
        "Do not proceed from the text alone. The written description is not sufficient" if gate else None,
        "on its own and will produce the wrong costume and the wrong face." if gate else None,
        "" if gate else None,
        "THE ATTACHED PHOTOGRAPHS OUTRANK THIS TEXT. Where they disagree, the photographs win." if gate else None,
        "Match the costume, materials, colours, face and build from them exactly." if gate else None,
        "Only the setting, pose and lighting change." if gate else None,
        "" if ref_note else None,
        ref_note if ref_note else None,
        "" if ref_note else None,
        # No reference yet: this prompt IS the one that creates it.
        "THIS IS THE FIRST PHOTOGRAPH OF THIS COSTUME. THERE IS NOTHING TO MATCH YET."
        if not gate else None,
        "" if not gate else None,
        "Build it from the description below, which is the only source. Read the"
        if not gate else None,
        "NON-NEGOTIABLE list as hard requirements, not suggestions — every one of"
        if not gate else None,
        "them must be visible and correct in this image."
        if not gate else None,
        "" if not gate else None,
        "Once approved, every other view of this costume is matched against THIS"
        if not gate else None,
        "PHOTOGRAPH. An error here propagates into all of"
        if not gate else None,
        "them, so it is worth several attempts to get right."
        if not gate else None,
        "" if not gate else None,
        retrieve_block if retrieve_block else None,
        "" if retrieve_block else None,
        scale_block if scale_block else None,
        "" if scale_block else None,
        must_block,
        "" if must_block else None,
        "=== SHOT ===",
        NATURAL_POSE if natural else TURN_POSE,
        "",
        "=== VIEW ===",
        ("The subject stands naturally, facing the camera three-quarters on."
         if natural else view_desc),
        "",
        "=== CONSISTENCY ===", CONSISTENCY, "",
        "=== STYLE ===", blocks.get("Style", ""), "",
        "=== DO NOT ===", blocks.get("Do Not", ""), "",
        "Additionally, for this image only: ignore any instruction about imperfect,",
        "off-centre or loose framing. A turnaround is deliberately centred and",
        "square-on. Keep every rule about real skin and real materials.",
        "",
        "=== PHOTOGRAPHIC REALISM ===", blocks.get("Realism", ""), "",
        "=== SKIN AND REALISM ===", blocks.get("Anti-synthetic", ""), "",
        "=== CHARACTER ===", blocks.get("Character Constants", ""), "",
        "=== THIS COSTUME ===",
        f"{outfit['name']} — {outfit.get('scenes', '')}".strip(" —"),
        "",
        outfit["description"].strip(),
        "",
        (("=== CHECK BEFORE YOU FINISH ===\n" + must_block + "\n")
         if must_block else ""),
        ("The fetched photographs outrank this text. If none were fetched, "
         "you should not have generated this." if gate else ""),
        f"Deliver a single image at {ratio}. It must look photographed, not generated.",
    ]
    return _stamp_version("\n".join(p for p in parts if p is not None).strip() + "\n")


def run(repo: Path, character: str) -> int:
    cdir = repo / "03-characters" / character
    ofile = cdir / "outfits.yaml"
    pfile = cdir / "Prompts.md"
    if not ofile.is_file():
        print(f"  skip {character}: no outfits.yaml", file=sys.stderr)
        return 0
    if not pfile.is_file():
        print(f"  skip {character}: no Prompts.md", file=sys.stderr)
        return 0

    cfg = yaml.safe_load(ofile.read_text(encoding="utf-8")) or {}
    for w in check_placement(character, cfg):
        print(f"  ! {w}", file=sys.stderr)
    blocks = parse_blocks(pfile.read_text(encoding="utf-8"))
    ratio = str(cfg.get("ratio", "2:3"))
    name = cfg.get("character", character.title())
    outfits = cfg.get("outfits", [])

    outdir = cdir / "prompts" / "turnarounds"
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("*.txt"):
        old.unlink()

    locked = [o for o in outfits if (o.get("approved") or {}).get("date")]
    for o in locked:
        a = o["approved"]
        print(f"  ! {character}/{o['id']} is APPROVED ({a['date']}) — regenerating "
              f"its prompts. Existing artwork may no longer match.", file=sys.stderr)
        ref = a.get("reference")
        if ref and not (repo / ref).is_file():
            print(f"  ! MISSING approved reference: {ref}\n"
                  f"    The other views name this file but it does not exist. Save the "
                  f"approved image there.", file=sys.stderr)

    count = 0
    rows = []
    for outfit in outfits:
        outfit["_handedness"] = cfg.get("handedness")
        # A per-outfit height wins, because mercenary-kit is four different
        # people in one file and Merc 1 is a Wookiee.
        outfit["_height"] = outfit.get("height") or cfg.get("height")
        # An outfit may override the file-level block — see short.py.
        outfit["_do_not_retrieve"] = (outfit.get("do_not_retrieve")
                                      or cfg.get("do_not_retrieve"))
        outfit["_dir"] = character
        views = VIEWS + [("natural", "NATURAL POSE", "")]
        for view_id, view_name, view_desc in views:
            path = outdir / f"turn-{outfit['id']}-{view_id}.txt"
            path.write_text(
                build(name, outfit, view_id, view_name, view_desc, blocks, ratio),
                encoding="utf-8")
            rows.append((outfit["name"], view_name,
                         f"turn-{outfit['id']}-{view_id}"))
            count += 1

    idx = [
        f"# {name} — costume turnarounds",
        "",
        "**The primary deliverable.** Five images per outfit: four technical views",
        "and one natural pose. Generate these in full before any mood image.",
        "",
        "Each file is self-contained — open, select all, paste. Every reference it",
        "needs is listed inside it as a public URL, to be fetched not attached.",
        "",
        f"All at **{ratio}**, tall, full figure.",
        "",
        "| Outfit | Status | View | Prompt | Output |",
        "|---|---|---|---|---|",
    ]
    status = {}
    for o in outfits:
        a = o.get("approved") or {}
        status[o["name"]] = f"**APPROVED** {a['date']}" if a.get("date") else "in progress"
    for oname, vname, stem in rows:
        idx.append(f"| {oname} | {status.get(oname,'')} | {vname} | "
                   f"`{stem}.txt` | `{stem}.png` |")
    idx += [
        "",
        "## Approved outfits",
        "",
        "An outfit marked **APPROVED** has a locked front turnaround. Every other view",
        "of that costume carries a `MATCH THE APPROVED REFERENCE` instruction naming",
        "the URL to fetch — and states that where the text and the image disagree,",
        "**the image wins**.",
        "",
        "**Editing an approved outfit invalidates artwork already made from it.** The",
        "generator prints a warning when you do. If a change is genuinely needed,",
        "clear the `approved` block, regenerate, and re-approve from a new reference.",
        "",
        "## The consistency rule",
        "",
        "The four turnaround views are **the same photograph with the subject",
        "rotated.** Same distance, lens, height, light, background and scale. If the",
        "figure changes size or the light shifts between images, the set is useless.",
        "",
        "Generate all five of an outfit in one sitting, in one conversation, before",
        "moving to the next outfit.",
        "",
        "Generated from `outfits.yaml` by `tools/prompt-splitter/turnarounds.py`.",
        "**Do not edit these files** — edit `outfits.yaml` and regenerate.",
        "",
    ]
    (outdir / "README.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"  {character}: {len(outfits)} outfits, {count} prompts "
          f"-> {outdir.relative_to(repo)}")
    return count


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate costume turnaround prompts.")
    ap.add_argument("character", nargs="?")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    if args.all == bool(args.character):
        ap.error("Give one character name or use --all.")

    repo = find_repo_root(Path(__file__).parent)
    names = (sorted(p.name for p in (repo / "03-characters").iterdir() if p.is_dir())
             if args.all else [args.character])
    total = sum(run(repo, n) for n in names)
    print(f"\n{total} turnaround prompts written.")


if __name__ == "__main__":
    main()
