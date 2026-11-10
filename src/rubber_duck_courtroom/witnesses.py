
"""Generate humorous witness testimonies for the Rubber Duck Courtroom."""


def call_witness(witness: str, mood: str) -> str:
    """Generate a courtroom testimony based on the witness and mood.

    Args:
        witness: Name of the witness giving testimony.
        mood: The witness's mood (calm, dramatic, or sarcastic).

    Returns:
        A humorous courtroom testimony.

    Raises:
        ValueError: If either argument is invalid.
    """

    # Validate witness
    if not isinstance(witness, str) or not witness.strip():
        raise ValueError("witness must be a non-empty string")

    # Validate mood
    if not isinstance(mood, str) or mood.strip().lower() not in (
        "calm", "dramatic", "sarcastic"
    ):
        raise ValueError("mood must be calm, dramatic, or sarcastic")

    # Normalize inputs
    witness = witness.strip()
    mood = mood.strip().lower()

    # Generate testimony
    if mood == "dramatic":
        return (
            f"{witness} takes the stand dramatically: "
            "'Your Honor! I have never witnessed such a horrifying bug!'"
        )

    if mood == "calm":
        return (
            f"{witness} calmly addresses the court: "
            "'Your Honor, let us examine the evidence carefully.'"
        )

    return (
        f"{witness} rolls their eyes: "
        "'Oh, wonderful. Another bug. Exactly what we needed.'"
    )
