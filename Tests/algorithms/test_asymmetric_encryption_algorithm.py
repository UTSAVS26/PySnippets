import unittest
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class TestRSA(unittest.TestCase):

    def setUp(self):
        # Generate an RSA private key for testing
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()
        self.data = b"Test RSA Encryption and Decryption"

    def encrypt(self, public_key, data):
        ciphertext = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt(self, private_key, ciphertext):
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext

    def test_rsa_encryption_decryption(self):
        encrypted_data = self.encrypt(self.public_key, self.data)
        decrypted_data = self.decrypt(self.private_key, encrypted_data)
        self.assertEqual(decrypted_data, self.data)  # Check if decrypted data matches original

    def test_invalid_key_size(self):
        with self.assertRaises(ValueError):
            # Generating a key with an unsupported size
            rsa.generate_private_key(public_exponent=65537, key_size=1024)

if __name__ == '__main__':
    unittest.main()
