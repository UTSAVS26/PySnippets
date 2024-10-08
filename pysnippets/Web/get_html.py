#get_html.py

import requests

def get_html(url: str) -> str:
    """
    Fetches the HTML content from the specified URL.

    Args:
        url (str): The URL from which to fetch the HTML content.

    Returns:
        str: The HTML content of the page if the request is successful.
             Returns None if there is an error fetching the URL.

    Example usage:
    get_html("https://www.example.com") -> "<!doctype html>... (HTML content)"
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Return the HTML content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    url = "https://www.example.com"  # Replace with your desired URL
    html_content = get_html(url)
    if html_content:
        print(html_content)  # Print the HTML content
