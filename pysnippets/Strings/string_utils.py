import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class StringUtils:
    text: str

    def __post_init__(self):
        if not isinstance(self.text, str):
            raise ValueError("Text must be a string.")

    def reverse_string(self) -> str:
        return self.text[::-1]

    def count_vowels(self) -> int:
        vowels = 'aeiouAEIOU'
        return sum(1 for char in self.text if char in vowels)

    def is_palindrome(self) -> bool:
        sanitized = ''.join(filter(str.isalnum, self.text)).lower()
        return sanitized == sanitized[::-1]

    def to_uppercase(self) -> str:
        return self.text.upper()

    def to_lowercase(self) -> str:
        return self.text.lower()

    def swap_case(self) -> str:
        return self.text.swapcase()

    def capitalize_words(self) -> str:
        return ' '.join(word.capitalize() for word in self.text.split())

    def remove_whitespace(self) -> str:
        return ''.join(self.text.split())

    def replace_substring(self, old: str, new: str) -> str:
        if not isinstance(old, str) or not isinstance(new, str):
            raise ValueError("Both old and new must be strings.")
        return self.text.replace(old, new)

if __name__ == "__main__":
    sample_text = "A man a plan a canal Panama"
    utils = StringUtils(sample_text)
    
    reversed_text = utils.reverse_string()
    logging.info(f"Reversed: {reversed_text}")
    
    vowel_count = utils.count_vowels()
    logging.info(f"Vowel Count: {vowel_count}")
    
    palindrome = utils.is_palindrome()
    logging.info(f"Is Palindrome: {palindrome}")
    
    uppercase = utils.to_uppercase()
    logging.info(f"Uppercase: {uppercase}")
    
    lowercase = utils.to_lowercase()
    logging.info(f"Lowercase: {lowercase}")
    
    swapped = utils.swap_case()
    logging.info(f"Swapped Case: {swapped}")
    
    capitalized = utils.capitalize_words()
    logging.info(f"Capitalized Words: {capitalized}")
    
    no_whitespace = utils.remove_whitespace()
    logging.info(f"Removed Whitespace: {no_whitespace}")
    
    replaced = utils.replace_substring("canal", "river")
    logging.info(f"Replaced Substring: {replaced}") 