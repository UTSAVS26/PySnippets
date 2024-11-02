import unittest
from pysnippets.Cipher_algorithms.playfair_cipher import playfair_encrypt, playfair_decrypt

class TestPlayfairCipher(unittest.TestCase):

    def test_playfair_encrypt(self):
        self.assertEqual(playfair_encrypt("HELLO", "KEYWORD"), "RIJVS")
        self.assertEqual(playfair_encrypt("PLAYFAIR", "KEYWORD"), "RLBMZIXR")
        self.assertEqual(playfair_encrypt("HACKTOBERFEST", "KEYWORD"), "RIBKZQKZBFXZ")

    def test_playfair_decrypt(self):
        self.assertEqual(playfair_decrypt("RIJVS", "KEYWORD"), "HELXLO")
        self.assertEqual(playfair_decrypt("RLBMZIXR", "KEYWORD"), "PLAYFAIR")
        self.assertEqual(playfair_decrypt("RIBKZQKZBFXZ", "KEYWORD"), "HACKTOBERFEST")

if __name__ == '__main__':
    unittest.main()
