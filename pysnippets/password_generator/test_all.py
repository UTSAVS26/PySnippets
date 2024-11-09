import unittest
from password_generator import PasswordGenerator, PasswordValidator, Hasher

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.pg = PasswordGenerator(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True)

    def test_generate_password_length(self):
        password, _ = self.pg.generate_password()
        self.assertEqual(len(password), 12)

    def test_generate_password_characters(self):
        password, _ = self.pg.generate_password()
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in '!@#$%^&*(),.?":{}|<>' for c in password))

    def test_password_validation_failure(self):
        with self.assertRaises(ValueError):
            pg = PasswordGenerator(use_upper=False, use_lower=False, use_digits=False, use_symbols=False)
            pg.generate_password()

    def test_password_hashing(self):
        password, hashed = self.pg.generate_password()
        self.assertTrue(len(hashed) > 0)
        
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
        self.assertFalse(self.validator.validate("UPPERCASE1!"))

    def test_validate_digits_failure(self):
        self.assertFalse(self.validator.validate("NoDigits!@#"))

    def test_validate_symbols_failure(self):
        self.assertFalse(self.validator.validate("NoSymbols123"))

class TestHasher(unittest.TestCase):
    def setUp(self):
        self.hasher = Hasher()

    def test_hash_and_verify_password(self):
        password = "TestP@ssw0rd!"
        hashed = self.hasher.hash_password(password)
        self.assertTrue(self.hasher.verify_password(password, hashed))

    def test_verify_wrong_password(self):
        password = "TestP@ssw0rd!"
        wrong_password = "WrongP@ssw0rd!"
        hashed = self.hasher.hash_password(password)
        self.assertFalse(self.hasher.verify_password(wrong_password, hashed))

    def test_hash_password_error(self):
        with self.assertRaises(Exception):
            self.hasher.hash_password(None)

    def test_verify_password_error(self):
        with self.assertRaises(Exception):
            self.hasher.verify_password("password", None)

if __name__ == '__main__':
    unittest.main() 