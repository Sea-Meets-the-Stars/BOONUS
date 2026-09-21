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

## Q&A

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
