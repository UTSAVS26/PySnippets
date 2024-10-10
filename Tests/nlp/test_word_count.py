#test_word_count.py

import unittest
from word_count import word_count

class TestWordCount(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("This is a test"), 4)
        self.assertEqual(word_count("Hello world"), 2)

if __name__ == "__main__":
    unittest.main()
