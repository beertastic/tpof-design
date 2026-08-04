---
title: "Publishing to Drive — images, boards and the daily check"
asset_id: "TRACK-DRIVE-PUBLISHING"
updated: "2026-08-04"
status: "live — publishing, Drive verified in sync 2026-08-04"
---

# Publishing to Drive — images, boards and the daily check

**When a character is signed off, their generated images and finished boards go
to Google Drive so the costume department can build from them.** One folder per
character, inside **Costume / Wardrobe**:

<https://drive.google.com/drive/folders/1twIFwScVQhGSgHpTfmPieEMA5jjU5g8T>

```
Costume / Wardrobe /
  Jasu /                       ← the folder name is NOT the repo slug. See below.
    _build_guide.md              what a maker works from
    _published-from-repo.txt     the commit, the files, their sizes
    turn-field-front.png         the build plates
    turn-field-left.png
    …
    blaster.png                  every other generated image
    material_cloth.png
    …
    Costume-Board.pdf            the finished boards
  archive /                    ← superseded folders and documents, kept not deleted
```

## FLAT IS THE STANDARD — decided 2026-08-04

**One folder per character, every file loose in it, no subfolders.** This applies
to every character added from now on.

**Why.** The costume department browses Drive by opening one image and arrowing
left and right through the set. Subfolders broke that: turnarounds, artwork and
boards each had to be opened separately, and nobody browses a costume that way.
Flat means the whole character is one uninterrupted scroll.

**The two meta files carry a `_` prefix** so they sort above the images and stay
out of the way. `_build_guide.md` is the first thing in the folder, which is
where the thing a maker actually works from belongs.

**What flat costs, stated plainly.** Until 2026-08-04 each set synced into its
own subfolder, so a sync could never reach the character's folder root and
anything left there by hand survived. It no longer does — the root *is* the sync
target, so **a file dropped into a character's Drive folder is deleted on the
next publish.** That is the contract rather than a regression: the repository is
the source of truth. But it used to have an escape hatch and no longer does.

**One namespace.** Flat means turnarounds, artwork and boards share a filename
space. The script refuses to publish a character with duplicate basenames rather
than let one file silently overwrite another.

**It also retired `check_shadows()`.** That function existed because the sync
wrote into subfolders and could not reach the folder root, so a superseded file
left loose up there survived every publish — which is exactly what happened to
Jasu's v1 turnarounds on 2026-08-03. Publishing flat designs the failure out
instead of reporting on it, so the function and its `--purge-shadows` flag are
gone.

## The build guide is published, not hand-written

**Until 2026-08-04 the build guide was a hand-uploaded Drive document with no
source in this repository**, and it drifted badly. `Jasu_outfit_build_guide.md.docx`
was written from photographs on 2026-08-01, two days before the v2 rebuild, and
was wrong in five ways at once:

| It said | It is |
|---|---|
| A **4'11" (150 cm)** wearer | **155 cm (5 ft 1 in)** |
| **Ankle boots** | **Tall**, well up the calf |
| A whistle as a **belt fob** | **One whistle, at her throat** |
| A bought **Etsy leather pauldron** | **Made, stiffened cloth** — `outfits.yaml` calls the pauldron "the single most wrong thing it is possible to buy for this costume" |
| **Hair cuffs** | **Two mismatched bone horns**, printed |

`outfits.yaml` had already caught two of them in its own component notes — the
"vintage keychain fob" and the pauldron — because the design moved and the guide
did not. **Nothing could have caught the rest, because nothing in the repository
knew the document existed.**

So it now lives at `03-characters/<character>/Build-Guide.md`, derived from
`outfits.yaml`, and publishes to `docs/` like everything else. **Only
`Build-Guide.md` is published** — `Character.md` and `Prompts.md` are working
documents for this repository, and the reasoning in them is not what a maker
needs at a bench.

The superseded `.docx` is in `archive/`.

## Holding a file back

**`do-not-publish.txt` in a character's folder keeps named files off Drive**, one
filename per line, `#` for comments. It exists for artwork that is on disk but
known wrong and waiting on a re-roll — **to rclone, a failed plate is
indistinguishable from a good one.**

Captain Jasu holds four: `captaining.png`, `headdress.png`, `portrait.png` and
`expression_strip.png`, all failed re-rolls listed in `Jasu-Image-TODO.md`.
Publishing them would send the costume department a generic dog and superseded
hair, which is the exact failure this whole process exists to prevent.

**Held files are reported on every run and counted in the summary**, because a
hold is a temporary state waiting on a re-roll. Silence is how four failed plates
become four permanently missing ones. Delete a line the moment its replacement is
generated and correct.

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

> **Prefer the official installer over `apt`.** Ubuntu 24.04 ships
> **v1.60.1-DEV, built in 2022**, whose errors during setup are close to
> unreadable. v1.75 says what is actually wrong.

```bash
sudo -v && curl https://rclone.org/install.sh | sudo bash
rclone version                   # confirm it is no longer 1.60.x
rclone config
```

### LEAVE `client_id` AND `client_secret` BLANK

**This is the one that cost an evening.** Both prompts say *"Leave blank
normally"* and they mean it — blank makes rclone use its own registered Google
application, which is what you want.

A stray keystroke put `client_id = scope1` in the config on the first attempt —
the answer to the *scope* question, one prompt too early. Every symptom after
that was downstream of it:

| What it looked like | What it was |
|---|---|
| rclone 1.60: `No code returned by remote server`, then the browser showing `ERR_CONNECTION_REFUSED` | Google rejected the client and redirected back with no code. The old build could not say so, and the closed port made it look like a firewall |
| rclone 1.75: **`Access blocked: Authorisation error — The OAuth client was not found. Error 401: invalid_client`** | The same thing, said plainly |

If you see `invalid_client`, check the config before anything else:

```bash
cat ~/.config/rclone/rclone.conf
```

It should be exactly this — no `client_id`, no `client_secret`:

```ini
[tpof]
type = drive
scope = drive
token = {"access_token":...}
```

**Sign in as `info@tristanpretty.com`.** The browser will offer whichever Google
account you last used; a personal account will authorise happily and then see
none of the production folders.

In `rclone config`:

| | |
|---|---|
| **n** | new remote |
| **name** | `tpof` — exactly this, the scripts look for it |
| **storage** | `drive` |
| **scope** | **`1`, full access.** `drive.file` scope can only see files rclone itself created, so it would not find the existing Costume / Wardrobe folder at all |
| **client_id** / **client_secret** | **blank, both.** See above — this is where it went wrong |
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

### DEADLINE — a client_id of our own is needed during 2026

Blank `client_id` means rclone's **shared** Google application, and rclone now
warns on every run:

> This remote uses rclone's shared Google Drive client_id, which is being
> retired and **will stop working during 2026**.

So the "no Google Cloud project needed" above is true **now and not for much
longer**. Before it lapses, make a client id — it is free, takes about ten
minutes, and the steps are at <https://rclone.org/drive/#making-your-own-client-id>
— then set it on the existing remote without redoing anything else:

```bash
rclone config update tpof client_id     <the id>
rclone config update tpof client_secret <the secret>
rclone config reconnect tpof:
```

**When that day comes, `client_id` finally gets a real value.** Until then it
stays blank, and `scope1` is not a value. The scripts pass
`--log-level ERROR` so the notice does not print five times a run; this section
is the record of it.

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
with a second browser tab. A request there without an OAuth `code` ends the flow
immediately, and on rclone 1.60 it does so fatally. That is a real effect, but
it was **not** what broke the setup here; `client_id` was.

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

**INSTALLED 2026-08-04**, in `tris`'s user crontab — no root, no sudo:

```
17 9 * * * /home/tris/tpof-design/tools/check-drive >/dev/null 2>&1
```

It points at the **main checkout**, not a worktree, so it keeps working after
any branch is merged and deleted.

One thing cron does not give you is a session bus or a `DISPLAY`, and without
them `notify-send` fails silently — which would have made the notification pure
decoration. The script now falls back to the user bus at
`/run/user/$(id -u)/bus`, which is where it always is, and says so in the log if
it still cannot raise one.

**What counts as drift**, in the words the report uses:

| | |
|---|---|
| `-` **stale on Drive** | A file on Drive the repo does not have. **The dangerous one** — something was superseded and the old copy is still being shown |
| `+` **not published** | A file in the repo not yet on Drive |
| `*` **differ** | Same name, different bytes. Somebody edited the Drive copy, or a publish was interrupted |
| **SHADOWED** | A file loose at the character's folder **root** with the same name as one we publish into a subfolder — see below |

The fix for all of them is `./tools/publish-to-drive --go`.

## RESOLVED 2026-08-04 — the first publish, and the drift it cleared

**Drive now matches the repository.** Verified by `--check`, which compares
every file byte for byte, and again through the Drive connector, which is a
different account path entirely.

| | |
|---|---|
| **Jasu** | 5 turnarounds, 3 artwork. No boards yet |
| **Shada** | 5 turnarounds, 16 artwork, 7 boards. Folder created by this run |

**What was wrong, and is no longer.** Jasu's folder held the **superseded v1
turnarounds** from 2026-08-01 — `turn-field-front.png` there was 2,207,890
bytes, byte-for-byte the v1 front archived at
`evolution/00-first-approved-2026-08-01.png`. The costume department was
looking at **ankle boots**, **a whistle at the belt**, and the superseded hair.

**They were loose at the folder root, not in a `turnarounds/` subfolder**, which
mattered more than it looked: publishing into subfolders would have left all
five one level up, still called `turn-field-front.png` — two files, same name,
different boots. `--purge-shadows` deleted exactly those five and nothing else.
`Jasu_outfit_build_guide.md` is untouched, as is the `.gitkeep`.

**The folder root is still not managed by publishing**, by design. Anything
dropped there by hand will be reported as shadowed if it collides with a
published name, and ignored otherwise.

## See also

- [`Cast-Data-Source.md`](Cast-Data-Source.md) — the traffic in the other
  direction, and why it does **not** happen: personal data stays in Drive and
  never enters this repository. Note that the Costume / Wardrobe folder holds
  cast measurements and a mood board belonging to other people. **Publishing
  never touches the parent folder**, only the per-character subfolders
- [`../03-characters/APPROVAL.md`](../03-characters/APPROVAL.md) — what sign-off means
