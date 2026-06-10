# National Park Playing Card Project

## Purpose

This repository contains design drafts and review assets for an American national parks themed playing-card deck. The product direction is a premium 54-card poker-size deck for English-speaking Western customers, using a vintage American national park poster style.

The current work is design/artwork focused. It is not a production-ready print package yet.

## Current Deliverables

- 52 standard card face PNGs
- 2 regenerated Joker face PNGs
- 1 selected card back PNG
- 5 card back direction option PNGs
- 1 tuck box 3D mockup PNG
- 2 tuck box unfolded design draft PNGs
- 1 HTML review page
- Prompt and planning documents

Primary review page:

```text
outputs/national-parks-poker/index.html
```

Open it directly in a browser to review the deck, packaging, and card back.

## Important Product Decisions

- The deck uses English only.
- The 52-card park mapping is preserved from the user's original map.
- Suits are poker identifiers only; they do not classify parks by terrain or theme.
- Each standard card should emphasize the assigned park's most recognizable scenery, wildlife, geology, plant life, water, or landmark.
- The visual system is a 1930s-1950s WPA / vintage national park poster style.
- The user preferred the reference-style card layout: ivory paper, large vertical side index, bottom-right inverted index, central poster panel, thin red internal rule, and park name integrated with the art.
- The final card assets are direct generated design images, not product mockups.

## Final / Active Assets

Standard cards:

```text
outputs/national-parks-poker/digital/cards/
```

Active card back:

```text
outputs/national-parks-poker/digital/card-back-v2.png
```

Active tuck box mockup:

```text
outputs/national-parks-poker/packaging/tuck-box-mockup-v1.png
```

Active tuck box unfolded design draft:

```text
outputs/national-parks-poker/packaging/tuck-box-dieline-v2.png
```

Prompt document:

```text
outputs/national-parks-poker/national-parks-poker-image-prompts.md
```

Design spec:

```text
docs/superpowers/specs/2026-06-09-national-parks-poker-design.md
```

Implementation plan:

```text
docs/superpowers/plans/2026-06-09-national-parks-poker.md
```

## Joker Rules

The deck uses two Jokers:

- Big Joker: bald eagle artwork, red `JOKER` lettering, red star medallions.
- Small Joker: bear artwork, deep green `JOKER` lettering, deep green star medallions.

The final card artwork should only show the word `JOKER`. Do not put animal names, `BIG`, `SMALL`, park names, captions, logos, or slogans on the Joker faces.

The HTML review page labels them as Big Joker / Small Joker for review clarity.

Backups of earlier Joker versions are kept under:

```text
outputs/national-parks-poker/digital/cards/joker-regenerated-backups/
```

## Card Back Direction

The selected card back is option A:

```text
outputs/national-parks-poker/digital/card-back-v2.png
```

It is a no-text, symmetrical compass + mountain/river ornament direction. It was chosen over more traditional and botanical alternatives because the user preferred its stronger theme expression.

Card back constraints:

- No text.
- No specific park names.
- No NPS / National Park Service marks.
- No official-looking Arrowhead badge.
- No single-direction landscape.
- Must be playable as a direction-neutral card back.

## Packaging Direction

The active tuck box unfolded concept is:

```text
outputs/national-parks-poker/packaging/tuck-box-dieline-v2.png
```

The back panel uses a brand badge / compass / mountain motif instead of showing fake sample cards. The user rejected the earlier back-panel card-preview idea because its small card illustrations did not match the actual deck.

Do not use `POKER SIZE` on the package unless the user explicitly asks for it. The preferred bottom text is `54 CARD DECK`.

## IP / Trademark Caution

Avoid anything that could be confused with official National Park Service branding.

Do not use:

- NPS
- National Park Service
- official Arrowhead badge shape
- official-looking park agency seals
- `Official`
- `Authorized`
- `Find Your Park`
- `America the Beautiful`

Recommended packaging disclaimer for commercial release:

```text
Not affiliated with or endorsed by the National Park Service.
```

This repository is not a legal review. Commercial use should be reviewed by a qualified US IP/trademark attorney.

## HTML Review Page Notes

The review page groups assets into:

- Packaging & Card Back
- Spades
- Hearts
- Clubs
- Diamonds
- Jokers

It includes search and suit filters. If card filenames change, update the `cards` array inside:

```text
outputs/national-parks-poker/index.html
```

## Validation Commands

Use this quick check after editing asset references:

```bash
node <<'NODE'
const fs = require('fs');
const path = require('path');
const html = fs.readFileSync('outputs/national-parks-poker/index.html', 'utf8');
const cardFiles = [...html.matchAll(/file: "([^"]+)"/g)].map((match) => `outputs/national-parks-poker/digital/cards/${match[1]}`);
const imageRefs = [...html.matchAll(/(?:href|src)="([^"]+\.png)"/g)].map((match) => `outputs/national-parks-poker/${match[1]}`);
const missing = [...new Set([...cardFiles, ...imageRefs])].filter((file) => !fs.existsSync(path.resolve(file)));
console.log(JSON.stringify({
  cardReferences: cardFiles.length,
  uniqueCardReferences: new Set(cardFiles).size,
  missing,
}, null, 2));
if (cardFiles.length !== 54 || new Set(cardFiles).size !== 54 || missing.length) process.exit(1);
NODE
```

Expected result:

```text
cardReferences: 54
uniqueCardReferences: 54
missing: []
```

## Working Guidelines For Future Agents

- Preserve the user's approved visual direction unless explicitly asked to explore alternatives.
- Do not replace working generated assets without keeping a backup or versioned file.
- Avoid adding Chinese text; this product is aimed at Western customers.
- Do not add animal names to the Joker artwork or review labels unless the user explicitly changes that requirement.
- Keep the current 52-card mapping unless the user asks to revise it.
- Keep suit categories as review organization only, not as art direction.
- Generated image outputs should be saved into the project, not left only under the default generated image cache.
- Before claiming completion, verify that the HTML references all 54 card faces and top-level review assets without missing files.
