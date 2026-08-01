# shin — paste-ready prompts

One file per image. Each is completely self-contained: open it, select all,
paste into the image generator. Nothing to assemble, nothing to remove.

Each prompt lists every reference image it needs as a public URL — fetch
them, do not ask for attachments. See 03-characters/CAST-REFERENCE.md.

Save each result to source/artwork/ using the exact filename stated at the
top of the prompt, then run:

    python tools/board-generator/generate.py shin

| File | Image | Ratio | Realism | Anamorphic | Skin |
|---|---|---|---|---|---|
| `01-portrait.txt` | `portrait.png` | 9:16 | yes | yes | yes |
| `02-forest.txt` | `forest.png` | 9:16 | yes | yes | yes |
| `03-sky.txt` | `sky.png` | 9:16 | yes | yes | yes |
| `04-camp_night.txt` | `camp_night.png` | 9:16 | yes | yes | yes |
| `05-mother.txt` | `mother.png` | 9:16 | yes | yes | yes |
| `06-detail_portrait.txt` | `detail_portrait.png` | 3:4 | yes | — | yes |
| `07-vision_shadow.txt` | `vision_shadow.png` | 21:9 | yes | yes | yes |
| `08-expression_strip.txt` | `expression_strip.png` | 16:9 | yes | — | yes |
| `09-clasp.txt` | `clasp.png` | 3:1 | yes | — | — |
| `10-hair_study.txt` | `hair_study.png` | 1:1 | yes | — | — |
| `11-utility.txt` | `utility.png` | 1:1 | yes | — | — |
| `12-ditch.txt` | `ditch.png` | 9:16 | yes | yes | yes |
| `13-materials.txt` | `materials.png` | 5:4 | yes | — | — |
| `14-tone-collage.txt` | `tone-collage.png` | 2:3 | yes | yes | yes |

Generated from `Prompts.md` by `tools/prompt-splitter/split.py`.
**Do not edit these files** — edit `Prompts.md` and regenerate.
