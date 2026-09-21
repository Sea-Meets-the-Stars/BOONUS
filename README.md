# BOONUS
The Boundary Ocean Observing Network of the United States

Defines and promotes BOONUS: the sustained network of boundary-current and
coastal observations of the United States, of which the California Underwater
Glider Network ([CUGN](https://spraydata.ucsd.edu/projects/CUGN/)) is one
component. We will generate data products, metrics, and diagnostics to share
with the community.

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

This package builds on the `cugn` package, which is not on PyPI. This
repository does not sit alongside it, so install it from its absolute path:

```bash
pip install -e /home/xavier/Oceanography/python/cugn
```

## Layout

```
boonus/            # the Python package
  tests/           # test suite (pytest)
claude_prompts/    # prompt docs driving the work (start here: start_up.md)
```

## Related work

- [cugn](https://github.com/AI-for-Ocean-Science/cugn) — CUGN glider data handling and analysis
- [cugn-climatology](https://github.com/Sea-Meets-the-Stars/cugn-climatology) — CUGN climatologies

## License

BSD 3-Clause (see [LICENSE](LICENSE)).
