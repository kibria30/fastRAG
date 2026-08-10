# Bangladesh Cropping Season Calendar

Source: Bangladesh Agro-Meteorological Information System (BAMIS) crop calendar
(https://www.bamis.gov.bd/en/calendar/) and Banglapedia "Crop"
(https://en.banglapedia.org/index.php/Crop), via search aggregate.
Retrieved: 2026-07-24/25

- **Kharif-1**: mid-March to end-June/July — Aus rice season.
- **Kharif-2**: July to mid-October — Aman rice season (monsoon-fed).
- **Rabi**: mid-October to mid-March, with regional variation — extreme west
  starts around 1-10 October, Northeast starts around 1-10 November; ends
  1-10 February in the west to 20-31 March in the Northeast.
- **Boro** (irrigated rice, overlapping Rabi/early pre-Kharif): planted
  November-December, harvested March-April.
- Data quality note — terminology varies by source: Banglapedia's "Crop"
  article instead frames the year as **Pre-Kharif** (late March-May: jute,
  broadcast aman, aus, groundnut), **Kharif** (May-October: aus,
  transplanted aman, sesame, cotton), and **Rabi** (November-April: wheat,
  boro, mustard, pulses, potato) — a two-season Kharif split by month rather
  than the Kharif-1/Kharif-2 by-crop split used above (and used consistently
  elsewhere in this knowledge base, e.g. aman_rice.md labels Aman as
  "Kharif-2"). Both framings describe the same underlying agricultural year;
  prefer the Kharif-1/Kharif-2-by-crop framing already used in this
  knowledge base for consistency, but don't be surprised if a source uses
  the Pre-Kharif/Kharif/Rabi framing instead — they aren't in conflict, just
  different ways of slicing the same calendar.
- Rabi growing period length varies regionally: about 100-120 days in
  western districts up to 140-150 days in the Northeast (Sylhet) — consistent
  with the BAMIS regional duration figures already in this knowledge base
  (e.g. potato 90-105 days, wheat 119 days, maize 112 days — all
  comfortably inside a 100-150 day Rabi window; see potato.md, wheat.md,
  maize.md).

## Rabi season crop list (beyond wheat/potato/maize/boro already detailed elsewhere)

Source: Banglapedia "Crop."

- Cereals: wheat, maize, barley, boro rice.
- Tuber/root crops: potato, sweet potato.
- Oilseeds: mustard, sesame, groundnut, niger, sunflower, linseed, safflower.
- Pulses: chickpea, lentil, grass pea, cowpea.
- Winter vegetables: cabbage, cauliflower, brinjal, tomato, carrot, turnip,
  radish, spinach, lettuce, bottle gourd, country bean, garden pea.
- Spices: chilli, onion, garlic, coriander, sweet cumin, black cumin,
  fenugreek.
- Fibre crop: sunhemp (distinct from jute, which is a Kharif-1/pre-monsoon
  crop — see jute.md).
- Sugar crop: sugarcane.
- Stimulant: tobacco.
- Fruit: watermelon.
- This knowledge base currently only has detailed agronomic files for a
  subset of these (wheat.md, potato.md, maize.md, boro_rice.md) — the rest
  (oilseeds, pulses, winter vegetables, spices, sugarcane, tobacco,
  watermelon) are named here for season-fit checking only; no fertilizer,
  yield, or BAMIS weather-calendar data exists for them in this knowledge
  base yet.

## Cropping patterns and intensity

Source: search aggregate of BBS-derived cropping-pattern studies (e.g.
"Distribution of Crops and Cropping Patterns in Bangladesh," "Cropping
Pattern, Intensity and Diversity in Dhaka Region," "Generation Change of
Cropping Intensity in Bangladesh: A Systematic Review").

- Rice dominates: roughly 74% of Bangladesh's total cropped area is under
  rice (some combination of Aus, Aman, and/or Boro).
- The single most common cropping pattern nationally is **Boro - Fallow -
  T. Aman** (Transplanted Aman), covering about 27% of net cropped area —
  i.e. many plots grow irrigated Boro then rain-fed T. Aman with a fallow
  gap, rather than a third crop.
- 316 distinct cropping patterns have been identified nationally (excluding
  very minor ones), reflecting how much cropping choice varies by local
  water availability, soil, and market access — the national pattern above
  is common, not universal.
- Regional variation example: in the South-East Coastal Region, single
  T. Aman alone (no second crop) is the dominant pattern at 35% of net
  cropped area, followed by Boro-Fallow-T.Aman (14%), Fallow-B.Aus-T.Aman
  (11%), and single Boro (11%) — a notably more single-cropped, less
  intensive pattern than the national figure, plausibly reflecting salinity
  and water-control constraints in coastal districts (see
  soil_types_bd.md's coastal salinity section).
- Cropping intensity (crops harvested per year per unit area, as a %)
  varies widely by region: national studies report intensity around 190%
  in the early 2010s, with favorable agro-ecological zones reaching
  196-202% (i.e. farmers there average nearly two full crops a year on the
  same land through sequential/relay cropping), while the greater Noakhali
  district averaged only 163% — again pointing to land/water-constrained
  coastal areas cropping less intensively than the high-Ganges/Brahmaputra
  floodplain heartland.
- Historically, the classic description of the cropping year is a "3-crop
  (three varieties of paddy)" combination — Aus, Aman, and Boro — with
  roughly 93-94% of the total Aus+Aman area being rain-fed rather than
  irrigated (Boro being the main irrigated rice season by contrast; see
  boro_rice.md).

## Regional precision available elsewhere in this knowledge base

This file gives only coarse, national-level season date ranges. For a much
more precise, region-by-region planting/harvest window (down to BAMIS
standard-week granularity, for 11-14 of Bangladesh's regions depending on
crop), see the "BAMIS Crop Weather Calendar" section in: aman_rice.md,
aus_rice.md, boro_rice.md, wheat.md, maize.md, potato.md, and jute.md. When
a farmer's district/region is known, prefer those regional figures over the
single national range given above.

## Notes for the agent

- Use this calendar to sanity-check a farmer-stated "target season" against
  what's actually plantable at that time of year, and to bound the season-plan
  dated calendar (land prep -> sowing -> harvest).
- Regional start/end dates vary — treat the ranges above as approximate guidance,
  not fixed cutoffs, and prefer the farmer's actual location/weather data when
  the two are in tension, or the region-specific BAMIS figures cross-referenced
  above when the region is known.
- Rice (Aus + Aman + Boro combined) covers the large majority of cropped
  area nationally — when a farmer's crop or season isn't specified, rice in
  some form is the statistically likely default, not an even split across
  all crops in this knowledge base.
- Cropping intensity and pattern data above are a proxy for how
  water/soil-constrained a region is — low intensity (~160%) or
  single-cropping-dominant patterns are a signal to weight irrigation
  access and salinity more heavily in that region's recommendations.
