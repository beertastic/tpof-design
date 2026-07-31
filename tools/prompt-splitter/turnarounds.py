#!/usr/bin/env python3
"""Generate costume turnaround prompts from a character's outfits.yaml.

Five paste-ready prompts per outfit: front, left, right, back, natural.

  python tools/prompt-splitter/turnarounds.py baylan
  python tools/prompt-splitter/turnarounds.py --all
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from split import find_repo_root, parse_blocks  # noqa: E402

SIDE_WORDS = ("her right", "her left", "his right", "his left",
              "their right", "their left")

# Things that exist on one side of a body and must be told which.
ASYMMETRIC = ("gauntlet", "bracer", "vambrace", "holster", "blaster", "pistol",
              "knife", "sheath", "sword", "bandolier", "bandoleer", "sling",
              "pauldron", "shoulder cap", "shoulder plate", "satchel", "quiver",
              "scabbard", "eyepatch", "prosthetic")


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
        found = [w for w in ASYMMETRIC if w in text]
        if found and not any(sw in text for sw in SIDE_WORDS):
            warnings.append(
                f"{character}/{o['id']}: mentions {', '.join(sorted(set(found))[:4])} "
                "but never says which side. State it from the wearer's own left "
                "and right, e.g. \"her right thigh\".")

        for r in (o.get("references") or []):
            if not (Path("03-characters") / character / r["path"]).is_file():
                warnings.append(
                    f"{character}/{o['id']}: reference plate {r['path']} does "
                    f"not exist, but every prompt tells the operator to attach "
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
    extra = [f"[for the operator, not the model: also attach "
             f"03-characters/{cdir}/{r['path']} — {r['what']}]"
             for r in (outfit.get("references") or [])]
    ref_note = "\n".join(
        ([f"[for the operator, not the model: attach {ref_path}]"] if gate else [])
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
    parts = [
        f"[{character.upper()} — TURNAROUND — {outfit['name'].upper()} — {view_name}]",
        f"Output file: turn-{outfit['id']}-{view_id}.png",
        f"Aspect ratio: {ratio}  (tall, full figure)",
        "",
        "THIS MUST LOOK LIKE A REAL COSTUME REFERENCE PHOTOGRAPH.",
        "A photograph of a real performer wearing a real, physically built costume,",
        "standing in a real studio under real light. Not a render, not an",
        "illustration, not concept art, not AI-looking output.",
        "",
        # The gate protects every view that has something to match against. The
        # first image of a costume has nothing, so demanding a reference there
        # would refuse the one prompt that has to work from text alone.
        "BEFORE YOU GENERATE — CHECK THIS FIRST." if gate else None,
        "" if gate else None,
        "Two reference images must be attached to this conversation:" if gate else None,
        "  1. The APPROVED COSTUME reference for this character." if gate else None,
        "  2. The ACTOR reference." if gate else None,
        "" if gate else None,
        "IF NO IMAGES ARE ATTACHED TO THIS CONVERSATION, STOP." if gate else None,
        "Do not generate anything. Reply with exactly:" if gate else None,
        "  \"No reference images attached. Please attach the approved costume" if gate else None,
        "   reference and the actor reference, then resend this prompt.\"" if gate else None,
        "" if gate else None,
        "Do not proceed from the text alone. The written description is not" if gate else None,
        "sufficient on its own and will produce the wrong costume and the wrong" if gate else None,
        "face." if gate else None,
        "" if gate else None,
        "THE ATTACHED IMAGES OUTRANK THIS TEXT. Where they disagree, the images win." if gate else None,
        "Match the costume, materials, colours, face and build from the attached" if gate else None,
        "reference exactly. Only the setting, pose and lighting change." if gate else None,
        "" if ref_note else None,
        ref_note if ref_note else None,
        "" if ref_note else None,
        # No reference yet: this prompt IS the one that creates it.
        "THIS IS THE FIRST IMAGE OF THIS COSTUME. THERE IS NO REFERENCE YET."
        if not gate else None,
        "" if not gate else None,
        "Build it from the description below, which is the only source. Read the"
        if not gate else None,
        "NON-NEGOTIABLE list as hard requirements, not suggestions — every one of"
        if not gate else None,
        "them must be visible and correct in this image."
        if not gate else None,
        "" if not gate else None,
        "Once approved, THIS IMAGE BECOMES THE REFERENCE that every other view of"
        if not gate else None,
        "this costume is matched against. An error here propagates into all of"
        if not gate else None,
        "them, so it is worth several attempts to get right."
        if not gate else None,
        "" if not gate else None,
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
        ("The attached reference images outrank this text. If nothing was attached, "
         "you should not have generated this." if gate else ""),
        f"Deliver a single image at {ratio}. It must look photographed, not generated.",
    ]
    return "\n".join(p for p in parts if p is not None).strip() + "\n"


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
        "Each file is self-contained — open, select all, paste. Attach actor",
        "reference first.",
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
        "An outfit marked **APPROVED** has a locked reference image. Every other view",
        "of that costume carries a `MATCH THE APPROVED REFERENCE` instruction naming",
        "the file to attach — and states that where the text and the image disagree,",
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
