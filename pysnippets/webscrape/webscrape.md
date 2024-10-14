# Overview

This module provides functions to scrape quotes from a static web page and save the data into a CSV file.

## Table of Contents

1. [Function: `scrape_static_quotes`](#function-scrape_static_quotes)

   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Example Usage](#example-usage)

2. [Function: `save_quotes_to_csv`](#function-save_quotes_to_csv)

   - [Arguments](#arguments-1)
   - [Returns](#returns-1)
   - [Example Usage](#example-usage-1)

3. [Function: `scrape_multiple_pages`](#function-scrape_multiple_pages)
   - [Arguments](#arguments-2)
   - [Returns](#returns-2)
   - [Example Usage](#example-usage-2)

---

## Function: `scrape_static_quotes`

```python
scrape_static_quotes(url: str) -> list
```

Scrapes quotes from a static page.

### Arguments

- **url** (str): The URL of the page to scrape quotes from.

### Returns

- **list**: A list of dictionaries containing quotes, authors, and tags. Each dictionary has the keys `quote`, `author`, and `tags`.

### Example Usage

```python
quotes = scrape_static_quotes("https://quotes.toscrape.com/page/1/")
for quote in quotes:
    print(quote)
```

---

## Function: `save_quotes_to_csv`

```python
save_quotes_to_csv(quotes: list, file_name='quotes.csv')
```

Saves scraped quotes data into a CSV file.

### Arguments

- **quotes** (list): A list of dictionaries containing quotes data to save.
- **file_name** (str, optional): The name of the CSV file to save the data. Defaults to 'quotes.csv'.

### Returns

- **None**

### Example Usage

```python
quotes = [{'quote': 'Life is what happens when you’re busy making other plans.', 'author': 'John Lennon', 'tags': ['life', 'misattributed-john-lennon']}]
save_quotes_to_csv(quotes)
```

---

## Function: `scrape_multiple_pages`

```python
scrape_multiple_pages(base_url: str, num_pages=3) -> list
```

Scrapes quotes from multiple pages.

### Arguments

- **base_url** (str): The base URL of the quotes website.
- **num_pages** (int, optional): The number of pages to scrape. Defaults to 3.

### Returns

- **list**: A combined list of all quotes scraped from the specified number of pages.

### Example Usage

```python
base_url = 'https://quotes.toscrape.com'
all_quotes = scrape_multiple_pages(base_url, num_pages=3)
```
