"""Test module."""

from hello_rye import main


def test_main() -> None:
    """Test main function."""
    result = main()
    assert result == 0
