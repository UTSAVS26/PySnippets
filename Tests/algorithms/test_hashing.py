import unittest
import hashlib

class TestHashing(unittest.TestCase):

    def setUp(self):
        self.data = b"Test Hashing"

    def hash_sha256(self, data):
        return hashlib.sha256(data).hexdigest()

    def hash_sha512(self, data):
        return hashlib.sha512(data).hexdigest()

    def hash_md5(self, data):
        return hashlib.md5(data).hexdigest()

    def test_sha256_hash(self):
        expected_hash = "66c2e9b4e7498b8d6cf7e66a46076e1e7e580edb3751188bb0d4d26ef3a30282"
        self.assertEqual(self.hash_sha256(self.data), expected_hash)

    def test_sha512_hash(self):
        expected_hash = "f4a3cb8baf45bc5e3cf165f53e80dc3bc98b54bbd2564d8e4c9fa1182da03a58a5b15edbffaf02560236fcd254a8282480f4fbdcd914a8a4ab6b38d7bb9e733a"
        self.assertEqual(self.hash_sha512(self.data), expected_hash)

    def test_md5_hash(self):
        expected_hash = "dd2a1abbe8a03437ec42ec95f74a9ee3"
        self.assertEqual(self.hash_md5(self.data), expected_hash)

if __name__ == '__main__':
    unittest.main()
