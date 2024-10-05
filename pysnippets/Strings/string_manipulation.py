# string_manipulation.py

def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string.
    """
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Returns the count of vowels (a, e, i, o, u) in the input string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def to_uppercase(s: str) -> str:
    """
    Converts the input string to uppercase.
    """
    return s.upper()

def to_lowercase(s: str) -> str:
    """
    Converts the input string to lowercase.
    """
    return s.lower()

def is_palindrome(s: str) -> bool:
    """
    Checks if the input string is a palindrome (reads the same forward and backward).
    """
    s = ''.join(filter(str.isalnum, s)).lower()  # Ignore spaces and case
    return s == s[::-1]

