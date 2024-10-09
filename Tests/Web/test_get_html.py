#test_get_html.py

import unittest
from unittest.mock import patch
from pysnippets.Web.get_html import get_html  # Replace with your actual module name
import requests


class TestGetHtml(unittest.TestCase):

    @patch('requests.get')
    def test_normal_case(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<html><body>Hello World</body></html>"
        
        result = get_html("https://www.example.com")
        self.assertEqual(result, "<html><body>Hello World</body></html>")

    @patch('requests.get')
    def test_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        
        result = get_html("https://www.example.com")
        self.assertIsNone(result)

    @patch('requests.get')
    def test_request_exception(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Connection Error")
        
        result = get_html("https://www.example.com")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
