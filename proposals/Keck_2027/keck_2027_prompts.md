# Keck 2027 Proposal

## Goals 

Write the proposal for the 2027 Keck Foundation grant application.
First the internal one for UCSC.  Then the main, assuming we get
UCSC's approval to go forward.

## Context

The internal submission call is given as a PDF in `Projects/BOONUS/proposals/Keck_2027/UCSC_Internal_call_Keck2027.pdf`.

The BOONUS one pager is given as a PDF in `Projects/BOONUS/proposals/Keck_2027/BOONUS_OnePager.pdf`.

I have also downloaded a multi-page BOONUS description, which does not include the modeling part as `BOONUS_MultiPager.pdf`.

The Keck Proposal will focus on the modeling part of the BOONUS project.
And, they tend to fund risky ideas, so we will emphasize the bleeding edge nature of the project, i.e. the AI component which is not well developed yet.

The 'da_ai_review.md' file is a review of the DA-AI part of the BOONUS project. 
Use it as useful.

## Prompts

### Internal UCSC Proposal

1. Read all of the context docs.  Then start a discussion with me about writing
the Internal UCSC Proposal.  Put your questions and ideas in the Q&A/Internal section below.  
Use Fable if you can.  Log your work in Logs

2. Ok, good catch on Keck's exclusion list and more.  Please draft an email that I will
send to our Foundation experts at UCSC: Sam Forde and Sarah Carle (and will CC Chris Edwards).
Have it describe what you found, including the Stanford point about climate change being well-funded.  And ask for further guidance on whether we should reconsider.
Point out that I was already pushing a square peg into a round hole by writing a DA-AI proposal for Keck.  
Use Fable if you can.  Log your work in Logs

3.  That is a fine draft, but (1) reduce it's length by ~2x and (2) put it in the Email section below.  And, I am CC'ing Chris because he had agreed to be a co-PI on the proposal.
Use Fable if you can.  Log your work in Logs

4. We are still encouraged to submit a proposal for the UCSC internal competition.  
Please generate a draft in `proposals/Keck_2027/internal_proposal.md` that includes the eight fields with counts checked by a script.  Note, we are using Markdown, but the intake
form will be straight ASCII.
Use Fable if you can.  Log your work in Logs

5. In the Downloads/ folder are the 3 biosketches for the proposal:
   - Edwards_cv_202610.pdf
   - cv-yi zhang nih 2026 10.pdf
   - CV_Oceanography.pdf

The last one is mine.  Please combine all 3 into 1 file named 
`BioSketches.pdf` in the `Projects/BOONUS/proposals/Keck_2027` folder.
Have mine be first in order, then Edwards, then Zhang.

## Email

**Draft v2, 2026-10-18 (prompt #3; halved from v1 in `email_keck_guidance.md`).**
**To:** Sam Forde, Sarah Carle. **CC:** Chris Edwards (co-PI).

**Subject:** Keck 2027 internal application: a reality check before I write it

Dear Sam and Sarah,

I started preparing an internal application for the June 2027 Keck cycle (due October 25)
and want your advice before going further, because I'm pretty sure the project
I have in mind is a poor fit.

The plan was the modeling arm of BOONUS which I have discussed a bit with each of you.
Keck's new Application Instructions (August 26) and webinar slides (September 22)
exclude, verbatim, "translational or applied work", "engineering for efficiency,
optimization, or cost reduction", "incremental extension of established research
directions or methods" and "digital twin implementations". 
BOONUS is, at heart, an observing network whose purpose is to monitor the coastal ocean under climate change and feed forecasts for fisheries, harmful algal blooms and extreme weather. Its modeling component, as we have described it, is a real-time predictive system continuously ingesting glider data, which a Keck reviewer would likely call a digital twin. 
Even the version I had narrowed to, improving the assimilation with machine learning, reads as optimizing an existing technique.

So, I ask: 
Should we reconsider Keck this cycle, or aim for June 2027 with a better-framed version?

Chris is copied as co-PI.  On the positive side, by considering this
opportunity, I reached out to Chris to engage him on the project. :)
But maybe our time is best spent refining some of the ideas without 
pursuing Keck.

Let me know what you think.

Thanks!

Xavier

## Q&A

### Internal

**Round 1 (2026-10-17, prompt #1).** Written by Claude Fable 5.1 after reading the UCSC
call, the one-pager, the multi-pager v0.4, the canonical brief
(`context/initial_context_for_claude.md`), `reports/data_assimilation/da_ai_review.md`
v0.1, your earlier answers in `claude_prompts/context_prompts.md`, and the Keck
Foundation's own Application Instructions (dated 26 Aug 2026) and research-webinar slides
(Sep 2026), both fetched from wmkeck.org because the UCSC call's "Detailed Instructions"
were not in the folder. Answer inline after each `>A.`; K-numbers are for cross-reference.

#### 1. What the internal application is, concretely

- **Due Sunday 25 October 2026, 11:59 pm, on InfoReady: eight days from today.** Two
  uploads: the **Project Summary** (eight short-answer fields) and **SciENcv
  biosketches** (NSF or NIH format, ORCID required).
- The eight fields are, character for character, the Summary fields of Keck's own portal.
  What we write for UCSC is therefore the text the Foundation would receive on
  7 December, and Keck requires the Summary to be consistent with the six-page narrative
  that follows it. We should write the Summary as if the narrative already existed.
- The full Keck application, if UCSC forwards us: Project Info (title up to 200 chars; an
  1800-char abstract for a lay reader, published if funded; a 1500 x 1500 px graphical
  abstract for the Board, "mostly not scientists"; up to 5 team publications with DOIs
  and a 300-char relation statement each), the Summary, a **6-page narrative with three
  mandated bold headers in this order: "State of the Field and the Gap", "Approach",
  "Feasibility"**, a bibliography, biosketches, Other Support, optional collaboration
  letters, and five suggested reviewers. No budget at submission; budgets are invited
  about six weeks after the deadline, Zoom presentations about four months after,
  decisions about six months after (mid-June 2027). $1.0-1.3M in multiples of $100k,
  3 years, no indirects, paid in full at award. Faculty salary capped at 10%/yr, PI and
  Co-PI salaries together at 20% of the budget.
- Keck's five review criteria (webinar): Scientific Question "rooted in basic science";
  Approach ("a feasible pathway"); Innovation ("Will it create a new field? Will it unseat
  a popular idea?"); Impact; Risk ("comfortable with potential for failure as long as
  there is potential for great impact"). Their four stated reasons for decline: no
  fundamental science question; too applied/translational; incremental; implementation
  or risk concerns.

#### 2. The framing problem, and my recommendation

The hard fact first. Keck's exclusion list now names, verbatim: translational or applied
work; "engineering for efficiency, optimization, or cost reduction"; "incremental
extension of established research directions or methods"; and **"digital twin
implementations"**. Read against that list, the BOONUS pitch as written fails on three
counts: building 100 gliders is engineering at scale; "improve forecasting of extreme
weather, diagnose HABs, change management from reactive to proactive" is applied; and
the one-pager's "seamless, predictive weather map for our waters" that "continuously
ingest[s] glider data" is a digital twin by any reviewer's definition. Stanford's Keck
guidance page adds that Keck regards climate change as an already well-funded area; that
is Stanford's reading, not Keck's text, but it is a warning against a climate-monitoring
frame.

So the Keck proposal cannot be "fund BOONUS" or even "fund the BOONUS models". It has to
be a basic-science question for which (a) the CUGN record is the one dataset where the
question can be tested, (b) AI is the untried route to an answer, and (c) BOONUS is the
horizon, not the deliverable. My recommended one-line frame:

> **Is the coastal ocean learnable?** Can the subsurface state and evolution of a coastal
> ocean be inferred from sparse, sustained observation alone, without a numerical model of
> the physics standing between the measurements and the answer?

Why this is Keck-shaped, with the evidence from the DA review:

- **The paradigm tested.** For forty years ocean state estimation has meant a numerical
  model plus an assimilation scheme: 4D-Var with a hand-coded adjoint, or an ensemble
  filter. Every system in the review's Table 1 works that way. The question asks whether
  that intermediary is necessary on a coast.
- **What is impossible or unknown today.** No ocean system learns from observations end
  to end (review Section 7.3: nothing beyond sea-surface-height mapping). No system,
  classical or learned, assimilates glider depth-average velocity, the one absolute
  measure of circulation a glider gives (Section 9). No machine learning touches glider
  data anywhere in the assimilation chain. And no one can verify a subsurface coastal
  forecast independently of the reanalysis it was trained on (question 10 for Matt).
- **Why the gap has persisted.** The atmosphere got GraphCast and GraphDOP because ERA5
  and dense observations exist; the ocean has neither (Section 6, closing paragraph). The
  GLORYS-trained emulators (XiHe, WenHai, GLONET) inherit a reanalysis with a poorly
  observed subsurface: the circularity caveat. On coasts the models are weakest and the
  data sparsest, so the field has stayed with the adjoint.
- **Why now, and why here.** CUGN is twenty years of repeated sections on five lines, more
  than 95,000 profiles by 2016 (canonical figure; the current total is not yet computed),
  absolute velocity on every dive, oxygen since 2017, and CalCOFI alongside as an
  independent truth since 1951. It is the only coastal subsurface record dense enough to
  train on and still withhold from. In 2024-2025 Aardvark and GraphDOP showed that
  observation-only learning works at all in the atmosphere. That conjunction did not
  exist three years ago.
- **Risk Keck will accept.** The honest outcome may be "no": the coastal ocean may be too
  sparsely observed to learn. A measured failure is still a result, because it bounds the
  information content of a sustained section, which is the number BOONUS's line spacing
  depends on.

What this does to the three AI strands in the brief (Section 5): anomaly detection on the
data stream becomes a by-product (a learned prior flags what it cannot explain); adaptive
piloting is dropped from the Keck story (it is engineering); learned components inside
ROMS 4D-Var or CASE (category 2 of the review) become the fallback aim rather than the
headline, because "replace the adjoint with a surrogate" reads as optimization of an
existing technique.

#### 3. Candidate Scientific Question field (up to 300 characters; no methods, no instruments)

K1. Pick one or edit. Counts from `scripts/count_chars.py`, spaces included.
- (a) 249 chars: "Can the three-dimensional state and evolution of a coastal ocean be
  learned directly from sparse, sustained observations, without a numerical model of the
  physics as intermediary, and what does that reveal about how predictable the coastal
  ocean is?"
- (b) 238 chars: "Is the coastal ocean learnable? Two decades of repeated subsurface
  measurements off California exist; no one knows whether they hold enough information
  to reconstruct and predict the ocean between and beyond them without a physical model."
- (c) 222 chars: "What is the information content of the coastal ocean: how far in space
  and time does one sustained subsurface section constrain the waters around it, and can
  that limit be found empirically rather than assumed from models?"

Recommendation: (a) as the question, with (c)'s content as one of the aims; (b) is the
title voice, not the question voice. If "numerical model" counts as a "field-specific
framework" for Keck, (c) is the safe fallback.
>A.

#### 4. Questions, each with a recommendation

K2. **Scope agreement.** Do you accept that the Keck proposal is not "BOONUS", asks for
no gliders, and uses BOONUS only as motivation (one paragraph in State of the Field; one
sentence in Impact: "a national network is being designed; this work determines what such
a network can know")? Related: should the word BOONUS appear at all, given that Keck
publishes the abstract if funded? Recommendation: yes to the scope; name the network once
as planned, with no fleet numbers.
>A.

K3. **Which AI entry point is the headline.** Category 3 (learn the map from observations
to state, verified only against withheld observations) is the Keck-shaped choice;
category 2 (learned pieces inside ROMS 4D-Var or CASE) the fallback; category 4 (anomaly
detection) a by-product; category 1 (emulate a reanalysis) excluded as incremental on
GLONET. Agree? Recommendation: yes, and say so in Risks ("if the model-free route fails,
the physics-constrained hybrid is the floor").
>A.

K4. **Aims, provisionally three.** (i) Learn the coastal state from the CUGN record plus
satellite surface fields, scored only against withheld lines, withheld years and CalCOFI,
never against a reanalysis. (ii) Make the glider's native observables first-class: the
dive as a slanted, time-varying path, and depth-average velocity as a constraint, which no
documented system has done. (iii) Measure the information horizon: how far from a section
the learned state stays skilful, and at what section spacing a coast becomes "known"; this
is the empirical observing-system-design result. Biogeochemistry (oxygen, pH) either
inside (i) or as a fourth aim, given that Mattern et al. (2026) found T/S assimilation did
nothing for pH. Recommendation: three aims, with biogeochemistry inside (i) as the hardest
variable. Keep, drop, add?
>A.

K5. **Lead PI and key personnel.** Keck rules: the Lead PI must be at the applicant
institution; key personnel need institutional PI status and commit effort (paid or not);
subawards to other institutions carry no penalty; "the research team must demonstrate
expertise in each area required"; anyone on an active Keck award is ineligible. The areas
here are machine learning, ocean state estimation, and glider observation. Proposed: you
(Lead PI, UCSC), Matt Mazloff (Co-PI, Scripps subaward; the brief's nominal AI lead), Dan
Rudnick (Co-PI if he will commit effort, otherwise a collaboration letter). Two questions:
have you asked Matt, and is he willing to sign on to a model-free framing rather than an
adjoint one? And should a UCSC DA expert whose ROMS 4D-Var already assimilates CUGN (Chris
Edwards, Andy Moore) be a Co-PI, which strengthens Feasibility and keeps more of the work
at UCSC, or be named instead as a peer group (K8), which sharpens the contrast?
Recommendation: Matt as Co-PI; Rudnick by letter unless he wants effort; Edwards as Co-PI
only if he embraces the framing, otherwise his system is the paradigm being tested.
Please also confirm no proposed key person holds an active Keck award.
>A.

K6. **Your affiliation and the "New Area" field (600 chars).** This field favours us: a
team whose prior work is glider observation (Rudnick), adjoint state estimation (Mazloff)
and, I assume from your record, machine learning in astrophysics (you) proposing
something new to all three. I need your exact title and department for the biosketch and
key-personnel fields (the brief says "UC Santa Cruz Ocean Sciences"; Q55 in
`context_prompts.md` was never answered), and one or two sentences in your words on how
your astrophysics machine learning transfers, plus the two or three of your papers you
would list among the application's five.
>A.

K7. **Competing UCSC submissions and the UCSC offices.** UCSC may forward three, no two
in the same area of science (judged by area, not department). Do you know of other UCSC
Keck bids this cycle in ocean, Earth, climate or AI? Have you told fr@ucsc.edu you intend
to apply, and do you want Research Development (resdev@ucsc.edu) to read a draft?
Recommendation: send the notice of intent now; the internal committee will not be
oceanographers, so the lay-accessible Scientific Question carries this round.
>A.

K8. **Peer Groups (2-4 entries, 300 chars each).** Proposed four: (1) Mercator Ocean's
GLONET and the GLORYS-trained emulators XiHe and WenHai: they learn a global reanalysis,
start every forecast from a classical analysis, and their skill is surface-dominated; we
learn from observations, on a coast, subsurface, with no reanalysis in the loop.
(2) ECMWF's GraphDOP and the Turing/Cambridge Aardvark: observation-only learning in an
atmosphere observed about a thousand times more densely; we ask whether it survives ocean
sparsity. (3) M2LInES (Zanna; Samudra) and 4DVarNet (Fablet, IMT Atlantique): emulators
of models and learned solvers tested on simulations; we test on withheld real
observations. (4) The California Current adjoint systems (UCSC ROMS 4D-Var; Scripps CASE):
the classical paradigm with the same gliders, the baseline we must beat or explain. Keep
(4) only if Edwards and Moore are not key personnel. Agree?
>A.

K9. **Potential Impact, two distinct consequences (600 chars each).** Candidates:
(A) State estimation without a numerical model: any coast with sustained observation gets
a subsurface picture, which opens an observation-native oceanography on coasts, in polar
seas and for biogeochemistry where models are weakest, and makes the design of observing
networks an empirical question. (B) The predictability of the coastal ocean becomes a
measured quantity: how far and how long a section's information travels tells us which
processes (upwelling, boundary currents, teleconnections) govern coastal variability, and
whether subsurface precursors of marine heat waves and hypoxia exist. (C) A learned
representation of twenty years of a coastal ocean is a new kind of climatology, one that
can be queried for anomalies as data arrive. Recommendation: A and B; C folds into B.
>A.

K10. **Risks (300 chars) and their mitigation.** Risks I would state: the record may be
too sparse to learn subsurface dynamics; a learned system may not beat the adjoint
baseline; skill may not transfer beyond California; leaning on reanalyses would make the
test circular. Mitigations for the narrative: a ladder of OSSE on a ROMS nature run, then
OSE on CUGN with withheld lines and years, then CalCOFI as independent truth;
physics-constrained hybrids as the floor; and the explicit statement that a bounded
negative result is a result. Anything to add, or anything you would rather not admit in
300 characters?
>A.

K11. **Enabling Advances (300 chars).** Proposed: the twenty-year CUGN record with
absolute velocity and oxygen (and the 2026 climatology just rebuilt); observation-only
learning demonstrated in the atmosphere in 2024-25; generative (score-based) assimilation;
differentiable frameworks that make a hand-coded adjoint unnecessary. Recommendation: lead
with the data, since it is the one thing no peer group has.
>A.

K12. **Prior Support and preliminary data (600 chars).** Keck does not require
preliminary data and Stanford's guidance warns against work that looks already done. Do we
have any machine-learning result on CUGN at all (from `cugn-climatology` or elsewhere)? If
not, Recommendation: say so, and build Feasibility from related results: the CUGN record
and climatology (NOAA for nearly 20 years, SCCOOS/CeNCOOS/IOOS, to be named exactly),
Mazloff's state estimates, your machine learning in astrophysics, and the atmospheric
existence proofs. A cheap preliminary (predict a withheld CUGN section from its
neighbours and the satellite fields with a simple learned mapper, scored against CalCOFI)
would be worth a week in November for the full proposal, not for the internal one. Shall I
scope that script now so it is ready?
>A.

K13. **AI Use (300 chars; "applications will not be evaluated on this answer").**
Proposed, 255 chars: "Claude (Anthropic) was used under the PI's direction to survey the
data-assimilation and machine-learning literature, draft and edit text, and check
citations. All scientific claims, framing and decisions are the authors', who verified
every cited result." Agree with disclosing at that level?
>A.

K14. **Tone.** The brief's style rule 1 (no hype; Rudnick's warning about an "excess of
hype") meets Keck's appetite for bold, paradigm-challenging claims. Recommendation: let
the boldness live in the question and the honesty in the risks; every capability claim
still carries a number and a source; none of "transform", "irrefutable", "wow".
>A.

K15. **Title (up to 200 chars; external round, but it anchors the internal text).**
Options: (a) 104 chars, "Is the Coastal Ocean Learnable? Inferring the Subsurface State of
Coastal Waters from Observations Alone"; (b) 69 chars, "Learning the Coastal Ocean from
Twenty Years of Sustained Observation"; (c) 42 chars, "The Information Content of a
Coastal Ocean". Recommendation: (a).
>A.

K16. **Deliverables and schedule for prompt #2.** Proposed: `proposals/Keck_2027/
internal_summary.md` holding the eight fields with counts checked by
`scripts/count_chars.py` (already written; it carries the Keck limits and the K1, K13,
K15 candidates), a short note for the internal committee on why Keck and not a federal
agency, and a checklist for the biosketches; then one round of your edits; then you
upload by 25 October. Biosketches take longer than the text: do you have a current SciENcv
biosketch with ORCID, and do Matt and Dan? Recommendation: ask them today.
>A.

#### 5. Things noticed that may matter later

- The Keck abstract and graphical abstract are published if funded. Nothing from the
  private one-pager or multi-pager should be pasted into the application; paraphrase
  substance only, as the brief's style rule 4 already says.
- Style rule 5 (name only JXP, Rudnick, Mazloff) has to be relaxed for the application's
  key-personnel and peer-group fields; the brief itself stays as written.
- The DA review's thirteen questions for Matt are now also the feasibility questions a
  Keck reviewer will ask (how CASE treats glider velocity; how CUGN is quality-controlled;
  whether any centre runs a learned component inside its analysis). Sharing the review
  with Matt before he signs on as Co-PI serves both purposes.
- Keck deadlines are fixed: the second Monday after Thanksgiving (7 Dec 2026) and the
  first Monday after Memorial Day (7 Jun 2027). If UCSC does not forward us this round,
  the June cycle is the next chance, with a new internal competition.
- Sources beyond the folder: Keck Application Instructions (26 Aug 2026) and webinar
  slides (Sep 2026) from wmkeck.org, saved only in the session scratchpad; Stanford's
  Keck guidance page for the climate-funding warning. The UCSC call's "Detailed
  Instructions" and InfoReady form were not available to me; if the form has fields
  beyond the eight, tell me.

## Logs

### 2026-10-17 (Execute prompt #1: read the context, open the internal-proposal discussion)

Model: Claude Fable 5.1. Read, in this order: `keck_2027_prompts.md`; `CLAUDE.md` and
`claude_prompts/start_up.md` (house conventions); `context/initial_context_for_claude.md`
v0.1; the three PDFs in this folder via `pdftotext` (UCSC call, one-pager, multi-pager
v0.4); `reports/data_assimilation/da_ai_review.md` v0.1 in full; JXP's answers in
`claude_prompts/context_prompts.md` on the AI component (Q11, Q43, Q54, Q55) and the team
roster (Q18), and in `claude_prompts/data_assimilation_prompts.md` (DA35-DA62). Because the
UCSC call refers to Keck's "Detailed Instructions" without including them, fetched the
Foundation's Application Instructions PDF (26 Aug 2026) and the September 2026 webinar
slides from wmkeck.org, plus Stanford's Keck guidance page, and extracted their text; the
downloads live in the session scratchpad only, not in the repository.

Wrote `## Q&A / ### Internal`, Round 1: what the internal application is (the eight
Summary fields, identical to Keck's portal; biosketches; the 25 October deadline), the
framing problem (Keck now excludes applied work, optimization, incremental extensions and
"digital twin implementations", so the BOONUS pitch as written cannot be the Keck
proposal), a recommended frame ("Is the coastal ocean learnable?", built on the gaps the
DA review documents: no end-to-end ocean learning, no assimilation of glider
depth-average velocity, no ML on glider data, no reanalysis-independent coastal
verification), three candidate Scientific Question texts with character counts, and
sixteen numbered questions K1-K16 with recommendations covering scope, AI entry point,
aims, key personnel, the New Area field, UCSC competition and offices, peer groups,
impact, risks, enabling advances, prior support, AI-use disclosure, tone, title, and the
prompt #2 deliverables.

Created `proposals/Keck_2027/scripts/count_chars.py` (Keck's character limits as a table;
candidate texts; run with `conda run -n ocean14 python ...`), per the CLAUDE.md rule that
calculations go to disk. Output: K1a 249/300, K1b 238/300, K1c 222/300, K13 255/300,
K15a 104/200, K15b 69/200, K15c 42/200.

**What I learned about the repository and the task.**

- Keck changed its process in August 2026: one full submission (Summary, six-page
  narrative with mandated headers, SciENcv biosketches and Other Support), no concept
  paper, no budget until invited, six-month decisions, two cycles a year. Older web
  guidance (concept paper, Phase I/II) is obsolete; the UCSC call matches the new process.
- The internal UCSC Summary fields are the external ones, so the internal round is the
  external text in draft, not a separate document.
- The DA review, written as a neutral review with "no implications for BOONUS", turns out
  to supply the "State of the Field and the Gap" section almost directly: its stated gaps
  (Sections 7.3, 7.4, 9) and its circularity caveat are the Keck-shaped argument. Its
  thirteen questions for Matt Mazloff double as the feasibility questions.
- The brief's style rule 5 (names) and rule 1 (no hype) will both need a stated exception
  or interpretation for a funder-facing document; raised as K5/K14 rather than changed.
- `proposals/Keck_2027/context/` exists and is empty; the three PDFs sit in the folder
  root. The repository's `.gitignore` covers `context/**/*.pdf` (line 222), not
  `proposals/**`; `git status` shows the three PDFs here as untracked, so they will be
  committed unless JXP adds a rule or moves them. Flagged here, not changed.

No git commands that change repository state were run (`git status` and `git log` only).

### 2026-10-18 (Execute prompt #2: draft the email to Foundation Relations)

Model: Claude Fable 5.1. Reread `keck_2027_prompts.md` (prompt #2 added; K1-K16 still
unanswered, which prompt #2 supersedes for now). Checked what the repository records
about the recipients: Sam Forde is the recipient of the BOONUS one-pager and the Simons
Foundation saw the multi-pager (`context_prompts.md`, Context items 4-5; Q19 deferred
funding strategy); Sarah Carle is the Keck liaison and Executive Director of Foundation
Relations per the UCSC call; Chris Edwards's ROMS 4D-Var assimilates CUGN per the DA
review, Section 5.1.

Wrote `proposals/Keck_2027/email_keck_guidance.md`: a header (audience, status), the
email itself, a sources list for every factual claim, and three notes for JXP before
sending. The email, in JXP's voice, (1) states the plan that was taking shape (the
DA-AI arm of BOONUS, CUGN as testbed, no gliders requested); (2) reports the findings
from Keck's 26 Aug 2026 instructions and Sep 2026 webinar (the exclusion list including
"digital twin implementations", the four reasons for decline) and Stanford's statement
that climate change is treated as an already well-funded area, labelled as Stanford's
reading rather than Keck's text; (3) makes the "square peg in a round hole" admission in
JXP's words, with the reasoning (BOONUS is an observing and forecasting enterprise; its
modeling arm as pitched is a digital twin; ML inside assimilation reads as optimization);
(4) offers the basic-science reframing from Round 1 ("is the coastal ocean learnable?")
as a possibility whose credibility to Keck JXP cannot judge alone; (5) asks five
questions: reconsider or not (June 2027 cycle noted); UCSC's record with ocean/climate
proposals at Keck; internal collisions under the one-per-field rule; alternative
funders; a short meeting before 25 October; and (6) explains the CC to Edwards.

Decisions made on JXP's behalf, reversible by editing: the email keeps the K-round
reframing as an option rather than a proposal; it names Simons as the only alternative
funder because it is the only one the repository records; the self-critical paragraph is
marked as cuttable in the notes. No email addresses were looked up beyond the call. No
message was sent or drafted in any mail client; the deliverable is the file.

**What I learned:** the repository holds no roster of UCSC contacts or funders beyond
the two mentions above; if funding strategy becomes a workstream, a short
`proposals/contacts.md` (gitignored if it carries addresses) would save this lookup.

No git commands that change repository state were run.

### 2026-10-18 (Execute prompt #3: halve the email, move it to `## Email`, Chris Edwards as co-PI)

Model: Claude Fable 5.1. Reread `keck_2027_prompts.md`; found prompt #3 and the new empty
`## Email` section. Wrote draft v2 of the email directly under `## Email`, cut from v1 to
about half the length (word counts in the log below), with the same five findings kept
(the four verbatim Keck exclusions, Stanford's climate statement labelled as Stanford's
reading, the "square peg" admission, the basic-science reframing as a possibility, and
the reconsider question). Cuts: the Keck "reasons for decline" list, the longer
description of the reframing, and the separate internal-collision question, which is now
folded into question 2; five questions became four. Changed for the new fact that Chris
Edwards had agreed to be co-PI: he is named with Matt Mazloff as co-PI in the plan
paragraph, and the closing line says he is copied as co-PI, replacing v1's explanation of
him as an outside reader. `email_keck_guidance.md` is marked superseded in its header and
kept for its sources list and pre-send notes (the Sarah Carle address, fr@ucsc.edu intent
notice, the cuttable paragraph), which still apply to v2.

Word counts (body from Subject through the sign-off, computed by the splice script
`scratchpad/resplice_email.py`, not by hand): v1 645 words, v2 360 words, ratio 1.79. The
last fifth of the way to 2.0 would have meant dropping one of the four verbatim Keck
exclusions or a question, so it was left to JXP.

No git commands that change repository state were run.

### 2026-10-22 (Execute prompt #4: draft the eight internal-application fields, with a checker)

Model: Claude Fable 5.1. Reread `keck_2027_prompts.md`: prompt #4 added, the `## Email`
section carries JXP's own rewrite of the message (shorter, first person, co-PI Chris
Edwards), and K1-K16 remain unanswered. Drafted therefore on the Round 1 recommendations
and said so in a "Working assumptions" block at the top of the new file.

Wrote `proposals/Keck_2027/internal_proposal.md` v0.1: the eight Keck Summary fields
(Scientific Question; two Potential Impacts; Risks; Enabling Advances; New Area; three
Peer Groups; Prior Support; AI Use), each inside a ```` ```keck:<field> ```` fence, with
the alternative question (K1c), the dropped fourth peer group, a biosketch checklist and
a list of where each field's claims come from (the DA review Sections 5.1, 6, 7.1, 7.3
and 9; the brief Section 3; `context/sources/rudnick2017.md` for CUGN's NOAA funding).
Frame: observation-only learning of the coastal subsurface state, no gliders requested,
BOONUS as motivation only; key personnel Prochaska (Lead PI) and Edwards (co-PI),
Rudnick and Mazloff written as collaborators pending K5. The PI's prior machine learning
is described from what is on disk (the Ulmo and Nenya notebooks under
`cugn/papers/ARCTERX/Analysis/`, satellite sea-surface work) plus astrophysics, flagged
for JXP to confirm. Two funding sources in Prior Support are left as [bracketed]
placeholders.

Rewrote `scripts/count_chars.py` from the candidate-list form of prompt #1 into a checker
that parses the fences, collapses line wraps to one paragraph, enforces Keck's limits
(spaces included), requires pure ASCII because the InfoReady intake form is ASCII, warns
on any remaining bracket, checks the required set and the 2-4 peer-group count, and
writes the paste-ready unwrapped text to `internal_proposal_fields.txt` (ASCII-encoded;
regenerate it after every edit, do not edit it by hand). Exit status 1 on any failure.
First run found three fields over (Enabling Advances by 10, New Area by 1, Peer Group 1
by 11); trimmed and re-run: all eleven blocks pass, counts 249/300, 477/600, 560/600,
300/300, 294/300, 591/600, 290/300, 297/300, 299/300, 436/600 (placeholder warning),
255/300.

**What I learned:** the `cugn` repository holds JXP's ocean machine-learning lineage
(Ulmo, Nenya) under `papers/ARCTERX/`, which is the natural "related results" material
for Feasibility and for the New Area field; and the Risks field at exactly 300 characters
is the one most likely to break on JXP's first edit, so the checker is the first thing to
run afterwards.

No git commands that change repository state were run.

### 2026-10-24 (Execute prompt #5: combine the three biosketches)

Model: Claude Opus 5.5 (per JXP's instruction for this prompt). Inspected the three PDFs in
`~/Downloads` (all readable, unencrypted), then wrote `scripts/merge_biosketches.py`
(pypdf; reads the sources in place, writes one PDF, adds a bookmark per person) and ran it
in `ocean14`. Output `proposals/Keck_2027/BioSketches.pdf`, 10 pages, verified by
extracting the first line of each section:

| Order | Person | Source | Pages | Format |
|---|---|---|---|---|
| 1 | J. Xavier Prochaska | `CV_Oceanography.pdf` | 1-2 | Own CV layout, A4, no ORCID |
| 2 | Chris Edwards | `Edwards_cv_202610.pdf` | 3-5 | NSF biosketch (SciENcv), letter, ORCID 0000-0002-2100-5674 |
| 3 | Yi Zhang | `cv-yi zhang nih 2026 10.pdf` | 6-10 | NIH Common Form, letter, ORCID 0000-0003-4299-1511 |

**Flags, not acted on:**

- JXP's sketch is not a SciENcv biosketch and carries no ORCID. The UCSC call asks for a
  "PDF from SciENcv in NSF or NIH format", and Keck's external instructions accept only
  SciENcv biosketches that include an ORCID. It may pass the internal round; it will not
  pass Keck's. It is also A4 where the other two are US letter.
- Yi Zhang (UCSC Engineering) is a new key person. `internal_proposal.md` v0.1 names only
  Prochaska and Edwards (New Area, Working assumptions); the New Area field should gain a
  clause on Zhang's expertise, and the checker rerun, before upload.

Sources in `~/Downloads` were not modified. No git commands that change repository state
were run.
