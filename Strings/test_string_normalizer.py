import unittest
from string_normalizer import normalize_string

class TestStringNormalizer(unittest.TestCase):
    def test_with_accents(self):
        self.assertEqual(normalize_string("Café"), "Cafe")

    def test_no_accents(self):
        self.assertEqual(normalize_string("Cafe"), "Cafe")

    def test_empty_string(self):
        self.assertEqual(normalize_string(""), "")

    def test_only_accents(self):
        self.assertEqual(normalize_string("àéîõü"), "aeiou")

    def test_mixed_characters(self):
        self.assertEqual(normalize_string("München"), "Munchen")

if __name__ == "__main__":
    unittest.main() 