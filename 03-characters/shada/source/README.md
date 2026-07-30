# Shada Production Board Source

`generate_shada_boards.py` rebuilds the five A2 landscape PDFs and their 7016 x 4961 PNG exports.

The approved concept image is stored under `../references/`. Cropped artwork panels under this folder are working derivatives used by the layout script. All headings, descriptions, callouts, metadata, and production notes in the PDFs are real vector typography.

## Requirements

- Python 3
- Pillow
- ReportLab
- PyMuPDF

## Rebuild

Run the script from the repository root or edit its output path for your local checkout.

```bash
python 03-characters/shada/source/generate_shada_boards.py
```

The current script was packaged for review and may need its `ROOT` and source-image paths adjusted after copying into the repository.
