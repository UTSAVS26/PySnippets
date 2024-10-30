import requests
from bs4 import BeautifulSoup

def fetch(url):
    response = requests.get(url)
    return response.text

def parse(html):
    return BeautifulSoup(html, 'html.parser')

def extract_links(soup):
    return [a['href'] for a in soup.find_all('a', href=True)]

def extract_text(soup, tag):
    return [element.get_text() for element in soup.find_all(tag)] 