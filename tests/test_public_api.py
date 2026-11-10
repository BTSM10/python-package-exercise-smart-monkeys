import pytest

import rubber_duck_courtroom as courtroom


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
    # This is the import style used by the demo and by someone installing our package.
    function = getattr(courtroom, name)
    assert name in courtroom.__all__
    assert callable(function)
    result = function(*args)
    assert isinstance(result, str)
    assert result
