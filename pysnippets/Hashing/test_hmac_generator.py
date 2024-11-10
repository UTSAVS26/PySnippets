import unittest
from hmac_generator import HMACGenerator
import hmac
import hashlib

class TestHMACGenerator(unittest.TestCase):
    def test_generate_hmac_sha256(self):
        generator = HMACGenerator(key=b'secret_key', message="Test Message", digestmod='sha256')
        expected = hmac.new(b'secret_key', b'Test Message', hashlib.sha256).hexdigest()
        self.assertEqual(generator.generate_hmac(), expected)

    def test_generate_hmac_sha1(self):
        generator = HMACGenerator(key=b'secret_key', message="Test Message", digestmod='sha1')
        expected = hmac.new(b'secret_key', b'Test Message', hashlib.sha1).hexdigest()
        self.assertEqual(generator.generate_hmac(), expected)

    def test_invalid_digestmod(self):
        generator = HMACGenerator(key=b'secret_key', message="Test Message", digestmod='invalid')
        with self.assertRaises(AttributeError):
            generator.generate_hmac()

if __name__ == "__main__":
    unittest.main() 