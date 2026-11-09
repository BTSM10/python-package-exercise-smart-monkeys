"""Tests for courtroom evidence reports."""

import pytest

from rubber_duck_courtroom.evidence import present_evidence


def test_zero_occurrences():
    """Zero occurrences should produce a no-evidence report."""
    assert present_evidence("IndexError", 0) == (
        "No evidence found against IndexError. "
        "The duck demands better detective work!"
    )


def test_one_occurrence():
    """One occurrence should use singular wording."""
    assert present_evidence("TypeError", 1) == (
        "Exhibit A: TypeError was spotted once "
        "at the scene of the bug!"
    )


def test_multiple_occurrences():
    """Multiple occurrences should include the supplied count."""
    assert present_evidence("IndexError", 5) == (
        "Exhibit A: IndexError was spotted 5 times "
        "at the scene of the bug!"
    )


def test_two_occurrences():
    """Two is the first count that should use plural wording."""
    assert present_evidence("SyntaxError", 2) == (
        "Exhibit A: SyntaxError was spotted 2 times "
        "at the scene of the bug!"
    )


def test_unknown_error_name():
    """Custom error names should work without special configuration."""
    assert present_evidence("MyCustomError", 1) == (
        "Exhibit A: MyCustomError was spotted once "
        "at the scene of the bug!"
    )


def test_name_whitespace_is_removed():
    """Leading and trailing whitespace should be removed."""
    assert present_evidence("  IndexError \n", 1) == (
        "Exhibit A: IndexError was spotted once "
        "at the scene of the bug!"
    )


@pytest.mark.parametrize("error_name", ["", "   ", "\t\n", None, 42, True])
def test_invalid_error_name(error_name):
    """Blank names and non-string names should raise ValueError."""
    with pytest.raises(ValueError, match="error_name must be a non-empty string"):
        present_evidence(error_name, 1)


@pytest.mark.parametrize("occurrences", [-1, 1.5, "3", None, True, False])
def test_invalid_occurrences(occurrences):
    """Negative counts and non-integer counts should raise ValueError."""
    with pytest.raises(
        ValueError,
        match="occurrences must be a non-negative integer",
    ):
        present_evidence("IndexError", occurrences)