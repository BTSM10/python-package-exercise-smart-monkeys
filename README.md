# Rubber Duck Courtroom

[![Python Package CI](https://github.com/BTSM10/python-package-exercise-smart-monkeys/actions/workflows/ci.yml/badge.svg)](https://github.com/BTSM10/python-package-exercise-smart-monkeys/actions/workflows/ci.yml)

A humorous Python package that puts programming errors on trial
before a fictional rubber duck judge.

The package will generate courtroom statements from supplied arguments.
It does not inspect or fix code.

## Project status

The package foundation and automated checks are being established.
The five planned functions are not implemented yet.
The package has not been published to PyPI.

## Planned functions

| Function | Owner |
|---|---|
| file_charge(error_name, severity) | Rayyan |
| present_evidence(error_name, occurrences) | Biniam |
| call_witness(witness, mood) | Bereket |
| deliver_verdict(error_name, severity) | Rwan |
| issue_sentence(error_name, severity) | Abel |

## Developer setup

Install Git, Python, and Pipenv first.

Clone the shared repository:

```bash
git clone https://github.com/BTSM10/python-package-exercise-smart-monkeys.git
cd python-package-exercise-smart-monkeys
```

Create an environment using an installed Python version.
For example, with Python 3.13:

```bash
pipenv --python 3.13
pipenv sync --dev
pipenv run python -m pip install -e .
```

Replace 3.13 with 3.12 or 3.14 if that is your installed version.
CI checks Python 3.12 and 3.13.

## Run tests

```bash
pipenv run python -m pytest -v
```

## Build and validate

```bash
pipenv run python -m build
pipenv run python -m twine check dist/*
```

These commands build and check the package locally.
They do not publish it.

## Contributing

1. Update your local main branch.
2. Create a feature branch.
3. Implement your changes and tests.
4. Run tests and build the package.
5. Open a pull request into this team's repository.
6. Have another teammate review the code and run tests.
7. Merge after review and passing automated checks.

## Configuration

No database, external API, or runtime secrets are required.

## Before final submission

- Implement and test all five functions.
- Add complete function documentation and usage examples.
- Add an example program demonstrating all five functions.
- Link all teammates to their GitHub profiles.
- Publish to PyPI and add the package link and installation instructions.