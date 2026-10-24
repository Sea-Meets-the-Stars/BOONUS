# Keck 2027: UCSC internal application, draft v0.1

**Date:** 2026-10-22. **Authors:** JXP and Claude (Fable 5.1), prompt #4 of
`keck_2027_prompts.md`. **For:** the UCSC internal competition (InfoReady, due 25 Oct
2026, 11:59 pm). **Checked by:** `scripts/count_chars.py`, which also writes the
paste-ready ASCII text to `internal_proposal_fields.txt`.

The eight fields below are Keck's own portal Summary fields, so this text is also the
draft of the external Summary. Everything inside a ` ```keck: ` block is straight ASCII
(no curly quotes, dashes or accents) and is what gets pasted; the script collapses line
wraps to one paragraph. Text outside the blocks is for JXP.

## Working assumptions (K1-K16 in `keck_2027_prompts.md` are unanswered)

- Frame: the Round 1 recommendation, "is the coastal ocean learnable?" (K1a). No gliders
  requested; BOONUS appears as motivation only (K2). Observation-only learning is the
  headline, learned components inside the existing adjoint systems the fallback (K3).
- Key personnel: J. Xavier Prochaska (Lead PI, UCSC) and Chris Edwards (co-PI, UCSC,
  confirmed per prompt #3). Matt Mazloff and Dan Rudnick (Scripps) are written in as
  collaborators whose roles are still to be settled (K5); edit New Area and Prior Support
  if they become co-PIs.
- Preliminary data: none from the proposed work (K12). The PI's prior machine-learning
  work is described as satellite sea-surface-temperature work (the Ulmo and Nenya
  models in the `cugn` repository) plus astrophysics; confirm the wording and supply the
  funding sources marked [in brackets]. The script flags any bracket left in.
- Title for reference only (the internal form has no title field, the external one
  allows 200 characters): "Is the Coastal Ocean Learnable? Inferring the Subsurface
  State of Coastal Waters from Observations Alone" (K15a, 104 characters).

## 1. Scientific Question (up to 300 characters; no methods, instruments or field-specific frameworks)

```keck:scientific_question
Can the three-dimensional state and evolution of a coastal ocean be learned directly
from sparse, sustained observations, without a numerical model of the physics as
intermediary, and what does that reveal about how predictable the coastal ocean is?
```

Alternative if "numerical model" is judged a field-specific framework (K1c, 222
characters): "What is the information content of the coastal ocean: how far in space
and time does one sustained subsurface section constrain the waters around it, and can
that limit be found empirically rather than assumed from models?"

## 2. Potential Impact (two distinct consequences, up to 600 characters each)

```keck:potential_impact_1
Ocean state estimation would no longer require a numerical model and its adjoint. Any
coast with sustained observation could be mapped below the surface, including polar
seas and the biogeochemical fields (oxygen, pH) where physical models are weakest. It
would also make the design of observing networks empirical: a learned system reports
how much each measurement constrains the state, so where and how often to observe
becomes a measured quantity rather than a modeled one.
```

```keck:potential_impact_2
The predictability of the coastal ocean would become a measured property. How far and
for how long the information in one subsurface section travels tells us which
processes (upwelling, boundary currents, remote forcing such as El Nino) govern coastal
variability from days to years, and whether marine heat waves and low-oxygen events
have subsurface precursors that are invisible at the surface. A learned representation
of twenty years of one coastal ocean is also a new kind of climatology, one that can be
queried for anomalies as new observations arrive.
```

## 3. Risks (up to 300 characters; mitigation belongs in the Narrative)

```keck:risks
The observations may be too sparse to learn subsurface dynamics; a learned system may
not match established model-based methods; skill may not transfer beyond California;
and training on model reanalyses would make any test circular. A bounded negative
result would still fix the information content.
```

## 4. Enabling Advances (up to 300 characters)

```keck:enabling_advances
Twenty years of repeated subsurface sections off California, with absolute velocity
on every dive and oxygen since 2017, dense enough to train on and still withhold
from; 2024-25 proofs in the atmosphere that forecasts can be learned from
observations alone; differentiable learning frameworks.
```

## 5. New Area (up to 600 characters)

```keck:new_area
Yes. The PI's machine learning has been applied to satellite images of the sea surface
(unsupervised detection of extremes) and to astrophysical spectra; co-PI Edwards
co-developed the variational assimilation system that ingests these gliders today;
collaborators Rudnick and Mazloff built the glider record and the adjoint state
estimates it feeds. Learning the subsurface state directly from in situ observations,
with no numerical model in the loop and the glider's own observables (slanted dive
paths, depth-average velocity) treated natively, is new to the whole team and to the
field.
```

## 6. Peer Groups (2 to 4, up to 300 characters each)

```keck:peer_group_1
Mercator Ocean (GLONET) and the GLORYS-trained emulators XiHe and WenHai: neural
forecasters trained on a global model reanalysis, started from a classical analysis,
with surface-dominated skill. We learn from the observations, on a coast, below the
surface, with no reanalysis in the loop.
```

```keck:peer_group_2
ECMWF (GraphDOP) and the Alan Turing Institute and Cambridge (Aardvark Weather):
end-to-end learning from observations to forecast in the atmosphere, which is observed
roughly a thousand times more densely than the ocean. We ask whether that route
survives ocean sparsity, which no one has tested.
```

```keck:peer_group_3
IMT Atlantique (4DVarNet, Fablet) and M2LInES (Zanna; the Samudra emulator): learned
assimilation solvers and ocean emulators developed and scored on simulations. We score
only against withheld real observations: glider lines, years, and independent ship
surveys, never a simulation or a reanalysis.
```

A fourth candidate, the California Current adjoint systems (UCSC ROMS 4D-Var, Scripps
CASE), was dropped because Edwards is on the team and Mazloff may be (K8).

## 7. Prior Support (up to 600 characters)

```keck:prior_support
No preliminary data from the proposed work are included. Related results cited: the
California Underwater Glider Network record and climatology (NOAA Climate Observation
Division and NOAA IOOS, through SCCOOS and CeNCOOS); the UC Santa Cruz California
Current ROMS 4D-Var analyses [funding sources to be supplied by C. Edwards]; the PI's
machine-learning work on satellite sea-surface temperature [funding source to be
supplied by JXP].
```

## 8. AI Use (up to 300 characters; "applications will not be evaluated on this answer")

```keck:ai_use
Claude (Anthropic) was used under the PI's direction to survey the data-assimilation
and machine-learning literature, draft and edit text, and check citations. All
scientific claims, framing and decisions are the authors', who verified every cited
result.
```

## Biosketch checklist (second upload)

- SciENcv, NSF or NIH format, ORCID included, one per key person, combined into one
  PDF; no signature needed. Needed now for Prochaska and Edwards; for Mazloff and
  Rudnick only if they become co-PIs.
- Keck's external round also wants SciENcv Other Support per key person; not required
  internally, but worth starting.

## Where each field's claims come from

- Scientific Question, Enabling Advances, Peer Groups: `reports/data_assimilation/
  da_ai_review.md` v0.1, Sections 6 (Aardvark, GraphDOP), 7.1 (GLONET, XiHe, WenHai,
  Samudra), 7.3 (4DVarNet; no end-to-end ocean system), 9 (depth-average velocity
  assimilated nowhere; dives assimilated as vertical profiles).
- Record facts (five lines, more than 95,000 profiles by 2016, oxygen in the record from
  2017, 0.01 m/s velocity): `context/initial_context_for_claude.md` Section 3; CUGN
  funding: `context/sources/rudnick2017.md`.
- Edwards's system and its glider inputs: review Section 5.1 (Mattern et al. 2026; the
  UCSC near-real-time page). "Co-developed" is deliberately modest; Edwards can restate.
- Impact 2's precursor claim is a hypothesis, not a result; it is phrased as "whether".
