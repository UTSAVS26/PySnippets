import unittest
from unittest.mock import Mock, patch
import asyncio
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pysnippets.webscrape.scraper import QuoteScraper

class TestQuoteScraper(unittest.TestCase):
    """Test cases for the QuoteScraper class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.base_url = 'https://quotes.toscrape.com'
        self.scraper = QuoteScraper(self.base_url)
        self.sample_html = '''
            <div class="quote">
                <span class="text">Test quote</span>
                <small class="author">Test Author</small>
                <div class="tags">
                    <a class="tag">test</a>
                    <a class="tag">sample</a>
                </div>
            </div>
        '''
        
    def tearDown(self):
        """Clean up after each test method."""
        # Remove test output files
        for file in Path('output').glob('test_*'):
            file.unlink()

    @patch('requests.Session.get')
    def test_scrape_static_quotes(self, mock_get):
        """Test the static quote scraping method."""
        # Mock the response
        mock_response = Mock()
        mock_response.text = self.sample_html
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        quotes = self.scraper.scrape_static_quotes(self.base_url)
        
        self.assertEqual(len(quotes), 1)
        self.assertEqual(quotes[0]['quote'], 'Test quote')
        self.assertEqual(quotes[0]['author'], 'Test Author')
        self.assertEqual(quotes[0]['tags'], ['test', 'sample'])

    def test_parse_quote_element(self):
        """Test parsing of individual quote elements."""
        soup = BeautifulSoup(self.sample_html, 'html.parser')
        quote_element = soup.find('div', class_='quote')
        
        result = self.scraper._parse_quote_element(quote_element)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['quote'], 'Test quote')
        self.assertEqual(result['author'], 'Test Author')
        self.assertIn('scraped_at', result)

    def test_analyze_quotes(self):
        """Test quote analysis functionality."""
        test_quotes = [
            {
                'quote': 'Test quote 1',
                'author': 'Author 1',
                'tags': ['test', 'sample']
            },
            {
                'quote': 'Test quote 2',
                'author': 'Author 1',
                'tags': ['test']
            }
        ]
        
        analysis = self.scraper.analyze_quotes(test_quotes)
        
        self.assertEqual(analysis['total_quotes'], 2)
        self.assertEqual(analysis['unique_authors'], 1)
        self.assertEqual(analysis['most_common_author'], 'Author 1')

    @patch('requests.Session.get')
    def test_error_handling(self, mock_get):
        """Test error handling in scraping."""
        mock_get.side_effect = requests.RequestException("Test error")
        
        with self.assertRaises(requests.RequestException):
            self.scraper.scrape_static_quotes(self.base_url)

    def test_get_headers(self):
        """Test header generation."""
        headers = self.scraper.get_headers()
        
        self.assertIn('User-Agent', headers)
        self.assertIn('Accept', headers)
        self.assertIn('Accept-Language', headers)

def async_test(coro):
    """Decorator for running async tests."""
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(coro(*args, **kwargs))
    return wrapper

if __name__ == '__main__':
    unittest.main()