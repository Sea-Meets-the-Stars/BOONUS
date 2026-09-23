# Reading list for the DA and AI review (candidates for JXP's approval)

**Prompt #1 in `claude_prompts/data_assimilation_prompts.md`, 2026-09-22, Claude Fable
for JXP; approved by JXP the same day (Q&A DA33-DA39, no inline edits) and turned into
`sources.md` and `sources.bib` by `scripts/build_bib.py` on 2026-09-22; completed
2026-09-23 after JXP's answers DA40-DA44.** Sixty-one references (the 60 candidates
plus `zanna2020data`, added under DA36c as the one learned-parameterization boundary
case), grouped by the section of `outline.md` they serve. `sources.md` is now the
authoritative record: complete author lists from Crossref and the arXiv API, and, for
the AI papers, maturity tags and verification notes rewritten from the full text of the
PDFs in `context/da/` (see its README). The entries below keep their prompt-#1
annotations except where a PDF changed a tag or a note, marked "[prompt #2: ...]" for
the 2026-09-22 session (which executed prompts #2 and #3 together under the numbering
JXP later fixed, DA41) and "[prompt #3, 2026-09-23: ...]" for this one.

**Conventions.**

- *Key:* the BibTeX key that `sources.md`, `sources.bib` and the report will share
  (`authorYEARword`).
- *Status:* `verified` = `curl -sI https://doi.org/<doi>` returned a 30x redirect on
  2026-09-22 (run by `scripts/verify_reading_list_dois.py`, output recorded at the end
  of this file) and Crossref metadata matched the citation; `preprint` = arXiv only, ID
  confirmed through the arXiv API on 2026-09-22, no journal version found in Crossref;
  `grey` = web page or repository, URL returned HTTP 200 to `curl -sI -L` on
  2026-09-22; `unverified` = no DOI or URL found (none in this list).
- *Citation:* authors are given as returned by Crossref or the arXiv API, truncated to
  three plus "et al." when longer; volume and article numbers are given only where
  confirmed today. The full author lists and page ranges were completed from Crossref
  in prompt #2 and live in `sources.md` and `sources.bib`. Do not quote page numbers
  from this file.
- *AI papers only:* `Cat.` is the taxonomy category from the Decisions block (1
  emulators/surrogates; 2 ML inside classical DA; 3 ML replacing DA; 4 ML around DA).
  `Maturity` is one of idealized / realistic hindcast / pre-operational / operational.
  `Verification` says what the skill was measured against (withheld observations vs the
  reanalysis or model output it was trained on). Both are filled in only where the text
  I read supports them: in prompt #1, the full paper for the eight anchors and the
  abstract (Crossref or arXiv) for the rest, marked "abstract only"; since 2026-09-23
  every one of the 24 AI papers rests on the full text (the "abstract only" marks below
  are historical and are superseded by the bracketed annotations that follow them). "?"
  means the text I read did not say; nothing is guessed.
- *Optional* marks the entries I would strike first if the list must shrink; the report
  can be written without them.

Counts: 61 entries; 52 `verified`, 4 `preprint`, 5 `grey`, 0 `unverified`; 12 marked
optional. 24 entries are AI papers carrying a category (the two AI reviews and the two
AI-related grey items carry none), all 24 now with maturity tag and verification note
from the full text. PDFs in hand (all gitignored in `context/da/`): the 8 anchors plus
all 20 non-anchor AI papers, 28 entries in total; 18 were fetched by
`scripts/fetch_pdfs.py` on 2026-09-22 and JXP downloaded `bonavita2020.pdf`,
`zanna2020.pdf` and the published `fablet2021_james.pdf` on 2026-09-23 (DA40). No PDF of
a non-AI entry is in hand except the anchors; per DA44 the Draft sessions fetch the
open-access ones as needed.

---

## A. Anchors and reviews (in `context/da/`; serve the primer, Sections 3, 6, 7)

1. **`moore2019synthesis`** — Moore, A. M., Martin, M. J., Akella, S., et al. (GODAE
   OceanView DA Task Team), "Synthesis of Ocean Observations Using Data Assimilation for
   Operational, Real-Time and Reanalysis Systems: A More Complete Picture of the State of
   the Ocean," *Front. Mar. Sci.* 6, 90 (2019). doi:10.3389/fmars.2019.00090.
   Sections 3, 4, 5. Reason: the community statement of what operational ocean DA does,
   its two families (Var, ensemble), the shared problems (B, R, bias, initialization
   shock) and the future list (hybrids, coupled DA, gliders/SWOT). Six pages; a frame,
   not a source of depth. Status: verified.

2. **`carrassi2018data`** — Carrassi, A., Bocquet, M., Bertino, L., and Evensen, G.,
   "Data assimilation in the geosciences: An overview of methods, issues, and
   perspectives," *WIREs Clim. Change* 9(5), e535 (2018). doi:10.1002/wcc.535;
   arXiv:1709.02798. Primer, Section 3. Reason: the derivations behind the boxed primer
   (Bayesian formulation, KF/KS, 3D/4D-Var, EnKF variants, EnVar hybrids, localization
   and inflation) and the TOPAZ example of an operational EnKF. Status: verified.

3. **`geer2021learning`** — Geer, A. J., "Learning earth system models from observations:
   machine learning or data assimilation?" *Phil. Trans. R. Soc. A* 379(2194), 20200089
   (2021). doi:10.1098/rsta.2020.0089. Sections 6, 7 (framing). Reason: the exact
   equivalences (4D-Var cost = loss; adjoint = backpropagation; cycling DA = RNN) that
   let the report define "ML inside DA" precisely, and the list of where emulators can
   enter DA (learnable modules, error learning, accelerators, adjoints). Status:
   verified.

4. **`cheng2023machine`** — Cheng, S., Quilodrán-Casas, C., Ouala, S., et al., "Machine
   Learning With Data Assimilation and Uncertainty Quantification for Dynamical Systems:
   A Review," *IEEE/CAA J. Autom. Sinica* 10(6), 1361-1387 (2023).
   doi:10.1109/JAS.2023.123537; arXiv:2303.10462. Section 7. Reason: the systematic
   survey behind categories 2 and 3 (model-error correction, error-covariance
   specification, end-to-end learning of DA, latent-space DA), with 4DVarNet as its
   ocean exemplar. Status: verified.

5. **`dheeshjith2025samudra`** — Dheeshjith, S., Subel, A., Adcroft, A., et al.,
   "Samudra: An AI Global Ocean Emulator for Climate," *Geophys. Res. Lett.* 52(10),
   e2024GL114318 (2025). doi:10.1029/2024GL114318; arXiv:2412.03795. Section 7.1.
   Reason: the full-depth, century-stable ocean emulator; the clean case of an emulator
   of a *model*. Cat. 1. Maturity: realistic hindcast (emulator of GFDL OM4 forced by
   JRA55-do, 1° grid, 5-day step; 8-year test rollout, 100- and 400-year control runs).
   Verification: against held-out years of the parent model OM4, not against
   observations; underestimates forced trends by 20-50%. Status: verified.

6. **`wang2024xihe`** — Wang, X., Wang, R., Hu, N., et al., "XiHe: A Data-Driven Model
   for Global Ocean Eddy-Resolving Forecasting," arXiv:2402.02995 (2024; no journal
   version found in Crossref on 2026-09-22). Section 7.1. Reason: the first 1/12°
   data-driven global ocean forecast model; the GLORYS12-trained family. Cat. 1.
   Maturity: realistic hindcast. Verification: IV-TT Class 4 against Argo, drifter and
   along-track altimeter observations for Jan 2019-Dec 2020, plus comparison with
   GLORYS12 and tropical moorings; trained on GLORYS12 (stated span 1993-2020) and ERA5
   winds, so whether the 2019-2020 test years were withheld from training needs to be
   checked in the PDF before the report states it. [prompt #2: PDF checked. The data
   section gives the GLORYS12 span as Jan 1993-Dec 2020; the abstract and conclusion say
   XiHe is trained on "25-year" reanalysis data, which would end in 2017 or 2018; the split
   is never stated explicitly. The report will say "implied, not stated" (DA34).] Status:
   preprint.

7. **`cui2025forecasting`** — Cui, Y., Wu, R., Zhang, X., et al., "Forecasting the
   eddying ocean with a deep neural network," *Nat. Commun.* 16, 2268 (2025). (WenHai.)
   doi:10.1038/s41467-025-57389-2. Section 7.1. Reason: bulk-formula air-sea fluxes
   inside the network, tendency output to preserve mesoscale variance, and the fairest
   comparison so far (same initial condition and forcing as GLO12v4). Cat. 1. Maturity:
   realistic hindcast bordering on pre-operational (forecasts run Apr-Nov 2024 from
   operational GLO12v4 analyses). Verification: withheld observations (Class 4: Argo
   T/S, drifter SST and 15 m currents, along-track SLA), RMSE and neighborhood CRPS;
   trained on GLORYS12 1993-2018, validated on 2019; the authors state that AI systems
   "stand on the shoulders of" the numerical reanalysis. Status: verified.

8. **`elaouni2025glonet`** — El Aouni, A., Gaudel, Q., Regnier, C., et al., "GLONET:
   Mercator's End-to-End Neural Global Ocean Forecasting System," *J. Geophys. Res.:
   Machine Learning and Computation* 2(3), e2025JH000686 (2025).
   doi:10.1029/2025JH000686; arXiv:2412.05454. Section 7.1. Reason: an operational
   center's own emulator (Fourier neural operator plus CNN, 1/4° from 1/12° GLORYS12),
   with NN-specific validation metrics beyond point-wise RMSE. Cat. 1. Maturity:
   pre-operational (Mercator "pre-operational pipeline"; experimental daily forecasts on
   the EDITO platform). Verification: IV-TT Class 4 against Argo T/S, drifter and
   altimeter observations, weekly Wednesday initializations; plus comparison with
   GLORYS12 and GLO12; trained on GLORYS12. Status: verified.

## B. Classical methods and the primer (Section 2 box, Section 3)

9. **`evensen2003ensemble`** — Evensen, G., "The Ensemble Kalman Filter: theoretical
   formulation and practical implementation," *Ocean Dyn.* 53, 343-367 (2003).
   doi:10.1007/s10236-003-0036-9. Primer, Section 3. Reason: the standard reference
   for the ensemble Kalman gain and the sampling-error argument behind localization and
   inflation. Status: verified.

10. **`bannister2017review`** — Bannister, R. N., "A review of operational methods of
    variational and ensemble-variational data assimilation," *Q. J. R. Meteorol. Soc.*
    143 (2017). doi:10.1002/qj.2982. Primer, Section 3. Reason: hybrids (EnVar,
    4DEnVar) as used operationally, in one place, with the notation the primer will
    adopt. Status: verified.

11. **`edwards2015regional`** — Edwards, C. A., Moore, A. M., Hoteit, I., and
    Cornuelle, B. D., "Regional Ocean Data Assimilation," *Annu. Rev. Mar. Sci.* 7
    (2015). doi:10.1146/annurev-marine-010814-015821. Sections 3, 5. Reason: the
    review of regional (coastal) DA specifically: open boundaries, forcing errors,
    4D-Var in ROMS and MITgcm, ensemble methods on shelves. Written by the UCSC and
    Scripps groups the report describes. Status: verified.

12. **`stammer2016ocean`** — Stammer, D., Balmaseda, M., Heimbach, P., Köhl, A., and
    Weaver, A., "Ocean Data Assimilation in Support of Climate Applications: Status and
    Perspectives," *Annu. Rev. Mar. Sci.* 8 (2016).
    doi:10.1146/annurev-marine-122414-034113. Sections 3, 4. Reason: the
    reanalysis/state-estimation side of the split: sequential reanalyses vs long-window
    adjoint smoothers (ECCO), what each is good for, and why they disagree. Status:
    verified.

## C. Global systems (Section 4; table in Fig. 4)

13. **`zuo2019ecmwf`** — Zuo, H., Balmaseda, M. A., Tietsche, S., Mogensen, K., and
    Mayer, M., "The ECMWF operational ensemble reanalysis-analysis system for ocean and
    sea ice: a description of the system and assessment," *Ocean Sci.* 15, 779-808
    (2019). doi:10.5194/os-15-779-2019. Section 4. Reason: ORAS5/OCEAN5, the ECMWF
    line; 3D-Var FGAT with a 5-member ensemble, bias correction, and what it assimilates.
    Status: verified.

14. **`lellouche2018recent`** — Lellouche, J.-M., Greiner, E., Le Galloudec, O., et al.,
    "Recent updates to the Copernicus Marine Service global ocean monitoring and
    forecasting real-time 1/12° high-resolution system," *Ocean Sci.* 14, 1093-1126
    (2018). doi:10.5194/os-14-1093-2018. Section 4. Reason: the operational
    (forecast) side of Mercator: the SEEK-derived reduced-order Kalman filter, 7-day
    cycle, the GLO12 baseline that WenHai and GLONET are compared against. Status:
    verified.

15. **`lellouche2021copernicus`** — Lellouche, J.-M., Greiner, E., Bourdallé-Badie, R.,
    et al., "The Copernicus Global 1/12° Oceanic and Sea Ice GLORYS12 Reanalysis,"
    *Front. Earth Sci.* 9, 698876 (2021). doi:10.3389/feart.2021.698876. Sections 4,
    7.1. Reason: the reanalysis that XiHe, WenHai and GLONET are trained on; the report
    needs its observing inputs, known deficiencies, and the fact that it is itself a
    DA product (the circularity caveat). Status: verified.

16. **`cummings2013variational`** — Cummings, J. A., and Smedstad, O. M., "Variational
    Data Assimilation for the Global Ocean," in *Data Assimilation for Atmospheric,
    Oceanic and Hydrologic Applications (Vol. II)*, Springer (2013), ch. 13.
    doi:10.1007/978-3-642-35088-7_13. Section 4. Reason: NCODA, the 3D-Var used with
    HYCOM in the U.S. Navy global system and (as RTOFS's parent) at NCEP; the source for
    the Navy row of the table. Status: verified.

17. **`forget2015ecco`** — Forget, G., Campin, J.-M., Heimbach, P., Hill, C. N., Ponte,
    R. M., and Wunsch, C., "ECCO version 4: an integrated framework for non-linear
    inverse modeling and global ocean state estimation," *Geosci. Model Dev.* 8,
    3071-3104 (2015). doi:10.5194/gmd-8-3071-2015. Section 4. Reason: ECCO v4 as the
    long-window adjoint smoother; the brief names ECCO for boundary conditions, and
    Mazloff's regional state estimates use the same machinery. Status: verified.

18. **`martin2015status`** — Martin, M. J., Balmaseda, M., Bertino, L., et al., "Status
    and future of data assimilation in operational oceanography," *J. Oper. Oceanogr.*
    8(sup1), s28-s48 (2015). doi:10.1080/1755876X.2015.1022055. Section 4 (table).
    Reason: the GODAE OceanView intercomparison of operational systems (Mercator, FOAM,
    Bluelink, GIOPS, HYCOM/NCODA, RTOFS and others) in one table; the source for the
    comparator rows (Bluelink, Copernicus) rather than one paper per system. Status:
    verified.

19. **`rtofs2026ncep`** — NOAA/NCEP Central Operations, "NCEP Data Products: RTOFS
    (Global Real-Time Ocean Forecast System)," https://www.nco.ncep.noaa.gov/pmb/products/rtofs/
    (accessed 2026-09-22). Section 4 (table). Reason: the current description of Global
    RTOFS (1/12° HYCOM, 8-day forecasts); note that the older site
    `polar.ncep.noaa.gov/global/` returned HTTP 404 on 2026-09-22, so the NCO page is
    the citable one. Status: grey.

20. **`soca2026jcsda`** — JCSDA, "SOCA: Sea-ice, Ocean and Coupled Assimilation (JEDI
    marine DA)," GitHub repository https://github.com/JCSDA/soca and JEDI documentation
    https://jcsda-jedi-docs.readthedocs-hosted.com/en/latest/ (accessed 2026-09-22).
    Section 4 (table), Section 5 (HAFS). Reason: the JEDI-based marine DA (3D-Var FGAT,
    hybrid 3DEnVar, LETKF) planned as the first operational SOCA use in GFSv17/GEFSv13
    and used in the Liu et al. (2023) HAFS glider experiments; no peer-reviewed system
    paper found in Crossref on 2026-09-22 (a Q&A item). Status: grey.

## D. Regional and coastal systems (Section 5; paragraphs for U.S. glider-assimilating systems)

21. **`moore2011roms`** — Moore, A. M., Arango, H. G., Broquet, G., Powell, B. S.,
    Weaver, A. T., and Zavala-Garay, J., "The Regional Ocean Modeling System (ROMS)
    4-dimensional variational data assimilation systems: Part I - System overview and
    formulation," *Prog. Oceanogr.* 91 (2011). doi:10.1016/j.pocean.2011.05.004.
    Section 5 (UCSC ROMS). Reason: the formulation of ROMS 4D-Var (primal/dual, strong
    and weak constraint) that assimilates CUGN; Parts II (California Current
    application, doi:10.1016/j.pocean.2011.05.003) and III (observation impact and
    sensitivity, doi:10.1016/j.pocean.2011.05.005) are companion papers to add if
    JXP wants the trilogy. Status: verified.

22. **`neveu2016historical`** — Neveu, E., Moore, A. M., Edwards, C. A., Fiechter, J.,
    Drake, P., Crawford, W. J., Jacox, M. G., and Nuss, E., "An historical analysis of
    the California Current circulation using ROMS 4D-Var: System configuration and
    diagnostics," *Ocean Modell.* 99 (2016). doi:10.1016/j.ocemod.2015.11.012.
    Section 5 (UCSC ROMS). Reason: the 31-year California Current ROMS 4D-Var
    reanalysis, its observation streams (including gliders) and diagnostics; the
    reanalysis side of the regional split. Status: verified.

23. **`todd2011poleward`** — Todd, R. E., Rudnick, D. L., Mazloff, M. R., Davis, R. E.,
    and Cornuelle, B. D., "Poleward flows in the southern California Current System:
    Glider observations and numerical simulation," *J. Geophys. Res.* 116 (2011).
    doi:10.1029/2010JC006536. Section 5 (Scripps state estimate), Section 9. Reason:
    CUGN Line 90 and 80 data in a MITgcm 4D-Var (adjoint) California Current state
    estimate; the brief cites it as `[demonstrated]` glider assimilation. Status:
    verified.

24. **`zaba2018annual`** — Zaba, K. D., Rudnick, D. L., Cornuelle, B. D., Gopalakrishnan,
    G., and Mazloff, M. R., "Annual and Interannual Variability in the California
    Current System: Comparison of an Ocean State Estimate with a Network of Underwater
    Gliders," *J. Phys. Oceanogr.* 48 (2018). doi:10.1175/JPO-D-18-0037.1. Sections 5,
    9. Reason: the Scripps California Current state estimate evaluated against CUGN;
    what a glider network does and does not constrain in a state estimate. Status:
    verified.

25. **`levin2020observation`** — Levin, J., Arango, H. G., Laughlin, B., Hunter, E.,
    Wilkin, J., and Moore, A. M., "Observation impacts on the Mid-Atlantic Bight front
    and cross-shelf transport in 4D-Var ocean state estimates: Part I - Multiplatform
    analysis," *Ocean Modell.* 156, 101721 (2020).
    doi:10.1016/j.ocemod.2020.101721. Sections 5 (Rutgers doppio), 9. Reason: the
    doppio ROMS 4D-Var system and quantified observation impacts by platform, gliders
    included; Part II (Pioneer Array, doi:10.1016/j.ocemod.2020.101731) is the
    companion. Status: verified.

26. **`wcofs2026coops`** — NOAA CO-OPS, "West Coast Operational Forecast System
    (WCOFS)," https://tidesandcurrents.noaa.gov/ofs/wcofs/wcofs.html (accessed
    2026-09-22). Section 5 (NOS OFS). Reason: the operational description of WCOFS
    (ROMS-based, U.S. West Coast); the DA configuration must be taken from the page or
    from Kurapov et al. (2016, *Ocean Dyn.*, doi:10.1007/s10236-016-1013-4, DOI
    confirmed today but not added as an entry) if the page is silent. Status: grey.

27. **`kim2024ocean`** — Kim, H.-S., Liu, B., Thomas, B., et al., "Ocean component of
    the first operational version of Hurricane Analysis and Forecast System: Evaluation
    of HYbrid Coordinate Ocean Model and hurricane feedback forecasts," *Front. Earth
    Sci.* 12, 1399409 (2024). doi:10.3389/feart.2024.1399409. Section 5 (hurricane
    models). Reason: the ocean component of HAFSv1 (HYCOM, operational 2023),
    initialized from RTOFS and evaluated against glider, Argo and buoy observations
    (abstract). Status: verified.

28. **`liu2023impact`** — Liu, B., Mehra, A., Kleist, D., et al., "Impact of
    Assimilating Satellite and Glider Observations on Hurricane Isaias (2020) Forecast
    Using Marine JEDI," *Weather Forecast.* 38(9) (2023). doi:10.1175/WAF-D-22-0014.1.
    Sections 5, 9. Reason: glider assimilation with JEDI/SOCA into MOM6 coupled to
    HAFS; the barrier-layer and intensity result (abstract). *Optional* (Dong et al.
    2017 carries the same point for the earlier HWRF-HYCOM system). Status: verified.

29. **`dong2017impact`** — Dong, J., Domingues, R., Goni, G., et al., "Impact of
    Assimilating Underwater Glider Data on Hurricane Gonzalo (2014) Forecasts,"
    *Weather Forecast.* 32 (2017). doi:10.1175/WAF-D-16-0182.1. Sections 5, 9.
    Reason: the IOOS hurricane-glider result the brief relies on: glider T/S improved
    the upper-ocean initial state and barrier layer in HWRF-HYCOM, with a localized
    footprint. Status: verified.

## E. Glider-specific DA (Section 9; Fig. 3)

30. **`oke2008representation`** — Oke, P. R., and Sakov, P., "Representation Error of
    Oceanic Observations for Data Assimilation," *J. Atmos. Oceanic Technol.* 25 (2008).
    doi:10.1175/2007JTECHO558.1. Section 9. Reason: the definition and estimation of
    representativeness error, which for a glider profile in a several-km ROMS grid is
    the dominant term in R. Status: verified.

31. **`shulman2009impact`** — Shulman, I., Rowley, C., Anderson, S., et al., "Impact of
    glider data assimilation on the Monterey Bay model," *Deep-Sea Res. II* 56 (2009).
    doi:10.1016/j.dsr2.2008.08.003. Section 9. Reason: an early U.S. West Coast glider
    assimilation study (NCOM/NCODA, Monterey Bay) with profile-vs-model impact; useful
    for the profile-vs-binned discussion. Status: verified.

32. **`rudnick2016ocean`** — Rudnick, D. L., "Ocean Research Enabled by Underwater
    Gliders," *Annu. Rev. Mar. Sci.* 8 (2016). doi:10.1146/annurev-marine-122414-033913.
    Section 9. Reason: section 7 of the review covers gliders in assimilating models
    and depth-average velocity as an absolutely referenced observation; already digested
    in `context/sources/rudnick2016.md`. Status: verified.

33. **`halliwell2017north`** — Halliwell, G. R., Mehari, M. F., Le Hénaff, M., et al.,
    "North Atlantic Ocean OSSE system: Evaluation of operational ocean observing system
    components and supplemental seasonal observations for potentially improving tropical
    cyclone prediction in coupled systems," *J. Oper. Oceanogr.* 10 (2017).
    doi:10.1080/1755876X.2017.1322770. Section 9. Reason: the OSSE methodology
    (fraternal-twin, HYCOM) used to value hurricane-season ocean observations; the
    template for OSSE claims in the glider section. *Optional*. Status: verified.

34. **`moore2018reduced`** — Moore, A. M., Arango, H. G., and Edwards, C. A.,
    "Reduced-Rank Array Modes of the California Current Observing System," *J. Geophys.
    Res. Oceans* 123 (2018). doi:10.1002/2017JC013172. Section 9. Reason: an
    adjoint-based observing-system analysis of the California Current array (gliders,
    HF radar, satellites) in ROMS 4D-Var; the method behind "line locations from
    observing-system design experiments" in the brief. *Optional*. Status: verified.

## F. AI in numerical weather prediction, the leading indicator (Section 6; Fig. 2)

35. **`bi2023accurate`** — Bi, K., Xie, L., Zhang, H., Chen, X., Gu, X., and Tian, Q.,
    "Accurate medium-range global weather forecasting with 3D neural networks,"
    *Nature* 619, 533-538 (2023). doi:10.1038/s41586-023-06185-3. Section 6
    (emulators). Cat. 1. Maturity: realistic hindcast. Verification: "stronger
    deterministic forecast results on reanalysis data" than IFS, i.e. against ERA5, the
    reanalysis it was trained on (abstract only). [prompt #2: full text. Trained on ERA5
    1979-2017, validated 2019, tested 2018; scored against ERA5 only, tracks against
    IBTrACS; the authors write that it "was trained and tested on reanalysis data, but
    real-world forecast systems work on observational data". No operational status.]
    Status: verified.

36. **`lam2023learning`** — Lam, R., Sanchez-Gonzalez, A., Willson, M., et al.,
    "Learning skillful medium-range global weather forecasting," *Science* 382,
    1416-1421 (2023). doi:10.1126/science.adi2336. Section 6 (emulators). Cat. 1.
    Maturity: realistic hindcast. Verification: trained on ERA5; 1380 verification
    targets against the operational deterministic system; whether the targets are ERA5
    or observations is not in the abstract (abstract only; ?). [prompt #2: full text
    (arXiv copy). Test years 2018-2021 explicitly held out; GraphCast is scored against
    ERA5 and HRES against its own analyses (HRES-fc0); no station or radiosonde
    verification; research system, "should not be regarded as a replacement for
    traditional weather forecasting methods".] Status: verified.

37. **`lang2024aifs`** — Lang, S., Alexe, M., Chantry, M., et al., "AIFS - ECMWF's
    data-driven forecasting system," arXiv:2406.01465 (2024). Section 6 (emulators).
    Cat. 1. Maturity: operational (see `ecmwf2025aifs`). Verification: "comparing its
    forecasts to NWP analyses and direct observational data" (arXiv abstract); trained
    on ERA5 and ECMWF operational analyses. [prompt #2: full text. "Experimental
    operational mode" from October 2023 per the paper; pre-trained on ERA5 1979-2020,
    fine-tuned on IFS operational analyses 2019-2020; 2022 scorecard against the
    operational analysis and against radiosonde and SYNOP observations; the day-1
    degradation seen against analyses "is not present in verification against radiosonde
    observations"; about 10% better than IFS through the troposphere.] Status: preprint.

38. **`ecmwf2025aifs`** — ECMWF, "ECMWF's AI forecasts become operational," news item,
    25 February 2025,
    https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational
    (accessed 2026-09-22). Section 6, Fig. 2. Reason: the date on which AIFS Single
    became operational (25 Feb 2025), 28 km grid, the first ML forecast model run
    operationally by a major center; a timeline milestone. *Optional* (needed only for
    the milestone date). Status: grey.

39. **`price2024probabilistic`** — Price, I., Sanchez-Gonzalez, A., Alet, F., et al.,
    "Probabilistic weather forecasting with machine learning," *Nature* 637, 84-90
    (2024, print 2025). (GenCast.) doi:10.1038/s41586-024-08252-9. Section 6
    (emulators, probabilistic). Cat. 1. Maturity: realistic hindcast. Verification:
    trained on reanalysis; 1320 targets against ECMWF ENS (abstract only; target data
    ?). [prompt #2: full text. Trained on ERA5 1979-2018, tested on 2019 after the model
    was frozen; each model scored against its own best-estimate analysis (GenCast vs
    ERA5, ENS vs HRES-fc0), no observations; better CRPS than ENS on 97.2% of targets;
    research system.] Status: verified.

40. **`bonavita2020machine`** — Bonavita, M., and Laloyaux, P., "Machine Learning for
    Model Error Inference and Correction," *J. Adv. Model. Earth Syst.* 12 (2020).
    doi:10.1029/2020MS002232. Section 6 (learned DA), Section 7.2 (the pattern). Cat.
    2. Maturity: realistic hindcast (operational IFS configuration, offline). Verification:
    reproduces the weak-constraint 4D-Var model-error estimates, i.e. against a DA
    product, not independent observations (abstract). [prompt #3, 2026-09-23: full text
    (publisher PDF downloaded by JXP). The abstract-based note was too narrow. The ANN
    is trained offline on a DA product (operational 12 h analysis increments of 2018 at
    T21, about 900 km; validated Jan-Feb 2019, tested from April 2019 for 3.5 months; it
    explains about 14% of the increment variance for mass, 5% for wind, none for
    humidity), but its model-error tendencies were then used inside cycled 4D-Var at the
    operational IFS configuration (Cycle 47R1, TCo1279, 16 July-24 August 2019), as a
    forcing in strong-constraint 4D-Var and as the first guess of the weak-constraint
    forcing, and those experiments are verified against observations: background
    departures for radiosondes, GPS-RO, winds, AMVs and surface pressure, and 72 h
    temperature forecast RMSE against independent GPS-RO retrievals. They replicate the
    stratospheric bias reduction of weak-constraint 4D-Var, extend it to the troposphere
    and roughly halve surface-pressure biases; most differences are not significant over
    the 5-6 week test. Maturity: realistic hindcast (cycled 4D-Var experiments at the
    operational configuration; the authors call the results preliminary and the hybrid a
    proof-of-concept, "not yet fully in place for reliable operational use").] Status:
    verified.

41. **`hatfield2021building`** — Hatfield, S., Chantry, M., Dueben, P., Lopez, P., Geer,
    A., and Palmer, T., "Building Tangent-Linear and Adjoint Models for Data
    Assimilation With Neural Networks," *J. Adv. Model. Earth Syst.* 13 (2021).
    doi:10.1029/2021MS002521. Section 6 (learned DA). Cat. 2 (adjoint surrogate).
    Maturity: realistic model, one parametrization (non-orographic gravity-wave drag).
    Verification: TL/adjoint consistency tests and 4D-Var experiments (abstract).
    [prompt #2: full text. The neural TL/adjoint replaced the hand-coded linear models of
    the scheme inside a cycled 4D-Var run (IFS 46r1, TCo399, Dec 2018-Feb 2019, 177
    ten-day forecasts); forecast RMSE differences from the reference were at most 4% and
    not significant; departures were also checked against ATMS and GPSRO observations,
    which are themselves assimilated.] *Optional*. Status: verified.

42. **`xu2025fuxida`** — Xu, X., Sun, X., Han, W., et al., "FuXi-DA: a generalized deep
    learning data assimilation framework for assimilating satellite observations," *npj
    Clim. Atmos. Sci.* 8 (2025). doi:10.1038/s41612-025-01039-3; arXiv:2404.08522.
    Section 6 (learned DA). Cat. 3 (learned assimilation of satellite radiances into an
    ML forecast model). [prompt #2: full text. Maturity: realistic hindcast, offline and
    non-cycled ("feasibility"). Assimilates FY-4B AGRI brightness temperatures (channels
    8-15) into a background from a FuXi 6 h forecast initialised from ERA5; the training
    target and the ground truth for every metric is ERA5, no independent observations;
    test Aug-Dec 2023. The Results section states a training span (June 2022-June 2024)
    that overlaps the test period while Methods gives June 2022-May 2023; flagged in Q&A
    (DA43). Analysis RMSE 2-4.5% below a bias-corrected background; Z500 forecast error
    0.67% lower at day 1.] [prompt #3, 2026-09-23, DA43 answered: the report uses the
    Methods split, training June 2022-May 2023, validation June-July 2023, test
    August-December 2023, and notes in one clause that the Results section states the
    training span inconsistently. Tag: "realistic hindcast, offline and non-cycled,
    verified against ERA5".] Status: verified.

43. **`allen2025endtoend`** — Allen, A., Markou, S., Tebbutt, W., et al., "End-to-end
    data-driven weather prediction," *Nature* 641, 1172-1179 (2025). (Aardvark
    Weather.) doi:10.1038/s41586-025-08897-0. Section 6 (end-to-end). Cat. 3. Maturity:
    realistic hindcast. Verification: against an operational NWP baseline for global
    fields and against station forecasts for local skill (abstract only; training target
    ?). [prompt #2: full text. The encoder and processor are pre-trained with ERA5 as the
    target, the station decoder on HadISD observations, then fine-tuned end to end; 2018
    held out as test; gridded fields scored against ERA5 (HRES and GFS baselines at 1.5
    degrees), station forecasts against held-out HadISD (station-corrected HRES and NDFD
    baselines). No NWP product enters at test time, but ERA5 is the pre-training target,
    so "end-to-end from observations" holds for deployment, not for training. Research
    prototype.] Status: verified.

44. **`alexe2024graphdop`** — Alexe, M., Boucher, E., Lean, P., et al., "GraphDOP:
    Towards skilful data-driven medium-range weather forecasts learnt and initialised
    directly from observations," arXiv:2412.15687 (2024). Section 6 (end-to-end).
    Cat. 3. Maturity: realistic hindcast (research system at ECMWF). Verification:
    trained and initialised from observations only, "no physics-based (re)analysis
    inputs"; skill measured against ? (arXiv abstract only). [prompt #2: full text.
    Trained on observations 2004-2021 (2022 validation), target the next 12 h of
    observations; an ERA5-departure QC step is flagged by the authors as a partial
    dependence on the reanalysis. Verified in observation space (SYNOP 2 m temperature,
    AMSU-A and SSMIS brightness temperatures) against operational IFS, and on a grid
    against ERA5 "employed exclusively for verification"; 15% better than IFS for 2 m
    temperature at day 1, mixed at days 3-5, worse for AMSU-A; "not yet close to matching
    state-of-the-art NWP performance".] *Optional*. Status: preprint.

45. **`manshausen2025generative`** — Manshausen, P., Cohen, Y., Harrington, P., et al.,
    "Generative Data Assimilation of Sparse Weather Station Observations at Kilometer
    Scales," *J. Adv. Model. Earth Syst.* 17 (2025). doi:10.1029/2024MS004505;
    arXiv:2406.16947. Section 6 (generative DA). Cat. 3. Maturity: realistic hindcast
    (km-scale central U.S. testbed). Verification: withheld stations (10% lower RMSE on
    left-out stations from 40 assimilated); the diffusion prior is trained on the HRRR
    analysis product (abstract). [prompt #2: full text (arXiv copy). Prior trained on
    HRRR 2018-2021, tested on 2017 ISD stations, 40 assimilated and 10 held out; the
    authors note the held-out stations are part of the METAR data HRRR itself
    assimilates; "proof of concept"; ensembles underdispersive.] Status: verified.

## G. AI in ocean DA, by taxonomy category (Section 7; Fig. 1)

46. **`yuan2026samudra2`** — Yuan, Y., Rusak, J., Merose, A., Subel, A., et al.,
    "Samudra 2: Scaling Ocean Emulators across Resolutions," arXiv:2606.02610 (2026).
    Section 7.1. Cat. 1. Maturity: ? (abstract: 1°, 1/2° and 1/4° emulators, ~8-year
    rollouts; fixes variance collapse and imprinting). Verification: against the parent
    OGCM output as for Samudra (abstract implies; ?). [prompt #2: full text. Maturity:
    realistic hindcast, emulator of a model, no DA. Trained on GFDL OM4 output
    coarse-grained to the three resolutions, 1975-2013; rollouts 2014-2022 scored against
    the OM4 truth, no observations; upper-ocean temperature R^2 0.56 to 0.87 at 1° versus
    Samudra, deep-ocean R^2 still negative.] *Optional* (recency). Status: preprint.

47. **`chattopadhyay2024oceannet`** — Chattopadhyay, A., Gray, M., Wu, T., et al.,
    "OceanNet: a principled neural operator-based digital twin for regional oceans,"
    *Sci. Rep.* 14, 21181 (2024). doi:10.1038/s41598-024-72145-0. Section 7.1
    (regional emulator). Cat. 1. Maturity: ? (abstract: Gulf Stream / northwest Atlantic
    SSH, seasonal prediction of Loop Current eddies and the meander). Verification:
    "trained using historical sea surface height data", compared with a dynamical model
    forecast (abstract only; whether the target is a reanalysis or observations: ?).
    [prompt #2: full text. The target is a reanalysis: a 4 km ROMS-EnKF northwest
    Atlantic reanalysis 1993-2018 (SSH, 5-day means, 90-120 day horizon); tested on
    2019-2020 against the same reanalysis, not observations; matches a ROMS forecast in
    the Gulf of Mexico and beats it in the Gulf Stream region; the authors call it "initial
    steps" and note that real systems run on real-time observations. Maturity: realistic
    hindcast (reanalysis emulator).] Status: verified.

48. **`gregory2023deep`** — Gregory, W., Bushuk, M., Adcroft, A., Zhang, Y., and Zanna,
    L., "Deep Learning of Systematic Sea Ice Model Errors From Data Assimilation
    Increments," *J. Adv. Model. Earth Syst.* 15 (2023). doi:10.1029/2023MS003757.
    Section 7.2. Cat. 2 (learned model-error / bias correction from increments).
    Maturity: realistic hindcast (GFDL SPEAR ice-ocean DA, 1982-2017). Verification:
    predicts DA increments, skill against a climatological-increment baseline; not
    against independent observations (abstract). The nearest ocean-side analogue of
    Bonavita and Laloyaux (2020). [prompt #2: full text (arXiv copy) confirms: offline
    feasibility study, 5-fold cross-validation plus an untouched 2018-2021 extension,
    daily pattern correlations 0.62-0.80 against the increments.] Status: verified.

49. **`fablet2021learning`** — Fablet, R., Chapron, B., Drumetz, L., Mémin, E., Pannekoucke,
    O., and Rousseau, F., "Learning Variational Data Assimilation Models and Solvers,"
    *J. Adv. Model. Earth Syst.* 13 (2021). doi:10.1029/2021MS002572. Section 7.3.
    Cat. 3 (4DVarNet: learned prior and learned solver of a variational cost).
    Maturity: idealized (Lorenz-63, Lorenz-96). Verification: against the known truth of
    the toy systems (abstract). [prompt #2: full text of arXiv v1 (2020), which carries the
    preprint title "End-to-end learning for variational data assimilation models and
    solvers" and the same six authors; confirms Lorenz-63/96 only, reconstruction error
    against the simulated truth. The published JAMES PDF is on JXP's list (DA40) in case
    it differs.] [prompt #3, 2026-09-23: published JAMES version read
    (`fablet2021_james.pdf`, downloaded by JXP). It does not differ materially from the
    arXiv v1: same six authors, same Lorenz-63 and Lorenz-96 experiments and the same
    headline numbers (Lorenz-63 reconstruction error 1.34 vs 3.55 for the fixed-step
    gradient descent baseline; Lorenz-96 0.38 vs 1.06). The published version changes the
    title, fills two placeholder cells of Table 1, expands the related-work section with
    pointers to the group's SSH applications and archives the code on Zenodo. The
    conclusion asks whether the findings "generalize to other systems, especially
    higher-dimensional ones". Maturity idealized, unchanged; basis now the published
    text.] Status: verified.

50. **`beauchamp2023fourdvarnet`** — Beauchamp, M., Febvre, Q., Georgenthum, H., and
    Fablet, R., "4DVarNet-SSH: end-to-end learning of variational interpolation schemes
    for nadir and wide-swath satellite altimetry," *Geosci. Model Dev.* 16, 2119-2147
    (2023). doi:10.5194/gmd-16-2119-2023. Section 7.3. Cat. 3. Maturity: realistic
    OSSE (NATL60 simulation, the SSH-mapping data challenge). Verification: against the
    simulated truth, not observations; 30-60% lower reconstruction error than
    operational OI (abstract). [prompt #2: full text confirms; test window Oct-Dec 2012
    separate from training; resolved scales 0.83°/8 days vs 1.42°/12 days for DUACS;
    real altimetry named as future work.] Status: verified.

51. **`martin2023synthesizing`** — Martin, S. A., Manucharyan, G. E., and Klein, P.,
    "Synthesizing Sea Surface Temperature and Satellite Altimetry Observations Using
    Deep Learning Improves the Accuracy and Resolution of Gridded Sea Surface Height
    Anomalies," *J. Adv. Model. Earth Syst.* 15 (2023). doi:10.1029/2022MS003589.
    Section 7.3. Cat. 3 (neural interpolation). Maturity: realistic hindcast (Gulf
    Stream Extension, real altimetry and SST). Verification: withheld observations
    (independent altimeter tracks, 17% lower RMSE; drifters) (abstract). [prompt #2: full
    text (published version via EarthArXiv) confirms: 2017 withheld, CryoSat-2 withheld
    as ground truth, AOML drifters independent; 24-27% lower surface-current RMSE than
    DUACS against drifters.] *Optional* (one of the two SSH-mapping exemplars). Status:
    verified.

52. **`oceandatachallenges2026`** — ocean-data-challenges consortium, "2020a SSH mapping
    NATL60" (and the 2021a OSE challenge), GitHub,
    https://github.com/ocean-data-challenges/2020a_SSH_mapping_NATL60 (accessed
    2026-09-22). Section 7.3. Reason: the shared benchmark on which 4DVarNet and the
    other neural mappers are scored; defines the OSSE (NATL60) vs OSE (real data)
    verification split the report will use. Status: grey.

53. **`sugiura2020machine`** — Sugiura, N., and Hosoda, S., "Machine Learning Technique
    Using the Signature Method for Automated Quality Control of Argo Profiles," *Earth
    Space Sci.* 7 (2020). doi:10.1029/2019EA001019. Section 7.4. Cat. 4 (QC).
    Maturity: realistic (Argo profiles with existing QC flags). Verification: cross
    validation against the existing QC flags, i.e. against human/rule-based labels
    (abstract). [prompt #2: full text (arXiv copy). 82,000 profiles deeper than 1000 m;
    target the JAMSTEC delayed-mode flag; 40% random training split (by float not stated),
    60% cross-validation; ROC curves only; at the cutoff that misflags no good profile it
    still accepts about 60% of bad ones. Offline method demonstration.] Status: verified.

## H. Biogeochemical DA (Section 8)

54. **`fennel2019advancing`** — Fennel, K., Gehlen, M., Brasseur, P., et al.,
    "Advancing Marine Biogeochemical and Ecosystem Reanalyses and Forecasts as Tools
    for Monitoring and Managing Ecosystem Health," *Front. Mar. Sci.* 6, 89 (2019).
    doi:10.3389/fmars.2019.00089. Section 8. Reason: the OceanObs'19 statement of BGC
    DA status: what is assimilated (ocean colour, BGC-Argo), physics-BGC coupling
    problems, non-Gaussianity, and the gap to operations. Status: verified.

55. **`mattern2017data`** — Mattern, J. P., Song, H., Edwards, C. A., Moore, A. M., and
    Fiechter, J., "Data assimilation of physical and chlorophyll a observations in the
    California Current System using two biogeochemical models," *Ocean Modell.* 109
    (2017). doi:10.1016/j.ocemod.2016.12.002. Section 8. Reason: coupled physical-BGC
    4D-Var in the California Current ROMS, the configuration BOONUS BGC data would
    enter; shows the model dependence of BGC assimilation. Status: verified.

56. **`verdy2017data`** — Verdy, A., and Mazloff, M. R., "A data assimilating model for
    estimating Southern Ocean biogeochemistry," *J. Geophys. Res. Oceans* 122 (2017).
    doi:10.1002/2016JC012650. Section 8. Reason: B-SOSE, adjoint-method state
    estimation with carbon, oxygen and nutrients constrained by floats and ships; the
    state-estimation side of BGC DA, and Mazloff's own work. Status: verified.

57. **`carroll2020ecco`** — Carroll, D., Menemenlis, D., Adkins, J. F., et al., "The
    ECCO-Darwin Data-Assimilative Global Ocean Biogeochemistry Model: Estimates of
    Seasonal to Multidecadal Surface Ocean pCO2 and Air-Sea CO2 Flux," *J. Adv. Model.
    Earth Syst.* 12 (2020). doi:10.1029/2019MS001888. Section 8. Reason: the Darwin
    ecosystem model named in the brief, coupled to the ECCO state estimate; the global
    BGC state-estimation reference. Status: verified.

58. **`ford2021assimilating`** — Ford, D., "Assimilating synthetic Biogeochemical-Argo
    and ocean colour observations into a global ocean model to inform observing system
    design," *Biogeosciences* 18, 509-534 (2021). doi:10.5194/bg-18-509-2021. Section
    8 (and 9). Reason: a BGC OSSE that values in situ chlorophyll, nitrate, oxygen and
    pH profiles against ocean colour; the template for asking what glider O2/pH/chl
    would add. *Optional*. Status: verified.

59. **`bittig2018canyonb`** — Bittig, H. C., Steinhoff, T., Claustre, H., et al., "An
    Alternative to Static Climatologies: Robust Estimation of Open Ocean CO2 Variables
    and Nutrient Concentrations From T, S, and O2 Data Using Bayesian Neural Networks,"
    *Front. Mar. Sci.* 5, 328 (2018). (CANYON-B.) doi:10.3389/fmars.2018.00328.
    Section 8, Section 7.4. Cat. 4 (derived variables around DA). [prompt #2: full text.
    Maturity: realistic, released mapping method with code, a "transfer function between
    components of the ocean observing system". Verification: Bayesian neural networks
    trained on GLODAPv2 bottle data (521 cruises, 1972-2013) with 20% set aside, validated
    against 19 post-GLODAPv2 GO-SHIP cruises 2012-2017 as a completely independent set
    plus Argo pH/pCO2 floats; RMSE nitrate 0.68, phosphate 0.051, silicate 2.3, AT 6.3,
    CT 7.1 umol/kg, pH 0.013, pCO2 20 uatm.] Reason: neural-network estimation of
    nutrients and carbonate variables from T, S and O2, the variables a glider carries;
    widely used with BGC-Argo. *Optional*. Status: verified.

60. **`gloege2022improved`** — Gloege, L., Yan, M., Zheng, T., and McKinley, G. A.,
    "Improved Quantification of Ocean Carbon Uptake by Using Machine Learning to Merge
    Global Models and pCO2 Data," *J. Adv. Model. Earth Syst.* 14 (2022).
    doi:10.1029/2021MS002620. Section 8, Section 7.2. Cat. 2 (ML correction of model-data
    misfit). Maturity: realistic hindcast (1982-2018 global pCO2). Verification:
    "better agreement with independent pCO2 observations" (abstract). [prompt #2: full
    text (publisher PDF via the NOAA repository). XGBoost learns the SOCAT-minus-model
    pCO2 misfit for nine global models; seven whole years withheld, plus fully independent
    non-SOCAT data (GLODAPv2, BATS, HOT); RMSE against GLODAP in the 2010s 15.4 vs
    15.7-17.7 for other products; released as the LDEO-HPD product.] *Optional*. Status:
    verified.

61. **`zanna2020data`** — Zanna, L., and Bolton, T., "Data-Driven Equation Discovery of
    Ocean Mesoscale Closures," *Geophys. Res. Lett.* 47(17), e2020GL088376 (2020).
    doi:10.1029/2020GL088376. Section 7.2 (one-sentence boundary case). Cat. 2 by
    placement only: a learned sub-grid closure changes the model, not the assimilation;
    kept so the DA30 list is honoured literally (DA36c, added in prompt #2 and numbered
    last to keep the prompt-#1 numbers stable). Maturity: idealized (offline, against the
    diagnosed sub-grid forcing of a high-resolution model; abstract only). Verification:
    against model-diagnosed forcing, not observations (abstract only). Not open access
    (Unpaywall and Semantic Scholar: closed); on JXP's download list (DA40). [prompt #3,
    2026-09-23: skimmed the publisher PDF downloaded by JXP (`zanna2020.pdf`), enough for
    the one sentence. Idealized MITgcm double-gyre runs (barotropic 3.75 km, baroclinic
    7.5 km) coarse-grained to 30 km; RVM equation discovery and a physics-constrained CNN
    fitted to the diagnosed eddy forcing (1000 snapshots, 50/50 train/validation;
    offline correlation about 0.6 for the temperature forcing, variance underestimated
    by about 50%); then run online in a different 30 km idealized shallow-water model
    with the forcing attenuated by factors 0.5-0.7 for stability, compared with the
    3.75 km run on kinetic energy, spectrum and PDFs. No observations anywhere; tags
    unchanged. Kept per DA42.] *Optional*. Status: verified.

---

## Not included, for the record

Candidates I checked (DOI confirmed in Crossref on 2026-09-22) and left out to stay at
60; add any back by name: Houtekamer and Zhang 2016 (EnKF review,
doi:10.1175/MWR-D-15-0440.1); Wunsch and Heimbach 2007 (state estimation,
doi:10.1016/j.physd.2006.09.040); Storto et al. 2019 (reanalyses,
doi:10.3389/fmars.2019.00418); Penny et al. 2015 (NCEP hybrid,
doi:10.1175/MWR-D-14-00376.1); Metzger et al. 2014 (Navy systems,
doi:10.5670/oceanog.2014.66); Heimbach et al. 2019 (doi:10.3389/fmars.2019.00055);
Wilkin et al. 2017 (IOOS coastal modelling, doi:10.1080/1755876X.2017.1322026);
Kurapov et al. 2016 (WCOFS, doi:10.1007/s10236-016-1013-4); Oke et al. 2008 (BODAS,
doi:10.1016/j.ocemod.2007.11.002); Sotillo et al. 2015 (Copernicus IBI,
doi:10.1080/1755876X.2015.1014663); Domingues et al. 2019
(doi:10.3389/fmars.2019.00446); Dobricic et al. 2010 (glider DA, Ionian Sea,
doi:10.1016/j.dynatmoce.2010.01.001); Mourre and Alvarez 2012 (glider adaptive
sampling, doi:10.1016/j.dsr.2012.05.010); Todd et al. 2017 (glider ADCP absolute
velocity, doi:10.1175/JTECH-D-16-0156.1); Lermusiaux 2007 (adaptive sampling,
doi:10.1016/j.physd.2007.02.014); Kochkov et al. 2024 (NeuralGCM,
doi:10.1038/s41586-024-07744-y); Melinc and Zaplotnik 2024 (VAE 3D-Var,
doi:10.1002/qj.4708); Farchi et al. 2021 (doi:10.1002/qj.4116); Brajard et al. 2020
(doi:10.1016/j.jocs.2020.101171); Bocquet et al. 2020 (doi:10.3934/fods.2020004);
Bire et al. 2025 (FNO double gyre, doi:10.1029/2023MS004137); Sane et al. 2023
(doi:10.1029/2023MS003890; Zanna and Bolton 2020 moved into the list as entry 61 in
prompt #2); Manucharyan
et al. 2021 (doi:10.1029/2019MS001965); Pauthenet et al. 2022
(doi:10.5194/os-18-1221-2022); Mieruch et al. 2021 (SalaciaML,
doi:10.3389/fmars.2021.611742); Maze et al. 2017 (doi:10.1016/j.pocean.2016.12.008);
Thiria et al. 2023 (doi:10.1016/j.ocemod.2023.102174); Raghukumar et al. 2015
(doi:10.1016/j.pocean.2015.01.004); Jacox et al. 2022 (MHW forecasts,
doi:10.1038/s41586-022-04573-9); Mehra and Rivin 2010 (RTOFS Atlantic,
doi:10.3319/TAO.2009.04.16.01(IWNOP)). Preprints checked and left out: FourCastNet
(arXiv:2202.11214), FengWu-4DVar (arXiv:2312.12455), DiffDA (arXiv:2401.05932),
Score-based DA (arXiv:2306.10574), McNally et al. 2024 (arXiv:2407.15586), AIFS-CRPS
(arXiv:2412.15832), Subel and Zanna 2024 (arXiv:2402.04342), AI-GOMS
(arXiv:2308.03152), Holmberg et al. 2024 (arXiv:2410.11807).

## DOI verification run

Output of `conda run -n ocean14 python reports/data_assimilation/scripts/verify_reading_list_dois.py`
on 2026-09-22 (the "Not included" DOIs above are checked as well, since the script
extracts every DOI in this file):

Location headers omitted here; the script prints them.

```
# reading_list.md: 85 DOIs, checked 2026-09-22
ok    302  10.3389/fmars.2019.00090
ok    302  10.1002/wcc.535
ok    302  10.1098/rsta.2020.0089
ok    302  10.1109/JAS.2023.123537
ok    302  10.1029/2024GL114318
ok    302  10.1038/s41467-025-57389-2
ok    302  10.1029/2025JH000686
ok    302  10.1007/s10236-003-0036-9
ok    302  10.1002/qj.2982
ok    302  10.1146/annurev-marine-010814-015821
ok    302  10.1146/annurev-marine-122414-034113
ok    302  10.5194/os-15-779-2019
ok    302  10.5194/os-14-1093-2018
ok    302  10.3389/feart.2021.698876
ok    302  10.1007/978-3-642-35088-7_13
ok    302  10.5194/gmd-8-3071-2015
ok    302  10.1080/1755876X.2015.1022055
ok    302  10.1016/j.pocean.2011.05.004
ok    302  10.1016/j.pocean.2011.05.003
ok    302  10.1016/j.pocean.2011.05.005
ok    302  10.1016/j.ocemod.2015.11.012
ok    302  10.1029/2010JC006536
ok    302  10.1175/JPO-D-18-0037.1
ok    302  10.1016/j.ocemod.2020.101721
ok    302  10.1016/j.ocemod.2020.101731
ok    302  10.1007/s10236-016-1013-4
ok    302  10.3389/feart.2024.1399409
ok    302  10.1175/WAF-D-22-0014.1
ok    302  10.1175/WAF-D-16-0182.1
ok    302  10.1175/2007JTECHO558.1
ok    302  10.1016/j.dsr2.2008.08.003
ok    302  10.1146/annurev-marine-122414-033913
ok    302  10.1080/1755876X.2017.1322770
ok    302  10.1002/2017JC013172
ok    302  10.1038/s41586-023-06185-3
ok    302  10.1126/science.adi2336
ok    302  10.1038/s41586-024-08252-9
ok    302  10.1029/2020MS002232
ok    302  10.1029/2021MS002521
ok    302  10.1038/s41612-025-01039-3
ok    302  10.1038/s41586-025-08897-0
ok    302  10.1029/2024MS004505
ok    302  10.1038/s41598-024-72145-0
ok    302  10.1029/2023MS003757
ok    302  10.1029/2021MS002572
ok    302  10.5194/gmd-16-2119-2023
ok    302  10.1029/2022MS003589
ok    302  10.1029/2019EA001019
ok    302  10.3389/fmars.2019.00089
ok    302  10.1016/j.ocemod.2016.12.002
ok    302  10.1002/2016JC012650
ok    302  10.1029/2019MS001888
ok    302  10.5194/bg-18-509-2021
ok    302  10.3389/fmars.2018.00328
ok    302  10.1029/2021MS002620
ok    302  10.1175/MWR-D-15-0440.1
ok    302  10.1016/j.physd.2006.09.040
ok    302  10.3389/fmars.2019.00418
ok    302  10.1175/MWR-D-14-00376.1
ok    302  10.5670/oceanog.2014.66
ok    302  10.3389/fmars.2019.00055
ok    302  10.1080/1755876X.2017.1322026
ok    302  10.1016/j.ocemod.2007.11.002
ok    302  10.1080/1755876X.2015.1014663
ok    302  10.3389/fmars.2019.00446
ok    302  10.1016/j.dynatmoce.2010.01.001
ok    302  10.1016/j.dsr.2012.05.010
ok    302  10.1175/JTECH-D-16-0156.1
ok    302  10.1016/j.physd.2007.02.014
ok    302  10.1038/s41586-024-07744-y
ok    302  10.1002/qj.4708
ok    302  10.1002/qj.4116
ok    302  10.1016/j.jocs.2020.101171
ok    302  10.3934/fods.2020004
ok    302  10.1029/2023MS004137
ok    302  10.1029/2020GL088376
ok    302  10.1029/2023MS003890
ok    302  10.1029/2019MS001965
ok    302  10.5194/os-18-1221-2022
ok    302  10.3389/fmars.2021.611742
ok    302  10.1016/j.pocean.2016.12.008
ok    302  10.1016/j.ocemod.2023.102174
ok    302  10.1016/j.pocean.2015.01.004
ok    302  10.1038/s41586-022-04573-9
ok    302  10.3319/TAO.2009.04.16.01(IWNOP)
# 85/85 redirected (30x)
```
