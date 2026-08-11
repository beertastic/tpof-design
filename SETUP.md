---
title: "Setting this repository up on a new machine"
asset_id: "SETUP"
updated: "2026-08-11"
status: "live — written for the 2026-08-11 machine move"
---

# Setting this repository up on a new machine

**A clone gets you the work. It does not get you the tools that move it.**
Everything in this file is the part that lives outside git: credentials, a
virtual environment, a cron job and a hook path. None of it is secret, and all
of it has to be done once per computer.

Written 2026-08-11, when the question was asked before the move rather than
after it, which is the only reason it is a checklist and not an archaeology.

## What a clone already gives you

All of it: `outfits.yaml` and the artwork, the prompts, the boards, the tools,
and the reasoning in `CHANGELOG.md` and `11-production-tracking/`. **The
decisions are written down on purpose** — a chat log does not survive a machine,
so anything that mattered went into the repository at the time.

## 1. Clone, and put the hook back

```bash
git clone git@github.com:beertastic/tpof-design.git
cd tpof-design
git config core.hooksPath tools/hooks
```

**The hook path is git config, not a file, so cloning does not carry it.**
Without it `REPO-STATE.md` stops being stamped and a connected model can no
longer tell whether it is reading current files.

Set it **relative**, exactly as above. It was absolute on the old machine
(`/home/tris/tpof-design/tools/hooks`), which works until the repository lives
anywhere else.

## 2. The virtual environment

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements-lock.txt
```

`.venv/` is gitignored. `requirements-lock.txt` is the exact freeze from the old
machine — **Python 3.12.3**, reportlab 5.0.0, pymupdf, CairoSVG, python-pptx,
screenplain.

**Run the tools through `./.venv/bin/python`, not bare `python3`.** The system
interpreter has no reportlab, and the failure is a traceback out of
`build-guide-pdf` that reads like a broken tool rather than a missing venv:

```bash
./.venv/bin/python tools/build-lists shada
./.venv/bin/python tools/build-guide-pdf shada
./.venv/bin/python tools/board-generator/generate.py shada --validate
```

## 3. rclone, for Google Drive

**Install from rclone's own script, not `apt`.** Ubuntu 24.04 ships v1.60.1-DEV
built in 2022, whose OAuth errors are close to unreadable.

```bash
sudo -v && curl https://rclone.org/install.sh | sudo bash
rclone version          # confirm it is not 1.60.x
rclone config
```

The remote must be named exactly **`tpof`**, storage `drive`, **scope 1 (full
access)**, and you must **sign in as `info@tristanpretty.com`** — not the Claude
account, and not whichever Google account the browser offers first. A personal
account authorises happily and then sees none of the production folders.

The full walkthrough, including the `client_id` mistake that cost an evening, is
in [`11-production-tracking/Drive-Publishing.md`](11-production-tracking/Drive-Publishing.md).

### Do the client_id here

rclone's shared Google application **stops working during 2026**. A new machine
means reauthorising anyway, so make your own client id in the same browser
session rather than twice. Steps: <https://rclone.org/drive/#making-your-own-client-id>.

**If you set up External rather than Internal, publish the app to production.**
In testing mode Google expires the refresh token after seven days — and since
the daily check runs from cron with nobody watching, the symptom would be a
notification a week later with no obvious cause.

Verify:

```bash
rclone lsd tpof: --drive-root-folder-id 1twIFwScVQhGSgHpTfmPieEMA5jjU5g8T
./tools/publish-to-drive --check          # read-only
```

## 4. The daily check

```bash
crontab -e
```

```
17 9 * * * /home/tris/tpof-design/tools/check-drive >/dev/null 2>&1
```

**Point it at the main checkout, not a worktree**, so it keeps working after a
branch is merged and deleted. Fix the path if the repository lives somewhere
else on this machine. It is read-only and never writes to Drive.

## 5. Claude Code's memory, if you use it

Four files at `~/.claude/projects/-home-tris-tpof-design/memory/` hold working
preferences — how prompts confirm their attachments, the TODO-table summary
format, that Tris plays Baylan, and that Drive is a different Google account.

**Copy that directory across by hand.** It is deliberately not in this
repository: the preferences are personal, and this repository is public.

## What is on disk but not in git, and how to get it back

| | |
|---|---|
| `03-characters/*/prompts/attach/` | Regenerate: `tools/prompt-splitter/short.py` |
| `03-characters/*/evolution/attachments/` | Regenerate: `tools/stage-evolution-attachments` — **run it after a fresh clone or the folders will not exist** |
| `03-characters/*/renders/` | Regenerate: `tools/board-generator/generate.py` |
| Scene `.pdf` / `.fdx` | Regenerate: `tools/script-convert/render.py` from the tracked `.fountain` |
| `10-assets/study/` | Copyrighted stills, never committed. Nothing was there at the move except its README |
| `TPOF-Complete.md` / `.pdf` | Regenerate: `tools/notebook-export/build.py` |

**The one thing with no generator is credentials**, which is why section 3 is the
longest here.

## Before you wipe the old machine

1. **`git push`.** Two commits sat unpushed when this file was written; `main`
   had no upstream at all, so `git status` said nothing about it. Check
   `git log --oneline origin/main..HEAD` and believe the answer.
2. **Check the worktrees.** `git worktree list` — anything under
   `.claude/worktrees/` is gitignored, so a branch that lives only there is
   invisible to a normal status. Both were fully merged at the move.
3. **Copy the memory directory** (section 5).
4. **Look at the ignored scene files.** `the-price-of-freedom-v10.pdf` and
   `.fdx` are gitignored. If they are renders, they rebuild. If the writer sent
   a v10 typeset draft, that copy is the only one.
