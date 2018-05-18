"""Test file for python checkPalindrome."""
import pytest
from check_palindrome import check_palindrome


class TestPalindrome:
    """Test the check_palindrome() function."""

    def test_palindrome(self):
        """Test a palindrome returns true."""
        word = "aabaa"
        assert check_palindrome(word)

    def test_non_palindrome(self):
        """Test a word which isn't a palindrome returns false."""
        word = "asdkaoskgo"
        assert not check_palindrome(word)
