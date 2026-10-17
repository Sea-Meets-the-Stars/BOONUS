# Outline: data assimilation in oceanography and where AI enters it

**Prompt #1 in `claude_prompts/data_assimilation_prompts.md`, 2026-09-22, Claude Fable;
reviewed by JXP the same day (Q&A DA33-DA39, no inline edits), updated in the 2026-09-22
session that executed prompts #2-#3 and again on 2026-09-23 (prompt #3 completed, Q&A
DA40-DA44). Prompt numbers below follow the numbering JXP fixed under DA41: Draft 4-6,
Figures 7, Verification 8-9, Follow-through 10.**
Section list for `da_ai_review.md` with a target length per section, the four figures
placed where they land, and for each section one or two sentences on what it argues and
the keys that carry it. Keys are those of `sources.bib` (identical to `reading_list.md`);
entries marked optional there are in parentheses here. Page counts assume about 500
words per Markdown page; the reference list is not counted.

**Target: 14.0 pages, ceiling relaxed** (DA38: "It is ok if the report is longer. Use
your judgement and emphasize clarity over brevity"). The per-section targets below stand
as the plan; a section may run over where a derivation or an example needs the room, and
the verification pass in prompt #8 checks the total against 10-15 pages as a guide rather
than a limit, trimming only repetition. Ocean-system content splits roughly 1/3 global
(Section 4, 1.25 pp.) to 2/3 regional and coastal (Sections 5, 8, 9 and the regional
parts of 7, about 4.5 pp.), as decided. No "implications for BOONUS" section; the report
stops at the review.

| # | Section | Pages | Figures / tables |
|---|---|---|---|
| 0 | Executive summary | 1.0 | |
| 1 | Introduction and scope | 0.25 | |
| 2 | Box: DA primer (skippable for DA specialists) | 1.0 | notation table |
| 3 | Classical methods in brief | 0.75 | |
| 4 | Global systems: reanalysis and state estimation vs operational forecasting | 1.25 | Table (Fig. 4), global rows |
| 5 | Regional and coastal systems | 2.0 | Table (Fig. 4), regional rows |
| 6 | AI in numerical weather prediction: the leading indicator | 2.0 | Fig. 2 (timeline) |
| 7 | AI in ocean DA, by where ML enters the pipeline | 2.5 | Fig. 1 (taxonomy) |
| 8 | Biogeochemical DA | 1.0 | |
| 9 | Gliders in DA | 1.25 | Fig. 3 (assimilation cycle) |
| 10 | Glossary | 0.5 | |
| 11 | Questions for Matt | 0.5 | |
| | **Total** | **14.0** | |

---

## 0. Executive summary (1 page; written last, prompt #6)

One page for a reader who stops here: what operational ocean DA is today (two method
families, a handful of global systems, ROMS 4D-Var and its relatives on U.S. coasts);
that AI has entered NWP first as emulators and is now entering the assimilation step;
that in the ocean the emulators are trained on reanalyses that are themselves DA
products, so their verification against withheld observations is the test that
matters; and what remains open for BGC and for gliders specifically. No BOONUS pitch.
Carries: none of its own; it cites the section anchors.

## 1. Introduction and scope (0.25 page)

States the purpose (educate JXP; shared with Matt Mazloff), the scope split (global
background, regional and coastal depth; reanalysis vs forecasting kept apart; physics
plus BGC), the 2019-2026 window for the AI literature, the maturity tags and the
verification note that every AI approach carries, and the citation conventions
(`preprint`, `grey`). Carries: `moore2019synthesis` (the field's own scope statement).

## 2. Box: DA primer, skippable for DA specialists (1 page, incl. notation table)

Fixed vocabulary for everything that follows: state x, background x^b, observations y,
operator H, covariances B and R; the linear Gaussian update and gain; the 3D-Var and
strong/weak-constraint 4D-Var cost functions and why the adjoint is needed; the
ensemble Kalman gain and why finite ensembles need localization and inflation. The
analogies used sparingly and only where exact: OI as GP regression/kriging, 4D-Var as
MAP with a dynamical prior, EnKF as a Monte Carlo Kalman filter, ECCO as a long-window
smoother. Argues nothing; defines what "learning B", "learning H" and "replacing the
adjoint" mean so Section 7 can use them. Carries: `carrassi2018data`,
`evensen2003ensemble`, `bannister2017review`, `geer2021learning` (cost = loss, adjoint =
backpropagation).

## 3. Classical methods in brief (0.75 page)

OI, 3D-Var (FGAT), 4D-Var (incremental, TLM/adjoint), EnKF/EnOI/SEEK, and the
ensemble-variational hybrids, each in a few sentences with the operational trade-off
(cost, need for an adjoint, flow dependence of B). Argues that the two families
persist because each fails differently, that hybrids are the convergence point in NWP
and are arriving in the ocean, and that model bias and representativeness error are
unsolved in both. Carries: `moore2019synthesis`, `carrassi2018data`,
`bannister2017review`, `edwards2015regional`.

## 4. Global systems (1.25 pages; global rows of the systems table, Fig. 4)

Two subsections make the split explicit. *Reanalysis and state estimation:* sequential
reanalyses (ORAS5, GLORYS12) vs the ECCO adjoint smoother, what each conserves and
what each is for. *Operational forecasting:* Mercator GLO12, ECMWF OCEAN5, NOAA RTOFS
(HYCOM/NCODA lineage), the Navy system, and JEDI/SOCA as the U.S. next step. Argues
that GLORYS12 matters twice for this report: as an operational product and as the
training set of the emulators in Section 7. Carries: `stammer2016ocean`,
`zuo2019ecmwf`, `lellouche2018recent`, `lellouche2021copernicus`,
`cummings2013variational`, `forget2015ecco`, `martin2015status`, `rtofs2026ncep`,
`soca2026jcsda`.

## 5. Regional and coastal systems (2 pages; regional rows of Fig. 4)

A paragraph each for the systems that assimilate or have assimilated gliders in U.S.
waters: the UCSC California Current ROMS 4D-Var (reanalysis and near-real-time); the
Scripps California Current state estimate (MITgcm adjoint) and its comparison with CUGN;
Rutgers doppio in the Mid-Atlantic Bight with its observation-impact accounting; NOAA
NOS operational forecast systems including WCOFS; and the ocean component of NOAA's
hurricane models (HWRF-HYCOM, then HAFS with MOM6 and Marine JEDI). Table rows for the
rest: the global systems of Section 4, Bluelink and Copernicus regional systems as
boundary-current comparators, with method, resolution, cycle, assimilated observations
and a source per row. Argues that regional systems are where in situ profiles carry the
most weight and where open boundaries, forcing errors and shelf representativeness
dominate the error budget. Carries: `edwards2015regional`, `moore2011roms`,
`neveu2016historical`, `todd2011poleward`, `zaba2018annual`, `levin2020observation`,
`wcofs2026coops`, `kim2024ocean`, `dong2017impact`, (`liu2023impact`),
`martin2015status` (comparator rows).

## 6. AI in numerical weather prediction: the leading indicator (2 pages; Fig. 2)

One paragraph per family, two or three exemplars each, every one with its maturity tag
and verification note. *Emulators:* Pangu-Weather, GraphCast, AIFS (operational since
Feb 2025), GenCast for the probabilistic step. *Learned components inside DA:*
model-error correction in weak-constraint 4D-Var (Bonavita and Laloyaux 2020: an ANN
trained on analysis increments, then run inside cycled 4D-Var at the operational IFS
configuration and verified against radiosondes and GPS-RO, the one exemplar in this
section whose assimilation experiments are scored against observations rather than a
reanalysis), neural tangent-linear/adjoint models. *End-to-end
observation-to-forecast:* Aardvark Weather, GraphDOP (trained on observations only).
*Generative DA:* score-based/diffusion assimilation of sparse stations at km scale;
FuXi-DA as learned assimilation into an ML model, tagged "realistic hindcast, offline
and non-cycled, verified against ERA5", with the Methods data split (training June
2022-May 2023, validation June-July 2023, test August-December 2023) and one clause on
the Results section stating it inconsistently (DA43). Argues that NWP shows the
sequence the ocean is likely to follow (emulate the model, then learn pieces of the
assimilation, then learn the whole map), and that the verification question (against
ERA5 vs against observations) was raised there first. Fig. 2, the
2018-2026 timeline with an NWP and an ocean track, sits here and is referred to again
in Section 7. Carries: `bi2023accurate`, `lam2023learning`, `lang2024aifs`,
(`ecmwf2025aifs`), `price2024probabilistic`, `bonavita2020machine`,
(`hatfield2021building`), `xu2025fuxida`, `allen2025endtoend`, (`alexe2024graphdop`),
`manshausen2025generative`, `geer2021learning`, `cheng2023machine`.

## 7. AI in ocean DA, by where ML enters the pipeline (2.5 pages; Fig. 1)

Opens with Fig. 1 (Mermaid: the four entry points laid over one DA cycle) and states
the central caveat once: the ocean emulators are trained on GLORYS12 or on a model run,
both of which are DA or model products with a poorly observed subsurface, so skill is
only established against withheld observations (the IV-TT Class 4 sets) and not against
the training reanalysis. Later paragraphs refer back to it. The XiHe training/test
overlap is stated as implied but not explicit: the paper gives the GLORYS12 span as
1993-2020 and the training set as "25-year", which would end in 2017 or 2018, and
evaluates on 2019-2020 (DA34; PDF checked 2026-09-22).

- **7.1 Emulators and surrogates (0.75 page).** Samudra (emulator of OM4, verified
  against the parent model), XiHe, WenHai and GLONET (GLORYS12-trained, verified
  against Class 4 observations; GLONET pre-operational at Mercator), a regional
  emulator (OceanNet, Gulf Stream), and Samudra 2. Argues that the global emulators
  now match or beat the operational systems they learned from on 1-10 day Class 4
  metrics while inheriting the reanalysis's deficiencies, and that regional emulators
  are few. Carries: `dheeshjith2025samudra`, `wang2024xihe`, `cui2025forecasting`,
  `elaouni2025glonet`, `chattopadhyay2024oceannet`, (`yuan2026samudra2`),
  `lellouche2021copernicus`.
- **7.2 ML inside classical DA (0.5 page).** Learned bias/model-error correction from
  DA increments (sea ice-ocean at GFDL as the nearest ocean case; ECMWF pattern from
  Section 6), the adjoint-surrogate idea, and the near absence of published ocean work
  on learned B or learned observation operators (a question for Matt). One sentence on
  learned sub-grid parameterizations as the boundary case: they change the model, not
  the assimilation, and are named only so the DA30 list is honoured (DA36c). Carries:
  `gregory2023deep`, `bonavita2020machine`, (`hatfield2021building`),
  `geer2021learning`, (`gloege2022improved`), (`zanna2020data`, boundary case).
- **7.3 ML replacing DA (0.75 page).** 4DVarNet from toy systems to the SSH-mapping
  data challenges (OSSE on NATL60 vs OSE on real altimetry), deep-learning SSH
  interpolation verified on withheld tracks; what "verified" means in each case.
  Carries: `fablet2021learning`, `beauchamp2023fourdvarnet`,
  (`martin2023synthesizing`), `oceandatachallenges2026`, `cheng2023machine`.
- **7.4 ML around DA (0.5 page).** ML quality control of profile streams (Argo), and
  the thinner literature on anomaly detection and adaptive sampling, stated as such;
  neural estimation of derived BGC variables is cross-referenced to Section 8.
  Carries: `sugiura2020machine`, (`bittig2018canyonb`), `moore2018reduced` (adjoint
  observing-system design as the classical counterpart).

## 8. Biogeochemical DA (1 page)

Physics-BGC coupling and why physical assimilation can disrupt the ecosystem state;
what is assimilated today (ocean colour chlorophyll, BGC-Argo O2, nitrate, pH) and the
non-Gaussian, model-dependent nature of BGC increments; the two routes in the
California Current and Southern Ocean (ROMS 4D-Var with two ecosystem models; B-SOSE and
ECCO-Darwin adjoint state estimates); OSSEs valuing in situ BGC profiles; and where ML
is being tried (correcting model-data misfit, neural estimation of nutrients and
carbonate variables from T, S, O2). Argues that BGC DA is the least mature part of the
field and the one where in situ subsurface data are scarcest. Carries:
`fennel2019advancing`, `mattern2017data`, `verdy2017data`, `carroll2020ecco`,
(`ford2021assimilating`), (`bittig2018canyonb`), (`gloege2022improved`).

## 9. Gliders in DA (1.25 pages; Fig. 3)

Fig. 3 (Mermaid: one assimilation cycle marking where glider T/S profiles and
depth-average velocity enter and where representativeness error arises). Profile vs
binned assimilation and the treatment of a slanted, 3-hour dive as an observation;
depth-average velocity as an observation type; representativeness error for a profile
in a several-km grid; observation-impact and OSE/OSSE results (California Current ROMS
and the Scripps state estimate, doppio's per-platform impacts, IOOS hurricane gliders in
HWRF-HYCOM and HAFS). Argues from the published impact studies only, without the "AI
makes gliders more valuable" thesis. Carries: `oke2008representation`,
`shulman2009impact`, `rudnick2016ocean`, `todd2011poleward`, `zaba2018annual`,
`levin2020observation`, `dong2017impact`, (`liu2023impact`), (`halliwell2017north`),
(`moore2018reduced`), `moore2011roms` (Part III if added).

## 10. Glossary (0.5 page)

Background, analysis, increment, innovation, B and R, observation operator,
tangent-linear and adjoint model, localization, inflation, FGAT, incremental analysis
update, OSE/OSSE, observation impact and FSOI, representativeness error, Class 4
verification, emulator, end-to-end. Definitions follow `carrassi2018data` and
`moore2019synthesis`.

## 11. Questions for Matt (0.5 page)

The open points the literature left, framed as JXP's reading notes for the Mazloff
conversation; the list will be built while drafting. Expected entries: whether any
operational ocean center runs an ML component inside its DA (as opposed to alongside
it); the status of learned B and learned observation operators in ocean DA; how the
Scripps state estimate treats depth-average velocity and representativeness error for
CUGN; whether the ROMS 4D-Var adjoint can be replaced or accelerated by an emulator;
how a GLORYS-trained emulator's subsurface should be verified on a coast where Argo is
sparse; what a BGC state estimate needs from glider O2 and pH.

---

## Figures and tables

| Figure | Section | Tool | Content |
|---|---|---|---|
| Fig. 1 | 7 (opening) | Mermaid | The four ML entry points (emulator; inside DA; replacing DA; around DA) laid over one cycle: background, observations, QC, analysis, forecast |
| Fig. 2 | 6 (opening), referenced in 7 | matplotlib, `scripts/make_timeline.py`, `figs/ai_da_timeline.png` | 2018-2026 milestones, NWP track and ocean track, each dated from a `sources.bib` entry |
| Fig. 3 | 9 (opening) | Mermaid | One assimilation cycle marking where glider T/S profiles and depth-average velocity enter and where representativeness error arises |
| Fig. 4 | 4-5 | Markdown table | Operational and reanalysis systems: system, center, model, DA method, resolution, cycle, assimilated observations, glider use, source |

No CUGN data are used in v0.1; the optional CUGN profile-density figure is deferred.

## Drafting guidance for prompts 4-6 (from Q&A DA40-DA44)

- **Sources in hand.** All 24 AI entries have their maturity tag and verification note
  written from the full text (`sources.md`, "Basis: full text"); the 28 PDFs are listed
  in `context/da/README.md`. Of the 37 non-AI entries only the anchors are in hand; the
  rest were checked against Crossref metadata and abstracts.
- **Fetching non-AI PDFs (DA44).** The Draft session fetches the open-access non-AI
  PDFs it needs (Zuo 2019, Lellouche 2018 and 2021, Forget 2015, Kim 2024, Fennel 2019,
  Ford 2021, and any other Copernicus, Frontiers or Nature-family entry) by adding them
  to the `PDFS` list of `scripts/fetch_pdfs.py` and running it in `ocean14`, then adds
  the files to `context/da/README.md`. Paywalled entries (Elsevier, AMS, Annual
  Reviews, T&F and the closed AGU/Wiley items) are written from their abstracts and from
  what the anchors and reviews say about them. **Every claim in the draft that rests on
  an abstract alone is flagged in the text** (for example "(abstract)" after the
  citation, or a `[abstract only]` marker the verification pass in prompt #8 collects);
  JXP downloads a paywalled PDF only where the draft flags that the abstract is not
  enough.
- **Citation rule.** Cite only keys in `sources.bib`; a new reference is added to
  `build_bib.py` (never to `sources.md`/`sources.bib` by hand), the script is rerun,
  and `check_sources.py --record` is rerun, before the key is cited.
- **XiHe and FuXi-DA.** State the XiHe training/test overlap as "implied, not stated"
  (DA34) and FuXi-DA's split per the Methods section with the one-clause caveat (DA43).

## Checks against the decisions

- 10-15 pages: 14.0 planned, references excluded; the ceiling is a guide after DA38
  (clarity over brevity).
- Learned parameterizations appear only as a one-sentence boundary case in 7.2 (DA36c).
- Executive summary one page, at the top, written last.
- Primer boxed, marked skippable, with a notation table; analogies only where exact.
- Global roughly 1/3, regional and coastal roughly 2/3 of the systems content.
- Reanalysis/state estimation vs operational forecasting split made explicit in Sections
  4 and 5.
- NWP section about 2 pages, one paragraph per family, two or three exemplars each.
- Ocean AI organized by the four categories; every approach carries a maturity tag and a
  verification note; the trained-on-reanalysis circularity stated once in Section 7 and
  referred back to.
- Full BGC section; glider-specific section; glossary; questions-for-Matt appendix.
- No implications-for-BOONUS section; the gliders thesis left out.
- Four figures placed as decided; the systems table is Fig. 4.
