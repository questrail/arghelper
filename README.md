# arghelper

arghelper is a Python package that provides functions to help with
argparse.

## Requirements

* Python standard `os` module

## Usage

```python
if __name__ == "__main__":
    # Process the arguments
    import argparse
    import arghelper
    parser = argparse.ArgumentParser(
        description='Process the TAFFmat CET files')
    parser.add_argument(
        'config_file',
        help='CSV configuration file.',
        metavar='FILE', type=lambda x: arghelper.is_valid_file(parser, x))
```

## Contributing

[arghelper][] is developed using [Scott Chacon][]'s [GitHub Flow][]. To
contribute, fork [arghelper][], create a feature branch, and then submit
a pull request.  [GitHub Flow][] is summarized as:

- Anything in the `master` branch is deployable
- To work on something new, create a descriptively named branch off of
  `master` (e.g., `new-oauth2-scopes`)
- Commit to that branch locally and regularly push your work to the same
  named branch on the server
- When you need feedback or help, or you think the brnach is ready for
  merging, open a [pull request][].
- After someone else has reviewed and signed off on the feature, you can
  merge it into master.
- Once it is merged and pushed to `master`, you can and *should* deploy
  immediately.

# License

[arghelper][] is released under the MIT license. Please see the
[LICENSE.txt][] file for more information.

[arghelper]: https://github.com/matthewrankin/arghelper
[github flow]: http://scottchacon.com/2011/08/31/github-flow.html
[LICENSE.txt]: https://github.com/matthewrankin/arghelper/blob/develop/LICENSE.txt
[pull request]: https://help.github.com/articles/using-pull-requests
[scott chacon]: http://scottchacon.com/about.html
