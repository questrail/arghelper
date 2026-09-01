# CHANGELOG.md

This file contains all notable changes to the [arghelper][] project.

## Unreleased

## v0.7.0 - 2026-09-01

### Changed

- List `369937+matthewrankin@users.noreply.github.com` as the author
  address in `pyproject.toml`, replacing a work address. It is what
  `Author-email` carries in the built metadata and what PyPI shows on the
  project page, so it changes there from the next release onward.

### Removed

- Support for Python 3.9, 3.10, and 3.11. `requires-python` is now
  `>=3.12`, which is the floor the other questrail projects use. The
  module still runs on the older three, and the suite passed on every one
  of them when this was checked, so anyone who needs one can keep
  installing v0.5.2, the last release published to PyPI that runs on
  them: pip reads `requires-python` and will not offer a later release to
  an interpreter it excludes. v0.6.0 was tagged but never reached PyPI,
  so it is not an option.

  Supporting 3.9 was not free. It held the lock file to versions of the
  dev tools that still supported it, and [zizmor][], which audits the
  workflows, needs 3.10 and had to be carried behind an environment
  marker. With the floor raised the marker is gone and the tools resolve
  to the same versions the other projects pin.

## v0.6.0 - 2026-08-28

### Fixed
- `parse_config()` and `parse_config_input_output()` no longer bind
  `sys.argv` as a default argument at import time. The default is now `None`
  and `sys.argv` is read when the function is called, so callers that
  reassign `sys.argv` are no longer silently ignored.
- `extant_item()` now raises `ValueError` for an `arg_type` other than
  `"file"` or `"directory"`. It previously fell through both branches and
  returned `None`, which argparse would store in the namespace.

### Changed
- **Breaking:** `extant_file()`, `extant_dir()`, and `extant_item()` now
  raise `argparse.ArgumentTypeError` instead of `argparse.ArgumentError`.
  `ArgumentTypeError` is the documented exception for an argparse `type=`
  callable, and argparse now reports the offending argument by name:
  `error: argument FILE: The file missing.csv does not exist.` Code that
  catches `argparse.ArgumentError` from these functions must be updated;
  the two exceptions are unrelated classes.

### Modified
- Migrated packaging and tooling to [uv][] and [Just][], matching the
  `applyaf` and `siganalysis` projects.
- Added `ruff` to the development dependency group. `just lint`, `just fix`,
  and `just deploy` previously relied on a globally installed `ruff` and
  failed on a clean checkout.
- Fixed the README: corrected the `metvar=` typo in the `add_argument()`
  example, added the missing `import sys` to the `parse_config_input_output()`
  and `parse_config()` examples, dropped the `sys` module from Requirements
  (no longer imported), removed the dead Travis-fed Coveralls badge, and
  pointed the Python Standard Library link at the Python 3 docs.
- Moved `arghelper.py` to a `src/arghelper/` layout built with hatchling.
- Switched the test runner to pytest and linting/formatting to ruff.

### Removed
- Removed `setup.py`, `setup.cfg`, `MANIFEST.in`, `requirements.txt`,
  `tasks.py`, and `.travis.yml`.
- Removed the unused `numpy` dependency declaration, which was declared via
  the inert distutils `requires` field and never used by the module.
- Removed the Python 2 `__future__` imports and encoding declarations.

## v0.5.2 - 2023-08-20

### Fixed
- Fixed deployment since v0.5.0 did not deploy correctly.

## v0.5.1 - 2023-08-20

### Fixed
- Fixed deployment since v0.5.0 did not deploy correctly.

## v0.5.0 - 2023-08-20

### Modified
- Updated dependencies.

## v0.4.2 - 2016-10-04

### Fixed
- Changed back from packages to py_modules in setup.py

## v0.4.0 - 2016-10-03

### Added
- Added parse_config function/pattern

### Modified
- Updated dependencies
- Started using Python3 venv for local development

## v0.3.2 - 2015-08-20

### Added
- Added coverage to test task and pip requirements.

## v0.3.0 - 2015-08-20

### Added
- Migrated from Travis-CI's legacy to container-based
  infrastructure.
- Added pandoc to Travis-CI's addons

## v0.2.3 - 2015-08-20

### Added
- Updated requirements.txt

## v0.2.2 - 2014-08-14

### Fixed
- `parse_config_input_output()` had an error causing it to fail.

## v0.2.1 - 2014-08-08

### Fixed
- Fixed all links due to moving Github repo:
  - **Old:** https://github.com/matthewrankin/arghelper
  - **New:** https://github.com/questrail/arghelper

## v0.2 - 2014-08-08

### Added
- Automate PyPI deployment
- Change badges to use shields.io
- Move CHANGES.md to CHANGELOG.md

## v0.1 - 2014-06-19

### Added
- Initial release to Github. Not released to PyPI.

[arghelper]: https://github.com/questrail/arghelper
[just]: https://just.systems/
[uv]: https://docs.astral.sh/uv/
[zizmor]: https://docs.zizmor.sh/
