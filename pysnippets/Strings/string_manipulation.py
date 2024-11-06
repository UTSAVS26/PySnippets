# string_manipulation.py

from typing import List, Dict

def reverse_string(s: str) -> str:
    """Returns the reversed version of the input string."""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Returns the count of vowels (a, e, i, o, u) in the input string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def to_uppercase(s: str) -> str:
    """Converts the input string to uppercase."""
    return s.upper()

def to_lowercase(s: str) -> str:
    """Converts the input string to lowercase."""
    return s.lower()

def is_palindrome(s: str) -> bool:
    """Checks if the input string is a palindrome, ignoring spaces, punctuation, and case."""
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def swap_case(s: str) -> str:
    """Swaps the case of all characters (upper to lower and vice versa)."""
    return s.swapcase()

def replace_substring(s: str, old: str, new: str) -> str:
    """Replaces all occurrences of the old substring with the new substring."""
    return s.replace(old, new)

def split_string(s: str, delimiter: str) -> List[str]:
    """Splits a string into a list of substrings based on a delimiter."""
    return s.split(delimiter)

def to_strip(s: str) -> str:
    """Removes leading and trailing whitespace or specified characters."""
    return s.strip()

def to_encode(s: str) -> bytes:
    """Encodes the string into a bytes object using UTF-8 encoding."""
    return s.encode("utf-8")

def to_decode(s: bytes) -> str:
    """Decodes a bytes object back into a string, handling decoding errors."""
    try:
        return s.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError("Failed to decode bytes. Ensure the bytes object is UTF-8 encoded.")

def word_count(s: str) -> Dict[str, int]:
    """Counts the occurrences of each word in the input string."""
    words = s.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

def character_frequency(s: str) -> Dict[str, int]:
    """Returns a dictionary of character frequencies in the input string."""
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def substring_search(s: str, sub: str) -> List[int]:
    """Finds all non-overlapping occurrences of a substring within the input string."""
    indices = []
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            break
        indices.append(start)
        start += len(sub)  # Move past the last found index for non-overlapping search
    return indices

# Example usage of the functions in the script
if __name__ == "__main__":
    sample_string = "A man a plan a canal Panama"
    substring = "a"
    
    print("Original String:", sample_string)
    print("Reversed String:", reverse_string(sample_string))
    print("Vowel Count:", count_vowels(sample_string))
    print("Uppercase:", to_uppercase(sample_string))
    print("Lowercase:", to_lowercase(sample_string))
    print("Is Palindrome?", is_palindrome(sample_string))
    print("Word Count:", word_count(sample_string))
    print("Character Frequency:", character_frequency(sample_string))
    print("Substring Indices for '{}':".format(substring), substring_search(sample_string, substring))