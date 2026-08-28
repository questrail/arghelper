# CHANGELOG.md

This file contains all notable changes to the [arghelper][] project.

## v0.6.0 - 28-Aug-26

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
- Moved `arghelper.py` to a `src/arghelper/` layout built with hatchling.
- Switched the test runner to pytest and linting/formatting to ruff.

### Removed
- Removed `setup.py`, `setup.cfg`, `MANIFEST.in`, `requirements.txt`,
  `tasks.py`, and `.travis.yml`.
- Removed the unused `numpy` dependency declaration, which was declared via
  the inert distutils `requires` field and never used by the module.
- Removed the Python 2 `__future__` imports and encoding declarations.

## v0.5.2 - 20-Aug-23

### Fixed
- Fixed deployment since v0.5.0 did not deploy correctly.

## v0.5.1 - 20-Aug-23

### Fixed
- Fixed deployment since v0.5.0 did not deploy correctly.

## v0.5.0 - 20-Aug-23

### Modified
- Updated dependencies.

## v0.4.2 - 04-Oct-16

### Fixed
- Changed back from packages to py_modules in setup.py

## v04.0 - 2016-10-03

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
