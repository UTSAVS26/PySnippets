import unittest
from password_generator import PasswordGenerator

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

if __name__ == '__main__':
    unittest.main() 