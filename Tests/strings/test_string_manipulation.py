# test_string_manipulation.py
import unittest
from pysnippets.strings.string_manipulation import (
    reverse_string,
    count_vowels,
    to_uppercase,
    to_lowercase,
    is_palindrome,
    word_count,
    character_frequency,
    substring_search,
)

class TestStringManipulation(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("Python"), "PYTHON")

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")
        self.assertEqual(to_lowercase("Python"), "python")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("No lemon, no melon"))

    def test_word_count(self):
        self.assertEqual(word_count("hello world"), 2)
        self.assertEqual(word_count("Python is great"), 3)
        self.assertEqual(word_count(""), 0)

    def test_character_frequency(self):
        self.assertEqual(character_frequency("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(character_frequency("Python"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1})

    def test_substring_search(self):
        self.assertTrue(substring_search("hello world", "world"))
        self.assertFalse(substring_search("hello world", "Python"))
        self.assertTrue(substring_search("hello", "hello"))

if __name__ == "__main__":
    unittest.main()

