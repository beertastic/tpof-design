# captain-jasu — paste-ready prompts

One file per image. Each is completely self-contained: open it, select all,
paste into the image generator. Nothing to assemble, nothing to remove.

Each prompt lists every photograph it needs as a public URL — fetch
them, do not ask for attachments. See 03-characters/CAST-REFERENCE.md.

Save each result to source/artwork/ using the exact filename stated at the
top of the prompt, then run:

    python tools/board-generator/generate.py captain-jasu

| File | Image | Ratio | Realism | Anamorphic | Skin |
|---|---|---|---|---|---|
| `01-hero.txt` | `hero.png` | 9:16 | yes | yes | yes |
| `02-scale_figure.txt` | `scale_figure.png` | 3:4 | yes | — | yes |
| `03-camp_day.txt` | `camp_day.png` | 9:16 | yes | yes | yes |
| `04-captaining.txt` | `captaining.png` | 9:16 | yes | yes | yes |
| `05-candid.txt` | `candid.png` | 9:16 | yes | yes | yes |
| `06-portrait.txt` | `portrait.png` | 3:4 | yes | — | yes |
| `07-headdress.txt` | `headdress.png` | 3:4 | yes | — | yes |
| `08-expression_strip.txt` | `expression_strip.png` | 16:9 | yes | — | yes |
| `09-blaster.txt` | `blaster.png` | 1:1 | yes | — | — |
| `10-whistle_and_leash.txt` | `whistle_and_leash.png` | 1:1 | yes | — | — |
| `11-mantle_detail.txt` | `mantle_detail.png` | 1:1 | yes | — | — |
| `12-akk_together.txt` | `akk_together.png` | 9:16 | yes | yes | yes |
| `13-material_cloth.txt` | `material_cloth.png` | 1:1 | yes | — | — |
| `14-material_leather.txt` | `material_leather.png` | 1:1 | yes | — | — |
| `15-material_hardware.txt` | `material_hardware.png` | 1:1 | yes | — | — |
| `16-tone_collage.txt` | `tone_collage.png` | 2:3 | yes | yes | yes |

Generated from `Prompts.md` by `tools/prompt-splitter/split.py`.
**Do not edit these files** — edit `Prompts.md` and regenerate.
