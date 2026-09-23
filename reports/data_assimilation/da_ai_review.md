# Data assimilation in oceanography and where AI enters it

**Version:** v0.1 draft · **Date:** 2026-09-23 · **Authors:** J. Xavier Prochaska and Claude ·
**Audience:** JXP; to be shared with Matt Mazloff at v0.2 ·
**Apparatus:** `outline.md`, `reading_list.md`, `sources.md` / `sources.bib` (shared BibTeX
keys), `scripts/` (this directory). A review, not a BOONUS document.

| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 draft | 2026-09-23 | JXP and Claude (Fable 5.1) | Skeleton from `outline.md`; drafted the primer (Section 2), classical methods (3), global systems (4), regional and coastal systems with the systems table (5); placeholders for 0 and 6-11 (prompts 5-6). |
| v0.1 draft | 2026-09-23 | JXP and Claude (Fable 5.1) | Prompt 5. Section 3 (4D-Var), 5.1 and the California Current row of Table 1 rewritten from the full text of Moore et al. (2011, Part II) and Neveu et al. (2016): the "[not read]" flags replaced by the WC30/WC10 and WCRA31/WCRA14 configurations and diagnostics; Part II added as `moore2011romsII` (JXP's `moore2011.pdf` is Part II, Q&A DA52); the earlier "gliders included" statement about the Neveu reanalysis corrected (EN3 profiles; gliders not named; no velocity data). Drafted Section 6 (NWP), Section 7 with 7.1-7.4 (ocean AI by taxonomy, circularity caveat stated in the Section 7 opening), Section 8 (BGC); Figure 1 and 2 placeholders; candidate questions for Section 11 from Q&A DA49, DA50, DA53. |

**Citation convention.** Author-year in the text followed by the BibTeX key in brackets,
e.g. Moore et al. (2019) [@moore2019synthesis]; the bare bracketed key is used on repeat
mention.
Only keys present in `sources.bib` are cited (checked by `scripts/check_citations.py`).
Items that are not peer-reviewed carry a flag after the citation: **(preprint)** for
arXiv-only papers, **(grey)** for web pages, repositories and reports. Two further flags
mark the evidential basis of a statement, per `outline.md` (DA44): **[abstract only]**
means the paper's full text was not in hand and the statement rests on its abstract;
**[not read; via `key`]** means neither the text nor an abstract was available and the
statement rests on what the named source says about the paper. Both flags are collected
by the verification pass (prompt 8). Every quantitative statement in Sections 2-8 traces
to a source read in the drafting sessions unless so flagged; the maturity tags and
verification notes of Sections 6-8 are those of `sources.md`, which rest on the full text
of every AI paper cited.

---

## 0. Executive summary

*[Placeholder: one page, written last in prompt 6. What operational ocean DA is today (two
method families, a handful of global systems, ROMS 4D-Var and its relatives on U.S.
coasts); that AI entered NWP first as emulators and is now entering the assimilation step;
that the ocean emulators are trained on reanalyses that are themselves DA products, so
verification against withheld observations is the test that matters; what remains open for
BGC and for gliders. No BOONUS pitch.]*

## 1. Introduction and scope

This report describes the state of data assimilation (DA) in oceanography and where
machine learning (ML) has entered it, for a reader who knows statistical inference but not
the DA literature. It was written to educate JXP and will be shared with Matt Mazloff; it
is a review, not a case for BOONUS, and it stops short of implications for any particular
observing network.

DA is, in the community's own words, "the rigorous and systematic combination of ocean
observations and ocean models that yields an optimal estimate of the ocean state," where
optimal means the maximum of a posterior probability under stated error assumptions
(Moore et al. 2019 [@moore2019synthesis]). The scope here follows the decisions recorded in
`claude_prompts/data_assimilation_prompts.md`: roughly one third on the global systems
(Section 4) and two thirds on regional and coastal systems (Sections 5, 8, 9 and parts of
7), with reanalysis and state estimation kept distinct from operational forecasting
throughout; classical methods in brief (Sections 2-3); the AI literature concentrated on
2019-2026, organized by where ML enters the DA pipeline (Section 7) after a look at
numerical weather prediction (NWP) as the leading indicator (Section 6); a full
biogeochemical (BGC) section (8); and a glider-specific section (9). Every AI approach in
Sections 6-8 carries a maturity tag (`idealized`, `realistic hindcast`, `pre-operational`,
`operational`) and a verification note stating whether its skill was measured against
withheld observations or against the reanalysis it was trained on; the latter distinction
is the central caveat of the AI half of the report. The one boxed section of mathematics
(Section 2) fixes the vocabulary that the rest of the report uses; readers who know DA can
skip it.

## 2. Box: DA primer (skippable for DA specialists)

---

**Box 1. The three ideas behind every operational ocean DA system.** The derivations follow
Carrassi et al. (2018) [@carrassi2018data]; the operational notation follows Bannister
(2017) [@bannister2017review]; the ML correspondences follow Geer (2021)
[@geer2021learning].

**2.1 Notation**

| Symbol | Meaning | Size |
|---|---|---|
| $\mathbf{x}$ | model state (all prognostic fields on the grid, stacked) | $m$ ($10^7$-$10^9$ in practice) |
| $\mathbf{x}^b$, $\mathbf{x}^a$, $\mathbf{x}^f$ | background (prior, usually the previous forecast), analysis (posterior), forecast | $m$ |
| $\mathbf{y}$ | observations in one assimilation window | $d \ll m$ |
| $\mathcal{H}$, $\mathbf{H}$ | observation operator mapping state to observation space, and its linearization | $d \times m$ |
| $\mathcal{M}_{k:k-1}$, $\mathbf{M}$ | model integration from $t_{k-1}$ to $t_k$, and its tangent-linear model (TLM); $\mathbf{M}^{\mathsf T}$ is the adjoint | $m \times m$ |
| $\mathbf{B}$ (also $\mathbf{P}^b$, $\mathbf{P}^f$) | background-error covariance | $m \times m$, never formed explicitly |
| $\mathbf{R}$ | observation-error covariance: instrument error plus representativeness error (what the observation sees that the model cannot represent) | $d \times d$, usually diagonal |
| $\mathbf{Q}$ | model-error covariance (weak-constraint methods only) | $m \times m$ |
| $\mathbf{d} = \mathbf{y} - \mathcal{H}(\mathbf{x}^b)$ | innovation (observation minus background) | $d$ |
| $\delta\mathbf{x} = \mathbf{x}^a - \mathbf{x}^b$ | analysis increment | $m$ |
| $\mathbf{K}$ | gain: how much of each innovation is added to the state, and where | $m \times d$ |
| $J$ | cost function (negative log posterior up to a constant) | scalar |
| $N$ | ensemble size | 5-100 in ocean systems |

**2.2 The linear Gaussian update.** If the prior is $\mathbf{x} \sim \mathcal{N}(\mathbf{x}^b,
\mathbf{B})$, observations are $\mathbf{y} = \mathbf{H}\mathbf{x} + \boldsymbol{\epsilon}$
with $\boldsymbol{\epsilon} \sim \mathcal{N}(0, \mathbf{R})$ independent of the prior, then
the posterior is Gaussian with mean and covariance

$$
\mathbf{x}^a = \mathbf{x}^b + \mathbf{K}\,(\mathbf{y} - \mathbf{H}\mathbf{x}^b), \qquad
\mathbf{K} = \mathbf{B}\mathbf{H}^{\mathsf T}\left(\mathbf{H}\mathbf{B}\mathbf{H}^{\mathsf T} + \mathbf{R}\right)^{-1}, \qquad
\mathbf{P}^a = (\mathbf{I} - \mathbf{K}\mathbf{H})\,\mathbf{B}.
$$

$\mathbf{K}$ "contains the regression coefficients of the optimal linear combination
between the prior and the observations"; the analysis is the minimum-variance unbiased
linear estimate whether or not the errors are Gaussian, the BLUE [@carrassi2018data].
Everything in operational DA is a way of applying this update when $m$ is $10^8$, $\mathbf{B}$
cannot be stored, $\mathcal{H}$ and $\mathcal{M}$ are nonlinear, and the state evolves between
observations. Cycled through time with a linear model, $\mathbf{x}^f_k = \mathbf{M}\mathbf{x}^a_{k-1}$
and $\mathbf{P}^f_k = \mathbf{M}\mathbf{P}^a_{k-1}\mathbf{M}^{\mathsf T} + \mathbf{Q}$, this is
the Kalman filter, exact for linear dynamics and Gaussian errors; the covariance propagation
is what no ocean model can afford, which is why the two families below exist.

*Analogy (exact).* With $\mathbf{B}$ prescribed and static and $\mathbf{H}$ linear, the update
is optimal interpolation (OI), and it is identical to Gaussian-process (GP) regression, or
simple kriging with known mean $\mathbf{x}^b$ and covariance kernel $\mathbf{B}$: the
posterior mean at unobserved grid points is the kriging predictor. *Where it breaks:* OI
prescribes $\mathbf{B}$ from physical balance relations and model statistics and does not fit
its hyperparameters by marginal likelihood; in a cycled system the effective prior
covariance changes every cycle even when $\mathbf{B}$ is nominally static; and nonlinear
$\mathcal{H}$ (satellite radiances, or salinity from a glider conductivity cell) takes the
problem outside GP regression.

**2.3 Variational methods.** Write the negative log posterior for one window. Three-dimensional
variational assimilation (3D-Var) treats all observations in the window as valid at one time,

$$
J_{\mathrm{3D}}(\mathbf{x}) = \tfrac12\,\|\mathbf{x} - \mathbf{x}^b\|^2_{\mathbf{B}^{-1}}
 + \tfrac12\,\|\mathbf{y} - \mathcal{H}(\mathbf{x})\|^2_{\mathbf{R}^{-1}},
$$

and its minimizer is the update of 2.2 when $\mathcal{H}$ is linear, found by iterative descent
on the gradient rather than by forming $\mathbf{K}$. Strong-constraint 4D-Var respects the
observation times $t_k$ inside the window and assumes a perfect model,

$$
J_{\mathrm{4D}}(\mathbf{x}_0) = \tfrac12\,\|\mathbf{x}_0 - \mathbf{x}^b\|^2_{\mathbf{B}^{-1}}
 + \tfrac12 \sum_{k=0}^{K} \|\mathbf{y}_k - \mathcal{H}_k\!\left(\mathcal{M}_{k:0}(\mathbf{x}_0)\right)\|^2_{\mathbf{R}_k^{-1}},
\qquad
\nabla_{\mathbf{x}_0} J_{\mathrm{4D}} = \mathbf{B}^{-1}(\mathbf{x}_0 - \mathbf{x}^b)
 - \sum_{k} \mathbf{M}_{k:0}^{\mathsf T}\mathbf{H}_k^{\mathsf T}\mathbf{R}_k^{-1}\left[\mathbf{y}_k - \mathcal{H}_k\!\left(\mathcal{M}_{k:0}(\mathbf{x}_0)\right)\right],
$$

so the control variable is the state at the start of the window alone and the gradient needs
the adjoint $\mathbf{M}^{\mathsf T}_{k:0}$, a backward integration that carries each
observation's influence to $t_0$ [@carrassi2018data]. Weak-constraint 4D-Var drops the
perfect-model assumption by adding $\tfrac12\sum_k \|\mathbf{x}_k -
\mathcal{M}_{k:k-1}(\mathbf{x}_{k-1})\|^2_{\mathbf{Q}_k^{-1}}$ and taking the whole trajectory
as control, at the price of specifying $\mathbf{Q}$ and a control vector of size $m \times K$.
Operational systems use the incremental form (Courtier et al. 1994, via
[@carrassi2018data]): the cost is made quadratic in $\delta\mathbf{x}_0$ by linearizing
$\mathcal{H}$ and $\mathcal{M}$ about the background trajectory (inner loop, often at reduced
resolution), and the trajectory is re-linearized a few times (outer loops).

*Analogy (exact).* Minimizing $J_{\mathrm{4D}}$ is maximum a posteriori (MAP) estimation of
$\mathbf{x}_0$ with the dynamics as the prior over trajectories: for Gaussian errors,
$\ln p(\mathbf{x}_{K:0}\,|\,\mathbf{y}_{K:0}) = -J + \text{const}$, and in the linear case the
weak-constraint minimizer coincides with the Kalman smoother and the strong-constraint
minimizer at $t_K$ with the Kalman filter [@carrassi2018data]. In ML terms, $J$ is the loss,
the adjoint is backpropagation through the model, and the observation term is a squared
loss with per-datum weights $\mathbf{R}^{-1}$; the background term has no counterpart in
standard ML, and Tikhonov regularization of weights corresponds to a Gaussian prior with
mean zero and unit variance [@geer2021learning]. *Where it breaks:* for a nonlinear model
the descent finds a local minimum of a non-convex $J$; incremental 4D-Var solves a sequence
of quadratic approximations, not the MAP problem itself; and no operational system computes
the posterior covariance (the inverse Hessian), so 4D-Var delivers a point estimate.

**2.4 Ensemble methods.** The ensemble Kalman filter (EnKF; Evensen 2003
[@evensen2003ensemble] is the standard reference [not read; via `carrassi2018data`]) replaces
$\mathbf{B}$ by the sample covariance of $N$ model states $\mathbf{x}_n$ with anomaly matrix
$\mathbf{X}$ (columns $(\mathbf{x}_n - \bar{\mathbf{x}})/\sqrt{N-1}$),

$$
\mathbf{P}^e = \mathbf{X}\mathbf{X}^{\mathsf T}, \qquad
\mathbf{K}_e = \mathbf{P}^e\mathbf{H}^{\mathsf T}\left(\mathbf{H}\mathbf{P}^e\mathbf{H}^{\mathsf T} + \mathbf{R}\right)^{-1},
$$

so that the update lives in the $N$-dimensional span of the ensemble and needs neither a
tangent-linear nor an adjoint model; the forecast step is $N$ runs of the nonlinear model.
In the stochastic EnKF each member assimilates observations perturbed with noise drawn from
$\mathbf{R}$; deterministic (square-root) variants such as the ETKF, EAKF and DEnKF update
the mean with $\mathbf{K}_e$ and transform the anomalies so that the posterior variance is
matched without perturbing the observations [@carrassi2018data]. Two fixes are unavoidable
because $N \ll m$. *Localization:* the sampling error of the covariance between two distant
grid points $i$ and $j$ is
$\mathbb{E}\,[\mathbf{P}^e - \mathbf{B}]^2_{ij} = \tfrac{1}{N-1}\left([\mathbf{B}]^2_{ij} + [\mathbf{B}]_{ii}[\mathbf{B}]_{jj}\right)$,
which does not vanish with distance although the true $[\mathbf{B}]_{ij}$ does, so the
sample covariance carries spurious long-range correlations and is rank-deficient; the
remedy is a Schur (element-wise) product with a compactly supported correlation function
(Gaspari-Cohn) or a set of independent local analyses. *Inflation:* residual sampling error
and model error shrink the ensemble spread cycle after cycle, so the anomalies are
inflated by a factor $\lambda \geq 1$ (or additive noise) that must be tuned or adapted;
"without counter-measures, the divergence of the EnKF in high-dimensional geophysical
systems is almost systematic" [@carrassi2018data].

*Analogy (exact in a limit).* The EnKF is a Monte Carlo Kalman filter: for linear dynamics
and Gaussian errors the stochastic EnKF converges to the Kalman filter at rate $1/\sqrt{N}$
(Le Gland et al. 2009, via [@carrassi2018data]). *Where it breaks:* for a nonlinear model the
forecast step is a correct Monte Carlo propagation but the analysis step is the linear
update of 2.2 applied to a non-Gaussian ensemble, so it does not solve Bayes' rule; and
localization and inflation are regularizations with no Monte Carlo interpretation.

**2.5 Hybrids and the long-window smoother.** Operational hybrids replace $\mathbf{B}$ by
$\mathbf{B}_h = (1-\beta)\,\mathbf{B}_0 + \beta\,\mathbf{P}^e$, a weighted average of the
static, full-rank, crudely modelled $\mathbf{B}_0$ and the flow-dependent, rank-deficient
$\mathbf{P}^e$ [@bannister2017review]; ensemble-variational (EnVar) methods go further and
use ensemble trajectories in place of the TLM and adjoint inside a 4D cost function
(4DEnVar). ECCO (Section 4.1) is the other limit: one window of two decades, the adjoint
method, and controls that include the initial state, surface forcing and mixing parameters
(Forget et al. 2015 [@forget2015ecco]). *Analogy:* ECCO is a long-window smoother in the
sense of 2.3, every observation in the window informing every earlier time. *Where it
breaks:* it treats model error by adjusting forcing and parameters rather than by adding
increments, so that "it avoids adding source/sink terms of unknown nature to the model
equations," a property the authors note does not hold for sequential schemes or for 4D-Var
as practiced in NWP [@forget2015ecco]; and it returns a single approximate minimum with no
posterior error estimate.

*End of Box 1.*

---

## 3. Classical methods in brief

Two families of sequential method serve nearly all operational and reanalysis systems, and
Moore et al. (2019) [@moore2019synthesis] describe the trade-off between them from the
operational side. This section names the variants that Sections 4 and 5 will refer to.

**OI and EnOI.** Optimal interpolation applies the update of Box 2.2 with a prescribed,
static $\mathbf{B}$; it is the form of the static matrix $\mathbf{C}$ that hybrids blend
with an ensemble [@carrassi2018data]. Ensemble OI (EnOI) estimates $\mathbf{B}$ once from a
time-invariant collection of model anomalies and reuses it every cycle; Moore et al. (2019)
list it among the "less-optimal and more practical approaches" used when a full EnKF is too
costly, and the Australian Bluelink system runs it (Martin et al. 2015 [@martin2015status]).
The SEEK filter used at Mercator is a reduced-order relative: the background error is
represented on a fixed basis of a few hundred anomalies from a long free run (Section 4.2).

**3D-Var and FGAT.** In 3D-Var all observations in a window of order days are treated as if
taken at one time; first guess at appropriate time (FGAT) computes each innovation against
the background interpolated to the observation's own time before solving the single-time
problem, which keeps the cost of a 3D-Var while removing the worst of the timing error
[@moore2019synthesis]. Only the nonlinear model is needed, which is why 3D-Var FGAT is the
choice of ECMWF, the Met Office and the U.S. Navy systems (Sections 4.1-4.2).

**4D-Var.** 4D-Var respects observation times and lets the model equations interpolate
information in space and time across the window, which introduces flow dependence into the
effective $\mathbf{B}$ through the TLM and adjoint. The costs are the additional
computation, the development and maintenance of the TLM and adjoint, and the fact that
"traditional 4D-Var methods are iterative sequential algorithms and are not readily
parallelizable in time" [@moore2019synthesis]. Whether 4D-Var beats 3D-Var for the ocean as
it has in NWP is, in the community's own assessment, "still an open question"
[@moore2019synthesis]. Both strong- and weak-constraint forms exist; the ROMS 4D-Var
system of Section 5.1 offers three incremental algorithms: I4D-Var, a primal (control-space)
strong-constraint scheme, and two dual (observation-space) schemes, 4D-PSAS and the indirect
representer R4D-Var, which alone support the weak constraint (Moore et al. 2011, Part I
[@moore2011roms] [not read; via Part II, Moore et al. 2011 [@moore2011romsII]]). In the
California Current all three converge to the same analysis for a single outer loop, but the
dual schemes "converge to the minimum of J more slowly" and visit unphysical states on the
way, so they must be run to convergence [@moore2011romsII].

**EnKF, stochastic and deterministic.** The EnKF needs only the nonlinear model and
parallelizes across members, and it delivers a flow-dependent $\mathbf{B}$ and a forecast
uncertainty estimate; the price is the ensemble integrations and the localization and
inflation of Box 2.4, which "can degrade the dynamical consistency of the computed
analyses" [@moore2019synthesis]. The one long-running operational ocean EnKF is TOPAZ (MET
Norway, North Atlantic and Arctic): near-real-time since January 2003 with the stochastic
EnKF, deterministic (DEnKF) since January 2010 [@carrassi2018data], 100 members with a
300 km localization radius and inflation applied by inflating the observation error used
for the anomaly update [@martin2015status]. ECMWF's ORAS5 uses a five-member ensemble, but
for uncertainty and observation perturbation rather than for $\mathbf{B}$ (Section 4.1).

**Hybrids.** Blending a static and an ensemble covariance (Box 2.5) is, per Moore et al.
(2019), "perhaps the most immediate development borrowed from NWP," where hybrid and EnVar
schemes are now standard [@bannister2017review]; in the ocean, efforts for global and
regional systems were "underway" in 2019 [@moore2019synthesis]. The U.S. JEDI/SOCA
framework (Section 4.2) is the vehicle for that step in the NOAA systems.

**What neither family has solved.** Moore et al. (2019) name the shared problems:
specifying $\mathbf{B}$, in particular how surface information (sea level) is spread to the
subsurface; model error and bias, which "violates the fundamental assumption that
underpins current approaches"; observation error $\mathbf{R}$, of which representativeness
error "is probably the most significant contributor ... and is perhaps the least well
understood" (citing Oke and Sakov 2008 [@oke2008representation]); and initialization shock,
mitigated in practice by adding the increment gradually over the cycle (incremental
analysis update, IAU) rather than at once. Every system in Sections 4-5 carries a version
of each.

## 4. Global systems: reanalysis and state estimation vs operational forecasting

The same centres produce two kinds of product with different aims, and the report keeps
them apart. A *reanalysis* or *state estimate* is run behind real time with reprocessed,
quality-controlled observations and an atmospheric reanalysis as forcing, and is judged on
climate-scale consistency; an *operational analysis-forecast* is run daily or weekly with
whatever observations have arrived, and is judged on forecast skill at 1-10 days. Sequential
reanalyses restart the model at every cycle, so "the conservation laws of the system may not
be continuously respected" and budgets need the analysis increments included explicitly; the
adjoint state estimate integrates the model once over a multi-decade window so that
conservation holds by construction [@moore2019synthesis]. Because the products differ in
method, "data assimilation products must be used judiciously and selected according to the
specific purpose, as not all related inferences would be equally reliable" (Stammer et al.
2016 [@stammer2016ocean]) [abstract only]. Table 1 (Section 5.6) has one row per system; the
paragraphs below give only what the table cannot hold.

### 4.1 Reanalysis and state estimation

**ECMWF ORAS5** (Zuo et al. 2019 [@zuo2019ecmwf]) is a sequential reanalysis: NEMO at 0.25
degree with 75 levels, NEMOVAR 3D-Var FGAT in 5-day windows with IAU, five members that
perturb observations and forcing (the control member is unperturbed), from 1979 onward.
It assimilates in situ T/S profiles (EN4, then the GTS from 2015), along-track sea level
anomaly (SLA) and sea-ice concentration; SST is nudged, not assimilated. The paper
quantifies what the observations buy: over 2005-2014 in situ profiles account for 65% of
the total RMSE reduction in temperature and nearly 90% in salinity, with Argo "the most
influential observation type". Stated deficiencies: sea-level variance underestimated by
about a quarter, large SST biases in the Gulf Stream, an upper-300 m ensemble spread too
small by about a factor of 2, and an error level that tracks the evolving observing system.
Gliders are not named; they enter, if at all, through the EN4 and GTS profile streams.

**Mercator/Copernicus GLORYS12** (Lellouche et al. 2021 [@lellouche2021copernicus]) is the
eddy-resolving reanalysis: NEMO at 1/12 degree (9.25 km at the equator, about 4.5 km at
subpolar latitudes), 50 levels, ERA-Interim forcing, run from December 1991 to December
2019 with the Mercator operational scheme of Section 4.2 (SEEK-derived reduced-order Kalman
filter, 7-day cycle, IAU, plus a 3D-Var correction of large-scale T/S biases). It
assimilates reprocessed SLA, AVHRR SST, sea-ice concentration and CORA in situ profiles
(Argo plus sea-mammal profiles). Accuracy against the assimilated profiles in 0-2000 m is
about 0.75 C and 0.2 psu over 1993-2002 and 0.45 C and 0.1 psu in the Argo period; the SLA
residual is about 5.5 cm, and "the major source of error in sea level comes from the
uncertainty of the MDT". The authors state that "the performance of the reanalysis shows a
clear dependency on the time-dependent in situ observation system": Argo's arrival in 2004
halved the departures from in situ data, the pre-2004 salinity bias could not be corrected,
the eddy-kinetic-energy record has discontinuities in 2002 and 2004, and the warming trend
is higher than observed with excess heat storage near 100 m. Gliders are not mentioned.
GLORYS12 matters twice here: as the 1/12 degree reference for the eastern Pacific, and as the
training set of the XiHe, WenHai and GLONET emulators of Section 7.1, which inherit these
properties.

**ECCO version 4** (Forget et al. 2015 [@forget2015ecco]) is the one global product built as a
single inverse problem: the MITgcm at a nominal 1 degree fitted over 1992-2011 by the adjoint
method through 45 iterations, with the initial T/S, time-mean mixing parameters and
bi-weekly atmospheric adjustments as controls, and about 1.9 million temperature and 1.24
million salinity profiles (Argo, CTD, XBT, ice-tethered profilers, elephant seals), SLA, a
mean dynamic topography, SST and sea-ice cover as constraints; gliders are not among them.
The result is "a dynamically consistent ocean state estimate without unidentified sources
of heat and buoyancy", with budgets closed to machine precision, and a normalized squared
misfit to hydrography of about 1.5 for both T and S (1 would mean perfectly specified
errors). The authors name "the lack of 'posterior' error estimates" as the most outstanding
issue, with the under-observed abyss and a global heat uptake of "high ... structural
uncertainty". ECCO is the parent of the regional adjoint state estimates of Section 5.2 and
of the BGC state estimates of Section 8; the brief names it for BOONUS boundary conditions.

### 4.2 Operational forecasting

**Mercator GLO12 (PSY4V3)** (Lellouche et al. 2018 [@lellouche2018recent]) has run since 19
October 2016 with weekly analyses and daily 10-day forecasts: NEMO at 1/12 degree, the SAM
assimilation (a SEEK-derived reduced-order Kalman filter with a fixed basis of 250 anomalies
from 2007-2015, 7-day cycle, localization, IAU, and the 3D-Var bias correction), no
ensemble. Skill against the assimilated data: SLA forecast RMS below 6 cm, SST innovation
RMS 0.45 C, T/S departures that "rarely exceed 0.5 C and 0.1 psu" except in the thermocline
and the western boundary currents, and mid-latitude surface currents 20-60% too weak
against drifters. Gliders are not named in the paper; Martin et al. (2015)
[@martin2015status] list them among the profile platforms Mercator receives through Coriolis.
GLO12 is the operational baseline the WenHai and GLONET emulators of Section 7.1 are
compared against, and GLORYS12 is its behind-real-time twin.

**ECMWF OCEAN5-RT** is the ORAS5 system run daily with a variable 8-12 day window started
from the last behind-real-time analysis, GTS in situ data, near-real-time SLA and
operational OSTIA, to supply initial conditions to the ECMWF ensemble (since November 2016),
seasonal (SEAS5, November 2017) and high-resolution (HRES, June 2018) forecasts
[@zuo2019ecmwf]; one system, two delays, the cleanest example of the split this section is
about.

**NOAA Global RTOFS** is HYCOM at 1/12 degree, run daily for 2 days of nowcast and 8 days
of forecast, with initial conditions "assimilated with timely available observations by the
flow-dependent 3DVar DA algorithm (Cummings, 2005 ...)" (Kim et al. 2024 [@kim2024ocean]),
that is, the Navy's NCODA (Cummings and Smedstad 2013 [@cummings2013variational]) [not read;
via `kim2024ocean` and `martin2015status`]. Neither Kim et al. nor the NCEP product page
(NCEP Central Operations 2026 [@rtofs2026ncep]) (grey) lists the assimilated observation
types. RTOFS supplies the ocean initial conditions of the operational hurricane model
(Section 5.5).

**U.S. Navy GOFS (HYCOM/NCODA).** In the GODAE OceanView intercomparison (Martin et al.
2015 [@martin2015status]) GOFS ran HYCOM at 1/12.5 degree with NCODA 3D-Var FGAT, a daily
cycle and IAU over 6 hours, assimilating swath SST, in situ SST, SLA, sea ice, and T/S
profiles from "Argo, XBT, CTD, moored buoys, gliders, marine mammals, from GTS and US Navy
sources". The same paper records that all eight GODAE systems drew on "a similar set of
platforms ... including Argo floats, XBTs (for temperature), moored buoys, gliders and
marine mammals", the earliest statement in this reading list that glider profiles are
routinely in the global operational streams.

**JEDI/SOCA.** The Joint Effort for Data assimilation Integration (JEDI) of the JCSDA is a
community framework that Moore et al. (2019) list alongside DART and PDAF as likely to
"play a more significant role in the development of existing and new ocean DA
capabilities"; SOCA is its marine component, described in its repository as the "JEDI
encapsulation of MOM6" (JCSDA 2026 [@soca2026jcsda]) (grey). No peer-reviewed system paper
exists (Q&A DA35). Its solver options (3D-Var FGAT, hybrid 3DEnVar, LETKF) and the plan for
first operational use in GFSv17/GEFSv13 are recorded in `sources.md` from the JEDI
documentation read on 2026-09-22 and were not re-verified here [not re-verified]. Its one
published use with gliders is the coupled HAFS-MOM6 experiment of Liu et al. (2023)
[@liu2023impact] [abstract only], Section 5.5.

## 5. Regional and coastal systems

Regional DA is where in situ profiles carry the most weight and where the error budget is
different: open lateral boundaries and surface forcing are "a significant source of error,
particularly at open boundaries in regional models" [@moore2019synthesis], the grids of a
few km make representativeness error (Box 2.1) the dominant term in $\mathbf{R}$ for a
profile, and the observing systems are sparser and more heterogeneous than the global
satellite and Argo streams. Edwards et al. (2015) [@edwards2015regional] review the first
fifteen years of the field, noting that "variational and sequential methods are among the
most widely used in regional ocean systems" with "recent advances in ensemble and
four-dimensional variational approaches" [abstract only]. This section gives a paragraph to
each system that assimilates or has assimilated glider profiles in U.S. waters and rows in
Table 1 to the rest.

### 5.1 The UCSC California Current ROMS 4D-Var

The Regional Ocean Modeling System (ROMS) carries a 4D-Var system built by the UCSC and
Rutgers groups with the TLM and adjoint of the full model. Its formulation is Part I of a
2011 trilogy (Moore et al. 2011 [@moore2011roms]) [not read; via Part II]; Part II (Moore et
al. 2011 [@moore2011romsII]) is the California Current application and Part III covers
observation impact and sensitivity. Part II fixes what the system does in this region. The
domain spans 134-116 W and 31-48 N in two configurations, WC30 (30 km, 30 levels) and WC10
(10 km, 42 levels), forced by the Navy's COAMPS and bounded by ECCO; the control vector holds
increments to the initial state, surface forcing and open boundaries; the observations were
Aviso dynamic topography, a 5-day blended GOES/AVHRR/MODIS SST at 10 km, EN3 in situ T/S
(XBT, Argo, and CTD from the CalCOFI, GLOBEC and LTOP cruises) and tagged elephant-seal
temperatures; gliders are not named. All observations in a grid cell within 6 h are merged
into a "super observation" whose scatter is taken as the representativeness error, added to
instrument errors of 0.02 m, 0.4 C (SST), 0.1 C and 0.01 (in situ T, S). Run sequentially
with 7-day windows over July 2002-December 2004, the system showed that "by far the largest
decrease in" the cost function "is always associated with adjustments in the initial
conditions", wind stress next, heat and freshwater fluxes and boundaries least, and that "more
than 90% of the observations assimilated into the model provide redundant information" (the
observations' degrees of freedom are 4-6% of their number in WC30 and 1-2% in WC10),
because satellite SST dominates the count. Part II also introduced the diagnostics the later
work relies on: posterior error variances from the Lanczos vectors of the minimization,
Desroziers consistency checks that showed the prior weights too confident in the observations,
and array modes, the observation-independent patterns through which an observing array can
move the analysis, which in the California Current are set "primarily by a combination of the
satellite data locations and the priors" [@moore2011romsII].

The historical analyses (Neveu et al. 2016 [@neveu2016historical]) apply that system at 1/10
degree (42 levels) over 30-48 N: WCRA31 covers 1980-2010 with ERA-40 (2.5 degree, 1980-2001),
ERA-Interim (0.7 degree, 2002-2010) and CCMP winds (25 km, 1988-2010) as forcing, WCRA14 covers
1999-2012 with COAMPS at 3-9 km, both with SODA boundaries,
8-day windows overlapping by 4 days so that each cycle starts from the mid-point of the last
(where a smoother's error is smallest), the dual algorithm under the strong constraint with one
outer and 15 inner loops, and a static, non-flow-dependent $\mathbf{B}$ with the multivariate
balance operator disabled. Assimilated: gridded 1/4 degree AVISO SSH (1993 onward, more than
50 km from the coast, because the system could not yet use along-track data with
time-correlated errors), Pathfinder, AMSR-E and MODIS SST, and EN3 profiles from XBT, MBT, CTD,
Argo and tagged mammals; "no velocity observations were assimilated", and gliders are again not
named, so whether CUGN profiles reached these analyses through the GTSPP stream inside EN3 is
not stated. The posterior cost is 2-5 times below the prior every cycle, less than 1% of
observations fail the background check, and the innovation statistics are diagnosed as
non-Gaussian with prior variances too high for T and SSH and too low for S. What the
assimilation buys: 4D-Var adjusts the wind stress by 5-10% of its mean and weakens the
upwelling-favourable alongshore wind; surface EKE off Cape Mendocino rises 10% over the free
run (95 vs 85 cm$^2$ s$^{-2}$, against 113 from AVISO and 235 from drifters), depth-averaged
EKE in the upper 500 m rises 50%, the eddy count rises 50% and decays back within 40-60 days
when assimilation stops; against CalCOFI profiles (not independent, since some are in EN3) the
free run's 0.7 C warm bias above 150 m falls to near zero in the top 50 m and 0.2 C at 50-150 m.
The authors list the limits of that version, homogeneous correlation lengths, no temporal
error correlations, no weak constraint, and a reanalysis that "consistently under estimate[s]
the level of EKE based on observational estimates" at 1/10 degree [@neveu2016historical]. The
near-real-time UCSC analyses that the brief cites as the demonstrated assimilation of CUGN data
(Section 5 of `context/initial_context_for_claude.md`) are not described by either paper and
have no source in this list (Q&A DA53). Beyond the analysis, the adjoint gives observation
impacts and the reduced-rank array modes of the California Current observing system (gliders,
HF radar, satellites) (Moore et al. 2018 [@moore2018reduced]) [abstract only; AGU host refuses
scripted fetches]; Rudnick (2016) [@rudnick2016ocean] sums up the observing side: "in coastal
regions, where Argo yields fewer profiles, a sustained glider program can be the dominant
source of in situ data". The treatment of glider profiles and depth-average velocity is deferred
to Section 9.

### 5.2 The Scripps California Current state estimate

Scripps (Cornuelle, Mazloff and colleagues) built the ECCO machinery of Section 4.1 into a
regional adjoint state estimate of the southern California Current. Todd et al. (2011)
[@todd2011poleward] combine three years of Spray glider sections on CUGN Lines 90 and 80
with "a numerical simulation [that] provides a dynamically consistent estimate of the ocean
state" to describe the poleward flows off Point Conception, inside the Southern California
Bight and offshore of the Santa Rosa Ridge, the last strongest below 350 m and propagating
westward as first-mode baroclinic Rossby waves [abstract only]; the brief cites this paper
as the demonstrated assimilation of CUGN data into a state estimate, and the model and
method (MITgcm, adjoint) are taken from the reading-list annotation rather than the
abstract, which does not name them. Zaba et al. (2018) [@zaba2018annual] evaluate the
California State Estimate (CASE) over 2007-2017 against both the assimilated glider data and
withheld CalCOFI data along the three CUGN lines, using 50 m potential temperature, 80 m
salinity and the depth and salinity of the 26 kg m$^{-3}$ isopycnal as metrics: CASE
reproduces the mean thermohaline and circulation structure including the California Current
and Undercurrent, captures the phase and "to a lesser extent, the magnitude" of the annual
cycle of upper-ocean warming and of springtime isopycnal heave, reproduces the semiannual
cycle of the Undercurrent, and carries the 2014-2016 warm and downwelling anomalies and the
isopycnal salinity anomaly that peaked with the 2015-2016 El Nino [abstract only]. This is
the one published case of a U.S. glider network used both as a constraint and as an
evaluation set for an adjoint state estimate; how CASE treats depth-average velocity and
representativeness error is a question for Matt (Section 11).

### 5.3 Rutgers doppio (Mid-Atlantic Bight)

The Rutgers group runs ROMS 4D-Var in the Mid-Atlantic Bight as doppio. Levin et al. (2020)
[@levin2020observation] describe a three-grid nested configuration from about 7 km to about
0.8 km spanning the Gulf Stream, the shelf-break eddy field and the sub-mesoscale, in which
"the 4D-Var system was found to perform well across this range of space- and time-scales".
Observations come "from a wide range of remote sensing, in situ, and mobile platforms", and
the adjoint is used to compute the impact of each platform on indexes of the shelf-break
front, stratification and cross-shelf exchange near the OOI Pioneer Array. The impacts vary
with grid, background circulation and assumed errors, but their geographic distribution is
"remarkably robust across the various indexes and the three grids", observations remote from
a target region can influence it as much as local ones, and the time series of impacts flag
outliers and serve as a performance indicator for the DA system itself [abstract only]. The
per-platform impact numbers, gliders included, are deferred to Section 9.

### 5.4 NOAA NOS operational forecast systems, including WCOFS

NOAA's National Ocean Service runs a family of Operational Forecast Systems (OFS) for
navigation. The West Coast OFS (WCOFS) is a three-dimensional ROMS configuration developed
jointly by NOS Office of Coast Survey, CO-OPS and NCEP Central Operations that "assimilates
real-time observations in a three-day window to generate water level, current, temperature
and salinity nowcast and forecast guidance once a day" and runs on NOAA's HPC within the
CO-OPS Coastal Ocean Modeling Framework (NOAA CO-OPS 2026 [@wcofs2026coops]) (grey). The page
does not state the assimilation method or the observation types; the WCOFS paper that
`reading_list.md` names as the fallback (Kurapov et al. 2017, *Ocean Dyn.* 67, 23-36, not in
`sources.bib`) has, per its abstract, sea-level verification as its subject and does not
describe the DA either, so this paragraph cannot say whether WCOFS has assimilated glider
profiles (Q&A DA49). The other NOS OFS (estuarine and Great Lakes systems) are outside this
report's scope.

### 5.5 The ocean component of NOAA's hurricane models

Hurricane forecast models are coupled atmosphere-ocean systems whose ocean is initialized
from a global analysis and whose skill depends on the upper-ocean heat and salinity
structure under the storm; they are the U.S. systems with the best-documented glider
impact. In the HWRF-HYCOM era, Dong et al. (2017) [@dong2017impact] ran the coupled model
(HWRF at 27/9/3 km; HYCOM at 1/12 degree over the North Atlantic with 32 hybrid layers) for
Hurricane Gonzalo (2014) with ocean initial conditions from AOML's research assimilation
cycle, a statistical-interpolation scheme with an ensemble-of-states background covariance,
in four configurations: no assimilation, gliders only, all standard observations, and all
plus gliders. The glider set was 180 profiles from two gliders off Puerto Rico (observation
errors 0.01 C and 0.02 psu), against 7,562 Argo profiles, 1,829 AXBTs and 1.28 million
altimeter observations over 1 March-13 October 2014. The barrier layer under the storm track
was represented "only with the use of underwater glider observations"; the upper-ocean
temperature and salinity forecast improved in the first 48 h; and the 126 h intensity
forecast reached 943 hPa and 103 kt with standard data and 939 hPa and 107 kt with gliders
added, against an observed peak of 125 kt and 90 kt with no assimilation, so the glider
contribution to intensity was "moderate" and localized. In the current system, HAFS
(operational June 2023, two configurations HFSA and HFSB, replacing HWRF and HMON), the ocean
is HYCOM at 1/12 degree with 41 hybrid layers whose initial state is "a simple subset of the
global RTOFS 3D restart file" from the 24 h nowcast; HAFS itself performs atmospheric DA
(4DEnVar) but the paper describes no ocean assimilation within HAFS (Kim et al. 2024
[@kim2024ocean]). Evaluated for Hurricane Laura (2020) against NDBC moorings, a few Argo
profiles and 33 glider profiles, the HYCOM fields are "overall biased to the cold upper ocean
conditions", with SST RMSE 1.0-1.1 C and mixed-layer-depth RMSE 10-12 m, and the model
reproduced the observed 1.3-2.4 C mixed-layer cooling but not the upwelling and internal-wave
undulations the glider recorded in the upper 130 m. The next step is documented in Liu et
al. (2023) [@liu2023impact], who assimilated six gliders and satellite observations with
Marine JEDI (SOCA) into MOM6 coupled to HAFS for Hurricane Isaias (2020): gliders increased
the analysed salinity-stratified barrier-layer thickness, which reduced storm-driven SST
cooling and increased enthalpy flux, and the intensity forecast improved further than with
satellites alone [abstract only]. Whether SOCA-MOM6 has replaced RTOFS-HYCOM in the
operational HAFS since 2023 is not established by any source in this list (Q&A DA50).

### 5.6 Table 1 (Fig. 4): operational and reanalysis systems

Rows for the global systems of Section 4, the comparator systems from the GODAE OceanView
intercomparison, and the U.S. regional systems of Section 5. "Gliders" records whether the
cited source names glider profiles among the assimilated observations; "not named" means
the source is silent, not that gliders are excluded (most systems ingest whatever profiles
the GTS or Coriolis carry). Resolution is horizontal; levels are vertical.

| System | Operator | Model and resolution | DA method | Window / cycle | Gliders assimilated? | Product type | Source |
|---|---|---|---|---|---|---|---|
| ORAS5 (OCEAN5-BRT) | ECMWF | NEMO 3.4.1 ORCA025, 0.25 deg, 75 levels, LIM2 | NEMOVAR 3D-Var FGAT, 5 members, bias correction, IAU | 5 d window, 5 d cycle, 7-11 d delay | not named (EN4/GTS profiles) | reanalysis, 1979-present | [@zuo2019ecmwf] |
| OCEAN5-RT | ECMWF | as ORAS5 | as ORAS5 | 8-12 d variable window, daily | not named (GTS) | real-time analysis for ENS, SEAS5, HRES | [@zuo2019ecmwf] |
| GLORYS12 | Mercator Ocean / Copernicus | NEMO ORCA12, 1/12 deg, 50 levels | SEEK-derived reduced-order KF + 3D-Var bias correction, IAU | 7 d cycle | not named (CORA profiles) | reanalysis, 1993-2019 (extended) | [@lellouche2021copernicus] |
| GLO12 (PSY4V3) | Mercator Ocean / Copernicus | NEMO 3.1 ORCA12, 1/12 deg, 50 levels, LIM2 | SAM: SEEK-derived reduced-order KF (250 fixed anomalies) + 3D-Var bias correction, IAU | 7 d cycle, weekly analysis, daily 10 d forecast | yes via Coriolis profiles per [@martin2015status]; not named in [@lellouche2018recent] | operational forecast, since Oct 2016 | [@lellouche2018recent] [@martin2015status] |
| ECCO v4 r1 | ECCO consortium (NASA) | MITgcm LLC90, nominal 1 deg | adjoint (Lagrange multiplier) least squares; controls: initial T/S, mixing, forcing | single 1992-2011 window, 45 iterations | no (not among constraints) | state estimate | [@forget2015ecco] |
| Global RTOFS | NOAA NCEP | HYCOM, 1/12 deg | flow-dependent 3D-Var (NCODA lineage) | daily; 2 d nowcast, 8 d forecast | not stated | operational forecast | [@kim2024ocean] [@rtofs2026ncep] (grey) |
| GOFS | U.S. Navy (NAVOCEANO) | HYCOM, 1/12.5 deg, 32 hybrid layers | NCODA 3D-Var FGAT, IAU 6 h | daily | yes (GTS and Navy sources) | operational forecast (2015 configuration) | [@martin2015status] [@cummings2013variational] |
| JEDI/SOCA | JCSDA / NOAA | MOM6 interface | variational and ensemble solvers per JEDI docs [not re-verified] | n/a (framework) | yes in the HAFS-MOM6 experiment of [@liu2023impact] | pre-operational framework | [@soca2026jcsda] (grey) [@liu2023impact] |
| Bluelink | Bureau of Meteorology (Australia) | MOM4, 1/10 deg Australian region, 51 levels | EnOI (static ensemble), adaptive nudging | daily; 1 d SST, 7 d in situ, 11 d altimetry windows; 4 staggered members | yes | operational forecast (2015 configuration) | [@martin2015status] |
| FOAM | Met Office (UK) | NEMO ORCA025, 1/4 deg, 75 levels | NEMOVAR 3D-Var FGAT + bias correction, IAU 1 d | daily, 2 d catch-up | yes | operational forecast (2015 configuration) | [@martin2015status] |
| TOPAZ | MET Norway | HYCOM, 1/8 deg North Atlantic and Arctic, 28 hybrid layers | EnKF (DEnKF), 100 members, 300 km localization | weekly, 7 d window, 3 d delay | not listed (Argo, XBT, moorings, ITP) | operational forecast (2015 configuration) | [@martin2015status] [@carrassi2018data] |
| California Current ROMS 4D-Var (WCRA31, WCRA14) | UC Santa Cruz | ROMS, 1/10 deg, 42 levels (WC30/WC10 in the 2011 tests) | ROMS 4D-Var, dual (R4D-Var/4D-PSAS) strong constraint; primal I4D-Var and weak constraint available | 8 d windows overlapping 4 d (7 d in 2011) | not named (EN3 profiles: XBT, MBT, CTD, Argo, mammals; no velocity) | reanalysis 1980-2010 and 1999-2012 | [@moore2011romsII] [@neveu2016historical] |
| CASE | Scripps | MITgcm regional, adjoint | ECCO-type adjoint state estimate | multi-year windows (not stated in abstracts) | yes (CUGN Lines 90, 80, 66.7) | state estimate, 2007-2017 | [@todd2011poleward] [@zaba2018annual] [abstract only] |
| doppio | Rutgers | ROMS, nested 7 km to 0.8 km | ROMS 4D-Var, adjoint observation impacts | not stated in abstract | "mobile platforms" (gliders implied, Section 9) | state estimates / analysis | [@levin2020observation] [abstract only] |
| WCOFS | NOAA NOS (CO-OPS, OCS, NCO) | ROMS, U.S. West Coast | not stated on the page | 3 d window, daily | not stated | operational nowcast/forecast | [@wcofs2026coops] (grey) |
| HWRF-HYCOM (research DA) | NOAA AOML/EMC | HYCOM 1/12 deg North Atlantic, 32 layers | statistical interpolation, ensemble-of-states covariance | daily | yes (180 profiles, 2 gliders, 2014) | research hindcast | [@dong2017impact] |
| HAFS v1 ocean | NOAA NCEP | HYCOM 1/12 deg, 41 layers | none in HAFS; initial state from RTOFS | 6-hourly cycles from RTOFS nowcast | via RTOFS only (not stated) | operational forecast since June 2023 | [@kim2024ocean] |
| HAFS-MOM6 with Marine JEDI (experiment) | NOAA EMC | MOM6 coupled to HAFS | SOCA | case study, Isaias 2020 | yes (6 gliders) | research hindcast | [@liu2023impact] [abstract only] |

*Note on the comparator rows.* Martin et al. (2015) [@martin2015status] cover the basin-scale
and global GODAE OceanView systems and defer coastal and shelf systems to a companion paper
not in this list, so the Copernicus *regional* systems (IBI, Mediterranean, North-West
Shelf) have no row; FOAM and TOPAZ stand as the European comparators (Q&A DA47).

## 6. AI in numerical weather prediction: the leading indicator

*[Figure 2 placeholder: prompt 7. `figs/ai_da_timeline.png` from `scripts/make_timeline.py`:
2018-2026 milestones on an NWP track and an ocean track, each dated from a key in
`sources.bib`; referred to again in Section 7.]*

ML entered NWP before it entered ocean DA, and it entered in a fixed order: first emulators
that replace the forecast model but are still started from a 4D-Var analysis, then learned
components inside the assimilation, then systems that learn the whole map from observations
to forecast, and, in parallel, generative methods that replace the analysis step itself. The
reason NWP went first is the training set: ERA5 is a DA product with four decades of hourly
global fields constrained by a dense observing system, and every emulator below is trained on
it. Geer (2021) [@geer2021learning] gives the frame the rest of this report uses: "the cost
function in variational DA is equivalent to the loss function for training a neural network",
gradient descent serves both, and "the adjoint method for calculating gradients in DA is
mathematically identical to the standard approach in ML known as backpropagation", so that a
learned component inside DA means replacing one of $\mathbf{B}$, $\mathcal{H}$, $\mathbf{M}$
or the model-error term by a fitted function while the Bayesian update of Box 1 stays.
Every system in this section carries the maturity tag and verification note of Section 1;
the question that Section 7 inherits, whether skill is measured against the reanalysis the
system was trained on or against observations, was raised in NWP first.

**Emulators.** Pangu-Weather (Bi et al. 2023 [@bi2023accurate]) is a 3D Earth-specific
transformer at 0.25 degree trained on ERA5 for 1979-2017, validated on 2019 and tested on
2018; its 5-day 500 hPa geopotential RMSE was 296.7 against 333.7 for the operational IFS,
and one forecast costs 1.4 s on one GPU, "more than 10,000-times faster than the operational
IFS". Skill is scored against ERA5 only, with cyclone tracks against IBTrACS, and the authors
say so: the model "was trained and tested on reanalysis data, but real-world forecast systems
work on observational data". Tag: *realistic hindcast*; verification: against the training
reanalysis. GraphCast (Lam et al. 2023 [@lam2023learning]) is a graph neural network at
0.25 degree with a 6 h step, ten days in "under one minute" on a TPU v4, trained on ERA5 with
2018 onward held out; it beat HRES on 90.3% of 1,380 targets, GraphCast scored against ERA5
and HRES against its own analyses (HRES-fc0), with no station or radiosonde verification,
and the paper states that it "should not be regarded as a replacement for traditional weather
forecasting methods". Tag: *realistic hindcast*; verification: against the training reanalysis.
AIFS (Lang et al. 2024 [@lang2024aifs]) (preprint) is ECMWF's own: pre-trained on ERA5
1979-2020, fine-tuned on IFS operational analyses for 2019-2020, initialised from the IFS
4D-Var analysis, run in "experimental operational mode" from October 2023 and at 0.25 degree
from February 2024; AIFS Single became operational on 25 February 2025 (ECMWF 2025
[@ecmwf2025aifs]) (grey). It is scored for 2022 against the operational analysis and against
radiosonde and SYNOP observations, about 10% better than IFS through the troposphere, and a
day-1 degradation seen against analyses "is not present in verification against radiosonde
observations", the first sign in this list that analysis-based and observation-based scores
can disagree. Tag: *operational*; verification: against observations as well as the centre's
own analysis. GenCast (Price et al. 2024 [@price2024probabilistic]) supplies the ensemble
step: a diffusion model at 0.25 degree, 12 h steps to 15 days in 8 min on a TPUv5, trained on
ERA5 1979-2018 and tested on 2019 after the model was frozen; it has better CRPS than ENS on
97.2% of 1,320 targets, each system against its own analysis and no observations, and the
authors underscore "the importance ... of traditional NWP-based data assimilation for
providing training and initialization data". Tag: *realistic hindcast*; verification: against
the training reanalysis. All four depend on 4D-Var twice, for the training set and for every
initial condition; they replace the model, not the assimilation.

**Learned components inside DA.** Bonavita and Laloyaux (2020) [@bonavita2020machine] trained
an artificial neural network on the operational 12 h analysis increments of 2018, averaged to
T21 (about 900 km), to predict model-error tendencies from the background column; the best
network explained about 14% of the increment variance for mass variables and about 5% for
wind, none for humidity. The tendencies were then used inside cycled 4D-Var at the
operational configuration (Cycle 47R1, TCo1279, about 9 km, 16 July-24 August 2019), as a
forcing in strong-constraint 4D-Var and as the first guess of the weak-constraint forcing,
and those experiments are verified against observations: background departures for
radiosondes, GPS-RO, conventional winds, AMVs and surface pressure, and 72 h temperature
forecast error against GPS-RO. They reproduce the stratospheric bias reduction of
weak-constraint 4D-Var, extend it to the troposphere and roughly halve surface-pressure
biases, though most differences are not significant over five to six weeks and the authors
call the hybrid "not yet fully in place for reliable operational use". Tag: *realistic
hindcast* (cycled at the operational configuration); verification: trained on a DA product,
verified against observations, which makes it, with AIFS, one of the two exemplars in this
section scored against observations rather than a reanalysis. Hatfield et al. (2021)
[@hatfield2021building] attack the adjoint instead: a neural-network emulator of the IFS
non-orographic gravity-wave drag scheme, trained on the scheme's inputs and outputs from
2015 with 2016 for validation and 2017 for testing, whose tangent-linear and adjoint are
obtained by differentiating the network and replace the hand-coded linear models inside
4D-Var; in a cycled run over December 2018-February 2019 with 177 ten-day forecasts the RMSE
differences from the reference were "no more than 4%" and not significant, with departures
also checked against ATMS and GPS-RO observations that are themselves assimilated. Tag:
*realistic hindcast* (one parametrization, the nonlinear scheme unchanged); verification:
against the experiment's own analysis and assimilated observations. Both are the pattern
Section 7.2 looks for in the ocean: the Bayesian update untouched, one ingredient learned.

**End-to-end observation-to-forecast.** Aardvark Weather (Allen et al. 2025
[@allen2025endtoend]) replaces the whole pipeline: an encoder maps raw observations (about 8%
of those conventional NWP ingests) to a gridded state, a processor forecasts, a decoder
produces station forecasts, and the three are fine-tuned end to end; the encoder and
processor are pre-trained with ERA5 as target and the station decoder on HadISD
observations, with 2018 held out. Gridded fields are scored against ERA5 (HRES and GFS
baselines at 1.5 degrees) and station forecasts against held-out HadISD, where end-to-end
fine-tuning cut MAE by 6% over Europe, West Africa, the Pacific and globally; no NWP product
enters at test time, but ERA5 is the pre-training target, so "end-to-end from observations"
holds for deployment, not for training. Tag: *realistic hindcast* (research prototype);
verification: against the reanalysis for fields, against withheld observations for stations.
GraphDOP (Alexe et al. 2024 [@alexe2024graphdop]) (preprint), from ECMWF, goes further:
trained on observations alone for 2004-2021 with 2022 for validation, the target being the
next 12 h of observations, no reanalysis in training except an ERA5-departure quality-control
step the authors flag as a partial dependence. It is verified in observation space (SYNOP 2 m
temperature, AMSU-A and SSMIS brightness temperatures) against the operational IFS and on a
grid against ERA5, "employed exclusively for verification": 15% better than IFS for 2 m
temperature at day 1, mixed at days 3-5, worse for AMSU-A, and in the authors' words "not yet
close to matching state-of-the-art NWP performance". Tag: *realistic hindcast*; verification:
against withheld observations. It is the first system in this list in which no physics-based
analysis sits anywhere in the loop.

**Generative DA and learned assimilation.** Manshausen et al. (2025)
[@manshausen2025generative] use score-based DA: a diffusion prior trained on HRRR analyses of
10 m wind and precipitation at 3 km over the central United States (128 x 128 patches,
2018-2021), with observations entering only at inference to guide the denoising. Tested on
2017 with 40 ISD stations assimilated and 10 held out, the analyses have about 10% lower RMSE
than HRRR at the held-out stations; the authors note that those stations belong to the METAR
data HRRR itself assimilates, that the ensembles are underdispersive, and that the work is a
"proof of concept, and the first at km-scale". Tag: *realistic hindcast*; verification:
against withheld stations that are not independent of the baseline. FuXi-DA (Xu et al. 2025
[@xu2025fuxida]) is learned assimilation into an ML model: FY-4B AGRI brightness
temperatures (channels 8-15, super-obbed to 0.25 degree) are combined with a background from
a 6 h FuXi forecast started from ERA5, the training target being ERA5. Per the Methods
section, training spans June 2022-May 2023, validation June-July 2023 and testing
August-December 2023 (the Results section states the training span as June 2022-June 2024,
which would overlap the test period; the Methods split is used here, Q&A DA43). Analysis RMSE
falls by 2-4.5% against a bias-corrected background (Z500 by 2.02%, 300 hPa humidity by
4.47%) and the day-1 Z500 forecast error by 0.67%, shrinking to 0.34% by day 7; the study is
offline and non-cycled and all-sky assimilation is not demonstrated. Tag: *realistic
hindcast, offline and non-cycled*; verification: against ERA5 only. Both belong to category
3 of Section 7 (ML replacing the analysis step); Cheng et al. (2023) [@cheng2023machine]
survey this "end-to-end learning of DA systems" strand as the youngest in the field.

**What NWP tells the ocean.** The sequence was emulate the model, learn pieces of the
assimilation, learn the whole map; the ocean is at the first step (Section 7.1) with
isolated cases of the second (7.2) and third (7.3). Two of the ten NWP systems above are
scored against observations in their own right (AIFS, GraphDOP) and two more partly
(Bonavita and Laloyaux, Aardvark); the rest are scored against the reanalysis or analysis
they learned from. The ocean lacks the three things that made the NWP path short: a training
reanalysis whose subsurface is as well constrained as ERA5's troposphere (Section 4.1), a
40-year hourly record at eddy-resolving resolution, and an observing system dense enough to
verify a 1/12 degree forecast independently of the analysis.

## 7. AI in ocean DA, by where ML enters the pipeline

*[Figure 1 placeholder: prompt 7. Mermaid: the four ML entry points (1 emulator of the
model; 2 inside the analysis: $\mathbf{B}$, $\mathcal{H}$, adjoint, model error; 3 replacing
the analysis; 4 around it: QC, downscaling, anomaly detection, sampling design) laid over one
DA cycle: background, observations, QC, analysis, forecast.]*

The ocean literature is organized by where ML enters the cycle of Box 1: (1) emulators of
the forecast model $\mathcal{M}$; (2) learned pieces inside a classical analysis
($\mathbf{B}$, $\mathcal{H}$, the adjoint or the model-error term), the Bayesian update
kept; (3) ML that replaces the analysis step; (4) ML around the cycle (quality control,
downscaling, anomaly detection, observing-system design).

**The circularity caveat, stated once.** The ocean emulators of Section 7.1 are trained on
GLORYS12 (Section 4.1) or on a free model run. GLORYS12 is itself a DA product: its authors
state that its "performance ... shows a clear dependency on the time-dependent in situ
observation system", its 0-2000 m departures halved when Argo arrived (0.75 C and 0.2 psu
before, 0.45 C and 0.1 psu after), its pre-2004 salinity bias could not be corrected, and its
eddy-kinetic-energy record is discontinuous (Lellouche et al. 2021
[@lellouche2021copernicus]). An emulator that reproduces GLORYS12 reproduces these
properties, and a score computed against GLORYS12 fields measures how well the training
product is reproduced, not how well the ocean is forecast. WenHai's authors put it plainly:
"the AI-based GOFSs, including WenHai, are trained based on high-quality ocean reanalysis
datasets produced via numerical GOFSs in combination with data assimilation. It is more
appropriate to think that AI-based GOFSs stand on the shoulders of numerical GOFSs" (Cui et
al. 2025 [@cui2025forecasting]). The same dependence holds in NWP (Section 6), where Pangu's
authors made the equivalent statement about ERA5. This report therefore treats skill as
established only against withheld observations, for the global systems the GODAE OceanView
IV-TT Class 4 sets (Argo temperature and salinity profiles, drifter SST and 15 m currents,
along-track sea-level anomaly), and records "verified against the training reanalysis" where
that is all a paper offers. A second, weaker dependence is shared by every emulator: each
forecast starts from an operational analysis (GLO12 or GLORYS12), so DA supplies the initial
condition as well as the training set. Later paragraphs refer to this as *the circularity
caveat*.

### 7.1 Emulators and surrogates

**Emulators of a model.** Samudra (Dheeshjith et al. 2025 [@dheeshjith2025samudra]) is a
ConvNeXt UNet that emulates GFDL's OM4: the native 1/4 degree output is interpolated to a
1 x 1 degree grid and 19 fixed depth levels, the state is potential temperature, salinity,
SSH and the two velocity components, the step is 5 days, and the training data are a 65-year
OM4 run (1958-2022). The emulator "is stable for centuries and 150 times faster than the
original ocean model", but "struggles to capture the correct magnitude of the forcing trends
and simultaneously remain stable": over the 8-year test rollout (2014-2022) "for most depths
the trained models underestimate trends by 20% to 50% relative to OM4". Tag: *realistic
hindcast*; verification: against held-out OM4 output, no observations; here the circularity is by design, since the target is the
model, not the ocean. Samudra 2 (Yuan et al. 2026 [@yuan2026samudra2]) (preprint) scales the
same architecture to 1, 1/2 and 1/4 degree, trained on OM4 1975-2013 with 8-year rollouts
over 2014-2022 scored against OM4; it names two failure modes of long rollouts, "variance
collapse" and "imprinting artifacts, in which velocity patterns leak into deep-ocean
fields", and raises upper-ocean temperature $R^2$ at 1 degree from 0.56 to 0.87. Tag:
*realistic hindcast*; verification: against the parent model only.

**Emulators of GLORYS12.** XiHe (Wang et al. 2024 [@wang2024xihe]) (preprint) is "the first
data-driven 1/12 degree resolution global ocean eddy-resolving forecasting model", a
hierarchical transformer whose training set is GLORYS12; the data section gives the GLORYS12
span as January 1993-December 2020 while the abstract calls the training data "25-year", and
the evaluation runs from January 2019 to December 2020 in the IV-TT Class 4 framework against
Argo, drifter and along-track altimeter observations, where XiHe outperforms PSY4 (GLO12),
GIOPS, FOAM and Bluelink on all evaluated variables at 10 days (15 m currents by 10.16% and
11.21% over PSY4), though at 1 and 5 days "GIOPS and PSY4 achieve comparable or slightly
better" scores for some variables, and it produces a forecast in 0.35 s.
Whether the test years were withheld from training is implied by "25-year" but never stated
(Q&A DA34). Tag: *realistic hindcast*; verification: withheld observations (Class 4), with the
training/test overlap unresolved. WenHai (Cui et al. 2025 [@cui2025forecasting]) builds the
bulk formulae for air-sea momentum, heat and freshwater fluxes into the network and predicts
daily tendencies of the upper 643 m; it is trained on GLORYS12 with ERA5 forcing for
1993-2018 and validated on 2019, and its April-November 2024 forecasts start from the
operational GLO12v4 analyses and use the same atmospheric forecast as GLO12v4, the fairest
comparison in this list. Against Class 4 observations at a 10-day lead its RMSE is 6.02%
(temperature profile) and 5.64% (salinity profile) below GLO12v4, and 8.94%, 10.67%, 6.95%
and 10.33% below for SST, SLA and the 15 m zonal and meridional currents; CRPS gives the same
ordering. Tag: *realistic hindcast bordering on pre-operational* (run from operational
analyses, not by the centre); verification: withheld observations (Class 4). GLONET (El Aouni
et al. 2025 [@elaouni2025glonet]) is Mercator Ocean's own emulator, a Fourier neural
operator with a CNN branch at 1/4 degree on interpolated GLORYS12 fields, predicting
temperature, salinity and currents on a set of levels from 0.49 to 1684 m plus SSH; trained
on 1993-2019 with 2020 "reserved for validation", forecasting January-July 2024 from the
operational GLO12 analyses in "a few seconds (GPU)" against "1h (HPC)" for GLO12. It is
scored in the Class 4 framework against Argo profiles and drifters, point-wise against
GLORYS12 "which serve as the reference", and with process-oriented checks (mixed-layer depth,
geostrophic currents). On Class 4 it "surpasses XIHE in SLA and surface currents,
consistently outperforming GLO12 for forecasts ranging from 5 to 9 days", while "for SST,
GLO12 demonstrates superior performance across all forecast horizons, except for the
one-day forecast", which the authors attribute to GLONET being "trained on historical
outputs of physical systems, without direct assimilation of real-time observations",
whereas GLO12 assimilates satellite SST directly. They report that "MOI has established
robust pre-operational pipelines", and experimental daily forecasts are served on the EDITO
platform. Tag: *pre-operational*; verification: withheld observations (Class 4) plus the
training reanalysis, of which only the former counts here.

**A regional emulator.** OceanNet (Chattopadhyay et al. 2024 [@chattopadhyay2024oceannet])
is a Fourier neural operator for sea-surface height in the northwest Atlantic, trained on a
4 km ROMS-EnKF regional reanalysis for 1993-2018 and tested on 2019-2020 against the same
reanalysis, for 120-day forecasts of Loop Current eddy shedding and the Gulf Stream meander,
at a cost "500,000" times below ROMS; it matches the ROMS forecast in the Gulf of Mexico and
beats it in the Gulf Stream region, and the authors call the work "initial steps". Tag:
*realistic hindcast*; verification: against the training reanalysis only, so the circularity
caveat applies in full. It is the only regional emulator in this list, and none exists for
the California Current.

What the GLORYS12-trained emulators show is that a network can match or beat the operational
system it learned from on 1-10 day Class 4 scores at a fraction of the cost; what they
inherit is everything Section 4.1 lists for GLORYS12, and what none of them has been tested
on is a region where the Class 4 profile set is sparse.

### 7.2 ML inside classical DA

Published ocean work on category 2 is thin. The clearest case is model-error learning from
increments, the ocean-side counterpart of Bonavita and Laloyaux (Section 6): Gregory et al.
(2023) [@gregory2023deep] trained a convolutional network on the GFDL SPEAR ice-ocean
system (nominal 1 degree), which "assimilates satellite observations of sea ice
concentration every 5 days between 1982-2017", to predict the sea-ice-concentration
increments from the model state; with 5-fold cross-validation on contiguous chunks and an
untouched 2018-2021 extension, the daily spatial pattern correlations with the true
increments run from 0.62 to 0.80 by season and hemisphere, and the seasonal climatologies
of predicted and true increments correlate at 0.96-0.98, consistently better than a
climatological-increment baseline. The study is offline; online bias correction is proposed,
not shown. Tag: *realistic hindcast* (offline feasibility); verification: against the DA
increments, a DA product, not independent observations. The BGC counterpart, learning the
model-minus-observation pCO2 misfit (Gloege et al. 2022 [@gloege2022improved]), is treated
in Section 8; its authors frame it as an observation-based product, not as DA. The
adjoint-surrogate idea of Hatfield et al. (Section 6) has
no ocean counterpart in this list, and no published ocean system in this list learns
$\mathbf{B}$ or the observation operator; Cheng et al. (2023) [@cheng2023machine] list
learned error covariances and model-error correction as active strands of the general
literature. Both absences are on the list for Matt (Section 11). One boundary case is named
because the decisions ask for it (Q&A DA36c): Zanna and Bolton (2020) [@zanna2020data]
discover closed-form mesoscale eddy closures with relevance vector machines and a CNN from
idealized MITgcm double-gyre runs at 3.75 and 7.5 km coarse-grained to 30 km, and test them
online in an idealized 30 km model; this changes the model, not the assimilation, uses no
observations, and is tagged *idealized*.

### 7.3 ML replacing DA

**Neural variational interpolation.** 4DVarNet (Fablet et al. 2021 [@fablet2021learning])
learns both the prior operator inside a 4D-Var-like cost and the iterative solver (an LSTM
gradient scheme) end to end, so the analysis becomes one trained network. On Lorenz-63 the
reconstruction error is 1.34 against 3.55 for fixed-step gradient descent on the 4D-Var cost
with the true equations, and on Lorenz-96 0.38 against 1.06; the paper closes by asking
whether the findings "generalize to other systems, especially higher-dimensional ones". Tag:
*idealized*; verification: against the simulated truth of the toy systems. 4DVarNet-SSH
(Beauchamp et al. 2023 [@beauchamp2023fourdvarnet]) is that generalization for sea-surface
height: trained and tested in the NATL60 observing-system simulation experiment of the
SSH-mapping data challenge (ocean-data-challenges 2026 [@oceandatachallenges2026]) (grey),
with pseudo-observations along four nadir tracks and a simulated SWOT swath, and scored on
22 October-2 December 2012 against the simulated truth: 30-60% lower reconstruction error
than the operational optimal interpolation, with resolved scales of 0.83 degree and 8.0 days
against 1.42 degree and 12.0 days for DUACS with four nadirs; application to real altimetry
is named as future work. Tag: *realistic OSSE* (a simulation-based hindcast); verification:
against simulated truth, not observations. Martin et al. (2023) [@martin2023synthesizing]
supply the observing-system-experiment half of the pair: a network trained on real altimetry
and SST in the Gulf Stream Extension for 2010-2020, with 2017 withheld for testing, CryoSat-2
withheld as ground truth and AOML drifters as an independent set; the map has 17% lower RMSE
and resolves scales 30% smaller than the DUACS optimal interpolation, and its geostrophic
currents have 24% and 27% lower RMSE against the drifters. Tag: *realistic hindcast*;
verification: against withheld and independent observations, the cleanest verification in
Section 7. The data challenges define what "verified" means in this strand: the 2020a NATL60
challenge is an OSSE with a known truth, the 2021a challenge scores against withheld real
altimetry, and a method's rank can differ between the two.

**End-to-end and generative assimilation.** No ocean counterpart of FuXi-DA, Aardvark or
GraphDOP (Section 6) is in this list: no published system learns to assimilate ocean
observations into an ML ocean model, cycled or not, and no generative reconstruction of the
ocean state from sparse in situ profiles at the maturity of Manshausen et al. was found among
the approved references. The ocean's category 3 is, so far, surface interpolation from
satellite tracks; the subsurface mapping problem that profiles pose, sparse in space and
slanted in time, is open in this literature.

### 7.4 ML around DA

**Quality control.** Sugiura and Hosoda (2020) [@sugiura2020machine] classify Argo
temperature and salinity profiles with features from the signature method (iterated
integrals of the profile path) against the JAMSTEC delayed-mode QC flags: $M = 8.2 \times
10^4$ profiles, 40% for training and 60% for cross-validation (a random split; whether it is
by float is not stated), scored with ROC curves. The method "never misidentifies negative
(normal) profiles if the appropriate cutoff ... is used, but it may accept positive (bad)
profiles with a probability 0.6" at the default cutoff, because part of the delayed-mode
criterion "cannot be decided only by the shape" of the profile; it is a screening tool, not a
replacement for delayed-mode QC. Tag: *realistic*, offline
method demonstration; verification: against human QC labels, not against the ocean. It is the
only QC paper in this list and there is none for glider streams.

**Anomaly detection, downscaling, adaptive sampling.** No approved reference addresses ML
anomaly detection on ocean data streams, ML downscaling of ocean analyses, or ML-driven
adaptive sampling; the report records the gap rather than fill it from memory. The classical
counterpart of sampling design is adjoint-based observing-system analysis: Moore et al.
(2018) [@moore2018reduced] derive the reduced-rank array modes of the California Current
observing system (gliders, HF radar, satellites) in ROMS 4D-Var [abstract only], the machinery
introduced in Part II of the 2011 trilogy (Section 5.1), and OSSEs value observation types by
fraternal-twin experiments (Sections 8 and 9). Neural estimation of derived BGC variables from
the T, S and oxygen a glider carries (CANYON-B) is the one category-4 case with an
independent verification and is treated in Section 8.

## 8. Biogeochemical DA

**Coupling.** The GODAE OceanView task team's OceanObs'19 statement (Fennel et al. 2019
[@fennel2019advancing]) is the reference for the state of the field. Its central warning is
that "assimilation of physical observations in coupled models often does not improve but
degrades the biogeochemical state", a degradation that "appears to arise at least partly when
physical and biogeochemical variables are updated independently in violation of
property-property relationships"; the remedies in use are multivariate balancing of the BGC
increments (the Met Office updates surface $\log_{10}$ chlorophyll and derives increments
for the other variables through a balancing scheme; Mercator's SEEK filter projects surface
corrections of phytoplankton groups and nutrients through the mixed layer). BGC increments
are not Gaussian: the authors name "the non-Gaussian characteristics of biogeochemical
observations, the strong non-linearity of biogeochemical models and the frequent lack of
direct correspondence between convenient observables and model variables" as the reasons the
physical schemes do not transfer unchanged, and the California Current system uses "a
lognormal form of 4D-Var" for that reason.

**What is assimilated, and by whom.** "Currently, the main biogeochemical data stream used
in assimilation is satellite ocean color, but this measurement is limited to the surface
ocean and provides an imperfect proxy of phytoplankton biomass." The systems table of Fennel
et al. gives the methods in use in 2019: the Met Office FOAM with HadOCC or MEDUSA
(NEMOVAR 3D-Var, pre-operational, with the capability to assimilate chlorophyll, nitrate,
oxygen and pH profiles), the North-West Shelf NEMO-ERSEM (3D-Var, operational, glider and
float assimilation "under development"), Mercator's PISCES run offline at 1/4 degree with a
SEEK-filter chlorophyll assimilation "being implemented", the Mediterranean OGSTM-BFM
(3D-Var; BGC-Argo chlorophyll and nitrate "in pre-operational mode"), the Black Sea system
(SEEK filter, Argo oxygen), the Great Barrier Reef eReefs system (a 100-member EnKF of
spectral ocean colour, with forecast errors "reduced by up to 50%" and withheld glider
fluorescence improved by 45%), and the UCSC ROMS-NEMURO California Current system (4D-Var,
"quasi-operationally", satellite chlorophyll only). The team's own assessment: schemes for
"data types other than surface observations (e.g., from floats and gliders)" exist "but thus
far they have mostly been used in OSSE-type twin experiments", and "biogeochemical/ecological
operational systems are still in their infancy compared to physical ocean forecasting". For
the California Current the two-ecosystem-model 4D-Var study of Mattern et al. (2017)
[@mattern2017data] is the relevant paper [not read; no abstract in Crossref, OpenAlex or
Semantic Scholar; described via `reading_list.md` as showing the model dependence of the
chlorophyll assimilation]. The state-estimation route is the adjoint one of Section 4.1:
B-SOSE (Verdy and Mazloff 2017 [@verdy2017data]) adds carbon, oxygen and nutrient cycles to
the Southern Ocean state estimate, constrained by "profiling floats, shipboard data, underway
measurements, and satellites" over 2008-2012, and captures 44% of the surface pCO2 variance
in Drake Passage and "over 60% of the variance" of oxygen profiles at 200 and 1000 m, with
the adjoint method "shown to be mature and ready to synthesize in situ biogeochemical
observations as they become more available" [abstract only]. ECCO-Darwin (Carroll et al.
2020 [@carroll2020ecco]) couples the Darwin ecosystem model to the ECCO physics and
optimizes initial conditions and six BGC parameters by a Green's function approach over
1995-2017, giving a global CO2 sink of 2.47 +/- 0.50 Pg C per year [abstract only]; the brief
names both ECCO and Darwin as planned components.

**Valuing in situ BGC profiles.** Ford (2021) [@ford2021assimilating] is the OSSE the field
points to: FOAM-MEDUSA with NEMOVAR 3D-Var FGAT in a fraternal-twin design over 2009,
assimilating ocean colour alone or with synthetic BGC-Argo chlorophyll, nitrate, oxygen and pH
profiles from a quarter of the Argo array (comparable to the planned 1000 floats) or from all
of it, and no physical observations, "reflecting the way state-of-the-art biogeochemical
reanalyses are run". Ocean colour cut the surface chlorophyll error by 72% and BGC-Argo added
nothing at the surface, but ocean colour alone degraded surface nitrate "almost everywhere"
and degraded DIC, alkalinity and pH, while the profiles gave "an almost universal
improvement" for nitrate, oxygen and pH through the water column, largest for pH, and
improved the unassimilated pCO2; the author notes that "alternative in situ observing
technologies such as gliders may be able to play a role".

**Where ML is being tried.** Fennel et al. (2019) contain no mention of machine learning;
the ML in this section sits around the assimilation (category 4), not inside it. CANYON-B
(Bittig et al. 2018 [@bittig2018canyonb]) is a committee of Bayesian multilayer perceptrons
that maps pressure, temperature, salinity, oxygen and position (and year for the carbonate
variables) to nitrate, phosphate, silicate, alkalinity, DIC, pH and pCO2, trained on GLODAPv2
bottle data (521 cruises, 1972-2013, 20% set aside) and validated against 19 later GO-SHIP
cruises (2012-2017) and float data: RMSE 0.68 (nitrate), 0.051 (phosphate), 2.3 (silicate),
6.3 (alkalinity) and 7.1 (DIC) umol/kg, 0.013 in pH and 20 uatm in pCO2. The authors present
it as a "transfer function between components of the ocean observing system", warn that it
"can only reproduce the variability that is present in the training data", and note that
of the derived variables "only pH can be measured on those platforms operationally" for
gliders and floats at the time of writing. Tag: *realistic*, released method; verification:
independent cruises. LDEO-HPD (Gloege et al. 2022 [@gloege2022improved]; Section 7.2) is the
other case: gradient-boosted trees learn the SOCAT-minus-model pCO2 misfit for nine global
models, with seven withheld years and independent GLODAPv2, BATS and HOT data, and reach an
RMSE of 15.4 uatm against GLODAP in the 2010s versus 15.7-17.7 for other products. Tag:
*realistic hindcast*, released product; verification: withheld and independent
observations. No approved reference puts ML inside a BGC assimilation step, and the
Southern Ocean and California Current state estimates above use the adjoint, not a learned
component.

## 9. Gliders in DA

*[Placeholder: prompt 6. Fig. 3 (one assimilation cycle marking where glider profiles and
depth-average velocity enter and where representativeness error arises) at the top;
profile vs binned assimilation; depth-average velocity as an observation; representativeness
error; observation-impact and OSE/OSSE results from Sections 5.1-5.5.]*

## 10. Glossary

*[Placeholder: prompt 6. Background, analysis, increment, innovation, B and R,
observation operator, TLM and adjoint, localization, inflation, FGAT, IAU, OSE/OSSE,
observation impact and FSOI, representativeness error, Class 4 verification, emulator,
end-to-end.]*

## 11. Questions for Matt

*[Placeholder: prompt 6. Built from the open points flagged while drafting; so far: how
CASE treats depth-average velocity and representativeness error (5.2); the WCOFS DA
configuration (5.4); the operational status of SOCA-MOM6 in HAFS (5.5); whether any
operational ocean centre runs an ML component inside its DA.]*

*Candidate questions carried from Q&A (for prompt 6 to work into the list):*

- *WCOFS (Q&A DA49): no public source states its DA method or the observation types it
  assimilates, only "real-time observations in a three-day window ... once a day"; does
  Matt know the configuration, and whether glider profiles have ever entered it?*
- *HAFS ocean DA (Q&A DA50a): has the operational HAFS ocean component moved from
  RTOFS-initialized HYCOM with no ocean DA (Kim et al. 2024) to MOM6 with Marine JEDI/SOCA
  (Liu et al. 2023, a case study), and if so since which HAFS version?*
- *SOCA solvers (Q&A DA50b): the solver list recorded in `sources.md` from the JEDI
  documentation (3D-Var FGAT, hybrid 3DEnVar, LETKF) and the GFSv17/GEFSv13 plan could not
  be re-found on 2026-09-23; which solvers does SOCA run today, and what is the
  operational timeline?*
- *Near-real-time UCSC ROMS 4D-Var (Q&A DA53): the brief cites the assimilation of CUGN
  profiles into the UCSC California Current analyses as demonstrated, but neither Moore
  et al. (2011, Part II) nor Neveu et al. (2016) name gliders among the assimilated
  platforms; which product and which paper document the CUGN assimilation?*

## References

See `sources.md` for the annotated list with access dates and `sources.bib` for BibTeX;
`scripts/check_citations.py` lists the keys cited here against `sources.bib`. Keys cited so
far: [@moore2019synthesis] [@carrassi2018data] [@bannister2017review] [@geer2021learning]
[@evensen2003ensemble] [@forget2015ecco] [@martin2015status] [@moore2011roms] [@moore2011romsII]
[@edwards2015regional] [@oke2008representation] [@stammer2016ocean] [@zuo2019ecmwf]
[@lellouche2021copernicus] [@lellouche2018recent] [@kim2024ocean]
[@cummings2013variational] [@rtofs2026ncep] [@soca2026jcsda] [@liu2023impact]
[@neveu2016historical] [@moore2018reduced] [@rudnick2016ocean] [@todd2011poleward]
[@zaba2018annual] [@levin2020observation] [@wcofs2026coops] [@dong2017impact]
[@bi2023accurate] [@lam2023learning] [@lang2024aifs] [@ecmwf2025aifs]
[@price2024probabilistic] [@bonavita2020machine] [@hatfield2021building]
[@allen2025endtoend] [@alexe2024graphdop] [@manshausen2025generative] [@xu2025fuxida]
[@cheng2023machine] [@dheeshjith2025samudra] [@yuan2026samudra2] [@wang2024xihe]
[@cui2025forecasting] [@elaouni2025glonet] [@chattopadhyay2024oceannet]
[@gregory2023deep] [@gloege2022improved] [@zanna2020data] [@fablet2021learning]
[@beauchamp2023fourdvarnet] [@oceandatachallenges2026] [@martin2023synthesizing]
[@sugiura2020machine] [@fennel2019advancing] [@mattern2017data] [@verdy2017data]
[@carroll2020ecco] [@ford2021assimilating] [@bittig2018canyonb].
