"""Direct PDF rendering for TPOF production boards.

Draws boards straight to PDF with reportlab — no PowerPoint, no LibreOffice.
Text stays vector, images are placed with a contain fit, and the geometry
matches the PPTX layout exactly (inches, top-left origin, flipped internally).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

PT = 72.0  # points per inch


class Board:
    """One A2 landscape page, addressed in inches from the top-left."""

    def __init__(self, path: Path, width_in: float, height_in: float):
        self.w, self.h = width_in, height_in
        self.c = canvas.Canvas(str(path), pagesize=(width_in * PT, height_in * PT))

    def _y(self, y_in: float, h_in: float = 0.0) -> float:
        """Top-left inches -> reportlab bottom-left points."""
        return (self.h - y_in - h_in) * PT

    def background(self, colour: str) -> None:
        self.c.setFillColor(HexColor(colour))
        self.c.rect(0, 0, self.w * PT, self.h * PT, stroke=0, fill=1)

    def rect(self, x, y, w, h, fill: str, line: str, line_w: float = 0.6) -> None:
        self.c.setFillColor(HexColor(fill))
        self.c.setStrokeColor(HexColor(line))
        self.c.setLineWidth(line_w)
        self.c.rect(x * PT, self._y(y, h), w * PT, h * PT, stroke=1, fill=1)

    def text(self, s: str, x, y, size, colour: str, bold=False, align="left",
             width: float | None = None) -> None:
        font = "Helvetica-Bold" if bold else "Helvetica"
        self.c.setFont(font, size)
        self.c.setFillColor(HexColor(colour))
        ty = self._y(y) - size
        if align == "right" and width:
            self.c.drawRightString((x + width) * PT, ty, s)
        elif align == "center" and width:
            self.c.drawCentredString((x + width / 2) * PT, ty, s)
        else:
            self.c.drawString(x * PT, ty, s)

    def wrapped(self, s: str, x, y, w, size, colour, leading_mult=1.22) -> float:
        """Draw text wrapped to width. Returns the y (inches) after the last line."""
        self.c.setFont("Helvetica", size)
        self.c.setFillColor(HexColor(colour))
        limit = w * PT
        words, line, lines = s.split(), "", []
        for word in words:
            trial = f"{line} {word}".strip()
            if self.c.stringWidth(trial, "Helvetica", size) <= limit:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
        leading = size * leading_mult
        for i, ln in enumerate(lines):
            self.c.drawString(x * PT, self._y(y) - size - i * leading, ln)
        return y + (len(lines) * leading) / PT

    def image_contain(self, path: Path, x, y, w, h, panel: str, line: str) -> None:
        self.rect(x, y, w, h, panel, line)
        with Image.open(path) as im:
            iw, ih = im.size
        scale = min(w / iw, h / ih)
        dw, dh = iw * scale, ih * scale
        px, py = x + (w - dw) / 2, y + (h - dh) / 2
        self.c.drawImage(ImageReader(str(path)), px * PT, self._y(py, dh),
                         dw * PT, dh * PT, mask="auto")

    def save(self) -> None:
        self.c.showPage()
        self.c.save()


def render_board(out_pdf: Path, character_dir: Path, config: dict[str, Any],
                 style: dict[str, str], board: dict[str, Any],
                 page: int, total: int, w_in: float, h_in: float) -> None:
    b = Board(out_pdf, w_in, h_in)
    b.background(style["background"])

    b.text(str(config["character"]).upper(), 0.45, 0.25, 30, style["ink"], bold=True)
    b.text(board["title"], 3.0, 0.34, 19, style["ink"], bold=True)
    meta = (f'{board.get("label", "")} | ASSET {config["asset_id"]} | '
            f'VERSION {config["version"]} | STATUS {config["status"]} | '
            f'{config.get("date", "")}')
    b.text(meta, 3.0, 0.82, 8.5, style["muted"])
    b.rect(0.45, 1.14, 22.45, 0.015, style["line"], style["line"], 0.3)

    for img in board.get("images", []):
        b.image_contain(character_dir / img["path"], img["x"], img["y"],
                        img["w"], img["h"], style["image_panel"], style["line"])

    for sec in board.get("sections", []):
        x, y, w, h = sec["x"], sec["y"], sec["w"], sec["h"]
        b.rect(x, y, w, h, style["panel"], style["line"])
        b.text(sec["heading"], x + 0.18, y + 0.14,
               sec.get("heading_size", 11.5), style["accent"], bold=True)
        size = sec.get("font_size", 12)
        cy = y + 0.56
        for item in sec.get("items", []):
            cy = b.wrapped(f"• {item}", x + 0.18, cy, w - 0.36, size, style["ink"])
            cy += 0.055

    b.text(config.get("footer_left", ""), 0.45, 16.03, 8.2, style["muted"])
    b.text(board.get("tagline", ""), 7.4, 16.03, 8.2, style["muted"],
           align="center", width=9.0)
    b.text(f"PAGE {page} OF {total}", 20.3, 16.03, 8.2, style["muted"],
           align="right", width=2.6)
    b.save()
