"""Unit tests for courtroom charge generation."""

import pytest

from rubber_duck_courtroom.charges import file_charge

@pytest.mark.parametrize("severity,classification", [
    (1, "MINOR OFFENCE"),
    (3, "MINOR OFFENCE"),
    (4, "MISDEMEANOR"),
    (7, "MISDEMEANOR"),
    (8, "FELONY"),
    (10, "FELONY"),
])
def test_severity_boundaries(severity, classification):
    output = file_charge("SyntaxError", severity)

    assert classification in output
    assert "SyntaxError" in output
    assert f"Severity: {severity}/10" in output


@pytest.mark.parametrize("error_name,crime", [
    ("ZeroDivisionError", "illegal mathematical operations"),
    ("SyntaxError", "Python grammar"),
    ("TypeError", "incompatible data types"),
    ("IndexError", "permitted list boundaries"),
])
def test_known_errors(error_name, crime):
    output = file_charge(error_name, 5)

    assert error_name in output
    assert crime in output


def test_unknown_error():
    output = file_charge("MyCustomError", 8)

    assert "MyCustomError" in output
    assert "disturbing the peace of the codebase" in output


def test_trims_whitespace():
    output = file_charge("  TypeError  ", 5)

    assert "TypeError" in output
    assert "  TypeError  " not in output


def test_returns_string():
    assert isinstance(file_charge("IndexError", 2), str)


def test_deterministic():
    assert file_charge("IndexError", 3) == file_charge("IndexError", 3)


@pytest.mark.parametrize("invalid_name", [
    "", "   ", None, 123
])
def test_invalid_error_name(invalid_name):
    with pytest.raises(
        ValueError, match="error_name must be a non-empty string"
    ):
        file_charge(invalid_name, 5)


@pytest.mark.parametrize("invalid_severity", [
    0, -1, 11, True, "5", 5.0, None
])
def test_invalid_severity(invalid_severity):
    with pytest.raises(
        ValueError,
        match="severity must be an integer between 1 and 10",
    ):
        file_charge("SyntaxError", invalid_severity)