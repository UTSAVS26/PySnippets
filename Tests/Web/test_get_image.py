# test_get_image.py

import unittest
from unittest.mock import patch, mock_open
from pysnippets.Web.get_image import get_image  # Replace with your module name

class TestDownloadImage(unittest.TestCase):

    @patch('requests.get')
    def test_download_successful(self, mock_get):
        # Mock the response of requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'image_data'

        with patch('builtins.open', mock_open()) as mock_file:
            result = get_image("https://www.example.com/image.jpg", "local_image.jpg")
            mock_file.assert_called_once_with("local_image.jpg", 'wb')
            mock_file().write.assert_called_once_with(b'image_data')
            self.assertTrue(result)

    @patch('requests.get')
    def test_download_failed(self, mock_get):
        # Simulate a request exception
        mock_get.side_effect = get_image.exceptions.RequestException("Error")

        result = get_image("https://www.example.com/image.jpg", "local_image.jpg")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
