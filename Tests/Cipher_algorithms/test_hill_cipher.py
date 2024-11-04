import unittest
from pysnippets.Cipher_algorithms.hill_cipher import HillCipher

class TestHillCipher(unittest.TestCase):
    def setUp(self):
        self.key_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
        self.cipher = HillCipher(self.key_matrix)

    def test_encrypt(self):
        plaintext = "ACT"
        expected_ciphertext = "POH"
        self.assertEqual(self.cipher.encrypt(plaintext), expected_ciphertext)

    def test_decrypt(self):
        ciphertext = "POH"
        expected_plaintext = "ACT"
        self.assertEqual(self.cipher.decrypt(ciphertext), expected_plaintext)

    def test_invalid_key_matrix(self):
        with self.assertRaises(ValueError):
            HillCipher([[1, 2], [3, 4]])

    def test_invalid_plaintext_length(self):
        with self.assertRaises(ValueError):
            self.cipher.encrypt("ACTG")

    def test_invalid_ciphertext_length(self):
        with self.assertRaises(ValueError):
            self.cipher.decrypt("POHG")

if __name__ == "__main__":
    unittest.main()
