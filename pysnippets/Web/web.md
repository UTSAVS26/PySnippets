# Overview

This module provides functions for fetching HTML content, downloading images, and extracting text from specified URLs.

## Table of Contents

1. [Function: `get_html`](#function-get_html)

   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Example Usage](#example-usage)

2. [Function: `get_image`](#function-get_image)

   - [Arguments](#arguments-1)
   - [Returns](#returns-1)
   - [Example Usage](#example-usage-1)

3. [Function: `get_text`](#function-get_text)
   - [Arguments](#arguments-2)
   - [Returns](#returns-2)
   - [Example Usage](#example-usage-2)

---

## Function: `get_html`

```python
get_html(url: str) -> str
```

Fetches the HTML content from the specified URL.

### Arguments

- **url** (str): The URL from which to fetch the HTML content.

### Returns

- **str**: The HTML content of the page if the request is successful.
- Returns **None** if there is an error fetching the URL.

### Example Usage

```python
html_content = get_html("https://www.example.com")
if html_content:
    print(html_content)  # Prints the HTML content
```

---

## Function: `get_image`

```python
get_image(url: str, file_path: str) -> bool
```

Downloads an image from the specified URL and saves it to the specified file path.

### Arguments

- **url** (str): The URL of the image to download.
- **file_path** (str): The file path where the image should be saved.

### Returns

- **bool**: `True` if the image was successfully downloaded, `False` otherwise.

### Example Usage

```python
image_url = "https://www.example.com/image.png"
success = get_image(image_url, "downloaded_image.png")
if success:
    print("Image downloaded successfully!")
else:
    print("Failed to download the image.")
```

---

## Function: `get_text`

```python
get_text(url: str) -> str
```

Fetches the text content from the specified URL.

### Arguments

- **url** (str): The URL from which to fetch the text content.

### Returns

- **str**: The text content of the page if the request is successful.
- Returns **None** if there is an error fetching the URL.

### Example Usage

```python
text_content = get_text("https://www.example.com")
if text_content:
    print(text_content)  # Prints the text content
```
