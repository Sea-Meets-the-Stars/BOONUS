# BOONUS: initial context for Claude

**Version 0.1, 2026-09-21, JXP and Claude.** Canonical project brief for the Boundary
Ocean Observing Network for the United States (BOONUS). Change log at the end.

**How to use this file.** Read it in full before writing anything about BOONUS
(documents, figures, requirements, code comments). Section 1 gives the single canonical
value for every project fact; where a source document disagrees, the digest in
`context/sources/` records the difference and this file wins. Claims in Sections 2-5
carry one of four tags: `[demonstrated]` (published, or in the CUGN record),
`[planned]` (a design decision JXP has made), `[aspirational]` (the pitch; not yet
shown), `[TBD]` (undecided). Canonical facts in Section 1 and project estimates
attributed to JXP are not tagged. Follow the style rules in Section 6.

---

## 1. Canonical fact sheet

| Item | Canonical value |
|---|---|
| Name | Boundary Ocean Observing Network **for** the United States. Always the acronym **BOONUS** after first use; never "BONUS", never "of the United States". |
| One sentence | A proposed, sustained network of 100+ autonomous underwater gliders that monitors the physical and biogeochemical state of U.S. coastal waters across the Exclusive Economic Zone (EEZ) and beyond, in near-real time, coupled to assimilative regional ocean models. |
| Framing | A coastal climate-observing network that uses boundary-current repeat sections (CUGN-style lines) as its sampling unit. Not a boundary-current transport network per se. |
| Fleet | 100+ gliders total; 50+ in the water at all times; at least 2 gliders committed per line (the CUGN ratio: one at sea, one in refurbishment); plus a separate pool for targets of opportunity (storms, blooms, events). At 2 per line, 100 gliders supports at most ~50 line-equivalents before the opportunity pool is set aside. |
| Footprint | The U.S. EEZ and beyond, sections reaching ~500 km offshore. |
| Lines | TBD. Locations will be selected by observing-system design experiments with the regional models, starting from the CUGN lines. The site map in the multi-pager is illustrative, not a plan. No regions are defined today. |
| Sampling | Dives to 500 m (or the bottom); a dive cycle of ~3 h covering ~3 km; a section of 350-500 km takes 2-3 weeks. CUGN practice, adopted as the BOONUS design. |
| Sensors (placeholder) | Temperature, salinity, horizontal currents (depth-average velocity from dead reckoning, plus ADCP shear), dissolved oxygen, chlorophyll fluorescence, pH, optical backscatter. Core versus optional is TBD; nitrate is under discussion for HAB work. |
| Platform | Spray glider (Scripps) is the default; platform-agnostic operation is TBD. |
| Data | Open, near-real time. Delivered to the IOOS Glider Data Assembly Center (DAC) and the GTS as CUGN data are today, and to a BOONUS public archive with analysis and visualization tools and a Python API. |
| Models | ROMS (regional, assimilative), ECCO (NASA global state estimate) for boundary conditions, the Darwin ecosystem model for biogeochemistry, and an AI-driven component (Section 5). |
| Horizon | Sustained for over 10 years. |
| People | J. Xavier Prochaska (JXP, UC Santa Cruz Ocean Sciences), lead. Daniel L. Rudnick (Scripps Institution of Oceanography), CUGN lead since 2005. Nominal lead for the AI-driven component: Matt Mazloff (Scripps). No one else is named in BOONUS documents until the roster is settled. |
| Governance | Organized and funded independently of IOOS (Section 4). |
| Funding | Model TBD. Working assumption: non-federal capital for construction; federal partnership for data products. |
| Cost | Model TBD. The pitch anticipates an economy of scale relative to CUGN `[aspirational]`. Do not invent a number. |
| Lineage | Takes its name from the OceanGliders Boundary Ocean Observing Network (BOON, 2018), which is dormant to our knowledge. BOONUS is not a formal BOON node. |
| Scaling anchor | CUGN: 4 standard lines plus 1 alongshore line, 10 gliders minimum to keep the program active (JXP). |
| Coverage gap | Less than 10% of U.S. coastal waters are regularly sampled in situ beyond the nearshore, versus ~300 km Argo spacing in the open ocean. Project estimate (JXP); not derived in this repository. |

## 2. Motivation and framing

**The coastal climate signal.** Climate change manifests at the coast differently from
the open ocean and differently region to region, through upwelling, river input, shelf
dynamics and weather `[demonstrated: IOOS 2021]`. About 40% of the U.S. population lives
in coastal counties; coastal and ocean activity is tied to more than half of GDP
`[demonstrated: IOOS 2021, citing NCA3]`. Coastal waters are the hardest part of the
ocean to model and predict, and are the least sampled in situ below the surface
(Section 1, coverage gap).

**Anomalous events BOONUS is meant to catch early.**

- *Marine heat waves.* The 2014-15 northeast Pacific warm anomaly ("the Blob") and the
  2015-16 El Nino were resolved in CUGN sections, including their subsurface structure
  `[demonstrated: Zaba & Rudnick 2016; Rudnick et al. 2017]`. The Blob's harmful algal
  bloom closed the Dungeness crab fishery at a cost above $100M `[demonstrated: IOOS
  2021]`. Subsurface heat content also feeds hurricanes; IOOS hurricane gliders already
  fly 40+ missions per season into forecast models `[demonstrated: IOOS 2021]`.
  BOONUS would provide this detection nationally `[aspirational]`.
- *Hypoxia.* Declining near-bottom oxygen off Oregon during upwelling has been
  documented from gliders `[demonstrated: Pierce et al. 2012; Adams et al. 2013, via
  Rudnick 2016]`. CUGN oxygen anomalies on isopycnals track source-water changes
  `[demonstrated: cugn El Nino 2026 report]`. Network-wide hypoxia early warning is
  `[aspirational]`.
- *Harmful algal blooms.* Glider chlorophyll and nitrate with satellite imagery to
  identify and eventually predict HABs `[aspirational]`.
- *Teleconnections.* El Nino's coastal expression was first observed by gliders in
  2009-10 `[demonstrated: Todd et al. 2011a]`; the Southern California Temperature
  Index from Line 90.0 tracks the Oceanic Nino Index `[demonstrated: Rudnick et al.
  2017]`. Resolving such events nationally requires sustained sampling `[planned]`.

**Basic research.** Mixed-layer depth, boundary-current position and speed, upwelling
structure, cross-shore heat flux, and their annual cycles and trends, for coasts where
these have been seen only from ship sections and sporadic glider campaigns
`[aspirational]`. The first comprehensive biogeochemical dataset (oxygen, pH,
chlorophyll) for most U.S. coastal waters `[aspirational]`.

**Regional ocean models.** Glider data are assimilated in several ROMS configurations
off California today; where Argo is sparse, a sustained glider line is the dominant
in situ constraint `[demonstrated: Todd et al. 2011b; Rudnick 2016 sec. 7]`. BOONUS
would extend that constraint to the whole coastline and to ecological forecasting via
biogeochemical variables `[aspirational]`.

**Why now.** Twenty years of glider operations have retired the technology risk;
hardware, software, calibration, piloting and small-boat logistics are mature
`[demonstrated: Rudnick 2016; Rudnick et al. 2017]`. The remaining risk is industrial:
no existing program, alone or combined, can build and sustain 100+ gliders `[planned:
this is the problem BOONUS sets out to solve]`.

## 3. CUGN, the proven core

The California Underwater Glider Network is the world's longest sustained glider
network `[demonstrated: Rudnick et al. 2017]` and the template for every BOONUS line.

| Line | Anchor | Length | Occupied |
|---|---|---|---|
| 90.0 | Dana Point, through the Southern California Bight | 530 km | since 2006 |
| 80.0 | Point Conception | 365 km | since 2006 |
| 66.7 | Monterey Bay | 400 km | since 2007 |
| 56.7 | Northern California | ~300 km | since ~2016 (data in the climatology from 2020) |
| alongshore | ~220 km, southern California | 220 km | data in the climatology from 2019 |

Line numbers are CalCOFI designations. Canonical label for the northern line is 56.7
(the `cugn` package uses `'56.0'`; map with `cugn.erddap.LINE_LONG`).

**Operations `[demonstrated]`.** Spray gliders; missions of ~100 days and >2000 km with
4-6 sections each; 20-30 profiles per day; sensors run on ascent only; Sea-Bird 41CP
pumped CTD, Sontek Argonaut or Nortek AD2CP ADCP, Seapoint fluorometer; dissolved oxygen
standard in recent years (in the climatology from 2017). Two gliders per line, one at
sea and one in the lab. Since 2009 the network achieved 97% of the ideal 3 glider-days
per day on three lines (Rudnick et al. 2017, Fig. 2.1). Depth-average velocity is
accurate to 0.01 m/s and gives absolutely referenced geostrophic velocity.

**Record `[demonstrated]`.** As of 2015: more than 80,000 profiles, 8,700 glider-days,
182,000 km (Rudnick 2016). As of late 2016: more than 95,000 dives, 10,000 glider-days,
210,000 km (Rudnick et al. 2017). Gliders produced 57 times as many profiles as CalCOFI
stations on Line 90.0 in 2010-12. Use these numbers until current totals are computed.

**Science `[demonstrated]`.** Deep poleward flow offshore of the Santa Rosa Ridge, found
only because gliders measure absolute velocity (Davis et al. 2008); Rossby-wave
modulation of the undercurrent (Todd et al. 2011b); the 2009-10 El Nino (Todd et al.
2011a); the Blob (Zaba & Rudnick 2016); the climatology of mean, annual cycle and
anomaly (Rudnick et al. 2017), with a 90-degree phase change in the temperature annual
cycle between 10 m and 50 m and spring-upwelling shoaling on all lines.

**Data access.**

- SprayData ERDDAP, `https://spraydata.ucsd.edu/erddap/tabledap`: delayed-mode,
  quality-controlled, 10 m binned line data (`binnedCUGN66`, ...), updated per mission.
- IOOS Glider DAC ERDDAP, `https://gliders.ioos.us/erddap/tabledap`: real-time
  Level-2 profiles with QARTOD flags for the mission at sea.
- Local (this machine): `$OS_SPRAY/CUGN/` (`CUGN_line_*.nc`, `CUGN_potential_line_*.nc`,
  grid tables; ~3 GB) and `$OS_CCS/` (ONI, SCTI, CUTI/BEUTI, tide gauges). Code:
  `/home/xavier/Oceanography/python/cugn` (`erddap.py`, `indices.py`, `oisst.py`,
  `climatology.py`).

**Products.** The CUGN climatology (Rudnick et al. 2017; 2026 beta with long-term
2007-2014 and short-term 2017-2025 baselines, 5 km by 10 m by 10 day grids); the
Southern California Temperature Index and El Nino page
(`https://spraydata.ucsd.edu/products/el-nino/`); and the monthly Line 66.7 El Nino
2026 report, newsletter and one-pager in `cugn/reports/El_Nino_2026/`, which is the
exemplar of a BOONUS-style actionable product.

## 4. Landscape: how BOONUS relates to existing programs

- **IOOS** (U.S. Integrated Ocean Observing System): 11 certified Regional
  Associations; runs the national Glider DAC; supports 365-day glider lines on the
  West Coast and Alaska and 40+ hurricane-glider missions per season in the Gulf,
  Caribbean, Southeast and Mid-Atlantic; its 2021 climate report's recommendation #2
  is to recapitalize profiling gliders. **BOONUS is organized and funded independently
  of IOOS; its data will be open and delivered to the IOOS Glider DAC and GTS, as
  CUGN's are today.** Do not describe BOONUS as an IOOS program or as a competitor.
- **NOAA** has funded most of CUGN for nearly 20 years; BOONUS data would constrain
  the regional models that inform NOAA Fisheries and forecasting. Partnership on data
  products is the working assumption (Section 1, Funding).
- **BOON** (OceanGliders Boundary Ocean Observing Network, white paper revised March
  2018, Rudnick first author, 32 international members): the global network of
  regional boundary-current glider networks, positioned as the coastal complement to
  Argo and OceanSITES. Dormant to our knowledge; BOONUS inherits the name and lineage
  only.
- **UG2** (Underwater Glider User Group): the international glider community; a
  stakeholder and source of collaborators.
- **Argo / BGC-Argo**: global open-ocean floats at ~300 km spacing; sparse on shelves
  and in boundary currents, which is the gap gliders fill.
- **CalCOFI**: quarterly ship surveys since 1951 (75 stations, 6 lines); the gold
  standard CUGN was validated against and the origin of the line numbering.
- **OOI** Endurance Array glider lines off Oregon and Washington (since 2014; one Oregon
  line since 2006).

## 5. Models and the AI-driven component

- **ROMS** (Regional Ocean Modeling System): the assimilative regional models, several
  km resolution over ~1000 km coastal domains; used for fisheries, search and rescue,
  and weather inputs; CUGN is assimilated in several California configurations
  `[demonstrated]`. Use "ROMS" for the software and "regional ocean models" for the
  class; never "ROMs".
- **ECCO** (NASA Estimating the Circulation and Climate of the Ocean): global state
  estimate providing boundary conditions `[planned]`.
- **Darwin**: MIT ecosystem model for biogeochemistry and ecological forecasting
  `[planned]`.
- **AI-driven component** `[planned; scope TBD]`: some combination of (a) adaptive
  piloting and fleet control, (b) learned components inside the assimilation system,
  and (c) anomaly and event detection on the real-time data stream. Nominal lead Matt
  Mazloff. Described in the pitch as continuously ingesting glider data to anticipate
  marine heat waves and track hurricanes and atmospheric rivers `[aspirational]`.
- Three-day operational forecasts fed by BOONUS data `[aspirational]`.

## 6. Style rules for Claude-written BOONUS documents

1. **Lead with demonstrated results**, above all CUGN's 20-year record, then state what
   BOONUS adds. Rudnick (2016) concludes that every prior attempt at a sustained
   national glider program failed and blames an "excess of hype"; write so that
   BOONUS documents cannot be read that way.
2. **Quantify.** Every claim of capability carries a number and a source, or a tag.
3. **Tag claims in drafts** with the four tags; strip tags only in final copy for
   external readers, and only after JXP has seen the tagged version.
4. **Do not reuse pitch headings** or superlatives from the private one-pager and
   multi-pager ("The Wow", "Irrefutable"). Paraphrase substance only.
5. **Name only** JXP and Dan Rudnick (and Matt Mazloff as nominal AI lead). No
   recipients, funders or foundations.
6. **Use canonical values** from Section 1; if a source disagrees, cite this file.
7. **Terminology:** "for the United States"; BOONUS; ROMS as defined in Section 5;
   "gliders" not "UAVs" or "drones"; "marine heat wave"; SI units with depths in m,
   distances in km, speeds in m/s.
8. **Citations:** keep a `sources.md` and `sources.bib` beside any report, in the
   `cugn/reports/El_Nino_2026` form; tag generated code docstrings "Generated by JXP
   and Claude".
9. **Calculations** go in Python scripts on disk (`ocean14` environment), never only
   in chat.
10. **Privacy:** the PDFs in `context/` never enter GitHub; do not paste their text
    into tracked files beyond the public-source digests.

## 7. Open decisions

| Decision | Status |
|---|---|
| Line locations and count | TBD; observing-system design experiments with regional models, from the CUGN lines |
| Sensor suite, core vs optional; pH readiness; nitrate | TBD; multi-pager list is the placeholder |
| Platform: Spray only or multi-vendor | TBD; Spray default |
| Team roster and institutions | TBD; JXP and Rudnick only |
| Funding and cost models | TBD; see Section 1 |
| AI-driven component scope | TBD; see Section 5 |
| Geographic reach beyond the contiguous coasts (Alaska, Hawaii, territories, Great Lakes) | TBD |
| Data policy details (latency, QC levels, archive host, API) | TBD |
| Whether the coverage-gap estimate (<10%) gets computed in this repository | Not requested |

## 8. Sources and digests

Private PDFs in `context/` (gitignored; see `context/README.md`) and their public
digests in `context/sources/`:

| Source | File | Digest |
|---|---|---|
| Rudnick et al., BOON white paper, rev. 26 Mar 2018 | `boon.pdf` | `sources/boon2018.md` |
| IOOS Association, *Detecting the Coastal Climate Signal*, July 2021 | `IOOS_CoastalClimateSignal_Final.pdf` | `sources/ioos2021.md` |
| Rudnick, *Ocean Research Enabled by Underwater Gliders*, Annu. Rev. Mar. Sci. 8, 2016 | `rudnick-2016-...pdf` | `sources/rudnick2016.md` |
| Rudnick, Zaba, Todd & Davis, CUGN climatology, Prog. Oceanogr. 154, 2017 | `rudnick2017.pdf` | `sources/rudnick2017.md` |
| BOONUS one-pager (JXP, private) | `BOONUS_one_pager.pdf` | none; folded into this brief |
| BOONUS multi-pager v0.4, 2026-04-22 (JXP, private) | `BOONUS_multi_pager.pdf` | none; folded into this brief |

Other on-disk context: `/home/xavier/Oceanography/python/cugn-climatology/context/`
(`context_cugn_2026beta.md`, `initial_exploration.md`, `file_inventory.csv`) and the
`cugn` repository. Web: `https://spraydata.ucsd.edu/projects/CUGN/`,
`https://ioos.github.io/glider-dac/`.

## 9. Glossary

| Term | Meaning |
|---|---|
| BOONUS | Boundary Ocean Observing Network for the United States (this project) |
| CUGN | California Underwater Glider Network, Scripps, since 2005 |
| BOON | OceanGliders Boundary Ocean Observing Network, 2018, dormant |
| UG2 | Underwater Glider User Group |
| IOOS / RA | U.S. Integrated Ocean Observing System / one of its 11 Regional Associations |
| DAC | (IOOS Glider) Data Assembly Center |
| GTS | WMO Global Telecommunication System, real-time data exchange |
| EEZ | Exclusive Economic Zone, 200 nautical miles (~370 km) from the coast |
| ROMS | Regional Ocean Modeling System |
| ECCO | Estimating the Circulation and Climate of the Ocean (NASA) |
| Darwin | MIT marine ecosystem model |
| MHW | Marine heat wave |
| HAB | Harmful algal bloom |
| CalCOFI | California Cooperative Oceanic Fisheries Investigations, since 1949/1951 |
| SCTI | Southern California Temperature Index: Line 90.0, 50 m, inshore 200 km, 3-month running mean |
| ONI | Oceanic Nino Index (NOAA CPC) |
| CUTI / BEUTI | Coastal Upwelling / Biologically Effective Upwelling Transport Index (Jacox et al. 2018) |
| TEOS-10 | Thermodynamic Equation of Seawater 2010 (`gsw`); the 2017 climatology used EOS-80 |
| QARTOD | IOOS Quality Assurance / Quality Control of Real-Time Oceanographic Data |
| OSSE | Observing-system simulation (design) experiment |

## 10. Change log

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-09-21 | JXP and Claude | First release, from three Q&A rounds in `claude_prompts/context_prompts.md` |
