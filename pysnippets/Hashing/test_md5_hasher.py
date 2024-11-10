import unittest
from md5_hasher import MD5Hasher

class TestMD5Hasher(unittest.TestCase):
    def test_hash_normal_string(self):
        hasher = MD5Hasher(data="Hello, World!")
        self.assertEqual(hasher.hash(), "fc3ff98e8c6a0d3087d515c0473f8677")

    def test_hash_empty_string(self):
        hasher = MD5Hasher(data="")
        self.assertEqual(hasher.hash(), "d41d8cd98f00b204e9800998ecf8427e")

    def test_hash_unicode_string(self):
        hasher = MD5Hasher(data="こんにちは")
        self.assertEqual(hasher.hash(), "9d735278cfbdb946834416adfb5aaf6c")

if __name__ == "__main__":
    unittest.main() 