import unittest
from cipher_manager import (
    encrypt_affine, decrypt_affine,
    encrypt_caesar, decrypt_caesar,
    encrypt_hill, decrypt_hill,
    encrypt_playfair, decrypt_playfair,
    encrypt_rail_fence, decrypt_rail_fence,
    encrypt_vigenere, decrypt_vigenere
)

class TestCipherManager(unittest.TestCase):

    def test_affine_cipher(self):
        plaintext = "PYSNIPPETS"
        a, b = 5, 8
        ciphertext = encrypt_affine(plaintext, a, b)
        decrypted_text = decrypt_affine(ciphertext, a, b)
        self.assertEqual(decrypted_text, plaintext)

    def test_caesar_cipher(self):
        plaintext = "PYSNIPPETS"
        shift = 3
        ciphertext = encrypt_caesar(plaintext, shift)
        decrypted_text = decrypt_caesar(ciphertext, shift)
        self.assertEqual(decrypted_text, plaintext)

    def test_hill_cipher(self):
        plaintext = "PYSNIP"
        key_matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]  # Example 3x3 matrix
        ciphertext = encrypt_hill(plaintext, key_matrix)
        decrypted_text = decrypt_hill(ciphertext, key_matrix)
        self.assertEqual(decrypted_text, plaintext)

    def test_playfair_cipher(self):
        plaintext = "PYSNIPPETS"
        key = "KEYWORD"
        ciphertext = encrypt_playfair(plaintext, key)
        decrypted_text = decrypt_playfair(ciphertext, key)
        self.assertEqual(decrypted_text, plaintext)

    def test_rail_fence_cipher(self):
        plaintext = "PYSNIPPETS"
        key = 3
        ciphertext = encrypt_rail_fence(plaintext, key)
        decrypted_text = decrypt_rail_fence(ciphertext, key)
        self.assertEqual(decrypted_text, plaintext)

    def test_vigenere_cipher(self):
        plaintext = "PYSNIPPETS"
        key = "KEY"
        ciphertext = encrypt_vigenere(plaintext, key)
        decrypted_text = decrypt_vigenere(ciphertext, key)
        self.assertEqual(decrypted_text, plaintext)

if __name__ == "__main__":
    unittest.main() 