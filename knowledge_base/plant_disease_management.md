# Plant Disease Control Measures — Rice, Wheat, Maize, Potato, Jute

This file gives **control measures** (fungicide/pesticide active ingredient,
dose, and Bangladesh market trade name) for diseases of the crops actually
covered elsewhere in this knowledge base: Rice (Aman/Aus/Boro), Wheat, Maize,
Potato, and Jute. It complements, rather than duplicates, the BAMIS
weather-trigger sections already in aman_rice.md, aus_rice.md, boro_rice.md,
wheat.md, maize.md, potato.md, and jute.md — those answer "how likely is
this disease right now," this file answers "what do I spray/apply, at what
dose, and at what growth stage." A prior version of this file focused on
generic PlantVillage-classifier crops (apple, grape, citrus, tomato, pepper,
etc.) that are not significant Bangladeshi field crops; it has been replaced
by this version, built from a Bangladesh-specific crop-protection reference
covering the crops actually grown here.

Source: user-provided crop-protection reference
(`data/knowledge_base/plant_disease.txt`). Its table formatting matches
Bangladesh Department of Agricultural Extension (DAE) / Bangladesh Rice
Research Institute (BRRI)-style crop-protection guidance (favorable
weather → control measure → infestation/growth stage, with generic name,
dose, and local trade name), but no source URL was provided — figures and
trade names below are reproduced as given, not independently re-verified
against a public source. Some rows in the original were broken across table
cells (common name and trade name on separate lines) and one field
("শীষ বের হওয়া", literally "panicle/ear emergence" — the rice heading stage)
was in Bangla; both are fixed/translated below.
Retrieved: 2026-07-25 (source document authored 2026-07-25/26).

## Glossary and units

- RH = Relative Humidity.
- **Decimal** (also called *shotangsho*): a land unit used in one wheat
  control-measure dose below. 1 decimal = 0.01 acre ≈ 40.47 m²; 100 decimals
  = 1 acre; ≈247.1 decimals = 1 hectare. This differs from the kg/ha or
  g/L-of-water dosing used everywhere else in this file and knowledge
  base — don't silently convert it, since the source gave it per-decimal
  specifically.
- Trade names are Bangladesh agrochemical market brand names as given in the
  source, reproduced alongside the generic (active ingredient) name where
  the source paired them. A few pairings (noted inline) look like they may
  have been scrambled by the original table's formatting — flagged, not
  silently corrected.

## Rice — Aman, Aus, and Boro (shared disease/control list)

The underlying disease list, favorable-weather triggers, and control
measures are identical across all three rice seasons in the source, with one
exception (False smut infestation timing — noted under that disease below).

### Blast
- Favorable weather: night temperature 16-20°C for 10 hours, day temperature
  25-30°C for 10 hours, day-night temperature difference above 10°C, RH
  above 90%, cloudy.
- Control measure: Nativo 75WG or Trooper @ 0.6 g/litre water; or Amistar
  Top 325 SC @ 1 ml/litre water.
- Infestation stage: all stages.
- Cross-check: aman_rice.md/aus_rice.md/boro_rice.md (BAMIS source) give the
  same 16-20°C/25-30°C temperature bands but a shorter 7-8.5 hour duration
  window rather than 10 hours — the two sources disagree on duration but
  agree on temperature; treat 7-10 hours as the plausible range rather than
  picking one.

### Brown spot
- Favorable weather: temperature 28-30°C, high RH, cloudy weather.
- Control measure: fertilizer management (balanced nutrition, not a
  standalone chemical fix), plus spray of Thiovit (sulphur-based fungicide)
  + Potash.
- Infestation stage: all stages.
- Cross-check: matches the temperature/RH/cloudy trigger already in
  aman_rice.md's Brown spot entry.

### Bacterial blight (Bacterial Leaf Blight)
- Favorable weather: temperature 28-30°C, RH 80-90%, cloudiness, rainfall
  above 30 mm.
- Control measure: fertilizer management, plus spray of Thiovit + Potash.
- Infestation stage: seedling to flowering stage.
- Cross-check: matches aman_rice.md's Bacterial Leaf Blight trigger exactly.

### Foot rot
- Favorable weather: temperature 28-30°C, RH above 90%, intermittent
  rainfall, cloudy.
- Control measure: seed treatment with Carboxin @ 2.5-3.0 g/kg seed (trade
  name: Vitavax-200).
- Infestation stage: seedling to tillering stage.
- Not previously in this knowledge base's rice files — net-new disease
  entry for Aman/Aus/Boro.

### Sheath blight
- Favorable weather: temperature 28-32°C, high RH, cloudy weather.
- Control measure: Hexaconazole @ 1 ml/litre water (paired with Nativo 75WG
  in the source), or Tebuconazole @ 1 ml/litre water (Folicur 250EC).
- Infestation stage: maximum tillering to dough stage.
- Cross-check: matches aman_rice.md's Sheath Blight trigger (28-32°C, high
  RH, cloudy) exactly. Note: Nativo 75WG is more commonly marketed elsewhere
  as a Tebuconazole+Trifloxystrobin combination, not Hexaconazole — this
  generic/trade pairing may be a table-alignment artifact in the source;
  reproduced as given rather than corrected.

### Sheath rot
- Favorable weather: temperature 25-28°C, cloudy weather, high RH above
  90%.
- Control measure: any one of Nativo 75WG, Trooper, Amistar Top 325 SC, or
  Hexaconazole @ 1 ml/litre water.
- Infestation stage: booting stage.
- Cross-check: matches aman_rice.md's Sheath rot trigger (25-28°C, cloudy,
  RH >90%) exactly.

### False smut
- Favorable weather: temperature 22-27°C.
- Control measure: fertilizer management (no chemical spray given in
  source).
- Infestation stage: **Aman** — heading/panicle-emergence stage through
  grain formation stage. **Aus and Boro** — soft dough to ripening stage.
  (This is the one point where the source gives different timing per
  season; everything else above is identical across Aman/Aus/Boro.)
- Not previously in this knowledge base's rice files — net-new entry.

## Wheat

### Wheat Blast
- Favorable weather: continuous rain and average temperature 18-20°C during
  the crop's flowering stage, followed by sunny weather and humid days.
  Blast intensity is highest at 30°C and increases with longer leaf-wetting
  duration; at 25°C with a wetting period under 10 hours intensity is
  lowest, but at 25°C with a 40-hour wetting period, intensity reached 85%
  in the source data — wetting-period duration matters as much as
  temperature.
- Control measure: Nativo 75WG @ 6 g/decimal (see Glossary for the decimal
  land unit), or seed treatment @ 2-3 g/kg seed with a product whose name is
  unclear in the source (rendered "Noen" — likely an OCR/transliteration
  artifact; do not treat this as a confirmed product name).
- Infestation stage: all stages.
- Cross-check: matches wheat.md's existing Wheat Blast entry (continuous
  rain, 18-20°C during flowering, sunny/humid after, intensifying at 30°C)
  and adds the wetting-period-duration detail wheat.md didn't have.

### Foot rot
- Favorable weather: temperature 18-24°C, RH above 40%.
- Control measure: Propiconazole @ 1.5 ml/litre water (Tilt-250EC or Shadid
  250EC), or Carbendazim @ 1.5 ml/litre water (G-gurd).
- Infestation stage: seedling stage.
- Not previously in wheat.md — net-new entry.

### Seed and seedling rot
- Favorable weather: not given in source.
- Control measure: same options as Foot rot — Propiconazole @ 1.5 ml/litre
  water (Tilt-250EC/Shadid 250EC), or Carbendazim @ 1.5 ml/litre water
  (G-gurd).
- Infestation stage: not given in source.
- Not previously in wheat.md — net-new entry.

### Leaf blight
- Favorable weather: temperature 25°C, high RH.
- Control measure: seed treatment with Carboxin @ 2.5-3.0 g/kg seed (trade
  name: Vitavax-200).
- Infestation stage: vegetative stage.
- Not previously in wheat.md — net-new entry (distinct from wheat.md's Leaf
  rust, below).

### Brown spot
- Favorable weather: temperature 20°C, dew present for 4 hours.
- Control measure: Carbendazim @ 1.5 ml/litre water (G-gurd), or
  Propiconazole @ 1.5 ml/litre water (Tilt-250EC/Shadid 250EC).
- Infestation stage: vegetative stage.
- Not previously in wheat.md — net-new entry.

### Leaf rust
- Favorable weather: temperature 15-25°C, rain and high dew.
- Control measure: Hexaconazole @ 1 ml/litre water (Anvil 5 SC), or
  Tebuconazole/Carbendazim @ 1 ml/litre water (Conza 5EC/Akonazol 250EC).
- Infestation stage: vegetative to reproductive stage.
- Cross-check: matches wheat.md's existing Leaf rust trigger (15-25°C, rain,
  high dew) exactly; this adds the fungicide control measures wheat.md
  lacked.

### Powdery mildew
- Seasonal window: 15 November – 5 April.
- Favorable weather: optimum temperature 15-20°C, RH above 40%.
- Control measure: spray Propiconazole @ 1 ml/litre water (Tilt-250EC).
- Infestation stage: vegetative stage.
- Not previously in wheat.md — net-new entry.

### Loose smut
- Favorable weather: temperature 22-25°C, RH 60-85%.
- Control measure: seed treatment with Carboxin @ 3.0 g/kg seed
  (Thiram/Vitavax-200).
- Infestation stage: booting to flowering stage.
- Cross-check: matches wheat.md's existing Loose smut trigger (22-25°C, RH
  60-85%) exactly; this adds the seed-treatment control measure wheat.md
  lacked.

### Karnal bunt
- Favorable weather: temperature 8-22°C, RH above 70%.
- Control measure: seed treatment with Carboxin @ 3.0 g/kg seed
  (Thiram/Vitavax-200).
- Infestation stage: grain filling stage.
- Not previously in wheat.md — net-new entry.

## Maize

### Stalk rot
- Favorable weather: temperature 18-35°C, RH 90%.
- Control measure: Propiconazole @ 1.5 ml/litre water (Tilt-250EC/Shadid
  250EC), or Carbendazim @ 1.5 ml/litre water (G-gurd).
- Infestation stage: vegetative to reproductive stage.
- Not previously in maize.md — net-new entry (maize.md's BAMIS pest list
  only covers Seed Rot and Fall Army worm, both insect/abiotic risks, not
  this fungal disease).

### Leaf blight
- Favorable weather: temperature 22-32.5°C, RH above 90%.
- Control measure: Carbendazim @ 1 ml/litre water, or Propiconazole @ 2
  ml/litre water.
- Infestation stage: vegetative stage.
- Not previously in maize.md — net-new entry.

### Seed and seedling rot
- Favorable weather: above 30°C; development requires a 14.6°C threshold
  temperature and 138 day-degrees C.
- Control measure: seed treatment with a Thiram/Vitavax-group fungicide @
  2.5-3.0 g/kg seed.
- Infestation stage: silking to cob-formation stage.
- Data quality flag: the 14.6°C / 138 day-degree figure here is identical
  to the Fall Army Worm **pupal** development threshold already cited in
  maize.md's BAMIS pest section. That threshold describes an insect life
  stage, not fungal disease development — this looks like a copy/mapping
  artifact in the original source (the same day-degree figure attached to
  two different organisms) rather than a real shared biological threshold.
  Flagged, not resolved — don't assume the two are actually linked.

### Corn ear and grain rot
- Favorable weather / infestation stage: not given in source.
- Control measure: Propiconazole @ 1.5 ml/litre water (Tilt-250EC/Shadid
  250EC), or Carbendazim @ 1.5 ml/litre water (G-gurd).
- Not previously in maize.md — net-new entry.

## Potato

### Potato Scab
- Favorable weather: temperature 15-25°C, RH 70-90%.
- Infestation period: December-February.
- Control measure: not given in source — treat as a gap, don't invent a
  chemical control for this entry.
- Not previously in potato.md — net-new entry.

### Late Blight
- Favorable weather: temperature 16-20°C; cold and humid weather is
  congenial; low night temperature with high humidity, drizzle, fog, and
  dew accumulation on leaves can make the disease epidemic.
- Control measure: spray Mancozeb @ 2 g/litre water (Dithane M-45/Indofil
  M-45/Haymancozeb 80WP/Mcozeb 80WP).
- Infestation stage: seedling to maturity stage.
- Cross-check: matches potato.md's existing Late Blight trigger (16-20°C,
  cold/humid/fog/dew → epidemic) exactly; this adds the fungicide control
  measure potato.md lacked. Also see potato.md's cited 25-57% Bangladesh
  yield-loss figure and BARI resistant-variety data for broader management
  context beyond fungicide spraying.

### Fusarium wilt
- Favorable weather: high night temperature 28-30°C, RH 80-90%.
- Control measure: spray Carbendazim @ 1 g/litre water, 2-3 times at 7-10
  day intervals (Bavistin WP/Bendazim 50WP/Haydazim 50WP).
- Infestation stage: seedling to vegetative growth stage.
- Cross-check: matches potato.md's existing Fusarium wilt trigger (night
  temp 28-30°C, RH 80-90%) exactly.

### Potato Leaf Roll Virus
- Favorable weather: average temperature 18-20°C, RH 70% (favors the aphid
  vector).
- Control measure: spray Imidacloprid @ 0.5 ml/litre water, or Malathion @
  2 ml/litre water, at 15-day intervals, to control the aphid vector
  (Admire/Fyfanon 57EC).
- Infestation stage: seedling to tuber bulking/development stage.
- Cross-check: matches potato.md's existing PLRV trigger (18-20°C, RH ~70%)
  exactly; this adds the vector-control spray measure potato.md lacked.

### Bacterial wilt
- Favorable weather: high night temperature 28-30°C, RH 80-90%.
- Control measure: apply stable bleaching powder (SBP) @ 25-30 kg/ha before
  final ploughing.
- Infestation stage: seedling to vegetative growth stage.
- Cross-check: matches potato.md's existing Bacterial wilt trigger (28-30°C,
  RH 80-90%) exactly.

## Jute

### Seedling blight
- Favorable weather: high soil temperature.
- Control measure: spray Mancozeb @ 2 g/litre water, or seed treatment with
  Provex-200 @ 4 g/kg seed (Dithane M-45/Manner M-45/Vitavax-200/Provex-200).
- Infestation stage: seedling stage.
- Cross-check: matches jute.md's existing Seedling blight trigger ("higher
  soil temperatures") and adds the control measure jute.md lacked.

### Stem rot
- Favorable weather: temperature 15-40°C, warm and dry weather.
- Control measure: spray Mancozeb @ 2 g/litre water (Dithane M-45/Manner
  M-45).
- Infestation stage: vegetative stage.
- Cross-check: matches jute.md's existing Stem rot trigger exactly.

### Die back
- Favorable weather: temperature 15-40°C, warm and dry weather (identical
  trigger to Stem rot).
- Control measure: spray Mancozeb @ 2 g/litre water (Dithane M-45/Manner
  M-45).
- Infestation stage: vegetative stage.
- Cross-check: matches jute.md's existing Die back trigger, which already
  noted this disease shares Stem rot's exact threshold.

### Leaf Mosaic
- Favorable weather: temperature 20-30°C, RH around 80% (favors the
  whitefly vector).
- Control measure: spray Malathion @ 2 ml/litre water (Fyfanon 57EC/Hilthion
  57EC/Rogor) to control the whitefly vector.
- Infestation stage: vegetative stage.
- Cross-check: matches jute.md's existing Leaf Mosaic trigger exactly.

### Blank band
- Favorable weather: not given in source.
- Control measure: spray Mancozeb @ 2 g/litre water (Dithane M-45/Manner
  M-45).
- Infestation stage: vegetative stage.
- Cross-check: jute.md gives this disease's favorable weather as 25-28°C
  (a detail this source didn't repeat) but had no control measure — the two
  sources complement each other here.

### Root knot
- Favorable weather: high temperature and prolonged water logging.
- Control measure: Carbofuran @ 40 kg/ha of land (Furadan-5G/Furataf
  5G/Razfuran 5G).
- Infestation stage: vegetative stage.
- Cross-check: matches jute.md's existing Root knot/rot trigger exactly.

## Notes for the agent

- Pair this file with the BAMIS weather-trigger sections in aman_rice.md,
  aus_rice.md, boro_rice.md, wheat.md, maize.md, potato.md, and jute.md: use
  those to flag disease *risk* proactively from the weather forecast, and
  this file to ground the specific spray/dose/product recommendation once a
  disease is suspected or confirmed (via farmer description or the
  `plant_disease.py` image classifier, where the crop/disease overlaps with
  its 38 classes — notably Corn/Maize's Common Rust and Northern Leaf
  Blight, and Potato's Late Blight).
- Several entries have gaps the source didn't fill (Potato Scab has no
  chemical control measure; Wheat's Corn ear/grain rot and Seed-and-seedling
  rot have no stated infestation stage; Jute's Blank band has no stated
  favorable weather). Don't invent values for these — state the gap if
  asked, the way potato.md and wheat.md already do for their own missing
  figures.
- Dosages here are almost all per-litre-of-spray-water (ml or g/litre) or
  per-kg-of-seed, not per-hectare/per-acre field-rate — this is a different
  unit convention from the kg/ha fertilizer figures elsewhere in this
  knowledge base (aman_rice.md, boro_rice.md, wheat.md, maize.md, potato.md,
  jute.md). Don't convert or combine the two without accounting for spray
  volume per unit area, which this source doesn't specify.
- Trade names are Bangladesh market brand names as given; where a
  generic-name/trade-name pairing looks chemically atypical (flagged inline,
  e.g. Rice Sheath blight's Hexaconazole/Nativo 75WG pairing), treat the
  pairing as reproduced-from-source rather than independently verified —
  don't present it to a farmer as definitively correct without a second
  source.
