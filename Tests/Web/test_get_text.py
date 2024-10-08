#get_html.py

import unittest
from unittest.mock import patch
from pysnippets.Web.get_text import get_text  # Replace with your actual module name
from bs4 import BeautifulSoup
import requests

class TestGetText(unittest.TestCase):

    @patch('requests.get')
    @patch('bs4.BeautifulSoup')
    def test_normal_case(self, mock_bs, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<html><body>Hello World</body></html>"
        
        mock_bs.return_value.get_text.return_value = "Hello World"
        
        result = get_text("https://www.example.com")
        self.assertEqual(result, "Hello World")

    @patch('requests.get')
    def test_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        
        result = get_text("https://www.example.com")
        self.assertIsNone(result)

    @patch('requests.get')
    def test_request_exception(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Connection Error")
        
        result = get_text("https://www.example.com")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
