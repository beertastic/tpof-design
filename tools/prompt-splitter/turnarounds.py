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
     "back. Shoulders level and parallel to the frame. Head level, facing away."),
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
    match_block = ""
    if ref_path and view_id != ref_view:
        match_block = (
            "MATCH THE APPROVED REFERENCE.\n"
            f"Attach this image to the conversation before generating:\n"
            f"    {ref_path}\n"
            f"It is the approved {ref_view.upper()} view of this costume. Match it exactly — "
            "the same\ncostume, the same materials, the same colours, the same scale, the same "
            "figure\nheight in frame. This image is a different view of that same photograph.\n"
            "Where this text and the reference image disagree, THE IMAGE WINS."
        )
    must = outfit.get("must_show") or []
    must_block = ""
    if must:
        must_block = ("NON-NEGOTIABLE — THIS IMAGE IS WRONG WITHOUT ALL OF THESE:\n"
                      + "\n".join(f"  {i}. {m.strip()}" for i, m in enumerate(must, 1)))

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
        match_block,
        "" if match_block else None,
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
    blocks = parse_blocks(pfile.read_text(encoding="utf-8"))
    ratio = str(cfg.get("ratio", "2:3"))
    name = cfg.get("character", character.title())
    outfits = cfg.get("outfits", [])

    outdir = cdir / "prompts" / "turnarounds"
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("*.txt"):
        old.unlink()

    locked = [o for o in outfits if (o.get("approved") or {}).get("date")]
    if locked:
        for o in locked:
            a = o["approved"]
            print(f"  ! {character}/{o['id']} is APPROVED ({a['date']}) — "
                  f"regenerating its prompts. Existing artwork may no longer match.",
                  file=sys.stderr)

    count = 0
    rows = []
    for outfit in outfits:
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
