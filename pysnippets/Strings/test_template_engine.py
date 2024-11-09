import unittest
from template_engine import substitute_template

class TestTemplateEngine(unittest.TestCase):
    def test_standard_substitution(self):
        template = "Hello, {name}!"
        substitutions = {"name": "Bob"}
        self.assertEqual(substitute_template(template, substitutions), "Hello, Bob!")

    def test_missing_substitution(self):
        template = "Hello, {name}! Welcome to {place}."
        substitutions = {"name": "Alice"}
        self.assertEqual(substitute_template(template, substitutions), "Hello, Alice! Welcome to {place}.")

    def test_extra_substitutions(self):
        template = "Hello, {name}!"
        substitutions = {"name": "Alice", "place": "Wonderland"}
        self.assertEqual(substitute_template(template, substitutions), "Hello, Alice!")

    def test_no_placeholders(self):
        template = "Hello, World!"
        substitutions = {"name": "Alice"}
        self.assertEqual(substitute_template(template, substitutions), "Hello, World!")

    def test_multiple_occurrences(self):
        template = "{greet}, {name}! {greet} again!"
        substitutions = {"greet": "Hi", "name": "Alice"}
        self.assertEqual(substitute_template(template, substitutions), "Hi, Alice! Hi again!")

    def test_empty_substitutions(self):
        template = "Hello, {name}!"
        substitutions = {}
        self.assertEqual(substitute_template(template, substitutions), "Hello, {name}!")

if __name__ == "__main__":
    unittest.main() 