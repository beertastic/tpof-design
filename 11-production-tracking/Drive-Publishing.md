---
title: "Publishing to Drive — signed-off turnarounds"
asset_id: "TRACK-DRIVE-PUBLISHING"
updated: "2026-08-03"
status: "open — rclone not yet installed"
---

# Publishing to Drive — signed-off turnarounds

**When a character is signed off, their turnarounds go to Google Drive so the
costume department can build from them.** One folder per character, inside
**Costume / Wardrobe**:

<https://drive.google.com/drive/folders/1twIFwScVQhGSgHpTfmPieEMA5jjU5g8T>

```
Costume / Wardrobe /
  Captain Jasu / turnarounds /   turn-field-front.png … + PUBLISHED-FROM-REPO.txt
  Shada        / turnarounds /   …
```

## The rule

> **THE REPOSITORY IS THE SOURCE OF TRUTH. Drive is a copy and may be
> overwritten without asking.**

Publishing is **one-way and destructive on the Drive side**: Drive is made to
match the repo, and anything in the character's `turnarounds/` folder that is not
in the repo is deleted.

That is deliberate. **The failure this exists to prevent is somebody building
from a superseded image**, and a stale file sitting beside a current one — same
character, same costume, different boots — is exactly how that happens. A
duplicate is worse than an absence, because an absence gets noticed.

Only the **turnarounds** are synced, into a `turnarounds/` subfolder, so a sync
can never delete build guides, sketches or notes that live in the same character
folder.

## Sign-off means an approved outfit

A character is published when `outfits.yaml` carries an `approved:` block.
That is already the sign-off gate everywhere else in this repository — the board
generator, the turnaround prompts and `APPROVAL.md` all key off it — and it is
the gate here too. **No approval, no publish**, and the script says so per
character rather than silently skipping.

## How

```bash
./tools/publish-to-drive                 # dry run — shows what WOULD change
./tools/publish-to-drive --go            # publish everything approved
./tools/publish-to-drive captain-jasu --go
```

**It needs `rclone`, which is not installed yet.** Setup is in the header of the
script: install it, run `rclone config`, create a Drive remote named exactly
`tpof`, and choose **full drive scope** — `drive.file` scope cannot see the
existing Costume/Wardrobe folder, because rclone did not create it.

The Drive account is **`info@tristanpretty.com`**, which is not the Claude
account.

### Why not the Drive connector Claude already has

Two hard limits, both checked rather than assumed:

1. **It cannot update or delete.** It can create files and folders and nothing
   else. Re-publishing through it leaves **two files with the same name and
   different contents**, which is the precise failure this process exists to
   prevent.
2. **It has to carry the image inline.** A 2 MB plate is about 2.7 million
   characters once base64-encoded. It is not a practical transport for a
   twenty-one image pack.

So the connector is used for **checking** — which is cheap, because listing
names, sizes and dates needs no file contents — and `rclone` does the moving.

## KNOWN DRIFT, 2026-08-03 — Drive is currently wrong

**Captain Jasu's Drive folder holds the SUPERSEDED v1 turnarounds**, uploaded
2026-08-01. `turn-field-front.png` there is **2,207,890 bytes — byte-for-byte the
v1 front** now archived at `evolution/00-first-approved-2026-08-01.png`.

So the costume department currently has, from Drive:

- **ankle boots** where the build list says tall to the calf
- **a whistle at the belt** where there is exactly one, at the throat
- the superseded hair

**This is the first thing to publish once rclone is set up.** A stray `.gitkeep`
also got uploaded and the sync will remove it.

## The daily check

- [ ] **Check Drive against the repository, daily.** Compare each published
      character's `turnarounds/` folder against `source/artwork/`: same filenames,
      and a `PUBLISHED-FROM-REPO.txt` whose commit matches what the repo has for
      those images. Report drift; do not fix it silently.

**Claude can run this check through the Drive connector** — it needs only file
listings, not contents, so it is cheap. It cannot fix the drift, only report it,
because the connector cannot delete or overwrite. Fixing is
`./tools/publish-to-drive --go`.

**What counts as drift:**

| | |
|---|---|
| A file in Drive that is not in the repo | **Stale — the dangerous one.** Something was superseded and the old copy is still being shown |
| A file in the repo that is not in Drive | Not yet published |
| Two files with the same name | Somebody uploaded by hand, or through a tool that cannot overwrite |
| `PUBLISHED-FROM-REPO.txt` missing or on an old commit | Published before this process existed, or published and then the repo moved on |

**Worth automating as a scheduled agent** rather than remembering — see `/schedule`.
Not set up yet; a daily run that reports drift and does nothing else is the
right shape, because the fix needs a person to have decided the repo is right.

## See also

- [`Cast-Data-Source.md`](Cast-Data-Source.md) — the traffic in the other
  direction, and why it does **not** happen: personal data stays in Drive and
  never enters this repository
- [`../03-characters/APPROVAL.md`](../03-characters/APPROVAL.md) — what sign-off means
