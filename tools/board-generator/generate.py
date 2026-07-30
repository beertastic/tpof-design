#!/usr/bin/env python3
"""Generate TPOF character production boards from JSON data and artwork.

Usage:
    python tools/board-generator/generate.py 03-characters/shada
    python tools/board-generator/generate.py 03-characters/shada --pdf-only
    python tools/board-generator/generate.py 03-characters/shada --png-only

The script is character-agnostic. It reads <character>/board-data.json and
places the referenced artwork into a fixed A2 landscape template. Text is
drawn as vector PDF typography, avoiding AI-generated blurry lettering.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A2, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

PAGE_W, PAGE_H = landscape(A2)

def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc

def wrap_lines(text: str, width: float, font: str, size: float) -> list[str]:
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip()
        if stringWidth(test, font, size) <= width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def draw_wrapped(c, text, x, y, width, font="Helvetica", size=12,
                 leading=16, colour=HexColor("#161817"), max_lines=None):
    c.setFont(font, size)
    c.setFillColor(colour)
    lines = wrap_lines(text, width, font, size)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y

def draw_fitted_image(c, image_path: Path, x, y, w, h):
    with Image.open(image_path) as im:
        iw, ih = im.size
    scale = max(w / iw, h / ih)
    dw, dh = iw * scale, ih * scale
    dx, dy = x + (w - dw) / 2, y + (h - dh) / 2
    c.saveState()
    path = c.beginPath()
    path.rect(x, y, w, h)
    c.clipPath(path, stroke=0, fill=0)
    c.drawImage(ImageReader(str(image_path)), dx, dy, dw, dh, preserveAspectRatio=True, mask="auto")
    c.restoreState()

def make_pdf(character_dir: Path, board: dict, data: dict, style: dict) -> Path:
    out = character_dir / board["filename"]
    bg = HexColor(style["background"])
    ink = HexColor(style["ink"])
    muted = HexColor(style["muted"])
    accent = HexColor(style["accent"])
    panel = HexColor(style["panel"])
    line = HexColor(style["line"])

    c = canvas.Canvas(str(out), pagesize=(PAGE_W, PAGE_H))
    c.setTitle(f'{data["character"]} - {board["title"]}')
    c.setAuthor("TPOF Art Department")
    c.setSubject("Production Design Bible character board")
    c.setFillColor(bg)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    margin = 32
    header_h = 72
    footer_h = 34

    c.setFillColor(ink)
    c.setFont("Helvetica-Bold", 27)
    c.drawString(margin, PAGE_H - 42, data["character"].upper())
    c.setFont("Helvetica-Bold", 15)
    c.drawString(220, PAGE_H - 36, board["title"])
    c.setFont("Helvetica", 8.5)
    meta = (
        f'PROJECT: {data["project"].upper()}   |   ASSET: {data["asset_id"]}   |   '
        f'STATUS: {data["status"]}   |   VERSION: {data["version"]}   |   DATE: {data["date"]}'
    )
    c.drawString(220, PAGE_H - 52, meta)
    c.setStrokeColor(line)
    c.line(margin, PAGE_H - header_h, PAGE_W - margin, PAGE_H - header_h)

    body_y = footer_h + 26
    body_h = PAGE_H - header_h - body_y - 6
    left_w = PAGE_W * 0.64
    art_x, art_y = margin, body_y + 112
    art_w, art_h = left_w - margin - 8, body_h - 112
    artwork = character_dir / board["artwork"]
    if not artwork.exists():
        raise SystemExit(f"Artwork not found: {artwork}")
    draw_fitted_image(c, artwork, art_x, art_y, art_w, art_h)
    c.setStrokeColor(line)
    c.rect(art_x, art_y, art_w, art_h, fill=0, stroke=1)

    summary_y = body_y + 98
    c.setFillColor(panel)
    c.roundRect(art_x, body_y, art_w, 88, 4, fill=1, stroke=0)
    c.setFillColor(accent)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(art_x + 12, summary_y - 14, "DESIGN INTENT")
    draw_wrapped(c, board["summary"], art_x + 12, summary_y - 31, art_w - 24,
                 size=10.2, leading=13.5, colour=ink, max_lines=4)

    right_x = left_w + 12
    right_w = PAGE_W - right_x - margin
    sec_top = PAGE_H - header_h - 10
    section_gap = 10
    section_h = (body_h - section_gap * 2) / 3

    for idx, section in enumerate(board["sections"]):
        sy = sec_top - (idx + 1) * section_h - idx * section_gap
        c.setFillColor(panel)
        c.roundRect(right_x, sy, right_w, section_h, 4, fill=1, stroke=0)
        c.setFillColor(accent)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(right_x + 12, sy + section_h - 20, section["heading"])
        y = sy + section_h - 39
        c.setFont("Helvetica", 9.5)
        c.setFillColor(ink)
        for item in section["items"]:
            c.circle(right_x + 17, y + 2, 1.5, fill=1, stroke=0)
            y = draw_wrapped(c, item, right_x + 25, y + 6, right_w - 38,
                             size=9.3, leading=12, colour=ink, max_lines=2) - 5

    c.setStrokeColor(line)
    c.line(margin, footer_h, PAGE_W - margin, footer_h)
    c.setFillColor(muted)
    c.setFont("Helvetica", 8)
    c.drawString(margin, 18, f'THE PRICE OF FREEDOM - PRODUCTION DESIGN BIBLE')
    c.drawCentredString(PAGE_W / 2, 18, board["footer"])
    c.drawRightString(PAGE_W - margin, 18, f'BOARD {board["number"]} / {len(data["boards"]):02d}')
    c.save()
    return out

def render_pdf(pdf_path: Path, png_path: Path, dpi: int):
    if fitz is None:
        raise SystemExit("PNG export requires PyMuPDF. Install requirements.txt or run with --pdf-only.")
    doc = fitz.open(pdf_path)
    page = doc[0]
    zoom = dpi / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    pix.save(png_path)
    doc.close()
    with Image.open(png_path) as im:
        im.save(png_path, dpi=(dpi, dpi))

def main():
    parser = argparse.ArgumentParser(description="Generate TPOF production boards.")
    parser.add_argument("character_dir", type=Path, help="Character directory containing board-data.json")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--pdf-only", action="store_true")
    group.add_argument("--png-only", action="store_true")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--template", type=Path, default=Path(__file__).parent / "templates" / "a2-landscape-v1.json")
    args = parser.parse_args()

    character_dir = args.character_dir.resolve()
    data = load_json(character_dir / "board-data.json")
    template = load_json(args.template)
    style = template["style"]
    render_dir = character_dir / template["output"]["png_directory"]
    render_dir.mkdir(parents=True, exist_ok=True)

    generated = []
    for board in data["boards"]:
        pdf_path = character_dir / board["filename"]
        png_path = render_dir / board["render"]
        if not args.png_only:
            pdf_path = make_pdf(character_dir, board, data, style)
            generated.append(pdf_path)
        if not args.pdf_only:
            if not pdf_path.exists():
                raise SystemExit(f"PDF required for PNG render is missing: {pdf_path}")
            render_pdf(pdf_path, png_path, args.dpi)
            generated.append(png_path)

    print("Generated:")
    for path in generated:
        print(f"  {path.relative_to(Path.cwd()) if path.is_relative_to(Path.cwd()) else path}")

if __name__ == "__main__":
    main()
