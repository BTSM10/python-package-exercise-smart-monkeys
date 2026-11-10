"""A humorous courtroom where Python errors go on trial."""

# The demo can import from the package without knowing each module's filename.
from .charges import file_charge
from .evidence import present_evidence
from .witnesses import call_witness
from .verdicts import deliver_verdict
from .sentences import issue_sentence

__all__ = [
    "file_charge",
    "present_evidence",
    "call_witness",
    "deliver_verdict",
    "issue_sentence",
]
