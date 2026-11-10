import pytest
from rubber_duck_courtroom.verdicts import deliver_verdict


def test_low_severity():
    result = deliver_verdict("SyntaxError", 2)
    assert "WARNING" in result
    assert "SyntaxError" in result


def test_medium_severity():
    result = deliver_verdict("TypeError", 5)
    assert "GUILTY!" in result
    assert "TypeError" in result


def test_high_severity():
    result = deliver_verdict("ZeroDivisionError", 9)
    assert "GUILTY WITH EXTREME PREJUDICE!" in result
    assert "ZeroDivisionError" in result


def test_severity_boundaries():
    assert "WARNING" in deliver_verdict("TypeError", 1)
    assert "WARNING" in deliver_verdict("TypeError", 3)
    assert "GUILTY!" in deliver_verdict("TypeError", 4)
    assert "GUILTY!" in deliver_verdict("TypeError", 7)
    assert "EXTREME PREJUDICE" in deliver_verdict("TypeError", 8)
    assert "EXTREME PREJUDICE" in deliver_verdict("TypeError", 10)


def test_custom_error():
    result = deliver_verdict("MyCustomError", 6)
    assert "MyCustomError" in result


def test_invalid_severity():
    with pytest.raises(ValueError):
        deliver_verdict("TypeError", 0)

    with pytest.raises(ValueError):
        deliver_verdict("TypeError", 11)

    with pytest.raises(ValueError):
        deliver_verdict("TypeError", True)

    with pytest.raises(ValueError):
        deliver_verdict("TypeError", 5.5)


def test_invalid_error_name():
    with pytest.raises(ValueError):
        deliver_verdict("", 5)

    with pytest.raises(ValueError):
        deliver_verdict("   ", 5)

    with pytest.raises(ValueError):
        deliver_verdict(None, 5)


def test_whitespace():
    result = deliver_verdict("  SyntaxError  ", 5)
    assert "SyntaxError" in result
    assert "  SyntaxError  " not in result