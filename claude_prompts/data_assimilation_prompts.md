# Data Assimilation Prompts

## Goals

We will generate a report that describes the state of the art in data assimilation (DA)
for oceanography, with emphasis on where and how AI is being adopted in DA. The report
is written to educate JXP and will be shared with Matt Mazloff. It is a review, not a
BOONUS pitch; BOONUS-specific documents will follow separately.

## Context

- `context/initial_context_for_claude.md` (v0.1): the canonical BOONUS brief. Read it
  before writing anything. Its Section 5 fixes what the report must respect: ROMS 4D-Var
  assimilation of CUGN is `[demonstrated]`; the AI-driven component (nominal lead Matt
  Mazloff) is `[planned; scope TBD]`.
- `context/da/README.md`: the anchor PDFs for this report (verified citations, DOIs or
  arXiv IDs, access status). The PDFs themselves are private and gitignored
  (`context/**/*.pdf`).
- `claude_prompts/context_prompts.md`, `## Q&A / ### Data assimilation`: the history of
  this effort, Round 1 (DA1-DA19) and Round 2 (DA20-DA32) with JXP's answers, plus the
  dated log entries for DA prompts #1-#3. That text stays where it is; do not move it.
  The decisions it produced are summarized below so a new session need not reread it.
- Exemplar for report conventions: `/home/xavier/Oceanography/python/cugn/reports/El_Nino_2026/`
  (`/Users/xavier/Oceanography/python/cugn/reports/El_Nino_2026/` on the Mac):
  `sources.md` + `sources.bib` with shared BibTeX keys, DOI verification by
  `curl -sI https://doi.org/<doi>` with access dates, `figs/`, `scripts/`, and a
  link-checking script.

## Decisions carried over (DA1-DA32, fixed 2026-09-22)

**Purpose and readers.** Educate JXP; shared with Matt Mazloff. Register: a technical
briefing, not a textbook and not a pitch; style rule 1 (no hype) applies. Authors may be
cited freely (style rule 5 concerns prospective partners, not citations).

**Deliverables and location.** `reports/data_assimilation/` holding `da_ai_review.md`
(versioned header `v0.1, date, JXP and Claude`, change-log table), `outline.md`,
`reading_list.md`, `sources.md`, `sources.bib`, `figs/`, `scripts/` (including
`check_sources.py`, which re-verifies every DOI and URL before delivery). Markdown,
10-15 pages, one-page executive summary at the top.

**Sequence.** Next step is `outline.md` plus an annotated `reading_list.md` (40-60
candidate references, one-line reason and verification status each) for JXP's approval;
then the v0.1 draft. Afterwards: a digest in `context/sources/` and a pointer in the
brief (v0.2, Section 5). Model: Claude Fable throughout.

**Scope.** Roughly 1/3 global DA (ECMWF ORAS/OCEAN5, Mercator/GLORYS, NOAA RTOFS, Navy
HYCOM/NCODA, JEDI/SOCA, ECCO) and 2/3 regional and coastal. Reanalysis/state estimation
and operational forecasting both, clearly split. Physics plus a full biogeochemical (BGC)
section. Classical methods (OI, 3D/4D-Var, EnKF, hybrids) in brief; AI literature
concentrated on 2019-2026. One NWP section (~2 pages) as the leading indicator, one
paragraph per family (emulators; learned DA; end-to-end observation-to-forecast;
generative DA), two or three exemplars each. The report stops at the review: no
"implications for BOONUS" section, and the "AI makes gliders more valuable" thesis is
left out for now.

**AI taxonomy.** Organized by where ML enters the DA pipeline: (1) emulators/surrogates
of the ocean model; (2) ML inside classical DA (learned B, bias correction, observation
operators, inflation/localization, adjoint surrogates); (3) ML replacing DA (end-to-end
mapping, generative reconstruction, neural interpolation such as SSH mapping); (4) ML
around DA (QC, downscaling, anomaly detection, adaptive sampling and OSSE design). Every
AI approach carries a maturity tag (`idealized`, `realistic hindcast`, `pre-operational`,
`operational`) and a verification note (withheld observations vs. the reanalysis it was
trained on); the trained-on-reanalysis circularity is the central caveat.

**Systems depth.** A paragraph for every system that assimilates or has assimilated
gliders in U.S. waters (UCSC California Current ROMS 4D-Var, Scripps California Current
state estimate, Rutgers doppio, NOAA NOS OFS including West Coast OFS, the ocean
component of NOAA hurricane models); a table row for the rest (global systems above;
Bluelink and Copernicus regional systems as comparators). Ocean ML to feature: Samudra
and the GLORYS-trained emulators (Xihe, WenHai, GLONET); 4DVarNet and the SSH-mapping
data challenges; ML bias correction and learned parameterizations; ML QC and anomaly
detection on Argo and glider streams. All are candidates to verify; the reading list is
where JXP adds or strikes.

**Glider-specific DA section.** Profile vs. binned assimilation, depth-average velocity
as an observation, representativeness error, observation-impact studies and OSEs/OSSEs
(IOOS hurricane gliders, California Current ROMS).

**Mathematics and apparatus.** A compact boxed primer marked "skippable for DA
specialists": linear Gaussian update and gain, 3D/4D-Var cost function, ensemble Kalman
gain with why localization and inflation are needed, plus a notation table; the rest in
prose. Analogies to inference JXP knows (OI as GP regression/kriging, 4D-Var as MAP with
a dynamical prior, EnKF as Monte Carlo Kalman filter, ECCO as a long-window smoother)
used sparingly and only where exact. A DA glossary and a closing "questions for Matt"
appendix.

**Figures (v0.1 schematic only, no CUGN data).** (1) taxonomy of the four ML entry
points over a DA cycle (Mermaid); (2) 2018-2026 timeline of AI-in-DA milestones, NWP and
ocean tracks (matplotlib, script in `scripts/`, PNG in `figs/`, run in `ocean14`);
(3) one assimilation cycle marking where glider profiles and depth-average velocity
enter and where representativeness error arises (Mermaid); (4) a table of operational
systems. Optional later: CUGN profile density against a ROMS grid from `$OS_SPRAY/CUGN`.

**Citations.** 40-60 references; author-year in text, BibTeX keys shared between
`sources.md` and `sources.bib`; every DOI verified with `curl -sI https://doi.org/<doi>`
and the access date recorded; arXiv preprints allowed, flagged `preprint`; grey
literature (ECMWF memoranda and newsletters, NOAA technical reports, JEDI/SOCA docs,
GitHub READMEs) allowed with URL and access date, flagged `grey`.

**Access.** `.claude/settings.json` (BOONUS only) allows WebSearch and WebFetch for the
domain list in DA20 (preprint servers and Crossref, publishers, ML venues, operational
centers). Several publisher hosts still return 403 to automated fetchers; anchor PDFs
live in `context/da/` (see its README). Fetches that are blocked fall back to `curl`.

## Prompts

### Outline and reading list

<!-- JXP will write the prompts for this section. -->

## Q&A

## Logs
