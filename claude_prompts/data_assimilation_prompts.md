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
  dated log entries for DA prompts #1-#4. That text stays where it is; do not move it.
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

Execute one numbered prompt per session, in order. Every prompt assumes the Context
files and the Decisions above have been read; the decisions are fixed and are not to be
reopened without asking in Q&A. Paths below are relative to the repository root.

### Outline and reading list

1. Read this file.  Read the eight PDFs in `context/da/` (see its README).  Then create
   `reports/data_assimilation/` and write two files for my review:

   - `outline.md`: the section list of the report with a target page count per section
     (summing to 10-15), the figures and tables placed where they land, and one or two
     sentences per section on what it will argue and which references carry it.
   - `reading_list.md`: 40-60 candidate references.  For each give the BibTeX key you
     will use, the citation, the DOI or arXiv ID, which section it serves, a one-line
     reason, and a status (`verified` = `curl -sI https://doi.org/<doi>` returned a
     redirect today; `preprint`; `grey`; `unverified`).  For every AI paper also give its
     taxonomy category (1-4) and, where you can tell from what you have read, the
     maturity tag and the verification note.  Mark the ones you consider optional so I
     know where to strike.

   Do not write the report.  Put any questions for me in Q&A.  Use Fable if you can.
   Log your work.

2. Read this file.  See my answers to questions DA33-DA39 and act accordingly. 
   Ask another round if needed.  Use Fable if you can.  Log your work.

3. Read this file.  I have reviewed `outline.md` and `reading_list.md` (my edits are
   inline, my answers are in Q&A).  Read those and act accordingly.  Then set up the
   citation apparatus in `reports/data_assimilation/`:

   - `sources.md` and `sources.bib` in the El Nino 2026 form, one entry per approved
     reference, shared keys, DOI verified and access date recorded, `preprint` and
     `grey` flagged.
   - `scripts/check_sources.py`: re-verifies every DOI and URL in `sources.bib` and
     reports the ones that fail or return 403; add the Europe PMC open-access check if
     it is cheap.  Run it in `ocean14` and record the result.
   - Fetch the open-access PDFs you still want in hand into `context/da/` (they are
     gitignored) and add them to `context/da/README.md`.  List in Q&A the paywalled ones
     you want me to download.

   Do not write the report.  Use Fable if you can.  Log your work.

### Draft

4. Read this file.  Start `reports/data_assimilation/da_ai_review.md` with the version
   header (`v0.1 draft`, date, JXP and Claude), a change-log table, a placeholder for
   the executive summary, and the full section skeleton from `outline.md`.  Then draft
   the first third:

   - the boxed primer, marked skippable for DA specialists, with the notation table;
   - classical methods in brief (OI, 3D/4D-Var, EnKF, hybrids);
   - the global systems, with the reanalysis/state-estimation vs operational-forecast
     split made explicit;
   - the regional and coastal systems: a paragraph for each system that assimilates or
     has assimilated gliders in U.S. waters, and the table of operational systems for
     the rest (this is figure 4).

   Cite only keys that exist in `sources.bib`; if you need a new reference, add it to
   `sources.md` and `sources.bib` with verification before you cite it.  Use Fable if
   you can.  Log your work.

5. Read this file.  Continue `da_ai_review.md` with the second third:

   - the NWP section (about 2 pages), one paragraph per family, two or three exemplars
     each;
   - the ocean AI sections, one per taxonomy category, every approach carrying its
     maturity tag and its verification note, with the trained-on-reanalysis circularity
     stated once and referred back to;
   - the BGC section (physics-BGC coupling, what is assimilated, where ML is being tried).

   Same citation rule as prompt 4.  Add a change-log row.  Use Fable if you can.  Log
   your work.

6. Read this file.  Finish the draft of `da_ai_review.md`:

   - the glider-specific DA section;
   - the glossary;
   - the "questions for Matt" appendix;
   - the one-page executive summary at the top, written last.

   Same citation rule.  Add a change-log row.  Use Fable if you can.  Log your work.

### Figures

7. Read this file.  Make the figures and place them in the report with captions:

   - (1) Mermaid: the four ML entry points laid over one DA cycle.
   - (2) `scripts/make_timeline.py` (matplotlib, `conda run -n ocean14`), writing
     `figs/ai_da_timeline.png`: 2018-2026 milestones on an NWP track and an ocean track,
     every milestone dated from a reference in `sources.bib`, the list of milestones
     kept in the script so it can be edited.
   - (3) Mermaid: one assimilation cycle marking where glider profiles and depth-average
     velocity enter and where representativeness error arises.
   - (4) Confirm the operational-systems table from prompt 4 is complete and referenced.

   Docstrings carry "Generated by JXP and Claude".  Add a change-log row.  Use Fable if
   you can.  Log your work.

### Verification and delivery

8. Read this file.  Verification pass on `da_ai_review.md`, then stamp it `v0.1` for my
   review:

   - run `scripts/check_sources.py`; fix or flag every failure;
   - every in-text citation has a key in `sources.bib` and every key is cited at least
     once; every `preprint` and `grey` item is flagged in the text as well as the
     bibliography;
   - every AI approach has a maturity tag and a verification note; every system in the
     table has a source;
   - length is 10-15 pages: estimate it with a short script in `scripts/` and trim or
     expand;
   - the style rules in Section 6 of the brief hold (no hype, quantified claims,
     terminology, ROMS usage), and Section 5 of the brief is not contradicted;
   - the change log has the v0.1 row.

   List in Q&A what you could not verify and the choices you want me to check.  Do not
   share anything.  Use Fable if you can.  Log your work.

9. Read this file.  I have reviewed v0.1; my comments are in Q&A and inline in the
   report as `[JXP: ...]`.  Act on them, remove the inline comments, rerun
   `check_sources.py`, and stamp `v0.2` with a change-log row.  This is the version I
   will share with Matt Mazloff.  Use Fable if you can.  Log your work.

### Follow-through

10. Read this file.  Write the digest `context/sources/da_ai_review.md` in the template
   of the other digests (what it is, key facts, quotable lines, relevance to BOONUS),
   short enough that a future session need not open the report.  Then update the brief
   `context/initial_context_for_claude.md` to v0.2: header, a pointer in Section 5 to
   the report and the digest, the row in Section 8, and a change-log row.  Update
   `context/README.md` if it lists the digests.  Use Fable if you can.  Log your work.

## Q&A

### Outline and reading list (prompt #1, 2026-09-22)

Numbering continues from DA32 in `context_prompts.md`. Answer inline with `>A.` lines;
edits to `outline.md` and `reading_list.md` themselves can be made inline in those
files. Where I have a recommendation I state it.

DA33. **Sixty entries, eleven optional.** `reading_list.md` holds exactly 60 candidates
      (51 `verified`, 4 `preprint`, 5 `grey`), with 11 marked optional and a "Not
      included" paragraph listing 31 more whose DOIs I confirmed but left out to stay at
      60. Two structural choices to confirm: (a) the Moore et al. (2011) ROMS 4D-Var
      trilogy is one entry (Part I) with Parts II and III named inside it; make it
      three entries? (b) Bluelink and the Copernicus regional systems are covered by
      one intercomparison paper (`martin2015status`) rather than a system paper each
      (Oke et al. 2008 and Sotillo et al. 2015 are in "Not included"). Recommendation:
      Part I only; the intercomparison paper for the comparator rows.
>A. Use your Recommendation

DA34. **Preprint-only items.** XiHe (`wang2024xihe`) exists only on arXiv (no journal
      version in Crossref on 2026-09-22), and AIFS and GraphDOP are ECMWF preprints.
      They are flagged `preprint` as decided. One check I could not close from the
      text I read: XiHe's data section gives GLORYS12 for 1993-2020 as the training
      set and evaluates on Jan 2019-Dec 2020; whether those two years were withheld is
      not stated where I looked. Recommendation: keep all three; the report states the
      XiHe overlap as "not stated" unless the PDF settles it in prompt #2.
>A. Use your Recommendation

DA35. **No peer-reviewed description of JEDI/SOCA.** The U.S. next-generation marine DA
      (planned first operational use in GFSv17/GEFSv13; used in the HAFS glider study,
      `liu2023impact`) is documented only in the GitHub repository, the JEDI docs and
      workshop slides, so it enters as `grey` (`soca2026jcsda`). Do you or Matt know a
      citable system paper? If not, the table row cites the repository and Liu et al.
      (2023).
>A.  I am unaware of a citable system paper for JEDI/SOCA.

DA36. **Two category calls and one exclusion.** (a) FuXi-DA (learned assimilation of
      satellite radiances into an ML forecast model) is placed in category 3 (ML
      replacing DA) rather than 2; (b) CANYON-B (neural estimation of nutrients and
      carbonate variables from T, S, O2) is placed in category 4 (around DA) and in the
      BGC section; (c) learned sub-grid parameterizations (Zanna and Bolton 2020, Sane
      et al. 2023) were left out because they change the model, not the assimilation,
      though DA30 named them for the "ML inside DA" strand. Recommendation: keep (a)
      and (b); for (c), add one learned-parameterization paper back to Section 7.2 as
      a one-sentence boundary case if you want the DA30 list honoured literally.
>A. Use your Recommendation

DA37. **Depth of reading and PDFs to fetch in prompt #2.** The eight anchors were read
      in full; the other 52 entries were checked against Crossref or arXiv metadata,
      and the AI papers' maturity tags and verification notes come from abstracts only
      (marked "abstract only"; "?" where the abstract is silent, and two entries,
      FuXi-DA and CANYON-B, have no abstract in Crossref). Before drafting Sections 6-7
      I would fetch the open-access PDFs of the 19 non-anchor AI entries into
      `context/da/` (Nature-family, Frontiers, Copernicus, AGU via arXiv where the AGU
      host returns 403) with `curl`, as prompt #2 provides. Recommendation: approve
      that fetch list as written in prompt #2; list any paywalled ones for you to
      download.
>A.  Use your Recommendation; I approve

DA38. **Length budget.** `outline.md` plans 14.0 pages at about 500 words per page,
      references excluded: executive summary 1, primer 1, classical 0.75, global 1.25,
      regional and coastal 2, NWP 2, ocean AI 2.5, BGC 1, gliders 1.25, glossary 0.5,
      questions for Matt 0.5, introduction 0.25. That leaves one page of slack under
      the 15-page ceiling. Do you want a leaner 12-page target instead (I would take
      0.5 from each of the NWP and ocean-AI sections and 0.25 from each of the
      regional, glider and primer sections)?
>A.  It is ok if the report is longer.  Use your judgement and emphasize clarity over brevity

DA39. **Mazloff's work in the list.** Included: Todd et al. (2011, the Scripps
      California Current state estimate with CUGN), Zaba et al. (2018, state estimate
      vs CUGN), Verdy and Mazloff (2017, B-SOSE). Nothing on ECCO-adjacent ML surrogates
      from his group turned up in Crossref under the terms I tried. If Matt has a
      preferred reference for the California Current state estimate or for ML work, it
      belongs in Sections 5, 7.1 or 8; otherwise the list stands.
>A. This is fine

### Citation apparatus (prompt #2, 2026-09-22)

DA33-DA39 were acted on as answered (details in the log). Numbering continues.

DA40. **PDFs for you to download into `context/da/`** (gitignored). Everything else on
      the DA37 list is in hand: 18 of the 20 non-anchor AI papers were fetched as
      publisher or repository PDFs, checked with `file` and by title, and are listed in
      `context/da/README.md`. Still wanted:
      (a) `bonavita2020machine`, Bonavita and Laloyaux (2020), *JAMES* 12, e2020MS002232,
      doi:10.1029/2020MS002232. Open access at AGU, but the host returns 403 to scripted
      fetches and no repository copy exists (Unpaywall, Semantic Scholar, arXiv checked).
      Needed: it is the Section 6 learned-DA exemplar and the pattern Section 7.2 looks
      for in the ocean, and its maturity tag and verification note still rest on the
      abstract.
      (b) `zanna2020data`, Zanna and Bolton (2020), *GRL* 47, e2020GL088376,
      doi:10.1029/2020GL088376. Not open access. Needed only if you keep the DA36c
      boundary case (one sentence in 7.2; abstract suffices if you would rather not).
      (c) Lower priority: the published *JAMES* PDF of `fablet2021learning`
      (doi:10.1029/2021MS002572); the copy in hand is the 2020 arXiv v1 under the title
      "End-to-end learning for variational data assimilation models and solvers" with
      the same authors and the Lorenz-63/96 experiments, so the published version may
      differ in detail. The *Science* version of `lam2023learning` is not needed; the
      arXiv v2 in hand is the fuller document (102 pp.). Save as `bonavita2020.pdf`,
      `zanna2020.pdf`, `fablet2021_james.pdf`.
>A. I have downloaded the PDFs.

DA41. **Prompt numbering.** Your edit inserted a new prompt 2 ("See my answers to
      DA33-DA39 and act accordingly") and renumbered the citation-apparatus prompt to 3,
      but the Draft section still starts at 3, so the file now has two prompts numbered
      3. This session executed the new 2 and the citation-apparatus 3 together, since
      the DA answers left nothing to do that was not part of setting up the apparatus.
      Recommendation: renumber Draft 3-5 to 4-6, Figures 6 to 7, Verification 7-8 to
      8-9, Follow-through 9 to 10 (and the cross-references "prompt 3" in prompts 4 and
      6, "prompt #5", "prompt #7" in `outline.md`). I did not touch the prompt text.
>A. I have renumbered the prompts.

DA42. **Sixty-one entries.** DA36c asked for one learned-parameterization paper as a
      boundary case if the DA30 list was to be honoured literally; "use your
      recommendation" was read as yes, and Zanna and Bolton (2020) was added as entry
      61 (`zanna2020data`, optional, Section 7.2, one sentence). `sources.bib` therefore
      has 61 keys: 52 `verified`, 4 `preprint`, 5 `grey`, 12 optional. Strike it if you
      meant no; nothing else depends on it.
>A. That's fine

DA43. **FuXi-DA's training period is stated inconsistently.** The Results section of Xu
      et al. (2025) says data "from June 2022 to June 2024 are used to train", which
      overlaps the stated test period (August-December 2023); the Methods section gives
      training June 2022-May 2023, validation June-July 2023, test August-December 2023.
      Its skill is measured against ERA5 only. Recommendation: the report uses the
      Methods split and notes the discrepancy in one clause, and tags FuXi-DA "realistic
      hindcast, offline and non-cycled, verified against ERA5".
>A. Use your recommendation

DA44. **PDFs of the non-AI entries before the draft.** Prompt 3 (Draft) writes the
      primer, classical methods and the global and regional systems from 33 non-AI
      entries that were checked against Crossref metadata and abstracts only (the
      anchors excepted). Several are open access and fetchable the same way (Zuo 2019,
      Lellouche 2018 and 2021, Forget 2015, Kim 2024, Fennel 2019, Ford 2021, Moore
      2019 in hand); the rest are paywalled at Elsevier, AMS, Annual Reviews and T&F
      (Moore 2011, Neveu 2016, Levin 2020, Zaba 2018, Oke 2008, Shulman 2009, Dong
      2017, Liu 2023, Edwards 2015, Stammer 2016, Martin 2015, Mattern 2017, Evensen
      2003, Bannister 2017, Cummings 2013). Recommendation: the draft session fetches
      the open-access ones with `fetch_pdfs.py` as it needs them and writes the rest
      from abstracts and from what the anchors and reviews say about them, flagging any
      claim that rests on an abstract; you download a paywalled one only where I flag
      that the abstract is not enough. Alternative: name the ones you want in hand
      regardless and I add them to the list.
>A. Use your recommendation

### Citation apparatus completed (prompt #3, 2026-09-23)

DA40-DA44 were acted on as answered (details in the log): the three PDFs are checked,
listed and read; the prompt cross-references follow the new numbering; `zanna2020data`
stays (61 entries); FuXi-DA carries the Methods split and the DA43 tag; the DA44
drafting guidance is in `outline.md`. The published JAMES version of Fablet et al.
(2021) does not differ materially from the arXiv v1 (same authors, experiments and
numbers; title changed, two table cells filled, related work expanded), so nothing to
ask there. Two items need you; nothing else does.

DA45. **Bonavita and Laloyaux (2020): the verification note changed on reading the full
      text.** The abstract-only note said the ANN "reproduces weak-constraint 4D-Var
      model-error estimates, i.e. against a DA product, not independent observations".
      That describes the training target (2018 operational analysis increments at T21,
      about 900 km) but not the test: the ANN tendencies were then used inside cycled
      4D-Var at the operational IFS configuration (Cycle 47R1, TCo1279, 16 July-24 August
      2019), and those experiments are verified against observations (radiosonde, GPS-RO,
      wind, AMV and surface-pressure departures; 72 h temperature forecast RMSE against
      independent GPS-RO retrievals). Category 2 and "realistic hindcast" stand; the note
      in `sources.md` now reads "trained on a DA product, verified against observations",
      which makes it the one Section 6 exemplar whose assimilation experiments are scored
      against observations rather than a reanalysis, and `outline.md` Section 6 says so.
      The authors call the results preliminary and not ready for operations; the test is
      5-6 weeks and most differences are not significant. Recommendation: accept the
      revised note; say so if you would rather the report kept the narrower framing.
>A. Use your recommendation

DA46. **Two cross-references inside the prompt text still read "prompt 3".** Prompt 5
      ("Same citation rule as prompt 3") and prompt 7 ("Confirm the operational-systems
      table from prompt 3 is complete") point at the first Draft prompt, which is now #4.
      I did not edit the prompt text (no session has). Recommendation: change both to
      "prompt 4", or tell me to and I will.
>A. I have asked you to do it.

### Draft, first third (prompt #4, 2026-09-23)

DA45 was acted on as answered (the full-text Bonavita note stands in `sources.md`; nothing
in this session's sections cites it). The first third of `da_ai_review.md` is drafted
(details in the log). Five items need you; the first two affect what the next sessions can
write.

DA47. **The "Copernicus regional" comparator row has no source.** Martin et al. (2015),
      chosen under DA33b to carry the Bluelink and Copernicus comparator rows, covers only
      the basin-scale and global GODAE OceanView systems and defers coastal and shelf
      systems to a companion paper (Kerafalou et al. 2015) that is not in the list. Table 1
      therefore has rows for Bluelink, FOAM (Met Office) and TOPAZ (MET Norway) from Martin
      et al. and none for the Copernicus regional systems (IBI, Mediterranean, North-West
      Shelf). Options: (a) accept FOAM and TOPAZ as the European comparators (the table
      note says so); (b) add Sotillo et al. (2015, Copernicus IBI, doi:10.1080/1755876X.2015.1014663,
      listed under "Not included" in `reading_list.md`) through `build_bib.py` for one true
      Copernicus regional row. Recommendation: (a) unless you want the regional row for
      Matt's benefit.
>A. (a)

DA48. **Two papers where the abstract is not enough (DA44).** The UCSC ROMS 4D-Var paragraph
      (Section 5.1) rests on Moore et al. (2011, Part I) and Neveu et al. (2016), and neither
      has an abstract in Crossref, OpenAlex or Semantic Scholar; the Elsevier host and its
      accepted-manuscript link return 403. Their content in the draft comes from the
      reading-list annotation and from Edwards et al. (2015) and is flagged "[not read]".
      Please download them as `context/da/moore2011.pdf` and `neveu2016.pdf` (and, for
      Section 9 in prompt #6, Shulman et al. 2009 as `shulman2009.pdf`, same problem). Lower
      priority, abstracts in hand and adequate for Section 5 but thin for Section 9: Todd et
      al. (2011, Wiley 403) and Zaba et al. (2018, AMS returns an empty 202) as
      `todd2011.pdf`, `zaba2018.pdf`; Moore et al. (2018, AGU 403, optional) as
      `moore2018.pdf`. Recommendation: the first two now, the glider ones before prompt #6.

>A. I have downloaded the first 3 PDFs

DA49. **WCOFS: the CO-OPS page does not state the DA method or the observation types.** It
      says only that WCOFS "assimilates real-time observations in a three-day window ...
      once a day". The fallback named in `reading_list.md`, Kurapov et al. (2017, *Ocean
      Dyn.*), has sea-level verification as its subject (abstract checked) and would not
      fill the gap, so it was not added. The draft says "not stated" and cannot say whether
      WCOFS has assimilated glider profiles. Do you or Matt know a citable NOAA technical
      report or paper on the WCOFS DA configuration? If not, the row stays as written.
>A. We do not

DA50. **Two operational-status facts I could not establish.** (a) Whether the HAFS ocean
      component has moved from RTOFS-initialized HYCOM (Kim et al. 2024, operational June
      2023, no ocean DA inside HAFS) to MOM6 with Marine JEDI/SOCA (Liu et al. 2023, a case
      study) in the operational system; (b) SOCA's solver list (3D-Var FGAT, hybrid 3DEnVar,
      LETKF) and its GFSv17/GEFSv13 plan, recorded in `sources.md` on 2026-09-22 from the
      JEDI documentation, which I could not re-find on the documentation landing page or in
      the repository README ("JEDI encapsulation of MOM6") today. Both are flagged in the
      text and both are candidates for the questions-for-Matt list. Recommendation: leave
      flagged; ask Matt.
>A. Use your recommendation

DA51. **Length.** The drafted sections run 1,041 words for the primer (target 500), 640 for
      classical methods (375), 1,291 for global systems (625, trimmed from 1,857 in a first
      pass, because the Decisions give the global systems table rows rather than
      paragraphs), and 1,657 plus a 573-word table for regional and coastal systems
      (1,000): 11.2 pages of prose plus 1.5 pages of tables against the outline's 5.25
      pages for Sections 1-5. At this rate the full report lands near 20 pages rather than
      14. Under DA38 ("clarity over brevity") I kept the numbers and quotations that make
      the systems comparable and did not cut further. Options: (a) leave trimming to the
      prompt-8 verification pass, which will cut repetition against the 15-page guide; (b)
      tell me now to cut each system paragraph to about 120 words and move the detail into
      Table 1. Recommendation: (a). A note rather than a question: Section 1 (Introduction,
      0.25 page in the outline) was not assigned to any prompt, so I drafted it here since
      it states the flags the rest of the text uses.
>A. (a)

### Draft, second third (prompt #5, 2026-09-23)

DA47-DA51 were acted on as answered (details in the log). Sections 6, 7 (7.1-7.4) and 8 are
drafted, and Sections 3, 5.1 and Table 1 were revised from the full text of the Moore and
Neveu PDFs. Four items need you; the first affects the bibliography.

DA52. **`moore2011.pdf` is Part II, not Part I.** DA48 asked for Moore et al. (2011) Part I
      (`moore2011roms`, *Prog. Oceanogr.* 91, 34-49, the formulation paper), but the file you
      downloaded is Part II ("Performance and application to the California Current System",
      91, 50-73, doi:10.1016/j.pocean.2011.05.003). Part II is in fact the paper Section 5.1
      needs (the WC30/WC10 configurations, observations, super-observations, control-vector
      impacts, degrees of freedom and array modes), so it was added to `build_bib.py` as
      `moore2011romsII` (62 entries) and is cited in Sections 3, 5.1 and Table 1; Part I stays
      as the formulation reference, cited "[not read; via Part II]". Options: (a) keep both
      entries as they are; (b) also download Part I as `moore2011_partI.pdf` so the flag can go;
      (c) drop Part I and cite Part II alone. Recommendation: (a); (b) only if you want the
      "[not read]" count at zero before v0.1.
>A. My mistake; I have moved Part II to `moore2011b.pdf`

DA53. **No source for the near-real-time UCSC assimilation of CUGN.** The brief (Section 5)
      records ROMS 4D-Var assimilation of CUGN as `[demonstrated]`, but neither Moore et al.
      (2011, Part II) nor Neveu et al. (2016) name gliders among the assimilated platforms:
      Part II assimilates Aviso SSH, blended SST, EN3 profiles (XBT, Argo, CalCOFI/GLOBEC/LTOP
      CTD) and tagged elephant seals; the WCRA31/WCRA14 reanalyses assimilate AVISO, Pathfinder,
      AMSR-E and MODIS SST and EN3 profiles (XBT, MBT, CTD, Argo, mammals), "no velocity
      observations", and gliders are not named (the earlier "gliders included" note in
      `sources.md` was wrong and is corrected). Section 5.1 now says the near-real-time analyses
      "are not described by either paper and have no source in this list", and a candidate
      question for Matt sits under Section 11. Do you know which UCSC product or paper documents
      the CUGN assimilation (a near-real-time system paper, or a later reanalysis)? If so I add
      it through `build_bib.py` in prompt #6; if not, the brief's `[demonstrated]` tag should
      cite Todd et al. (2011) and Zaba et al. (2018) (the Scripps state estimate) rather than the
      UCSC ROMS system when the brief goes to v0.2 (prompt #10).
>A.  I am confident that Chris Edwards' ROM assimilates glider data.  And they are now working on pH as well.

DA54. **The ocean-side gaps in Section 7 are stated as gaps.** The approved list has no ocean
      counterpart of the NWP end-to-end systems (FuXi-DA, Aardvark, GraphDOP), no ML anomaly
      detection, downscaling or adaptive-sampling paper, no glider QC paper, and no ocean
      paper that learns B or the observation operator; Section 7.3 and 7.4 say so in one
      sentence each rather than citing from memory, and the two absences most relevant to Matt
      (learned B/H; learned adjoint for ROMS 4D-Var) are on the Section 11 candidate list.
      Option: name candidates for prompt #6 or #8 to verify and add (I have none I would
      vouch for without reading them). Recommendation: leave the gaps stated; revisit after
      Matt's comments.
>A.  Le's follow your recommendation

DA55. **Length.** Sections 6-8 as kept run 1,340, 1,731 and 705 words of prose (2.7, 3.5
      and 1.4 pages at 500 words per page, `check_citations.py`) against the outline's 2, 2.5
      and 1, a 1.35x overrun, mostly from the per-exemplar maturity tags, verification notes
      and the one or two numbers each that the Decisions require. The whole draft is now
      19.8 pages of prose plus 1.8 of tables against the 15-page guide, with Sections 0, 9
      and 10 still to come. (A longer version of Sections 6-8, 4,922 words, is in commit
      abfc04e; JXP chose the shorter one, see the log.) Per DA51 (a), trimming is left to
      prompt #8; if you would rather Sections 6-8 were cut now, say which exemplars can go
      (candidates: Samudra 2, GraphDOP, Hatfield 2021, Martin 2023, Zanna and Bolton, all
      marked optional in `sources.md`; each costs about 100-150 words).
>A.  If you run longer than anticipated, that is fine

### Draft completed (prompt #6, 2026-09-23)

DA52-DA55 were acted on as answered (details in the log). The draft is complete except for
the figures (prompt #7). Four items need you; none blocks prompt #7.

DA56. **DA53 has sources now; confirm the two additions.** Searching for a citable record of
      glider assimilation in Chris Edwards' system found (a) Mattern, Takeshita, Rocha and
      Edwards (2026), *Biogeosciences* 23, 2621-2639, doi:10.5194/bg-23-2621-2026 (DOI 302,
      open access, PDF fetched as `context/da/mattern2026.pdf` and read in full): the UCSC
      1/10 degree ROMS-NEMUCSC 4D-Var over 2019 assimilates CUGN and IOOS glider T/S in its
      reference configuration and then glider pH (MBARI Line 67 Spray) plus pH and
      alkalinity estimated from CUGN T, S and O2; this is also the "pH work" you mention.
      (b) The UCSC near-real-time page `https://oceanmodeling.ucsc.edu/ccsnrt/` (HTTP 200;
      its TLS chain is incomplete for some clients), which lists SCCOOS/CeNCOOS glider lines
      among the inputs of the daily 4-day-cycle analysis but carries a 2011 footer and no
      system paper; added as `grey` (`ucsc2026ccsnrt`). Both are cited in 5.1, 8 (Mattern),
      9 and Table 1, and 5.1 also records your confirmation as "pers. comm., 2026". The list
      is now 64 entries (54 verified, 4 preprint, 6 grey; 33 PDFs in hand). Recommendation:
      keep both, and when the brief goes to v0.2 (prompt #10) cite Mattern et al. (2026) for
      the `[demonstrated]` CUGN-in-ROMS tag alongside Todd et al. (2011) and Zaba et al.
      (2018); strike the grey page if you would rather not cite a web page with a 2011
      footer.
>A. Use your recommendation

DA57. **Glider operating numbers in Section 9.** The section quotes Rudnick (2016) for a
      1000 m Spray dive (about 6 h, about 6 km, 0.25 m/s), which is what the source says;
      the brief's canonical CUGN values (Section 1) are 500 m, about 3 h, about 3 km.
      Recommendation: keep Rudnick's numbers, since Section 9 describes gliders in general
      and cites its source; say so if you want the CUGN values substituted with a pointer
      to the brief.

DA58. **Length.** As drafted: executive summary 588 words (1.2 pp against the one-page
      target), Section 9 1,608 words (3.2 pp against 1.25), glossary 835 (1.7 against 0.5,
      49 terms because the report uses more undefined terms than the placeholder listed),
      questions 657 (1.3 against 0.5, thirteen questions), whole report 27.8 pp of prose plus
      2.1 pp of tables against the 15-page guide (`check_citations.py`). Per DA51/DA55,
      trimming is left to prompt #8; the executive summary is the one section I would cut
      further now if you want it at 500 words. Recommendation: leave it; tell me if the
      thirteen questions should be cut to the outline's six before Matt sees them.

DA59. **Section 9 rests on seven abstracts.** Oke and Sakov (2008), Halliwell et al. (2017),
      Levin et al. (2020), Todd et al. (2011), Zaba et al. (2018), Liu et al. (2023) and
      Moore et al. (2018) are cited "[abstract only]" (the report-wide count rose from 14 to
      21). The full texts of Shulman, Dong, Mattern and the two Moore 2011 papers carry the
      quantified claims, so nothing rests on an abstract alone that a number depends on,
      except Halliwell's OSSE ranking (altimetry, then Argo, then SST; gliders "modest").
      Recommendation: no downloads needed for v0.1; if you want Section 9 on full text for
      Matt, `halliwell2017north` (T&F, closed) and `oke2008representation` (AMS) are the two
      to fetch as `halliwell2017.pdf` and `oke2008.pdf`.

## Logs

### 2026-09-23 (Execute prompt #6: act on DA52-DA55, finish the draft)

Read `CLAUDE.md`, this prompt doc (Decisions, all Q&A through DA55, the two most recent log
entries), `da_ai_review.md` in full, `outline.md` (Sections 0, 9-11 and the drafting
guidance), `sources.md`, `sources.bib` (keys), `context/da/README.md`,
`context/sources/rudnick2016.md`, and Sections 5-6 of the brief. Model: Claude Fable 5.1,
single session, no subagents. Sources read via `pdftotext`: Moore et al. (2011) Part I in
full (new), Shulman et al. (2009) in full, Mattern et al. (2026) in full (new), the relevant
sections of Moore et al. (2011) Part II, Neveu et al. (2016), Dong et al. (2017), Moore et
al. (2019), Martin et al. (2015), Ford (2021) and Fennel et al. (2019), and the OpenAlex,
Semantic Scholar and Crossref abstracts of Halliwell 2017, Levin 2020, Todd 2011, Zaba 2018,
Oke 2008, Liu 2023 and Moore 2018. Every quotation and number written today was grep-checked
against a reading-order `pdftotext` extraction (the `-layout` extraction interleaves the two
columns and hides phrases that span a line break; the check script in the session used both).

**Step A.** DA52: `context/da/moore2011a.pdf` is Part I (page-1 title "Part I - System
overview and formulation", *Prog. Oceanogr.* 91, 34-49, 16 pp.) and `moore2011b.pdf` Part II
(91, 50-73), both `file` = PDF 1.7. `build_bib.py`: `moore2011roms` now has
`pdf='moore2011a.pdf'` and a "supports" note written from Part I; `moore2011romsII` points
at `moore2011b.pdf`. The two "[not read; via Part II]" flags on `moore2011roms` (Sections 3
and 5.1) are gone: Section 3 now states from Part I why I4D-Var is strong-constraint in
practice and why the dual schemes admit the weak constraint (observation-space dimension
independent of the constraint), the Lanczos machinery and the 4D-PSAS/R4D-Var outer-loop
difference; Section 5.1 opens with Part I's system description (TLROMS/ADROMS coverage and
exclusions, control vector, diffusion-operator covariances, balance operator, no time
correlations, the Lanczos-based diagnostics, the unfinished items). DA53: JXP's answer led to
a search (WebSearch, the UCSC site, Crossref, Semantic Scholar, OpenAlex). Found and verified:
Mattern, Takeshita, Rocha and Edwards (2026), *Biogeosciences* 23, 2621-2639,
doi:10.5194/bg-23-2621-2026 (DOI HTTP 302; Copernicus open access; fetched by
`fetch_pdfs.py`, title match 1.00; read in full), which documents CUGN and IOOS glider T/S in
the reference assimilation of the UCSC 1/10 degree ROMS 4D-Var (91 four-day cycles, 2019)
and the glider-pH assimilation JXP referred to; and the UCSC near-real-time page
(`https://oceanmodeling.ucsc.edu/ccsnrt/`, HTTP 200 via `curl -k`; WebFetch fails on its
certificate chain), which names SCCOOS/CeNCOOS and NANOOS glider lines among the inputs,
added as `grey`. Both were added through `build_bib.py` (64 entries; regenerated
`sources.md`/`sources.bib`; `check_sources.py --record`: 58 DOIs and 10 URLs, 0 failed).
Also checked and not used: the NOAA IR document noaa/61871 (Amaya et al. 2023, a reanalysis
evaluation, silent on the UCSC inputs) and the Springer chapter Moore et al. (2013,
doi:10.1007/978-3-642-35088-7_14, no abstract served). Section 5.1's "no source in this
list" paragraph was replaced by the two sources plus "J. X. Prochaska (pers. comm., 2026)";
the Table 1 California Current row and Section 8 (the one glider-BGC assimilation in the
list, with its numbers and limits) were revised to match; the Section 11 question now asks
for a citable near-real-time system paper, the treatment of glider profiles and velocity, and
the status of the pH work. DA54: gaps left stated. DA55: no trimming; nothing padded.

**Step B.** Section 9 (1,608 words, 3.2 pp): Figure 3 placeholder; what a glider delivers
(Rudnick); profile vs binned (Shulman's vertical-profile treatment and 26-degree paths, the
6 h grid-cell super-observations of Moore Part II, Mattern's one-per-cell rule and the
super-observation vs original-observation fit, Dong's 0000 UTC thinning); depth-average
velocity (every source negative or silent; no documented system assimilates it);
representativeness error (Oke and Sakov's definition and estimate, the 2011 scatter-based
and 2019 tuned R values, 0.1 C/0.01 vs 0.28 C/0.15, Dong's 0.01 C/0.02, Rudnick's 30 km
sampling limit, Moore 2019's judgement); impacts, OSEs and OSSEs (Shulman's mooring numbers
and the 1-1.5 day memory; Dong's TCHP 59/81/92/81 against 86 kJ cm-2 and the intensity
null; Liu; Halliwell's OSSE ranking; Moore Part II redundancy and array modes; Moore 2018
RAMs; Mattern's cross-validation; CASE; doppio; Ford); a closing paragraph of what the record
establishes, without the "AI makes gliders more valuable" thesis. `shulman2009impact` and
`halliwell2017north` are now cited. Section 10 (835 words, 1.7 pp): 49 terms in five groups
(estimation problem; algorithms; observations and experiments; evaluation; AI vocabulary),
the placeholder's list plus every term the report uses without defining it (primal/dual,
super-observation, array modes, balance operator, Lanczos vectors, Class 4, Desroziers,
fraternal twin, barrier layer/TCHP, threaded profile, the maturity tags, the circularity
caveat). Section 11 (657 words, 1.3 pp): thirteen numbered questions, each naming its
section, built from the placeholder, the five candidate bullets (rewritten; DA53's now
reflects the new sources) and the open points flagged in Sections 3, 5.2, 7.1, 7.2, 7.4, 8
and 9; the candidate scaffolding is removed. Section 0 (588 words, 1.2 pp; written
last): classical DA, the global and coastal systems, the NWP sequence, the four ocean
categories with maturity, the circularity caveat, BGC, gliders; quantified, no BOONUS pitch.
All "[Placeholder: prompt 5/6 ...]" text removed; Figure 1-3 placeholders kept for prompt 7.
Change-log row added.

**Citation check** (`scripts/check_citations.py`, ocean14, exit 0): 64 keys in
`sources.bib`, 64 cited, 0 missing, 0 uncited (every key is cited). Flags: [abstract only]
x21, [not read x6, [not re-verified] x2, (preprint) x5, (grey) x11. Length by section: 0:
1.2 pp, 3: 1.6, 5: 5.1 (+622 table words), 8: 1.8, 9: 3.2, 10: 1.7, 11: 1.3; total 27.8 pp
of prose plus 2.1 pp of tables (DA58).

**Choices made.** (i) Mattern et al. (2026) placed in bibliography group E (glider-specific
DA), serving 5.1, 8 and 9; the UCSC page in group D. (ii) The grey UCSC page is cited with
its 2011 footer stated in the text, and the report says the page "has no system paper"
rather than inferring one. (iii) JXP's confirmation is recorded as "(pers. comm., 2026)"
next to the two sources, not in place of them. (iv) Depth-average velocity is reported as
"documented by no system in this list" rather than "not assimilated anywhere", since the
CASE abstracts are silent (Section 11, question 1). (v) Rudnick's 1000 m dive numbers were
kept over the brief's canonical CUGN values (DA57). (vi) The executive summary was trimmed
three times (685 to 588 words) and left slightly over the 550-word target rather than lose
the numbers (DA58). (vii) The glossary is grouped, not alphabetical, so that related terms
sit together; each entry is one or two lines.

**What I learned.** Copernicus journals serve their PDFs to `curl` and the Crossref record
carries the abstract, so a Biogeosciences paper can be verified, fetched and read in one
pass; `oceanmodeling.ucsc.edu` serves an incomplete TLS chain, so WebFetch fails and `curl
-k` is needed. Two-column Elsevier PDFs need a reading-order `pdftotext` (no `-layout`) for
phrase checks; `-layout` is better for tables. Moore et al. (2011) Part I is where the
strong/weak and primal/dual reasoning lives; Part II has the configuration numbers. The
Section 9 sources agree that no published system assimilates glider depth-average velocity,
which is a stronger statement than the outline anticipated and is now a question for Matt.

Files created: `context/da/mattern2026.pdf` (gitignored). Files modified:
`reports/data_assimilation/da_ai_review.md`, `scripts/build_bib.py` (two entries added, two
edited, docstring history), `scripts/fetch_pdfs.py` (one entry), `sources.md` and
`sources.bib` (regenerated), `context/da/README.md` (count line, Part I/II rows, Mattern
table, "not in hand" list), this prompt doc (Q&A DA56-DA59, this entry). Not touched: the
prompt text above `## Q&A`, `outline.md`, `reading_list.md`, `check_sources.py`,
`check_citations.py`, the brief, `.claude/settings.json`. No git commands that change
repository state were run (`git status` only, at the start).



### 2026-09-23 (Execute prompt #5: act on DA47-DA51, draft the second third)

Model: Claude Fable 5.1 subagents, orchestrated by the main session (Claude Opus 5.5).
The work ran in three pieces, which is why this entry is written by the main session.

**Step A (DA47-DA51), by a prompt-5 subagent.** DA47: the Table 1 note says FOAM and TOPAZ
stand as the European comparators. DA48: `moore2011.pdf`, `neveu2016.pdf` and
`shulman2009.pdf` checked (`file`, page-1 title) and listed in `context/da/README.md`;
`moore2011.pdf` turned out to be Part II, so Part II was added to `build_bib.py` as
`moore2011romsII` (62 entries, 53 verified; `sources.md`/`sources.bib` regenerated;
`check_sources.py`: 57 DOIs and 9 URLs, 0 failed) and Part I kept as "[not read; via Part
II]" (DA52). Section 3 (4D-Var), Section 5.1 and the California Current row of Table 1 were
rewritten from the full text of Part II and Neveu et al. (2016), every number grep-checked;
two errors fixed on the way (WCRA31 forcing is ERA-40 2.5 deg / ERA-Interim 0.7 deg / CCMP
25 km, not "25-200 km"; WC10 degrees of freedom are 1-2%, not "as little as 2%"). The earlier
statement that the Neveu reanalysis assimilated gliders was wrong (EN3 profiles; gliders not
named; no velocity data) and is corrected, which leaves the brief's `[demonstrated]` UCSC
CUGN assimilation without a source in the list (DA53). Shulman et al. (2009), for Section 9:
NCOM/NCODA in Monterey Bay during AOSN-II 2003, each glider descent/ascent assimilated as a
vertical profile, slanted ("threaded") profiles named as future work. DA49, DA50 and DA53
became candidate bullets under the Section 11 placeholder. DA51 (a): no trimming.

**Step B (Sections 6-8).** The prompt-5 subagent drafted Sections 6-8 (4,922 words of
prose) and wrote Q&A DA52-DA55. Its hand-back reached the main session before the drafting
was visible in the file, so the main session also had three Fable subagents draft Sections
6, 7 and 8 in parallel into scratch files (every number grep-checked against `pdftotext`
output of the PDFs; the circularity caveat stated once, in the Section 7 opening, with the
explicit "stand on the shoulders of numerical GOFSs" statement attributed to WenHai (Cui et
al. 2025) only; Section 6's framing sentence edited to refer forward to it) and merged them.
That merge replaced the subagent's version, which JXP had meanwhile committed (abfc04e).
Asked which to keep, JXP chose the shorter parallel drafts (3,776 words). The committed
version stays in git history. Lesson: a subagent's completion notice is not proof it has
stopped writing; check the file and `git log` before a second pass on the same text.

**As kept.** Section 6 (NWP): framing paragraph plus emulators (Pangu-Weather, GraphCast,
GenCast, AIFS), learned components inside DA (Bonavita and Laloyaux 2020; Hatfield et al.
2021), end-to-end (Aardvark; GraphDOP), generative and learned DA (Manshausen et al. 2025;
FuXi-DA with the DA43 split), Fig. 2 placeholder; only AIFS is tagged operational. Section 7:
intro with Fig. 1 placeholder and the circularity caveat; 7.1 Samudra, Samudra 2, XiHe (split
implied, not stated, DA34), WenHai, GLONET (pre-operational), OceanNet; 7.2 Gregory et al.
2023 offline, the absence of ocean learned B/H or adjoint surrogates, Zanna and Bolton as the
one-sentence boundary case; 7.3 4DVarNet (Fablet 2021 idealized; Beauchamp 2023 OSSE) and
Martin et al. 2023 as the OSE verified against withheld CryoSat-2 and drifters; 7.4 Sugiura
and Hosoda 2020 Argo QC, CANYON-B, the missing glider-QC/anomaly/sampling literature stated as
a gap, adjoint array modes as the classical counterpart. Section 8: coupling and
initialization shock, log-space increments, what is assimilated, ROMS-NEMURO/Mattern 2017
[not read; via Fennel], B-SOSE and ECCO-Darwin [abstract only], the Ford 2021 BGC-Argo OSSE,
CANYON-B (cat. 4) and LDEO-HPD (cat. 2); the Gloege RMSE figure in `sources.md` was not used
because it is not in the extracted text (from a figure). Change-log row added.

**Citation check** (`scripts/check_citations.py`, ocean14): 62 keys, 60 cited, 0 missing,
uncited `shulman2009impact` and `halliwell2017north` (Section 9); flags [abstract only] x14,
[not read x7, [not re-verified] x2, (preprint) x5, (grey) x9. Length by section: 6: 2.68 pp,
7: 3.46 pp, 8: 1.41 pp; total 19.8 pp prose plus 1.8 pp tables. No new references beyond
`moore2011romsII`; references the drafters wanted but did not cite (not in the list): Keisler
2022, Pathak et al. 2022, Hersbach et al. 2020 (ERA5); Song et al. 2012, Yu et al. 2018,
Wood et al. 2018, Cossarini et al. 2019, Hemmings et al. 2008, Jones et al. 2016 (BGC).

Files modified: `reports/data_assimilation/da_ai_review.md`, `scripts/build_bib.py`,
`sources.md`, `sources.bib`, `context/da/README.md`, this prompt doc (Q&A DA52-DA55, this
entry). No git commands that change state were run.

### 2026-09-23 (Execute prompt #4: start `da_ai_review.md`, draft the first third)

Read `CLAUDE.md`, this prompt doc in full (Decisions fixed; Q&A through DA46, with DA45
"use your recommendation" taken as accepting the full-text Bonavita note and DA46 already
done), `context/initial_context_for_claude.md` (Sections 5 and 6 in particular),
`outline.md` including its "Drafting guidance for prompts 4-6", `sources.md`, the key list
of `sources.bib`, the global, regional and glider groups of `reading_list.md`,
`context/da/README.md`, `context/sources/rudnick2016.md`, and the El Nino 2026 exemplar
(`El_Nino_2026_09.md` header and References; `sources.md`) for conventions. Model: Claude
Fable 5.1. Sources read in full or in the relevant sections via `pdftotext`: Moore et al.
2019 (all 6 pp.), Carrassi et al. 2018 (introduction, Bayesian formulation, Kalman filter
and smoother, variational section, EnKF, square-root schemes, localization and inflation,
EnVar and hybrids, TOPAZ, Appendix D), Geer 2021 (the equivalence passages), and the ten
PDFs fetched today (below), with three read-only subagents extracting facts from Zuo 2019,
Lellouche 2018 and 2021, Forget 2015 and Kim 2024 in parallel and every number used in the
text re-checked by grep against the source before it was written.

**Files created.** `reports/data_assimilation/da_ai_review.md` (v0.1 draft header, change
log with one row, citation-convention note, executive-summary placeholder, the full
section skeleton 0-11 with 7.1-7.4, placeholders naming prompt 5 or 6 and the intended
content, References listing the cited keys in the exemplar's form). Drafted: Section 1
(Introduction and scope, 280 words; not assigned to any prompt, drafted here because it
defines the flags the text uses, DA51), Section 2 (the primer as "Box 1" set off by rules,
skippable, notation table of 13 symbols, the linear Gaussian update and gain, 3D-Var and
strong/weak/incremental 4D-Var with the gradient and adjoint, the ensemble gain with the
Carrassi sampling-error formula behind localization and the reason for inflation, hybrid B
and ECCO; the four analogies each with an "exact" statement and a "where it breaks"
clause; 1,041 words plus table), Section 3 (OI/EnOI, 3D-Var FGAT, 4D-Var, EnKF stochastic
and deterministic with TOPAZ, hybrids/EnVar, and Moore et al.'s list of unsolved problems;
640 words), Section 4 (the reanalysis/state-estimation vs operational-forecast split with
Moore 2019 and Stammer 2016, then 4.1 ORAS5, GLORYS12, ECCO v4 and 4.2 GLO12, OCEAN5-RT,
Global RTOFS, GOFS/NCODA, JEDI/SOCA; 1,291 words), Section 5 (5.1 UCSC ROMS 4D-Var, 5.2
Scripps CASE, 5.3 doppio, 5.4 NOS OFS/WCOFS, 5.5 HWRF-HYCOM, HAFS and HAFS-MOM6/SOCA, 5.6
Table 1 = Fig. 4 with 18 rows and 8 columns, every row citing a key; 1,657 words plus a
573-word table). `scripts/check_citations.py` (docstring "Generated by JXP and Claude":
lists `[@key]` citations, keys missing from `sources.bib`, keys not yet cited, the
evidential flags, and a per-section page estimate at 500 words/page with math, keys and
table rows excluded from prose and table words counted separately; `--strict` for prompt
8). Result in `ocean14`: 61 keys in `sources.bib`, 27 cited, 0 missing, 34 not yet cited
(all of them serve Sections 6-9 and are expected in prompts 5-6, except `shulman2009impact`
and `halliwell2017north`, Section 9); flags: `[abstract only]` x11, `[not read` x7,
`[not re-verified]` x2, `(preprint)` x1 (the convention note), `(grey)` x7; exit 0. Length:
5,616 prose words = 11.2 pp plus 732 table words = 1.5 pp, of which the drafted Sections
1-5 are 4,909 prose words = 9.8 pp against the outline's 5.25 (DA51). A first version of
Section 4 ran 1,857 words and was cut to 1,291 because the Decisions give the global
systems table rows, not paragraphs.

**PDFs fetched (DA44).** Ten open-access non-AI PDFs were added to the `PDFS` list of
`fetch_pdfs.py` and fetched into `context/da/` (all `file` = PDF, title match 1.00; total
now 38 files, 28 in the script's list): Zuo 2019, Lellouche 2018, Forget 2015, Ford 2021
(Copernicus), Lellouche 2021, Kim 2024, Fennel 2019 (Frontiers), and three repository
copies of publisher PDFs found through Unpaywall and OpenAlex where the publisher host
refuses `curl`: Dong 2017 (NOAA Institutional Repository noaa/17960; AMS returns an empty
HTTP 202), Bannister 2017 (CentAUR, University of Reading; Wiley 403), Martin 2015
(Figshare 22957895; T&F 403 even with browser headers and `needAccess=true`). Fennel 2019
and Ford 2021 are for prompt 5 and were not read. Listed in a new table in
`context/da/README.md` with the reasons the remaining non-AI entries are still not in hand.
Kurapov et al. (2017) was checked (Crossref, DOI 302, Springer abstract) and not added: its
subject is sea-level verification, not the WCOFS DA (DA49). No reference was added to
`build_bib.py`, so `sources.md`/`sources.bib` are unchanged and `check_sources.py` was not
rerun.

**Choices made.** (i) Citation form "Author (year) [@key]" with the bare key on repeat,
matching the exemplar's bracketed-key convention and its References paragraph that lists
the cited keys; stated in a convention note at the top. (ii) Two evidential flags beyond
the DA44 "[abstract only]": "[not read; via `key`]" for the papers with no abstract
anywhere (Moore 2011, Neveu 2016, Cummings 2013), and "[not re-verified]" for the SOCA
solver list carried over from `sources.md`. (iii) The primer is set off by horizontal
rules with a "Box 1" heading and an explicit end line, so display math renders outside a
blockquote. (iv) Analogies only with a stated exactness condition: OI = GP regression
(static B, linear H), 4D-Var = MAP with the dynamics as prior (Carrassi eq. 28-29), EnKF =
Monte Carlo Kalman filter in the linear-Gaussian N -> infinity limit (Le Gland via
Carrassi), ECCO = long-window smoother (linear-case equivalence to the Kalman smoother),
each with where it breaks. (v) Table 1 carries a "Gliders assimilated?" column with "not
named" distinguished from "no", since most systems ingest whatever profiles the GTS or
Coriolis carry; Martin et al. (2015) Table 1 is the one source that names gliders as an
assimilated platform for GOFS, FOAM, Bluelink, Mercator, CONCEPTS and ECMWF (2015
configurations). (vi) For the comparator rows, FOAM and TOPAZ stand in for "Copernicus
regional", which Martin et al. do not cover (DA47). (vii) Zaba 2018's "CASE" and Todd
2011's state estimate are described from abstracts; the MITgcm/adjoint attribution is
marked as coming from the reading-list annotation.

**Abstract-only and not-read flags placed** (for prompt 8): Stammer 2016 (Section 4
opening); Moore 2011 and Neveu 2016 (5.1, not read); Moore 2018 (5.1); Edwards 2015 (5 and
3); Todd 2011 and Zaba 2018 (5.2); Levin 2020 (5.3); Liu 2023 (4.2, 5.5, table);
Cummings 2013 (4.2, table, not read); Evensen 2003 (Box 2.4, not read, via Carrassi); SOCA
solver list (4.2, table, not re-verified).

**What I learned about the repository and the sources.** Unpaywall
(`api.unpaywall.org/v2/<doi>?email=`) and OpenAlex `locations` find repository copies of
publisher PDFs that the publishers' own hosts refuse: CentAUR for QJRMS, Figshare for T&F
open-access supplements, the NOAA IR for AMS papers by NOAA authors; Zenodo record 31969
(Stammer 2016) exists but its files return 403. Elsevier serves nothing to `curl` (403 on
landing pages, abstracts and accepted manuscripts) and its Prog. Oceanogr. and Ocean
Modelling records carry no abstract in Crossref, OpenAlex or Semantic Scholar, so the two
core ROMS 4D-Var papers cannot be characterized without JXP's copies (DA48). Springer
landing pages return a CSP stub without the abstract to `curl`. `conda run` swallows
heredocs (as logged before), so the Section 4 splice was done with a plain `python3`
heredoc. `pdftotext -layout` interleaves the two columns of the Copernicus and Frontiers
PDFs, so a quoted phrase can span two line numbers; grep on a distinctive fragment is the
reliable check. The El Nino exemplar's `[@key]` convention has no author-year in the
text; this report adds it because the audience will read the text, not the bibliography.
`git status` shows `reports/` is now staged (the earlier files are "A"), so from this
session on JXP's inline edits to the report will be visible in `git diff`.

No git commands that change repository state were run (`git status` only). Files created:
`reports/data_assimilation/da_ai_review.md`,
`reports/data_assimilation/scripts/check_citations.py`. Files modified:
`reports/data_assimilation/scripts/fetch_pdfs.py` (ten entries), `context/da/README.md`
(count line and a new table), this prompt doc (Q&A DA47-DA51 and this entry). Not
touched: the prompt text above `## Q&A`, `outline.md`, `reading_list.md`, `build_bib.py`,
`check_sources.py`, `sources.md`, `sources.bib`, the brief, `.claude/settings.json`,
`context_prompts.md`.

### 2026-09-23 (Act on DA46: fix stale cross-references in the prompt text)

At JXP's request, changed "prompt 3" to "prompt 4" in prompt 5 ("Same citation rule as
prompt 4") and prompt 7 ("Confirm the operational-systems table from prompt 4"), so both
point at the first Draft prompt after the DA41 renumbering. No other prompt text refers
to a prompt by number. The DA46 question text in Q&A was left as written. No git
commands were run.

### 2026-09-23 (Complete prompt #3: act on DA40-DA44, re-verify the citation apparatus)

Read `CLAUDE.md`, this prompt doc in full (Decisions fixed; JXP's answers DA40-DA44 and
the renumbered prompts), the 2026-09-22 log entry, `outline.md`, `reading_list.md`,
`sources.md`, `scripts/build_bib.py`, `scripts/check_sources.py`, `scripts/fetch_pdfs.py`
and `context/da/README.md`. Model: Claude Fable 5.1. The report itself was not started.
Most of prompt #3 had been built on 2026-09-22; this session did only what JXP's answers
left open and re-verified the whole list, without redoing anything that was already
correct.

**How each answer was acted on.** DA40: `context/da/bonavita2020.pdf`, `zanna2020.pdf`
and `fablet2021_james.pdf` are real PDFs (`file`: PDF 1.4) whose first pages carry the
Crossref titles and DOIs; they are listed in `context/da/README.md` in a new table (the
"wanted but not fetched" list is gone; the *Science* version of GraphCast is recorded as
not wanted). Bonavita and Laloyaux (2020) was read in full (22 pp.), the published Fablet
et al. (2021) in full (15 pp.) and compared with the arXiv v1 already in hand, Zanna and
Bolton (2020) skimmed (data and methods, offline diagnostics, online implementation,
summary), enough for its one sentence. DA41: the prompt doc now numbers Draft 4-6,
Figures 7, Verification 8-9, Follow-through 10; `outline.md` ("prompt #7" -> #8 for the
verification pass, "prompt #5" -> #6 for the executive summary, and a header note on the
numbering), `reading_list.md` and the README now say so, and the "[prompt #2: ...]"
annotations of 2026-09-22 are explained in the reading-list header as the session that
executed prompts #2 and #3 together, rather than being rewritten. Two stale
cross-references inside the prompt text itself ("prompt 3" in prompts 5 and 7) were left
for JXP (DA46). DA42: `zanna2020data` kept; still 61 entries. DA43: FuXi-DA's
maturity tag is now "realistic hindcast, offline and non-cycled, verified against ERA5"
and its verification note leads with the Methods split (training June 2022-May 2023,
validation June-July 2023, test August-December 2023) with one clause on the Results
section stating the span inconsistently, in `build_bib.py` (hence `sources.md` and
`sources.bib`), `reading_list.md` entry 42 and `outline.md` Section 6. DA44: nothing
fetched; `outline.md` gained a "Drafting guidance for prompts 4-6" section: the Draft
session adds open-access non-AI PDFs to the `PDFS` list of `fetch_pdfs.py` and fetches
them as needed, writes paywalled entries from abstracts and reviews, and flags every
claim that rests on an abstract alone; the citation rule (add to `build_bib.py`, rerun
both scripts, then cite) is restated there.

**What the three full texts changed.** `bonavita2020machine`: category 2 and "realistic
hindcast" stand, but the verification note moved from "against a DA product, not
independent observations" (abstract) to "trained on a DA product (2018 operational
analysis increments at T21; the ANN explains about 14% of the increment variance for
mass, 5% for wind, none for humidity), then used inside cycled 4D-Var at the operational
IFS configuration and verified against observations" (radiosonde, GPS-RO, wind, AMV and
surface-pressure departures; 72 h forecast RMSE against independent GPS-RO; Z500 and
MSLP against own analysis); the maturity tag now carries the cycled-experiment
qualifier and the authors' own "preliminary, not yet ready for operational use". Flagged
as DA45. `fablet2021learning`: tags unchanged (category 3, idealized Lorenz-63/96); basis
now the published text; the published version and the arXiv v1 share authors,
experiments and headline numbers (Lorenz-63 error 1.34 vs 3.55, Lorenz-96 0.38 vs
1.06); the differences are the title, two placeholder cells of Table 1 filled in, an
expanded related-work section pointing to the group's SSH work, and the code archived on
Zenodo. `zanna2020data`: tags unchanged (category 2 by placement, idealized); the note
now records the setup (idealized MITgcm double gyres at 3.75 and 7.5 km coarse-grained
to 30 km, RVM and physics-constrained CNN, 50/50 train/validation, offline correlation
about 0.6 for the temperature forcing) and the online test in a different 30 km
shallow-water model with the forcing attenuated by factors 0.5-0.7 for stability; no
observations anywhere. With these, all 24 AI entries rest on the full text.

**Rebuild and re-verification.** `build_bib.py` was given a `VERIFIED_ON` list
(2026-09-22, 2026-09-23) that the headers of both files print, a count of AI notes
resting on the full text, and the three PDF fields; it was rerun with `--no-cache` so
every bibliographic field was refetched from Crossref and the arXiv API today and every
DOI and URL resolved today: 61 entries, 56 DOIs all 302, 9 URLs all 200, no arXiv title
mismatch, no flags. Access dates: since the script really did re-resolve everything
today, `urldate` and the per-entry "HTTP 302 on 2026-09-23" were allowed to move to
today, and the `sources.md` header states both dates and that the per-entry date is the
last run; the README keeps 2026-09-22 as the date its citations were taken and adds the
re-verification. `check_sources.py --record` in `ocean14`, 2026-09-23: 56 DOIs and 9 URLs
checked, 0 failed, 0 blocked, exit 0, footer written. Europe PMC (informative only): 5
open access, 4 not open access, 47 not indexed, as yesterday, but the not-open-access
four are `edwards2015regional`, `stammer2016ocean`, `rudnick2016ocean`,
`lam2023learning`; yesterday `geer2021learning` was in that set and Edwards was not
indexed, so the Europe PMC lookup is not stable from day to day and should not be
quoted in the report. Counts checked across the four files: 61 entries; 52 `verified`,
4 `preprint`, 5 `grey`; 12 optional; 24 AI papers with taxonomy notes, 24 on the full
text; 28 PDFs in hand (8 anchors + 18 fetched + 2 downloaded; the published Fablet
replaces the arXiv copy in the "In hand" field). `sources.bib`: 51 `@article`, 1
`@incollection`, 4 `@misc`, 5 `@online`; 12 `optional`, 4 `preprint`, 5 `grey`
keywords. A small script (`count_reading_list.py`, scratchpad only, not kept) confirmed
the reading-list counts, since its "Status:" lines wrap and defeat `grep -c`.

**What I learned about the repository and the sources.** Wiley-served PDFs (the three
JXP downloaded) carry a per-page "Downloaded from ... on [23/09/2026]" banner in the
text layer, as the AGU anchors did. `build_bib.py` pads BibTeX field names to a common
width, so `grep "keywords = {"` undercounts; use `grep -E "keywords +="`. `conda run`
swallows a heredoc on stdin, so scratch scripts must be written to a file. The
`--no-cache` rebuild returned the same 61 keys with the same statuses, flags and
counts as yesterday, but a field-by-field comparison with yesterday's `sources.bib`
was not possible: `reports/` is still untracked and no copy of the previous output was
kept, so any Crossref metadata drift between the two days would not have been noticed
(none is expected for published records). That also means JXP's review reached this
session only through the prompt doc.

No git commands that change repository state were run (`git status`, `git log` and
`git diff --stat` only). Files modified: `reports/data_assimilation/scripts/build_bib.py`,
`reports/data_assimilation/sources.md` and `sources.bib` (regenerated by the script, not
edited by hand), `reports/data_assimilation/reading_list.md`,
`reports/data_assimilation/outline.md`, `context/da/README.md`, and this prompt doc (Q&A
DA45-DA46 and this entry). Not touched: the prompt text above `## Q&A`, the earlier Q&A
wording, the older log entries, the brief, `.claude/settings.json`,
`context_prompts.md`, `check_sources.py`, `fetch_pdfs.py`.

### 2026-09-22 (Execute prompt #2: act on DA33-DA39, set up the citation apparatus)

Read `CLAUDE.md`, this prompt doc in full (Decisions fixed; JXP's answers DA33-DA39),
`outline.md` and `reading_list.md` (checked for inline edits with grep and against git:
`reports/` is untracked, so there is no diff, and no `[JXP: ...]`, strike or comment
marks were found; the review is entirely in Q&A), `context/da/README.md`, Sections 5
and 6 of the brief, and the El Nino 2026 exemplar (`sources.md`, `sources.bib`,
`scripts/check_links.py`). Model: Claude Fable 5.1. The report itself was not started.
Because JXP's edit to this file left two prompts numbered 3, this session executed the
new prompt 2 (act on the answers) together with the citation-apparatus prompt that the
answers point to (DA37 approves the fetch list "as written in prompt #2"); DA41 asks
for the renumbering.

**How each answer was acted on.** DA33: Part I only for the ROMS 4D-Var trilogy (Parts
II and III named in the entry's note) and `martin2015status` for the Bluelink and
Copernicus comparator rows; no change. DA34: XiHe, AIFS and GraphDOP kept as `preprint`;
`wang2024.pdf` was reread for the training/test split: the data section gives the
GLORYS12 span as Jan 1993-Dec 2020, the abstract and conclusion say "25-year" training
data (which ends in 2017 or 2018), the evaluation is Jan 2019-Dec 2020, and the split is
never stated explicitly, so the report will say "implied, not stated" (recorded in
`outline.md` Section 7, `reading_list.md` entry 6 and `sources.md`). DA35: JEDI/SOCA
stays `grey` (`soca2026jcsda`, repository plus JEDI docs, both HTTP 200), with Liu et
al. (2023) as the citable use. DA36: FuXi-DA stays in category 3 and CANYON-B in 4;
Zanna and Bolton (2020) added as `zanna2020data`, optional, a one-sentence boundary
case in Section 7.2 (DA42 asks JXP to confirm). DA37: the open-access PDFs of the
non-anchor AI entries were fetched (below). DA38: `outline.md` keeps the 14.0-page plan
but states that the 15-page ceiling is a guide, not a limit, per "clarity over brevity".
DA39: no change.

**Files created** (under `reports/data_assimilation/` unless noted):

- `scripts/build_bib.py` (docstring "Generated by JXP and Claude"): holds the approved
  list (61 entries: key, DOI or arXiv ID or URL, group, sections, "supports" text,
  flags, and for the 24 AI papers the category, maturity tag, verification note and its
  basis), pulls every bibliographic field from the Crossref works API (articles, the
  Springer chapter) or the arXiv API (the four preprints), re-resolves every DOI with
  `curl -sI`, checks each companion arXiv ID by title overlap, fetches each grey URL
  with `curl -sI -L`, and writes `sources.bib` and `sources.md`. Nothing bibliographic
  is typed from memory; API responses are cached in the system temp directory. Run
  three times in `ocean14` (fixes between runs: Crossref HTML in three titles,
  `<scp>`/`<sub>`/`<i>`, is now stripped; the Crossref record for
  `lellouche2021copernicus` holds given and family names reversed and is swapped back
  with a note; year taken from Crossref `issued` so GenCast is 2024, matching its key;
  corporate authors braced once). Final run: 61 entries, all 56 DOIs 302, all 9 URLs
  200, no arXiv title mismatch.
- `sources.bib`: 61 records in eight topical groups, `@article` (51), `@incollection`
  (1), `@misc` for the arXiv preprints (4, with `eprint`, `archivePrefix`,
  `primaryClass`, the resolvable `10.48550/arXiv.` DOI and `keywords = {preprint}`),
  `@online` for the grey items (5, `url`, `urldate`, `keywords = {grey}`, HTTP code in
  `note`); `keywords = {optional}` on the 12 optional entries; every record carries
  `urldate = 2026-09-22`; journal articles with a preprint carry `eprint` and the arXiv
  ID in `note`.
- `sources.md`: El Nino 2026 form, header paragraph with the verification convention
  and access date, entries numbered 1-61 within the same eight groups, each with the
  full author list, DOI and HTTP code, arXiv ID, sections served, "Supports", the AI
  notes (category, maturity, verification, basis: full text or abstract only), the
  private PDF in hand, status and key; a footer section that `check_sources.py
  --record` fills.
- `scripts/check_sources.py` (docstring "Generated by JXP and Claude"): regex BibTeX
  reader, `curl -sI` on every DOI (30x passes), `curl -sI -L` on every non-doi.org URL
  (200/30x passes, 403 reported as "blocked, not broken"), Europe PMC lookup per DOI
  (informative only), summary and failure list, exit 1 on any failure, `--record` to
  write the summary into `sources.md`. Result in `ocean14`, 2026-09-22: 56 DOIs and 9
  URLs checked, 0 failed, 0 blocked, exit 0; Europe PMC indexes 5 as open access
  (Pangu-Weather, GenCast, WenHai, Aardvark, OceanNet), 4 as not open access
  (`geer2021learning`, `stammer2016ocean`, `rudnick2016ocean`, `lam2023learning`), 47
  not indexed.
- `scripts/fetch_pdfs.py` (docstring "Generated by JXP and Claude"): the fetch list
  with one URL per paper, `curl -L` download, `file` check, title match on the first
  two pages (word fraction, 0.8 threshold), deletes and reports failures. Result:
  18/18 fetched and checked, all title matches 1.00, about 250 MB into `context/da/`
  (gitignored by `context/**/*.pdf`, confirmed). Sources: Nature-family publisher PDFs
  (5: Pangu-Weather, GenCast, FuXi-DA, Aardvark, OceanNet), Frontiers (CANYON-B),
  Copernicus (4DVarNet-SSH), arXiv (GraphCast, AIFS, GraphDOP, Samudra 2, Manshausen,
  Gregory, Fablet, Sugiura), and for AGU papers whose host returns 403 the publisher
  PDF from a repository (Hatfield via Zenodo 7624565, Martin via EarthArXiv, Gloege via
  the NOAA Institutional Repository noaa/59204). Two could not be fetched:
  `bonavita2020machine` (open access but AGU-only, 403) and `zanna2020data` (closed);
  both are on JXP's list (DA40).

**Files modified.** `outline.md` (header: reviewed, ceiling relaxed per DA38; Section 7
opening: the XiHe finding; 7.2: the boundary case; checks list). `reading_list.md`
(header and counts: 61 entries, 52/4/5, 12 optional, 24 AI papers, PDFs in hand; the
convention bullet on author lists; entry 61 added; Zanna and Bolton moved out of "Not
included"; 18 entries annotated "[prompt #2: ...]" where the full text changed or
confirmed a maturity tag or verification note, and FuXi-DA and CANYON-B, which had no
abstract, filled in). `context/da/README.md` (anchors table given a key column; new
table of the 18 fetched papers with file, citation, identifiers, access, status, key;
a "wanted but not fetched" list). This prompt doc (Q&A DA40-DA44 and this entry).

**What the full texts changed.** Of the 24 AI entries, 22 now rest on the full text
(the 8 anchors read in prompt #1, 18 read here via `pdftotext`, the six per file split
across three read-only subagents whose extracts were checked against the PDFs' own
statements) and 2 on the abstract (`bonavita2020machine`, `zanna2020data`). Tags that
moved: FuXi-DA from "?" to "realistic hindcast, offline and non-cycled, verified
against ERA5 only", with an inconsistency between its Results and Methods training
periods (DA43); CANYON-B from "?" to "released mapping method validated against
independent GO-SHIP cruises" with its RMSEs; OceanNet's training target identified as a
4 km ROMS-EnKF reanalysis, verified against the same reanalysis; Samudra 2 as an
emulator of OM4 verified against OM4; GraphCast and GenCast confirmed as verified
against ERA5 or each system's own analysis with no observations; AIFS confirmed as
verified against radiosondes and SYNOP as well as analyses, and "experimental
operational mode" from October 2023; Aardvark's "end-to-end from observations" holds
at deployment but ERA5 is the pre-training target; GraphDOP verified in observation
space with ERA5 for verification only; Manshausen's held-out stations are themselves
assimilated by HRRR; Hatfield's neural adjoint ran inside a cycled 4D-Var; Sugiura's
40/60 split is random and not stated to be by float. Two file-identity findings:
`fablet2021.pdf` is the 2020 arXiv v1 under a different title (same authors, same
experiments), and `martin2023.pdf` is the published JAMES PDF deposited at EarthArXiv,
not a preprint.

**What I learned about the repository and the sources.** `reports/` is still untracked,
so `git diff` cannot show JXP's review of files under it; his edits arrived through the
prompt doc only. `ocean14` has no `bibtexparser`, so both scripts read BibTeX with a
regex, which is enough for files `build_bib.py` writes. Crossref answers `curl` from this
machine for every DOI in the list but its titles carry HTML for small caps and
subscripts and, for one Frontiers paper, reversed name fields; OpenAlex and Crossref
both omit the "Part I" subtitle of Moore et al. (2011). Nature, Frontiers, Copernicus,
arXiv, EarthArXiv, Zenodo and the NOAA repository serve PDFs to `curl`; every
Wiley/AGU host (`agupubs.onlinelibrary.wiley.com`, `onlinelibrary.wiley.com`) and the
Europe PMC PDF renderer return 403, while the Europe PMC REST API, Unpaywall
(`api.unpaywall.org/v2/<doi>?email=`) and Semantic Scholar answer and were the way to
find repository copies. Europe PMC indexes only the Nature-family, Royal Society, Annual
Reviews and Science titles in this list, so its open-access flag is informative for a
few entries only. The exemplar's convention (30x from doi.org is verified; 403 is
blocked, not broken; access date on every entry) transferred directly; the only
addition is the `--record` footer so `sources.md` carries its own last check.

No git commands that change repository state were run (`git status`, `git diff` and
`git log` only). Not touched: the brief, `.claude/settings.json`, `context_prompts.md`,
the prompt text above `## Q&A`.

### 2026-09-22 (Execute prompt #1: outline and annotated reading list)

Read `CLAUDE.md`, this prompt doc in full (Decisions block treated as fixed), the brief
(v0.1, Sections 5 and 6 in particular), `context/da/README.md`, the DA Q&A history
(DA1-DA32) in `context_prompts.md`, the El Nino 2026 exemplar (`sources.md`,
`sources.bib`, `scripts/check_links.py`) for conventions, and the eight anchor PDFs in
`context/da/` via `pdftotext -layout` (Moore et al. 2019 in full; Samudra, WenHai,
GLONET and XiHe through their methods, evaluation and discussion sections; Geer 2021
introduction and conclusion; Carrassi et al. 2018 and Cheng et al. 2023 abstracts,
section structure, the TOPAZ example, the end-to-end-DA section and conclusions). Model:
Claude Fable 5.1, as requested. The report itself was not started.

**Files created** (all under `reports/data_assimilation/`, which did not exist):

- `outline.md`: twelve sections with page targets summing to 14.0 pages (executive
  summary 1, introduction 0.25, boxed primer 1, classical methods 0.75, global systems
  1.25, regional and coastal 2, NWP 2, ocean AI by category 2.5, BGC 1, gliders 1.25,
  glossary 0.5, questions for Matt 0.5); a figure table placing Fig. 1 (Mermaid
  taxonomy) at the top of Section 7, Fig. 2 (matplotlib timeline) at the top of Section
  6, Fig. 3 (Mermaid glider cycle) at the top of Section 9 and Fig. 4 (systems table)
  across Sections 4-5; one or two sentences per section on the argument and the keys
  that carry it; a closing checklist against the Decisions block.
- `reading_list.md`: 60 candidates in eight groups (anchors and reviews 8; classical 4;
  global 8; regional and coastal 9; glider DA 5; NWP AI 11; ocean AI 8; BGC 7), each
  with key, citation, DOI or arXiv ID or URL, sections served, one-line reason, status,
  and for the 23 AI papers the taxonomy category plus maturity tag and verification
  note where the text read supports them ("?" otherwise). Status counts: 51
  `verified`, 4 `preprint`, 5 `grey`, 0 `unverified`; 11 marked optional. A "Not
  included" paragraph records 31 further DOI-confirmed candidates and 9 preprints that
  were checked and cut, so JXP can add by name.
- `scripts/verify_reading_list_dois.py` (docstring "Generated by JXP and Claude"):
  extracts every `doi:` and `doi.org/` DOI from `reading_list.md`, runs `curl -sI`
  against `https://doi.org/<doi>` and prints status and Location; exit code 1 on any
  non-30x. Run with `conda run -n ocean14 python ...`: 85 DOIs (the 60-list plus the
  "Not included" ones), all 302 after one regex fix (parentheses are legal in a DOI;
  the first run truncated `10.3319/TAO.2009.04.16.01(IWNOP)`). The output is pasted at
  the end of `reading_list.md`.
- `figs/` created empty for prompt #6.

**How the DOIs were found and checked.** Candidate DOIs were first resolved through the
Crossref works API (`api.crossref.org/works/<doi>`, title/author/year compared to the
intended paper) and, where my recollection was wrong or absent, through Crossref
bibliographic search; arXiv IDs through the arXiv API; grey URLs with `curl -sI -L`.
Four recollected DOIs were wrong and corrected from Crossref (Pangu-Weather, Dobricic et
al. 2010, Bire et al., Manshausen et al.); two preprints turned out to have journal
versions (FuXi-DA in *npj Clim. Atmos. Sci.*, Manshausen et al. in JAMES) and are
listed as `verified` with the arXiv ID alongside. No DOI was written from memory
alone. WebSearch and WebFetch were used only for the operational-center pages (ECMWF
AIFS news, RTOFS, SOCA/JEDI, HAFS); the older RTOFS site `polar.ncep.noaa.gov/global/`
returns 404 today, so the NCO products page is cited instead.

**Choices made.** (i) Sixty entries exactly, with the cut candidates listed rather than
discarded, since DA30 made the reading list the place to add or strike. (ii) One
intercomparison paper (Martin et al. 2015) covers the Bluelink and Copernicus comparator
rows instead of a system paper each. (iii) Learned parameterizations were left out as
model-side rather than DA-side (DA36c). (iv) Maturity tags and verification notes were
written only from text actually read; 19 of the 23 AI entries carry "abstract only" and
several carry "?". (v) The XiHe training/test overlap is flagged rather than asserted
either way. (vi) Page counts assume 500 words per page and exclude references; the
plan sits at 14.0 with one page of slack (DA38).

**What I learned about the repository and the sources.** `pdftotext -layout` on the
anchors gives clean two-column text for the Frontiers and Nature PDFs and readable
single-column text for the arXiv copies; the AGU and Royal Society PDFs carry per-page
download banners that grep picks up. Crossref returns abstracts for most AGU, Nature,
Copernicus and AMS papers but not for Frontiers or npj titles, which is why two entries
have no abstract-level note. The Crossref and arXiv APIs, doi.org, GitHub, ECMWF, NOAA
CO-OPS and NCO pages all answer `curl` from this machine; the exemplar's convention
(30x from doi.org = verified, access date recorded) transfers directly. WenHai and
GLONET both verify against the GODAE OceanView IV-TT Class 4 observation sets, and both
papers state in their own words that the AI systems depend on the numerical reanalysis
they were trained on, which gives the report's central caveat two primary sources.
The El Nino 2026 `sources.md` numbers entries within topical groups and states its
verification convention in a header, the form `reading_list.md` follows.

No git commands that change repository state were run (`git status` only, at the
start). Files created: `reports/data_assimilation/outline.md`,
`reports/data_assimilation/reading_list.md`,
`reports/data_assimilation/scripts/verify_reading_list_dois.py`, empty
`reports/data_assimilation/figs/`. Files modified: this prompt doc (Q&A DA33-DA39 and
this log entry). Not touched: the brief, `context/da/README.md`, `.claude/settings.json`,
`context_prompts.md`.

### 2026-09-22 (Write the report prompts, from `context_prompts.md` DA prompt #4)

Wrote the nine numbered prompts above under `## Prompts`, replacing the placeholder
comment JXP had left under `### Outline and reading list`. Driven by prompt #4 in
`claude_prompts/context_prompts.md` ("update the `data_assimilation_prompts.md` file
with a set of prompts" for the report). Model: Claude Fable 5.1, as requested. Nothing
was started on the outline, reading list or report, and no other file was changed
except the matching log entry in `context_prompts.md`.

**Shape of the sequence.** Five subheadings, one JXP review gate after prompt 1
(outline and reading list) and one after prompt 7 (v0.1): Outline and reading list
(1-2), Draft (3-5), Figures (6), Verification and delivery (7-8), Follow-through (9).
Each prompt is a single-session chunk in the house form: "Read this file.", the task,
"Use Fable if you can. Log your work." Every element of DA1-DA32 is placed in exactly
one prompt: the primer, classical methods, global/regional systems and the
reanalysis-vs-forecast split in 3; NWP families, the four-way ocean taxonomy with
maturity tags and verification notes, and BGC in 4; glider DA, glossary,
questions-for-Matt and the executive summary in 5; the four figures with their tooling
(Mermaid for the two schematics, matplotlib in `ocean14` for the timeline, a table for
the systems) in 6; `check_sources.py` and the citation rules in 2 and 7; the digest and
brief v0.2 pointer (DA18) in 9. Version labels: `v0.1 draft` while writing, `v0.1` at
the review gate, `v0.2` for the copy shared with Mazloff, so the change log records
what he saw.

**Choices made while writing them.** (i) The citation apparatus (`sources.md`,
`sources.bib`, `check_sources.py`) is set up in prompt 2, before any prose, so that
prompts 3-5 can be held to "cite only keys that exist in `sources.bib`", the rule that
keeps the review free of unverified references. (ii) The executive summary is written
last (prompt 5) but sits at the top. (iii) The timeline script keeps its milestone list
in the code so JXP can edit dates without touching the report. (iv) Prompt 8 takes
JXP's review comments both in Q&A and inline as `[JXP: ...]`, the way the brief's
drafts were reviewed. (v) No prompt was written for Mazloff's eventual comments; that
round follows the prompt-8 pattern when it comes.

**What I learned about the repository.** On this machine all eight anchor PDFs are now
in `context/da/`, including `geer2021.pdf` that JXP downloaded after Round 3, so prompt
1 can read them directly with `pdftotext`. `reports/` does not exist yet; prompt 1
creates it. The El Nino 2026 exemplar's `check_links.py` checks only the links in a
Markdown file, not DOIs, so `check_sources.py` is a new script rather than a copy;
its 403-is-not-broken convention carries over. The exemplar's `sources.md` numbers
entries within topical groups and states its verification convention in a header
paragraph, which is the form prompt 2 asks for.

No git commands were run. Files modified: this prompt doc and
`claude_prompts/context_prompts.md` (log entry only).
