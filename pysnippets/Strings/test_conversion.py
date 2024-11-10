import unittest
from basic_conversion import number_to_words_basic, words_to_number_basic
from regex import number_to_words_regex, words_to_number_regex
from dict_conversion import number_to_words_advanced, words_to_number_advanced
from inflect_conversion import number_to_words_inflect, words_to_number_inflect

class TestNumberWordConversions(unittest.TestCase):

    def test_basic_conversion(self):
        self.assertEqual(number_to_words_basic("123"), "one two three")
        self.assertEqual(words_to_number_basic("one two three"), "123")

    def test_regex_conversion(self):
        self.assertEqual(number_to_words_regex("I have 2 apples"), "I have two apples")
        self.assertEqual(words_to_number_regex("I have two apples"), "I have 2 apples")

    def test_advanced_dict_conversion(self):
        self.assertEqual(number_to_words_advanced(42), "forty-two")
        self.assertEqual(words_to_number_advanced("forty-two"), 42)

    def test_inflect_conversion(self):
        self.assertEqual(number_to_words_inflect(99), "ninety-nine")
        self.assertEqual(words_to_number_inflect("ninety-nine"), 99, "words_to_number_inflect returned None instead of 99")

if __name__ == "__main__":
    unittest.main()
