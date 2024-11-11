import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from datetime import datetime
from pysnippets.webscrape.scraper import QuoteScraper, Quote

class TestQuoteScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = QuoteScraper('https://quotes.toscrape.com')
        self.sample_html = '''
        <div class="quote">
            <span class="text">“A witty saying proves nothing.”</span>
            <span>
                <small class="author">Voltaire</small>
                <a class="tag" href="/tag/wit/page/1/">wit</a>
            </span>
        </div>
        '''

    def test_parse_quote_element_valid(self):
        """Test parsing a valid quote element."""
        soup = BeautifulSoup(self.sample_html, 'html.parser')
        quote_element = soup.find('div', class_='quote')
        quote = self.scraper._parse_quote_element(quote_element)
        
        # Expected quote
        expected_quote = Quote(
            text='“A witty saying proves nothing.”',
            author='Voltaire',
            tags=['wit'],
            scraped_at=quote.scraped_at  # Dynamic field
        )
        
        # Check if parsed data matches expected
        self.assertEqual(quote.text, expected_quote.text)
        self.assertEqual(quote.author, expected_quote.author)
        self.assertEqual(quote.tags, expected_quote.tags)

    def test_parse_quote_element_missing_author(self):
        """Test parsing when the author is missing."""
        incomplete_html = '''
        <div class="quote">
            <span class="text">“Incomplete quote without author.”</span>
            <span>
                <a class="tag" href="/tag/incomplete/page/1/">incomplete</a>
            </span>
        </div>
        '''
        soup = BeautifulSoup(incomplete_html, 'html.parser')
        quote_element = soup.find('div', class_='quote')
        quote = self.scraper._parse_quote_element(quote_element)
        self.assertIsNone(quote)  # Expect None due to missing author

    @patch('pysnippets.webscrape.scraper.requests.Session.get')
    def test_fetch_page_success(self, mock_get):
        """Test fetching a page successfully."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = self.sample_html
        mock_get.return_value = mock_response

        response = self.scraper.fetch_page('https://quotes.toscrape.com')
        self.assertEqual(response.status_code, 200)
        self.assertIn("A witty saying proves nothing.", response.text)

    @patch('pysnippets.webscrape.scraper.requests.Session.get')
    def test_fetch_page_failure(self, mock_get):
        """Test fetch_page with a failure (e.g., 404 or timeout)."""
        mock_get.side_effect = Exception("Failed to fetch page")
        
        with self.assertRaises(Exception):
            self.scraper.fetch_page('https://quotes.toscrape.com')

    @patch('pysnippets.webscrape.scraper.QuoteScraper.fetch_page')
    def test_scrape_static_quotes(self, mock_fetch_page):
        """Test static scraping function."""
        # Mock response to simulate static scraping
        mock_fetch_page.return_value.text = self.sample_html
        quotes = self.scraper.scrape_static_quotes('https://quotes.toscrape.com')
        
        self.assertEqual(len(quotes), 1)
        self.assertEqual(quotes[0]['text'], "“A witty saying proves nothing.”")
        self.assertEqual(quotes[0]['author'], "Voltaire")
        self.assertIn("wit", quotes[0]['tags'])

    def tearDown(self):
        """Clean up after tests if needed."""
        pass

if __name__ == '__main__':
    unittest.main()