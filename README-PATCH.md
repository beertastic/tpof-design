# TPOF Board Generator Patch

This patch intentionally includes **only Shada** as the first test character.
It does not create, restore, or modify any other character folders.

Copy the contents into the root of `tpof-design`, then run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tools/board-generator/requirements.txt
python tools/board-generator/generate.py 03-characters/shada
```

The included outputs were generated with the same command and can be reviewed
before committing.

Suggested commit:

```bash
git add tools/board-generator 03-characters/shada
git commit -m "tools(design): add reusable board generator and Shada test"
git push
```
