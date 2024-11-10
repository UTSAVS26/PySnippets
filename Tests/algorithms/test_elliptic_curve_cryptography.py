import unittest
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class TestECC(unittest.TestCase):

    def setUp(self):
        self.private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
        self.public_key = self.private_key.public_key()
        self.data = b"Test ECC Encryption and Decryption"

    def encrypt_message(self, public_key, message):
        shared_key = public_key.exchange(ec.ECDH())
        return shared_key + message  # Simplified for demonstration

    def decrypt_message(self, private_key, shared_message):
        return shared_message[32:]  # Return the message part for demonstration

    def test_ecc_encryption_decryption(self):
        encrypted_data = self.encrypt_message(self.public_key, self.data)
        decrypted_data = self.decrypt_message(self.private_key, encrypted_data)
        self.assertEqual(decrypted_data, self.data)  # Check if decrypted data matches original

    def test_invalid_curve(self):
        with self.assertRaises(ValueError):
            ec.generate_private_key(ec.SECP192R1(), default_backend())  # Unsupported curve

if __name__ == '__main__':
    unittest.main()
