import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

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

def scrape_dynamic_quotes(url):
    """Scrape quotes from dynamically loaded content using Selenium."""
    # Set up headless Selenium Chrome
    options = Options()
    options.headless = True
    service = Service('/path/to/chromedriver')  # Path to your ChromeDriver

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    time.sleep(2)

    quotes = []
    for quote_div in driver.find_elements(By.CLASS_NAME, 'quote'):
        text = quote_div.find_element(By.CLASS_NAME, 'text').text
        author = quote_div.find_element(By.CLASS_NAME, 'author').text
        tags = [tag.text for tag in quote_div.find_elements(By.CLASS_NAME, 'tag')]
        quotes.append({'quote': text, 'author': author, 'tags': tags})
    
    driver.quit()
    return quotes

# Function that will save scraped data into a CSV file
def save_quotes_to_csv(quotes, file_name='quotes.csv'):
    df = pd.DataFrame(quotes)
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")

# Function to scrape multiple pages
def scrape_multiple_pages(base_url, num_pages=3, dynamic=False):
    """Scraping multiple pages either statically or dynamically."""
    all_quotes = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}/page/{page}/"
        print(f"Scraping page {page}...")
        if dynamic:
            quotes = scrape_dynamic_quotes(url)
        else:
            quotes = scrape_static_quotes(url)
        all_quotes.extend(quotes)
    return all_quotes
