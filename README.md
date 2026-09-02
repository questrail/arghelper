# arghelper

[![PyPI Version][pypi ver image]][pypi ver link]
[![Python Versions][pyversions image]][pypi ver link]
[![CI Status][ci image]][ci link]
[![Coverage Status][coveralls image]][coveralls link]
[![License Badge][license image]][LICENSE.txt]

[arghelper][] is a Python 3.12+ module providing functions to help with argparse.

## Installation

You can install [arghelper][] either via the Python Package Index (PyPI) or from
source.

To add it to a project managed with [uv][], which records it in your
`pyproject.toml` and lock file:

```bash
$ uv add arghelper
```

Or to install it with pip:

```bash
$ pip install arghelper
```

**Source:** https://github.com/questrail/arghelper

## Requirements

- `argparse` module from the [Python Standard Library][]
- `os` module from the [Python Standard Library][]

## Usage

`arghelper` provides functions to determine if a file or directory
exists:

- `extant_file`
- `extant_dir`

These can be used as follows:

```python
if __name__ == "__main__":
    # Process the arguments
    import argparse
    import arghelper

    parser = argparse.ArgumentParser(description="Process the TAFFmat CET files")
    parser.add_argument(
        "config_file",
        help="CSV configuration file.",
        metavar="FILE",
        type=arghelper.extant_file,
    )
    parser.add_argument(
        "input_dir",
        help="Directory containing input files.",
        metavar="DIR",
        type=arghelper.extant_dir,
    )
    args = parser.parse_args()
```

A common pattern, for me at least, is to have three positional arguments
consisting of:

1. `config_file` --- A configuration file
2. `input_dir` --- A directory containing input files to be read
3. `output_dir` --- A directory where the output files should be saved

This pattern has been abstracted to a Facade function called
`parse_config_input_output`, which can be used as follows:

```python
if __name__ == "__main__":
    # Process the arguments
    import sys

    import arghelper

    args = arghelper.parse_config_input_output(sys.argv)
```

Another common pattern is to just parse the name of a config file:

```python
if __name__ == "__main__":
    # Process the arguments
    import sys

    import arghelper

    args = arghelper.parse_config(sys.argv)
```

## Contributing

Contributions are welcome! To contribute please:

1. Fork the repository
2. Create a feature branch
3. Add code and tests
4. Pass lint and tests
5. Submit a [pull request][]

## Development Setup

[arghelper][] uses [uv][] to manage the virtualenv and dependencies, and
[just][] as the task runner.

```bash
$ brew install uv just
```

`uv sync` creates the virtualenv and installs the dependencies, including
the development group, and `just` on its own lists the available recipes.

```bash
$ uv sync
$ just
```

The most common recipes are:

```bash
$ just test    # Run the tests using pytest
$ just lint    # Check lint, formatting, types, and workflows
$ just fix     # Lint and format the code using ruff, applying fixes
$ just cov     # Run the tests and report coverage
$ just add X   # Add X as a dependency
$ just out     # List the outdated dependencies
```

[ruff][] and [pyright][] are deliberately absent from that `brew install`
line. Both are dev dependencies pinned in `uv.lock` and reached through `uv
run`, so every recipe and every CI job uses the same version. A `brew
install ruff` would put a second, unpinned copy on the path for an editor
to find, and ruff releases change how code is formatted: the editor would
then reformat code that `ruff format --check` rejects on the next run.

The suite runs on 3.12, 3.13, and 3.14 in [CI][ci link], which is what
`requires-python` and the classifiers claim.

### Releasing to PyPI

`just release` cuts the release. It first checks that a release is possible
at all, then lints, type checks, and tests, then shows the entries waiting
under Unreleased and the version each kind of bump would produce, and asks
which to cut. Once answered it bumps the version, closes out the CHANGELOG,
updates the lock file, commits, and tags. Pushing the tag is what publishes.

```bash
$ just release
...
Which release? [1] 1

Tagged v0.6.1. Publish it with:

    git push --follow-tags
```

Do not tag by hand. The tag push runs the [release workflow][], which waits
on the whole [CI workflow][ci link] before it does anything else. It then
checks that the tagged commit is on `master`, since a tag is only a pointer
and one placed anywhere else would otherwise publish whatever it points at,
rechecks the tag against the version in `pyproject.toml`, and builds.

Every check to that point runs against the source tree, so the workflow
then installs the wheel it just built somewhere `src/` is not on the path
and exercises it there, which is the only step that can catch a packaging
mistake. It uploads once that passes. There is no PyPI API token anywhere:
the workflow authenticates with [trusted publishing][], which mints a short
lived credential from the GitHub OIDC identity of that run, and that same
identity signs a [PEP 740][] attestation for each distribution.

Uploading is followed by a [GitHub release][releases] for the tag, carrying
the CHANGELOG section for that version as its notes.

Pushing the tag is the point of no return, since PyPI never lets a version
number be reused. Everything `just release` does is local and amendable
until then, and it refuses to start against a dirty working tree, off
`master`, on a `master` behind its upstream, with a CHANGELOG whose
Unreleased section is empty, or when the tag it would create already
exists. `just release-check` runs those refusals on their own.

`just build` runs the same checks and produces the same distributions
without releasing anything.

This depends on one piece of configuration that lives outside the
repository. A [trusted publisher][trusted publishing] has to be registered
for `arghelper` on PyPI, pointing at the `questrail/arghelper` repository,
the `release.yml` workflow, and the `pypi` environment. It is a one time
setup per project.

## License

[arghelper][] is released under the MIT license. Please see the
[LICENSE.txt][] file for more information.

[arghelper]: https://github.com/questrail/arghelper
[ci image]: https://github.com/questrail/arghelper/actions/workflows/ci.yml/badge.svg?branch=master
[ci link]: https://github.com/questrail/arghelper/actions/workflows/ci.yml
[coveralls image]: https://coveralls.io/repos/github/questrail/arghelper/badge.svg?branch=master
[coveralls link]: https://coveralls.io/github/questrail/arghelper?branch=master
[github flow]: http://scottchacon.com/2011/08/31/github-flow.html
[just]: https://just.systems/
[license image]: https://img.shields.io/pypi/l/arghelper.svg
[LICENSE.txt]: https://github.com/questrail/arghelper/blob/master/LICENSE.txt
[PEP 740]: https://peps.python.org/pep-0740/
[pull request]: https://help.github.com/articles/using-pull-requests
[pypi ver image]: https://img.shields.io/pypi/v/arghelper.svg
[pypi ver link]: https://pypi.python.org/pypi/arghelper
[pyright]: https://microsoft.github.io/pyright/
[python standard library]: https://docs.python.org/3/library/
[pyversions image]: https://img.shields.io/pypi/pyversions/arghelper.svg
[release workflow]: https://github.com/questrail/arghelper/blob/master/.github/workflows/release.yml
[releases]: https://github.com/questrail/arghelper/releases
[ruff]: https://docs.astral.sh/ruff/
[trusted publishing]: https://docs.pypi.org/trusted-publishers/
[uv]: https://docs.astral.sh/uv/
