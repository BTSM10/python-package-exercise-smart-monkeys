import pytest

from rubber_duck_courtroom.sentences import issue_sentence


@pytest.mark.parametrize("severity", [1, 2, 3])
def test_warning(severity):
    result = issue_sentence("SyntaxError", severity)
    assert "SyntaxError" in result
    assert "formal warning" in result
    assert "hours" not in result


@pytest.mark.parametrize("severity, hours", [(4, 8), (5, 10), (6, 12), (7, 14)])
def test_refactoring(severity, hours):
    result = issue_sentence("TypeError", severity)
    assert "TypeError" in result
    assert f"{hours} hours of refactoring" in result
    assert "debugging" not in result


@pytest.mark.parametrize("severity, hours", [(8, 24), (9, 27), (10, 30)])
def test_debugging(severity, hours):
    result = issue_sentence("ZeroDivisionError", severity)
    assert "ZeroDivisionError" in result
    assert f"{hours} hours of supervised debugging" in result
    assert "refactoring" not in result


@pytest.mark.parametrize("severity", [2, 5, 9])
def test_custom_error(severity):
    result = issue_sentence("MyCustomError", severity)
    assert isinstance(result, str)
    assert "MyCustomError" in result
    assert result == issue_sentence("MyCustomError", severity)


@pytest.mark.parametrize("severity", [2, 5, 9])
def test_whitespace_in_name(severity):
    assert issue_sentence(" \tInfinite loop\n", severity) == issue_sentence(
        "Infinite loop", severity
    )


@pytest.mark.parametrize("error_name", ["", "   ", "\t\n", None, 42, True, [], {}])
def test_invalid_name(error_name):
    with pytest.raises(ValueError, match="error_name must be a non-empty string"):
        issue_sentence(error_name, 5)


@pytest.mark.parametrize(
    "severity", [0, -1, 11, 100, True, False, 5.0, "5", None, [], {}]
)
def test_invalid_severity(severity):
    with pytest.raises(ValueError, match="severity must be an integer from 1 to 10"):
        issue_sentence("TypeError", severity)
