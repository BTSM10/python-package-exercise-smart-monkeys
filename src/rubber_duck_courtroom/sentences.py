def issue_sentence(error_name: str, severity: int) -> str:
    if not isinstance(error_name, str) or not error_name.strip():
        raise ValueError("error_name must be a non-empty string")
    if type(severity) is not int or not 1 <= severity <= 10:
        raise ValueError("severity must be an integer from 1 to 10")

    error_name = error_name.strip()

    if severity <= 3:
        return f"{error_name} receives a formal warning. The duck is watching you!"
    if severity <= 7:
        return f"{error_name} is sentenced to {severity * 2} hours of refactoring!"
    return f"{error_name} is sentenced to {severity * 3} hours of supervised debugging!"
