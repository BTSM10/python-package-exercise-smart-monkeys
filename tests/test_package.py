"""Tests for the package installation."""

import rubber_duck_courtroom


def test_package_imports():
    """Verify the package imports under its expected name."""
    assert rubber_duck_courtroom.__name__ == "rubber_duck_courtroom"