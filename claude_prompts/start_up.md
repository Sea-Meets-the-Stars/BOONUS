# Getting started 

## Goals

This repository will be used to define and promote the Boundary
Ocean Observing Network of the United States (BOONUS), the sustained network of
boundary-current and coastal observations of which the California Underwater Glider
Network (CUGN) is one component.  We will generate data products, metrics, and
diagnostics to share with the community.

## Prompts

1. Read this file.  Execute the 1st task under "Claude/CLAUDE.md file"
2. Read this file.  Execute the 1st task under "Claude/Skills"
3. Read this file.  Execute the 1st task under "Claude/Settings"
4. Read this file.  Execute the 1st task under "Basic start up"

5. Read this file.  I have answered your questions in Q&A.  Read those and act accordingly.  I will then execute a PR for this branch.

## Claude

### CLAUDE.md file

1. Please generate a basic CLAUDE.md file for this project.  Have it indicate:

- I will perform git commands
- Add to the CLAUDE.md file:  If you do any calculation, generate it as a python script and write it to disk so that I can add it to the Repository.
- Add to the CLAUDE.md file:  If you need to run Python, use the "ocean14" conda environment.
- Include in the CLAUDE.md file a pointer to the `cugn` repository on this computer: `/home/xavier/Oceanography/python/cugn`
- Note in the CLAUDE.md file that this repository lives in `/home/xavier/Projects`, not in `/home/xavier/Oceanography/python` with its sibling science repositories.

### Skills

1. Copy over the skills/ files from the `IOPtics` repository:
   `/home/xavier/Oceanography/python/IOPtics/.claude/skills`.  Copy them verbatim --
   they are repo-agnostic, so there is nothing to prune.  (Note that `cugn` itself has
   no `.claude/skills/` directory; IOPtics is upstream.)

### Settings

1. Copy over the settings.json file from the `IOPtics` repository:
   `/home/xavier/Oceanography/python/IOPtics/.claude/settings.json`.  Copy the policy
   (the allow/deny/ask structure), not the accumulated path-specific entries that
   reference IOPtics' own scratchpad and test files.

## Basic start up

1. Generate the basic files that one needs for a Python GitHub repository, e.g. a file
   for dependencies.  Examine the other Repositories in
   `/home/xavier/Oceanography/python` -- especially `cugn`, `cugn-climatology`, and
   `EPFT-UP` -- to see how I tend to organize things.  Also, make a suggestion of which
   of their settings.json files to copy into this one.

## Q&A

None of these blocked prompts 1-4; all four were executed. They are decisions I
made on your behalf and would like confirmed.

1. **Is the `## Goals` paragraph right?** I wrote it from the README's one line
   ("The Boundary Ocean Observing Network of the United States") plus the CUGN
   connection, and it is now echoed in three places: `CLAUDE.md`, `README.md`,
   and `setup.py`'s description. If the network's scope is different -- or if
   CUGN is not actually a component of it -- correct it here and I will
   propagate the change.

>A. It was ok.  I improved it

2. **Should BOONUS depend on `cugn` at all?** I assumed it does, by analogy with
   `cugn-climatology`, and gave it the glider-flavoured dependency stack
   (`gsw`, `gsw-xarray`, `xhistogram`, `dask`) rather than IOPtics'/EPFT-UP's
   ocean-colour stack. The `cugn` dependency is only a comment in
   `requirements.txt` and `setup.py`, not an active install line, so nothing
   breaks if the answer is no -- but the dependency list would want revisiting.

>A. It might.  Best to model it; thanks

3. **Add the three GitHub `WebFetch` domains to `.claude/settings.json`?**
   `github.com`, `raw.githubusercontent.com`, and `api.github.com` are the only
   generic allow entries any sibling has that we lack (PAB and
   retrieve-or-bust have them; retrieve-or-bust also has
   `Bash(git ls-remote *)`). They would be needed if we start installing
   sibling packages from GitHub. I did not add them -- your call.

>A. No need for now

4. **Is `boonus` the package name you want?** It follows the house convention
   (snake_case of the repo name, as in `ioptics`, `cugn_climatology`,
   `epft_up`), but the repo name is an acronym, so a different module name
   would be easy to justify while the package is still empty.

>A. Yes that is good

## Logging

The "Logs" section will record Claude's work.  Please use the following format:

### <Date> (Short summary of the work)

<Detailed description of the work and what you learned>

...

## Logs

### 2026-09-21 (Execute start-up prompts 1-4: CLAUDE.md, skills, settings, basic repo files)

Executed all four numbered prompts in one session.

**Prompt #1 -- `CLAUDE.md`.** Wrote `CLAUDE.md` at the repository root in the house
form, closest to `EPFT-UP/CLAUDE.md` and `cugn-climatology/CLAUDE.md` (the two that
carry the same set of directives). Sections: Project Overview (with repository
layout), Repository Location, Working Conventions, Related Repositories. All five
requested directives are present: the user performs git commands (read-only git
permitted), calculations are written to disk as Python scripts, Python runs in the
`ocean14` conda environment, `cugn` at `/home/xavier/Oceanography/python/cugn` is
named as related work, and the location caveat (this repo is in
`/home/xavier/Projects`, not in `/home/xavier/Oceanography/python`) has its own
section rather than a single line, because it changes how every other path in the
file has to be read.

**Prompt #2 -- skills.** Created `.claude/` and copied
`/home/xavier/Oceanography/python/IOPtics/.claude/skills` in verbatim: two skills,
one `SKILL.md` each -- `critical-partner` (constructive disagreement: surface an
untested assumption before agreeing, argue the strongest opposing case, retreat only
on new evidence, review weaknesses first, do not manufacture flaws, end with a
question) and `grill-me` (interview one question at a time down each branch of the
design tree, always offering a recommended answer, exploring the codebase rather than
asking what the codebase can answer). Verified byte-identical with `diff -r`.

**Prompt #3 -- settings.** Wrote `.claude/settings.json` from the IOPtics policy:
37 allow entries, 7 deny, 1 ask; validated as JSON.
- **Kept:** read-only shell (`ls`, `cat`, `cd`, `pwd`, `echo`, `find`, `grep`, `rg`,
  `head`, `tail`, `wc`, `sort`, `which`, `env`), benign file ops (`mkdir`, `touch`,
  `cp`, `mv`), read-only git (`status`, `diff`, `log`, `show`, `branch`),
  conda/python/pip/pytest/jupyter including `conda run -n ocean14`, and the four
  publisher `WebFetch` domains (Optica, ASLO/Wiley, doi.org, Taylor & Francis).
- **Pruned (28 entries):** every path-specific accretion -- absolute-path
  `pytest`/`python` invocations naming machine-specific interpreters (both
  `/home/xavier/miniconda3/...` and the stale `/Users/xavier/miniforge3/...`), the two
  Crossref `curl` calls with a literal DOI and a literal bibliographic query baked in
  and the two `python3 -c` JSON parsers that went with them, sphinx builds pointing at
  IOPtics' own scratchpad, `grep`s of IOPtics report files and of bokeh's minified JS
  in site-packages, and a `bing` import check. None of them could ever match here.
- **deny** and **ask** copied unchanged: `sudo`, `rm -rf /`, `rm -rf ~`,
  `git push`/`commit`/`reset`/`rebase`; `ask` on `rm:*`.

**Prompt #4 -- basic start up.** Surveyed the sibling repositories, then created:
- `boonus/` -- the package (snake_case of the repo name, per the house convention),
  with `__init__.py` declaring `__version__ = '0.0.dev0'` and `boonus/tests/` holding
  `__init__.py` plus `test_import.py` (import and version smoke tests).
- `requirements.txt` -- core scientific stack plus the *glider/gridded* set
  (`xarray`, `h5netcdf`, `netcdf4`, `cftime`, `gsw`, `gsw-xarray`, `xhistogram`,
  `dask`), i.e. cugn-climatology's list rather than EPFT-UP's ocean-colour one.
- `setup.py` -- the house `setup_keywords` dict idiom, `python_requires='>=3.12'`,
  `find_packages()`, README as `long_description`, the conditional `bin/` scripts
  block, and `url` pointing at the real remote (`Sea-Meets-the-Stars/BOONUS`).
- `pytest.ini` -- `testpaths = boonus/tests`, matching cugn-climatology and EPFT-UP.
- `.github/workflows/ci.yml` -- light advisory CI (install + import smoke check +
  `pytest -q` on py3.12 and py3.14), modelled on cugn-climatology's data-independent
  workflow rather than EPFT-UP's, since there is no `docs/` here to build.
- `README.md` -- expanded from two lines to the house form: description,
  Installation, Layout, Related work, License.

Verified: `setup.py` parses, `ci.yml` is valid YAML, and
`conda run -n ocean14 python -m pytest -q` passes (2 tests).

**Suggestion requested by prompt #4 -- which sibling `settings.json` to copy:**
Keep the IOPtics-derived policy installed by prompt #3. I compared every sibling's
allow-list against it programmatically. Six repos in `Oceanography/python` have a
committed `settings.json` (EPFT-UP, IOPtics, PAB, bing, cugn-climatology,
retrieve-or-bust). Ours is byte-for-byte the same policy as EPFT-UP's (37/37, the
most recently pruned one) and a strict superset of cugn-climatology's 33. All five
of the others agree on the identical `deny` and `ask` blocks except `bing`, which is
a minimal 8-entry outlier. The **only** generic entries any sibling has that we lack
are PAB's and retrieve-or-bust's three GitHub `WebFetch` domains (`github.com`,
`raw.githubusercontent.com`, `api.github.com`) plus retrieve-or-bust's
`Bash(git ls-remote *)`. I did not add them -- see Q&A #3.

**What I learned about this repository:**

- BOONUS is the first of these science repos to live outside
  `/home/xavier/Oceanography/python`, and that breaks one house idiom concretely:
  cugn-climatology installs its sibling with `pip install -e ../cugn`, which cannot
  work from `/home/xavier/Projects/BOONUS`. `requirements.txt`, `setup.py`, and
  `README.md` all use the absolute path instead, and the reason is written next to
  each so a future session does not "fix" it back to the relative form.
- The remote is `https://github.com/Sea-Meets-the-Stars/BOONUS.git` and the LICENSE
  is BSD 3-Clause, copyright 2026 Sea-Meets-the-Stars -- the same org as
  cugn-climatology, not IOPtics' `ocean-colour`. `setup.py`'s author/license/url
  fields were taken from cugn-climatology for that reason.
- The house layout is `requirements.txt` + `setup.py`, **not** `pyproject.toml`; none
  of the siblings uses one, and `setup.py` is effectively a shared template differing
  only in name/description/url/install_requires.
- `.github/workflows/` exists in cugn, cugn-climatology, EPFT-UP, and IOPtics, so CI
  is the house default and was included. I added the smoke tests deliberately:
  `pytest` exits 5 ("no tests collected") on an empty suite, which would make the new
  workflow red on its first run.
- The `ocean14` environment is Python 3.14.6, which is what the 3.14 leg of the CI
  matrix is tracking; 3.12 is the declared floor in `setup.py`.
- The pre-existing `.gitignore` (218 lines) already covers `__pycache__/`,
  `*.egg-info/`, and `.pytest_cache/`, so nothing needed adding there. `.gitignore`,
  `LICENSE`, and the `README.md` title line were the only files present before this
  session; only `README.md` was modified (extended, title kept).
- `cugn` itself has no `.claude/` directory at all, which is why prompt #2 points at
  IOPtics rather than at `cugn` the way cugn-climatology's does.

No git commands that change repository state were run (`git remote -v` and
`git status` only).

### 2026-09-21 (Execute prompt 5: act on the Q&A answers)

Read your four answers in `## Q&A` and acted on them. Only #1 required changes; the
other three confirmed what prompts 1-4 had already put in place.

**Q&A #1 (Goals -- "It was ok. I improved it") -- propagated.** Your edit changed the
scope verb: the repository is to *define and promote* BOONUS, where I had written
*assemble and analyze observations from* it. That is a meaningful difference, not a
rewording, so I pushed it into the two files that carried my phrasing:

- `CLAUDE.md` -- rewrote `## Project Overview` to match the new Goals text, and added a
  short paragraph making the emphasis explicit: the work is to define and promote the
  network, not only to analyze data from it, so deliverables that argue for and specify
  the network (documents, figures, requirements) are expected alongside analysis code.
  A future session reading only `CLAUDE.md` would otherwise assume this is a
  data-analysis repo like `cugn-climatology`.
- `README.md` -- opening paragraph now reads "Defines and promotes BOONUS: ..." and
  carries the community-sharing sentence from Goals.
- `setup.py` -- **no change needed.** Its `description` is the bare expansion of the
  acronym ("Boundary Ocean Observing Network of the United States (BOONUS)"), which is
  scope-neutral and correct under either reading. I had listed it as a propagation
  target in the question; on inspection it never contained the wording that changed.

**Q&A #2 (depend on `cugn`? -- "It might. Best to model it") -- no change.** Kept the
cugn-climatology model: the glider/gridded dependency stack (`gsw`, `gsw-xarray`,
`xhistogram`, `dask`) and the `cugn` dependency recorded as a comment rather than an
active install line, in both `requirements.txt` and `setup.py`. Nothing needs to
change if BOONUS does take the dependency -- uncommenting the absolute-path
`pip install -e /home/xavier/Oceanography/python/cugn` is the whole step.

**Q&A #3 (GitHub `WebFetch` domains? -- "No need for now") -- no change.**
`.claude/settings.json` stays at 37 allow / 7 deny / 1 ask. Worth knowing for whoever
hits it later: if a session ever needs to install a sibling package from GitHub, the
three domains (`github.com`, `raw.githubusercontent.com`, `api.github.com`) are the
entries to add, and they exist verbatim in PAB and retrieve-or-bust.

**Q&A #4 (package name -- "Yes that is good") -- no change.** `boonus/` stands.

Verified after the edits: `setup.py` still parses and
`conda run -n ocean14 python -m pytest -q` passes (2 tests).

**What I learned about this repository:**

- The scope correction is the substantive outcome of this prompt. "Define and promote"
  puts this repo closer to an advocacy/specification project with analysis in support,
  which is unlike every sibling in `Oceanography/python` -- those are all analysis
  packages. If that holds, the layout will want a `docs/`, `papers/`, or `reports/`
  directory before it wants more Python; I did not create one, since the house pattern
  is to add those directories when there is something to put in them.
- My propagation list in Q&A #1 was one file too long. Worth checking what a file
  actually says before promising to update it -- `setup.py`'s description had been
  written generically enough to survive the change.

No git commands that change repository state were run (`git status` only). The branch
is `start_up`; everything is left unstaged for your PR.
