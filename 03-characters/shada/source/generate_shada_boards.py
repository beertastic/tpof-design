from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A2, landscape
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
import fitz
import shutil, zipfile, textwrap, json

ROOT = Path('/mnt/data/TPOF-Shada-Production-Package/03-characters/shada')
ROOT.mkdir(parents=True, exist_ok=True)
for d in ['renders','references','source']:
    (ROOT/d).mkdir(exist_ok=True)
SRC = Path('/mnt/data/a_photo_graphic_design_layout_showing_a_multi_page.png')
REF = ROOT/'references'/'Shada-Five-Board-Concept-Preview.png'
shutil.copy2(SRC, REF)

character_md = '''---
title: Shada
asset_id: CH-001
version: 1.0
status: locked
faction: Independent mercenary crew
role: Infiltrator, tracker, assassin, thief
last_updated: 2026-07-30
---

# Shada

The canonical long-form development document remains `Shada.md` in the main TPOF repository. This production-package copy records the approved visual brief used by the five art-department boards.

All visual work must apply the Production Design Bible before this character-specific direction.

## Art Department Brief

Shada is a compact, highly disciplined mercenary infiltrator whose visual and behavioural language combines a natural predator's patience with the practical habits of a survivor. She is human first, with restrained inherited serpentine traits visible through selected areas of exposed skin.

> Crew reputation: "Watch your back with her, but she'll always watch yours."

> Internal rule: "Only the hunted are prey."

> Visual principle: She should look like someone who belongs in a wet forest even when standing inside a starship.

## Story Function

Shada is the crew's assassin, thief, scout, tracker, and stealth specialist. She reads terrain, finds access routes, identifies signs of the quarry, infiltrates defended spaces, and strikes from advantage. She is an antagonist rather than a covert hero; her appeal comes from competence, dry humour, reciprocal loyalty, and the contrast between her profession and the ordered community life she might otherwise have lived.

## Design Intent

- Predator shaped by nature, not soldier shaped by an institution.
- Compact, athletic, agile build; small relative to the crew.
- Economical movement, patient stillness, alert observation.
- Mostly human appearance with subtle ancient serpentine ancestry.
- Fine scale patterning on face, neck, collarbone, shoulders, forearms, and hands.
- Exposed skin is functional: mobility, reduced weight, heat management, sensory function, and visibility of heritage.
- Light scavenged armour protects vital areas only.
- Mismatched equipment is made cohesive through careful maintenance and habitual placement.
- Few scars, suggesting avoidance and precision rather than invulnerability.

## Costume and Armour

- Integrated scale-textured undersuit.
- Layered technical fabrics, weathered leather, flexible armour mesh, and small vital-area plates.
- Practical harnesses, belts, pouches, repair patches, and climbing boots.
- Functional asymmetry; nothing rattles, snags, or hangs without purpose.
- Muted earth palette: charcoal, ash grey, weathered black, faded olive, dark brown, natural bone.
- No polished surfaces or bright colour blocking.

## Weapons and Equipment

Shada always carries a compact, modified blaster and an old, well-maintained combat knife. The knife never leaves her side and is a survival tool first: food preparation, cutting material, repairs, markers, and close combat. Supporting gear may include rope, lock picks, climbing hardware, repair tools, field tools, and a small utility pouch. No unnecessary datapads or decorative technology.

## Performance

- Watches and listens before acting.
- Scans exits and environmental changes.
- Becomes very still when assessing danger.
- Moves with minimal wasted motion.
- Avoids heroic or military posing.
- Can soften around the crew during meals, drinks, and sabacc.
- May use scent subtly when gathering information.

## Production Boards

1. `Production-Board.pdf` - overall identity and hero sheet.
2. `Costume-Board.pdf` - construction, layers, materials, and exposed-skin purpose.
3. `Weapons-Board.pdf` - knife, compact blaster, carry systems, and utility kit.
4. `Performance-Board.pdf` - posture, movement, expression, and actor direction.
5. `Materials-Board.pdf` - approved palette, surfaces, wear, environment, and lighting.

## Revision History

| Version | Status | Change |
|---|---|---|
| 1.0 | Locked | Production-package brief aligned to the Character Lock and five-board standard. |
'''
(ROOT/'Character.md').write_text(character_md, encoding='utf-8')

lock_md = '''---
title: Shada Character Lock
asset_id: CH-001
version: 1.0
status: locked
last_updated: 2026-07-30
---

# Character Lock

These traits are non-negotiable unless a formal design revision is approved.

## Visual Identity

- Female; fundamentally human.
- Compact, athletic, agile build.
- Subtle ancient serpentine ancestry; never a full reptilian creature.
- Fine scales visible on selected exposed skin.
- Scale distribution: portions of face, neck, collarbone, shoulders, forearms, and hands.
- Eyes retain a subtle reptilian quality while remaining expressive and human.
- Few scars.

## Costume

- Light, fitted, scavenged armour.
- Integrated scale-textured undersuit.
- Vital-area protection only.
- Functional exposed shoulders, upper arms, forearms, and selected upper-back areas.
- Layered technical fabrics, practical belts and harnesses, repair patches, and forest-capable boots.
- Every item is repaired, maintained, and purpose-driven.

## Exposed Skin

Exposed skin exists for freedom of movement, reduced weight, heat management, sensory function, and visibility of heritage. It is never decorative or sexualised. The read is practical first.

## Weapons

Always present:

- Compact modified blaster.
- Old, well-maintained combat knife.

May carry rope, lock picks, climbing gear, field-repair tools, and a small utility pouch. No high-tech gadgets without a clear mission function.

## Behaviour

- Dangerous while standing still.
- Observes before acting.
- Economical, controlled, quiet, patient movement.
- Preferred actions: watching, listening, crouching, tracking, cleaning equipment, scanning surroundings.
- No superhero poses, exaggerated action poses, or smiles for camera.

## Colour Language

Muted earth tones: charcoal, ash grey, weathered black, faded olive, dark brown, natural bone. No bright colours or polished metals.

## Design Drift Prevention

Reject any design that:

- resembles a Caribbean pirate, medieval warrior, generic fantasy rogue, or modern tactical operator;
- hides the serpentine ancestry or covers all exposed skin;
- uses heavy, ornamental, symmetrical, or decorative armour;
- adds oversized weapons, unnecessary datapads, or technology for visual noise;
- glamourises or sexualises the costume;
- removes the sense that she belongs in a wet forest;
- makes her posture heroic rather than observant and predatory.

## Art Direction Test

In three seconds, the audience should believe that:

- she belongs in this forest;
- she notices everything;
- she wastes no movement;
- she could disappear at any moment.

**Core design statement:** She survives because she notices everything.
'''
(ROOT/'Character-Lock.md').write_text(lock_md, encoding='utf-8')

# crop artwork panels from the approved five-board preview
im = Image.open(SRC).convert('RGB')
crops = {
    'production': (170, 35, 820, 545),
    'costume': (835, 25, 1525, 585),
    'weapons': (0, 600, 530, 955),
    'performance': (530, 600, 1000, 955),
    'materials': (995, 600, 1535, 955),
}
for k, box in crops.items():
    crop = im.crop(box)
    crop = ImageEnhance.Contrast(crop).enhance(1.12)
    crop = ImageEnhance.Brightness(crop).enhance(1.05)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))
    crop.save(ROOT/'source'/f'{k}-artwork.png', quality=95)

PAGE_W, PAGE_H = landscape(A2)
BG = HexColor('#F2EFE7')
INK = HexColor('#161817')
MUTED = HexColor('#5D625C')
ACCENT = HexColor('#536B56')
RUST = HexColor('#7A4A2B')
PANEL = HexColor('#E5E0D5')
LINE = HexColor('#A9A397')

boards = {
'Production-Board.pdf': {
 'title':'CHARACTER PRODUCTION BOARD', 'num':'01', 'art':'production-artwork.png',
 'summary':'A compact mercenary infiltrator: human first, with restrained serpentine ancestry. Predator rather than soldier; she survives through observation, concealment, timing, and control of distance.',
 'sections':[
  ('FIRST IMPRESSION',['Belongs in the wet forest','Notices everything','Wastes no movement','Could disappear at any moment']),
  ('CHARACTER LOCK',['Subtle scales and reptilian eyes','Functional exposed skin','Compact blaster and knife always present','Light scavenged vital-area armour','Quiet, economical, dangerous while still']),
  ('STORY FUNCTION',['Scout, tracker, thief, assassin','Reads terrain and access routes','Strikes from advantage','Integral member of the mercenary family'])],
 'footer':'Visual principle: she belongs in a forest even inside a starship.'},
'Costume-Board.pdf': {
 'title':'COSTUME CONSTRUCTION BOARD', 'num':'02', 'art':'costume-artwork.png',
 'summary':'A buildable costume assembled from flexible armour mesh, technical cloth, reinforced synth-leather, worn hardware, and repaired field gear. Exposure is functional, never ornamental.',
 'sections':[
  ('LAYER SYSTEM',['Scale-textured flexible undersuit','Breathable base layer','Crossed chest harness and light plates','Tattered outer panels to break silhouette','Lightweight boots and quiet wraps']),
  ('EXPOSED SKIN PURPOSE',['Freedom of movement','Weight and heat reduction','Sensory function','Makes inherited scales legible','Practical first; never sexualised']),
  ('CONSTRUCTION RULES',['Believable seams and fasteners','No floating armour pieces','Functional asymmetry','Nothing rattles or snags','Visible repairs and field replacement'])],
 'footer':'Nothing new. Everything earned.'},
'Weapons-Board.pdf': {
 'title':'WEAPONS & EQUIPMENT BOARD', 'num':'03', 'art':'weapons-artwork.png',
 'summary':'Shada carries only proven equipment. Her hero knife is personal, old, repeatedly sharpened, and maintained daily. Her blaster is compact, modified, reliable, and immediately accessible.',
 'sections':[
  ('COMBAT KNIFE',['Survival tool first; weapon second','Old blade with repeated sharpening','Wrapped, repaired grip','Secure silent sheath','Never leaves her side']),
  ('COMPACT BLASTER',['Mechanically believable','Modified from long use','Easy to conceal and draw','Scratched finish and replacement parts','No oversized silhouette']),
  ('UTILITY KIT',['Rope and climbing hardware','Lock picks and field tools','Small repair kit','Habitual belt placement','No datapad or unnecessary gadgets'])],
 'footer':'Maintained daily. Trusted always.'},
'Performance-Board.pdf': {
 'title':'PERFORMANCE & MOVEMENT BOARD', 'num':'04', 'art':'performance-artwork.png',
 'summary':'The actor should inhabit Shada through restraint. She enters a space by reading it, not owning it. Stillness is active; every glance checks distance, scent, vibration, exits, and changes in the environment.',
 'sections':[
  ('MOVEMENT PRINCIPLES',['Economical and controlled','Low profile and quiet footwork','Patient before explosive action','Predatory, never theatrical','Uses terrain and shadow']),
  ('FACIAL LANGUAGE',['Neutral alertness','Suspicion without panic','Focused assessment','Protective boundary around the helpless','Cold, lethal calm toward the hunted']),
  ('ACTOR NOTES',['Breathe low and quiet','Scan before speaking','Shift weight onto the balls of the feet','Avoid military posture','Allow warmth only around the crew'])],
 'footer':"She doesn't enter a space. She studies it."},
'Materials-Board.pdf': {
 'title':'MATERIALS & COLOUR BOARD', 'num':'05', 'art':'materials-artwork.png',
 'summary':'The palette belongs to rain, bark, mud, smoke, patina, and repaired workwear. Dark clothing must separate from the environment through value contrast, rim light, wet highlights, and material variation.',
 'sections':[
  ('APPROVED PALETTE',['Charcoal #2B2A26','Ash brown #3A352F','Dust brown #544E42','Faded olive #4F563F','Weathered black #2E2F33','Natural bone #BDAF95']),
  ('SURFACE LANGUAGE',['Flexible scale mesh','Worn reinforced leather','Coarse technical fabric','Weathered matte metal','Rope and natural fibre','Stitching, patches, mud, patina']),
  ('LIGHT & CONTRAST',['Lift forest midtones behind silhouette','Keep clothing dark but not crushed','Use wet edge highlights','Warm firelight only when motivated','No dramatic coloured light without story purpose'])],
 'footer':'Muted. Natural. Weathered. Functional. Non-reflective.'},
}

def wrap(c, text, x, y, width, font='Helvetica', size=13, leading=17, color=INK, max_lines=None):
    c.setFont(font,size); c.setFillColor(color)
    words=text.split(); lines=[]; line=''
    for w in words:
        test=(line+' '+w).strip()
        if stringWidth(test,font,size) <= width:
            line=test
        else:
            if line: lines.append(line)
            line=w
    if line: lines.append(line)
    if max_lines: lines=lines[:max_lines]
    for ln in lines:
        c.drawString(x,y,ln); y-=leading
    return y

def fit_image(c, path, x,y,w,h):
    pic=Image.open(path); iw,ih=pic.size
    scale=max(w/iw,h/ih)
    sw,sh=iw*scale,ih*scale
    # crop to fit using ImageReader after a pre-crop
    left=max(0,(sw-w)/2/scale); top=max(0,(sh-h)/2/scale)
    right=iw-left; bottom=ih-top
    cropped=pic.crop((int(left),int(top),int(right),int(bottom)))
    c.drawImage(ImageReader(cropped),x,y,w,h,mask='auto')

def draw_board(out_path, spec):
    c=canvas.Canvas(str(out_path), pagesize=(PAGE_W,PAGE_H), pageCompression=1)
    c.setFillColor(BG); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
    m=40
    # header
    c.setFillColor(INK); c.rect(0,PAGE_H-108,PAGE_W,108,fill=1,stroke=0)
    c.setFillColor(white); c.setFont('Helvetica-Bold',34); c.drawString(m,PAGE_H-51,'SHADA')
    c.setFont('Helvetica-Bold',21); c.drawString(250,PAGE_H-48,spec['title'])
    c.setFont('Helvetica',10); c.drawString(250,PAGE_H-73,'THE PRICE OF FREEDOM  |  ASSET CH-001  |  VERSION 1.0  |  STATUS: REVIEW  |  2026-07-30')
    c.setFillColor(ACCENT); c.setFont('Helvetica-Bold',13); c.drawRightString(PAGE_W-m,PAGE_H-52,f"BOARD {spec['num']} / 05")
    # main image card
    img_x=m; img_y=290; img_w=PAGE_W*0.62; img_h=PAGE_H-430
    c.setFillColor(white); c.roundRect(img_x-6,img_y-6,img_w+12,img_h+12,5,fill=1,stroke=0)
    fit_image(c, ROOT/'source'/spec['art'],img_x,img_y,img_w,img_h)
    c.setStrokeColor(LINE); c.rect(img_x,img_y,img_w,img_h,fill=0,stroke=1)
    # right text column
    tx=img_x+img_w+30; tw=PAGE_W-tx-m; top=PAGE_H-145
    c.setFillColor(INK); c.setFont('Helvetica-Bold',17); c.drawString(tx,top,'ART DEPARTMENT BRIEF')
    top-=28; top=wrap(c,spec['summary'],tx,top,tw,'Helvetica',13,18,MUTED)
    top-=15
    for heading, bullets in spec['sections']:
        c.setFillColor(ACCENT); c.setFont('Helvetica-Bold',14); c.drawString(tx,top,heading); top-=20
        for b in bullets:
            c.setFillColor(INK); c.setFont('Helvetica',11.5)
            c.drawString(tx,top,u'•')
            top=wrap(c,b,tx+14,top,tw-14,'Helvetica',11.5,15,INK)
            top-=3
        top-=12
    # bottom band
    c.setFillColor(PANEL); c.rect(0,0,PAGE_W,250,fill=1,stroke=0)
    c.setStrokeColor(LINE); c.line(0,250,PAGE_W,250)
    # metadata and lock
    bx=m; by=44
    c.setFillColor(INK); c.setFont('Helvetica-Bold',15); c.drawString(bx,213,'PRODUCTION NOTES')
    notes=['Production Design Bible governs all choices.','Generated artwork is visual reference; PDF typography is canonical.','Review against Character-Lock.md before approval.','Print size: A2 landscape, 300 DPI equivalent.']
    yy=188
    for n in notes:
        c.setFont('Helvetica',11); c.drawString(bx,yy,u'• '+n); yy-=19
    c.setFillColor(ACCENT); c.setFont('Helvetica-BoldOblique',16); c.drawString(bx,62,spec['footer'])
    # signoff
    sx=PAGE_W-520
    c.setFillColor(INK); c.setFont('Helvetica-Bold',13); c.drawString(sx,213,'DEPARTMENT SIGN-OFF')
    c.setFont('Helvetica',11)
    for i,label in enumerate(['Costume','Weapons','Hair','Makeup / SFX','Production Design']):
        x=sx+(i%3)*165; y=184-(i//3)*32
        c.rect(x,y-3,12,12,fill=0,stroke=1); c.drawString(x+20,y,label)
    c.setFont('Helvetica',10); c.drawRightString(PAGE_W-m,30,'ART DEPARTMENT SHEET - REVIEW COPY')
    c.showPage(); c.save()

for name,spec in boards.items():
    draw_board(ROOT/name,spec)

# render PDFs to exact A2 300dpi PNGs
for pdf in [ROOT/n for n in boards]:
    doc=fitz.open(pdf)
    page=doc[0]
    pix=page.get_pixmap(matrix=fitz.Matrix(300/72,300/72), alpha=False)
    # A2 landscape can round to 7017x4961; normalize exactly 7016x4961
    tmp=ROOT/'renders'/(pdf.stem+'-A2-300dpi.tmp.png')
    pix.save(tmp)
    img=Image.open(tmp).convert('RGB').resize((7016,4961),Image.Resampling.LANCZOS)
    out=ROOT/'renders'/(pdf.stem+'-A2-300dpi.png')
    img.save(out,optimize=True)
    tmp.unlink()

# source docs
source_readme='''# Shada Production Board Source\n\n`generate_shada_boards.py` rebuilds the five A2 landscape PDFs and their 7016 x 4961 PNG exports.\n\nThe approved concept image is stored under `../references/`. Cropped artwork panels under this folder are working derivatives used by the layout script. All headings, descriptions, callouts, metadata, and production notes in the PDFs are real vector typography.\n\n## Requirements\n\n- Python 3\n- Pillow\n- ReportLab\n- PyMuPDF\n\n## Rebuild\n\nRun the script from the repository root or edit its output path for your local checkout.\n\n```bash\npython 03-characters/shada/source/generate_shada_boards.py\n```\n\nThe current script was packaged for review and may need its `ROOT` and source-image paths adjusted after copying into the repository.\n'''
(ROOT/'source'/'README.md').write_text(source_readme,encoding='utf-8')
# Copy this generator itself as editable source
shutil.copy2('/mnt/data/create_shada_package.py', ROOT/'source'/'generate_shada_boards.py')

package_readme='''# Shada Production Package\n\nThis folder is a Git-ready review package for the TPOF character-board standard.\n\n- The five PDFs are A2 landscape with crisp vector typography.\n- `renders/` contains exact 7016 x 4961 PNG exports for print review and raster workflows.\n- `references/` preserves the approved five-board concept preview.\n- `source/` contains the rebuild script and working artwork crops.\n\nSuggested commit:\n\n```text\ndesign(shada): add five-board A2 production package\n```\n'''
(ROOT/'README.md').write_text(package_readme,encoding='utf-8')

# manifest
manifest=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file():
        manifest.append(str(p.relative_to(ROOT.parent.parent.parent)))
(ROOT/'source'/'MANIFEST.txt').write_text('\n'.join(manifest)+'\n',encoding='utf-8')

# zip
zip_path=Path('/mnt/data/TPOF-Shada-Production-Package.zip')
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    base=Path('/mnt/data/TPOF-Shada-Production-Package')
    for p in base.rglob('*'):
        if p.is_file(): z.write(p,p.relative_to(base))
print(zip_path)
for p in sorted(ROOT.glob('*.pdf')):
    print(p.name,p.stat().st_size)
for p in sorted((ROOT/'renders').glob('*.png')):
    print(p.name,Image.open(p).size,p.stat().st_size)
