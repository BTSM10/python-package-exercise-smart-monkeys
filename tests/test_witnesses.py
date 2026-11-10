
"""Tests for courtroom witness testimonies."""

import pytest

from rubber_duck_courtroom.witnesses import call_witness


def test_dramatic_witness():
    result = call_witness("Stack Overflow", "dramatic")
    assert "Stack Overflow takes the stand dramatically" in result
    assert "horrifying bug" in result


def test_angry_witness():
    result = call_witness("GitHub", "angry")
    assert "GitHub slams the witness stand" in result
    assert "I demand justice!" in result


def test_sarcastic_witness():
    result = call_witness("Python Interpreter", "sarcastic")
    assert "Python Interpreter rolls their eyes" in result
    assert "Another bug" in result


def test_whitespace_and_uppercase():
    result = call_witness("  Stack Overflow  ", " DRAMATIC ")
    assert result.startswith("Stack Overflow takes the stand")


@pytest.mark.parametrize("witness", ["", "   ", None, 42, True])
def test_invalid_witness(witness):
    with pytest.raises(ValueError):
        call_witness(witness, "dramatic")


@pytest.mark.parametrize("mood", ["", "happy", None, 123, True])
def test_invalid_mood(mood):
    with pytest.raises(ValueError):
        call_witness("GitHub", mood)
