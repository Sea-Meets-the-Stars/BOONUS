# context/da/

Anchor and supporting papers for the data assimilation (DA) and AI review
(`reports/data_assimilation/`, see `claude_prompts/data_assimilation_prompts.md`).
The eight anchors were fixed in the DA Q&A, rounds 1-2 (DA15, DA21, DA30) in
`claude_prompts/context_prompts.md`; the 18 AI papers below them were fetched on
2026-09-22 (the session that executed prompts #2-#3 of `data_assimilation_prompts.md`)
under DA37 by `reports/data_assimilation/scripts/fetch_pdfs.py`, which checks each
download with `file` and by matching the title in the first two pages; the last three
were downloaded by JXP on 2026-09-23 (DA40) and checked the same way by hand. With
them every AI entry of the reading list (8 anchors plus 20 others, 28 files) is in hand.
Per DA44 the Draft sessions (prompts #4-#6) add the open-access non-AI PDFs they need
to the `PDFS` list of `fetch_pdfs.py`, fetch them and list them here; the first Draft
session (prompt #4, 2026-09-23) fetched 10, JXP downloaded three paywalled Elsevier
papers for the second (prompt #5, 2026-09-23, DA48) and a fourth, Part I of the ROMS
4D-Var trilogy, for the third (prompt #6, DA52), which also fetched one open-access
Copernicus paper (DA53; last two tables below), for 44 files in all (43 papers;
`fablet2021learning` is present twice).

## Tracked in git

- `README.md`: this file.

## Private, never committed (`.gitignore` rule `context/**/*.pdf`)

Citations below were taken from Crossref (`api.crossref.org/works/<doi>`) and the arXiv
API on 2026-09-22; every DOI returned HTTP 302 from `curl -sI https://doi.org/<doi>` on
that date and again on 2026-09-23 (`build_bib.py --no-cache` and `check_sources.py`). "arXiv copy" means the publisher's PDF host returned 403 to `curl` and the
preprint was fetched instead; check the published version for differences before
quoting page numbers. Full author lists are in `reports/data_assimilation/sources.md`
under the key given in the last column.

### Anchors (read in full in prompt #1)

| File | Citation | DOI / arXiv | Access | Status | Key |
|---|---|---|---|---|---|
| `moore2019.pdf` | Moore, A. M., Martin, M. J., Akella, S., Arango, H. G., Balmaseda, M., Bertino, L., Ciavatta, S., Cornuelle, B., Cummings, J., Frolov, S., Lermusiaux, P., Oddo, P., Oke, P. R., Storto, A., Teruzzi, A., Vidard, A., Weaver, A. T., and the GODAE OceanView DA Task Team, "Synthesis of Ocean Observations Using Data Assimilation for Operational, Real-Time and Reanalysis Systems: A More Complete Picture of the State of the Ocean," *Front. Mar. Sci.* 6, 90 (2019). Mini review, 6 pp. | doi:10.3389/fmars.2019.00090 | Open access (CC BY 4.0) | Present (publisher PDF) | `moore2019synthesis` |
| `carrassi2018.pdf` | Carrassi, A., Bocquet, M., Bertino, L., and Evensen, G., "Data assimilation in the geosciences: An overview of methods, issues, and perspectives," *WIREs Clim. Change* 9(5), e535 (2018). | doi:10.1002/wcc.535; arXiv:1709.02798 | Publisher version under Wiley terms (403 to fetchers); preprint open | Present (arXiv copy, v3, 79 pp.) | `carrassi2018data` |
| `geer2021.pdf` | Geer, A. J., "Learning earth system models from observations: machine learning or data assimilation?" *Phil. Trans. R. Soc. A* 379(2194), 20200089 (2021). Correction: doi:10.1098/rsta.2022.0004 (2022). | doi:10.1098/rsta.2020.0089 | Not open access (Europe PMC `isOpenAccess: N`); publisher returned 403; no arXiv or ECMWF copy found | Present (publisher PDF, downloaded by JXP 2026-09-22) | `geer2021learning` |
| `cheng2023.pdf` | Cheng, S., Quilodrán-Casas, C., Ouala, S., Farchi, A., Liu, C., Tandeo, P., Fablet, R., Lucor, D., Iooss, B., Brajard, J., Xiao, D., Janjic, T., Ding, W., Guo, Y., Carrassi, A., Bocquet, M., and Arcucci, R., "Machine Learning With Data Assimilation and Uncertainty Quantification for Dynamical Systems: A Review," *IEEE/CAA J. Autom. Sinica* 10(6), 1361-1387 (2023). | doi:10.1109/JAS.2023.123537; arXiv:2303.10462 | Publisher paywalled (IEEE Xplore); preprint open | Present (arXiv copy, v1, 26 pp.) | `cheng2023machine` |
| `dheeshjith2025.pdf` | Dheeshjith, S., Subel, A., Adcroft, A., Busecke, J., Fernandez-Granda, C., Gupta, S., and Zanna, L., "Samudra: An AI Global Ocean Emulator for Climate," *Geophys. Res. Lett.* 52(10), e2024GL114318 (2025). | doi:10.1029/2024GL114318; arXiv:2412.03795 | Open access (CC BY 4.0) at AGU, but 403 to fetchers; preprint open | Present (arXiv copy, v4, 29 pp.) | `dheeshjith2025samudra` |
| `wang2024.pdf` | Wang, X., Wang, R., Hu, N., Wang, P., et al. (19 authors), "XiHe: A Data-Driven Model for Global Ocean Eddy-Resolving Forecasting," arXiv preprint (first posted 2024-02-05, v4 2024-10-22). No journal version found in Crossref or arXiv metadata on 2026-09-22. | arXiv:2402.02995 | Open (preprint only) | Present (arXiv v4, 18 pp.); flag `preprint` | `wang2024xihe` |
| `cui2025.pdf` | Cui, Y., Wu, R., Zhang, X., Zhu, Z., Liu, B., Shi, J., Chen, J., Liu, H., Zhou, S., Su, L., Jing, Z., An, H., and Wu, L., "Forecasting the eddying ocean with a deep neural network," *Nat. Commun.* 16, 2268 (2025). (The WenHai system.) | doi:10.1038/s41467-025-57389-2 | Open access (CC BY-NC-ND 4.0) | Present (publisher PDF, 11 pp.) | `cui2025forecasting` |
| `elaouni2025.pdf` | El Aouni, A., Gaudel, Q., Regnier, C., Van Gennip, S., Le Galloudec, O., Drevillon, M., Drillet, Y., and Lellouche, J.-M., "GLONET: Mercator's End-to-End Neural Global Ocean Forecasting System," *J. Geophys. Res.: Machine Learning and Computation* 2(3), e2025JH000686 (2025). | doi:10.1029/2025JH000686; arXiv:2412.05454 | Open access (CC BY 4.0) at AGU, but 403 to fetchers; preprint open | Present (arXiv copy, v3, 34 pp.) | `elaouni2025glonet` |

### Non-anchor AI papers (fetched 2026-09-22; skimmed for maturity tags and verification notes)

| File | Citation | DOI / arXiv | Access | Status | Key |
|---|---|---|---|---|---|
| `bi2023.pdf` | Bi, K., Xie, L., Zhang, H., Chen, X., Gu, X., and Tian, Q., "Accurate medium-range global weather forecasting with 3D neural networks," *Nature* 619, 533-538 (2023). (Pangu-Weather.) | doi:10.1038/s41586-023-06185-3 | Open access (CC BY 4.0; PMC10356604) | Present (publisher PDF, 20 pp.) | `bi2023accurate` |
| `lam2023.pdf` | Lam, R., Sanchez-Gonzalez, A., Willson, M., et al. (18 authors), "Learning skillful medium-range global weather forecasting," *Science* 382, 1416-1421 (2023). (GraphCast.) | doi:10.1126/science.adi2336; arXiv:2212.12794 | Publisher paywalled (Europe PMC `isOpenAccess: N`); preprint open | Present (arXiv copy, v2, 102 pp., titled "GraphCast: ...") | `lam2023learning` |
| `lang2024.pdf` | Lang, S., Alexe, M., Chantry, M., et al. (16 authors), "AIFS - ECMWF's data-driven forecasting system," arXiv preprint (2024). | arXiv:2406.01465 | Open (preprint only) | Present (arXiv v2, 13 pp.); flag `preprint` | `lang2024aifs` |
| `price2024.pdf` | Price, I., Sanchez-Gonzalez, A., Alet, F., et al. (12 authors), "Probabilistic weather forecasting with machine learning," *Nature* 637, 84-90 (2024; print 2025). (GenCast.) | doi:10.1038/s41586-024-08252-9 | Open access (CC BY 4.0) | Present (publisher PDF, 21 pp.) | `price2024probabilistic` |
| `hatfield2021.pdf` | Hatfield, S., Chantry, M., Dueben, P., Lopez, P., Geer, A., and Palmer, T., "Building Tangent-Linear and Adjoint Models for Data Assimilation With Neural Networks," *J. Adv. Model. Earth Syst.* 13(9), e2021MS002521 (2021). | doi:10.1029/2021MS002521 | Open access (CC BY 4.0) at AGU, 403 to fetchers; publisher PDF deposited at Zenodo record 7624565 | Present (publisher PDF via Zenodo, 16 pp.) | `hatfield2021building` |
| `xu2025.pdf` | Xu, X., Sun, X., Han, W., Zhong, X., Chen, L., Gao, Z., and Li, H., "FuXi-DA: a generalized deep learning data assimilation framework for assimilating satellite observations," *npj Clim. Atmos. Sci.* 8, 156 (2025). | doi:10.1038/s41612-025-01039-3; arXiv:2404.08522 | Open access (CC BY-NC-ND 4.0) | Present (publisher PDF, 15 pp.) | `xu2025fuxida` |
| `allen2025.pdf` | Allen, A., Markou, S., Tebbutt, W., et al. (11 authors), "End-to-end data-driven weather prediction," *Nature* 641, 1172-1179 (2025). (Aardvark Weather.) | doi:10.1038/s41586-025-08897-0 | Open access (CC BY 4.0; PMC12119340) | Present (publisher PDF, 15 pp.) | `allen2025endtoend` |
| `alexe2024.pdf` | Alexe, M., Boucher, E., Lean, P., et al. (14 authors), "GraphDOP: Towards skilful data-driven medium-range weather forecasts learnt and initialised directly from observations," arXiv preprint (2024). | arXiv:2412.15687 | Open (preprint only) | Present (arXiv v1, 23 pp.); flag `preprint` | `alexe2024graphdop` |
| `manshausen2025.pdf` | Manshausen, P., Cohen, Y., Harrington, P., et al. (10 authors), "Generative Data Assimilation of Sparse Weather Station Observations at Kilometer Scales," *J. Adv. Model. Earth Syst.* 17(10), e2024MS004505 (2025). | doi:10.1029/2024MS004505; arXiv:2406.16947 | Open access (CC BY 4.0) at AGU, 403 to fetchers; preprint open | Present (arXiv copy, v3, 25 pp.) | `manshausen2025generative` |
| `yuan2026.pdf` | Yuan, Y., Rusak, J., Merose, A., Subel, A., Perezhogin, P., Adcroft, A., Fernandez-Granda, C., and Zanna, L., "Samudra 2: Scaling Ocean Emulators across Resolutions," arXiv preprint (2026). | arXiv:2606.02610 | Open (preprint only) | Present (arXiv v2, 35 pp.); flag `preprint` | `yuan2026samudra2` |
| `chattopadhyay2024.pdf` | Chattopadhyay, A., Gray, M., Wu, T., Lowe, A. B., and He, R., "OceanNet: a principled neural operator-based digital twin for regional oceans," *Sci. Rep.* 14, 21181 (2024). | doi:10.1038/s41598-024-72145-0; arXiv:2310.00813 | Open access (CC BY 4.0; PMC11390968) | Present (publisher PDF, 10 pp.) | `chattopadhyay2024oceannet` |
| `gregory2023.pdf` | Gregory, W., Bushuk, M., Adcroft, A., Zhang, Y., and Zanna, L., "Deep Learning of Systematic Sea Ice Model Errors From Data Assimilation Increments," *J. Adv. Model. Earth Syst.* 15(10), e2023MS003757 (2023). | doi:10.1029/2023MS003757; arXiv:2304.03832 | Open access (CC BY 4.0) at AGU, 403 to fetchers; preprint open | Present (arXiv copy, v1, 38 pp.) | `gregory2023deep` |
| `fablet2021.pdf` | Fablet, R., Chapron, B., Drumetz, L., Mémin, E., Pannekoucke, O., and Rousseau, F., "Learning Variational Data Assimilation Models and Solvers," *J. Adv. Model. Earth Syst.* 13(10), e2021MS002572 (2021). | doi:10.1029/2021MS002572; arXiv:2007.12941 | Open access (CC BY 4.0) at AGU, 403 to fetchers; preprint open | Present (arXiv copy, v1 of 2020, 13 pp., under the preprint title "End-to-end learning for variational data assimilation models and solvers"; the published version is `fablet2021_james.pdf` below and is the one `sources.md` names) | `fablet2021learning` |
| `beauchamp2023.pdf` | Beauchamp, M., Febvre, Q., Georgenthum, H., and Fablet, R., "4DVarNet-SSH: end-to-end learning of variational interpolation schemes for nadir and wide-swath satellite altimetry," *Geosci. Model Dev.* 16, 2119-2147 (2023). | doi:10.5194/gmd-16-2119-2023; arXiv:2211.05904 | Open access (CC BY 4.0) | Present (publisher PDF, 29 pp.) | `beauchamp2023fourdvarnet` |
| `martin2023.pdf` | Martin, S. A., Manucharyan, G. E., and Klein, P., "Synthesizing Sea Surface Temperature and Satellite Altimetry Observations Using Deep Learning Improves the Accuracy and Resolution of Gridded Sea Surface Height Anomalies," *J. Adv. Model. Earth Syst.* 15(5), e2022MS003589 (2023). | doi:10.1029/2022MS003589 | Open access (CC BY-NC-ND 4.0) at AGU, 403 to fetchers; publisher PDF deposited at EarthArXiv | Present (publisher PDF via EarthArXiv, 26 pp.) | `martin2023synthesizing` |
| `sugiura2020.pdf` | Sugiura, N., and Hosoda, S., "Machine Learning Technique Using the Signature Method for Automated Quality Control of Argo Profiles," *Earth Space Sci.* 7(9), e2019EA001019 (2020). | doi:10.1029/2019EA001019; arXiv:1907.00500 | Open access (CC BY 4.0) at AGU, 403 to fetchers; preprint open | Present (arXiv copy, v7, 21 pp.) | `sugiura2020machine` |
| `bittig2018.pdf` | Bittig, H. C., Steinhoff, T., Claustre, H., Fiedler, B., Williams, N. L., Sauzède, R., Körtzinger, A., and Gattuso, J.-P., "An Alternative to Static Climatologies: Robust Estimation of Open Ocean CO2 Variables and Nutrient Concentrations From T, S, and O2 Data Using Bayesian Neural Networks," *Front. Mar. Sci.* 5, 328 (2018). (CANYON-B.) | doi:10.3389/fmars.2018.00328 | Open access (CC BY 4.0) | Present (publisher PDF, 29 pp.) | `bittig2018canyonb` |
| `gloege2022.pdf` | Gloege, L., Yan, M., Zheng, T., and McKinley, G. A., "Improved Quantification of Ocean Carbon Uptake by Using Machine Learning to Merge Global Models and pCO2 Data," *J. Adv. Model. Earth Syst.* 14(2), e2021MS002620 (2022). | doi:10.1029/2021MS002620 | Open access (CC BY-NC 4.0) at AGU, 403 to fetchers; publisher PDF in the NOAA Institutional Repository (noaa/59204) | Present (publisher PDF via NOAA IR, 19 pp.) | `gloege2022improved` |

### Downloaded by JXP on 2026-09-23 (Q&A DA40; read for the tags on the same day)

Each file was checked with `file` (PDF 1.4) and by `pdftotext` of its first page against
the Crossref title; all three match. These are Wiley-served PDFs and carry a per-page
"Downloaded from ... on [23/09/2026]" banner that `grep` picks up.

| File | Citation | DOI / arXiv | Access | Status | Key |
|---|---|---|---|---|---|
| `bonavita2020.pdf` | Bonavita, M., and Laloyaux, P., "Machine Learning for Model Error Inference and Correction," *J. Adv. Model. Earth Syst.* 12(12), e2020MS002232 (2020). | doi:10.1029/2020MS002232 | Open access (CC BY 4.0) at AGU, but the AGU/Wiley host returns 403 to fetchers and Unpaywall, Semantic Scholar and arXiv list no repository copy | Present (publisher PDF, 22 pp.; read in full) | `bonavita2020machine` |
| `zanna2020.pdf` | Zanna, L., and Bolton, T., "Data-Driven Equation Discovery of Ocean Mesoscale Closures," *Geophys. Res. Lett.* 47(17), e2020GL088376 (2020). | doi:10.1029/2020GL088376 | Not open access (Unpaywall `is_oa: false`); JXP's institutional copy | Present (publisher PDF, 13 pp.; skimmed, enough for the one-sentence boundary case) | `zanna2020data` |
| `fablet2021_james.pdf` | Fablet, R., Chapron, B., Drumetz, L., Mémin, E., Pannekoucke, O., and Rousseau, F., "Learning Variational Data Assimilation Models and Solvers," *J. Adv. Model. Earth Syst.* 13(10), e2021MS002572 (2021). | doi:10.1029/2021MS002572; arXiv:2007.12941 | Open access (CC BY 4.0) at AGU, 403 to fetchers | Present (publisher PDF, 15 pp.; read in full and compared with the arXiv v1 `fablet2021.pdf`: same authors, experiments and headline numbers; title changed, two Table 1 cells filled, related work expanded, code moved to Zenodo) | `fablet2021learning` |

Not wanted: the *Science* version of `lam2023learning`; the arXiv v2 in hand (102 pp.)
is the fuller document.

### Non-AI system, method and BGC papers (fetched 2026-09-23, prompt #4, per DA44)

Fetched by `fetch_pdfs.py` (each checked with `file` and by title match 1.00) for the
primer, classical-methods and systems sections of the draft. Where a publisher host refused
`curl`, a repository copy of the publisher PDF found through Unpaywall or OpenAlex was used.
Still not in hand and written from abstracts or from what the reviews say (the draft flags
each use): `cummings2013variational`, `evensen2003ensemble`
(Springer, no abstract served), `edwards2015regional`, `stammer2016ocean`, `rudnick2016ocean`
(Annual Reviews, 403; Stammer's Zenodo record 31969 returns 403 on its files),
`todd2011poleward`, `moore2018reduced` (AGU/Wiley, 403), `zaba2018annual`, `liu2023impact`,
`oke2008representation` (AMS `downloadpdf` returns an empty HTTP 202), `levin2020observation`
(Elsevier accepted manuscript, 403; abstract via Semantic Scholar), `halliwell2017north` (T&F,
closed).

| File | Citation | DOI | Access | Status | Key |
|---|---|---|---|---|---|
| `zuo2019.pdf` | Zuo, H., Balmaseda, M. A., Tietsche, S., Mogensen, K., and Mayer, M., "The ECMWF operational ensemble reanalysis-analysis system for ocean and sea ice: a description of the system and assessment," *Ocean Sci.* 15, 779-808 (2019). | doi:10.5194/os-15-779-2019 | Open access (CC BY 4.0) | Present (publisher PDF, 30 pp.; read for Section 4) | `zuo2019ecmwf` |
| `lellouche2018.pdf` | Lellouche, J.-M., et al., "Recent updates to the Copernicus Marine Service global ocean monitoring and forecasting real-time 1/12 degree high-resolution system," *Ocean Sci.* 14, 1093-1126 (2018). | doi:10.5194/os-14-1093-2018 | Open access (CC BY 4.0) | Present (publisher PDF, 34 pp.; read for Section 4) | `lellouche2018recent` |
| `lellouche2021.pdf` | Lellouche, J.-M., et al., "The Copernicus Global 1/12 degree Oceanic and Sea Ice GLORYS12 Reanalysis," *Front. Earth Sci.* 9, 698876 (2021). | doi:10.3389/feart.2021.698876 | Open access (CC BY 4.0) | Present (publisher PDF, 27 pp.; read for Sections 4 and 7.1) | `lellouche2021copernicus` |
| `forget2015.pdf` | Forget, G., Campin, J.-M., Heimbach, P., Hill, C. N., Ponte, R. M., and Wunsch, C., "ECCO version 4: an integrated framework for non-linear inverse modeling and global ocean state estimation," *Geosci. Model Dev.* 8, 3071-3104 (2015). | doi:10.5194/gmd-8-3071-2015 | Open access (CC BY 3.0) | Present (publisher PDF, 34 pp.; read for Sections 2 and 4) | `forget2015ecco` |
| `kim2024.pdf` | Kim, H.-S., et al., "Ocean component of the first operational version of Hurricane Analysis and Forecast System: Evaluation of HYbrid Coordinate Ocean Model and hurricane feedback forecasts," *Front. Earth Sci.* 12, 1399409 (2024). | doi:10.3389/feart.2024.1399409 | Open access (CC BY 4.0) | Present (publisher PDF, 70 MB; read for Sections 4 and 5) | `kim2024ocean` |
| `dong2017.pdf` | Dong, J., et al., "Impact of Assimilating Underwater Glider Data on Hurricane Gonzalo (2014) Forecasts," *Wea. Forecasting* 32, 1143-1159 (2017). | doi:10.1175/WAF-D-16-0182.1 | Open access at AMS (the `downloadpdf` host returns an empty 202 to `curl`); publisher PDF in the NOAA Institutional Repository (noaa/17960) | Present (publisher PDF via NOAA IR; read for Sections 5 and 9) | `dong2017impact` |
| `bannister2017.pdf` | Bannister, R. N., "A review of operational methods of variational and ensemble-variational data assimilation," *Q. J. R. Meteorol. Soc.* 143, 607-633 (2017). | doi:10.1002/qj.2982 | Open access (CC BY) at Wiley, 403 to fetchers; publisher PDF at CentAUR (University of Reading, 68685) | Present (publisher PDF via CentAUR; hybrid and EnVar sections read for Sections 2-3) | `bannister2017review` |
| `martin2015.pdf` | Martin, M. J., et al., "Status and future of data assimilation in operational oceanography," *J. Oper. Oceanogr.* 8(sup1), s28-s48 (2015). | doi:10.1080/1755876X.2015.1022055 | Open access (CC BY 4.0) at T&F, 403 to fetchers; publisher PDF at Figshare (article 22957895) | Present (publisher PDF via Figshare; Tables 1-2 and the methods sections read for Sections 3-5) | `martin2015status` |
| `fennel2019.pdf` | Fennel, K., et al., "Advancing Marine Biogeochemical and Ecosystem Reanalyses and Forecasts as Tools for Monitoring and Managing Ecosystem Health," *Front. Mar. Sci.* 6, 89 (2019). | doi:10.3389/fmars.2019.00089 | Open access (CC BY 4.0) | Present (publisher PDF, 9 pp.; read for Section 8 in prompt #5) | `fennel2019advancing` |
| `ford2021.pdf` | Ford, D., "Assimilating synthetic Biogeochemical-Argo and ocean colour observations into a global ocean model to inform observing system design," *Biogeosciences* 18, 509-534 (2021). | doi:10.5194/bg-18-509-2021 | Open access (CC BY 4.0) | Present (publisher PDF, 26 pp.; read for Section 8 in prompt #5; Section 9 in prompt #6) | `ford2021assimilating` |

### Downloaded by JXP on 2026-09-23 (Q&A DA48 and DA52; read in prompts #5 and #6)

Each file was checked with `file` (PDF 1.7) and by `pdftotext` of its first page against the
Crossref title. The file JXP first saved as `moore2011.pdf` (DA48) turned out to be **Part II**
of the ROMS 4D-Var trilogy rather than Part I (Q&A DA52); Part II was added to `build_bib.py`
as `moore2011romsII`, and after DA52 JXP renamed it `moore2011b.pdf` and downloaded Part I as
`moore2011a.pdf` (page-1 title "Part I - System overview and formulation", 16 pp.), which
prompt #6 read in full, so no "[not read]" flag remains on `moore2011roms`.

| File | Citation | DOI | Access | Status | Key |
|---|---|---|---|---|---|
| `moore2011a.pdf` | Moore, A. M., Arango, H. G., Broquet, G., Powell, B. S., Weaver, A. T., and Zavala-Garay, J., "The Regional Ocean Modeling System (ROMS) 4-dimensional variational data assimilation systems. Part I - System overview and formulation," *Prog. Oceanogr.* 91, 34-49 (2011). | doi:10.1016/j.pocean.2011.05.004 | Elsevier, paywalled; JXP's institutional copy | Present (publisher PDF, 16 pp.; read in full in prompt #6 for Sections 3, 5.1 and 9) | `moore2011roms` |
| `moore2011b.pdf` | Moore, A. M., Arango, H. G., Broquet, G., Edwards, C., Veneziani, M., Powell, B., Foley, D., Doyle, J. D., Costa, D., and Robinson, P., "The Regional Ocean Modeling System (ROMS) 4-dimensional variational data assimilation systems. Part II - Performance and application to the California Current System," *Prog. Oceanogr.* 91, 50-73 (2011). | doi:10.1016/j.pocean.2011.05.003 | Elsevier, paywalled; JXP's institutional copy | Present (publisher PDF, 24 pp.; read in full for Sections 3, 5.1 and 9; was `moore2011.pdf` until DA52) | `moore2011romsII` |
| `neveu2016.pdf` | Neveu, E., Moore, A. M., Edwards, C. A., Fiechter, J., Drake, P., Crawford, W. J., Jacox, M. G., and Nuss, E., "An historical analysis of the California Current circulation using ROMS 4D-Var: System configuration and diagnostics," *Ocean Modelling* 99, 133-151 (2016). | doi:10.1016/j.ocemod.2015.11.012 | Elsevier, paywalled; JXP's institutional copy | Present (publisher PDF, 19 pp.; read in full for Section 5.1) | `neveu2016historical` |
| `shulman2009.pdf` | Shulman, I., Rowley, C., Anderson, S., DeRada, S., Kindle, J., Martin, P., Doyle, J., Cummings, J., Ramp, S., Chavez, F., Fratantoni, D., and Davis, R., "Impact of glider data assimilation on the Monterey Bay model," *Deep-Sea Res. II* 56, 188-198 (2009). | doi:10.1016/j.dsr2.2008.08.003 | Elsevier, paywalled; JXP's institutional copy | Present (publisher PDF, 11 pp.; read in full, for Section 9 in prompt #6) | `shulman2009impact` |

### Fetched 2026-09-23 (prompt #6, Q&A DA53; read in full)

Found while looking for a citable record of glider assimilation in the UCSC California Current
ROMS 4D-Var system (DA53); fetched by `fetch_pdfs.py` (`file` = PDF 1.5, title match 1.00).
The companion grey source, the UCSC near-real-time page
`https://oceanmodeling.ucsc.edu/ccsnrt/` (`ucsc2026ccsnrt`, HTTP 200), is a web page and has
no file here; its TLS certificate chain is incomplete for some clients (`curl -k` needed).

| File | Citation | DOI | Access | Status | Key |
|---|---|---|---|---|---|
| `mattern2026.pdf` | Mattern, J. P., Takeshita, Y., Rocha, C., and Edwards, C. A., "Improving coastal ocean pH estimates through assimilation of glider observations and hybrid statistical methods," *Biogeosciences* 23, 2621-2639 (2026). | doi:10.5194/bg-23-2621-2026 | Open access (Copernicus, CC BY 4.0) | Present (publisher PDF, 19 pp.; read in full for Sections 5.1, 8 and 9) | `mattern2026improving` |

Also checked and not added: Kurapov et al. (2017, *Ocean Dyn.* 67, 23-36,
doi:10.1007/s10236-016-1013-4), the WCOFS paper named as a fallback in `reading_list.md`;
its abstract (Springer landing page) concerns sea-level verification against tide gauges
and does not describe the WCOFS data assimilation, so it would not fill the gap the draft
flags for WCOFS (Q&A DA49).
