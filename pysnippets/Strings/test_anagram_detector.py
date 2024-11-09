import unittest
from anagram_detector import are_anagrams

class TestAnagramDetector(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(are_anagrams("Listen", "Silent"))

    def test_not_anagrams(self):
        self.assertFalse(are_anagrams("Hello", "World"))

    def test_different_lengths(self):
        self.assertFalse(are_anagrams("test", "testing"))

    def test_with_spaces(self):
        self.assertTrue(are_anagrams("conversation", "voices rant on"))

    def test_case_insensitivity(self):
        self.assertTrue(are_anagrams("Dormitory", "Dirty room"))

    def test_special_characters(self):
        self.assertTrue(are_anagrams("A gentleman", "Elegant man"))
        self.assertFalse(are_anagrams("Clint Eastwood", "Old West Action!"))

if __name__ == "__main__":
    unittest.main() 