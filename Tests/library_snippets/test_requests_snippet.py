import unittest
from unittest.mock import patch
from library_snippets.requests_snippet import fetch, parse

class TestRequestsSnippet(unittest.TestCase):
    @patch('library_snippets.requests_snippet.requests.get')
    def test_fetch(self, mock_get):
        """ Test fetching HTML content. """
        mock_get.return_value.text = 'Mocked page content'
        result = fetch('http://example.com')
        self.assertEqual(result, 'Mocked page content')

    def test_parse(self):
        """ Test parsing HTML content. """
        html_content = '<html><head><title>Test</title></head><body><p>Hello World</p></body></html>'
        soup = parse(html_content)
        self.assertEqual(soup.title.string, 'Test')

# Additional tests for extracting links and text can be added similarly.

if __name__ == '__main__':
    unittest.main() 