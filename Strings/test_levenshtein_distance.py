import unittest
from levenshtein_distance import levenshtein_distance

class TestLevenshteinDistance(unittest.TestCase):
    def test_identical_strings(self):
        self.assertEqual(levenshtein_distance("test", "test"), 0)

    def test_empty_strings(self):
        self.assertEqual(levenshtein_distance("", ""), 0)
        self.assertEqual(levenshtein_distance("a", ""), 1)
        self.assertEqual(levenshtein_distance("", "a"), 1)

    def test_different_lengths(self):
        self.assertEqual(levenshtein_distance("short", "longer"), 3)

    def test_case_sensitivity(self):
        self.assertEqual(levenshtein_distance("Kitten", "kitten"), 1)

    def test_non_alphabetic_characters(self):
        self.assertEqual(levenshtein_distance("hello!", "hello"), 1)

if __name__ == "__main__":
    unittest.main() 