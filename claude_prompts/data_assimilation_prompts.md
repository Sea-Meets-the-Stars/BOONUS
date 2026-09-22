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

2. Read this file.  I have reviewed `outline.md` and `reading_list.md` (my edits are
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

3. Read this file.  Start `reports/data_assimilation/da_ai_review.md` with the version
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

4. Read this file.  Continue `da_ai_review.md` with the second third:

   - the NWP section (about 2 pages), one paragraph per family, two or three exemplars
     each;
   - the ocean AI sections, one per taxonomy category, every approach carrying its
     maturity tag and its verification note, with the trained-on-reanalysis circularity
     stated once and referred back to;
   - the BGC section (physics-BGC coupling, what is assimilated, where ML is being tried).

   Same citation rule as prompt 3.  Add a change-log row.  Use Fable if you can.  Log
   your work.

5. Read this file.  Finish the draft of `da_ai_review.md`:

   - the glider-specific DA section;
   - the glossary;
   - the "questions for Matt" appendix;
   - the one-page executive summary at the top, written last.

   Same citation rule.  Add a change-log row.  Use Fable if you can.  Log your work.

### Figures

6. Read this file.  Make the figures and place them in the report with captions:

   - (1) Mermaid: the four ML entry points laid over one DA cycle.
   - (2) `scripts/make_timeline.py` (matplotlib, `conda run -n ocean14`), writing
     `figs/ai_da_timeline.png`: 2018-2026 milestones on an NWP track and an ocean track,
     every milestone dated from a reference in `sources.bib`, the list of milestones
     kept in the script so it can be edited.
   - (3) Mermaid: one assimilation cycle marking where glider profiles and depth-average
     velocity enter and where representativeness error arises.
   - (4) Confirm the operational-systems table from prompt 3 is complete and referenced.

   Docstrings carry "Generated by JXP and Claude".  Add a change-log row.  Use Fable if
   you can.  Log your work.

### Verification and delivery

7. Read this file.  Verification pass on `da_ai_review.md`, then stamp it `v0.1` for my
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

8. Read this file.  I have reviewed v0.1; my comments are in Q&A and inline in the
   report as `[JXP: ...]`.  Act on them, remove the inline comments, rerun
   `check_sources.py`, and stamp `v0.2` with a change-log row.  This is the version I
   will share with Matt Mazloff.  Use Fable if you can.  Log your work.

### Follow-through

9. Read this file.  Write the digest `context/sources/da_ai_review.md` in the template
   of the other digests (what it is, key facts, quotable lines, relevance to BOONUS),
   short enough that a future session need not open the report.  Then update the brief
   `context/initial_context_for_claude.md` to v0.2: header, a pointer in Section 5 to
   the report and the digest, the row in Section 8, and a change-log row.  Update
   `context/README.md` if it lists the digests.  Use Fable if you can.  Log your work.

## Q&A

## Logs

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
