from rubber_duck_courtroom import (
    file_charge,
    present_evidence,
    call_witness,
    deliver_verdict,
    issue_sentence,
)


def run_case(error_name, severity, occurrences, witness, mood):
    """Print one complete case using all five package functions.

    Arguments follow the package's rules. Invalid inputs raise ValueError.
    The output goes to the terminal; this function returns None.
    """
    # Keep the same error and severity throughout, so the verdict and sentence agree.
    # Build the statements first. A bad input should not leave half a trial printed.
    statements = [
        ("CHARGES FILED", file_charge(error_name, severity)),
        ("EVIDENCE PRESENTED", present_evidence(error_name, occurrences)),
        ("WITNESS TESTIMONY", call_witness(witness, mood)),
        ("VERDICT", deliver_verdict(error_name, severity)),
        ("SENTENCE", issue_sentence(error_name, severity)),
    ]

    print("RUBBER DUCK COURTROOM")
    print("=" * 45)
    for heading, statement in statements:
        print(heading)
        print(statement)
        print()
    print("CASE CLOSED")
    print("=" * 45)


def main():
    """Show a warning, a refactoring sentence, and a debugging sentence."""
    # These cases also cover zero, one, and several pieces of evidence.
    # Change the arguments here to try a different case without editing the package.
    run_case("SyntaxError", 2, 0, "Compiler", "calm")
    print()
    run_case("TypeError", 5, 1, "Debugger", "sarcastic")
    print()
    # A made-up error name should work too, not just Python's built-in errors.
    run_case("MyCustomError", 8, 3, "Rubber Duck", "dramatic")


# Importing the example should not start printing trials.
if __name__ == "__main__":
    main()
