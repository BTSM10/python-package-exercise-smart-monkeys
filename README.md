# Rubber Duck Courtroom

[![Python Package CI](https://github.com/software-students-fall2026/python-package-exercise-smart-monkeys/actions/workflows/ci.yml/badge.svg)](https://github.com/software-students-fall2026/python-package-exercise-smart-monkeys/actions/workflows/ci.yml)

A humorous Python package that puts programming errors on trial
before a fictional rubber duck judge.

The package generates courtroom statements from supplied arguments.
It does not inspect or fix code.

## Installation

Install Rubber Duck Courtroom from PyPI:

```bash
python -m pip install rubber-duck-courtroom
```

The package generates humorous courtroom statements from developer-supplied arguments.

## Quick Start

```python
from rubber_duck_courtroom import (
    file_charge,
    present_evidence,
    call_witness,
    deliver_verdict,
    issue_sentence,
)

error = "SyntaxError"
severity = 8

print(file_charge(error, severity))
print(present_evidence(error, 3))
print(call_witness("Compiler", "dramatic"))
print(deliver_verdict(error, severity))
print(issue_sentence(error, severity))
```

Each function returns a string. Invalid arguments raise ValueError.

For a complete demonstration, see [examples/demo.py](examples/demo.py).

## Project status

All five courtroom functions have been implemented, including their input validation and unit tests.
The package supports filing charges, presenting evidence, calling witnesses, delivering verdicts, and issuing sentences.

## Available functions

| Function | Owner |
|---|---|
| file_charge(error_name, severity) | Rayyan |
| present_evidence(error_name, occurrences) | Biniam |
| call_witness(witness, mood) | Bereket |
| deliver_verdict(error_name, severity) | Rwan |
| issue_sentence(error_name, severity) | Abel |

## API Documentation

Rubber Duck Courtroom provides five functions for putting programming errors on trial. Each function accepts arguments and returns a humorous courtroom statement as a string.

### 1. File a Charge

**Function:** `file_charge(error_name, severity)`

Creates a fictional charge against a programming error. The charge depends on the error name and severity.

**Parameters:**
- `error_name` (str): Non-empty error name.
- `severity` (int): Integer from 1 to 10.

**Severity levels:**
- 1–3: Minor offence
- 4–7: Misdemeanor
- 8–10: Felony

**Example:**

```python
from rubber_duck_courtroom.charges import file_charge

print(file_charge("SyntaxError", 8))
```

**Output:**

```text
FELONY: SyntaxError is charged with violating the laws of Python grammar. Severity: 8/10.
```

### 2. Present Evidence

**Function:** `present_evidence(error_name, occurrences)`

Generates an evidence report describing how many times a programming error occurred.

**Parameters:**
- `error_name` (str): Non-empty error name.
- `occurrences` (int): Non-negative integer.

**Example:**

```python
from rubber_duck_courtroom.evidence import present_evidence

print(present_evidence("TypeError", 3))
```

**Output:**

```text
Exhibit A: TypeError was spotted 3 times at the scene of the bug!
```

### 3. Call a Witness

**Function:** `call_witness(witness, mood)`

Generates a witness testimony based on the selected mood.

**Parameters:**
- `witness` (str): Non-empty witness name.
- `mood` (str): "calm", "dramatic", or "sarcastic".

**Example:**

```python
from rubber_duck_courtroom.witnesses import call_witness

print(call_witness("GitHub", "calm"))
```

**Output:**

```text
GitHub calmly addresses the court: 'Your Honor, let us examine the evidence carefully.'
```

### 4. Deliver a Verdict

**Function:** `deliver_verdict(error_name, severity)`

Determines the guilt of a programming error based on its severity.

**Parameters:**
- `error_name` (str): Non-empty error name.
- `severity` (int): Integer from 1 to 10.

**Severity levels:**
- 1–3: Warning
- 4–7: Guilty
- 8–10: Guilty with extreme prejudice

**Example:**

```python
from rubber_duck_courtroom.verdicts import deliver_verdict

print(deliver_verdict("SyntaxError", 8))
```

**Output:**

```text
GUILTY WITH EXTREME PREJUDICE! SyntaxError has terrorized the codebase.
```

### 5. Issue a Sentence

**Function:** `issue_sentence(error_name, severity)`

Assigns a humorous punishment to a programming error.

**Parameters:**
- `error_name` (str): Non-empty error name.
- `severity` (int): Integer from 1 to 10.

**Severity levels:**
- 1–3: Formal warning
- 4–7: Severity × 2 hours of refactoring
- 8–10: Severity × 3 hours of debugging

**Example:**

```python
from rubber_duck_courtroom.sentences import issue_sentence

print(issue_sentence("SyntaxError", 8))
```

**Output:**

```text
SyntaxError is sentenced to 24 hours of supervised debugging!
```

### Error Handling

All five functions raise `ValueError` when arguments are invalid.

Examples of invalid inputs include:
- Empty or whitespace-only error names and witness names
- Severity values outside 1–10
- Non-integer severity values, including booleans
- Negative or non-integer occurrence counts
- Unsupported witness moods

Leading and trailing whitespace is removed from names. Witness moods are case-insensitive.

## Developer setup

Install Git, Python, and Pipenv first.

Clone the shared repository:

```bash
git clone https://github.com/software-students-fall2026/python-package-exercise-smart-monkeys.git
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

## Complete demo

After completing the developer setup, run:

```bash
pipenv run python examples/demo.py
```

The [example program](examples/demo.py) uses all five functions to show three
complete trials. See the [sentencing and demo guide](docs/sentencing.md) for
punishment rules, exact output examples and verification commands.

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

## Contributors

- [Rayyan](https://github.com/RayyanAhmed21) - Charges and package integration
- [Biniam](https://github.com/BTSM10) - Project setup, CI, and evidence
- [Bereket](https://github.com/Bereket-454) - Witnesses and quality assurance
- [Rwan](https://github.com/rz3007) - Verdicts and documentation
- [Abel](https://github.com/Abel200595) - Sentences and example program