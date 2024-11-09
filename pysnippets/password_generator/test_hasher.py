import unittest
from hasher import Hasher

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