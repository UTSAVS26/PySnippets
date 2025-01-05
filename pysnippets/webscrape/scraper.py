import asyncio
import aiohttp
import logging
import random
import time
import pickle
import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path
from retry import retry
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
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
    
    def __init__(self, base_url: str, output_dir: str = 'output', cache_file: str = 'cache.pkl', max_concurrent_requests: int = 5) -> None:
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.cache_file = Path(cache_file)
        self.session = requests.Session()
        self.ua = UserAgent()
        self.quotes_cache: Dict[str, List[Quote]] = self.load_cache()
        self.max_concurrent_requests = max_concurrent_requests
        logging.debug("Initialized QuoteScraper with base_url: %s and output_dir: %s", base_url, output_dir)

    def load_cache(self) -> Dict[str, List[Quote]]:
        """Load cached data from a file if available."""
        if self.cache_file.exists():
            with open(self.cache_file, 'rb') as f:
                cache = pickle.load(f)
                logging.info("Loaded cache with %d entries", len(cache))
                return cache
        return {}

    def save_cache(self) -> None:
        """Save cached data to a file."""
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.quotes_cache, f)
        logging.info("Cache saved to %s", self.cache_file)

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
        """Scrape quotes from a static page with retries and error handling."""
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

    async def scrape_page_async(self, page: int, semaphore: asyncio.Semaphore) -> List[Quote]:
        """Asynchronously scrape a single page and return a list of Quote objects."""
        url = f"{self.base_url}/page/{page}/"
        logging.info("Asynchronously scraping page: %d", page)
        async with semaphore:
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
        semaphore = asyncio.Semaphore(self.max_concurrent_requests)
        tasks = [self.scrape_page_async(page, semaphore) for page in range(1, num_pages + 1)]
        results = await asyncio.gather(*tasks)
        return [quote for page_quotes in results for quote in page_quotes]

    def scrape_with_threading(self, num_pages: int, max_workers: int = 4) -> List[Quote]:
        """Scrape multiple pages using thread pool."""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
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
            
            # Save CSV
            csv_path = self.output_dir / f"{base_filename}.csv"
            df.to_csv(csv_path, index=False, encoding='utf-8')
            logging.debug("Saved quotes to CSV: %s", csv_path)
    
            # Save JSON
            json_path = self.output_dir / f"{base_filename}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump([quote.__dict__ for quote in quotes], f, ensure_ascii=False, indent=2)
            logging.debug("Saved quotes to JSON: %s", json_path)
                    
            # Save Excel
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
                'average_quote_length': df['text'].str.len().mean(),
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
                
            # Introduce random delay between requests to avoid triggering anti-scraping mechanisms
            time.sleep(random.uniform(1, 3))
        
        self.save_cache()  # Save updated cache to disk after scraping
        return all_quotes