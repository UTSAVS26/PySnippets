import unittest
from Crypto.Random import get_random_bytes
from encryption import AESCipher, encrypt_file, encrypt_folder
import os

class TestAESCipher(unittest.TestCase):
    def setUp(self):
        self.key = get_random_bytes(16)
        self.cipher = AESCipher(self.key)
        self.test_data = b"Test data for encryption"
        self.test_file = "test_file.txt"
        self.test_folder = "test_folder"
        
        # Setup test file and folder with data
        os.makedirs(self.test_folder, exist_ok=True)
        with open(self.test_file, 'wb') as f:
            f.write(self.test_data)
        with open(os.path.join(self.test_folder, self.test_file), 'wb') as f:
            f.write(self.test_data)

    def tearDown(self):
        # Cleanup the test file and folder
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_folder):
            for root, _, files in os.walk(self.test_folder):
                for file in files:
                    os.remove(os.path.join(root, file))
            os.rmdir(self.test_folder)

    def test_encrypt_decrypt(self):
        # Test basic encrypt and decrypt functionality
        encrypted = self.cipher.encrypt(self.test_data)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted.encode(), self.test_data)

    def test_encrypt_file(self):
        # Test encryption and decryption of a file
        encrypt_file(self.test_file, self.cipher)
        with open(self.test_file, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = self.cipher.decrypt(encrypted_data.decode())
        self.assertEqual(decrypted_data.encode(), self.test_data)

    def test_encrypt_folder(self):
        # Test encryption and decryption of all files in a folder
        encrypt_folder(self.test_folder, self.cipher)
        for root, _, files in os.walk(self.test_folder):
            for file in files:
                with open(os.path.join(root, file), 'rb') as f:
                    encrypted_data = f.read()
                decrypted_data = self.cipher.decrypt(encrypted_data.decode())
                self.assertEqual(decrypted_data.encode(), self.test_data)

    def test_pad_unpad(self):
        # Test padding and unpadding functionality
        padded_data = self.cipher.pad(self.test_data)
        unpadded_data = self.cipher.unpad(padded_data)
        self.assertEqual(unpadded_data, self.test_data)

    def test_encrypt_empty_data(self):
        # Test encryption and decryption of empty data
        empty_data = b""
        encrypted = self.cipher.encrypt(empty_data)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted.encode(), empty_data)

    def test_encrypt_large_data(self):
        # Test encryption and decryption of large data (1MB)
        large_data = b"A" * 1024 * 1024  # 1MB of data
        encrypted = self.cipher.encrypt(large_data)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted.encode(), large_data)

if __name__ == "__main__":
    unittest.main()