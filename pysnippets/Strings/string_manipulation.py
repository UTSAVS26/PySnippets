# string_manipulation.py

def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string.

    Example usage:
    reverse_string("hello") -> "olleh"
    """
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Returns the count of vowels (a, e, i, o, u) in the input string.

    Example usage:
    count_vowels("hello") -> 2
    count_vowels("Python") -> 1
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def to_uppercase(s: str) -> str:
    """
    Converts the input string to uppercase.

    Example usage:
    to_uppercase("hello") -> "HELLO"
    """
    return s.upper()

def to_lowercase(s: str) -> str:
    """
    Converts the input string to lowercase.

    Example usage:
    to_lowercase("HELLO") -> "hello"
    """
    return s.lower()

def is_palindrome(s: str) -> bool:
    """
    Checks if the input string is a palindrome (reads the same forward and backward).

    Ignores spaces, punctuation, and case sensitivity.

    Example usage:
    is_palindrome("madam") -> True
    is_palindrome("A man a plan a canal Panama") -> True
    """
    s = ''.join(filter(str.isalnum, s)).lower()  # Ignore spaces, punctuation, and case
    return s == s[::-1]

def word_count(s: str) -> dict:
    """
    Counts the occurrences of each word in the input string.

    Example usage:
    word_count("hello world hello") -> {'hello': 2, 'world': 1}
    """
    words = s.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

def character_frequency(s: str) -> dict:
    """
    Returns a dictionary of character frequencies in the input string.

    Example usage:
    character_frequency("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def substring_search(s: str, sub: str) -> list:
    """
    Finds all occurrences of a substring within the input string.

    Returns a list of starting indices.

    Example usage:
    substring_search("hello world", "o") -> [4, 7]
    """
    indices = []
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            break
        indices.append(start)
        start += 1  # Move past the last found index
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

