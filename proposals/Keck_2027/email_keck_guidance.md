# Draft email: guidance on the Keck 2027 internal application

**Drafted:** 2026-10-18, JXP and Claude (Fable 5.1), prompt #2 of `keck_2027_prompts.md`.
**To:** Sam Forde, Sarah Carle (Foundation Relations). **CC:** Chris Edwards.
**Status:** v1, superseded 2026-10-18 by the halved v2 in `keck_2027_prompts.md`, `## Email` (prompt #3). Kept for its sources and notes; v1 also predates the information that Chris Edwards is a co-PI. Sources behind every factual claim are listed
after the email.

---

**Subject:** Keck 2027 internal application: a reality check before I write it

Dear Sam and Sarah,

I am preparing an internal application for the June 2027 Keck cycle (due October 25) and
want your advice before I go further, because what I have learned this week makes me
doubt the fit.

The idea I had been shaping is the modeling arm of BOONUS, the national glider network
Dan Rudnick (Scripps) and I are developing: a machine-learning approach to assimilating
glider observations into coastal ocean state estimates, led with Matt Mazloff (Scripps),
using the twenty-year California Underwater Glider Network record as the testbed. The
network itself would not be in the request.

Here is what I found in Keck's new Application Instructions (dated August 26) and the
slides from their September 22 webinar.

- Keck's exclusion list now names, verbatim, "translational or applied work",
  "engineering for efficiency, optimization, or cost reduction", "incremental extension
  of established research directions or methods", and "digital twin implementations".
- Their four stated reasons for decline are: no fundamental science question; too
  applied or translational; incremental; implementation or risk concerns.
- Stanford's internal guidance for this same cycle goes a step further and says that
  areas already well funded or highly competitive, naming the BRAIN Initiative and
  climate change, are not appropriate for Keck. That sentence is Stanford's reading, not
  Keck's own text, but I would like to know whether it matches your experience with the
  Foundation.

Reading our pitch against that list, I have to be honest: I was already pushing a square
peg into a round hole by writing a data-assimilation-and-AI proposal for Keck. BOONUS is,
at heart, an observing network whose purpose is to monitor the coastal ocean under
climate change and feed forecasts for fisheries, harmful algal blooms and extreme
weather. Its modeling component, as we have described it, is a real-time predictive
system continuously ingesting glider data, which a Keck reviewer would call a digital
twin. Even the version I had narrowed to, improving the assimilation with machine
learning, reads as optimizing an existing technique.

There may be a genuinely basic-science version. The question would be whether the
subsurface state of a coastal ocean can be learned from sparse, sustained observations
alone, without a numerical model in between, and how much information such observations
hold. No one has done that for the ocean; it has only just been shown possible for the
atmosphere; and the California glider record is the one dataset where it can be tested.
That proposal would request no gliders, would mention the network only as motivation,
and might fail, which Keck says it accepts. But I cannot tell from here whether that
reframing is credible to Keck or whether it still carries the climate and applied labels.

So my questions are these:

1. Given the exclusions above and the Stanford note, should I reconsider submitting to
   Keck at all this cycle? The June 2027 deadline is also available if a slower, better
   framed version would be stronger.
2. Has UCSC seen ocean, Earth or climate-adjacent proposals succeed with Keck under the
   new process or recently, and if so, how were they framed?
3. Are there other UCSC Keck applications in ocean, Earth or AI this cycle that mine
   would collide with under the one-project-per-field rule?
4. If Keck is the wrong home, which foundations would you point this work toward? The
   Simons Foundation has seen the fuller BOONUS description already.
5. Could we find twenty minutes before the 25th? I would rather decide with you than
   submit something that costs the campus one of its three slots.

I am copying Chris Edwards because his group's ROMS assimilation system already ingests
the California glider data, so he is the natural reader of whether the basic-science
version holds up, and because he knows the campus landscape for this kind of proposal.

Thank you both,

Xavier

---

## Sources for the claims in the email

- W. M. Keck Foundation, *Research Program Application Instructions*, 26 Aug 2026,
  wmkeck.org (exclusions, p. 1; Summary fields, pp. 2-3; narrative, pp. 3-4; deadlines
  and cycle, p. 5). Fetched 2026-10-17.
- W. M. Keck Foundation, *Research Program: New Application Process*, webinar slides,
  Sep 2026, wmkeck.org ("Keck does not fund" list including "Digital twin
  implementations"; "Why do projects get declined?"; "What Keck looks for during review";
  Pasteur's-quadrant slide, which admits use-inspired basic research and excludes
  applied research and development). Fetched 2026-10-17.
- Stanford Research Development Office, *W.M. Keck Foundation Research Program
  Guidelines* (the sentence on areas "already well funded or highly competitive, such as
  the BRAIN Initiative or climate change"). Fetched 2026-10-17.
- UCSC Offices of Research and Foundation Relations, *Limited submission call, W.M. Keck
  Foundation Research Program, June 2027 cycle* (internal deadline 25 Oct 2026; three
  applications per campus; one project per field).
- `reports/data_assimilation/da_ai_review.md` v0.1 for the statements that no ocean
  system learns end to end from observations (Section 7.3) and that the atmospheric
  demonstrations are from 2024-2025 (Section 6: Aardvark, GraphDOP).
- Chris Edwards's group and glider assimilation: Mattern et al. (2026) and the UCSC
  near-real-time analysis page, as recorded in the review, Section 5.1.

## Notes for JXP before sending

- Sam Forde's and Chris Edwards's email addresses are not in the repository; Sarah
  Carle's is sacarle@ucsc.edu per the call. The call also asks that intent to apply be
  signalled to fr@ucsc.edu.
- Question 4 names only Simons because that is the one foundation the repository records
  as having seen BOONUS material (`claude_prompts/context_prompts.md`, Context item 5).
  Add others if you have them in mind.
- If you would rather not state the "square peg" judgement in writing to Foundation
  Relations, the paragraph beginning "Reading our pitch against that list" can be cut to
  its last sentence without losing the argument.
