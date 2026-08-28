# arghelper

[![PyPi Version][pypi ver image]][pypi ver link]
[![License Badge][license image]][LICENSE.txt]

[arghelper][] is a Python 3.9+ module providing functions to help with argparse.

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

### Development Setup Using uv

With [uv][] and [Just][] installed, development has been simplified to
simply running [Just][] to see the available commands. [ruff][] is a
development dependency, so `uv` installs it for you.

```bash
$ just
```

#### Deploying with uv

```bash
$ just test
$ git tag -a vX.Y.Z -m "vX.Y.Z"
$ just deploy
```

#### Development Setup on macOS

```bash
$ brew install uv just
```

# License

[arghelper][] is released under the MIT license. Please see the
[LICENSE.txt][] file for more information.

[arghelper]: https://github.com/questrail/arghelper
[just]: https://just.systems/
[github flow]: http://scottchacon.com/2011/08/31/github-flow.html
[LICENSE.txt]: https://github.com/questrail/arghelper/blob/master/LICENSE.txt
[license image]: http://img.shields.io/pypi/l/arghelper.svg
[pull request]: https://help.github.com/articles/using-pull-requests
[pypi ver image]: http://img.shields.io/pypi/v/arghelper.svg
[pypi ver link]: https://pypi.python.org/pypi/arghelper
[ruff]: https://docs.astral.sh/ruff/
[uv]: https://docs.astral.sh/uv/
[python standard library]: https://docs.python.org/3/library/
