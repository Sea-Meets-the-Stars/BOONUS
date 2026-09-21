# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is used to define and promote BOONUS, the Boundary Ocean Observing
Network for the United States — the sustained network of boundary-current and coastal
observations of which the California Underwater Glider Network (CUGN) is one component.
We will generate data products, metrics, and diagnostics to share with the community.

Note the emphasis: the work is to *define and promote* the network, not only to analyze
data from it. Expect deliverables that argue for and specify the network (documents,
figures, requirements) alongside the analysis code.

Repository layout:

- `context/initial_context_for_claude.md` — the canonical project brief; read it
  before writing anything about BOONUS. `context/sources/` holds digests of the source
  documents; the source PDFs themselves are private and gitignored.
- `claude_prompts/` — prompts and task definitions that drive this work. Read the
  relevant prompt doc (starting with `start_up.md`) before acting, and execute only
  the numbered task you were pointed at.

## Repository Location

This repository lives at `/home/xavier/Projects/BOONUS` — **not** in
`/home/xavier/Oceanography/python`, where its sibling science repositories (`cugn`,
`cugn-climatology`, `IOPtics`, `EPFT-UP`, `PAB`, …) are kept. When looking to those
repositories for conventions or code, use their absolute paths; they are not siblings
of this directory.

## Working Conventions

- **Git:** The user (J. Xavier Prochaska) will perform all git commands (add, commit,
  push, etc.). Do not run git commands that change repository state unless explicitly
  asked. Read-only git commands (e.g. `git status`, `git diff`, `git log`) are fine.
- **Calculations:** If you do any calculation, generate it as a Python script and write
  it to disk so that it can be added to the repository. Do not perform one-off
  calculations only in memory or in the chat.
- **Python environment:** If you need to run Python, use the `ocean14` conda environment
  (e.g. `conda run -n ocean14 python script.py`).
- **Logging:** Record completed work under the `## Logs` section of the prompt doc that
  drove it, dated, including what was learned about the repository.

## Related Repositories

- **cugn:** The main CUGN analysis package lives on this computer at
  `/home/xavier/Oceanography/python/cugn`. Refer to it for glider data handling,
  existing analysis code, and project conventions.
- **cugn-climatology:** CUGN climatologies at
  `/home/xavier/Oceanography/python/cugn-climatology`.
- **IOPtics:** `/home/xavier/Oceanography/python/IOPtics` is the upstream source for
  this project's `.claude/skills/` and `.claude/settings.json`.
