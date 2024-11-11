import unittest
from Crypto.Random import get_random_bytes
from encryption import AESCipher

class TestAESCipher(unittest.TestCase):
    def setUp(self):
        self.passphrase = "test_passphrase"
        self.salt = get_random_bytes(16)
        self.key = AESCipher.generate_key(self.passphrase, self.salt)
        self.cipher = AESCipher(self.key)

    def test_encryption_decryption(self):
        original_data = b"Hello, World!"
        encrypted_data = self.cipher.encrypt(original_data)
        decrypted_data = self.cipher.decrypt(encrypted_data)
        self.assertEqual(original_data.decode(), decrypted_data)

    def test_padding_unpadding(self):
        data = b"Hello"
        padded_data = self.cipher.pad(data)
        unpadded_data = self.cipher.unpad(padded_data)
        self.assertEqual(data, unpadded_data)

if __name__ == "__main__":
    unittest.main() 