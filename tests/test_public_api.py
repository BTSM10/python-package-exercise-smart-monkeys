"""Tests for the public Rubber Duck Courtroom API."""

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