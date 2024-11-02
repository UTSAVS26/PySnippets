import unittest
from ...pysnippets.Cipher_algorithms.Vigenère_Cipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher("LEMON")

    def test_encrypt(self):
        plaintext = "ATTACK AT DAWN"
        expected_ciphertext = "LXFOPV EF RNHR"
        self.assertEqual(self.cipher.encrypt(plaintext), expected_ciphertext)

    def test_decrypt(self):
        ciphertext = "LXFOPV EF RNHR"
        expected_plaintext = "ATTACKATDAWN"
        self.assertEqual(self.cipher.decrypt(ciphertext), expected_plaintext)

    def test_non_alpha_key(self):
        with self.assertRaises(ValueError):
            VigenereCipher("LEMON123")

    def test_empty_string(self):
        self.assertEqual(self.cipher.encrypt(""), "")
        self.assertEqual(self.cipher.decrypt(""), "")

    def test_case_insensitivity(self):
        plaintext = "attack at dawn"
        expected_ciphertext = "LXFOPV EF RNHR"
        self.assertEqual(self.cipher.encrypt(plaintext), expected_ciphertext)

    def test_special_characters_in_plaintext(self):
        plaintext = "ATTACK! AT DAWN."
        expected_ciphertext = "LXFOPV EF RNHR"
        self.assertEqual(self.cipher.encrypt(plaintext), expected_ciphertext)

if __name__ == "__main__":
    unittest.main()
