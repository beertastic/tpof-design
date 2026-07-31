# baylan — paste-ready prompts

One file per image. Each is completely self-contained: open it, select all,
paste into the image generator. Nothing to assemble, nothing to remove.

Attach actor reference images to the conversation first — see
03-characters/CAST-REFERENCE.md.

Save each result to source/artwork/ using the exact filename stated at the
top of the prompt, then run:

    python tools/board-generator/generate.py baylan

| File | Image | Ratio | Realism | Anamorphic | Skin |
|---|---|---|---|---|---|
| `01-portrait.txt` | `portrait.png` | 9:16 | yes | yes | yes |
| `02-forest.txt` | `forest.png` | 9:16 | yes | yes | yes |
| `03-industrial_a.txt` | `industrial_a.png` | 9:16 | yes | yes | yes |
| `04-industrial_b.txt` | `industrial_b.png` | 9:16 | yes | yes | yes |
| `05-industrial_c.txt` | `industrial_c.png` | 9:16 | yes | yes | yes |
| `06-detail_portrait.txt` | `detail_portrait.png` | 3:4 | yes | — | yes |
| `07-vision_robes.txt` | `vision_robes.png` | 21:9 | yes | yes | yes |
| `08-expression_strip.txt` | `expression_strip.png` | 16:9 | yes | — | yes |
| `09-blaster.txt` | `blaster.png` | 3:1 | yes | — | — |
| `10-crystal.txt` | `crystal.png` | 1:1 | yes | — | — |
| `11-utility.txt` | `utility.png` | 1:1 | yes | — | — |
| `12-maintenance.txt` | `maintenance.png` | 9:16 | yes | yes | yes |
| `13-materials.txt` | `materials.png` | 5:4 | yes | — | — |

Generated from `Prompts.md` by `tools/prompt-splitter/split.py`.
**Do not edit these files** — edit `Prompts.md` and regenerate.
