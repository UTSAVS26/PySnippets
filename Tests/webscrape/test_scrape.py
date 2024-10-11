import unittest
from unittest.mock import patch, MagicMock
from pysnippets.webscrape.scraper import scrape_static_quotes, save_quotes_to_csv
from colorama import Fore, Style

class TestScraper(unittest.TestCase):

    @patch('pysnippets.webscrape.scraper.requests.get')
    def test_scrape_static_quotes_success(self, mock_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''
        <div class="quote">
            <span class="text">The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.</span>
            <small class="author">Albert Einstein</small>
            <a class="tag" href="/tag/change/">change</a>
            <a class="tag" href="/tag/world/">world</a>
        </div>
        '''
        mock_get.return_value = mock_response

        url = 'https://quotes.toscrape.com/page/1/'
        quotes = scrape_static_quotes(url)

        self.assertEqual(len(quotes), 1)
        self.assertEqual(quotes[0]['quote'], "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.")
        self.assertEqual(quotes[0]['author'], "Albert Einstein")
        self.assertIn('change', quotes[0]['tags'])
        self.assertIn('world', quotes[0]['tags'])

    @patch('pysnippets.webscrape.scraper.requests.get')
    def test_scrape_static_quotes_non_200_response(self, mock_get):
        # Mock the response from requests.get to return a non-200 status code
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        url = 'https://quotes.toscrape.com/page/1/'
        quotes = scrape_static_quotes(url)

        self.assertEqual(quotes, [])
        mock_get.assert_called_once_with(url)

    @patch('pysnippets.webscrape.scraper.pd.DataFrame.to_csv')
    def test_save_quotes_to_csv(self, mock_to_csv):
        quotes = [{'quote': 'Test quote', 'author': 'Test Author', 'tags': ['test']}]
        save_quotes_to_csv(quotes, 'test_quotes.csv')

        # Check if to_csv was called with the correct parameters
        mock_to_csv.assert_called_once_with('test_quotes.csv', index=False)

if __name__ == '__main__':
    unittest.main()

    # Custom output for test results
    for test in unittest.TestLoader().loadTestsFromTestCase(TestScraper):
        result = unittest.TextTestRunner().run(test)
        if result.wasSuccessful():
            print(Fore.GREEN + f"Test {test._testMethodName} passed!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Test {test._testMethodName} failed!" + Style.RESET_ALL)
            for failure in result.failures:
                print(Fore.RED + f"Failure in {failure[0]}: {failure[1]}" + Style.RESET_ALL)
