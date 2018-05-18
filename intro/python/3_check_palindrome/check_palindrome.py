"""Solution for checkPalindrome."""


def check_palindrome(input: str) -> bool:
    """Check if a given str is a palindrome or not, returning true or false."""
    if input == input[::-1]:
        return True
    return False
