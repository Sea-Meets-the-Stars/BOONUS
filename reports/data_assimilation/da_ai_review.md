# Data assimilation in oceanography and where AI enters it

**Version:** v0.1 draft · **Date:** 2026-09-23 · **Authors:** J. Xavier Prochaska and Claude ·
**Audience:** JXP; to be shared with Matt Mazloff at v0.2 ·
**Apparatus:** `outline.md`, `reading_list.md`, `sources.md` / `sources.bib` (shared BibTeX
keys), `scripts/` (this directory). A review, not a BOONUS document.

| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 draft | 2026-09-23 | JXP and Claude (Fable 5.1) | Skeleton from `outline.md`; drafted the primer (Section 2), classical methods (3), global systems (4), regional and coastal systems with the systems table (5); placeholders for 0 and 6-11 (prompts 5-6). |
| v0.1 draft | 2026-09-23 | JXP and Claude (Fable 5.1) | Prompt 5. Section 3 (4D-Var), 5.1 and the California Current row of Table 1 rewritten from the full text of Moore et al. (2011, Part II) and Neveu et al. (2016): the "[not read]" flags replaced by the WC30/WC10 and WCRA31/WCRA14 configurations and diagnostics; Part II added as `moore2011romsII` (JXP's `moore2011.pdf` is Part II, Q&A DA52); the earlier "gliders included" statement about the Neveu reanalysis corrected (EN3 profiles; gliders not named; no velocity data). Drafted Section 6 (NWP), Section 7 with 7.1-7.4 (ocean AI by taxonomy, circularity caveat stated in the Section 7 opening), Section 8 (BGC); Figure 1 and 2 placeholders; candidate questions for Section 11 from Q&A DA49, DA50, DA53. |
| v0.1 draft | 2026-09-23 | JXP and Claude (Fable 5.1) | Prompt 6. DA52: Part I read (`moore2011a.pdf`), every "[not read; via Part II]" flag on `moore2011roms` replaced by Part I content in Sections 3 and 5.1. DA53: the UCSC glider assimilation now has sources, Mattern et al. (2026, `mattern2026improving`, Biogeosciences, open access, read in full) and the UCSC near-real-time page (`ucsc2026ccsnrt`, grey); Section 5.1, the California Current row of Table 1 and Section 8 (glider-pH assimilation) revised accordingly, the "no source in this list" wording removed. Drafted Section 9 (gliders in DA: profile vs binned, depth-average velocity, representativeness error, impacts and OSEs/OSSEs; Figure 3 placeholder), Section 10 (glossary), Section 11 (thirteen numbered questions, candidate scaffolding removed) and Section 0 (executive summary, written last). All prompt-5/6 placeholders removed; figure placeholders kept for prompt 7. |

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

Ocean data assimilation (DA) combines a model forecast with observations under stated
error statistics to produce an analysis; every operational system approximates one linear
Gaussian update applied to a state of $10^7$-$10^9$ numbers (Section 2). Two families do the
work: variational methods (3D-Var, 4D-Var), which minimize a cost function and, in 4D-Var,
carry information through the window with the model's tangent-linear and adjoint; and
ensemble methods (EnKF, EnOI), which estimate the background covariance from a set of
forecasts and need localization and inflation to survive. Unsolved in both: the background
covariance, model bias, representativeness error and initialization shock (Section 3).

The global systems split by purpose (Section 4): reanalyses and state estimates behind real
time (ECMWF ORAS5 at 1/4 degree, Mercator GLORYS12 at 1/12 degree, the ECCO adjoint
smoother), and daily analysis-forecast systems (Mercator GLO12, ECMWF OCEAN5, NOAA RTOFS,
the Navy's HYCOM/NCODA, with JEDI/SOCA as the U.S. next step). In ORAS5 in situ profiles
supply 65% of the temperature-error reduction and nearly 90% of the salinity reduction. On
U.S. coasts (Section 5) gliders are assimilated by the UCSC California Current ROMS 4D-Var
(reanalyses 1980-2012, a daily near-real-time analysis, and a 2019 coupled run that took CUGN
and IOOS glider T/S), the Scripps state estimate CASE, Rutgers doppio, and the ocean
component of NOAA's hurricane models, where 180 glider profiles cut the heat-content
underestimate under Hurricane Gonzalo from 31% to 6%.

Machine learning entered weather prediction in a fixed order (Section 6): emulators of the
forecast model (Pangu-Weather, GraphCast and GenCast, scored against the ERA5 reanalysis they
were trained on; ECMWF's AIFS, operational since 25 February 2025 and about 10% better than
IFS against radiosondes), then learned pieces inside 4D-Var verified against observations,
then end-to-end systems learning from observations alone, "not yet close" to operational
skill.

The ocean is one to three steps behind at each of the four entry points (Section 7).
Emulators (category 1) are the mature case: GLORYS12-trained XiHe, WenHai and GLONET match or
beat Mercator's operational system on 1-10 day Class 4 scores and GLONET is pre-operational;
all start from a classical analysis and replace no assimilation step. ML inside the analysis
(category 2) has one offline ocean example (sea-ice increments) and no cycled,
observation-scored one; learned covariances, observation operators and adjoint surrogates are
absent. ML replacing DA (category 3) exists for sea-surface height mapping, 17-60% below
optimal interpolation, with no ocean end-to-end or generative system. ML around DA (category
4) has an Argo quality-control method and CANYON-B, nothing for gliders. The central caveat:
the ocean emulators are trained on reanalyses that are themselves DA products with a poorly
observed subsurface, so skill against the training reanalysis measures agreement with the
target, not the ocean; only withheld observations count, and those are not fully independent
either.

Biogeochemical DA is the least mature part (Section 8): "only a few" operational systems,
mostly satellite chlorophyll in log space, physical increments that can degrade the
ecosystem, and one glider-pH assimilation, in the California Current, which more than halved
the pH misfit where T/S from the same gliders had done nothing for pH. For gliders (Section
9) the record is specific: profiles are assimilated as vertical and binned into grid cells,
with representativeness error handled by binning and tuned errors; the impact is real but
local in space and one to two days in time; depth-average velocity is used by no documented
system; and no glider DA study here involves machine learning. Thirteen questions for Matt
Mazloff close the report (Section 11).

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
system of Section 5.1 offers three incremental algorithms (Moore et al. 2011, Part I
[@moore2011roms]): I4D-Var, a primal scheme that searches the full control-vector space and
is in practice run under the strong constraint only, because "relaxing the strong constraint
in I4D-Var is challenging ... because of the very large increase in the dimension of the
problem"; and two dual schemes, 4D-PSAS and the indirect-representer R4D-Var, which search
the observation space, whose dimension "is independent of the strong and weak constraint"
and in ocean applications "is typically several orders of magnitude smaller than the
dimension of the control vector", so that model error is tractable there. All three solve
their linear system by conjugate gradients recast as a Lanczos algorithm, and the saved
Lanczos vectors are reused for the posterior-error, observation-impact and
observation-sensitivity diagnostics of Section 5.1; the dual pair differ only in the outer
loop, which 4D-PSAS relinearizes about the nonlinear model and R4D-Var about a
finite-amplitude linearization (RPROMS) through Picard iterates [@moore2011roms]. In the
California Current all three converge to the same analysis for a single outer loop, but the
dual schemes "converge to the minimum of J more slowly" and visit unphysical states on the
way, so they must be run to convergence (Moore et al. 2011, Part II [@moore2011romsII]).

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
2011 trilogy (Moore et al. 2011 [@moore2011roms]): the tangent-linear and adjoint models
TLROMS and ADROMS exist "for all of the commonly used numerical and physical options" except
most vertical-mixing closures and the bulk surface fluxes, whose linearizations are unstable
and are left out; the control vector holds increments to the initial state, surface forcing
and open boundaries, plus a model-error correction under the weak constraint; the
background-error covariances are modelled as solutions of a diffusion equation with
homogeneous, isotropic correlations that are separable in the horizontal and vertical, a
multivariate balance operator built on the temperature increment (geostrophy, hydrostatics
and a T-S relation), and no correlations in time; and the Lanczos vectors of the minimization
yield a reduced-rank posterior error covariance, per-observation impacts on any scalar
function of the circulation, and, through the adjoint of the whole 4D-Var procedure,
observation sensitivities. The authors list as unfinished the anisotropic and time-correlated
covariances and an initialization method against gravity-wave shock [@moore2011roms]. Part
II (Moore et al. 2011 [@moore2011romsII]) is the California Current application and Part III
covers observation impact and sensitivity. Part II fixes what the system does in this region. The
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
the level of EKE based on observational estimates" at 1/10 degree [@neveu2016historical].

Neither 2011-2016 paper names gliders; two later sources do, and they are the record behind the
brief's statement that CUGN is assimilated in ROMS (Section 5 of
`context/initial_context_for_claude.md`). The group's near-real-time analysis (UC Santa Cruz
2026 [@ucsc2026ccsnrt]) (grey) runs incremental strong-constraint 4D-Var at 1/10 degree with 42
levels, COAMPS forcing and HYCOM boundaries, "over 4-day cycles" performed every day for the
previous four days, and lists its inputs as AVISO sea-level anomalies, NOAA tide gauges, OSTIA
SST, Aquarius SSS, Argo, and "glider lines in the central and southern California regions ...
supported by SCCOOS and CeNCOOS" plus NANOOS gliders off Washington, with the caveat that "not
all data mentioned above is generally assimilated into every cycle"; the page carries a 2011
footer and no system paper. The peer-reviewed record is Mattern et al. (2026)
[@mattern2026improving], who ran the same 1/10 degree, 42-level ROMS coupled to the NEMUCSC
ecosystem model through 91 four-day cycles over 2019 with GLORYS12 boundaries: the reference
assimilation takes satellite SST, gridded SLA, ocean-colour chlorophyll, Argo, and "in situ
observations of temperature and salinity from gliders, including gliders from the California
Underwater Glider Network (CUGN)" and the IOOS glider archive, merged into grid-cell
super-observations, with in situ errors tuned to 0.28 C and 0.15 in salinity; the paper then
adds glider pH, the "pH work" of Q&A DA53, described in Sections 8 and 9. JXP confirms the
glider assimilation independently (pers. comm., 2026). What no source in this list documents is
the observation-error and super-observation treatment of the near-real-time glider stream or
any use of glider depth-average velocity (Sections 9 and 11). Beyond the analysis, the adjoint
gives observation impacts and the reduced-rank array modes of the California Current observing
system (gliders, HF radar, satellites) (Moore et al. 2018 [@moore2018reduced]) [abstract only;
AGU host refuses scripted fetches]; Rudnick (2016) [@rudnick2016ocean] sums up the observing
side: "in coastal regions, where Argo yields fewer profiles, a sustained glider program can be
the dominant source of in situ data". The treatment of glider profiles and depth-average
velocity is deferred to Section 9.

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
| California Current ROMS 4D-Var (WCRA31, WCRA14; near-real-time) | UC Santa Cruz | ROMS, 1/10 deg, 42 levels (WC30/WC10 in the 2011 tests) | ROMS 4D-Var, dual (R4D-Var/4D-PSAS) strong constraint in the reanalyses; incremental strong-constraint 4D-Var in near-real time; weak constraint available | 8 d windows overlapping 4 d (7 d in 2011); 4 d cycles daily in near-real time | not named in the reanalyses (EN3 profiles; no velocity); yes in near-real time and in 2019 (CUGN and IOOS glider T/S; glider pH in experiments) | reanalysis 1980-2010 and 1999-2012; near-real-time analysis | [@moore2011romsII] [@neveu2016historical] [@ucsc2026ccsnrt] (grey) [@mattern2026improving] |
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

*[Figure 2: 2018-2026 timeline of AI-in-DA milestones, NWP and ocean tracks; made in prompt 7.]*

Machine learning entered weather prediction before ocean prediction, and in a fixed
order: emulators of the forecast model first, then learned pieces of the assimilation
system, then attempts to learn the whole map from observations to forecast. ERA5
supplied a dense, hourly, four-decade training set, and the NWP centres already had the
adjoint and cycling infrastructure that learned components plug into. Geer (2021) [@geer2021learning] makes
the kinship exact: the 4D-Var cost function is the loss function of a network, the
adjoint is backpropagation, and cycled DA is a recurrent network. Most of the emulators
below are trained on, and scored against, ERA5, itself a DA product; this is the NWP form
of the circularity caveat stated in Section 7, and it is why the verification note on each
exemplar separates scores against a reanalysis from scores against observations.

**Emulators.** Pangu-Weather (Bi et al. 2023 [@bi2023accurate]) was the first ML model
to beat the operational IFS on reanalysis-based scores: trained on ERA5 1979-2017,
validated on 2019 and tested on 2018, it reports a 5-day Z500 RMSE of 296.7 against
333.7 for IFS, more than 10,000 times faster *[maturity: realistic hindcast; verified
against: ERA5 only, cyclone tracks against IBTrACS]*. GraphCast (Lam et al. 2023
[@lam2023learning]), a graph neural network on the 0.25 degree ERA5 grid trained on
1979-2015 with 2018-2021 held out, outperforms HRES on 90% of 1380 targets in under a
minute per 10-day forecast. GraphCast is scored against ERA5 and HRES against its own
step-0 analysis (HRES-fc0), with no verification against stations or radiosondes *[maturity: realistic hindcast; verified
against: ERA5 and HRES-fc0, no observations]*. GenCast (Price et al. 2024
[@price2024probabilistic]) supplies the probabilistic step: a conditional diffusion model
producing 15-day, 0.25 degree ensembles in about 8 minutes, trained on ERA5 1979-2018 and
tested on 2019, with better CRPS than the ECMWF ensemble on 97.2% of 1320 targets
*[maturity: realistic hindcast; verified against: ERA5 vs HRES-fc0 respectively, no
observations]*. The operational exemplar is AIFS (Lang et al. 2024 [@lang2024aifs]
(preprint)), ECMWF's own model at about 1 degree, pre-trained on ERA5 1979-2020 and
fine-tuned on IFS operational analyses for 2019-2020, operational as AIFS Single since
25 February 2025 [@ecmwf2025aifs] (grey). Its 2022
scorecard shows gains over IFS "of the order of 10%" through the troposphere, and skill
was measured against radiosonde and SYNOP observations as well as analyses: a day-1
degradation seen against analyses "is not present in verification against radiosonde
observations" *[maturity: operational; verified against: operational analyses and
radiosonde and SYNOP observations]*. AIFS is still initialised from the IFS 4D-Var
analysis; the emulators replace the forecast model, not the assimilation.

**Learned components inside DA.** The second family leaves 4D-Var in place and replaces
a piece of it. Bonavita and Laloyaux (2020) [@bonavita2020machine] trained a neural
network on ECMWF's 12-hourly analysis increments for 2018, coarsened to T21 (about 900
km), to predict the model-error tendency. Offline it explains about 14% of the increment
variance for mass, about 5% for wind and none for humidity. They then ran it inside
cycled 4D-Var at the operational 9 km configuration for 16 July to 24 August 2019, in
strong- and weak-constraint form. This is the one exemplar in this section whose assimilation
experiments are scored against observations rather than a DA product: background
departures for radiosondes, GPS-RO, winds and surface pressure, and 72 h temperature
forecast error against independent GPS-RO retrievals. The weak-constraint runs roughly
halve the observed surface-pressure biases and extend the stratospheric bias correction
into the troposphere, though most differences are not statistically significant and the
infrastructure is "not yet fully in place for reliable operational use" *[maturity:
realistic hindcast; verified against: radiosonde, GPS-RO and surface observations]*.
Hatfield et al. (2021) [@hatfield2021building] attack the adjoint bottleneck: they
emulate the IFS non-orographic gravity-wave-drag scheme with a network trained on the
scheme's 2015-2017 inputs and outputs, differentiate it to obtain tangent-linear and
adjoint models, and run cycled 4D-Var at TCo399 for December 2018-February 2019 (177
forecasts). RMSE differences from the reference are no more than 4% and not significant,
and departures against ATMS and GPS-RO show no degradation *[maturity: realistic
hindcast; verified against: own analyses, plus departures against assimilated ATMS and
GPS-RO observations]*, the null that an adjoint surrogate must first show.

**End-to-end observation-to-forecast.** The third family removes the assimilation system
as a separate object. Aardvark Weather (Allen et al. 2025 [@allen2025endtoend]) maps
satellite and in situ observations directly to 1.5 degree gridded forecasts and to
station forecasts, ingesting "approximately 8%" of the observations available to
conventional NWP. With 2018 held out it matched or outperformed GFS on the headline
gridded variables, and its station forecasts were competitive with station-corrected
HRES and NDFD out to 10 days. Because the encoder and processor are pre-trained against
ERA5 before end-to-end fine-tuning, the observation-only claim holds at deployment, not
in training *[maturity: realistic
hindcast; verified against: ERA5 for gridded fields, held-out HadISD stations for point
forecasts]*. GraphDOP (Alexe et al. 2024 [@alexe2024graphdop] (preprint)), from ECMWF,
trains on observations alone, 2004-2021 with 2022 for validation, predicting the next
12 h of observations with no reanalysis in the loop except an ERA5-departure
quality-control step. Verification is in observation space: for SYNOP 2 m temperature
GraphDOP beats IFS by a global 15% at day 1 (winter 2022-2023), with mixed results at
days 3-5 and degraded AMSU-A departures; gridded fields for January 2023 are scored
against ERA5 "employed exclusively for verification." Skill "is not yet close to matching
state-of-the-art NWP performance" *[maturity: realistic hindcast; verified against: SYNOP
and satellite observations, ERA5 for gridded fields only]*, but it is the nearest
existence proof that the map can be learned without a reanalysis.

**Generative and learned DA.** The fourth family keeps the analysis as the product but
learns the update. Manshausen et al. (2025) [@manshausen2025generative] use score-based
data assimilation with a diffusion prior trained on HRRR analyses of 10 m wind and
precipitation for 2018-2021 at 3 km over Oklahoma; observations enter only at inference.
Guided by 40 stations and tested on 2017, a 15-member ensemble gives around 10% lower
RMSE than the HRRR analysis at the held-out stations, while a single member is similar to
HRRR. The held-out stations are among the METAR winds HRRR itself assimilates, so the
comparator is not blind, the ensembles are underdispersive, and the authors call it a
proof of concept *[maturity:
realistic hindcast; verified against: withheld surface stations]*. FuXi-DA (Xu et al.
2025 [@xu2025fuxida]) learns the assimilation of satellite radiances into an ML forecast
model: FY-4B AGRI brightness temperatures (channels 8-15, averaged to 0.25 degree) are
combined with a 6 h FuXi background initialised from ERA5 to produce an analysis, with
ERA5 as both training target and ground truth. Per the Methods section
the split is training June 2022-May 2023, validation June-July 2023, test
August-December 2023, although the Results section states the training span
inconsistently as extending to June 2024, which would overlap the test period; the
report uses the Methods split (DA43). Analysis RMSE for the reported fields (R300, R500,
Z300, Z500) falls by about 2-4.5%, and Z500 forecast error by 0.67% at day 1, decaying to
0.34% at day 7 *[maturity: realistic hindcast, offline and non-cycled; verified against:
ERA5]*. Without cycling or independent observations it sits a step behind Manshausen et
al. evidentially, though it assimilates the harder observation type.

What carries over to the ocean is the sequence (emulate the model, learn pieces of the
assimilation, then learn the whole map, which Section 7 traces on the ocean track of
Figure 2) and the question of whether skill against the training reanalysis survives
verification against independent observations, answered in part in NWP by AIFS and by
Bonavita and Laloyaux. What does not carry over is the data: the ocean is observed at a
small fraction of the atmosphere's density, and there is no ocean equivalent of ERA5
constrained at anything like observation density, so an ocean emulator trained on the
reanalyses of Section 4 inherits more of the model and less of the ocean than GraphCast
inherits of the atmosphere.

## 7. AI in ocean DA, by where ML enters the pipeline

*[Figure 1: the four ML entry points over one DA cycle (Mermaid); made in prompt 7.]*

The ocean literature is organized by where ML enters the cycle of Section 2 (Fig. 1): as a
surrogate for the forecast model (category 1, Section 7.1), as a learned component inside the
classical analysis (category 2, 7.2), as a learned map replacing the analysis (category 3,
7.3), or around the cycle in quality control, downscaling and sampling design (category 4,
7.4), with categories 2 and 3 as surveyed by Cheng et al. (2023) [@cheng2023machine]. Each
approach carries a tag giving its category, maturity and what its skill was measured against.

One caveat is stated here once and referred to below as **the circularity caveat**. The
global forecast emulators of Section 7.1 are trained on GLORYS12 (Section 4.1) and the
regional one on a ROMS-EnKF reanalysis; both are DA products carrying the deficiencies of their
model and of the observing system that fed them. An emulator fitted to such a record learns
its biases along with its dynamics, and skill scored against the same reanalysis measures
agreement with the training target, not with the ocean. The GLONET paper concedes that its
point-wise scores against GLORYS12 assess forecasts that "align closely with the data on which
they were trained" [@elaouni2025glonet]; the WenHai authors state the dependence outright: the AI systems "stand
on the shoulders of numerical GOFSs", and GLORYS "is approximated as the ground truth ... with
caution about the fidelity of the GLORYS reanalysis in representing reality" (Cui et al. 2025
[@cui2025forecasting]). Skill against the ocean is therefore established only against withheld
observations, in practice the GODAE OceanView IV-TT Class 4 protocol (Argo profiles, drifter
SST and currents, along-track SLA), and even that is not fully independent, because the same
platforms fed the reanalysis.

### 7.1 Emulators and surrogates

The clean case emulates a model, not a reanalysis. Samudra (Dheeshjith et al. 2025
[@dheeshjith2025samudra]) is a ConvNeXt U-Net trained on GFDL OM4 output over 1975-2014; it is
"stable for centuries", 150 times faster than OM4, and over an 8-year rollout "underestimate[s]
trends by 20% to 50% relative to OM4" *[cat. 1; maturity: realistic hindcast; verified against:
held-out years of the parent model, no observations]*. Samudra 2 (Yuan et al. 2026
[@yuan2026samudra2]) (preprint) scales the design to 1, 1/2 and 1/4 degree: upper-ocean
global-mean temperature $R^2$ rises from 0.56 to 0.87 at 1 degree over 2014-2022 rollouts,
while deep-ocean $R^2$ stays negative at every resolution
*[cat. 1; maturity: realistic hindcast; verified against: the parent model OM4]*. Both escape
the circularity caveat by construction; neither contains an assimilation step.

Three GLORYS12-trained forecast emulators are the ocean counterparts of the NWP emulators of
Section 6. XiHe (Wang et al. 2024 [@wang2024xihe]) (preprint) is a 1/12 degree transformer
forecasting to 10 days; the GLORYS12 record used spans January 1993 to December
2020, the training set is called "25-year", which would end in 2017 or 2018, and the
evaluation covers January 2019 to December 2020, so the withholding of the test years is
implied but never stated (Q&A DA34). On Class 4 metrics its 6-day vertically averaged
temperature error is 11.10% below PSY4's *[cat. 1; maturity: realistic hindcast; verified
against: withheld Class 4 observations; training overlap not stated]*. WenHai (Cui et al. 2025
[@cui2025forecasting]) works at 1/12 degree over 0-643 m, predicting tendencies with bulk-formula
air-sea fluxes inside the network; trained on GLORYS12 and ERA5 over 1993-2018 and validated
on 2019, it was then run from GLO12v4's own initial conditions and forcing for April-November
2024, the fairest comparison in this list.
Against Class 4 observations its vertical-mean RMSE is 6.02% (5.64%) below GLO12v4's for
temperature (salinity) profiles and its 10-day CRPS 3.5-10.0% lower; winter was not tested *[cat. 1; maturity: realistic hindcast
bordering on pre-operational; verified against: withheld Class 4 observations]*. GLONET (El
Aouni et al. 2025 [@elaouni2025glonet]) is Mercator's own: Fourier neural operators with a CNN
at 1/4 degree, trained on GLORYS12 1993-2019 with 2020 for validation, then initialised weekly
from GLO12 analyses over January-July 2024. It "surpasses XIHE in SLA and surface currents"
and beats GLO12 at 5-9 day leads, while GLO12 keeps the advantage for SST at all leads; a
"pre-operational pipeline" exists and "experimental daily forecast[s]" are served on EDITO,
with no statement that it runs in the operational chain
*[cat. 1; maturity: pre-operational; verified against: withheld Class 4 observations and,
point-wise, GLORYS12]*. All three match or beat the systems they learned from on 1-10 day
Class 4 metrics; all three start from a GLO12 analysis, so none replaces an assimilation step,
and the circularity caveat applies to each.

Regional emulators are few. OceanNet (Chattopadhyay et al. 2024 [@chattopadhyay2024oceannet])
is a Fourier neural operator for SSH alone in the northwest Atlantic, trained on a 4 km
ROMS-EnKF reanalysis over 1993-2018 and scored for 2019-2020 against the same reanalysis out
to 120 days: better than a ROMS forecast for the Gulf Stream, 500,000 times cheaper, but "more
diffusive than reanalysis"; the authors call it "initial steps" *[cat. 1; maturity: realistic hindcast; verified against: the training
reanalysis, no observations]*. The circularity caveat applies in full; no emulator of a
California Current system appears in this list.

### 7.2 ML inside classical DA

The ECMWF pattern of Section 6, Bonavita and Laloyaux (2020) [@bonavita2020machine] learning
model error from analysis increments and then cycling the correction inside 4D-Var scored
against radiosondes and GPS-RO, has one published ocean-side counterpart. Gregory et al.
(2023) [@gregory2023deep] train a CNN to map the state and tendencies of GFDL's SPEAR ice-ocean
model to the sea-ice-concentration increments of its ensemble Kalman filter over 1982-2017,
with an untouched 2018-2021 extension; daily pattern correlations with the increments run from
0.62 (Arctic autumn) to 0.80 (Antarctic summer). The study is offline, a demonstration of
"feasibility" with an online correction inside SPEAR as the goal, and skill is measured against
the increments, a DA product, not observations *[cat. 2; maturity: realistic hindcast, offline;
verified against: the DA increments it learns]*. The cycled, observation-scored step has no
ocean paper in this list; nor has the adjoint surrogate of Hatfield et al. (2021)
[@hatfield2021building], and the ROMS 4D-Var of Section 5.1 runs hand-coded linearizations. Learned background-error covariances and
learned observation operators are likewise absent from the ocean literature here; whether any
ocean centre runs a learned component inside its analysis is a question for Matt (Section 11). On the BGC side, Gloege et al. (2022) [@gloege2022improved] is the one ocean category-2
case scored against independent observations (Section 8). The boundary case of Q&A DA36c: Zanna and Bolton (2020) [@zanna2020data] discover
mesoscale closures from idealized 3.75 km MITgcm double-gyre simulations coarse-grained to 30
km, run online only after scaling by factors of 0.5-0.7 found "through trial and error" *[cat. 2
(boundary); maturity: idealized; verified against: the high-resolution simulation, no
observations]*; a learned parameterization changes the model, not the assimilation, and is
named only so the DA30 list is complete.

### 7.3 ML replacing DA

4DVarNet is the ocean community's route from toy systems to real data. Fablet et al. (2021)
[@fablet2021learning] learn jointly a neural dynamical prior for a weak-constraint 4D-Var cost
and a neural solver that replaces gradient descent, "with no need to explicitly code the
adjoint operators" [@cheng2023machine]. On Lorenz-63 the reconstruction error is 1.34 against
3.55 for gradient descent on the true-ODE cost, on Lorenz-96 0.38 against 1.06, and the
authors ask whether the findings "generalize to other systems, especially higher-dimensional
ones" *[cat. 3;
maturity: idealized; verified against: the simulated truth]*. 4DVarNet-SSH (Beauchamp et al.
2023 [@beauchamp2023fourdvarnet]) is the answer on the NATL60 observing-system simulation
experiment: a 1/60 degree North Atlantic simulation sampled along simulated nadir and SWOT
tracks, trained on 2013 and tested on 22 October-2 December 2012, with reconstruction error
30-60% below the operational optimal interpolation and
resolved scales of 0.83 degree and 8.01 days against 1.42 degree and 12 days for DUACS;
application "to real altimetry datasets" is "a future challenge" *[cat. 3; maturity: realistic
OSSE; verified against: the simulated truth, not observations]*. The ocean-data-challenges
repositories (2026 [@oceandatachallenges2026]) (grey) make that distinction a benchmark: the
2020a NATL60 challenge is the OSSE, the 2021a challenge on real altimetry the OSE. Martin et
al. (2023) [@martin2023synthesizing] supply the OSE half: a ConvLSTM trained on real altimetry
and SST in the Gulf Stream Extension over 2010-2020, with 2017 kept aside and CryoSat-2
withheld as ground truth, gives 17% lower SSH RMSE and 30% smaller resolved scales than DUACS
and 24-27% lower surface-current RMSE against independent AOML drifters
*[cat. 3; maturity: realistic hindcast (OSE); verified against: withheld observations]*. The
pair defines what "verified" means for a neural mapper: against a simulation it is scored
everywhere, against the ocean only along tracks it did not see; the OSE never touches a
reanalysis, so the circularity caveat does not arise. No generative or end-to-end assimilation
system for the ocean (the counterparts of Section 6) appears in this list.

### 7.4 ML around DA

Quality control has the one mature ocean exemplar. Sugiura and Hosoda (2020)
[@sugiura2020machine] apply the signature method to 8.2 x 10$^4$ Argo T/S profiles spanning
more than 1000 m to reproduce the JAMSTEC delayed-mode flag, training on 40% and
cross-validating on 60%; at the cutoff that
"never misidentifies" a good profile it still accepts bad ones "with a probability 0.6", and the
reference is the human flag, not the ocean *[cat. 4; maturity: realistic, offline method
demonstration; verified against: human delayed-mode QC flags]*. Nothing comparable for glider
streams appears in this list. CANYON-B (Bittig et al. 2018 [@bittig2018canyonb]), neural
estimation of nutrients and carbonate variables from T, S and O$_2$, belongs here by taxonomy
as a "transfer function between components of the ocean observing system" and is described in
Section 8 *[cat. 4; maturity: realistic, released method; verified against: independent
GO-SHIP cruises]*. For anomaly detection, adaptive sampling, downscaling and ML-designed OSSEs
this list holds no ocean paper, and the report says so rather than borrowing from the
atmosphere. The classical counterpart of ML sampling design is the adjoint machinery of Section
5.1: the array modes and observation degrees of freedom of Moore et al. (2011)
[@moore2011romsII] and the reduced-rank array modes of the California Current observing system
(Moore et al. 2018 [@moore2018reduced]) [abstract only], which quantify what an array can move
in the analysis without any training set and so sit outside the circularity caveat.

## 8. Biogeochemical DA

Biogeochemical (BGC) DA is the least mature part of the field. Fennel et al. (2019)
[@fennel2019advancing] count "only a few" operational forecasting systems that assimilate
BGC variables; the rest are pre-operational or research. Two features set it
apart from Sections 3-5.

**Coupling.** A BGC model rides on a physical model, whose increments can hurt it: "assimilation of physical observations in coupled models often does not improve but
degrades the biogeochemical state" [@fennel2019advancing], at least partly because
physical and BGC variables are updated independently, violating property-property
relationships (e.g. nutrient against density); accounting for their correlation reduces
the damage substantially. This is initialization shock in BGC form: an analysis nearer
the T/S data but inconsistent with the ecosystem it carries.

**Non-Gaussian, positive-definite variables.** Chlorophyll and nutrients are bounded below
by zero and skewed, so the Gaussian machinery of Section 2 is applied to their logarithm:
the Met Office FOAM-HadOCC/MEDUSA systems assimilate satellite chlorophyll as a 3D-Var
update of surface log10(chlorophyll) and spread it to other BGC variables by a balancing
scheme; the California Current ROMS-NEMURO system uses a lognormal 4D-Var
[@fennel2019advancing]. The increments are therefore multiplicative: one log-space
correction is a small absolute change in a gyre, a large one in a bloom. The
multivariate updates that follow are model-dependent; their adequacy "hinges on the accuracy of biogeochemical models and is not well
tested."

**What is assimilated.** Mainly satellite ocean-colour chlorophyll, a surface-only,
imperfect biomass proxy. BGC-Argo profiles are entering: chlorophyll and
nitrate pre-operationally in the Mediterranean, Argo oxygen in the Black Sea
[@fennel2019advancing]. In that 2019 survey glider BGC sensors appear only at the margins: their assimilation is "ongoing" on the Northwest European Shelf, and the Great Barrier Reef
eReefs EnKF used withheld glider fluorescence (improved by 45%) for validation, not input. The
one glider-BGC assimilation in this list is later and in the California Current: Mattern et al.
(2026) [@mattern2026improving] assimilate glider pH into the coupled ROMS-NEMUCSC 4D-Var of
Section 5.1, directly measured on the MBARI pH-sensor Spray on Line 67 (error 0.013) and
statistically estimated from CUGN T, S and O$_2$ elsewhere (error 0.05), jointly with
estimated alkalinity because pH alone leaves alkalinity and DIC underdetermined, "analogous to
temperature and salinity estimates being underdetermined by density observations". Assimilating
physical data and chlorophyll alone, including T/S from the same gliders, "has negligible
impact" on pH; adding pH and alkalinity "more than halves the average RMSE of the CUGN pH data";
and a hybrid that feeds the assimilated T and S into the ESPER regression often beats the
biogeochemical model without carbonate DA, so that "physical ocean models and DA systems can
obtain reasonable carbonate system estimates" without a BGC model. The limits are the
univariate covariances of ROMS 4D-Var (no cross-variable terms, so pH increments barely touch
oxygen or nitrate) and the reliance on estimated alkalinity.

**The systems.** Mattern et al. (2017) [@mattern2017data] [not read; via
`fennel2019advancing`] assimilated physical and chlorophyll observations into the
California Current ROMS 4D-Var with two different BGC models; the 1/10-degree
ROMS-NEMURO system runs quasi-operationally, assimilating only satellite chlorophyll. The
adjoint route of Section 4.1 has two BGC descendants. B-SOSE (Verdy and Mazloff 2017
[@verdy2017data]) [abstract only] adds carbon, oxygen and nutrient cycles to the Southern
Ocean State Estimate (2008-2012; floats, ships, satellites; closed budgets); it captures 44% of the surface pCO2 variance in Drake Passage and over 60%
of the oxygen-profile variance at 200 and 1000 m. ECCO-Darwin (Carroll et al. 2020
[@carroll2020ecco]) [abstract only] couples the MIT Darwin ecosystem model to ECCO adjoint
physics, optimizing the biogeochemistry by a Green's function adjustment of initial
conditions and six parameters (1995-2017); global sink 2.47 +/- 0.50 Pg C/yr.

**The BGC-Argo OSSE.** Ford (2021) [@ford2021assimilating] ran a global 1/4-degree
NEMO-MEDUSA OSSE with 3D-Var, assimilating synthetic ocean colour and BGC-Argo profiles
for sensors on one in four Argo floats (comparable to the planned 1000-float array) or on
all of them. Ocean colour alone constrained surface chlorophyll; BGC-Argo added 7% and
15% at the surface for the two arrays and much more below the mixed layer, and improved
unassimilated pCO2. The OSSE ignored observation biases; gliders "may also bring additional benefits, for instance for O2 in the mixed layer."

**Where ML is being tried.** Two released methods are typical; both are trained and
verified on observations, so the circularity caveat of Section 7 does not apply.
CANYON-B (Bittig et al. 2018 [@bittig2018canyonb]) estimates nutrients and carbonate
variables from T, S and O2, the variables a glider carries, with
Bayesian neural networks trained on GLODAPv2 bottle data (521 cruises, 1972-2013, 20% set
aside) and validated on 19 later GO-SHIP cruises (2012-2017): RMSEs of 0.68 (NO3), 0.051
(PO4), 2.3 (silicate), 6.3 (AT) and 7.1 (CT) umol/kg, 0.013 in pH and 20 uatm in pCO2
*[cat. 4; maturity: released method with code, not a DA component; verified against:
independent GO-SHIP bottle data]*. LDEO-HPD (Gloege et al. 2022 [@gloege2022improved])
uses XGBoost to learn the SOCAT-minus-model pCO2 misfit of nine global BGC models and adds
it back, mapping pCO2 for 1982-2018; seven whole years (about 16% of the data) were
withheld, plus independent BATS, HOT and GLODAP data *[cat. 2; maturity:
realistic hindcast, released product; verified against: withheld SOCAT years and
independent time series]*. Neither touches coupling or non-Gaussianity; both stretch the
sparse observations that Fennel et al. call the binding constraint.

## 9. Gliders in DA

*[Figure 3: one assimilation cycle marking where glider profiles and depth-average velocity
enter and where representativeness error arises (Mermaid); made in prompt 7.]*

A glider delivers two kinds of observation. The first is a T/S profile from each descent or
ascent: a Spray dive to 1000 m takes about 6 h and covers about 6 km at a forward speed near
0.25 m/s, so the "profile" is a slanted section through a moving ocean, and a sustained line
yields such profiles at a density no other in situ platform matches on a coast (57 times as
many as CalCOFI stations on Line 90 in 2010-2012) (Rudnick 2016 [@rudnick2016ocean]). The
second is the depth-average velocity over the dive, from dead reckoning between GPS fixes,
accurate to 0.01 m/s, which with the thermal-wind shear gives absolutely referenced
geostrophic velocity, the "fundamental value" of gliders for sustained transport observation
[@rudnick2016ocean]. The DA literature in this list uses the first and, so far as its texts
say, not the second.

**Profile or binned.** Every system here assimilates glider T/S as vertical profiles and
reduces them before use. Shulman et al. (2009) [@shulman2009impact] assimilated the AOSN-II
gliders of August-September 2003 (five Sprays to 400 m, ten Slocums to 200 m) into a 1-4 km
NCOM of Monterey Bay through NCODA, a 3D multivariate OI, every 12 h: "temperature and
salinity data from each descent/ascent glider path from a particular dive are treated as
vertical profiles", which "introduces additional error into the glider data assimilation,
because glider paths have angles sometimes reaching 26 degrees"; with the Sprays' nominal
horizontal resolution of 2.3 km and the Slocums' 0.8 km, "the spatial error in treating
gliders as vertical profiles does not exceed one model grid point", and assimilation of
"threaded" profiles, each with latitude and longitude changing with depth, was left as
future research. Coarser grids bin further: the California Current ROMS 4D-Var merges "all
observations within each model grid cell, over a 6 h time window" into one super-observation
whose standard deviation is taken as its representativeness error (Moore et al. 2011
[@moore2011romsII]); Mattern et al. (2026) [@mattern2026improving] keep at most one
super-observation per variable per grid cell and time step, note that "for dense data sets,
such as glider-based observations, the process of creating super-observations can reduce the
number of data points considerably", and score their fit against the original observations
instead, which comes out better than against the super-observations because the
terrain-following cells are larger at depth and the misfit is larger near the surface. The
hurricane systems thin in time: Dong et al. (2017) [@dong2017impact] assimilated only the
0000 UTC profiles of two gliders, 180 profiles in three months against 7,562 Argo profiles
(Section 5.5). No source here assimilates a dive as the slanted, time-varying path it is,
although a 4D-Var observation operator, which already samples the model at each observation's
own time, could.

**Depth-average velocity.** The sources are consistent and negative. Part II's observation
list has no velocity; the WCRA reanalyses assimilated "no velocity observations"
[@neveu2016historical]; Mattern et al.'s reference dataset takes glider "temperature and
salinity" although, as they note, the CUGN gliders "measure temperature, salinity, water
velocity, chlorophyll fluorescence, and more recently, oxygen" [@mattern2026improving]; NCODA
analyses vector velocity, but Shulman et al. assimilated glider T/S only; Dong et al. and Liu
et al. (2023) [@liu2023impact] [abstract only] list T/S; and the Scripps state-estimate
abstracts are silent (Todd et al. 2011 [@todd2011poleward]; Zaba et al. 2018
[@zaba2018annual]) [abstract only]. No system in this list is documented as assimilating
glider depth-average velocity, the one glider quantity that is an absolute reference for the
circulation; whether CASE does is the first question of Section 11.

**Representativeness error.** For a profile in a several-km grid the dominant term in
$\mathbf{R}$ is not the sensor. Oke and Sakov (2008) [@oke2008representation] [abstract
only] define representation error as the part of an observation due to "unresolved
processes and scales in the model", estimate it as a function of resolution by averaging
mapped and along-track sea-level anomalies onto the model grid and projecting the residual
onto T and S, and find values "typically greater than or comparable to measurement error,
particularly in regions of strong mesoscale variability". The California Current system has
handled it two ways: the 2011 configuration adds the super-observation scatter to instrument
errors of 0.1 C and 0.01 (Section 5.1) [@moore2011romsII]; the 2019 configuration starts
from 0.1 C and 0.05 and lets a consistency-based tuning (the "FPI" of Mattern et al. 2018,
not in this list) raise them to 0.28 C and 0.15 for all in situ T and S, about three and
fifteen times the starting values, with a 50 km horizontal decorrelation length in
$\mathbf{B}$ [@mattern2026improving]. Dong et al. prescribe 0.01 C and 0.02 psu for glider
profiles [@dong2017impact], an order of magnitude tighter, and attribute the analysed mixed
layer that stays too shallow to "inaccurate horizontal and vertical covariance of the
statistical interpolation approach". Part of the mismatch is the glider's own sampling:
at constant depth, wavelengths shorter than about 30 km are contaminated by temporal
variability, while on isopycnals they are resolved [@rudnick2016ocean], so a profile through
a front carries variance the grid cannot hold and the sensor did not cause. Moore et al.
(2019) [@moore2019synthesis] call representativeness "probably the most significant
contributor" to $\mathbf{R}$ "and ... perhaps the least well understood" (Section 3).

**Observation impact, OSEs and OSSEs.** The published impact studies agree on the sign and
on the footprint. In Monterey Bay, assimilating gliders with unchanged (biased) atmospheric
forcing cut the SST bias at mooring M1 during the 20-23 August 2003 relaxation from 1.7 to
0.5 C and the RMS from 2.15 to 1.12 C, as much as correcting the 30-40% overestimate of
short-wave radiation did; at M2 during upwelling the bias fell from 0.7 to 0.4 C; surface
salinity bias and RMS fell "by more than 50%" at both moorings; subsurface temperature RMS at
M1 fell from 1.38 to 0.76 C; and the complex correlation of the subsurface velocity profile
during relaxation rose from 0.66 to 0.96 with the angular error down from 92 to 7 degrees. The
gain did not persist: "for 1-1.5 days after glider data assimilation ends" the SST returned
to the free run's, and "for more extended forecasts it is critical to have accurate
atmospheric forcing" [@shulman2009impact]. In the hurricane systems, 180 glider profiles
raised the analysed tropical cyclone heat potential at the glider from 59 (no assimilation)
to 81 kJ cm$^{-2}$ against the observed 86, an underestimate of 31% cut to 6%, while all
standard observations gave 92 and all plus gliders 81; the barrier layer, about 20 m thick,
"did not exist" without gliders; the 48 h forecast temperature error above 30 m stayed below
0.2 C with gliders; yet the assimilation of "glider observations alone does not have a
significant impact on the intensity forecast", because their footprint was "too localized
along the storm track", and the combination of standard data and gliders was best (Section
5.5) [@dong2017impact]. Liu et
al. (2023) [@liu2023impact] [abstract only] found six gliders in a SOCA-MOM6 analysis
thickened the barrier layer, reduced storm cooling and improved the Isaias intensity forecast
beyond satellites alone. The OSSE view is more measured: in a fraternal-twin HYCOM OSSE of
the 2014 season, altimetry gave "the greatest positive impact, followed by Argo floats and
sea surface temperature", and regional glider deployments "modest positive impacts on ocean
analyses that were limited by (1) errors in the horizontal structure of the increment field
imposed by individual gliders and (2) memory loss in the spreading of these corrections by
nonlinear model dynamics" (Halliwell et al. 2017 [@halliwell2017north]) [abstract only]. In
the California Current the adjoint diagnostics say the same in their own terms: more than
90% of the 2002-2004 observations were redundant and the array modes were set "primarily by
a combination of the satellite data locations and the priors" [@moore2011romsII]; after three
decades of 4D-Var "much of the space spanned by the background error covariance is
unconstrained by the present ocean observing system" (Moore et al. 2018 [@moore2018reduced])
[abstract only]; and in the 2019 cross-validation, assimilating the neighbouring CUGN lines
still improved pH along a withheld Line 67 transect, but "assimilation of large temperature and
salinity datasets, including CUGN data, does little to improve overall estimates at the
pH-sensor glider line", and in one case advected increments raised the salinity misfit above
the free run's [@mattern2026improving]. The Scripps state estimate is the one case where a
glider network is both constraint and evaluation set (Section 5.2) [@zaba2018annual]
[abstract only]; doppio's platform impacts are "remarkably robust" in their geography and
include remote observations, but the abstract gives no per-platform number for gliders
(Levin et al. 2020 [@levin2020observation]) [abstract only]. For BGC, the Argo OSSE of Ford
(2021) [@ford2021assimilating] remarks only that gliders "may also bring additional benefits,
for instance for O2 in the mixed layer" (Section 8).

What the record establishes is therefore specific: glider T/S improve the analysed upper
ocean where and when the glider is, by tens of percent in T/S misfit and by the presence or
absence of sharp features (barrier layers, halocline depth), with a memory of one to two days
in a coastal model and a footprint set by the decorrelation length of $\mathbf{B}$; the
impact on integrated forecasts (storm intensity) is small unless the glider sits on the
track; representativeness error is handled by binning and by tuning $\mathbf{R}$, not by
modelling the dive; depth-average velocity is not used; and none of the glider DA studies in
this list involves machine learning at any of the four entry points of Section 7.

## 10. Glossary

Definitions follow Carrassi et al. (2018) [@carrassi2018data] and Moore et al. (2019)
[@moore2019synthesis] unless a section is named; symbols are those of Box 1. Grouped: the
estimation problem, the algorithms, the observations, evaluation, and the AI vocabulary.

*The estimation problem.*
**Background** ($\mathbf{x}^b$): the prior state, usually the previous forecast.
**Analysis** ($\mathbf{x}^a$): the posterior state after the observations are used.
**Increment** ($\delta\mathbf{x}$): analysis minus background, the quantity DA actually
computes.
**Innovation** ($\mathbf{d}$): observation minus the background mapped to observation space;
the only place the observations enter.
**B** and **R**: background- and observation-error covariances; their ratio sets how far an
innovation moves the state, and their structure sets where.
**Observation operator** ($\mathcal{H}$): the map from model state to what the instrument
measures, including interpolation to the observation's position and time.
**Balance operator**: the part of B that ties increments in T to S, sea level and velocity
(geostrophy, hydrostatics, a T-S relation); disabled in the WCRA reanalyses, univariate in the
2019 UCSC system (Sections 5.1, 8).
**Strong / weak constraint**: whether the model is assumed perfect over the window (control =
initial state, forcing, boundaries) or allowed an error term with covariance Q.
**Primal / dual**: minimizing in the control-vector space (I4D-Var) or in the space of the
observations (4D-PSAS, R4D-Var), which is smaller and admits the weak constraint (Section 3).
**Representativeness error**: the part of an observation the model cannot represent at its
resolution; folded into R, estimated from the scatter of a super-observation or from
sub-grid SLA variance (Section 9).

*The algorithms.*
**OI / EnOI**: the linear Gaussian update with a prescribed static B, or with a B from a fixed
set of model anomalies.
**3D-Var / 4D-Var**: iterative minimization of the cost function at one time, or over a window
with the model carrying information between observation times; **incremental** means the
cost is made quadratic by linearizing about the background (inner loop) and relinearized a
few times (outer loop).
**TLM and adjoint**: the linearized model and its transpose; the adjoint carries an
observation's influence backward in time and is the gradient engine of 4D-Var.
**Lanczos vectors**: the by-product of the conjugate-gradient minimization in ROMS, reused for
posterior errors, observation impacts and array modes.
**EnKF**: Kalman update with B from an ensemble of nonlinear forecasts; **localization**
suppresses spurious long-range sample covariances, **inflation** restores the spread the
ensemble loses each cycle.
**Hybrid / EnVar**: B blended from a static and an ensemble covariance; 4DEnVar uses ensemble
trajectories in place of the TLM and adjoint.
**FGAT**: first guess at appropriate time; innovations computed at the observation's own time
inside a 3D-Var.
**IAU**: incremental analysis update; the increment is added gradually over the cycle to
limit initialization shock.
**Super-observation**: the average of all observations of one type in one grid cell and time
bin, assimilated in place of the individual values.
**Array modes / degrees of freedom of signal**: the patterns an observing array can excite in
the analysis, and the number of independent pieces of information it supplies (1-6% of the
observation count in the 2002-2004 California Current cycles).

*Observations and experiments.*
**OSE**: observing-system experiment, real assimilation with and without a platform.
**OSSE**: observing-system simulation experiment, the same on a simulated "nature run"
sampled synthetically; **fraternal twin** when the forecast model differs from the nature run.
**Observation impact / FSOI**: the contribution of each observation to a scalar measure of the
analysis or forecast (forecast-sensitivity observation impact), computed with the adjoint of
the assimilation system.
**Depth-average velocity**: a glider's mean horizontal velocity over a dive, from the offset
between dead-reckoned and GPS positions; an absolute velocity reference (Section 9).
**Threaded profile**: a glider dive treated with its position varying along the path rather
than as a vertical profile at one point.
**Barrier layer / TCHP**: the salinity-stratified layer beneath the mixed layer that
suppresses storm-driven cooling, and the tropical cyclone heat potential (heat above the
26 C isotherm) that hurricane models depend on.

*Evaluation.*
**Class 4**: the GODAE OceanView protocol scoring forecasts against withheld or
near-independent observations (Argo profiles, drifter SST and currents, along-track SLA)
rather than against a gridded analysis.
**Desroziers diagnostics**: consistency checks of the prescribed B and R against innovation
statistics.
**Circularity caveat** (Section 7): skill measured against the reanalysis a model was trained
on measures agreement with the training target, not with the ocean.
**Maturity tags**: `idealized` (toy or simulated system), `realistic hindcast` (real system,
past period), `pre-operational` (running in a centre's test chain), `operational` (in the
production chain).

*The AI vocabulary.*
**Emulator / surrogate**: a network trained to reproduce a model's or a reanalysis's next
state; replaces the forecast model, not the assimilation.
**Learned component inside DA**: a network replacing one piece of the classical cycle
(model-error tendency, adjoint, B, H) with the rest unchanged.
**End-to-end**: a network trained from observations to forecast (or to analysis) with no
separate assimilation step.
**Generative DA**: sampling the posterior with a diffusion or score-based prior conditioned on
observations.
**Neural mapper / interpolation**: a network that turns sparse observations into a gridded
field without a dynamical model (4DVarNet, ConvLSTM SSH mapping).
**QC**: quality control, the accept/reject decision on each observation before assimilation.

## 11. Questions for Matt

The open points the literature left, framed as JXP's reading notes for the conversation
with Matt Mazloff; each names the section it comes from.

1. **CASE and glider velocity (Sections 5.2, 9).** Does the California State Estimate
   assimilate CUGN depth-average velocity, or only the T/S profiles, and how does it set the
   representativeness error for a Spray profile on its grid? No source in this list documents
   any system assimilating glider depth-average velocity.
2. **CASE method details (Section 5.2).** The Todd et al. (2011) and Zaba et al. (2018)
   abstracts give neither the window length nor the controls of the adjoint state estimate;
   which paper should be cited for the CASE configuration?
3. **The UCSC near-real-time system (Sections 5.1, 9).** Mattern et al. (2026) and the UCSC
   web page document CUGN and IOOS glider T/S in the 2019 experiments and the near-real-time
   inputs, but the web page carries a 2011 footer. Is there a citable system paper for the
   near-real-time analysis, and how does it treat glider profiles (super-observation window,
   observation errors, any velocity)? What is the status of the glider-pH assimilation, and
   is it headed for the near-real-time chain?
4. **Weak constraint in the California Current (Sections 3, 5.1).** Neveu et al. (2016)
   list the missing weak constraint and time correlations among the limits of WCRA31/14 and
   report an under-estimated EKE; does the current UCSC configuration run weak-constraint
   4D-Var, and did it change the EKE result?
5. **WCOFS (Section 5.4).** No public source states its DA method or observation types, only
   "real-time observations in a three-day window ... once a day"; does Matt know the
   configuration, and whether glider profiles have entered it?
6. **HAFS ocean DA (Section 5.5).** Has the operational HAFS ocean component moved from
   RTOFS-initialized HYCOM with no ocean DA (Kim et al. 2024) to MOM6 with Marine JEDI/SOCA
   (Liu et al. 2023, a case study), and if so since which HAFS version?
7. **SOCA (Section 4.2).** The solver list recorded from the JEDI documentation (3D-Var FGAT,
   hybrid 3DEnVar, LETKF) and the GFSv17/GEFSv13 plan could not be re-found on 2026-09-23;
   which solvers does SOCA run today, and what is the operational timeline?
8. **ML inside an operational ocean analysis (Section 7.2).** Does any operational ocean
   centre run a learned component inside its assimilation step (as opposed to an emulator
   alongside it, like GLONET at Mercator)? The list has none.
9. **Learned B, H and adjoint for ROMS (Section 7.2).** The list holds no ocean paper that
   learns the background-error covariance or the observation operator, and none that replaces
   the hand-coded TLM and adjoint of ROMS 4D-Var with a learned surrogate (the ocean
   counterpart of Hatfield et al. 2021); does Matt know of such work, published or in
   progress, and would a surrogate adjoint be acceptable inside the UCSC or Scripps systems?
10. **Verifying an emulator on a coast (Section 7.1).** The GLORYS12-trained emulators are
    scored by Class 4 metrics dominated by Argo; how should a subsurface forecast be verified
    off California, where Argo is sparse and the sustained profiles are gliders that the
    reanalysis may itself have assimilated?
11. **Glider QC and anomaly detection (Section 7.4).** The list has ML quality control for
    Argo only; what QC does the CUGN stream receive before it enters CASE or the UCSC system,
    and is any of it learned?
12. **BGC state estimation and glider sensors (Section 8).** What would B-SOSE-style adjoint
    state estimation of the California Current need from glider O2 and pH, given that the
    UCSC 4D-Var found physical and chlorophyll assimilation had "negligible impact" on pH and
    that its covariances are univariate?
13. **Per-platform glider impacts (Section 9).** Levin et al. (2020) compute adjoint
    observation impacts by platform in doppio; has the same been done for CUGN in either
    California Current system, and what fraction of the analysis impact do the gliders carry
    against satellite SST and SLA?

## References

See `sources.md` for the annotated list with access dates and `sources.bib` for BibTeX;
`scripts/check_citations.py` lists the keys cited here against `sources.bib`. Keys cited:
[@moore2019synthesis] [@carrassi2018data] [@bannister2017review] [@geer2021learning]
[@evensen2003ensemble] [@forget2015ecco] [@martin2015status] [@moore2011roms] [@moore2011romsII]
[@ucsc2026ccsnrt] [@mattern2026improving] [@shulman2009impact] [@halliwell2017north]
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
