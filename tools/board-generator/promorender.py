"""A4 character promo sheet — the outward-facing counterpart to the boards.

A board documents: flat light, every fitting legible, nothing concealed. This
does the opposite job. One hero image carries the page and the copy is a teaser
rather than a spec — but it is laid out as a dossier, not a poster, so there is
room for real information about the character and what she carries.

Driven by `promo-data.yaml` in the character folder. Geometry is in inches from
the top-left, matching pdfrender.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from pdfrender import Board

A4_WIDTH_IN = 8.268
A4_HEIGHT_IN = 11.693

MARGIN = 0.50
FOOT_Y = A4_HEIGHT_IN - 0.86


def _letterspace(s: str) -> str:
    return " ".join(s.upper())


class Promo:
    """Layout helpers shared by every block on the page."""

    def __init__(self, b: Board, style: dict[str, str]):
        self.b, self.s = b, style
        self.warnings: list[str] = []

    def heading(self, text: str, x: float, y: float, w: float) -> float:
        """Accent rule, then a letterspaced label. Returns the y below it."""
        self.b.rect(x, y, 0.34, 0.018, self.s["accent"], self.s["accent"], 0.2)
        self.b.text(_letterspace(text), x, y + 0.20, 7.2, self.s["accent"], bold=True)
        return y + 0.40

    def body(self, text: str, x: float, y: float, w: float, size=7.4) -> float:
        return self.b.wrapped(text.strip(), x, y, w, size, self.s["muted"],
                              leading_mult=1.42)

    def bullets(self, items: list[str], x: float, y: float, w: float,
                size=7.4) -> float:
        for item in items:
            y = self.b.wrapped(f"—  {item.strip()}", x, y, w, size, self.s["muted"],
                               leading_mult=1.42)
            y += 0.045
        return y

    def columns(self, items: list[str], x: float, y: float, w: float,
                cols: int = 2, gap: float = 0.24, size=7.4) -> float:
        """Bullets laid side by side — cheaper vertically than one long list."""
        cw = (w - gap * (cols - 1)) / cols
        bottom = y
        for i, item in enumerate(items):
            cy = self.bullets([item], x + (i % cols) * (cw + gap),
                              y + (i // cols) * 0.0, cw, size)
            bottom = max(bottom, cy)
        return bottom

    def caption(self, text: str, x: float, y: float, w: float) -> float:
        return self.b.wrapped(text, x, y, w, 6.3, self.s["faint"], leading_mult=1.35)


def render_promo(out_pdf: Path, character_dir: Path, promo: dict[str, Any],
                 style: dict[str, str]) -> list[str]:
    b = Board(out_pdf, A4_WIDTH_IN, A4_HEIGHT_IN)
    p = Promo(b, style)
    col_w = A4_WIDTH_IN - MARGIN * 2

    b.background(style["background"])

    # --- Header --------------------------------------------------------------
    b.text(str(promo["character"]).upper(), MARGIN, MARGIN, 38, style["ink"], bold=True)
    b.text(_letterspace(promo.get("role", "")), MARGIN, MARGIN + 0.58, 8,
           style["accent"], bold=True)
    b.text(promo.get("project", ""), MARGIN, MARGIN + 0.06, 7.4, style["muted"],
           align="right", width=col_w)
    b.text(_letterspace(promo.get("kicker", "")), MARGIN, MARGIN + 0.25, 6.6,
           style["faint"], align="right", width=col_w)
    rule_y = MARGIN + 0.84
    b.rect(MARGIN, rule_y, col_w, 0.012, style["rule"], style["rule"], 0.2)

    # --- Hero row: text column left, image right -----------------------------
    top = rule_y + 0.22
    text_w = float(promo.get("text_column", 2.42))
    gutter = 0.18
    hero_x = MARGIN + text_w + gutter
    hero_w = A4_WIDTH_IN - MARGIN - hero_x
    hero_h = float(promo.get("hero_height", 4.35))

    b.image_cover(character_dir / promo["hero_image"], hero_x, top, hero_w, hero_h,
                  anchor=float(promo.get("hero_anchor", 0.16)))

    y = top
    for i, panel in enumerate(promo.get("panels", [])):
        if i:
            y += 0.26  # gap between panels, never after the last one
        y = p.heading(panel["heading"], MARGIN, y, text_w)
        if panel.get("text"):
            y = p.body(panel["text"], MARGIN, y, text_w)
        if panel.get("items"):
            y = p.bullets(panel["items"], MARGIN, y, text_w)
    if y > top + hero_h + 0.05:
        p.warnings.append(
            f"left column runs {y - top:.2f}in against a {hero_h:.2f}in hero — "
            f"trim a panel, or set `hero_height: {y - top:.2f}`")

    # Flow from whichever side is deeper, so an overlong column pushes the page
    # down rather than printing on top of the next block.
    y = max(y, top + hero_h) + 0.30

    # --- Pull quote ----------------------------------------------------------
    if promo.get("logline"):
        y = b.wrapped(promo["logline"], MARGIN, y, col_w, 17, style["ink"],
                      font="Helvetica-BoldOblique", leading_mult=1.26)
        y += 0.18
    if promo.get("pull"):
        y = b.wrapped(promo["pull"], MARGIN, y, col_w, 8.4, style["muted"],
                      font="Helvetica-Oblique", leading_mult=1.45)
        y += 0.24

    b.rect(MARGIN, y, col_w, 0.012, style["rule"], style["rule"], 0.2)
    y += 0.24

    # --- Weapons and equipment ----------------------------------------------
    weapons = promo.get("weapons") or {}
    if weapons.get("plates"):
        y = p.heading(weapons.get("heading", "Weapons & Equipment"), MARGIN, y, col_w)
        plates = weapons["plates"]
        gap = 0.14
        cell_w = (col_w - gap * (len(plates) - 1)) / len(plates)
        cell_h = float(weapons.get("plate_height", 1.32))
        cap_y = y + cell_h + 0.10
        for i, plate in enumerate(plates):
            px = MARGIN + i * (cell_w + gap)
            # Prop plates are shot flat on plain ground: contain, never crop.
            b.image_contain(character_dir / plate["path"], px, y, cell_w, cell_h,
                            style["plate"], style["rule"])
            p.caption(plate.get("caption", ""), px, cap_y, cell_w)
        y = cap_y + 0.34
        if weapons.get("notes"):
            y = p.columns(weapons["notes"], MARGIN, y, col_w,
                          cols=int(weapons.get("note_columns", 2)))
            y += 0.10

    # --- Field strip, pinned above the footer -------------------------------
    field = promo.get("field") or {}
    if field.get("images"):
        images = field["images"]
        cell_h = float(field.get("height", 1.02))
        gap = 0.10
        strip_y = FOOT_Y - 0.28 - cell_h
        head_y = strip_y - 0.42
        if y > head_y - 0.10:
            p.warnings.append("body copy runs into the field strip — "
                              "shorten a panel, or drop `field`")
        p.heading(field.get("heading", "In the Field"), MARGIN, head_y, col_w)
        cell_w = (col_w - gap * (len(images) - 1)) / len(images)
        for i, item in enumerate(images):
            rel = item["path"] if isinstance(item, dict) else item
            anchor = float(item.get("anchor", 0.3)) if isinstance(item, dict) else 0.3
            b.image_cover(character_dir / rel, MARGIN + i * (cell_w + gap), strip_y,
                          cell_w, cell_h, anchor=anchor)
    elif y > FOOT_Y - 0.10:
        p.warnings.append("body copy runs into the footer — shorten a panel")

    # --- Footer --------------------------------------------------------------
    b.rect(MARGIN, FOOT_Y, col_w, 0.012, style["rule"], style["rule"], 0.2)
    b.text(promo.get("project", ""), MARGIN, FOOT_Y + 0.20, 7.5, style["muted"])
    b.text(_letterspace(promo.get("kicker", "")), MARGIN, FOOT_Y + 0.20, 6.6,
           style["muted"], align="right", width=col_w)
    if promo.get("disclaimer"):
        b.wrapped(promo["disclaimer"], MARGIN, FOOT_Y + 0.40, col_w, 6.2,
                  style["faint"], leading_mult=1.35)

    b.save()
    return p.warnings
