import unittest
from sha3_hasher import SHA3Hasher
import hashlib

class TestSHA3Hasher(unittest.TestCase):
    def test_hash_sha3_256(self):
        hasher = SHA3Hasher(data="Test Data", variant='sha3_256')
        expected = hashlib.sha3_256(b'Test Data').hexdigest()
        self.assertEqual(hasher.hash_data(), expected)

    def test_hash_sha3_512(self):
        hasher = SHA3Hasher(data="Test Data", variant='sha3_512')
        expected = hashlib.sha3_512(b'Test Data').hexdigest()
        self.assertEqual(hasher.hash_data(), expected)

    def test_invalid_variant(self):
        hasher = SHA3Hasher(data="Test Data", variant='sha3_999')
        with self.assertRaises(AttributeError):
            hasher.hash_data()

if __name__ == "__main__":
    unittest.main() 