# Shada Production Package v3

This rebuild removes blurred AI-generated labels from the board artwork.

- All production text is editable PowerPoint text and vector PDF typography.
- Artwork is placed without cropping.
- The five clean review PDFs are A2 landscape.
- Matching PNG renders are exactly 7016 x 4961 pixels at 300 DPI.
- The package contains only Shada and does not restore deleted characters.

Editable master: `source/Shada-Production-Boards.pptx`

Suggested commit:

```bash
git add 03-characters/shada
git commit -m "design(shada): rebuild clean editable A2 production boards"
git push
```
