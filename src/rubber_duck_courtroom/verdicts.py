def deliver_verdict(error_name: str, severity: int) -> str:
    """Deliver a courtroom verdict based on an error's severity.

    Args:
        error_name: Name of the programming error.
        severity: Integer between 1 and 10.

    Returns:
        A humorous verdict describing the error's guilt.

    Raises:
        ValueError: If the arguments are invalid.
    """
    if not isinstance(error_name, str) or not error_name.strip():
        raise ValueError("error_name must be a non-empty string")

    if type(severity) is not int or not 1 <= severity <= 10:
        raise ValueError("severity must be an integer from 1 to 10")

    error_name = error_name.strip()

    if severity <= 3:
        return f"{error_name} receives a WARNING! The duck lets you off easy."

    if severity <= 7:
        return f"GUILTY! {error_name} has disturbed the peace of the codebase."

    return (
        f"GUILTY WITH EXTREME PREJUDICE! "
        f"{error_name} has terrorized the codebase."
    )