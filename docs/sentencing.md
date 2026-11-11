# Sentencing and the complete demo

## Using `issue_sentence`

`issue_sentence(error_name, severity)` returns a string. It does not print anything
or change the caller's code.

- `error_name`: a non-empty string. Surrounding whitespace is removed. Custom
  names such as `MyCustomError` are accepted too.
- `severity`: an integer from 1 to 10, inclusive. Booleans, floats and numeric
  strings are not accepted.
- Invalid arguments raise `ValueError` with an explanation.
- The same inputs always produce the same output; there is no randomness.

| Severity | Punishment |
| --- | --- |
| 1–3 | Formal warning |
| 4–7 | `severity * 2` hours of refactoring |
| 8–10 | `severity * 3` hours of supervised debugging |

These ranges match `deliver_verdict`, so the verdict and punishment stay consistent.

### Examples

After installing the package, these calls work in a Python interpreter:

```pycon
>>> from rubber_duck_courtroom import issue_sentence
>>> print(issue_sentence("SyntaxError", 2))
SyntaxError receives a formal warning. The duck is watching you!

>>> print(issue_sentence("TypeError", 5))
TypeError is sentenced to 10 hours of refactoring!

>>> print(issue_sentence("ZeroDivisionError", 8))
ZeroDivisionError is sentenced to 24 hours of supervised debugging!

>>> print(issue_sentence("  MyCustomError  ", 10))
MyCustomError is sentenced to 30 hours of supervised debugging!

```

For example, `issue_sentence("", 5)`, `issue_sentence("TypeError", True)`, and
`issue_sentence("TypeError", 11)` each raise `ValueError`.

## Running the complete demo

From the repository root, follow the [developer setup](../README.md#developer-setup),
then run:

```bash
pipenv run python -m pip install -e .
pipenv run python examples/demo.py
```

The [demo](../examples/demo.py) calls all five public functions in order: charge,
evidence, witness, verdict and sentence. It prints three cases so that each
punishment tier, each witness mood, and zero/one/multiple occurrences are shown.
No database, API key or extra runtime dependency is needed.

The middle case prints:

```text
RUBBER DUCK COURTROOM
=============================================
CHARGES FILED
MISDEMEANOR: TypeError is charged with recklessly mixing incompatible data types. Severity: 5/10.

EVIDENCE PRESENTED
Exhibit A: TypeError was spotted once at the scene of the bug!

WITNESS TESTIMONY
Debugger rolls their eyes: 'Oh, wonderful. Another bug. Exactly what we needed.'

VERDICT
GUILTY! TypeError has disturbed the peace of the codebase.

SENTENCE
TypeError is sentenced to 10 hours of refactoring!

CASE CLOSED
=============================================
```

To try your own case, change the arguments in `main()` in `examples/demo.py`.
`run_case` uses the package's input validation and returns `None`. It builds all
five statements before printing, so an invalid input does not print a partial
trial. Evidence counts and verdicts are separate inputs: zero evidence does not
override the severity-based verdict in this fictional demo.

## Checking this work

```bash
pipenv run python -m pytest tests/test_sentences.py tests/test_public_api.py tests/test_demo.py -v
pipenv run python -m doctest docs/sentencing.md
pipenv run python -m pytest -v
```

The unit tests check sentencing rules and invalid inputs. The integration tests
check public imports, the ordering of all five stages, matching verdict and
sentence tiers, repeatable output, and execution as a standalone script.
