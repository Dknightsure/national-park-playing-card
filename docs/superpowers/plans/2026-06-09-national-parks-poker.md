# American National Parks Playing Cards Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a print-ready and digital-ready American National Parks playing-card deck system with 52 park cards, 2 animal Jokers, a symmetrical card back, tuck box artwork direction, and reviewable asset packages.

**Architecture:** Treat this as a staged design-production pipeline. First create a shared deck kit and sample cards, then lock the card template, then batch-produce the remaining assets against the same rules and quality gates.

**Tech Stack:** Markdown specs and tracking files, raster/vector design tools such as Figma/Illustrator/Photoshop/Affinity, optional AI image generation for concept art, 300 DPI CMYK print exports, PNG/PDF digital exports.

---

## File Structure

Create and maintain this working structure under the current project root:

- `work/national-parks-poker/brief/`
  Product brief, production checklist, and reference notes.
- `work/national-parks-poker/references/`
  Official or licensed visual references collected per park. Do not place unlicensed final artwork here as customer-facing deliverables.
- `work/national-parks-poker/source/`
  Editable source files for card template, card faces, card back, and tuck box.
- `work/national-parks-poker/review/`
  Low-resolution review exports and contact sheets.
- `outputs/national-parks-poker/`
  Final user-facing digital and print deliverables.

Use this naming convention:

- Standard card face: `<rank><suit>-<park-slug>`, for example `AS-grand-canyon`.
- Jokers: `joker-bald-eagle`, `joker-bear`.
- Back: `card-back`.
- Tuck box: `tuck-box`.

Suit letters:

- `S` = Spades
- `H` = Hearts
- `C` = Clubs
- `D` = Diamonds

## Task 1: Create Production Workspace And Tracking Files

**Files:**
- Create: `work/national-parks-poker/brief/deck-production-checklist.md`
- Create: `work/national-parks-poker/brief/card-list.csv`
- Create: `outputs/national-parks-poker/README.md`

- [ ] **Step 1: Create the folder structure**

Run:

```bash
mkdir -p work/national-parks-poker/{brief,references,source,review}
mkdir -p outputs/national-parks-poker
```

Expected: all five project folders exist.

- [ ] **Step 2: Create the production checklist**

Create `work/national-parks-poker/brief/deck-production-checklist.md` with:

```markdown
# National Parks Playing Cards Production Checklist

## Locked Product Decisions

- 52 standard cards plus 2 Jokers.
- Final customer-facing text is English only.
- Existing park-to-card mapping is preserved.
- Suits are poker identifiers only and do not control each park's visual concept.
- Visual style is vintage American national parks travel poster.
- Jokers are Bald Eagle and Bear.

## Global Acceptance Checks

- Every standard card has top-left and bottom-right rank/suit indexes.
- Every standard card uses the assigned park name in uppercase English.
- No final customer-facing card face includes Chinese text.
- `NATIONAL PARK` is used consistently across standard cards, or removed consistently deck-wide after proofing.
- Long names fit without crowding.
- Card back is symmetrical and cannot identify orientation.
- Print files include bleed and safe margins.
- Digital exports use consistent filenames.
- Visual motifs are verified against official NPS or licensed references before final art.
```

- [ ] **Step 3: Create the full card list**

Create `work/national-parks-poker/brief/card-list.csv` with:

```csv
filename,card,park,asset_type,status
AS-grand-canyon,A Spades,Grand Canyon,standard,planned
KS-zion,K Spades,Zion,standard,planned
QS-bryce-canyon,Q Spades,Bryce Canyon,standard,planned
JS-arches,J Spades,Arches,standard,planned
10S-canyonlands,10 Spades,Canyonlands,standard,planned
9S-capitol-reef,9 Spades,Capitol Reef,standard,planned
8S-badlands,8 Spades,Badlands,standard,planned
7S-black-canyon-of-the-gunnison,7 Spades,Black Canyon of the Gunnison,standard,planned
6S-guadalupe-mountains,6 Spades,Guadalupe Mountains,standard,planned
5S-mesa-verde,5 Spades,Mesa Verde,standard,planned
4S-petrified-forest,4 Spades,Petrified Forest,standard,planned
3S-carlsbad-caverns,3 Spades,Carlsbad Caverns,standard,planned
2S-mammoth-cave,2 Spades,Mammoth Cave,standard,planned
AH-yosemite,A Hearts,Yosemite,standard,planned
KH-grand-teton,K Hearts,Grand Teton,standard,planned
QH-glacier,Q Hearts,Glacier,standard,planned
JH-denali,J Hearts,Denali,standard,planned
10H-rocky-mountain,10 Hearts,Rocky Mountain,standard,planned
9H-mount-rainier,9 Hearts,Mount Rainier,standard,planned
8H-sequoia,8 Hearts,Sequoia,standard,planned
7H-kings-canyon,7 Hearts,Kings Canyon,standard,planned
6H-glacier-bay,6 Hearts,Glacier Bay,standard,planned
5H-kenai-fjords,5 Hearts,Kenai Fjords,standard,planned
4H-lassen-volcanic,4 Hearts,Lassen Volcanic,standard,planned
3H-great-basin,3 Hearts,Great Basin,standard,planned
2H-pinnacles,2 Hearts,Pinnacles,standard,planned
AC-yellowstone,A Clubs,Yellowstone,standard,planned
KC-great-smoky-mountains,K Clubs,Great Smoky Mountains,standard,planned
QC-acadia,Q Clubs,Acadia,standard,planned
JC-olympic,J Clubs,Olympic,standard,planned
10C-shenandoah,10 Clubs,Shenandoah,standard,planned
9C-cuyahoga-valley,9 Clubs,Cuyahoga Valley,standard,planned
8C-new-river-gorge,8 Clubs,New River Gorge,standard,planned
7C-redwood,7 Clubs,Redwood,standard,planned
6C-congaree,6 Clubs,Congaree,standard,planned
5C-theodore-roosevelt,5 Clubs,Theodore Roosevelt,standard,planned
4C-indiana-dunes,4 Clubs,Indiana Dunes,standard,planned
3C-voyageurs,3 Clubs,Voyageurs,standard,planned
2C-wind-cave,2 Clubs,Wind Cave,standard,planned
AD-joshua-tree,A Diamonds,Joshua Tree,standard,planned
KD-death-valley,K Diamonds,Death Valley,standard,planned
QD-hawaii-volcanoes,Q Diamonds,Hawai'i Volcanoes,standard,planned
JD-everglades,J Diamonds,Everglades,standard,planned
10D-saguaro,10 Diamonds,Saguaro,standard,planned
9D-haleakala,9 Diamonds,Haleakala,standard,planned
8D-white-sands,8 Diamonds,White Sands,standard,planned
7D-big-bend,7 Diamonds,Big Bend,standard,planned
6D-great-sand-dunes,6 Diamonds,Great Sand Dunes,standard,planned
5D-crater-lake,5 Diamonds,Crater Lake,standard,planned
4D-biscayne,4 Diamonds,Biscayne,standard,planned
3D-virgin-islands,3 Diamonds,Virgin Islands,standard,planned
2D-channel-islands,2 Diamonds,Channel Islands,standard,planned
joker-bald-eagle,Joker,Bald Eagle,joker,planned
joker-bear,Joker,Bear,joker,planned
card-back,Back,National Parks,back,planned
tuck-box,Tuck Box,National Parks Playing Cards,packaging,planned
```

- [ ] **Step 4: Create output README**

Create `outputs/national-parks-poker/README.md` with:

```markdown
# National Parks Playing Cards Outputs

This folder is reserved for final user-facing exports.

Expected final contents:

- `digital/cards/`: 54 individual card-front PNG exports plus card back.
- `digital/contact-sheet.pdf`: full deck visual review sheet.
- `digital/hero-mockups/`: marketing preview images.
- `print/cards/`: print-ready card front and back files.
- `print/tuck-box/`: print-ready tuck box artwork.
- `print/production-notes.md`: printer-facing production notes.
```

- [ ] **Step 5: Verify file count**

Run:

```bash
find work/national-parks-poker outputs/national-parks-poker -maxdepth 3 -type d | sort
wc -l work/national-parks-poker/brief/card-list.csv
```

Expected: project folders are listed and `card-list.csv` reports 57 lines including the header.

## Task 2: Lock The Shared Card Template

**Files:**
- Create: `work/national-parks-poker/brief/card-template-spec.md`
- Create: `work/national-parks-poker/source/card-template-source-notes.md`

- [ ] **Step 1: Define the physical card geometry**

Create `work/national-parks-poker/brief/card-template-spec.md` with:

```markdown
# Card Template Specification

## Size

- Trim size: 2.5 x 3.5 in.
- Bleed size: 2.75 x 3.75 in.
- Bleed: 0.125 in on all sides.
- Minimum safe area: 0.125 in inside trim.
- Preferred index/title safe area: 0.18 in inside trim.
- Raster export: 825 x 1125 px at 300 DPI including bleed.
- Trim preview export: 750 x 1050 px at 300 DPI.

## Required Face Elements

- Top-left index: rank plus suit.
- Bottom-right index: rank plus suit rotated 180 degrees.
- Park title in uppercase English.
- `NATIONAL PARK` series line used consistently unless removed deck-wide after proofing.
- Central vintage poster illustration.
- Border system that does not interfere with safe area.

## Index Rules

- Spades and clubs use near-black ink.
- Hearts and diamonds use deep vintage red.
- Indexes must remain readable when a card is viewed at physical size.
- Long park titles use two-line title lockups instead of excessive shrinking.

## Export Rules

- Print files: CMYK, 300 DPI, bleed included.
- Digital review files: RGB PNG or PDF.
- Source files: layered and editable.
```

- [ ] **Step 2: Define source-file expectations**

Create `work/national-parks-poker/source/card-template-source-notes.md` with:

```markdown
# Card Template Source Notes

Use one shared template for all standard card faces.

Required layers or groups:

- Bleed boundary.
- Trim boundary.
- Safe-area guides.
- Top-left index.
- Bottom-right rotated index.
- Park title.
- Series line.
- Illustration area.
- Border and texture overlays.

Keep text editable until final export. Keep rank, suit, and park-name fields easy to update per card.
```

- [ ] **Step 3: Review the template spec against the design spec**

Run:

```bash
rg -n "Trim size|Bleed|NATIONAL PARK|Spades and clubs|Hearts and diamonds" work/national-parks-poker/brief/card-template-spec.md
```

Expected: all five template requirements are present.

## Task 3: Produce The Six-Asset Pilot Set

**Files:**
- Create or update editable design source files in `work/national-parks-poker/source/`
- Create review exports in `work/national-parks-poker/review/pilot-set/`

- [ ] **Step 1: Prepare the pilot-set folder**

Run:

```bash
mkdir -p work/national-parks-poker/review/pilot-set
```

Expected: `work/national-parks-poker/review/pilot-set` exists.

- [ ] **Step 2: Create these six pilot assets**

Create editable source artwork and review PNG/PDF exports for:

```text
AS-grand-canyon
AH-yosemite
AC-yellowstone
AD-joshua-tree
joker-bald-eagle
card-back
```

Design requirements:

- `AS-grand-canyon`: layered canyon cliffs, Colorado River depth, sunrise or sunset light.
- `AH-yosemite`: Half Dome, El Capitan, and waterfall valley composition.
- `AC-yellowstone`: Old Faithful geyser, thermal basin, optional bison accent if it does not clutter the scene.
- `AD-joshua-tree`: Joshua trees, boulders, desert sunset.
- `joker-bald-eagle`: bald eagle as an iconic national symbol, using the same poster system.
- `card-back`: symmetrical `NATIONAL PARKS` badge, mirrored landscape elements, no directional marking.

- [ ] **Step 3: Check pilot card face consistency**

For each pilot standard card, verify:

```text
[ ] Top-left index exists.
[ ] Bottom-right rotated index exists.
[ ] Correct rank and suit are shown.
[ ] Park name is uppercase English.
[ ] No Chinese appears.
[ ] `NATIONAL PARK` treatment is consistent.
[ ] Main visual is specific to that park.
[ ] Suit does not force the illustration palette.
```

- [ ] **Step 4: Check pilot physical legibility**

Export a physical-size PDF contact sheet with the six assets. Print it or view it at actual size.

Expected:

```text
[ ] Rank/suit indexes are readable at poker-card size.
[ ] Longest visible title in the pilot does not crowd the border.
[ ] Card back looks symmetrical when rotated 180 degrees.
[ ] Texture does not blur title or indexes.
```

- [ ] **Step 5: Record pilot approval notes**

Create `work/national-parks-poker/review/pilot-set/pilot-review-notes.md` with:

```markdown
# Pilot Set Review Notes

## Assets Reviewed

- AS-grand-canyon
- AH-yosemite
- AC-yellowstone
- AD-joshua-tree
- joker-bald-eagle
- card-back

## Decisions

- Template approved: yes
- Index size approved: yes
- Title style approved: yes
- Texture level approved: yes
- Card back direction approved: yes
- `NATIONAL PARK` series line: keep

## Required Changes Before Batch Production

- None
```

If any item is not approved, replace `yes` or `None` with the exact required change before moving to Task 4.

## Task 4: Produce Remaining Standard Card Faces

**Files:**
- Update: `work/national-parks-poker/brief/card-list.csv`
- Create source and review exports for all remaining standard cards.

- [ ] **Step 1: Produce Spades batch**

Create source and review exports for:

```text
KS-zion
QS-bryce-canyon
JS-arches
10S-canyonlands
9S-capitol-reef
8S-badlands
7S-black-canyon-of-the-gunnison
6S-guadalupe-mountains
5S-mesa-verde
4S-petrified-forest
3S-carlsbad-caverns
2S-mammoth-cave
```

Expected: every file follows the shared template and its park-specific motif from the design spec.

- [ ] **Step 2: Produce Hearts batch**

Create source and review exports for:

```text
KH-grand-teton
QH-glacier
JH-denali
10H-rocky-mountain
9H-mount-rainier
8H-sequoia
7H-kings-canyon
6H-glacier-bay
5H-kenai-fjords
4H-lassen-volcanic
3H-great-basin
2H-pinnacles
```

Expected: every file follows the shared template and its park-specific motif from the design spec.

- [ ] **Step 3: Produce Clubs batch**

Create source and review exports for:

```text
KC-great-smoky-mountains
QC-acadia
JC-olympic
10C-shenandoah
9C-cuyahoga-valley
8C-new-river-gorge
7C-redwood
6C-congaree
5C-theodore-roosevelt
4C-indiana-dunes
3C-voyageurs
2C-wind-cave
```

Expected: every file follows the shared template and its park-specific motif from the design spec.

- [ ] **Step 4: Produce Diamonds batch**

Create source and review exports for:

```text
KD-death-valley
QD-hawaii-volcanoes
JD-everglades
10D-saguaro
9D-haleakala
8D-white-sands
7D-big-bend
6D-great-sand-dunes
5D-crater-lake
4D-biscayne
3D-virgin-islands
2D-channel-islands
```

Expected: every file follows the shared template and its park-specific motif from the design spec.

- [ ] **Step 5: Update production status**

Update `work/national-parks-poker/brief/card-list.csv` so every completed standard card has `status` set to `review`.

Expected command for checking remaining planned standard cards:

```bash
awk -F, '$4=="standard" && $5=="planned" {print}' work/national-parks-poker/brief/card-list.csv
```

Expected: no output.

## Task 5: Complete Joker, Back, And Tuck Box Artwork

**Files:**
- Create source and review exports for `joker-bear`
- Finalize source and review exports for `joker-bald-eagle`
- Finalize source and review exports for `card-back`
- Create: `work/national-parks-poker/source/tuck-box-source-notes.md`
- Create review exports for `tuck-box`

- [ ] **Step 1: Create Bear Joker**

Create `joker-bear` source and review export.

Acceptance checks:

```text
[ ] Uses the same vintage poster system as the deck.
[ ] Main subject is clearly a bear.
[ ] Includes Joker identity.
[ ] Does not look like a park-specific standard card.
[ ] No Chinese appears.
```

- [ ] **Step 2: Finalize Bald Eagle Joker**

Review and update `joker-bald-eagle`.

Acceptance checks:

```text
[ ] Main subject is clearly a bald eagle.
[ ] Includes Joker identity.
[ ] Pairs visually with `joker-bear`.
[ ] Does not look like a park-specific standard card.
[ ] No Chinese appears.
```

- [ ] **Step 3: Finalize card back**

Review and update `card-back`.

Acceptance checks:

```text
[ ] Symmetrical at 180-degree rotation.
[ ] No single park dominates the back.
[ ] Includes a central or integrated `NATIONAL PARKS` identity.
[ ] Uses no directional elements that could mark the card.
```

- [ ] **Step 4: Define tuck box source notes**

Create `work/national-parks-poker/source/tuck-box-source-notes.md` with:

```markdown
# Tuck Box Source Notes

Front:

- Title: NATIONAL PARKS PLAYING CARDS
- Vintage poster hero image representing the whole deck.
- Small line: 54 CARD DECK

Back:

- Short product copy.
- Mini preview grid or selected card samples.
- Barcode or production area if required by vendor.

Sides:

- NATIONAL PARKS
- PLAYING CARDS

Top and bottom:

- Brand mark, edition mark, or simple park-badge motif.

Production:

- Use the printer's final dieline before final export.
- Keep all text inside the dieline safe area.
- Keep fold, glue, and cut areas visible in source files but hidden or separated in final artwork as the vendor requires.
```

- [ ] **Step 5: Create tuck box review artwork**

Create a flat tuck-box review export and one 3D-style mockup if the design tool supports it.

Expected: front, back, sides, top, and bottom are all represented.

## Task 6: Export Digital Review Package

**Files:**
- Create: `outputs/national-parks-poker/digital/cards/`
- Create: `outputs/national-parks-poker/digital/contact-sheet.pdf`
- Create: `outputs/national-parks-poker/digital/hero-mockups/`

- [ ] **Step 1: Create digital export folders**

Run:

```bash
mkdir -p outputs/national-parks-poker/digital/cards
mkdir -p outputs/national-parks-poker/digital/hero-mockups
```

Expected: both folders exist.

- [ ] **Step 2: Export card PNGs**

Export:

```text
54 front PNGs
1 card-back PNG
```

Expected naming examples:

```text
outputs/national-parks-poker/digital/cards/AS-grand-canyon.png
outputs/national-parks-poker/digital/cards/AH-yosemite.png
outputs/national-parks-poker/digital/cards/AC-yellowstone.png
outputs/national-parks-poker/digital/cards/AD-joshua-tree.png
outputs/national-parks-poker/digital/cards/joker-bald-eagle.png
outputs/national-parks-poker/digital/cards/joker-bear.png
outputs/national-parks-poker/digital/cards/card-back.png
```

- [ ] **Step 3: Verify digital card count**

Run:

```bash
find outputs/national-parks-poker/digital/cards -maxdepth 1 -name '*.png' | wc -l
```

Expected: `55` PNG files.

- [ ] **Step 4: Create contact sheet**

Create `outputs/national-parks-poker/digital/contact-sheet.pdf` showing all 54 card fronts plus the card back.

Expected:

```text
[ ] Cards are shown in rank/suit order.
[ ] Jokers are grouped at the end.
[ ] Card back is labeled or placed separately.
[ ] Each thumbnail is large enough to inspect title placement.
```

- [ ] **Step 5: Create hero mockups**

Create 6-10 preview images in `outputs/national-parks-poker/digital/hero-mockups/`.

Minimum set:

```text
deck-spread.png
four-aces.png
jokers.png
card-back-preview.png
tuck-box-front.png
tuck-box-and-cards.png
```

## Task 7: Export Print Package

**Files:**
- Create: `outputs/national-parks-poker/print/cards/`
- Create: `outputs/national-parks-poker/print/tuck-box/`
- Create: `outputs/national-parks-poker/print/production-notes.md`

- [ ] **Step 1: Create print export folders**

Run:

```bash
mkdir -p outputs/national-parks-poker/print/cards
mkdir -p outputs/national-parks-poker/print/tuck-box
```

Expected: both folders exist.

- [ ] **Step 2: Export print-ready card files**

Export CMYK 300 DPI files with bleed included:

```text
54 card fronts
1 card back
```

Expected: every file includes 0.125 in bleed on all sides unless the printer's final spec says otherwise.

- [ ] **Step 3: Export tuck box print files**

Export print-ready tuck-box artwork using the selected printer's dieline.

Expected:

```text
[ ] Dieline source is preserved.
[ ] Artwork is aligned to trim, folds, glue areas, and safe zones.
[ ] Vendor-required hidden/visible dieline layers follow printer instructions.
```

- [ ] **Step 4: Create production notes**

Create `outputs/national-parks-poker/print/production-notes.md` with:

```markdown
# National Parks Playing Cards Production Notes

## Deck

- 52 standard cards plus 2 Jokers.
- Poker trim size: 2.5 x 3.5 in.
- Bleed: 0.125 in on all sides unless vendor spec overrides.
- Color: CMYK.
- Resolution: 300 DPI minimum.

## Files

- Card fronts: `print/cards/`
- Card back: `print/cards/card-back`
- Tuck box: `print/tuck-box/`

## Proofing Checks

- Confirm card trim and bleed against vendor requirements.
- Print one physical proof sheet before mass production.
- Check index legibility at physical size.
- Check title legibility for long park names.
- Check card back symmetry.
- Check color shifts from RGB previews to CMYK print files.
```

## Task 8: Final Quality Review And Handoff

**Files:**
- Create: `outputs/national-parks-poker/final-review.md`

- [ ] **Step 1: Run file-count checks**

Run:

```bash
find outputs/national-parks-poker/digital/cards -maxdepth 1 -name '*.png' | wc -l
find outputs/national-parks-poker/digital/hero-mockups -maxdepth 1 -type f | wc -l
find outputs/national-parks-poker/print/cards -maxdepth 1 -type f | wc -l
```

Expected:

```text
55 digital card PNGs.
At least 6 hero mockup files.
55 print card files, unless the selected printer requires a combined sheet instead of individual files.
```

- [ ] **Step 2: Review text and language**

Inspect all final customer-facing assets.

Expected:

```text
[ ] All park names are spelled correctly.
[ ] No Chinese appears on final customer-facing assets.
[ ] Jokers read as Bald Eagle and Bear.
[ ] Tuck box title reads NATIONAL PARKS PLAYING CARDS.
```

- [ ] **Step 3: Review visual consistency**

Inspect the contact sheet and hero mockups.

Expected:

```text
[ ] The deck reads as one cohesive vintage travel-poster series.
[ ] Each park still has a distinct identity.
[ ] Suits do not visually override park identity.
[ ] The card back is symmetrical and playable.
```

- [ ] **Step 4: Create final review record**

Create `outputs/national-parks-poker/final-review.md` with:

```markdown
# National Parks Playing Cards Final Review

## Package Contents

- Digital card PNGs: complete
- Digital contact sheet: complete
- Hero mockups: complete
- Print card files: complete
- Tuck box files: complete
- Production notes: complete

## Review Results

- English-only customer-facing text: pass
- Card mapping preserved: pass
- Rank and suit legibility: pass
- Long-title layout: pass
- Card back symmetry: pass
- Print bleed and safe margins: pass
- CMYK print export: pass

## Remaining Production Dependency

Final mass-production files must be checked against the selected printer's official dieline, color profile, paper stock, finish, and proofing requirements.
```

- [ ] **Step 5: Handoff**

Provide the user links to:

```text
outputs/national-parks-poker/digital/contact-sheet.pdf
outputs/national-parks-poker/digital/hero-mockups/
outputs/national-parks-poker/print/
outputs/national-parks-poker/final-review.md
```

## Plan Self-Review

Spec coverage:

- Product positioning is covered by Task 1 and the output README.
- Card template, typography, indexes, and card-face rules are covered by Task 2.
- Pilot visual validation is covered by Task 3.
- All 52 standard cards are covered by Task 4.
- Jokers, card back, and tuck box are covered by Task 5.
- Digital exports are covered by Task 6.
- Print exports are covered by Task 7.
- Final quality checks and handoff are covered by Task 8.

Red-flag scan:

- No unspecified implementation gaps are intentionally left in this plan.

Scope check:

- This plan covers design production only. It does not include online gameplay, vendor sourcing, manufacturing quotes, or ecommerce launch work.
