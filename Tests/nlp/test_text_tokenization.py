#test_text_tokenization.py
import unittest
from text_tokenization import text_tokenization

class TestTokenizeText(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(text_tokenization("This is a test"), ["This", "is", "a", "test"])
        self.assertEqual(text_tokenization("Hello world"), ["Hello", "world"])

if __name__ == "__main__":
    unittest.main()
