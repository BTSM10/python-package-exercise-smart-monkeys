"""Generate humorous witness testimonies for the Rubber Duck Courtroom."""


def call_witness(witness: str, mood: str) -> str:
    """Generate a courtroom testimony based on the witness and mood.

    Args:
        witness: Name of the witness giving testimony.
        mood: The witness's mood (dramatic, angry, or sarcastic).

    Returns:
        A humorous courtroom testimony.

    Raises:
        ValueError: If either argument is invalid.
    """

    # 1. Validate the witness name
    if not isinstance(witness, str) or not witness.strip():
        raise ValueError("witness must be a non-empty string")

    # 2. Validate the mood
    if not isinstance(mood, str) or mood.strip().lower() not in (
        "dramatic", "angry", "sarcastic"
    ):
        raise ValueError("mood must be dramatic, angry, or sarcastic")

    # 3. Normalize the inputs
    witness = witness.strip()
    mood = mood.strip().lower()
        # 4. Generate testimony based on the witness's mood
    if mood == "dramatic":
        return (
            f"{witness} takes the stand dramatically: "
            "'Your Honor! I have never witnessed such a horrifying bug!'"
        )

    if mood == "angry":
        return (
            f"{witness} slams the witness stand: "
            "'This bug has wasted enough of my time! I demand justice!'"
        )

    # The remaining supported mood is sarcastic
    return (
        f"{witness} rolls their eyes: "
        "'Oh, wonderful. Another bug. Exactly what we needed.'"
    )