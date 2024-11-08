import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import json
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path
import aiohttp
import asyncio
from fake_useragent import UserAgent
import concurrent.futures
from retry import retry
from dataclasses import dataclass
from typing import Any
import time
import argparse

logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@dataclass
class Quote:
    """Data class to represent a scraped quote."""
    text: str
    author: str
    tags: List[str]
    scraped_at: datetime

class QuoteScraper:
    """A class to handle quote scraping with enhanced readability and performance."""
    
    def __init__(self, base_url: str, output_dir: str = 'output') -> None:
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.ua = UserAgent()
        self.quotes_cache: Dict[str, List[Quote]] = {}
        logging.debug("Initialized QuoteScraper with base_url: %s and output_dir: %s", base_url, output_dir)
        
    def get_headers(self) -> Dict[str, str]:
        """Generate random headers for each request."""
        headers = {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        logging.debug("Generated headers: %s", headers)
        return headers

    @retry(tries=3, delay=2, backoff=2)
    def fetch_page(self, url: str) -> requests.Response:
        """Fetch a page with retries and return the response."""
        try:
            logging.info("Fetching URL: %s", url)
            response = self.session.get(url, headers=self.get_headers(), timeout=10)
            response.raise_for_status()
            logging.debug("Fetched URL successfully: %s", url)
            return response
        except requests.RequestException as e:
            logging.error("Failed to fetch URL %s: %s", url, e)
            raise

    def scrape_static_quotes(self, url: str) -> List[Dict[str, Any]]:
        """
        Scrape quotes from a static page with retries and error handling.
        
        Args:
            url (str): The URL of the page to scrape.
        
        Returns:
            List[Dict[str, Any]]: A list of scraped quotes.
        """
        response = self.fetch_page(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = [self._parse_quote_element(quote) for quote in soup.find_all('div', class_='quote') if self._parse_quote_element(quote)]
        logging.info("Scraped %d quotes from %s", len(quotes), url)
        return quotes

    def _parse_quote_element(self, quote_element: Any) -> Optional[Quote]:
        """Parse a single quote element and return a Quote object."""
        try:
            text = quote_element.find('span', class_='text').get_text(strip=True)
            author = quote_element.find('small', class_='author').get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote_element.find_all('a', class_='tag')]
            quote = Quote(text=text, author=author, tags=tags, scraped_at=datetime.now())
            logging.debug("Parsed quote: %s", quote)
            return quote
        except AttributeError as e:
            logging.warning("Missing elements in quote: %s", e)
            return None
        except Exception as e:
            logging.error("Error parsing quote: %s", e)
            return None

    async def scrape_page_async(self, page: int) -> List[Quote]:
        """Asynchronously scrape a single page and return a list of Quote objects."""
        url = f"{self.base_url}/page/{page}/"
        logging.info("Asynchronously scraping page: %d", page)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.get_headers()) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, 'html.parser')
                        quotes = [self._parse_quote_element(quote) for quote in soup.find_all('div', class_='quote') if self._parse_quote_element(quote)]
                        logging.info("Scraped %d quotes from page %d", len(quotes), page)
                        return quotes
                    else:
                        logging.error("Error %d on page %d", response.status, page)
                        return []
        except aiohttp.ClientError as e:
            logging.error("Async scraping error on page %d: %s", page, e)
            return []

    async def scrape_multiple_pages_async(self, num_pages: int) -> List[Quote]:
        """Scrape multiple pages asynchronously."""
        tasks = [self.scrape_page_async(page) for page in range(1, num_pages + 1)]
        results = await asyncio.gather(*tasks)
        return [quote for page_quotes in results for quote in page_quotes]

    def scrape_with_threading(self, num_pages: int, max_workers: int = 4) -> List[Quote]:
        """Scrape multiple pages using thread pool."""
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {
                executor.submit(self.scrape_static_quotes, 
                              f"{self.base_url}/page/{page}/"): page 
                for page in range(1, num_pages + 1)
            }
            
            all_quotes = []
            for future in concurrent.futures.as_completed(future_to_url):
                page = future_to_url[future]
                try:
                    quotes = future.result()
                    all_quotes.extend(quotes)
                    logging.info(f"Successfully scraped page {page}")
                except Exception as e:
                    logging.error(f"Error scraping page {page}: {e}")
                    
            return all_quotes

    def save_to_multiple_formats(self, quotes: List[Quote], base_filename: str) -> None:
        """Save scraped quotes in multiple formats (CSV, JSON, Excel)."""
        try:
            df = pd.DataFrame([quote.__dict__ for quote in quotes])
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            base_filename = f"{base_filename}_{timestamp}"
            
            csv_path = self.output_dir / f"{base_filename}.csv"
            df.to_csv(csv_path, index=False, encoding='utf-8')
            logging.debug("Saved quotes to CSV: %s", csv_path)
    
            json_path = self.output_dir / f"{base_filename}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump([quote.__dict__ for quote in quotes], f, ensure_ascii=False, indent=2)
            logging.debug("Saved quotes to JSON: %s", json_path)
                    
            excel_path = self.output_dir / f"{base_filename}.xlsx"
            df.to_excel(excel_path, index=False)
            logging.debug("Saved quotes to Excel: %s", excel_path)
                
            logging.info("Data saved in multiple formats in %s", self.output_dir)
                
        except Exception as e:
            logging.error("Error saving data: %s", e)
            raise

    def analyze_quotes(self, quotes: List[Quote]) -> Dict:
        """Analyzing the scraped quotes data."""
        try:
            df = pd.DataFrame([quote.__dict__ for quote in quotes])
            
            analysis = {
                'total_quotes': len(quotes),
                'unique_authors': len(df['author'].unique()),
                'most_common_author': df['author'].mode().iloc[0],
                'average_quote_length': df['quote'].str.len().mean(),
                'most_common_tags': pd.Series([
                    tag for tags in df['tags'] for tag in tags
                ]).value_counts().head(5).to_dict(),
                'quotes_per_author': df['author'].value_counts().to_dict()
            }
            
            return analysis
            
        except Exception as e:
            logging.error(f"Error analyzing quotes: {e}")
            return {}

    def scrape_with_caching(self, num_pages: int) -> List[Quote]:
        """Scrape multiple pages with caching to avoid redundant requests."""
        all_quotes = []
        for page in range(1, num_pages + 1):
            url = f"{self.base_url}/page/{page}/"
            if url in self.quotes_cache:
                logging.info("Loading quotes from cache for URL: %s", url)
                all_quotes.extend(self.quotes_cache[url])
            else:
                quotes = self.scrape_static_quotes(url)
                self.quotes_cache[url] = quotes
                all_quotes.extend(quotes)
        return all_quotes

    def scrape_with_rate_limiting(self, num_pages: int, delay: float = 1.0) -> List[Quote]:
        """Scrape multiple pages with a delay between requests to respect rate limits."""
        all_quotes = []
        for page in range(1, num_pages + 1):
            quotes = self.scrape_static_quotes(f"{self.base_url}/page/{page}/")
            all_quotes.extend(quotes)
            logging.debug("Sleeping for %.2f seconds to respect rate limits", delay)
            time.sleep(delay)
        return all_quotes

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Advanced Quote Scraper")
    parser.add_argument('--base_url', type=str, default='https://quotes.toscrape.com', help='Base URL of the quotes website')
    parser.add_argument('--num_pages', type=int, default=3, help='Number of pages to scrape')
    parser.add_argument('--output_dir', type=str, default='output', help='Directory to save output files')
    parser.add_argument('--mode', type=str, choices=['sync', 'async', 'thread'], default='thread', help='Scraping mode')
    return parser.parse_args()

def main():
    """Main execution function with multiple scraping options."""
    args = parse_arguments()
    scraper = QuoteScraper(args.base_url, args.output_dir)
    
    try:
        logging.info("Starting scraping in %s mode", args.mode)
        if args.mode == 'async':
            quotes = asyncio.run(scraper.scrape_multiple_pages_async(args.num_pages))
        elif args.mode == 'thread':
            quotes = scraper.scrape_with_threading(args.num_pages)
        else:
            quotes = scraper.scrape_static_quotes(args.base_url)
        
        scraper.save_to_multiple_formats(quotes, 'quotes_output')
        analysis = scraper.analyze_quotes([quote.__dict__ for quote in quotes])
        logging.info("Analysis: %s", analysis)
        print(f"Total unique quotes collected: {len(quotes)}")
        
    except Exception as e:
        logging.error("Scraping failed: %s", e)
        raise

if __name__ == "__main__":
    main()