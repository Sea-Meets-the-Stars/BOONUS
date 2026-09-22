# Context Prompts

## Goals

We will generate context for the BOONUS project.  
This will be one or more files for Claude to rely
on when they need it.

## Context

Here are a number of things to start with in the `context` folder:

1. boon.pdf -- A short write-up describing the global BOON project
2. IOOS_CoastalClimateSignal_Final.pdf -- An IOOS report on the Coastal Climate Signal
3. rudnick-2016-ocean-research-enabled-by-underwater-gliders.pdf -- An Annual Review article by Dan Rudnick on the use of underwater gliders in ocean research
4. BOONUS_one_pager.pdf -- A one-pager describing the BOONUS project for Sam Forde
5. BOONUS_multi_pager.pdf -- A multi-pager describing the BOONUS project that I shared with the Simons Foundation

## Prompts

### First bits

1. Read this file.  Examine all of the items in the Context section.  We are eventually going to create a context file named `context/initial_context_for_claude.md`.  We will first have a conversation with Claude to determine what to include in the context file.  Place a series of questions in the Q&A section and I will answer them.  Use Fable if you can.  Log your work.  

2. Read this file.  I have answered your first round of questions in Q&A.  Read those and
then ask me another round.  Use Fable if you can.  Log your work.  Let me know if you need
me to download any additional files and place them in the `context` folder.

3. Read this file.  I have answered your second round of questions in Q&A.  Read those, act accordingly,
and then ask me another round if needed.  Use Fable if you can.  Log your work.  Do not write the
context file yet.

4. Read this file.  I have answered your third round of questions in Q&A.  Read those, act accordingly.
Then proceed to write the context file.  Use Fable if you can.  Log your work.  
If you have any additional questions, ask me in the Q&A section.

### Data assimilation

1. Read your context.  We will generate a report that describes the state-of-the-art in data assimilation for oceanography.  With emphasis on where and how AI is being adopted in data assimilation.  Before generating the report, we will discuss it.  Ask me a series of questions in Q&A/Data assimilation.

2. I have answered your first round of questions in Q&A/Data assimilation.  Read those and ask another round as you need.  Use Fable if you can.  Log your work.

3. I have answered your second round of questions in Q&A/Data assimilation.  Read those and ask another round as you need.  Use Fable if you can.  Log your work.

4. Ok, I think we are ready to work on the Report.  Please update the `data_assimilation_prompts.md` file with a set of prompts to do so.  Use Fable if you can.  Log your work.

## Q&A

### Data assimilation

#### Round 1 (2026-09-22)

I have re-read the brief (`context/initial_context_for_claude.md` v0.1) and the digests.
The brief already fixes several things this report must respect: ROMS 4D-Var
assimilation of CUGN is `[demonstrated]`; the AI-driven component (nominal lead Matt
Mazloff) is `[planned; scope TBD]` as some combination of adaptive piloting, learned
components inside assimilation, and anomaly detection; line locations will come from
observing-system design experiments. Questions are numbered DA1, DA2, ... so they do not
collide with Q1-Q57 above. Where I have a recommendation I state it. Answer inline with
`>A.` lines; "as recommended" is enough.

#### DA-A. Purpose and audience

DA1. **What is the report for?** Options: (a) an internal reference that steers BOONUS
     design (what DA systems will ingest BOONUS data, what they need from it);
     (b) an advocacy-grade review arguing that sustained coastal glider data are the
     limiting input for AI-era ocean prediction; (c) a neutral, publishable review of
     the field. Recommendation: (a) written to the standard of (b), so it can later
     be cut into a proposal section. Neutral (c) is a much larger job.
>A. This first document will be to educate JXP. We will write separate documents for BOONUS in the future. 

DA2. **Primary reader.** Oceanographers who are not DA specialists (you, Dan, glider
     operators), DA/modeling specialists (Mazloff and colleagues), or non-specialist
     funders? This sets how much of the DA machinery (Kalman filters, adjoints,
     background-error covariances) I explain from scratch. Recommendation:
     oceanographers who are not DA specialists, with a one-page primer.
>A. JXP.  But I will also share with Matt Mazloff.

DA3. **Length and form.** Recommendation: a Markdown report of roughly 10-15 pages in
     `reports/data_assimilation/` with `sources.md` and `sources.bib` (style rule 8),
     a one-page executive summary at the top, and 2-4 figures (a taxonomy diagram of
     AI-in-DA approaches; a timeline; a table of operational systems). Or would you
     prefer LaTeX/PDF, a shared Claude Doc, or an HTML artifact?
>A. I like 10-15 pages and Markdown.  Include figures where you can.

#### DA-B. Scope

DA4. **Spatial scope.** Global ocean DA (ECMWF, Mercator, NOAA RTOFS, Navy, ECCO) as
     background, with the depth spent on regional and coastal DA (U.S. West Coast
     ROMS 4D-Var, NOAA's operational coastal forecast systems, boundary-current
     systems elsewhere)? Recommendation: yes, roughly 1/3 global, 2/3 regional and
     coastal, because that is where BOONUS data land.
>A. Yes, roughly 1/3 global, 2/3 regional and coastal.

DA5. **Physical only, or biogeochemical too?** The brief lists oxygen, pH, chlorophyll
     and the Darwin model, and BGC assimilation is where DA is least mature and where
     ML is most tempting. Recommendation: include BGC as a full section.
>A. Yes, include BGC as a full section.

DA6. **Reanalysis and state estimation, or forecasting only?** ECCO-style
     smoother/state estimation (Mazloff's home turf, e.g. the Southern Ocean and
     California Current state estimates) versus operational filtering for forecasts.
     Recommendation: both, with a clear split, since BOONUS claims both a climate
     record and 3-day forecasts.
>A. Yes, both.  With a clear split.

DA7. **Time window.** Classical methods summarized briefly (OI, 3D/4D-Var, EnKF and
     hybrids), with the literature review concentrated on roughly 2019-2026 for AI?
     Recommendation: yes.
>A. Yes

DA8. **Should atmospheric (weather) AI be covered?** The AI-in-DA story is being written
     mostly in numerical weather prediction: ML emulators (GraphCast, Pangu, FourCastNet,
     AIFS), then ML used inside or instead of DA (learned 4D-Var, end-to-end
     observation-to-forecast systems, diffusion-model DA). Ocean work follows with a
     lag. Recommendation: one section on NWP as the leading indicator, then ocean.
>A. Follow your recommendation

#### DA-C. The AI emphasis

DA9. **Taxonomy.** I propose to organize the AI material by where ML enters the DA
     pipeline: (1) ML emulators/surrogates of the ocean model (as the forecast model or
     for cheap ensembles); (2) ML inside classical DA (learned background-error
     covariances, model-error/bias correction, observation operators, ensemble
     inflation/localization, tangent-linear/adjoint surrogates); (3) ML replacing DA
     (end-to-end mapping of observations to state or forecast; generative/diffusion
     reconstructions; neural interpolation of sparse observations, e.g. SSH mapping);
     (4) ML around DA (observation QC, super-resolution/downscaling, anomaly detection,
     adaptive sampling and OSSE design). Does this match how you and Mazloff think
     about it, or do you want another axis (e.g. maturity: research / pre-operational
     / operational)?
>A. I like the way you have defined it.

DA10. **Maturity and honesty.** Consistent with style rule 1 (no hype), should every AI
      approach carry a maturity tag (e.g. `idealized`, `realistic hindcast`,
      `pre-operational`, `operational`) and a note on how its skill was verified
      (against withheld observations vs. against a reanalysis it was trained on)?
      Recommendation: yes; the training-on-reanalysis circularity is the central
      caveat for ocean ML and the natural argument for independent in situ data.
>A. Yes, use your recommendation.

DA11. **The BOONUS thesis.** Should the report explicitly argue that AI models trained
      largely on reanalyses inherit the reanalyses' poorly constrained coastal
      subsurface, so sustained subsurface observations (gliders) become *more*
      valuable, not less, as AI spreads? This is my reading of where the argument is
      strongest, but it must be evidenced, not asserted. Keep, soften, or drop?
>A. Avoid for now

DA12. **Glider-specific DA.** Should I dedicate a section to how gliders enter DA
      (profile vs. binned assimilation, depth-average velocity as an observation,
      representativeness error, observation-impact studies and OSEs/OSSEs showing
      glider value, including the IOOS hurricane-glider results and the California
      Current ROMS work)? Recommendation: yes; it connects the review to BOONUS design.
>A. Yes, it connects the review to BOONUS design.

DA13. **Which AI component work to frame toward.** The brief lists three strands for
      the BOONUS AI component. Should the report end with a section mapping the
      literature onto those three strands (what exists, what BOONUS would add, what a
      first demonstration could be, e.g. an ML emulator of the CCS ROMS state
      estimate constrained by CUGN)? Or stop at the review and leave design to a later
      prompt? Recommendation: a short "implications for BOONUS" section, tagged
      `[TBD]`/`[aspirational]`, no commitments.
>A. Stop at the review.

#### DA-D. Sources and people

DA14. **Literature access.** WebFetch is allowed only for `doi.org`, `tandfonline.com`,
      `opg.optica.org` and the ASLO Wiley domain; WebSearch is not in the allow list.
      For a 2019-2026 review I will need arXiv, ESS Open Archive, AGU/Wiley (JAMES,
      GRL, JGR), AMS journals, Frontiers, Copernicus (GMD, OS, NPG), Nature, and
      ECMWF/NOAA pages. Options: (a) you add those domains and WebSearch to
      `.claude/settings.json`; (b) you approve fetches one by one; (c) you download key
      PDFs into a private folder (e.g. `context/da/`, gitignored). Recommendation: (a)
      plus (c) for anchor papers. I will not cite anything I have not verified by
      DOI.
>A. (a) plus (c) for anchor papers.

DA15. **Anchor papers.** Candidates I would want in hand (to verify, not assumed):
      Moore et al. 2019 (Front. Mar. Sci., ocean DA for operational and reanalysis
      systems, OceanObs'19); Carrassi et al. 2018 (WIREs Clim. Change, DA in the
      geosciences); Geer 2021 (Phil. Trans. R. Soc. A, ML vs. DA for learning Earth
      system models); Cheng et al. 2023 (IEEE/CAA JAS, ML with DA and UQ review); and
      recent ocean emulator papers (e.g. Samudra, and the Chinese ocean forecast
      emulators). Do you or Mazloff have a reading list, or specific papers you want
      featured (including your own or Mazloff's)?
>A. I like your list, let's use it.

DA16. **Naming people.** Style rule 5 limits names to JXP, Rudnick and Mazloff. A
      literature review must cite authors. I propose: author names appear only in
      citations (as in any review), never as prospective partners or collaborators.
      OK?
>A.  It is perfectly fine to cite authors 

DA17. **Mazloff's role in this report.** Should the draft be written for Mazloff to
      review (and possibly co-author), and should it describe his group's work (e.g.
      the California Current and Southern Ocean state estimates, ML-DA projects) in
      detail? If so, can you point me to what he considers representative?
>A.  I am the main reader of this report.  I will share with Matt Mazloff.

#### DA-E. Process

DA18. **Brief update.** Once the report exists, should a short digest go into
      `context/sources/` and a pointer into the brief (v0.2, Section 5), so future
      sessions know the AI-DA landscape without rereading the report?
      Recommendation: yes.
>A. yes

DA19. **Model and rounds.** Earlier prompts asked for Fable; this one does not. Which
      model do you want for the drafting, and do you expect another Q&A round before
      the outline, or should the next step be an outline for your approval?
      Recommendation: next step is a one-page outline plus reading list for approval,
      then the draft.
>A.  Use Fable for this effort

#### Round 2 (2026-09-22)

Round 1 is fully answered and every answer is now a fixed decision: the report educates
JXP and will be shared with Matt Mazloff; 10-15 pages of Markdown with figures; roughly
1/3 global and 2/3 regional and coastal; a full BGC section; reanalysis/state estimation
and forecasting both, clearly split; classical methods in brief, AI literature 2019-2026;
NWP as the leading indicator; the four-way taxonomy of where ML enters DA; a maturity tag
and a verification note on every AI approach; the "AI makes gliders more valuable" thesis
is left out; a glider-specific DA section; the report stops at the review; literature
access by (a) new domains in settings plus (c) anchor PDFs in a private folder; the
anchor list stands; authors are cited freely; a digest and brief v0.2 pointer afterwards;
Fable throughout. Nothing below reopens those. Two of the round-1 answers need a concrete
follow-through before drafting can start (DA20, DA21), and DA19's "use Fable" left the
outline-versus-draft question open (DA22). The rest settle shape and depth. Answer inline
with `>A.` lines; "as recommended" is enough.

#### DA-F. Access and files (needed before any drafting)

DA20. **The domain list for `.claude/settings.json`.** Nothing has been added yet: the
      allow list still holds only `doi.org`, `www.tandfonline.com`, `opg.optica.org` and
      the ASLO Wiley host, and no `WebSearch`. I propose adding `WebSearch` plus
      `WebFetch(domain:...)` for: preprints and metadata (`arxiv.org`,
      `essopenarchive.org`, `api.crossref.org`, `api.semanticscholar.org`); publishers
      (`agupubs.onlinelibrary.wiley.com`, `onlinelibrary.wiley.com`,
      `rmets.onlinelibrary.wiley.com`, `journals.ametsoc.org`, `www.frontiersin.org`,
      `gmd.copernicus.org`, `os.copernicus.org`, `npg.copernicus.org`,
      `egusphere.copernicus.org`, `www.nature.com`, `www.science.org`,
      `royalsocietypublishing.org`, `ieeexplore.ieee.org`, `www.sciencedirect.com`,
      `linkinghub.elsevier.com`, `link.springer.com`, `www.pnas.org`); ML venues
      (`openreview.net`, `proceedings.neurips.cc`, `proceedings.mlr.press`); and
      operational centers (`www.ecmwf.int`, `www.jcsda.org`, `ecco-group.org`,
      `www.mercator-ocean.eu`, `marine.copernicus.eu`, `polar.ncep.noaa.gov`,
      `tidesandcurrents.noaa.gov`, `ioos.noaa.gov`, `gliders.ioos.us`, `github.com`).
      Expect some publisher hosts to return 403 to automated fetchers regardless (the
      El Nino 2026 `sources.md` records this for several), which is why (c) matters.
      Recommendation: authorize me to make this edit to the BOONUS `settings.json` in the
      next prompt (BOONUS only; `CLAUDE.md` names IOPtics as the upstream for that file,
      and I would not touch IOPtics). Strike any host you object to.
>A.  That all is fine

DA21. **Anchor-PDF folder and its gitignore rule.** `context/da/` does not exist, and
      the current rule `context/*.pdf` does not reach into subfolders (verified with
      `git check-ignore`: `context/da/x.pdf` is *not* ignored today). Proposal: create
      `context/da/` holding the anchor PDFs, replace the rule with `context/**/*.pdf`
      (one rule for the current folder and every future subfolder), and add a tracked
      `context/da/README.md` listing each PDF with citation, DOI and "how to obtain",
      mirroring `context/README.md`. On who downloads: Moore et al. 2019 (Frontiers),
      Carrassi et al. 2018 (WIREs), Geer 2021 (Phil. Trans. A), Cheng et al. 2023
      (IEEE/CAA JAS; also on arXiv) and Samudra (arXiv/JAMES) are open access as far
      as I know, so I could fetch them with `curl` once you approve that command; the
      Chinese ocean-emulator papers may be paywalled (Nature-family journals). Would
      you rather download all of them yourself into `context/da/`, or let me fetch the
      open-access ones and leave you only the paywalled ones? Recommendation: the
      latter, with the rule and README edits authorized in the same prompt as DA20.
>A. Go with your recommendation.

#### DA-G. Process and shape

DA22. **Outline first, or draft directly?** DA19 recommended a one-page outline plus an
      annotated reading list for your approval before the draft; your answer fixed the
      model but not the sequence. Recommendation: outline plus reading list as the next
      prompt (roughly 40-60 candidate references, each with a one-line reason and a
      verification status), then the draft. For a 10-15 page document that Mazloff will
      read, a half-hour of your review at the outline stage is cheap insurance against
      a wrong emphasis. Alternative: go straight to a full v0.1 and iterate.
>A. Go with your recommendation.

DA23. **Location and filenames.** Nothing exists yet. Proposal, following the El Nino 2026
      exemplar: `reports/data_assimilation/da_ai_review.md` (versioned in its header,
      `v0.1, date, JXP and Claude`, with a change-log table), beside `sources.md`,
      `sources.bib`, `figs/` and `scripts/`. The outline and reading list from DA22
      would live in the same folder as `outline.md` and `reading_list.md`, so they stay
      with the report rather than in this prompt doc. OK, or a different name and place?
>A. That looks very good

DA24. **Level of mathematics.** Options: (a) prose only; (b) a compact boxed primer with
      the handful of equations that everything else refers to (the linear Gaussian
      update and gain, the 3D/4D-Var cost function, the ensemble Kalman gain and why
      localization and inflation are needed), plus a notation table, with the rest of
      the report in prose; (c) derivations. Recommendation: (b). You are a working
      scientist fluent in Bayesian inference, and Mazloff will skip the primer; the
      equations give the AI sections a fixed vocabulary (what "learning B", "learning
      the observation operator" or "replacing the adjoint" actually means).
>A. (b)

DA25. **Register, and analogies to inference you already know.** Some DA machinery has
      exact counterparts in astrophysical and statistical practice: optimal
      interpolation is Gaussian-process regression (kriging); 4D-Var is MAP estimation
      with a dynamical prior; the EnKF is a Monte Carlo Kalman filter; ECCO-style state
      estimation is a smoother over a decades-long window. Recommendation: use such
      analogies sparingly, only where exact, and mark the primer "skippable for DA
      specialists" so the document does not lecture Mazloff. Tone: a technical
      briefing, not a textbook and not a pitch (style rule 1 still applies even though
      the BOONUS thesis is out). Object if you want a different register.
>A. Sounds fine

#### DA-H. Figures and citations

DA26. **How the figures are made, and whether any uses CUGN data.** Candidates: (1) a
      taxonomy figure of the four ML entry points laid over a DA cycle; (2) a 2018-2026
      timeline of AI-in-DA milestones, NWP on one track and ocean on the other; (3) a
      schematic of one assimilation cycle (background, observations, analysis, forecast)
      marking where glider profiles and depth-average velocity enter and where
      representativeness error arises; (4) a table of operational systems (a table, not
      a figure). Tooling options: matplotlib scripts run in `ocean14` and committed to
      `scripts/` (reproducible, PNG in `figs/`, per style rule 9 and the exemplar), or
      Mermaid diagrams inline in the Markdown (render on GitHub with no build step but
      are box-and-arrow only). Recommendation: matplotlib for the timeline and anything
      that carries data; Mermaid for the two flow schematics. On data: a review does
      not need new computations, so v0.1 would be schematic only; an optional later
      figure could show CUGN profile density along a line against the resolution of a
      ROMS grid, from the local `$OS_SPRAY/CUGN` files, if you want one concrete image.
      Schematic only for v0.1?
>A. Those look good

DA27. **Citation volume, style and verification.** Recommendation: 40-60 references;
      author-year in the text, e.g. "(Carrassi et al. 2018)", with the BibTeX key in
      `sources.md`/`sources.bib` as in the exemplar; every DOI verified with
      `curl -sI https://doi.org/<doi>` and the access date recorded; arXiv preprints
      allowed but flagged `preprint` in both the text and the bibliography; grey
      literature (ECMWF newsletters and technical memoranda, NOAA technical reports,
      JEDI/SOCA documentation, GitHub READMEs) allowed with URL and access date, flagged
      `grey`. A `scripts/check_sources.py` would re-verify every DOI and URL before
      delivery, as `check_links.py` does for the El Nino report. OK?
>A. OK

#### DA-I. Depth on specific systems (candidates to verify, not commitments)

DA28. **Ocean systems: paragraph or table row.** Candidates I expect to find in the
      literature, each to be verified before it is named in the report. Global:
      ECMWF's ocean reanalysis and analysis (ORAS/OCEAN5 line), Mercator Ocean's global
      analysis and the GLORYS reanalysis, NOAA RTOFS, the U.S. Navy HYCOM/NCODA system,
      NOAA's JEDI/SOCA ocean DA for the coupled UFS, and ECCO (v4 and the regional
      state estimates). Regional and coastal U.S.: the UC Santa Cruz California Current
      ROMS 4D-Var system, the Scripps California Current state estimate, the Rutgers
      Mid-Atlantic ROMS 4D-Var ("doppio"), NOAA's NOS operational forecast systems
      (including the West Coast OFS), and the ocean component of NOAA's hurricane
      models that ingests hurricane-glider data. Elsewhere: Australia's Bluelink and
      Copernicus regional systems as boundary-current comparators. Recommendation: a
      paragraph for every system that assimilates or has assimilated gliders in U.S.
      waters; a table row for the rest. Add or drop any?
>A.  Use your recommendation.

DA29. **NWP AI systems: how many, how deep.** Candidates to verify: emulators GraphCast,
      Pangu-Weather, FourCastNet, FengWu/FuXi, NeuralGCM and ECMWF's AIFS (with its
      ensemble); ML inside or instead of DA: ECMWF's observation-driven work (GraphDOP),
      the end-to-end Aardvark Weather system, FengWu-4DVar / FuXi-DA style learned
      assimilation, and diffusion-model DA (DiffDA, score-based DA). Recommendation:
      one paragraph per family rather than per model (emulators; learned DA; end-to-end
      observation-to-forecast; generative DA), naming two or three exemplars each, so
      the NWP section stays near 2 pages and the ocean sections get the depth. OK?
>A. OK

DA30. **Ocean ML systems to feature.** Candidates to verify: Samudra (an emulator trained
      on a GFDL ocean model's output) and the GLORYS-trained Chinese and Mercator
      emulators (e.g. Xihe, WenHai, GLONET) for the emulator strand, with the
      trained-on-reanalysis caveat from DA10 made concrete; 4DVarNet and the ocean
      SSH-mapping data challenges for neural mapping; ML bias correction and learned
      parameterizations inside ocean models for the "ML inside DA" strand; ML QC and
      anomaly detection on Argo and glider streams for "ML around DA". Anything on your
      or Mazloff's radar that must appear (ECCO-adjacent ML surrogates, for example)?
      Recommendation: proceed with these and let the reading list (DA22) be the place
      you add or strike.
>A. Follow your recommendation.

#### DA-J. Apparatus

DA31. **Glossary and a "questions for Matt" appendix.** Recommendation: yes to a DA
      glossary (background, analysis, increment, innovation, B and R matrices, adjoint
      and tangent-linear model, localization, inflation, OSE/OSSE, observation impact
      and FSOI, representativeness error), and yes to a short closing appendix listing
      the questions the literature left open that a state-estimation expert would
      settle quickly, framed as your reading notes for the Mazloff conversation. Cut
      either if you prefer a leaner document.
>A.  Sounds good

DA32. **The prompt doc for this work.** The DA prompts and Q&A currently sit inside
      `context_prompts.md`, whose goal statement is the context brief. Fine to continue
      here, or would you rather I start `claude_prompts/data_assimilation_prompts.md`
      when the outline prompt comes (you would move prompt #3 there; I would not move
      your text)? Recommendation: a new prompt doc, following the one-doc-per-effort
      pattern (`start_up.md`, `context_prompts.md`).
>A. Start a new prompt doc.

#### Round 3 (2026-09-22)

No further questions. Every round-2 answer accepted the recommendation, so DA1-DA32 are
now fixed decisions and nothing that remains open would change the outline; the reading
list is the agreed place to add or strike specific papers (DA30). Acted on this round:
the `settings.json` domain list (DA20), the `context/**/*.pdf` rule and `context/da/`
folder with its README (DA21), the anchor PDFs fetched where open access (DA21), and the
new prompt doc `claude_prompts/data_assimilation_prompts.md` (DA32), which carries a
compact summary of DA1-DA32 so future sessions need not reread this file. **One download
request:** Geer (2021), *Phil. Trans. R. Soc. A* 379, 20200089,
doi:10.1098/rsta.2020.0089, is not open access (Europe PMC) and the publisher returns
403 to fetchers; please save it as `context/da/geer2021.pdf`. The next step is the
outline plus annotated reading list, driven from the new prompt doc (JXP to write the
prompt under `### Outline and reading list` there).

### First

I have read all five items in the Context section (text of every page, plus the two
figures in the multi-pager: the flag map of proposed sites and the Spray photo).
Questions are grouped by theme. Where I have a recommendation I state it. Answer inline
with `>A.` lines as in `start_up.md`; a bare "yes" or "as recommended" is enough.

### A. What the context file is for

1. **Who reads `context/initial_context_for_claude.md`, and for which tasks?** My reading
   of `CLAUDE.md` is: fresh Claude sessions that will draft advocacy and specification
   documents (one-pagers, proposals, figures, requirements) and build data products
   from CUGN. Recommendation: a fact-anchored reference brief that a session reads
   before writing anything about BOONUS, not a narrative. Is it also meant to steer
   analysis code, or only the writing?
>A. Correct, not a narrative.  A fact-anchored reference brief makes sense.

2. **One file, or a brief plus per-source digests?** Recommendation: the brief itself
   (roughly 3-5 pages) plus `context/sources/<name>.md`, one per PDF, holding a
   structured digest (key claims, numbers, quotable lines, page references). The brief
   cites the digests; future sessions do not re-read 11 MB of PDF; the PDFs remain the
   ground truth.
>A. Your recommendation is fine.

3. **How to record disagreements between sources.** The five documents disagree on
   several numbers (Section B). Should the brief carry (a) one canonical value you pick
   here, (b) the range with attribution, or (c) both, with the canonical value marked?
   Recommendation (c).

>A. (a)

### B. Canonical facts the sources disagree on

4. **The name.** README and one-pager: "Boundary Ocean Observing Network *of* the United
   States". Multi-pager: "... *for* the United States", and once "BONUS". Which is
   canonical? Recommendation: "of", matching `CLAUDE.md` and `README.md`.

>A. Let's go with "for".  Always BOONUS

5. **Fleet size.** One-pager: "~100 glider network", then "100+ gliders (50+ in the water
   at all times)". Multi-pager: "~100 active (200+ total)". That is a factor of two in
   gliders in the water. Which is right? Should the brief record the derivation (number
   of lines x gliders per line x turnaround overhead) so the number can be defended?
>A. Let's go with 100+ gliders (50+ in the water at all times).

6. **Spatial footprint.** Multi-pager: "~500 km offshore", "entire U.S. coastline".
   One-pager: "entire EEZ ... hundreds of kilometers offshore". The U.S. EEZ extends
   200 nautical miles, about 370 km. Is 500 km the intended line length (CUGN lines
   run 350-550 km) or is the EEZ the intended framing? Which coasts count: the map
   flags Alaska, Hawaii, the West Coast, Gulf, East Coast and Puerto Rico. Great Lakes?
   Guam, American Samoa, the other Pacific territories? IOOS has 11 Regional
   Associations including the Great Lakes and Pacific Islands.
>A. Let's stick with EEZ and beyond, ~500km offshore.

7. **Sampling design.** Both BOONUS documents: profiles to 500-1000 m every 3-6 h, 3-6 km
   apart, consistent with Rudnick 2016 and boon.pdf. Is the canonical design CUGN
   practice (500 m dives, about 3 km and 3 h between profiles) or 1000 m? This sets
   line occupation time and therefore fleet size.
>A. 500m is good

8. **Sensor suite.** Multi-pager: temperature, salinity, horizontal currents, dissolved
   oxygen, chlorophyll fluorescence, pH, optical backscatter; the HAB paragraph adds
   nitrate. The one-pager lists none. Which sensors are core (every glider) and which
   are optional? Is "currents" depth-averaged velocity only, or ADCP? Is pH core,
   given boon.pdf (2018) still called pH sensors maturing?
>A. Undecided.  But let's go with the multi-pager for now.

9. **Platform.** The photo is a Spray, and the one-pager mentions "new partnerships with
   industry (for both platforms and sensors)". Is BOONUS Spray-based or
   platform-agnostic (Spray, Slocum, Seaglider)? This determines who the "~10
   substantial U.S. programs" partners are.
>A. TBD.  Spray is the default

10. **"Less than 10% of U.S. coastal waters are regularly sampled in situ"**
    (multi-pager, Why Now). What is the source? If it is your estimate, should I write
    a script that computes it (fraction of EEZ area within some distance of a
    sustained glider line or mooring) so it becomes a defensible, repeatable metric?
    That is squarely the kind of metric `CLAUDE.md` says this repository will produce.
>A. It is fine.  Trust me

11. **Models and terminology.** One-pager: ECCO (NASA global), ROMS coastal, the Darwin
    ecosystem model, "AI-driven predictive systems", 3-day forecasts. The multi-pager
    uses "ROMs" for regional ocean models generally, which collides with ROMS the code.
    Should the brief fix terminology (e.g., "regional ocean models" spelled out, ROMS
    reserved for the software)? Is the "AI-driven" element a real component with a
    named lead, or pitch language to be toned down?
>A. Use ROMS.  Yes, the AI-driven component is critical.  It will need a lead.  The nominal is
Matt Mazloff.

12. **Planning horizon.** "Sustained for over 10 years" (one-pager) versus "multi-decade"
    (multi-pager). Canonical figure?
>A. Let's go with "over 10 years".

### C. Framing and positioning

13. **Boundary currents or coastal ocean?** BOON (boon.pdf) is about boundary *currents*
    (Gulf Stream, Kuroshio, California Current) with a transport-and-climate framing.
    The BOONUS documents are framed around coastal waters, climate impacts, marine heat
    waves, HABs and hypoxia. Rudnick 2016 places gliders' sweet spot at "connecting the
    coastal and open ocean". Which framing leads: BOONUS as the U.S. node of BOON, or a
    coastal climate-observing network that happens to use boundary-current lines? This
    governs what "define the network" means in practice (which lines, where).
>A. The latter -- coastal climate-observing network that happens to use boundary-current lines.

14. **Relationship to IOOS.** The IOOS report documents an existing U.S. glider network:
    365-day glider runs across the four West Coast Regional Associations and Alaska,
    40+ hurricane-glider missions per season in the Gulf, Caribbean, Southeast and
    Mid-Atlantic, and IOOS recommendation #2 is to "recapitalize and modernize ...
    profiling gliders". The multi-pager never names IOOS. Is BOONUS (a) an expansion of
    IOOS's glider component, (b) an independent, non-federally funded network that
    feeds IOOS and the Glider DAC, or (c) deliberately positioned apart from IOOS? The
    multi-pager's "substantial capital investment from a non-federal source [too
    strong?]" bears directly on this.
>A. Ideally, BOONUS would be a part of IOOS.  But that is not likely feasible with the current administration.  So let's go with (c) deliberately positioned apart from IOOS.

15. **Relationship to BOON.** The multi-pager says "[comment on current status]". Is
    BOON still active (boon.pdf is a March 2018 revision)? Is BOONUS formally BOON's
    U.S. regional network, with Rudnick as the link?
>A. To my knowledge, it is not active

16. **Tone guardrail.** Rudnick 2016 concludes that "none of these attempts at
    establishing a sustained national or international glider observational program
    have been successful" and blames an "excess of hype". The one-pager's "The Wow" and
    "The Irrefutable Case" are pitch language. Should the brief carry a style rule that
    Claude-written documents lead with demonstrated results (CUGN's 20-year record) and
    quantify claims, and should it explicitly tag which claims in the current drafts
    are demonstrated versus aspirational? Recommendation: yes to both; the review's own
    caveat is the strongest argument for sobriety.
>A. Yes to both

17. **Bracketed notes in the multi-pager.** "[is there any mitigation??]" on hypoxia,
    "[comment on current status]" on BOON, "[too strong?]" on non-federal capital.
    Carry these into the brief as an open-questions list, or do you have answers now?
>A. Let's ignore these for now

### D. People, audiences, stakeholders

18. **Team roster.** One-pager glider team: Prochaska, Rudnick, Takeshita, Cusak, Todd,
    Ren. Modeling team: Matzloff, Edwards, Carroll, Cornuelle, Menemelis. Three spellings
    look off (Cusack? Mazloff? Menemenlis?). Please give full names, institutions and
    roles, and say whether the list is confirmed or aspirational. The multi-pager
    instead names institutions (Hawaii, Alaska, Washington, Oregon, California). Record
    both lists?
>A. This is largely TBD.  So, keep it to JXP and Dan Rudnick (SIO) for now

19. **Audiences.** Who is Sam Forde, and what was the Simons Foundation ask? Should the
    brief hold a short audience profile for each document already written, and a list
    of intended future audiences (NOAA and IOOS, NSF, private philanthropy, Congress,
    industry)? Recommendation: yes; the documents this repository produces will be
    audience-specific.
>A. Don't worry about those.  We'll worry about funding strategies later

20. **Public repository caution.** The remote is public (Sea-Meets-the-Stars/BOONUS).
    The one-pager and multi-pager name people, a funder and a recipient. Are you
    comfortable with those PDFs, and a brief that names them, being public? If not,
    options are to gitignore `context/` or keep names in a private file.
>A. I am not going to add those files to the Repo.  They will remain private.  You do
    not need to name folks in your context file other than me and Dan Rudnick.

### E. Sources and repository hygiene

21. **Keep the PDFs in git?** 11 MB total, and the Rudnick review is an Annual Reviews
    copyrighted article. Recommendation: keep boon.pdf and the two BOONUS documents
    (small, yours), keep the IOOS report (public), and replace Rudnick 2016 with a
    citation plus digest, or gitignore it.
>A. None of those docs go into GitHub

22. **What else belongs in the context set?** Candidates: the CUGN project page
    (spraydata.ucsd.edu), Rudnick et al. 2017 on the CUGN, the IOOS Glider DAC, U.S.
    EEZ boundaries, NOAA GOMO, the OceanGliders and UG2 pages, and the `cugn` repository's
    own documentation. Should I fetch and digest any of these (WebFetch domains are
    restricted in `.claude/settings.json`), or will you supply them?
>A.  Add:
    - Rudnick et al. 2017
    - Info from the `cugn` repo

23. **Document versions.** The multi-pager is v0.4 dated 2026-04-22. Is it the latest?
    Should the brief keep a version table for the BOONUS documents?
>A. Don't worry about versioning this.  But you can and should version the context doc itself.

24. **CUGN evidence numbers.** Rudnick 2016 quotes, as of 2015: more than 80,000
    profiles, 8,700 glider-days, 182,000 km, and 57 times as many profiles as CalCOFI
    stations on line 90. Should I compute current totals from the `cugn` repository
    data as a script and include them in the brief as the demonstrated-results anchor?
>A. No, it is fine to use the 2016 numbers for now

### Round 2 (2026-09-21)

Your round-1 answers are all reflected below. Between rounds I surveyed the `cugn`
repository and its sibling `cugn-climatology` (which already has a `context/` folder
with a Claude-written reference doc, the closest house exemplar for this brief). One
file request: **please download Rudnick, Zaba, Todd & Davis (2017), "A climatology of
the California Current System from a network of underwater gliders," Prog. Oceanogr.
154, 64-106, doi:10.1016/j.pocean.2017.03.002, into `context/` as `rudnick2017.pdf`.**
It is not on this machine (the path the cugn-climatology context cites does not exist
here). Nothing else needs downloading; the `cugn` information is on disk.

### F. Follow-ups to round 1

25. **Canonical-only, but where do the disagreements go?** You chose (a): the brief
    states one value. I recommend the per-source digests still carry a one-line note
    where a source differs from canonical ("multi-pager says 100 active / 200 total;
    canonical is 100+ / 50+ in water"), so a future session does not re-raise the
    question. OK?
>A. Ok

26. **Propagate "for the United States".** `README.md`, `CLAUDE.md` and `setup.py`
    currently say "of". Shall I change all three when I write the brief (prompt #3),
    or leave repository files alone and only use "for" in the brief? Recommendation:
    propagate.

>A. Yes, change all of those to "for".

27. **IOOS wording, given CUGN reality.** You chose "deliberately positioned apart from
    IOOS". But CUGN's real-time data flow through the IOOS Glider DAC today
    (`cugn/erddap.py` reads both the SprayData and DAC ERDDAP servers), NOAA funds
    CUGN, and the IOOS report counts the West Coast glider lines as IOOS-supported.
    How should the brief phrase it? (a) "BOONUS is organized and funded independently
    of IOOS; its data will be open and delivered to the IOOS Glider DAC and GTS like
    CUGN's are today." (b) Say nothing about IOOS. (c) An explicit contrast with IOOS.
    Recommendation (a): it is true of CUGN now and is the sober version of "apart".
>A. (a)

28. **Funding line.** You said to ignore the bracketed notes, but the brief needs one
    sentence on funding for framing. Proposed: "Funding model: TBD. Working assumption
    is non-federal capital for construction; federal partnership for data products."
    OK, or omit funding entirely?
>A. Yes, that's ok

29. **BOON status sentence.** Proposed: "BOON (2018) is dormant to our knowledge. BOONUS
    takes its name and lineage from BOON but is not a formal BOON node." OK?
>A. Yes, that's ok

30. **Should the brief define lines or regions?** The multi-pager map has roughly 40
    flags. Options: (a) no geography beyond "the U.S. EEZ, ~500 km offshore"; (b) a
    region list with the map's implied coverage (Gulf of Alaska and Aleutians, Hawaii,
    West Coast including the four CUGN lines, Gulf of Mexico, Florida and the Southeast,
    Mid-Atlantic and Northeast, Puerto Rico); (c) digitize the flag positions into a
    table. Recommendation (b). Note that 40 lines with 50+ gliders in the water is
    about 1.2 gliders per line, which is the CUGN ratio, so the numbers are
    self-consistent.
>A. We will not define regions today.  It will be a sampling of the EEZ informed by ocean models.

31. **CUGN scaling anchor.** The "scale from CUGN" argument needs CUGN's own fleet
    numbers, which are not in any source here: gliders owned, gliders in the water
    at once, lines occupied, people. The one-pager says Scripps has ~40 gliders. Can
    you supply these (or ask Dan), or should the brief say "CUGN: 4 lines, ~1 glider
    per line in the water" and leave the rest TBD?
>A. CUGN has 4 standard lines and one along-shore.  They need 10 gliders minimum to keep that
program active.

### G. CUGN facts from the `cugn` repository

32. **Northern line label.** `cugn/defs.py` calls it `56.0`; the climatology product and
    Rudnick 2017's continuation call it `56.7`; boon.pdf (2018) says the "fourth line
    off northern California has been occupied for two years". Canonical label? And is
    the alongshore line (`al`, ~220 km, Point Conception to the Channel Islands, in
    the short-term climatology) part of CUGN as the brief describes it (5 lines), or
    not (4 lines)?

>A. Ok, 56.7

33. **Which CUGN facts go in the brief.** Proposed, all derivable from `cugn`,
    `cugn-climatology/context`, Rudnick 2016 and Rudnick 2017: line endpoints and
    lengths (90.0: 530 km; 80.0: 365 km; 66.7: 400 km; 56: 300 km); occupied since
    2005-2007 (lines 66.7, 80.0, 90.0), later for 56 and `al`; Spray gliders; 500 m
    dives, ~3 h and ~3 km per cycle; Sea-Bird 41CP CTD, ADCP, fluorometer, dissolved
    oxygen (standard since ~2017); ~100-day missions with 4-6 sections each; data via
    SprayData ERDDAP (delayed mode, 10 m bins) and the IOOS Glider DAC (real time);
    products: the climatology (Rudnick 2017; 2026 beta) and the Southern California
    Temperature Index El Nino page. Confirm or trim. Do you know when line 56 and
    `al` began? The climatology data start in 2020 and 2019 respectively, which is
    availability, not necessarily first occupation.
>A. Yes, all of those are good.

34. **Local data pointers.** CUGN NetCDF files for all four lines exist at `$OS_SPRAY/CUGN`
    (3 GB), plus `$OS_CCS` indices. Should the brief name these environment variables
    and paths so future BOONUS sessions can compute from them, or stay
    machine-independent and cite only the ERDDAP servers? Recommendation: both.
>A. Both is good.

35. **The El Nino 2026 report as exemplar.** `cugn/reports/El_Nino_2026` is a live
    CUGN-based monthly product with a full report, a public newsletter, a one-pager
    for UCSC leadership, `sources.md` + `sources.bib`, and "Generated by JXP and
    Claude" docstrings. It is exactly the "actionable data product" the BOONUS pitch
    promises. Should the brief cite it as the existing exemplar and adopt its
    conventions (sources files, figure directories, docstring tag) for BOONUS
    deliverables? Recommendation: yes.
>A. Yes

36. **Reuse the cugn-climatology digests.** `cugn-climatology/context/context_cugn_2026beta.md`
    already digests Rudnick 2017 (its section 13) and the climatology product. May I
    reuse that material with attribution rather than re-derive it, and should those
    two context files be listed as sources in the brief? Recommendation: yes to both;
    I will still read the Rudnick 2017 PDF once you download it, to check the digest.
>A. Sure, reuse.

### H. Structure and versioning of the brief

37. **Proposed outline for `initial_context_for_claude.md` v0.1.**
    0. Header: version, date, how to use this file.
    1. Canonical fact sheet (name, one-sentence definition, fleet, footprint,
       sampling, sensors, platform, horizon, people: JXP and Dan Rudnick).
    2. Motivation and framing (coastal climate signal; anomalous events; basic
       research; model assimilation), every claim tagged (see Q39).
    3. CUGN, the proven core (Section G facts and the Rudnick 2016 numbers).
    4. Landscape: IOOS, BOON, UG2, Argo, OceanSITES, and how BOONUS relates.
    5. Models: ROMS, ECCO, Darwin, the AI-driven component (nominal lead Mazloff).
    6. Style rules for Claude-written BOONUS documents.
    7. Open decisions (sensors, platform, roster, funding, lines).
    8. Sources and digest index.
    9. Glossary.
    10. Change log.
    Approve, reorder, or cut?
>A. Approve

38. **Versioning scheme.** Header line `Version 0.1, 2026-09-21, JXP and Claude` and a
    `## Change log` table at the end, one row per revision. OK?
>A. Good

39. **Claim tags.** `[demonstrated]` (published or in the CUGN record), `[planned]` (a
    design decision you have made, e.g. 500 m dives), `[aspirational]` (pitch
    language), `[TBD]` (undecided). OK, or fewer categories?
>A. Ok

40. **Length.** With canonical-only values and no names beyond you and Dan, I expect
    about 4 pages for the brief. Fine, or do you want a 1-page fact sheet with
    everything else in the digests?
>A. 4 pages is good; this is mainly for Claude whenever I start a new Code session.

41. **gitignore.** Nothing in `.gitignore` excludes PDFs, so `git add context/` would
    stage them. Shall I add `context/*.pdf` to `.gitignore` in prompt #3 so the brief
    and digests are tracked and the PDFs never are? Recommendation: yes.
>A. Yes

42. **Digests of the private documents.** The digests will be public if committed.
    Recommendation: write public digests only for the published documents (boon.pdf,
    IOOS 2021, Rudnick 2016, Rudnick 2017) and fold the one-pager and multi-pager
    content directly into the brief with no separate digest. OK?
>A. Yes

### I. Terminology

43. **The AI-driven component, in one sentence.** So the brief does not invent it:
    is it (a) adaptive piloting and fleet control, (b) machine-learned emulators or
    surrogates inside the assimilation, (c) anomaly and event detection on the data
    stream, or some combination?
>A. some combination

44. **Glossary must-haves.** Proposed: BOONUS, CUGN, BOON, UG2, IOOS, RA (Regional
    Association), DAC, GTS, EEZ, ROMS, ECCO, Darwin, MHW, HAB, CalCOFI, SCTI, ONI,
    CUTI/BEUTI, TEOS-10, QARTOD. Add or remove?
>A. Those look good

### Round 3 (2026-09-21)

Round 2 is fully answered and I have acted on the two answers that authorized
repository edits (Q26, Q41; see the log). Everything else in rounds 1-2 is now a fixed
decision to encode in the brief. This round is short, and I expect it to be the last
before writing. **Reminder: `context/rudnick2017.pdf` has not been downloaded yet**; the
gitignore will keep it out of GitHub once it is there.

### J. Design principles that round 2 introduced

45. **Model-informed sampling of the EEZ.** Your Q30 answer replaces the map's flags with
    a principle: line locations are not fixed today and will be chosen by sampling the
    EEZ as informed by ocean models. Proposed wording, tagged `[planned]`: "Line
    locations are TBD. They will be selected by observing-system design experiments
    with the regional models, starting from the CUGN lines; the multi-pager map is
    illustrative, not a plan." Is "observing-system design experiments" the right
    term, and is the CUGN-as-starting-point clause correct?
>A. Correct

46. **The CUGN scaling ratio.** You said CUGN needs 10 gliders minimum to keep 4 standard
    lines plus the alongshore line active. Is that 10 the total inventory (in the water
    plus in refurbishment), or 10 in the water? At 2 gliders per line total, 100+
    gliders supports about 50 line-equivalents; at 2 in the water per line, 50+ in
    the water supports about 25. The brief should state the arithmetic once, and I
    want the right basis.
>A. At least 2 gliders per line.  We would also have an extra pool for target of opportunity gliders.

47. **Cost.** No source gives a cost, and funding is deferred. Should the brief carry
    one line, "Cost model: TBD; the one-pager anticipates an economy of scale relative
    to CUGN `[aspirational]`", or omit cost entirely? Recommendation: the one line, so a
    future session does not invent a number.
>A. The one line is good.

### K. Tagging and the private sources

48. **One `[demonstrated]` tag or two?** Some claims are demonstrated by CUGN (El Nino
    2009-10, the Blob, El Nino 2015-16, the 20-year record), others by other programs
    (IOOS hurricane gliders improving intensity forecasts; Oregon glider hypoxia
    records). Recommendation: one tag, with the citation making the source clear, so
    the vocabulary stays at four tags. OK?
>A. Ok

49. **Quoting the private documents.** The brief folds in the one-pager and
    multi-pager content, and the brief will be public. I plan to paraphrase their
    substance, not quote their pitch headings ("The Wow", "The Irrefutable Case"), and
    not mention the recipients or the foundation. Confirm?
>A. Yes

### L. Files around the brief

50. **Point `CLAUDE.md` at the brief.** So every new Code session loads it, add one line
    under Repository layout: "`context/initial_context_for_claude.md` is the canonical
    project brief; read it before writing anything about BOONUS." Do this when the
    brief is written (prompt #4)? Recommendation: yes.
>A. Yes

51. **A `context/README.md`.** Short file saying which contents are tracked (the brief,
    `sources/*.md`) and which are private and gitignored (the PDFs), with the citation
    for each PDF so a fresh clone knows what to obtain. Recommendation: yes, written
    with the brief.
>A. Yes

52. **Digest template.** For each of the four published sources
    (`context/sources/boon2018.md`, `ioos2021.md`, `rudnick2016.md`, `rudnick2017.md`):
    citation and local filename; one-paragraph "what it is"; key facts with page
    references; quotable lines; a "differs from canonical" note where relevant (Q25);
    and a "relevance to BOONUS" paragraph. Approve, or add a field?
>A. Approve

53. **Sequencing for prompt #4.** I propose to write, in one prompt: the brief (v0.1),
    the four digests (Rudnick 2017 only if its PDF is present), `context/README.md`,
    and the one-line `CLAUDE.md` pointer, then log. If you would rather review the
    digests before the brief, say so and I will split it.
>A. Ok

### Round 4 (2026-09-21): checks on the written brief

The brief is written (`context/initial_context_for_claude.md` v0.1). Four small points
where I made a call you may want to reverse; none blocks use of the brief.

54. **Matt Mazloff is named** as nominal lead of the AI-driven component (Q11, and the
    approved outline in Q37), despite the "JXP and Dan only" rule from Q18/Q20. The
    style rules say so explicitly. Keep, or drop the name?
>A.

55. **Your affiliation and role** are given as "J. Xavier Prochaska (JXP, UC Santa Cruz
    Ocean Sciences), lead". Correct wording?
>A.

56. **Line 56.7 "since ~2016"** is inferred from boon.pdf (March 2018: "occupied for
    two years"); the alongshore line has no start date, only "data in the climatology
    from 2019". Corrections welcome.
>A.

57. **The coverage-gap estimate (<10%)** is recorded untagged as a "project estimate
    (JXP); not derived in this repository". If you would rather it carry a tag or a
    sentence of justification, say which.
>A.

## Logs

### 2026-09-21 (Execute context prompt #1: read the five context documents, pose Q&A)

Read `context_prompts.md`, then all five items in `## Context`. Wrote the 24 questions
above, grouped by theme (purpose of the brief; canonical facts the sources disagree on;
framing; people and audiences; sources and hygiene). Did **not** create
`context/initial_context_for_claude.md`, per the prompt; that waits on your answers.
Model: Claude Fable 5.1, as requested.

**How the documents were read.** `pdftotext` (poppler) is installed and handles all five
cleanly; extractions went to the session scratchpad, not the repository. The Rudnick
review needs its per-page "Downloaded from / For personal use only" watermark lines
stripped. The multi-pager's two figures (site map, Spray photo) were rendered with
`pdftoppm` and inspected; the one-pager and boon.pdf have no images.

**What each document is (one line each, for the future digests):**

- `boon.pdf` (4 pp., revised 26 March 2018): the OceanGliders Boundary Ocean Observing
  Network white paper, Rudnick first author, 32 international members. Boundary-*current*
  framing; catalogues sustained glider lines worldwide (CUGN, OOI Oregon/Washington,
  Solomon Sea, Med, Norwegian Atlantic Current, Gulf Stream, Ellett, OSNAP, EAC) and
  proposed ones (Line P, AZMP, Kuroshio, Agulhas, Florida Current, Canaries). Positions
  BOON as complement to Argo and OceanSITES; data to GTS and a central DAC.
- `IOOS_CoastalClimateSignal_Final.pdf` (14 pp., July 2021, IOOS Association): coastal
  climate signal report; 11 Regional Associations; case studies including the West Coast
  glider network and "The Blob" (Dungeness crab closure >$100M), hurricane gliders (40+
  missions/season), Gulf of Maine warming. Five recommendations; #2 names profiling
  gliders for recapitalization. Rudnick and Clarissa Anderson acknowledged.
- `rudnick-2016-...pdf` (Annu. Rev. Mar. Sci. 8:519-541): the glider review, organized
  by scale. Key reusable facts: glider speeds (0.1 m/s vertical, ~1 km/h horizontal),
  1000 m dive = ~6 h and ~6 km, missions 1-6 months, ~3000 km and ~500 dives per
  4-month mission; depth-average velocity to 0.01 m/s; CUGN totals as of 2015; gliders
  are the dominant in situ source where Argo is sparse (coastal). Sober conclusion
  about hype and the failure of prior national glider-program attempts.
- `BOONUS_one_pager.pdf` (2 pp., "for Sam"): funder pitch. Sections "The Wow", "The
  Irrefutable Case", "Unique". Names the glider and modeling teams; ECCO + ROMS + Darwin
  + AI; ~100 gliders, 50+ in water; hurricanes, atmospheric rivers, HABs, El Nino.
- `BOONUS_multi_pager.pdf` (6 pp., v0.4, JXP, 2026-04-22, shared with Simons): the
  fuller case. What/Why/Why now/Who/Stakeholders/Challenges structure; ~100 active
  (200+ total) gliders, ~500 km offshore, 500-1000 m; sensor list; "<10% of coastal
  waters sampled"; BOON and UG2 as stakeholders; NOAA; three bracketed author notes
  still open.

**Discrepancies found across the sources (each is a question above):** "of" vs "for"
in the name; 50+ vs ~100 gliders in the water; 500 km vs the 370 km EEZ; sensor list
present in only one document and inconsistent within it (nitrate); IOOS never named in
either BOONUS document despite being the existing U.S. glider network; BOON's
boundary-current framing vs BOONUS's coastal-impacts framing; three probable misspelled
surnames in the one-pager; "ROMs" vs "ROMS".

**What I learned about the repository:**

- `context/` is untracked and holds only the five PDFs (11 MB). Nothing in `.gitignore`
  excludes PDFs, so a plain `git add context/` would commit a copyrighted Annual
  Reviews article to a public remote. Raised as Q21.
- The branch for this work is `context`, matching the house pattern of one branch per
  prompt doc (`start_up` for `start_up.md`).
- The one-pager and multi-pager are the first project artefacts that name external
  people and funders; nothing in `CLAUDE.md` yet says how such material should be
  handled in a public repository. Raised as Q20.
- The scope statement in `CLAUDE.md` ("define and promote") maps onto a real tension in
  the sources: BOON defines a network by boundary currents, the BOONUS drafts by coastal
  climate impacts. Whichever answer Q13 gets should probably be echoed into `CLAUDE.md`'s
  Project Overview.
- `conda run -n ocean14 python -` does not read a heredoc from stdin; scripts must be
  written to a file first. Plain `cat` heredocs work.

No git commands that change repository state were run (`git status` only). No files
were created or modified other than this prompt doc.

### 2026-09-21 (Execute context prompt #2: read round-1 answers, survey `cugn`, pose round 2)

Read your 24 answers, then surveyed the `cugn` and `cugn-climatology` repositories
because Q22 asked for `cugn` information in the brief. Wrote round 2 (Q25-Q44) above,
in five groups: follow-ups forced by round-1 answers, CUGN facts, brief structure and
versioning, terminology. One download requested: Rudnick et al. 2017 into `context/`.
Did not create the brief. Model: Claude Fable 5.1.

**Decisions now fixed by round 1 (to be encoded in the brief):** "for the United
States", always BOONUS; 100+ gliders, 50+ in the water; EEZ and beyond, ~500 km
offshore; 500 m dives; multi-pager sensor list as placeholder; Spray default, platform
TBD; the <10% claim stands as stated; ROMS terminology, AI component is critical with
Matt Mazloff as nominal lead; over 10 years; coastal climate-observing network that
uses boundary-current lines; positioned apart from IOOS; BOON dormant; tone guardrail
and claim tagging: yes; bracketed notes ignored; people named: JXP and Dan Rudnick
only; audiences and funding deferred; PDFs never enter GitHub; add Rudnick 2017 and
`cugn` info; version the brief itself; 2016 CUGN numbers are fine.

**What the `cugn` survey found (inputs to Q32-Q36):**

- `cugn/defs.py` lines are `56.0, 66.7, 80.0, 90.0`; `cugn/utils.py` has endpoints;
  the climatology product uses `56`/`56.7` and adds an alongshore line `al`. Label
  conflict raised as Q32.
- `cugn/erddap.py` documents the two data paths: SprayData ERDDAP (delayed mode,
  10 m bins, per mission) and the IOOS Glider DAC ERDDAP (real time, QARTOD flags).
  This is why the IOOS relationship needed a second question (Q27).
- `cugn/indices.py` and `cugn/oisst.py` already fetch ONI, SCTI, CUTI/BEUTI, CO-OPS
  sea level and OISST; `cugn/climatology.py` implements the Rudnick 2017
  decomposition. `cugn/piloting.py` holds survey-pattern simulators (relevant to the
  AI-driven piloting reading of Q43).
- `cugn/reports/El_Nino_2026/` is a complete monthly product: report, public
  newsletter, one-pager, `sources.md`/`sources.bib`, figure scripts, and an rclone
  push to the AIOcean Google Drive. Proposed as the exemplar for BOONUS deliverables
  (Q35).
- `cugn-climatology/context/context_cugn_2026beta.md` (25 KB) is the house pattern
  for a Claude context doc: purpose statement, source table, numbered sections,
  canonical-parameter tables, gotchas, and a reference digest (its section 13 covers
  Rudnick 2017). Its `initial_exploration.md` and `file_inventory.csv` sit beside it.
  Proposed outline in Q37 follows that pattern.
- Local data: `$OS_SPRAY=/home/xavier/Oceanography/data/Spray/` holds `CUGN/` with the
  four line NetCDFs and derived grids (3 GB); `$OS_CCS` holds indices. The
  climatology NetCDFs and the Rudnick 2017 PDF referenced by cugn-climatology are
  **not** on this machine (that context was written on the laptop).

**What I learned about the repository:**

- The house pattern for "context" is already established in `cugn-climatology`:
  `context/` holds Claude-written reference docs plus small CSV inventories and
  figures, and later prompt docs (e.g. `cugn/claude_prompts/super_el_nino_prompts.md`)
  point at those files by path. `context/initial_context_for_claude.md` should be
  written to be pointed at the same way.
- BOONUS's `context/` differs from the pattern in one way: it holds source PDFs that
  must stay private. Hence Q41 (gitignore) and Q42 (public digests only for published
  sources).
- Two of the four line-label conventions in the CUGN ecosystem disagree (`56.0` vs
  `56.7`); any BOONUS code that touches CUGN lines will need the mapping that
  `cugn/erddap.py` already provides (`LINE_LONG`).

No git commands that change repository state were run (`git status`, `git log` on
`cugn` read-only). Only this prompt doc was modified.

### 2026-09-21 (Execute context prompt #3: act on round-2 answers, pose round 3)

Read your answers to Q25-Q44. Two of them authorized repository edits, which I made;
the rest are decisions that the brief will encode. Wrote round 3 (Q45-Q53), nine
questions, which I expect to be the last round. Did not write the brief or the
digests. Model: Claude Fable 5.1.

**Edits made:**

- **Q26, "for the United States":** changed the network name in `README.md` (title
  line), `CLAUDE.md` (Project Overview), `setup.py` (`description`), and
  `boonus/__init__.py` (module docstring). Left `README.md` line 5 alone: its "coastal
  observations of the United States" is grammar, not the name. Left the three
  occurrences in `claude_prompts/start_up.md` alone: they are the historical log of an
  earlier decision and rewriting them would falsify the record. Tests still pass
  (`conda run -n ocean14 python -m pytest -q`, 2 passed).
- **Q41, gitignore:** appended a `context/*.pdf` rule with a two-line comment.
  Verified with `git check-ignore` that all five PDFs are now ignored and that
  `git status --ignored` reports `context/` as ignored-only, so `git add context/`
  is safe once the brief exists.

**Decisions fixed by round 2 (added to the round-1 list):** discrepancies noted in
digests only; IOOS wording (a): independent organization and funding, open data to the
Glider DAC and GTS; funding line as proposed; BOON dormant, lineage only; no regions
or lines today, sampling of the EEZ informed by ocean models; CUGN = 4 standard lines
plus one alongshore, 10 gliders minimum; northern line is 56.7; the proposed CUGN fact
list, local paths plus ERDDAP servers, El Nino 2026 report as exemplar, reuse of the
cugn-climatology digests; outline, versioning, four claim tags, ~4 pages; public
digests for published sources only; AI component is "some combination" of piloting,
learned assimilation components, and event detection; glossary as proposed.

**What I learned about the repository:**

- Renaming touched four files, not the three I predicted in Q26: the package
  docstring in `boonus/__init__.py` also carried the name. Grep before promising a
  file list.
- `.gitignore` is the 218-line GitHub Python template plus local additions at the
  end; project-specific rules go at the bottom with a comment, which is where the
  new rule sits (line 222).
- The Rudnick 2017 PDF requested in round 2 is still absent from `context/`.

No git commands that change repository state were run (`git status`,
`git check-ignore` only). Files modified: this prompt doc, `README.md`, `CLAUDE.md`,
`setup.py`, `boonus/__init__.py`, `.gitignore`.

### 2026-09-21 (Execute context prompt #4: act on round-3 answers, write the context file)

Read your answers to Q45-Q53 (all approvals or clarifications; no reversals), then
wrote the full context set in one pass as agreed in Q53. Model: Claude Fable 5.1.

**Files created:**

- `context/initial_context_for_claude.md` (v0.1, ~2800 words, about four pages): the
  canonical brief in the ten-section outline approved in Q37. Section 1 is a fact
  table with one value per item; Sections 2-5 carry the four claim tags; Section 6
  holds ten style rules; Section 7 lists open decisions; Section 10 is the change log.
- `context/sources/boon2018.md`, `ioos2021.md`, `rudnick2016.md`, `rudnick2017.md`:
  public digests in the Q52 template (citation and local file; what it is; key facts
  with page references; quotable lines; differs from canonical; relevance to BOONUS).
  The Rudnick 2017 digest was written from the PDF you downloaded (45 MB, 43 pp.) and
  cross-checked against section 13 of the cugn-climatology context doc, which it
  credits and points to.
- `context/README.md`: what is tracked and what is private, with a citation and
  "how to obtain" for each PDF.

**File modified:** `CLAUDE.md`, one new bullet under Repository layout pointing at the
brief and the digests (Q50). Also this prompt doc (Round 4 and this log).

**Calls made while writing, flagged in Round 4:** Mazloff named as nominal AI lead;
JXP's affiliation and role wording; the inferred 2016 start of line 56.7; the untagged
coverage-gap estimate. Two other choices worth knowing: canonical facts in Section 1
are untagged by design (tags are for claims, not settled values), and the brief
attributes the "97% of 3 glider-days/day since 2009" and "two gliders per line" facts
to Rudnick et al. 2017 rather than to your Q31/Q46 answers, which they corroborate.

**What I learned about the repository and sources:**

- Rudnick et al. (2017) contains, almost verbatim, the BOONUS thesis: "A series of
  networks like the CUGN in boundary currents around the world is a conceivable future
  for gliders in global ocean observing" (p. 104). It is the citation to lead with.
- The same paper states the two-gliders-per-line operating model and the
  glider-days/day metric, which makes the fleet arithmetic in the brief a published
  ratio rather than a project assumption.
- The Rudnick 2017 PDF as downloaded is 45 MB and 43 pages, mostly figures;
  `pdftotext` handles it but figure axis labels flood the text, so digests should be
  written from the prose sections (2, 3, 5, 6) and the figure captions.
- `context/` now mixes tracked Markdown with ignored PDFs; `git status --ignored`
  is the way to see both. `git add context/` stages only the Markdown.
- The brief's Section 3 data-access block duplicates paths documented in
  `cugn/CLAUDE.md` and `cugn/erddap.py`; if those move, the brief needs a version bump.

No git commands that change repository state were run (`git status`,
`git check-ignore` only). The five PDFs remain untracked and ignored.

### 2026-09-22 (Execute data assimilation prompt #1: pose Q&A for the DA/AI report)

Re-read this prompt doc, the brief (`context/initial_context_for_claude.md` v0.1),
`context/README.md` and the digests, then wrote Round 1 of the data assimilation Q&A
(DA1-DA19) under `## Q&A / ### Data assimilation`, nested with `####` headings so the
earlier context rounds stay intact. Model: Claude Opus 5.5 (the prompt did not ask for
Fable). No report or outline yet, per the prompt.

**Question groups:** purpose and audience (DA1-3); scope: global vs coastal, physics vs
BGC, reanalysis vs forecast, time window, NWP as leading indicator (DA4-8); the AI
emphasis: a four-way taxonomy by where ML enters the DA pipeline, maturity tags, the
"AI trained on reanalyses needs independent in situ data" thesis, glider-specific DA,
mapping onto the brief's three AI strands (DA9-13); sources, literature access and
naming rules (DA14-17); process (DA18-19).

**What I learned about the repository:**

- The brief already carries the facts this report must honor: ROMS assimilation of CUGN
  is `[demonstrated]` (Todd et al. 2011b; Rudnick 2016 sec. 7), IOOS hurricane-glider
  data are assimilated into NOAA intensity forecasts (IOOS 2021 digest), and the AI
  component is `[planned; scope TBD]`.
- `.claude/settings.json` allows WebFetch only for `doi.org`, `tandfonline.com`,
  `opg.optica.org` and `aslopubs.onlinelibrary.wiley.com`, and no WebSearch. A
  2019-2026 AI-DA literature review will be blocked without more domains (DA14).
- Style rule 5 (name only JXP, Rudnick, Mazloff) conflicts with a literature review's
  citations; DA16 proposes the resolution.
- There is no `reports/` directory yet; DA3 proposes `reports/data_assimilation/`.

No git commands that change repository state were run.

### 2026-09-22 (Execute data assimilation prompt #2: read round-1 answers, pose round 2)

Read `CLAUDE.md`, the brief (v0.1) and all nineteen round-1 answers (DA1-DA19), then
wrote Round 2 (DA20-DA32) under `## Q&A / ### Data assimilation`, inserted directly
after Round 1 and before the older `### First` context Q&A, which is untouched. Round 2
opens by restating the round-1 decisions as fixed and asks thirteen questions in five
groups: access and files (the exact domain list for `settings.json` and the anchor-PDF
folder with its gitignore rule, both offered as edits I make on authorization); process
and shape (outline first or draft directly, location and filenames, level of
mathematics, register and analogies); figures and citations (matplotlib vs Mermaid,
whether any figure uses CUGN data, citation volume, style and DOI verification); depth
on specific ocean, NWP-AI and ocean-ML systems, all framed as candidates to verify; and
apparatus (glossary, a "questions for Matt" appendix, a separate prompt doc for the DA
effort). Did not start the report, outline or reading list. Model: Claude Fable 5.1,
as requested.

**Facts checked before asking (so the questions are grounded, not assumed):**

- `.claude/settings.json` is unchanged since round 1: WebFetch for four domains, no
  WebSearch, and it matches the IOPtics upstream line for line, so DA14(a) has not
  been acted on. DA20 lists the proposed additions explicitly.
- `git check-ignore -v context/da/x.pdf` returns nothing: the rule `context/*.pdf`
  (`.gitignore` line 222) does not cover a subfolder. DA21 proposes `context/**/*.pdf`.
- Neither `reports/` nor `context/da/` exists.
- The El Nino 2026 exemplar (`cugn/reports/El_Nino_2026/`) records its conventions in
  `sources.md`: DOI verified by `curl -sI https://doi.org/<doi>`, access dates, BibTeX
  keys shared with `sources.bib`, a `check_links.py` script, and a note that several
  publisher hosts return 403 to automated fetchers. DA27 adopts these for the report.

**What I learned about the repository:**

- This session runs on macOS with the repository at `/Users/xavier/Projects/BOONUS` and
  the sibling repositories at `/Users/xavier/Oceanography/python/{cugn,
  cugn-climatology, IOPtics}`. `CLAUDE.md` and the brief give `/home/xavier/...` paths
  (the Linux machine). Both machines are in use; paths in the brief's Section 3
  data-access block and in `CLAUDE.md` are machine-specific and may need a
  per-machine note. Not changed here.
- On this machine `context/` holds only the tracked Markdown (README, brief, four
  digests); none of the six private PDFs is present. The gitignore worked as intended,
  and any PDF work for the report will need the PDFs fetched here.
- `pdftotext` is available at `/opt/homebrew/bin/pdftotext`; conda is
  `/Users/xavier/miniforge3/bin/conda`.
- Two of the round-1 answers ("(a) plus (c)" in DA14, "use Fable" in DA19) were
  approvals in principle that left the concrete step undecided; the prompt-doc pattern
  handles this well by carrying the follow-through into the next round rather than
  guessing.

No git commands that change repository state were run (`git status`, `git branch`,
`git check-ignore` only). Only this prompt doc was modified.

### 2026-09-22 (Execute data assimilation prompt #3: act on round-2 answers)

Read `CLAUDE.md`, the brief (v0.1), `context/README.md` and all thirteen round-2
answers (DA20-DA32). Every answer accepted the recommendation, so this prompt was
follow-through rather than discussion. Model: Claude Fable 5.1, as requested.

**Edits made by the parent session before this work (recorded here, not redone):**

- **DA20, `.claude/settings.json`:** `WebSearch` and `WebFetch(domain:...)` added for the
  full DA20 domain list (preprint servers and Crossref, publishers, ML venues,
  operational centers). BOONUS only; IOPtics untouched. Settings changes do not reach a
  running session, so all fetching below used `curl` via Bash.
- **DA21, `.gitignore`:** rule changed from `context/*.pdf` to `context/**/*.pdf`;
  `git check-ignore` confirmed `context/da/x.pdf` and `context/boon.pdf` are ignored.
  Empty `context/da/` created.

**Done in this session:**

- **Citations verified, nothing guessed.** Each anchor was resolved through the Crossref
  API (`api.crossref.org/works`) and the arXiv API (`export.arxiv.org/api/query`, https;
  the http endpoint returns an empty body), then `curl -sI https://doi.org/<doi>` was
  run for every DOI (all HTTP 302 on 2026-09-22). Full author lists were taken from
  Crossref.
- **PDFs fetched into `context/da/` (seven), each checked with `file` and `pdfinfo`:**
  `moore2019.pdf` (Frontiers, publisher PDF, CC BY; a 6-page Mini Review, which is the
  real length, not a truncated download); `carrassi2018.pdf` (arXiv 1709.02798v3; Wiley
  returned 403); `cheng2023.pdf` (arXiv 2303.10462v1; IEEE returned an empty 202);
  `dheeshjith2025.pdf` (Samudra, arXiv 2412.03795v4; AGU returned 403 despite CC BY);
  `wang2024.pdf` (XiHe, arXiv 2402.02995v4, preprint only, no journal version found);
  `cui2025.pdf` (WenHai, *Nat. Commun.* 16, 2268, publisher PDF, CC BY-NC-ND);
  `elaouni2025.pdf` (GLONET, arXiv 2412.05454v3; AGU returned 403 despite CC BY). Five
  HTML landing pages and one empty file returned by the 403/202 hosts were deleted.
- **User to download (one):** Geer (2021), *Phil. Trans. R. Soc. A* 379, 20200089,
  doi:10.1098/rsta.2020.0089. Europe PMC reports it not open access; the Royal Society
  host returned 403; no arXiv or ECMWF-elibrary copy was found. Save as
  `context/da/geer2021.pdf`. Requested in Round 3.
- **`context/da/README.md`** (tracked): table of the eight papers with verified
  citation, DOI or arXiv ID, access status and present/user-to-download status,
  mirroring `context/README.md`; notes the `context/**/*.pdf` rule and that arXiv copies
  may differ from the published versions. Also records Samudra 2 (arXiv 2606.02610,
  May 2026) as a reading-list candidate found in passing.
- **`claude_prompts/data_assimilation_prompts.md`** (DA32): new prompt doc with Goals,
  Context (brief, `context/da/README.md`, and a pointer to the DA Q&A history here, which
  is not moved), a "Decisions carried over" section summarizing DA1-DA32 compactly, an
  empty `### Outline and reading list` prompt heading for JXP to fill, and empty Q&A and
  Logs sections. No prompt text of JXP's was copied or moved.
- **Round 3** added above as a one-paragraph note: no further questions; the Geer
  download request; next step is the outline plus reading list from the new prompt doc.
  Nothing was started on the outline, reading list or report.

**What I learned about the repository and the sources:**

- Crossref and the arXiv API are reliable and fast from this machine; publisher PDF
  hosts (Wiley/AGU, Royal Society, IEEE) block `curl` even for CC BY articles, while
  Frontiers, Nature and arXiv serve PDFs directly. For the report, plan on arXiv copies
  for AGU/Wiley papers and record the published DOI alongside.
- Europe PMC's REST API (`ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:...`)
  gives a quick, citable open-access status for any DOI; useful for `check_sources.py`.
- Moore et al. (2019) is a 6-page OceanObs'19 Mini Review, not a full review; the
  outline should treat it as a systems overview and lean on Carrassi et al. (2018,
  79 pp. on arXiv) and Cheng et al. (2023) for method depth.
- `context/da/` now holds ~75 MB of PDFs, all ignored (`git check-ignore -v` points at
  `.gitignore:222`); `git status` shows only `context/da/README.md` as new content
  there, as intended.
- The repository now has two prompt docs for two efforts plus this one; the pattern of
  a "Decisions carried over" block in a new prompt doc is how history can be left in
  place without forcing a reread.

No git commands that change repository state were run (`git status`, `git check-ignore`
only). Files created: `context/da/README.md`, `claude_prompts/data_assimilation_prompts.md`,
seven PDFs in `context/da/` (ignored). Files modified: this prompt doc. Not touched:
`.claude/settings.json`, `.gitignore`, `CLAUDE.md`, the brief.

### 2026-09-22 (Execute data assimilation prompt #4: write the report prompts)

Read `CLAUDE.md`, the brief (v0.1), `context/da/README.md`, the DA Q&A rounds 1-3 and
the three DA log entries above, the new prompt doc's "Decisions carried over" block, the
El Nino 2026 exemplar (`sources.md`, `sources.bib`, `scripts/check_links.py`, report
header), and the house prompt style in `start_up.md` and this file. Then wrote nine
numbered prompts under `## Prompts` in `claude_prompts/data_assimilation_prompts.md`,
replacing the placeholder comment, and logged them there in detail. Model: Claude Fable
5.1, as requested. Nothing was started on the outline, reading list or report.

**The sequence, one line each:** (1) read the eight anchor PDFs, write `outline.md` and
the annotated 40-60 item `reading_list.md`, questions in Q&A, JXP review gate; (2) act on
the review, set up `sources.md`/`sources.bib`/`scripts/check_sources.py`, fetch further
open-access PDFs; (3) start `da_ai_review.md`: primer, classical methods, global and
regional systems, the operational-systems table; (4) NWP section, ocean AI by the
four-way taxonomy with maturity tags and verification notes, BGC; (5) glider-specific DA,
glossary, questions for Matt, executive summary; (6) the four figures (two Mermaid, the
matplotlib timeline in `ocean14`, the table); (7) verification pass and `v0.1` for JXP's
review; (8) revise to `v0.2`, the copy shared with Matt Mazloff; (9) digest in
`context/sources/` and brief v0.2 pointer (DA18). Each ends "Use Fable if you can. Log
your work." No Q&A was added: nothing blocked writing the prompts.

**What I learned about the repository.** All eight anchor PDFs are present in
`context/da/` on this machine (Geer 2021 included, downloaded by JXP after Round 3), so
the outline session can start reading at once. The exemplar's link checker verifies
Markdown links only, not DOIs; the DA report needs a new `check_sources.py`. The pattern
of a new prompt doc carrying a "Decisions carried over" block let every prompt refer to
the decisions by name instead of repeating them, which kept the prompts at JXP's length.

No git commands were run. Files modified: this prompt doc (this log entry only) and
`claude_prompts/data_assimilation_prompts.md`.
