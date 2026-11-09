"""Generate courtroom evidence reports for programming errors."""


def present_evidence(error_name: str, occurrences: int) -> str:
    """Return a humorous evidence report.

    Args:
        error_name: A nonempty error name.
        occurrences: A nonnegative integer count.

    Returns:
        An evidence statement for zero, one, or multiple occurrences.

    Raises:
        ValueError: If either argument is invalid.
    """
    if not isinstance(error_name, str) or not error_name.strip():
        raise ValueError("error_name must be a non-empty string")

    if type(occurrences) is not int or occurrences < 0:
        raise ValueError("occurrences must be a non-negative integer")

    error_name = error_name.strip()

    if occurrences == 0:
        return (
            f"No evidence found against {error_name}. "
            "The duck demands better detective work!"
        )

    if occurrences == 1:
        return (
            f"Exhibit A: {error_name} was spotted once "
            "at the scene of the bug!"
        )

    return (
        f"Exhibit A: {error_name} was spotted {occurrences} times "
        "at the scene of the bug!"
    )