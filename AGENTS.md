# AGENTS.md

Facts about this repository; the working rules are the global instructions and the skills.

- Python runs through `uv run --frozen` (`pyproject.toml`, `uv.lock`); no dependencies.
- Check: `uv run --frozen python tools/verify.py "<install dir>"`. Run it in every change to
  `config/`.
- A new name goes into `config/symbols/<image>.txt` at its address, in address order, typed
  `func` (an entry), `label` (inside code) or untyped (data); the port bumps this submodule in the
  change that uses it.
- The frontier: `uv run --frozen python <re-harness>/tools/re_frontier.py <cmd>` from this root.
- Game files never enter git.
