# American National Parks Playing Cards - Design Spec

## Status

Draft approved direction from product brainstorming. This spec is ready for user review before implementation planning.

## Product Goal

Create a premium standard playing-card deck for Western customers, themed around American national parks. The deck must work as both a playable physical poker deck and a digital visual asset set for previews, marketing, crowdfunding, and print production discussions.

## Confirmed Direction

- Product format: physical print deck plus digital card assets.
- Deck structure: 52 standard cards plus 2 Jokers.
- Visual style: vintage American national parks travel poster style.
- Market: English-speaking / Western customers.
- Card language: English only on final card faces.
- Mapping: preserve the existing 52-card park-to-rank mapping from `/Users/hushuo/Desktop/national-parks-poker-card-map.md`.
- Suit treatment: suits are functional poker identifiers only. They do not define the landscape category, palette, or visual concept for each park.
- Main card principle: each card should emphasize the most recognizable scenery, wildlife, geological feature, plant life, water feature, or landmark of its assigned park.

## Design Principles

1. Park identity comes first.
   Each card should feel specific to its park. Do not force a park into a suit-based terrain category.

2. The deck must still feel unified.
   Unity comes from consistent poster framing, typography, print texture, illustration treatment, corner index placement, and production color discipline.

3. The cards must remain playable.
   The rank and suit indexes must be legible at a glance. The art should not compete with the poker information.

4. Avoid encyclopedic information.
   Final card faces should not include Chinese names, long descriptions, founding years, state labels, or dense trivia.

5. Use print-safe design.
   All deliverables should support CMYK print, 300 DPI raster exports, bleed, safe area, and clear separation between print files and digital preview files.

## Card Face Layout

Each standard card face contains:

- Top-left index: rank plus suit.
- Bottom-right mirrored index: rank plus suit.
- Center area: vintage poster-style illustration for the assigned park.
- Park title: uppercase English name, for example `GRAND CANYON`, `YOSEMITE`, `YELLOWSTONE`.
- Small series line: `NATIONAL PARK`.
- Subtle border system inspired by park signage, poster mats, or printed ephemera.

The illustration should occupy most of the card face, but the indexes and title must remain readable at poker-table distance.

The `NATIONAL PARK` series line should be used consistently across the standard cards. If physical-size proofing shows that it crowds long park names, remove it deck-wide rather than using it inconsistently card by card.

## Typography

Recommended type direction:

- Park names: bold condensed sans serif or slab serif inspired by vintage travel posters.
- Indexes: highly legible standard playing-card style, not overly decorative.
- Small series line: simple uppercase sans serif.

Typography should support all long names without cramped or overlapping text, especially:

- `BLACK CANYON OF THE GUNNISON`
- `GREAT SMOKY MOUNTAINS`
- `HAWAI'I VOLCANOES`
- `THEODORE ROOSEVELT`

For long names, use two-line title lockups rather than shrinking text excessively.

## Color System

The deck should use restrained, print-friendly vintage poster palettes:

- Warm canyon reds, ochres, and sunset oranges where appropriate.
- Forest greens, lake blues, and misty grays where appropriate.
- Alpine blues, snow whites, and evergreen tones where appropriate.
- Desert tans, volcanic blacks, marsh greens, and coastal aquas where appropriate.

Suit colors should remain conventional:

- Spades and clubs: dark ink, likely black or near-black.
- Hearts and diamonds: red ink, likely deep vintage red.

Suit colors should not dictate the main illustration palette.

## Jokers

Create two Jokers:

1. `BALD EAGLE JOKER`
   - Main subject: bald eagle.
   - Tone: iconic, national, elevated.
   - Suggested composition: eagle in flight or perched above mountain/lake scenery.

2. `BEAR JOKER`
   - Main subject: bear.
   - Tone: wild, powerful, national-park wilderness.
   - Suggested composition: bear standing or walking in a forest/mountain setting.

Both Jokers should share the deck's vintage poster system but feel slightly more emblematic than the standard park cards.

## Card Back

The card back should be symmetrical and playable. Recommended elements:

- Center medallion or badge reading `NATIONAL PARKS`.
- Subtle wildlife and landscape icons, potentially including deer as a secondary motif.
- Mirrored mountain, forest, river, or trail shapes.
- No single park should dominate the back.
- No directional composition that makes the card back accidentally marked.

Recommended palette: deep green, cream, muted red, and dark ink, adjusted after sample mockups.

## Tuck Box

Front:

- Product title: `NATIONAL PARKS PLAYING CARDS`.
- Vintage poster hero image that represents the full deck rather than one specific park.
- Optional small line: `54 CARD DECK`.

Back:

- Short product copy.
- Mini preview grid or selected card samples.
- Barcode / production area if needed.

Sides:

- `NATIONAL PARKS`
- `PLAYING CARDS`

Top / bottom:

- Brand mark, edition, or simple park-badge motif.

## Print Specifications

Default production assumptions:

- Poker size: 2.5 x 3.5 in.
- Bleed: 0.125 in on all sides.
- Safe area: at least 0.125 in inside trim; larger for indexes and titles if printer recommends.
- Resolution: 300 DPI minimum.
- Color: CMYK print files.
- Source files: layered editable format where possible.
- Exports: print PDF, individual card fronts, card back, tuck box dieline artwork.

Final vendor specs may override these values.

## Digital Deliverables

Digital asset package:

- 54 individual front images as PNG.
- 1 card back PNG.
- 1 full-deck preview PDF.
- 1 contact sheet showing all card faces.
- 6-10 hero mockups for marketing or crowdfunding.
- Optional social preview crops.

Recommended naming pattern:

- `AS-grand-canyon.png`
- `KH-grand-teton.png`
- `AC-yellowstone.png`
- `JD-everglades.png`
- `joker-bald-eagle.png`
- `joker-bear.png`
- `card-back.png`

## 52-Card Mapping And Visual Motifs

These card assignments preserve the user's existing mapping. The visual motif column is a production starting point and should be verified against official NPS references or licensed visual references before final illustration.

| Card | Park | Suggested main visual motif |
|---|---|---|
| A Spades | Grand Canyon | Layered canyon cliffs, Colorado River depth, sunrise or sunset light |
| K Spades | Zion | Zion canyon walls, The Watchman, Virgin River corridor |
| Q Spades | Bryce Canyon | Hoodoo amphitheater, orange limestone spires |
| J Spades | Arches | Delicate Arch or sandstone arch formation |
| 10 Spades | Canyonlands | Mesa overlook, canyon maze, desert plateau |
| 9 Spades | Capitol Reef | Waterpocket Fold cliffs, sandstone domes, orchard valley hint |
| 8 Spades | Badlands | Striped eroded buttes and prairie horizon |
| 7 Spades | Black Canyon of the Gunnison | Narrow dark canyon walls and river below |
| 6 Spades | Guadalupe Mountains | Desert mountain ridge, El Capitan profile |
| 5 Spades | Mesa Verde | Cliff dwelling architecture set into sandstone alcove |
| 4 Spades | Petrified Forest | Painted Desert bands and petrified wood forms |
| 3 Spades | Carlsbad Caverns | Cavern chamber, stalactites, dramatic cave lighting |
| 2 Spades | Mammoth Cave | Cave passage, limestone arch, lantern-lit depth |
| A Hearts | Yosemite | Half Dome, El Capitan, waterfall valley composition |
| K Hearts | Grand Teton | Teton range, alpine lake, crisp mountain reflection |
| Q Hearts | Glacier | Glacial lake, rugged peaks, mountain goat or wildflower accent |
| J Hearts | Denali | Denali peak, tundra foreground, vast Alaskan scale |
| 10 Hearts | Rocky Mountain | Alpine peaks, meadow, elk silhouette or clear mountain lake |
| 9 Hearts | Mount Rainier | Snow-capped volcano, wildflower meadow |
| 8 Hearts | Sequoia | Giant sequoia trunk scale, forest canopy |
| 7 Hearts | Kings Canyon | Granite canyon, high Sierra forest, river valley |
| 6 Hearts | Glacier Bay | Tidewater glacier, floating ice, blue water |
| 5 Hearts | Kenai Fjords | Fjord cliffs, glacier, cold coastal water |
| 4 Hearts | Lassen Volcanic | Volcanic peak, hydrothermal steam, alpine terrain |
| 3 Hearts | Great Basin | Bristlecone pine, high desert sky, mountain backdrop |
| 2 Hearts | Pinnacles | Rock spires, condor silhouette, chaparral landscape |
| A Clubs | Yellowstone | Old Faithful geyser, thermal basin, bison accent if composition allows |
| K Clubs | Great Smoky Mountains | Layered blue ridges, forest mist |
| Q Clubs | Acadia | Granite coast, lighthouse or rocky shoreline, Atlantic sunrise |
| J Clubs | Olympic | Temperate rainforest, mossy trees, mountain/coast hint |
| 10 Clubs | Shenandoah | Blue Ridge overlook, rolling forested mountains |
| 9 Clubs | Cuyahoga Valley | Forested river valley, waterfall, rail/trail hint |
| 8 Clubs | New River Gorge | Steel arch bridge over river gorge |
| 7 Clubs | Redwood | Towering redwood forest, vertical scale |
| 6 Clubs | Congaree | Cypress swamp, boardwalk, floodplain forest |
| 5 Clubs | Theodore Roosevelt | Badlands prairie, bison or wild horse, butte landscape |
| 4 Clubs | Indiana Dunes | Lake Michigan dunes, beach grass, freshwater shoreline |
| 3 Clubs | Voyageurs | Lake islands, canoe/kayak silhouette, northern forest |
| 2 Clubs | Wind Cave | Prairie bison above ground or cave boxwork below ground |
| A Diamonds | Joshua Tree | Joshua trees, boulders, desert sunset |
| K Diamonds | Death Valley | Salt flats, desert basin, distant mountains |
| Q Diamonds | Hawai'i Volcanoes | Lava glow, volcanic crater, tropical volcanic landscape |
| J Diamonds | Everglades | Wetland grasses, water channel, wading bird or alligator accent |
| 10 Diamonds | Saguaro | Giant saguaro cactus, Sonoran desert, sunset sky |
| 9 Diamonds | Haleakala | Volcanic summit crater, sunrise above clouds |
| 8 Diamonds | White Sands | White gypsum dunes, wave-like sand, blue sky contrast |
| 7 Diamonds | Big Bend | Rio Grande bend, desert mountains, canyon wall |
| 6 Diamonds | Great Sand Dunes | Tall dunes with mountain backdrop |
| 5 Diamonds | Crater Lake | Deep blue lake, Wizard Island, caldera rim |
| 4 Diamonds | Biscayne | Clear water, coral reef, mangrove/coastal horizon |
| 3 Diamonds | Virgin Islands | Tropical beach, turquoise water, island hills |
| 2 Diamonds | Channel Islands | Sea cliffs, ocean, island fox or kelp/coastal motif |

## Production Workflow

1. Build a small visual test set before producing all 54 cards.
   Recommended first cards:
   - A Spades Grand Canyon
   - A Hearts Yosemite
   - A Clubs Yellowstone
   - A Diamonds Joshua Tree
   - Joker Bald Eagle
   - Card back

2. Confirm template, title lockups, corner indexes, texture level, and print legibility.

3. Produce the remaining 50 front designs using the approved system.

4. Export print and digital files.

5. Review with physical-size proofs before committing to full production.

## Quality Checks

- Each park name is spelled correctly in English.
- Long names fit without crowding.
- Rank and suit are legible when the card is held in hand.
- Card backs are symmetrical and not directionally marked.
- No Chinese appears on final customer-facing card assets.
- The deck is visually unified without flattening each park's identity.
- Print files include bleed and safe margins.
- Digital exports are consistently named.
- Visual motifs are checked against official or licensed reference material before final illustration.

## Out Of Scope For This Phase

- Online playable game implementation.
- Educational trivia copy on each card.
- State-by-state map system.
- Alternate editions for all 63+ national parks.
- Final vendor selection and print quote negotiation.
