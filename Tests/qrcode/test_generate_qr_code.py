# test_generate_qr_code.py

import unittest
import os
from pysnippets.qrcode.generate_qr_code import generate_qr_code  # Replace with the correct import

class TestGenerateQRCode(unittest.TestCase):

    def setUp(self):
        """Set up a temporary file path for testing."""
        self.test_file_path = "test_qr_code.png"
        self.test_data = "https://www.example.com"

    def test_generate_qr_code(self):
        """Test if the QR code is generated and saved as an image file."""
        generate_qr_code(self.test_data, self.test_file_path)
        self.assertTrue(os.path.exists(self.test_file_path))

    def test_invalid_file_path(self):
        """Test if the function handles an invalid file path."""
        with self.assertRaises(OSError):
            generate_qr_code(self.test_data, "/invalid_path/test_qr_code.png")

    def tearDown(self):
        """Remove the generated test file after the test."""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

if __name__ == "__main__":
    unittest.main()
