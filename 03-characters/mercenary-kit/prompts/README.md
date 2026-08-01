# generic-mercenary — paste-ready prompts

One file per image. Each is completely self-contained: open it, select all,
paste into the image generator. Nothing to assemble, nothing to remove.

Attach actor reference images to the conversation first — see
03-characters/CAST-REFERENCE.md.

Save each result to source/artwork/ using the exact filename stated at the
top of the prompt, then run:

    python tools/board-generator/generate.py generic-mercenary

| File | Image | Ratio | Realism | Anamorphic | Skin |
|---|---|---|---|---|---|
| `01-lineup.txt` | `lineup.png` | 2:1 | yes | — | yes |
| `02-sabacc.txt` | `sabacc.png` | 16:9 | yes | yes | yes |
| `03-pursuit.txt` | `pursuit.png` | 16:9 | yes | yes | yes |
| `04-kit-heads.txt` | `kit-heads.png` | 3:1 | yes | — | yes |
| `05-kit-harness.txt` | `kit-harness.png` | 3:1 | yes | — | — |
| `06-kit-plating.txt` | `kit-plating.png` | 3:1 | yes | — | — |
| `07-kit-boots.txt` | `kit-boots.png` | 3:1 | yes | — | — |
| `08-kit-marks.txt` | `kit-marks.png` | 3:1 | yes | — | — |
| `09-bandolier.txt` | `bandolier.png` | 1:1 | yes | — | — |
| `10-heavy-fur.txt` | `heavy-fur.png` | 1:1 | yes | — | — |
| `11-nearhuman-markings.txt` | `nearhuman-markings.png` | 3:4 | yes | — | yes |
| `12-materials.txt` | `materials.png` | 1:1 | yes | — | — |
| `13-tone-collage.txt` | `tone-collage.png` | 2:3 | yes | yes | yes |

Generated from `Prompts.md` by `tools/prompt-splitter/split.py`.
**Do not edit these files** — edit `Prompts.md` and regenerate.
