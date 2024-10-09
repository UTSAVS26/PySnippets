#get_text.py

import requests
from bs4 import BeautifulSoup

def get_text(url: str) -> str:
    """
    Fetches the text content from the specified URL.

    Args:
        url (str): The URL from which to fetch the text content.

    Returns:
        str: The text content of the page if the request is successful.
             Returns None if there is an error fetching the URL.

    Example usage:
    get_text("https://www.example.com") -> "Example Domain\n\nThis domain is for use in illustrative examples... (text content)"
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()  # Return the text content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    url = "https://www.example.com"  # Replace with your desired URL
    text_content = get_text(url)
    if text_content:
        print(text_content)  # Print the text content
