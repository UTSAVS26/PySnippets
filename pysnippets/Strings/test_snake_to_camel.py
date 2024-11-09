import unittest
from snake_to_camel import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(snake_to_camel("snake_case"), "snakeCase")

    def test_multiple_words(self):
        self.assertEqual(snake_to_camel("convert_snake_case_to_camel"), "convertSnakeCaseToCamel")

    def test_no_underscore(self):
        self.assertEqual(snake_to_camel("snakecase"), "snakecase")

    def test_leading_trailing_underscores(self):
        self.assertEqual(snake_to_camel("_snake_case_"), "snakeCase")

    def test_multiple_consecutive_underscores(self):
        self.assertEqual(snake_to_camel("snake__case"), "snakeCase")

if __name__ == "__main__":
    unittest.main() 