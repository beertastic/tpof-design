# TPOF Top-Level Board Generator Patch

Extract this archive into the root of `tpof-design`.

The patch contains:

- `tools/board-generator/` - the reusable generator
- `03-characters/shada/board-data.yaml` - Shada's publishing configuration

It does not contain or recreate any other character directories.

After extraction:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tools/board-generator/requirements.txt
python tools/board-generator/generate.py shada --validate
python tools/board-generator/generate.py shada
```
