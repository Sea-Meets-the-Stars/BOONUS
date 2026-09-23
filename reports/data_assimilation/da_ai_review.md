# Data assimilation in oceanography and where AI enters it

**Version:** v0.1 draft · **Date:** 2026-09-23 · **Authors:** J. Xavier Prochaska and Claude ·
**Audience:** JXP; to be shared with Matt Mazloff at v0.2 ·
**Apparatus:** `outline.md`, `reading_list.md`, `sources.md` / `sources.bib` (shared BibTeX
keys), `scripts/` (this directory). A review, not a BOONUS document.

| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 draft | 2026-09-23 | JXP and Claude (Fable 5.1) | Skeleton from `outline.md`; drafted the primer (Section 2), classical methods (3), global systems (4), regional and coastal systems with the systems table (5); placeholders for 0 and 6-11 (prompts 5-6). |

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
by the verification pass (prompt 8). Every quantitative statement in Sections 2-5 traces
to a source read in this session unless so flagged.

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
system of Section 5.1 provides both, in primal (state-space) and dual (observation-space)
formulations (Moore et al. 2011 [@moore2011roms]) [not read; via `reading_list.md` and
Edwards et al. 2015 [@edwards2015regional], abstract only].

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
Rutgers groups with the TLM and adjoint of the full model. Its formulation paper (Moore et
al. 2011 [@moore2011roms]) is Part I of a trilogy whose Parts II and III cover the California
Current application and the observation-impact and sensitivity tools; the reading list
describes it as offering strong- and weak-constraint 4D-Var in both primal and dual form
[not read; via `reading_list.md`; the paper has no abstract in Crossref, OpenAlex or
Semantic Scholar, and the Elsevier host refuses scripted fetches]. Two products of that
system frame the California Current: a multi-decade historical analysis (Neveu et al. 2016
[@neveu2016historical]) whose configuration and diagnostics paper the reading list records
as a 31-year reanalysis assimilating satellite SST and SSH and in situ profiles, gliders
included [not read; same access problem as Moore et al. 2011], and the near-real-time
analyses that the brief cites as the demonstrated assimilation of CUGN data (Section 5 of
`context/initial_context_for_claude.md`). What the ROMS 4D-Var adjoint adds beyond the
analysis is the observation-impact and array-mode machinery: the impact of each platform on
a chosen circulation index can be computed directly, and the reduced-rank array modes of the
California Current observing system (gliders, HF radar, satellites) have been derived in this
way (Moore et al. 2018 [@moore2018reduced]) [abstract only; AGU host refuses scripted
fetches]. Rudnick (2016) [@rudnick2016ocean] sums up the observing side: "in coastal
regions, where Argo yields fewer profiles, a sustained glider program can be the dominant
source of in situ data". The ROMS-specific treatment of glider profiles and depth-average
velocity is deferred to Section 9. *Flag for JXP:* Moore et al. (2011) and Neveu et al.
(2016) are the two papers for which the abstract is not enough for this paragraph (Q&A
DA48).

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
| California Current ROMS 4D-Var | UC Santa Cruz | ROMS, several km | ROMS 4D-Var (strong/weak, primal/dual), TLM and adjoint | multi-day windows (not confirmed this session) | yes (CUGN) per the brief and [@rudnick2016ocean]; system papers not read | reanalysis (1980-2010) and near-real-time analysis | [@moore2011roms] [@neveu2016historical] [not read] |
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

*[Placeholder: prompt 5. About 2 pages; Fig. 2 (timeline) at the top. One paragraph per
family with two or three exemplars, each with a maturity tag and verification note:
emulators (Pangu-Weather, GraphCast, AIFS, GenCast); learned components inside DA (Bonavita
and Laloyaux 2020; neural TLM/adjoint); end-to-end observation-to-forecast (Aardvark,
GraphDOP); generative DA (Manshausen et al.; FuXi-DA with the DA43 data split).]*

## 7. AI in ocean DA, by where ML enters the pipeline

*[Placeholder: prompt 5. Fig. 1 (taxonomy over one DA cycle) at the top; the
trained-on-reanalysis circularity stated once here and referred back to; the XiHe
training/test overlap stated as implied but not explicit (DA34).]*

### 7.1 Emulators and surrogates

*[Placeholder: prompt 5. Samudra, XiHe, WenHai, GLONET, OceanNet, Samudra 2; GLORYS12 from
Section 4.1 as the training set.]*

### 7.2 ML inside classical DA

*[Placeholder: prompt 5. Learned model-error correction from increments (Gregory et al.
2023; the ECMWF pattern from Section 6), adjoint surrogates, the near absence of ocean work
on learned B and H; the learned-parameterization boundary case in one sentence (DA36c).]*

### 7.3 ML replacing DA

*[Placeholder: prompt 5. 4DVarNet from Lorenz systems to the SSH-mapping data challenges
(OSSE on NATL60 vs OSE on real altimetry); what "verified" means in each case.]*

### 7.4 ML around DA

*[Placeholder: prompt 5. ML QC of Argo profiles; the thin literature on anomaly detection
and adaptive sampling; adjoint array modes (Section 5.1) as the classical counterpart;
derived BGC variables cross-referenced to Section 8.]*

## 8. Biogeochemical DA

*[Placeholder: prompt 5. Physics-BGC coupling and initialization shock; what is
assimilated (ocean colour, BGC-Argo); non-Gaussian increments; ROMS 4D-Var with two
ecosystem models, B-SOSE and ECCO-Darwin; the BGC OSSE; where ML is being tried.]*

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

## References

See `sources.md` for the annotated list with access dates and `sources.bib` for BibTeX;
`scripts/check_citations.py` lists the keys cited here against `sources.bib`. Keys cited so
far: [@moore2019synthesis] [@carrassi2018data] [@bannister2017review] [@geer2021learning]
[@evensen2003ensemble] [@forget2015ecco] [@martin2015status] [@moore2011roms]
[@edwards2015regional] [@oke2008representation] [@stammer2016ocean] [@zuo2019ecmwf]
[@lellouche2021copernicus] [@lellouche2018recent] [@kim2024ocean]
[@cummings2013variational] [@rtofs2026ncep] [@soca2026jcsda] [@liu2023impact]
[@neveu2016historical] [@moore2018reduced] [@rudnick2016ocean] [@todd2011poleward]
[@zaba2018annual] [@levin2020observation] [@wcofs2026coops] [@dong2017impact].
