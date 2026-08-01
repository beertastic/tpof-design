# shada — paste-ready prompts

One file per image. Each is completely self-contained: open it, select all,
paste into the image generator. Nothing to assemble, nothing to remove.

Each prompt lists every reference image it needs as a public URL — fetch
them, do not ask for attachments. See 03-characters/CAST-REFERENCE.md.

Save each result to source/artwork/ using the exact filename stated at the
top of the prompt, then run:

    python tools/board-generator/generate.py shada

| File | Image | Ratio | Realism | Anamorphic | Skin |
|---|---|---|---|---|---|
| `01-hero.txt` | `hero.png` | 9:16 | yes | yes | yes |
| `02-scale_figure.txt` | `scale_figure.png` | 3:4 | yes | — | yes |
| `03-camp_day.txt` | `camp_day.png` | 9:16 | yes | yes | yes |
| `04-forest.txt` | `forest.png` | 9:16 | yes | yes | yes |
| `05-scale_portrait.txt` | `scale_portrait.png` | 3:4 | yes | — | yes |
| `06-species_strip.txt` | `species_strip.png` | 21:9 | yes | — | yes |
| `07-expression_strip.txt` | `expression_strip.png` | 16:9 | yes | — | yes |
| `08-knife.txt` | `knife.png` | 3:1 | yes | — | — |
| `09-blaster.txt` | `blaster.png` | 1:1 | yes | — | — |
| `10-utility.txt` | `utility.png` | 1:1 | yes | — | — |
| `11-maintenance.txt` | `maintenance.png` | 9:16 | yes | yes | yes |
| `12-material-scale.txt` | `material-scale.png` | 1:1 | yes | — | — |
| `13-material-leather.txt` | `material-leather.png` | 1:1 | yes | — | — |
| `14-material-cloth.txt` | `material-cloth.png` | 1:1 | yes | — | — |
| `15-material-hardware.txt` | `material-hardware.png` | 1:1 | yes | — | — |
| `16-tone-collage.txt` | `tone-collage.png` | 2:3 | yes | yes | yes |

Generated from `Prompts.md` by `tools/prompt-splitter/split.py`.
**Do not edit these files** — edit `Prompts.md` and regenerate.
