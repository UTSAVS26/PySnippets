import unittest
from pysnippets.Cipher_algorithms.affine_cipher import AffineCipher

class TestAffineCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = AffineCipher(a=5, b=8)

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt('HELLO'), 'MJQQT')
        self.assertEqual(self.cipher.encrypt('AFFINE CIPHER'), 'IHHWVC SWFRCP')

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt('MJQQT'), 'HELLO')
        self.assertEqual(self.cipher.decrypt('IHHWVC SWFRCP'), 'AFFINE CIPHER')

if __name__ == '__main__':
    unittest.main()
