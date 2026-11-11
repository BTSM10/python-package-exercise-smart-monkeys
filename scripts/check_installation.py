
"""Verify that both package distributions install and work correctly."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path


# Find the project and its built distribution files.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DIST_DIR = PROJECT_ROOT / "dist"

# Run these checks in a fresh environment after installation.
SMOKE_TEST = """
from rubber_duck_courtroom import (
    file_charge,
    present_evidence,
    call_witness,
    deliver_verdict,
    issue_sentence,
)

results = [
    file_charge("SyntaxError", 8),
    present_evidence("SyntaxError", 3),
    call_witness("GitHub", "calm"),
    deliver_verdict("SyntaxError", 8),
    issue_sentence("SyntaxError", 8),
]

assert len(results) == 5
assert all(isinstance(result, str) and result for result in results)
print("PASS: All five functions work!")
"""


def check_installation(package_path: Path) -> None:
    """Install and test a package in a fresh virtual environment."""

    print(f"\nTesting: {package_path.name}", flush=True)

    # A temporary directory prevents interference with the project.
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        venv_path = temp_path / "venv"

        # Create a clean Python virtual environment.
        subprocess.run(
            [sys.executable, "-m", "venv", str(venv_path)],
            check=True,
        )

        # Locate Python inside the new environment.
        if os.name == "nt":
            python = venv_path / "Scripts" / "python.exe"
        else:
            python = venv_path / "bin" / "python"

        # Install the actual distribution, not the editable source.
        subprocess.run(
            [
                str(python),
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                "--no-deps",
                str(package_path),
            ],
            cwd=temp_path,
            check=True,
        )

        # Run all five functions outside the repository.
        subprocess.run(
            [str(python), "-c", SMOKE_TEST],
            cwd=temp_path,
            check=True,
        )

    print(f"PASS: {package_path.name}", flush=True)


def main() -> None:
    """Test both the wheel and source distribution."""

    wheels = list(DIST_DIR.glob("*.whl"))
    source_packages = list(DIST_DIR.glob("*.tar.gz"))

    if len(wheels) != 1 or len(source_packages) != 1:
        raise RuntimeError(
            "Expected exactly one wheel and one source distribution. "
            "Build the package in a clean dist directory first."
        )

    check_installation(wheels[0])
    check_installation(source_packages[0])

    print("\nSUCCESS: Both package installations passed!", flush=True)


if __name__ == "__main__":
    main()
