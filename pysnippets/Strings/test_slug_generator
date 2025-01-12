import unittest
from slug_generator import generate_slug

class TestGenerateSlug(unittest.TestCase):

    def test_basic_slug(self):
        input_text = "Where to find best cafés in Bhopal?"
        expected = "where-to-find-best-cafes-in-bhopal"
        self.assertEqual(generate_slug(input_text), expected)

    def test_multiple_spaces(self):
        input_text = "Hello    world   how    are    you?"
        expected = "hello-world-how-are-you"
        self.assertEqual(generate_slug(input_text), expected)

    def test_accented_characters(self):
        input_text = "café naïve résumé"
        expected = "cafe-naive-resume"
        self.assertEqual(generate_slug(input_text), expected)

    def test_special_characters(self):
        input_text = "Hello, world! Let's test @ this#"
        expected = "hello-world-lets-test-this"
        self.assertEqual(generate_slug(input_text), expected)

    def test_empty_string(self):
        input_text = ""
        expected = ""
        self.assertEqual(generate_slug(input_text), expected)

    def test_single_word(self):
        input_text = "Python"
        expected = "python"
        self.assertEqual(generate_slug(input_text), expected)

    def test_numeric_characters(self):
        input_text = "Test123 with numbers 456"
        expected = "test123-with-numbers-456"
        self.assertEqual(generate_slug(input_text), expected)

    def test_mixed_input(self):
        input_text = "Welcome to 2025!"
        expected = "welcome-to-2025"
        self.assertEqual(generate_slug(input_text), expected)

    def test_non_string_input(self):
        with self.assertRaises(ValueError):
            generate_slug(12345)  # Integer input

    def test_only_spaces(self):
        input_text = "     "
        expected = ""
        self.assertEqual(generate_slug(input_text), expected)

    def test_leading_trailing_spaces(self):
        input_text = "  Hello World!   "
        expected = "hello-world"
        self.assertEqual(generate_slug(input_text), expected)

    def test_leading_trailing_hyphen(self):
        input_text = "  --hello world--  "
        expected = "hello-world"
        self.assertEqual(generate_slug(input_text), expected)

    def test_large_input(self):
        input_text = " ".join(["word"] * 1000)
        expected = "word-" * 999 + "word"
        self.assertEqual(generate_slug(input_text), expected)

    def test_single_special_character(self):
        input_text = "$"
        expected = ""
        self.assertEqual(generate_slug(input_text), expected)

    def test_mixed_case(self):
        input_text = "PyThOn Is FuN!"
        expected = "python-is-fun"
        self.assertEqual(generate_slug(input_text), expected)

    def test_repeated_hyphens(self):
        input_text = "hello   -- world --"
        expected = "hello-world"
        self.assertEqual(generate_slug(input_text), expected)

if __name__ == '__main__':
    unittest.main()
