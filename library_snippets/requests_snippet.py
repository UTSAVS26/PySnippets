import requests
from bs4 import BeautifulSoup
from typing import List

def fetch(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        return str(e)

def parse(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, 'html.parser')

def extract_links(soup: BeautifulSoup) -> List[str]:
    return [a['href'] for a in soup.find_all('a', href=True)]

def extract_text(soup: BeautifulSoup, tag: str) -> List[str]:
    return [element.get_text() for element in soup.find_all(tag)] 