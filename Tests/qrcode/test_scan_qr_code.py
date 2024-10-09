# test_scan_qr_code.py

import cv2
from pyzbar.pyzbar import decode
import unittest
from unittest.mock import patch
from pysnippets.qrcode.scan_qr_code import scan_qr_code  # Replace with the correct import

class TestScanQRCode(unittest.TestCase):

    @patch('cv2.imread')
    @patch('pyzbar.pyzbar.decode')
    def test_scan_qr_code_success(self, mock_decode, mock_imread):
        """Test if the QR code is successfully decoded."""
        mock_imread.return_value = "fake_image_data"
        
        # Mock the decoding process to return fake QR code data
        mock_decode.return_value = [type('', (), {'data': b'https://www.example.com'})()]
        
        result = scan_qr_code("test_qr_code.png")
        self.assertEqual(result, "https://www.example.com")

    @patch('cv2.imread')
    @patch('pyzbar.pyzbar.decode')
    def test_no_qr_code_found(self, mock_decode, mock_imread):
        """Test if the function handles no QR code found in the image."""
        mock_imread.return_value = "fake_image_data"
        
        # Simulate no QR code being found
        mock_decode.return_value = []
        
        result = scan_qr_code("test_qr_code.png")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
