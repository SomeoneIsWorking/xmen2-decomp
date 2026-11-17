# AGENTS.md

Facts about this repository; the working rules are the global instructions and the skills.

- Python runs through `uv run --frozen` (`pyproject.toml`, `uv.lock`); no dependencies.
- Check: `uv run --frozen python tools/verify.py "<install dir>"` (the pinned images). Run it in
  every change to `config/images.toml`.
- The symbol map is checked by x86port's `tools/symbol_constants.py` (format, duplicates, sections
  and executable code), which generates the port's constants on every port build:
  `python <x86port>/tools/symbol_constants.py --images config/images.toml --namespace x --output <tmp dir>`.
- A new name goes into `config/symbols/<image>.txt` at its address, in address order, typed
  `func` (an entry), `label` (inside code) or untyped (data), named for the guest concept
  (`MenuMgr_Get`, `PopupDialog_Draw`, `g_MenuStyle`, `s_StyleMenu`), not the port file that uses it;
  the port bumps this submodule in the change that uses it.
- The frontier: `uv run --frozen python <re-harness>/tools/re_frontier.py <cmd>` from this root.
- Game files never enter git.
