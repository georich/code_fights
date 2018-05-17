def check_palindrome(input):
    if input == input[::-1]:
        return True
    return False


word = "aabaa"
print(f"Is {word} a palindrome? {check_palindrome(word)}")
