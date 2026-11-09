"""Generate charges for fictional Python error trials."""

def file_charge(error_name: str, severity: int) -> str:
    """Return a fictional charge for an error and a severity from 1 to 10.

    Args:
        error_name: Non-empty string with the name of the error.
        severity: Integer from 1 (minor) to 10 (critical).

    Returns:
        A humorous courtroom charge as a string.

    Raises:
        ValueError: If either argument is invalid.
    """
    if not isinstance(error_name, str) or not error_name.strip():
        raise ValueError("error_name must be a non-empty string")

    if type(severity) is not int or not 1 <= severity <= 10:
        raise ValueError("severity must be an integer between 1 and 10")

    error_name = error_name.strip()

    crimes = {
        "ZeroDivisionError": "attempting illegal mathematical operations",
        "SyntaxError": "violating the laws of Python grammar",
        "TypeError": "recklessly mixing incompatible data types",
        "IndexError": "trespassing beyond permitted list boundaries",
    }

    crime = crimes.get(
        error_name,
        "disturbing the peace of the codebase"
    )

    if severity <= 3:
        classification = "MINOR OFFENCE"
    elif severity <= 7:
        classification = "MISDEMEANOR"
    else:
        classification = "FELONY"

    return (
        f"{classification}: {error_name} is charged with {crime}. "
        f"Severity: {severity}/10."
    )