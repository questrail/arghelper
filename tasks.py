from invoke import run, task

TESTPYPI = "https://testpypi.python.org/pypi"


@task
def lint(ctx):
    """Run flake8 to lint code"""
    run("python setup.py flake8")


@task(lint)
def test(ctx):
    """Lint, unit test, and check setup.py"""
    cmd = "{} {}".format(
        "nosetests",
        "--with-coverage --cover-erase --cover-package=arghelper --cover-html")
    run(cmd)
    run("python setup.py check")


@task()
def release(ctx, deploy=False, test=False, version=''):
    """Tag release, run Travis-CI, and deploy to PyPI
    """
    if test:
        run("python setup.py check")
        run("python setup.py register sdist upload --dry-run")

    if deploy:
        run("python setup.py check")
        if version:
            run("git checkout master")
            run("git tag -a v{ver} -m 'v{ver}'".format(ver=version))
            run("git push")
            run("git push origin --tags")
            run("python setup.py sdist bdist_wheel")
            run("twine upload --skip-existing dist/*")
    else:
        print("- Have you updated the version?")
        print("- Have you updated CHANGELOG.md, README.md, and AUTHORS.md?")
        print("- Have you fixed any last minute bugs?")
        print("- Have you merged changes for release into the master branch?")
        print("If you answered yes to all of the above questions,")
        print("then run `inv release --deploy -vX.YY.ZZ` to:")
        print("- Checkout master")
        print("- Tag the git release with provided vX.YY.ZZ version")
        print("- Push the master branch and tags to repo")
