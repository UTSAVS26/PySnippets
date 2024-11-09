import unittest
from validators import PasswordValidator

class TestPasswordValidator(unittest.TestCase):
    def setUp(self):
        self.validator = PasswordValidator()

    def test_validate_success(self):
        self.assertTrue(self.validator.validate("ValidP@ssw0rd"))

    def test_validate_length_failure(self):
        self.assertFalse(self.validator.validate("Short1!"))

    def test_validate_upper_failure(self):
        self.assertFalse(self.validator.validate("lowercase1!"))

    def test_validate_lower_failure(self):
        self.assertFalse("UPPERCASE1!")

    def test_validate_digits_failure(self):
        self.assertFalse(self.validator.validate("NoDigits!@#"))

    def test_validate_symbols_failure(self):
        self.assertFalse(self.validator.validate("NoSymbols123"))

if __name__ == '__main__':
    unittest.main() 