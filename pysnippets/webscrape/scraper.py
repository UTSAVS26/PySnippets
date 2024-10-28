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

logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class QuoteScraper:
    """A class to handle quote scraping with advanced features."""
    
    def __init__(self, base_url: str, output_dir: str = 'output'):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.ua = UserAgent()
        self.quotes_cache = {}
        
    def get_headers(self) -> Dict[str, str]:
        """Generating some random headers for each request."""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

    @retry(tries=3, delay=2, backoff=2)
    def scrape_static_quotes(self, url: str) -> List[Dict]:
        """
        Scraping quotes from a static page with retries and error handling code.
        """
        try:
            response = self.session.get(
                url,
                headers=self.get_headers(),
                timeout=10
            )
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = []
            
            for quote in soup.find_all('div', class_='quote'):
                try:
                    quote_data = self._parse_quote_element(quote)
                    if quote_data:
                        quotes.append(quote_data)
                        
                except AttributeError as e:
                    logging.error(f"Error parsing quote element: {e}")
                    continue
                    
            return quotes
            
        except requests.RequestException as e:
            logging.error(f"Error fetching the page {url}: {e}")
            raise
            
    def _parse_quote_element(self, quote_element) -> Optional[Dict]:
        """Parse a single quote element with validation."""
        try:
            text = quote_element.find('span', class_='text')
            author = quote_element.find('small', class_='author')
            tags = quote_element.find_all('a', class_='tag')
            
            if not (text and author):
                logging.warning("Missing required quote elements")
                return None
                
            return {
                'quote': text.text.strip(),
                'author': author.text.strip(),
                'tags': [tag.text.strip() for tag in tags],
                'scraped_at': datetime.now().isoformat()
            }
        except Exception as e:
            logging.error(f"Error parsing quote: {e}")
            return None

    async def scrape_page_async(self, page: int) -> List[Dict]:
        """Asynchronously scrape a single page."""
        url = f"{self.base_url}/page/{page}/"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.get_headers()) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, 'html.parser')
                        quotes = []
                        
                        for quote in soup.find_all('div', class_='quote'):
                            quote_data = self._parse_quote_element(quote)
                            if quote_data:
                                quotes.append(quote_data)
                                
                        return quotes
                    else:
                        logging.error(f"Error {response.status} on page {page}")
                        return []
        except Exception as e:
            logging.error(f"Async scraping error on page {page}: {e}")
            return []

    async def scrape_multiple_pages_async(self, num_pages: int) -> List[Dict]:
        """Scrape multiple pages asynchronously."""
        tasks = [self.scrape_page_async(page) for page in range(1, num_pages + 1)]
        results = await asyncio.gather(*tasks)
        return [quote for page_quotes in results for quote in page_quotes]

    def scrape_with_threading(self, num_pages: int, max_workers: int = 4) -> List[Dict]:
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

    def save_to_multiple_formats(self, quotes: List[Dict], base_filename: str):
        """Save scraped data in multiple formats."""
        try:
            df = pd.DataFrame(quotes)
            csv_path = self.output_dir / f"{base_filename}.csv"
            df.to_csv(csv_path, index=False, encoding='utf-8')

            json_path = self.output_dir / f"{base_filename}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(quotes, f, ensure_ascii=False, indent=2)
                
            excel_path = self.output_dir / f"{base_filename}.xlsx"
            df.to_excel(excel_path, index=False)
            
            logging.info(f"Data saved in multiple formats in {self.output_dir}")
            
        except Exception as e:
            logging.error(f"Error saving data: {e}")
            raise

    def analyze_quotes(self, quotes: List[Dict]) -> Dict:
        """Analyzing the scraped quotes data."""
        try:
            df = pd.DataFrame(quotes)
            
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

def main():
    """Main execution function with multiple scraping options."""
    base_url = 'https://quotes.toscrape.com'
    num_pages = 3
    scraper = QuoteScraper(base_url)
    
    try:
        logging.info("Starting threaded scraping...")
        quotes_threaded = scraper.scrape_with_threading(num_pages)
        
        logging.info("Starting async scraping...")
        quotes_async = asyncio.run(scraper.scrape_multiple_pages_async(num_pages))
        
        all_quotes = quotes_threaded + quotes_async
        df = pd.DataFrame(all_quotes).drop_duplicates(subset=['quote', 'author'])
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        scraper.save_to_multiple_formats(df.to_dict('records'), f'quotes_{timestamp}')
        
        analysis = scraper.analyze_quotes(df.to_dict('records'))
        
        analysis_path = scraper.output_dir / f'analysis_{timestamp}.json'
        with open(analysis_path, 'w') as f:
            json.dump(analysis, f, indent=2)
            
        logging.info("Scraping completed successfully")
        print(f"Total unique quotes collected: {len(df)}")
        print(f"Analysis saved to {analysis_path}")
        
    except Exception as e:
        logging.error(f"Script failed: {e}")
        raise

if __name__ == "__main__":
    main()