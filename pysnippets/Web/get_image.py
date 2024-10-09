# get_image.py

import requests

def get_image(url: str, file_path: str) -> bool:
    """
    Downloads an image from the specified URL and saves it to the specified file path.

    Args:
        url (str): The URL of the image to download.
        file_path (str): The file path where the image should be saved.

    Returns:
        bool: True if the image was successfully downloaded, False otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image: {e}")
        return False

