# TPOF Production Bible

Version-controlled pre-production documentation for the TPOF fan film.

## Canonical source order

1. Production Design Bible
2. Faction guide
3. Character or asset sheet
4. Scene brief
5. Camera direction

Later documents may add detail but must not contradict earlier governing documents without a recorded revision.

## Repository structure

- `01-production-design/` — governing visual rules
- `02-story/` — story and sequence information
- `03-characters/` — one directory per character
- `04-factions/` — shared group visual language
- `05-props/` — hero and background props
- `06-vehicles/` — vehicles and craft
- `07-locations/` — sets, planets, and environments
- `08-species/` — biological and cultural design rules
- `09-prompt-library/` — shared prompt blocks used by every character pack
- `10-assets/` — reference images and exported production sheets
- `11-production-tracking/` — status board and open questions
- `tools/board-generator/` — builds the A2 production boards from `board-data.yaml`

Each number is used exactly once. Empty categories carry a `.gitkeep` so the
structure is present in the repository rather than only on one machine.

## Working method

1. Create or revise Markdown on a feature branch.
2. Record unresolved decisions under **Outstanding Questions**.
3. Change status from `Draft` to `Approved` only after review.
4. Merge approved work into `main`.
5. Tag milestones such as `character-shada-v1.0`.

## Suggested commit style

- `docs(character): define Shada biography`
- `design(costume): revise Shada armour language`
- `prop(shada): lock hero knife design`
- `chore(repo): add production folder structure`

## Remote hosting

This repository is local and includes its Git history. After extracting it, connect it to GitHub, GitLab, or another Git host:

```bash
git remote add origin <repository-url>
git push -u origin main --tags
```

## Generated output is not committed

`renders/`, the PPTX and the multi-page master PDF are gitignored — they are
rebuilt in one command and would otherwise add ~100 MB per character per
rebuild. Committed instead: source documents, `board-data.yaml`,
`source/artwork/` and the five board PDFs.

## Current production import

The Filmanize scene breakdown has been imported under `02-story/script-breakdown/`. Placeholder documents now exist for all currently identified principal characters, factions and locations.