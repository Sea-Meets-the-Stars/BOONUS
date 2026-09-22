# context/da/

Anchor papers for the data assimilation (DA) and AI review
(`reports/data_assimilation/`, see `claude_prompts/data_assimilation_prompts.md`).
The list was fixed in the DA Q&A, rounds 1-2 (DA15, DA21, DA30) in
`claude_prompts/context_prompts.md`.

## Tracked in git

- `README.md`: this file.

## Private, never committed (`.gitignore` rule `context/**/*.pdf`)

Citations below were taken from Crossref (`api.crossref.org/works/<doi>`) and the arXiv
API on 2026-09-22; every DOI returned HTTP 302 from `curl -sI https://doi.org/<doi>` on
that date. "arXiv copy" means the publisher's PDF host returned 403 to `curl` and the
preprint was fetched instead; check the published version for differences before
quoting page numbers.

| File | Citation | DOI / arXiv | Access | Status |
|---|---|---|---|---|
| `moore2019.pdf` | Moore, A. M., Martin, M. J., Akella, S., Arango, H. G., Balmaseda, M., Bertino, L., Ciavatta, S., Cornuelle, B., Cummings, J., Frolov, S., Lermusiaux, P., Oddo, P., Oke, P. R., Storto, A., Teruzzi, A., Vidard, A., Weaver, A. T., and the GODAE OceanView DA Task Team, "Synthesis of Ocean Observations Using Data Assimilation for Operational, Real-Time and Reanalysis Systems: A More Complete Picture of the State of the Ocean," *Front. Mar. Sci.* 6, 90 (2019). Mini review, 6 pp. | doi:10.3389/fmars.2019.00090 | Open access (CC BY 4.0) | Present (publisher PDF) |
| `carrassi2018.pdf` | Carrassi, A., Bocquet, M., Bertino, L., and Evensen, G., "Data assimilation in the geosciences: An overview of methods, issues, and perspectives," *WIREs Clim. Change* 9(5), e535 (2018). | doi:10.1002/wcc.535; arXiv:1709.02798 | Publisher version under Wiley terms (403 to fetchers); preprint open | Present (arXiv copy, v3, 79 pp.) |
| `geer2021.pdf` | Geer, A. J., "Learning earth system models from observations: machine learning or data assimilation?" *Phil. Trans. R. Soc. A* 379(2194), 20200089 (2021). Correction: doi:10.1098/rsta.2022.0004 (2022). | doi:10.1098/rsta.2020.0089 | Not open access (Europe PMC `isOpenAccess: N`); publisher returned 403; no arXiv or ECMWF copy found | Present (publisher PDF, downloaded by JXP 2026-09-22) |
| `cheng2023.pdf` | Cheng, S., Quilodrán-Casas, C., Ouala, S., Farchi, A., Liu, C., Tandeo, P., Fablet, R., Lucor, D., Iooss, B., Brajard, J., Xiao, D., Janjic, T., Ding, W., Guo, Y., Carrassi, A., Bocquet, M., and Arcucci, R., "Machine Learning With Data Assimilation and Uncertainty Quantification for Dynamical Systems: A Review," *IEEE/CAA J. Autom. Sinica* 10(6), 1361-1387 (2023). | doi:10.1109/JAS.2023.123537; arXiv:2303.10462 | Publisher paywalled (IEEE Xplore); preprint open | Present (arXiv copy, v1, 26 pp.) |
| `dheeshjith2025.pdf` | Dheeshjith, S., Subel, A., Adcroft, A., Busecke, J., Fernandez-Granda, C., Gupta, S., and Zanna, L., "Samudra: An AI Global Ocean Emulator for Climate," *Geophys. Res. Lett.* 52(10), e2024GL114318 (2025). | doi:10.1029/2024GL114318; arXiv:2412.03795 | Open access (CC BY 4.0) at AGU, but 403 to fetchers; preprint open | Present (arXiv copy, v4, 29 pp.) |
| `wang2024.pdf` | Wang, X., Wang, R., Hu, N., Wang, P., et al., "XiHe: A Data-Driven Model for Global Ocean Eddy-Resolving Forecasting," arXiv preprint (first posted 2024-02-05). No journal version found in Crossref or arXiv metadata on 2026-09-22. | arXiv:2402.02995 | Open (preprint only) | Present (arXiv v4, 18 pp.); flag `preprint` |
| `cui2025.pdf` | Cui, Y., Wu, R., Zhang, X., Zhu, Z., Liu, B., Shi, J., Chen, J., Liu, H., Zhou, S., Su, L., Jing, Z., An, H., and Wu, L., "Forecasting the eddying ocean with a deep neural network," *Nat. Commun.* 16, 2268 (2025). (The WenHai system.) | doi:10.1038/s41467-025-57389-2 | Open access (CC BY-NC-ND 4.0) | Present (publisher PDF, 11 pp.) |
| `elaouni2025.pdf` | El Aouni, A., Gaudel, Q., Regnier, C., Van Gennip, S., Le Galloudec, O., Drevillon, M., Drillet, Y., and Lellouche, J.-M., "GLONET: Mercator's End-to-End Neural Global Ocean Forecasting System," *J. Geophys. Res.: Machine Learning and Computation* 2(3), e2025JH000686 (2025). | doi:10.1029/2025JH000686; arXiv:2412.05454 | Open access (CC BY 4.0) at AGU, but 403 to fetchers; preprint open | Present (arXiv copy, v3, 34 pp.) |

Author lists for Wang et al. (XiHe) are truncated to the first four as returned by the
arXiv API; take the full list from the PDF when writing `sources.bib`.

Also noted while searching (not fetched): Yuan, Y., Rusak, J., Merose, A., Subel, A., et
al., "Samudra 2: Scaling Ocean Emulators across Resolutions," arXiv:2606.02610 (posted
2026-05-24), a candidate for the reading list.
