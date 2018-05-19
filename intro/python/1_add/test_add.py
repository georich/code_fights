"""Test file for python add."""
from add import add


class TestAdd:
    """Test the add() function."""

    def test_add_positive(self):
        """Make sure adding two positive integers gives the correct result."""
        assert (add(2, 4)) == 6

    def test_add_negative(self):
        """Make sure adding two negative integers gives the correct result."""
        assert (add(-2, -8)) == -10

    def test_mixed_signs(self):
        """Make sure adding mixed integers gives correct result."""
        assert (add(-50, 100)) == 50
