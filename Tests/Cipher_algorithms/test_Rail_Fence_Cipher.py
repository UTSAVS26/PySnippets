import unittest
from pysnippets.Cipher_algorithms.Rail_Fence_Cipher import rail_fence_cipher_encrypt, rail_fence_cipher_decrypt

class TestRailFenceCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(rail_fence_cipher_encrypt("HELLO", 3), "HOELL")
        self.assertEqual(rail_fence_cipher_encrypt("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN")

    def test_decrypt(self):
        self.assertEqual(rail_fence_cipher_decrypt("HOELL", 3), "HELLO")
        self.assertEqual(rail_fence_cipher_decrypt("WECRLTEERDSOEEFEAOCAIVDEN", 3), "WEAREDISCOVEREDFLEEATONCE")

    def test_invalid_input_encrypt(self):
        with self.assertRaises(ValueError):
            rail_fence_cipher_encrypt(12345, 3)
        with self.assertRaises(ValueError):
            rail_fence_cipher_encrypt("HELLO", "three")
        with self.assertRaises(ValueError):
            rail_fence_cipher_encrypt("HELLO", -1)

    def test_invalid_input_decrypt(self):
        with self.assertRaises(ValueError):
            rail_fence_cipher_decrypt(12345, 3)
        with self.assertRaises(ValueError):
            rail_fence_cipher_decrypt("HOELL", "three")
        with self.assertRaises(ValueError):
            rail_fence_cipher_decrypt("HOELL", -1)

if __name__ == '__main__':
    unittest.main()
