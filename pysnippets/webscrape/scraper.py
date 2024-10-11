import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_static_quotes(url):
    """Scrape quotes from a static page."""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            quotes.append({'quote': text, 'author': author, 'tags': tags})
        return quotes
    else:
        print("Error fetching the page.")
        return []

# Function that will save scraped data into a CSV file
def save_quotes_to_csv(quotes, file_name='quotes.csv'):
    df = pd.DataFrame(quotes)
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")

# Function to scrape multiple pages
def scrape_multiple_pages(base_url, num_pages=3):
    """Scraping multiple pages statically."""
    all_quotes = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}/page/{page}/"
        print(f"Scraping page {page}...")
        quotes = scrape_static_quotes(url)
        all_quotes.extend(quotes)
    return all_quotes

if __name__ == "__main__":
    base_url = 'https://quotes.toscrape.com'
    quotes = scrape_multiple_pages(base_url, num_pages=3)
    save_quotes_to_csv(quotes, 'quotes.csv')  # Save the scraped data to a CSV file