# test_longest_palindrome.py

import unittest
from Snippets.Strings.longest_palindrome.py import longest_palindrome   # Importing the function from longest_palindrome.py


class TestLongestPalindrome(unittest.TestCase):

    def test_basic_palindromes(self):
        self.assertEqual(longest_palindrome("babad"), "bab")  # or "aba"
        self.assertEqual(longest_palindrome("cbbd"), "bb")
        self.assertEqual(longest_palindrome("racecar"), "racecar")

    def test_single_character(self):
        self.assertEqual(longest_palindrome("a"), "a")
        self.assertEqual(longest_palindrome("z"), "z")

    def test_no_palindrome(self):
        self.assertEqual(longest_palindrome("abcd"), "a")  # In this case, return the first character
        self.assertEqual(longest_palindrome("xyz"), "x")

    def test_entire_string_palindrome(self):
        self.assertEqual(longest_palindrome("madam"), "madam")
        self.assertEqual(longest_palindrome("noon"), "noon")

    def test_empty_string(self):
        self.assertEqual(longest_palindrome(""), "")

    def test_long_string(self):
        s = "forgeeksskeegfor"
        self.assertEqual(longest_palindrome(s), "geeksskeeg")

    def test_palindrome_with_spaces(self):
        self.assertEqual(longest_palindrome("a man a plan a canal panama"), "a man a plan a canal panama")

    def test_palindrome_with_special_characters(self):
        self.assertEqual(longest_palindrome("A!bb!A"), "A!bb!A")


if __name__ == "__main__":
    unittest.main()
