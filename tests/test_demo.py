from pathlib import Path
import runpy
import subprocess
import sys

import pytest

from rubber_duck_courtroom import (
    file_charge,
    present_evidence,
    call_witness,
    deliver_verdict,
    issue_sentence,
)


DEMO = Path(__file__).resolve().parents[1] / "examples" / "demo.py"


@pytest.fixture
def demo():
    # Load the example without calling main, so each test can choose its own case.
    return runpy.run_path(str(DEMO))


def test_loading_demo_does_not_print(demo, capsys):
    assert callable(demo["run_case"])
    assert callable(demo["main"])
    assert capsys.readouterr().out == ""


def test_case_uses_all_five_functions_in_order(demo, capsys):
    result = demo["run_case"]("ZeroDivisionError", 8, 3, "Compiler", "dramatic")
    lines = capsys.readouterr().out.splitlines()
    # Compare the demo with the real functions, rather than copying their jokes here.
    expected = [
        ("CHARGES FILED", file_charge("ZeroDivisionError", 8)),
        ("EVIDENCE PRESENTED", present_evidence("ZeroDivisionError", 3)),
        ("WITNESS TESTIMONY", call_witness("Compiler", "dramatic")),
        ("VERDICT", deliver_verdict("ZeroDivisionError", 8)),
        ("SENTENCE", issue_sentence("ZeroDivisionError", 8)),
    ]
    positions = []
    for heading, statement in expected:
        assert lines.count(heading) == 1
        position = lines.index(heading)
        assert lines[position + 1] == statement
        positions.append(position)

    assert positions == sorted(positions)
    assert lines[0] == "RUBBER DUCK COURTROOM"
    assert lines[-2] == "CASE CLOSED"
    assert result is None


@pytest.mark.parametrize(
    "severity, verdict, sentence",
    [
        (1, "WARNING!", "formal warning"),
        (3, "WARNING!", "formal warning"),
        (4, "GUILTY!", "8 hours of refactoring"),
        (7, "GUILTY!", "14 hours of refactoring"),
        (8, "GUILTY WITH EXTREME PREJUDICE!", "24 hours of supervised debugging"),
        (10, "GUILTY WITH EXTREME PREJUDICE!", "30 hours of supervised debugging"),
    ],
)
def test_verdict_and_sentence_agree(demo, capsys, severity, verdict, sentence):
    # Check both ends of each tier. A mismatch is easiest to miss at 3/4 or 7/8.
    demo["run_case"]("CustomError", severity, 1, "Debugger", "calm")
    output = capsys.readouterr().out
    assert verdict in output
    assert sentence in output
    assert "CustomError" in output


@pytest.mark.parametrize(
    "args",
    [
        ("", 5, 1, "Compiler", "calm"),
        ("TypeError", 11, 1, "Compiler", "calm"),
        ("TypeError", True, 1, "Compiler", "calm"),
        ("TypeError", 5, -1, "Compiler", "calm"),
        ("TypeError", 5, 1, "", "calm"),
        ("TypeError", 5, 1, "Compiler", "sleepy"),
    ],
)
def test_invalid_case_does_not_print_partial_output(demo, capsys, args):
    with pytest.raises(ValueError):
        demo["run_case"](*args)
    assert capsys.readouterr().out == ""


def test_main_shows_all_three_tiers(demo, capsys):
    demo["main"]()
    output = capsys.readouterr().out
    assert output.count("RUBBER DUCK COURTROOM") == 3
    assert output.count("CASE CLOSED") == 3
    assert "formal warning" in output
    assert "10 hours of refactoring" in output
    assert "24 hours of supervised debugging" in output
    assert "No evidence found" in output
    assert "spotted once" in output
    assert "spotted 3 times" in output
    assert "calmly addresses" in output
    assert "rolls their eyes" in output
    assert "takes the stand dramatically" in output


def test_main_is_repeatable(demo, capsys):
    demo["main"]()
    first_run = capsys.readouterr().out
    demo["main"]()
    assert capsys.readouterr().out == first_run


def test_demo_runs_as_a_script(tmp_path):
    # Use the same Python as pytest, but a different working directory.
    # This checks the installed package, not an accidental import from the repo root.
    result = subprocess.run(
        [sys.executable, "-I", str(DEMO)],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    assert result.stdout.count("CASE CLOSED") == 3
