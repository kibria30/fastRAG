# Aus Rice (Pre-Monsoon / Kharif-1 Season)

Source: BAMIS (Bangladesh Agro-Meteorological Information Portal) — Crop
Weather Calendar of Aus Rice, covering Sylhet, Rangpur, Rangamati, Rajshahi,
Mymensingh, Khulna, Jashore, Faridpur, Dinajpur, Dhaka, Cumilla, Chattogram,
Bogura, and Barishal regions (14 regions — full national coverage).
Retrieved: 2026-07-24

- BAMIS-wide crop duration: 126 days from seedbed to harvest, uniform across
  all 14 regions. This is shorter than Aman rice's 133-day BAMIS duration
  (see aman_rice.md) — Aus is the shortest-season rice crop of the three
  covered in this knowledge base.
- Growth-stage sequence (same order in all regions): Seedbed → Transplanting
  → Tillering → Heading → Flowering → Grain Formation → Maturity to
  Harvesting.
- Regional season windows (by transplanting start, std. week):
  - March-start regions (std. week ~11): Rangpur, Rangamati, Faridpur,
    Dinajpur, Chattogram, Barishal — harvest by July.
  - April-start regions (std. week ~15-17): Sylhet, Mymensingh, Khulna,
    Dhaka, Cumilla, Bogura — harvest by August-September.
  - May-start regions (std. week ~20): Rajshahi, Jashore — harvest by
    September.
- This makes Aus the earliest-planted rice crop of the year (pre-monsoon,
  Kharif-1), sown well before Aman rice's June-July transplanting window
  (see aman_rice.md) and harvested before the monsoon peaks in most regions.

## Favorable weather conditions by growth stage (consistent across all 14 regions)

- Germination: minimum temperature at least 10°C.
- Mid-season (tillering): light intensity ≤200% of normal, high relative
  humidity, soil temperature above 16°C.
- Later season: 22-25°C then 23-27°C temperature windows favor grain
  formation through maturity.
- Phase-wise water requirement across 5 broad growth phases (seedbed,
  transplanting, tillering, heading/flowering, grain formation-maturity): 76,
  120, 190, 145, 100 mm — total ≈ 621 mm/season. This matches the Aman rice
  water-requirement profile exactly (same BAMIS national template applied to
  both seasons).

## Congenial weather conditions for pests & diseases (uniform trigger values nationwide; presence varies by region)

- Blast: night temperature 16-20°C for 7.5 hours, day temperature 25-30°C
  for 7.5 hours, day-night temperature difference >10°C, RH >90%, cloudy.
  Universal — listed for every region in this source.
- Stem borer: minimum temperature >20.3°C, maximum 29.5-34.7°C, optimum
  24-29°C, morning RH >84%, afternoon RH >38.7%, dry weather. Universal.
- Leaf roller: maximum temperature 32-33°C, RH 92-95%. Universal.
- Rice bug: higher maximum temperature >31.9°C, morning sunshine >5.9 hrs;
  alternatively lower minimum temperature <22.1°C, afternoon RH <66.4%, dry
  or intermittent rain. Universal.
- Sheath rot: temperature 25-28°C, RH >90%, cloudy weather. Listed for every
  region in this source.
- Bacterial Leaf Blight (BLB): temperature 28-30°C, RH 80-90%, cloudy,
  rainfall >30 mm. Listed for every region except Barishal.
- Sheath Blight: temperature 28-32°C, high RH, cloudy weather. Listed for 11
  of 14 regions; absent from Mymensingh, Faridpur, and Barishal.
- Brown plant hopper: temperature >32°C, RH 80-90%, drizzle, wet spell,
  rainfall <75 mm. Listed for Rangpur, Rajshahi, Khulna, Faridpur, Dinajpur,
  Cumilla, Chattogram, and Barishal (8 of 14); absent from Sylhet, Rangamati,
  Mymensingh, Jashore, Dhaka, and Bogura.
- Gall midge: maximum temperature >33.0°C, afternoon RH <71%, sunshine
  >7.4 hrs/day. Only listed for Jashore — same trigger values as the Aman
  rice calendar's Jashore entry.
- Rice hispa: maximum temperature 32-35°C, minimum temperature 24-26°C,
  maximum RH 96-99%, minimum RH 75-81%. Only listed for Bogura — this pest
  does not appear anywhere in the Aman rice calendar.
- Rat: cloudy weather with high humidity and high temperature. Only listed
  for Barishal — the only rodent-pest entry in this knowledge base.

## Weather warning thresholds (BAMIS, same nationwide)

- Heavy rain: >50 mm/day (early season), rising to >100 mm/day (mid season),
  back to >50 mm/day (late season).
- Wet spell: >25 mm over 3 days (early), >50 mm over 4 days (mid), 20 mm
  over 4 days (late).
- Cloudy weather: flagged as a risk factor in mid- and late-season windows.
- High wind: >50 km/hr (early), >40 km/hr (mid), >30 km/hr (late).
- Temperature warning: minimum temperature <10°C, flagged at every stage.

## Notes for the agent

- This is the only source in this knowledge base for Aus rice. Unlike
  potato.md and aman_rice.md, there's no separate field-trial or BARI
  fertilizer/variety-yield source cross-checked here — treat the 126-day
  duration and every figure above as BAMIS-only until a second source is
  added.
- Aus, Aman, and Boro are Bangladesh's three rice-growing seasons; this file
  covers only Aus. See aman_rice.md and boro_rice.md for the other two — the
  pest/disease trigger values (temperature/RH thresholds for Blast, Stem
  borer, Leaf roller, Rice bug, Sheath rot, BLB, Sheath Blight, and Brown
  plant hopper) are identical between the Aus and Aman BAMIS calendars; only
  which regions flag each pest, and the crop calendar/duration, differ.
- Blast, Stem borer, Leaf roller, Rice bug, and Sheath rot are universal
  risks (all 14 regions); BLB, Sheath Blight, and Brown plant hopper are
  regional (see the per-pest notes above). Gall midge (Jashore), Rice hispa
  (Bogura), and Rat (Barishal) are each unique to a single region.
- No fertilizer, seeding-rate, or yield figures were present in this source.
  If those are needed for cost/yield estimates (the way crop_reference.py
  uses figures for other crops), they must come from a separate BARI/DAE
  source — don't fabricate them here.
