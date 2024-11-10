import unittest
from Capitalization import capitalize_each_word, title_case, alternate_capitalization, random_capitalization

class TestCapitalizationMethods(unittest.TestCase):

    def test_capitalize_each_word(self):
        self.assertEqual(capitalize_each_word("hello world"), "Hello World")
        self.assertEqual(capitalize_each_word("a quick brown fox"), "A Quick Brown Fox")

    def test_title_case(self):
        self.assertEqual(title_case("the quick brown fox jumps over the lazy dog"), 
                         "The Quick Brown Fox Jumps Over the Lazy Dog")
        self.assertEqual(title_case("to be or not to be"), "To Be or Not to Be")

    def test_alternate_capitalization(self):
        self.assertEqual(alternate_capitalization("hello"), "HeLlO")
        self.assertEqual(alternate_capitalization("python"), "PyThOn")

    def test_random_capitalization(self):
        result = random_capitalization("hello world")
        self.assertEqual(len(result), len("hello world"))
        self.assertTrue(all(c.isalpha() or c.isspace() for c in result))

if __name__ == "__main__":
    unittest.main()
