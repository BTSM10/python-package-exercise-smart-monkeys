
"""Tests for the public Rubber Duck Courtroom API."""

import pytest
import rubber_duck_courtroom as courtroom

from rubber_duck_courtroom import (
    file_charge,
    present_evidence,
    call_witness,
    deliver_verdict,
    issue_sentence,
)


def test_all_functions_are_importable():
    assert callable(file_charge)
    assert callable(present_evidence)
    assert callable(call_witness)
    assert callable(deliver_verdict)
    assert callable(issue_sentence)


def test_public_api_returns_strings():
    assert isinstance(file_charge("SyntaxError", 5), str)
    assert isinstance(present_evidence("IndexError", 3), str)
    assert isinstance(call_witness("Compiler", "dramatic"), str)
    assert isinstance(deliver_verdict("TypeError", 7), str)
    assert isinstance(issue_sentence("TypeError", 7), str)


@pytest.mark.parametrize(
    "name, args",
    [
        ("file_charge", ("TypeError", 5)),
        ("present_evidence", ("TypeError", 1)),
        ("call_witness", ("Compiler", "calm")),
        ("deliver_verdict", ("TypeError", 5)),
        ("issue_sentence", ("TypeError", 5)),
    ],
)
def test_functions_are_available_from_package(name, args):
    """Verify each public function is exported and returns nonempty text."""
    function = getattr(courtroom, name)

    assert name in courtroom.__all__
    assert callable(function)

    result = function(*args)
    assert isinstance(result, str)
    assert result
