# test_sentiment_analysis_simple.py

import unittest
from sentiment_analysis_simple import sentiment_analysis_simple

class TestAnalyzeSentiment(unittest.TestCase):
    def test_positive_sentiment(self):
        self.assertEqual(sentiment_analysis_simple("I love this!"), "Positive")

    def test_negative_sentiment(self):
        self.assertEqual(sentiment_analysis_simple("I hate this"), "Negative")

    def test_neutral_sentiment(self):
        self.assertEqual(sentiment_analysis_simple("This is a book"), "Neutral")

if __name__ == "__main__":
    unittest.main()
