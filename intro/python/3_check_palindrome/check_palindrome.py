"""Solution for checkPalindrome."""


def check_palindrome(input_string: str) -> bool:
    """Check if a given str is a palindrome or not, returning true or false."""
    if input_string == input_string[::-1]:
        return True
    return False
