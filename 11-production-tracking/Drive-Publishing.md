---
title: "Publishing to Drive — images, boards and the daily check"
asset_id: "TRACK-DRIVE-PUBLISHING"
updated: "2026-08-03"
status: "open — rclone not yet installed"
---

# Publishing to Drive — images, boards and the daily check

**When a character is signed off, their generated images and finished boards go
to Google Drive so the costume department can build from them.** One folder per
character, inside **Costume / Wardrobe**:

<https://drive.google.com/drive/folders/1twIFwScVQhGSgHpTfmPieEMA5jjU5g8T>

```
Costume / Wardrobe /
  Jasu /                       ← the folder name is NOT the repo slug. See below.
    turnarounds /   turn-*.png            the build plates
    artwork /       every other .png      hero, scale, props, materials, expressions
    boards /        *.pdf                 the finished boards
    Jasu_outfit_build_guide.md            hand-written, NOT touched by publishing
```

Each set carries a `PUBLISHED-FROM-REPO.txt` listing the files, their sizes and
the commit that last changed them.

## The rule

> **THE REPOSITORY IS THE SOURCE OF TRUTH. Drive is a copy and may be
> overwritten without asking.**

Publishing is **one-way and destructive on the Drive side**: Drive is made to
match the repo, and anything in those three subfolders that is not in the repo
is deleted.

That is deliberate. **The failure this exists to prevent is somebody building
from a superseded image**, and a stale file sitting beside a current one — same
character, same costume, different boots — is exactly how that happens. A
duplicate is worse than an absence, because an absence gets noticed.

Each set syncs into **its own subfolder**, so a sync can never reach anything
else in the character's folder: build guides, fitting photographs, notes.

### What does not publish

| | |
|---|---|
| `evolution/` | **Superseded by definition.** It is the record of what was rejected, and putting it where a maker can see it is the precise failure above |
| `renders/` | The A2 300 dpi PNGs of the boards. Same content as the PDFs, twenty times the bytes |
| `prompts/attach/` | Inputs to the generator, not outputs. Reference images belong to whoever they came from |

## The Drive folder names are not the repo slugs

`captain-jasu` in this repository is a folder called **`Jasu`** on Drive. People
made those folders by hand before any of this existed.

**The mapping is explicit, in `drive_folder()` at the top of the script, and a
character who is not in it is an error rather than a new folder.** Deriving the
name would be a guess, and a wrong guess does not fail loudly — it quietly
creates a *second* folder for the same character, which is the duplicate this
whole tool exists to prevent. **Add new characters to that mapping using the
exact name of their folder**, which the script prints on every run.

## Sign-off means an approved outfit

A character is published when `outfits.yaml` carries an `approved:` block.
That is already the sign-off gate everywhere else in this repository — the board
generator, the turnaround prompts and `APPROVAL.md` all key off it — and it is
the gate here too. **No approval, no publish**, and the script says so per
character rather than silently skipping.

Right now that is **Captain Jasu** (8 images, no boards yet) and **Shada**
(21 images, 7 boards).

## What you need to install

**One thing: `rclone`.** It needs no Google Cloud project and no API keys — but
it does need to be a **current** build.

> **DO NOT install it with `apt`.** Ubuntu 24.04 ships **v1.60.1-DEV, built in
> 2022**, and its OAuth flow could not complete against Google on 2026-08-03.
> Use the official installer.

```bash
sudo -v && curl https://rclone.org/install.sh | sudo bash
rclone version                   # confirm it is no longer 1.60.x
rclone config
```

**Why the old one fails, diagnosed rather than guessed.** It binds the callback
server on `127.0.0.1:53682` correctly, and localhost is reachable — a `curl` to
it answered in under a millisecond. But **any request to that port without an
OAuth `code` parameter kills the flow instantly**, with
`Auth Error … No code returned by remote server`, after which the port closes
and the browser shows `ERR_CONNECTION_REFUSED`. A browser that prefetches or
preconnects the URL — Brave is the default here — trips it before the real
redirect ever arrives. The failure looks like a firewall problem and is not one.

In `rclone config`:

| | |
|---|---|
| **n** | new remote |
| **name** | `tpof` — exactly this, the scripts look for it |
| **storage** | `drive` |
| **scope** | **`1`, full access.** `drive.file` scope can only see files rclone itself created, so it would not find the existing Costume / Wardrobe folder at all |
| **service_account_file** | blank. That is for non-interactive server auth |
| **advanced config** | `n` |
| **auth** | `y` to use the browser, then **sign in as `info@tristanpretty.com`** |
| **Shared Drive (Team Drive)** | `n`, unless rclone offers a list containing The Price of Freedom |

Then check it, and publish:

```bash
# Costume / Wardrobe is NOT the top of the Drive, so the folder id is needed
# here. The scripts pass it themselves; this one check is by hand.
rclone lsd tpof: --drive-root-folder-id 1twIFwScVQhGSgHpTfmPieEMA5jjU5g8T

./tools/publish-to-drive                    # dry run — shows what WOULD change
./tools/publish-to-drive --go               # publish everything approved
./tools/publish-to-drive captain-jasu --go  # one character
```

That gives full **read, write, overwrite and delete** on Drive. One caveat worth
knowing: **native Google formats** — Docs, Sheets, Slides — can be read and
exported but not overwritten in place. Everything this repo publishes is PNG and
PDF, so it does not arise here.

**The Drive account is `info@tristanpretty.com`**, which is not the Claude
account. That mismatch is expected.

### If the browser step still fails

Take the browser's automatic launch out of it, and paste the link by hand into
**Firefox** rather than the default browser:

```bash
rclone authorize "drive" --auth-no-open-browser
```

Open the link it prints, sign in as `info@tristanpretty.com`, and it will print
a token as JSON. Put that into the remote:

```bash
rclone config update tpof token '{"access_token":...}'
```

**Do not touch `http://127.0.0.1:53682/` while it waits** — not with `curl`, not
with a second browser tab. On the old rclone that request alone ends the flow.

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

## The daily check

```bash
./tools/check-drive          # read-only; exit 1 if anything has drifted
```

**Read-only, always.** It never writes to Drive, because the fix always needs a
person to have decided the repository is right. It appends to
`~/.local/state/tpof/drive-check.log` and raises a desktop notification when
something has drifted, so a cron job nobody reads still reaches you on the day
it matters.

To run it daily — no root, no sudo:

```bash
crontab -e
# then add, adjusting the path if the repo moves:
17 9 * * *  /home/tris/tpof-design/tools/check-drive >/dev/null 2>&1
```

**What counts as drift**, in the words the report uses:

| | |
|---|---|
| `-` **stale on Drive** | A file on Drive the repo does not have. **The dangerous one** — something was superseded and the old copy is still being shown |
| `+` **not published** | A file in the repo not yet on Drive |
| `*` **differ** | Same name, different bytes. Somebody edited the Drive copy, or a publish was interrupted |
| **SHADOWED** | A file loose at the character's folder **root** with the same name as one we publish into a subfolder — see below |

The fix for all of them is `./tools/publish-to-drive --go`.

## KNOWN DRIFT, 2026-08-03 — Drive is currently wrong

Verified against the live folder, not assumed.

**Captain Jasu's Drive folder holds the SUPERSEDED v1 turnarounds**, uploaded
2026-08-01. `turn-field-front.png` there is **2,207,890 bytes — byte-for-byte
the v1 front** now archived at `evolution/00-first-approved-2026-08-01.png`.

So the costume department currently has, from Drive:

- **ankle boots** where the build list says tall to the calf
- **a whistle at the belt** where there is exactly one, at the throat
- the superseded hair

**And they are loose at the folder root, not in a `turnarounds/` subfolder.**
That matters more than it looks. Publishing creates `turnarounds/` with the
correct plates and **leaves the five superseded ones sitting one level up, still
called `turn-field-front.png`** — two files, same name, different boots, which
is this document's opening failure with extra steps.

The sync deliberately cannot reach the folder root, because
`Jasu_outfit_build_guide.md` lives there and is hand-written. So the script
**reports** shadowed files, and removes them only when asked:

```bash
./tools/publish-to-drive captain-jasu --go --purge-shadows
```

That deletes **only** root files whose names exactly match something being
published. The build guide is untouched. A stray `.gitkeep` is also up there;
it is excluded from publishing and is harmless, so it is left alone.

**This is the first job once rclone is set up.**

## See also

- [`Cast-Data-Source.md`](Cast-Data-Source.md) — the traffic in the other
  direction, and why it does **not** happen: personal data stays in Drive and
  never enters this repository. Note that the Costume / Wardrobe folder holds
  cast measurements and a mood board belonging to other people. **Publishing
  never touches the parent folder**, only the per-character subfolders
- [`../03-characters/APPROVAL.md`](../03-characters/APPROVAL.md) — what sign-off means
