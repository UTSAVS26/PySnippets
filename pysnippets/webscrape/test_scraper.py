import unittest

from bs4 import BeautifulSoup
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
        soup = BeautifulSoup(self.sample_html, 'html.parser')
        quote_element = soup.find('div', class_='quote')
        quote = self.scraper._parse_quote_element(quote_element)
        expected_quote = Quote(
            text='“A witty saying proves nothing.”',
            author='Voltaire',
            tags=['wit'],
            scraped_at=quote.scraped_at  # Dynamic field
        )
        self.assertEqual(quote.text, expected_quote.text)
        self.assertEqual(quote.author, expected_quote.author)
        self.assertEqual(quote.tags, expected_quote.tags)

    def test_parse_quote_element_missing_author(self):
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
        self.assertIsNone(quote)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main() 