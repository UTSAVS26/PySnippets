import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from pysnippets.Cipher_algorithms.caesar_cipher import CaesarCipher

class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher()
    
    def test_default_encryption(self):
        message = "Hello, World!"
        expected = "Khoor, Zruog!"
        self.assertEqual(self.cipher.encrypt(message), expected)
    
    def test_default_decryption(self):
        encrypted = "Khoor, Zruog!"
        expected = "Hello, World!"
        self.assertEqual(self.cipher.decrypt(encrypted), expected)
    
    def test_custom_shift(self):
        custom_cipher = CaesarCipher(shift=5)
        message = "Python Programming"
        encrypted = custom_cipher.encrypt(message)
        decrypted = custom_cipher.decrypt(encrypted)
        self.assertEqual(decrypted, message)
    
    def test_non_alphabetic_characters(self):
        message = "Hello, World! 123"
        encrypted = self.cipher.encrypt(message)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(message, decrypted)
    
    def test_brute_force_decryption(self):
        message = "Hello, World!"
        encrypted = self.cipher.encrypt(message)
        decryptions = self.cipher.brute_force_decrypt(encrypted)
        found_decryption = any(
            decryption == message for _, decryption in decryptions
        )
        self.assertTrue(found_decryption)
    
    def test_full_cycle(self):
        message = "The quick brown fox jumps over the lazy dog!"
        encrypted = self.cipher.encrypt(message)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(message, decrypted)
    
    def test_empty_string(self):
        message = ""
        encrypted = self.cipher.encrypt(message)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(message, decrypted)
    
    def test_large_shift(self):
        custom_cipher = CaesarCipher(shift=30)
        message = "Large Shift"
        encrypted = custom_cipher.encrypt(message)
        decrypted = custom_cipher.decrypt(encrypted)
        self.assertEqual(decrypted, message)
    
    def test_negative_shift(self):
        custom_cipher = CaesarCipher(shift=-3)
        message = "Negative Shift"
        encrypted = custom_cipher.encrypt(message)
        decrypted = custom_cipher.decrypt(encrypted)
        self.assertEqual(decrypted, message)
    
    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            self.cipher.encrypt(12345)
        with self.assertRaises(TypeError):
            self.cipher.decrypt(12345)
