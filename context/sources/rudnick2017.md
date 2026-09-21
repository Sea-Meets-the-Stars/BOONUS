# Digest: Rudnick, Zaba, Todd & Davis (2017), A climatology of the California Current System from a network of underwater gliders

**Citation.** Rudnick, D. L., K. D. Zaba, R. E. Todd and R. E. Davis (2017), "A
climatology of the California Current System from a network of underwater gliders,"
*Progress in Oceanography* 154, 64-106, doi:10.1016/j.pocean.2017.03.002.
**Local file.** `context/rudnick2017.pdf` (private, copyrighted; gitignored). A fuller
methods digest, written for the climatology port, is section 13 of
`/home/xavier/Oceanography/python/cugn-climatology/context/context_cugn_2026beta.md`;
parts of it are reused here.

## What it is

The methodology and results paper for the CUGN climatology: how a decade of Spray
glider sections on CalCOFI lines 66.7, 80.0 and 90.0 is turned into gridded mean,
annual-cycle and anomaly fields of temperature, salinity and velocity, presented as an
atlas by line, followed by a synthesis of the 2009-10 El Nino, 2010-11 La Nina, the
2014-15 warm anomaly and the 2015-16 El Nino. It is the specification of record for
CUGN operations and for the climatology products at spraydata.ucsd.edu.

## Key facts (page)

- CUGN is "the world's longest sustained glider network, to our knowledge"; since 2006
  on lines 66.7, 80.0, 90.0; gliders dive surface to 500 m, 3 h and 3 km per cycle;
  sections 350-500 km take 2-3 weeks; >10,000 glider-days, >210,000 km, >95,000 dives
  (abstract, p. 64; p. 65).
- Missions ~100 days and >2000 km at ~0.25 m/s; 20-30 profiles per day; pitch 17
  degrees, path angle ~20 degrees (pp. 65-66).
- Payload: Sea-Bird 41CP pumped CTD sampled every 8 s (~0.8 m resolution), run on ascent
  only, off at 2 m, tributyltin antifouling; Sontek Argonaut 750 kHz ADCP in 4 m bins,
  some Nortek AD2CP 1 MHz in 2 m bins from 2013; Seapoint chlorophyll fluorometer;
  acoustic backscatter as a zooplankton proxy. Backscatter and fluorescence were not in
  this climatology but "may be added in the future" (pp. 66-67).
- QC: automatic then manual, profile by profile after recovery; active-mission data
  included without manual QC; 10 m bins from 10 to 500 m; 5 m excluded for bubbles
  (pp. 66-67).
- Depth-average velocity by dead reckoning, accurate to 0.01 m/s; references both
  geostrophic shear and ADCP shear to give absolute velocity (p. 67).
- Operations model: one glider on each line at all times, achieved by deploying a fresh
  glider as one is recovered, so "two gliders to be committed to each line, with one
  glider in the lab being refurbished"; more than two per line "makes operations more
  manageable"; "a critical mass of personnel and equipment is essential". Performance
  metric glider-days/day; 97% of the ideal 3 glider-days/day since 2009 (Fig. 2.1,
  pp. 67-68).
- 57 times as many glider profiles as CalCOFI stations on line 90.0 in 2010-12 (p. 68).
- Methods: wavelengths >30 km resolved (spectral break at 0.03 cpkm); annual cycle by
  weighted least squares (constant plus three harmonics, 365.25 d period, 5 km
  intervals, Gaussian window L = 15 km, base years 2007-2013, 2008-2013 for 66.7);
  anomaly by objective map with Gaussian covariance of 60 d and 30 km, noise-to-signal
  0.1, on a 10 m by 5 km by 10 d grid, masked where error/signal > 0.3 (pp. 69-72).
- Results: poleward California Undercurrent inshore, equatorward California Current
  offshore; deep poleward flow offshore of the Santa Rosa Ridge revealed only by
  absolute velocity; annual cycle of temperature nearly 90 degrees out of phase between
  10 m and 50 m (surface heat flux vs. spring upwelling); offshore-propagating annual
  isopycnal displacement consistent with Rossby waves; undercurrent maximum in summer
  with a weaker winter maximum (pp. 72-86, 100).
- Events: warming began concurrently on all three lines in early 2014, strongest at the
  surface and nearshore, with freshening and anomalous downwelling; the 2015-16 El Nino
  penetrated deeper and showed anomalous poleward advection (isopycnal salinity) on
  line 90.0 only; the 2009-10 El Nino was moderate and mainly felt on line 90.0
  (pp. 90-95).
- Indices: the SoCal Temperature Index (line 90.0, 50 m, inshore 200 km, 3-month
  running mean) tracks the ONI except during the 2014-15 anomaly; 10 m indices on all
  lines; isopycnal salinity on 26 kg/m3 over the inshore 100 km as an advection index;
  depth of the 26 kg/m3 isopycnal over the inshore 50 km as an upwelling index
  (Jacox et al. 2016) (pp. 95-100).
- Base-year choice (2007-2013, before the 2014 anomaly) is deliberate and will change
  in future versions (pp. 101-102).
- Distribution: figures via a menu-driven interface and CF-compliant NetCDF on regular
  grids at spraydata.ucsd.edu, updated regularly (p. 103).
- Funding: NOAA Climate Observation Division and NOAA IOOS grants (p. 104).

## Quotable lines

- "Autonomous underwater gliders offer the possibility of sustained observation of the
  coastal ocean." (abstract)
- "If there is any overriding take-home message, it is that of the diversity of
  responses along the three lines to the major climate events of the past decade."
  (p. 90)
- "With better observations and models, the lesson is that no single mode or index
  will do." (p. 95)
- "In sustaining these glider lines for a decade, our goal has been to establish a new
  approach for regional ocean observation. A series of networks like the CUGN in
  boundary currents around the world is a conceivable future for gliders in global
  ocean observing." (p. 104)

## Differs from canonical

- Three lines; canonical CUGN is 4 standard lines plus 1 alongshore (the paper predates
  56.7 and the alongshore line).
- Physical variables only; the 2026 beta climatology adds chlorophyll, backscatter and
  dissolved oxygen.
- Two gliders per line is the paper's practice; canonical BOONUS adopts "at least 2
  per line" plus an opportunity pool, and JXP's 10-glider minimum for CUGN.

## Relevance to BOONUS

The single best source for what a BOONUS line is: the operating envelope, payload, QC,
two-gliders-per-line staffing model, the glider-days/day performance metric, and the
demonstrated products (climatology, indices, event analyses). Its closing paragraph is
the direct intellectual ancestor of BOON and BOONUS. Its indices (SCTI, 10 m indices,
isopycnal salinity, 26 kg/m3 depth) are ready-made templates for BOONUS metrics and
diagnostics, and its base-year discussion is the caution to carry into any BOONUS
anomaly product.
