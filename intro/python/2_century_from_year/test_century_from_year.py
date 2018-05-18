"""Test file for python centuryFromYear."""
import pytest
from century_from_year import century_from_year


class TestCenturyFromYear:
    """Test the century_from_year() function."""

    def test_non_100_divisible(self):
        """Test that a non 100 divisible number gives the correct century."""
        year = 2405
        assert (century_from_year(year)) == 25

    def test_100_divisble(self):
        """Test that a 100 divisble number gives correct century."""
        year = 2000
        assert (century_from_year(year)) == 20
