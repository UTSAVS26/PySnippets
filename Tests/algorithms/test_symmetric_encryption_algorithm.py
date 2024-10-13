import unittest
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

class TestAES(unittest.TestCase):

    def setUp(self):
        self.key = os.urandom(32)  # AES-256 key
        self.data = b"Test AES Encryption and Decryption"

    def pad(self, data):
        padder = padding.PKCS7(128).padder()
        return padder.update(data) + padder.finalize()

    def unpad(self, data):
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(data) + unpadder.finalize()

    def encrypt(self, data):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = self.pad(data)
        return iv + encryptor.update(padded_data) + encryptor.finalize()

    def decrypt(self, ciphertext):
        iv = ciphertext[:16]
        actual_ciphertext = ciphertext[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
        return self.unpad(padded_data)

    def test_aes_encryption_decryption(self):
        encrypted_data = self.encrypt(self.data)
        decrypted_data = self.decrypt(encrypted_data)
        self.assertEqual(decrypted_data, self.data)  # Check if decrypted data matches original

if __name__ == '__main__':
    unittest.main()
