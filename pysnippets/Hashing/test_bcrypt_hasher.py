import unittest
from bcrypt_hasher import BcryptHasher
import bcrypt

class TestBcryptHasher(unittest.TestCase):
    def test_hash_and_check_password(self):
        hasher = BcryptHasher(password="mypassword")
        hashed = hasher.hash_password()
        self.assertTrue(hasher.check_password(hashed))

    def test_check_password_incorrect(self):
        hasher = BcryptHasher(password="mypassword")
        hashed = hasher.hash_password()
        hasher_wrong = BcryptHasher(password="wrongpassword")
        self.assertFalse(hasher_wrong.check_password(hashed))

    def test_hash_with_custom_rounds(self):
        hasher = BcryptHasher(password="mypassword", rounds=14)
        hashed = hasher.hash_password()
        self.assertTrue(hasher.check_password(hashed))
        self.assertTrue(hashed.startswith(b'$2b$14$'))

if __name__ == "__main__":
    unittest.main() 