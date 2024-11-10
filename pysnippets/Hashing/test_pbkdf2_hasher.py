import unittest
import os
from pbkdf2_hasher import PBKDF2Hasher
import hashlib

class TestPBKDF2Hasher(unittest.TestCase):
    def test_hash_password_default(self):
        salt = b'salt123456789012'
        hasher = PBKDF2Hasher(password="password", salt=salt)
        expected = hashlib.pbkdf2_hmac('sha256', b'password', salt, 100000, 32)
        self.assertEqual(hasher.hash_password(), expected)

    def test_hash_password_custom_iterations(self):
        salt = b'salt123456789012'
        hasher = PBKDF2Hasher(password="password", salt=salt, iterations=200000)
        expected = hashlib.pbkdf2_hmac('sha256', b'password', salt, 200000, 32)
        self.assertEqual(hasher.hash_password(), expected)

    def test_hash_password_invalid_salt(self):
        with self.assertRaises(AttributeError):
            PBKDF2Hasher(password="password", salt="not_bytes").hash_password()

if __name__ == "__main__":
    unittest.main() 