# Akk Dog — Reference Plates

Renders from the built and rigged asset. These are the ground truth for every
generated image containing the akk dog.

## What to put here

Render these from the rig. Neutral grey background, even lighting, no dramatic
key, no depth of field, no motion blur. These are references, not beauty shots.

| Filename | What | Why it matters |
|---|---|---|
| `turnaround-side.png` | Full side profile, perfectly orthographic | The primary shape reference |
| `turnaround-front.png` | Head-on, orthographic | Chest width and stance, which side views hide |
| `turnaround-three-quarter.png` | 3/4 front, the most useful working angle | How it reads in most shots |
| `turnaround-rear.png` | Rear, orthographic | Hindquarters and tail |
| `head-detail.png` | Head close, 3/4 | Jaw, eyes, ears — where generators drift most |
| `hide-detail.png` | Close crop of hide texture | Plating, scale or hair at real scale |
| `scale-with-figure.png` | **Side view beside a 1.8 m human figure** | The single most important plate |
| `pose-standing.png` | Neutral standing pose | Default posture |
| `pose-seated.png` | Seated or lying, as in Scene 9 | The pose it is actually in on screen |

Add `-v2`, `-v3` etc. rather than overwriting, if a version needs to be kept for
comparison. Otherwise replace in place — the repository keeps one current copy.

## Why the scale plate matters most

Image generators get creature scale wrong more reliably than they get anything
else wrong. A description like "large quadruped" produces anything from
knee-height to elephant-sized between one image and the next.

A single render of the animal beside a 1.8 m human, with the shoulder height
written into `Creature.md` and repeated in every prompt, fixes it. Do this plate
first.

## Getting these to an image generator

A model reading this repository can read the *text*. Whether it can see these
*images* depends on how it is connected — a repository connector may only expose
file contents as text, in which case the PNGs are unreadable to it.

Attach the plates directly to the conversation alongside the prompt. Do not
assume repository access means the model has seen them. If the generated animal
comes back wrong, that is the first thing to check.

## Keep these small

Reference plates are committed to the repository, unlike `renders/` elsewhere.
Export at a sensible working size — 2048 px on the long edge is plenty. A folder
of 20 MB turntable frames will undo the repository slimming.
