#!/usr/bin/env python3
"""Render the Fountain screenplay to PDF, and optionally to Final Draft.

    python tools/script-convert/render.py                 # current draft -> PDF
    python tools/script-convert/render.py --format fdx    # -> Final Draft

The Fountain file is the source. Everything this produces is disposable and
regenerable, which is why the outputs are gitignored.

FDX matters more than it looks: it is what lets the writer open a revision in
Final Draft, work in the tool they actually use, and hand it back — without
anyone having to adopt this repository's way of working.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_SOURCE = Path("02-story/scenes/the-price-of-freedom-v9.fountain")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", nargs="?", type=Path, default=DEFAULT_SOURCE)
    ap.add_argument("--format", default="pdf", choices=["pdf", "fdx", "html"])
    ap.add_argument("--out", type=Path, help="defaults to the source name")
    args = ap.parse_args()

    if not args.source.is_file():
        print(f"no such file: {args.source}", file=sys.stderr)
        return 1

    try:
        from screenplain.main import main as screenplain_main
    except ImportError:
        print("screenplain is not installed. pip install -r "
              "tools/script-convert/requirements.txt", file=sys.stderr)
        return 2

    out = args.out or args.source.with_suffix("." + args.format)
    screenplain_main(["--format", args.format, str(args.source), str(out)])
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
