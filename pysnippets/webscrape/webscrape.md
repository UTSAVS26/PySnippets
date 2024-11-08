# Advanced Web Scraper

A robust, feature-rich web scraping tool built in Python for extracting quotes from websites. This scraper supports multiple scraping methods, data analysis, and various output formats.

## Features

- 🚀 Multiple scraping methods:
  - **Synchronous scraping with retry mechanism**: This method scrapes pages one by one, with a retry mechanism to handle temporary network errors.
  - **Threaded scraping for parallel execution**: This method utilizes multiple threads to scrape pages simultaneously, significantly improving the scraping speed.
  - **Asynchronous scraping for improved performance**: This method leverages asyncio for asynchronous I/O operations, allowing for efficient use of resources and faster scraping.
- 📦 Data analysis capabilities: The scraper includes functions for analyzing scraped data, such as calculating the total number of quotes, unique authors, most common authors, average quote length, and most common tags.
- 💾 Multiple output formats (CSV, JSON, Excel): The scraper supports saving scraped data in various formats, making it easy to integrate with different workflows.
- 🔄 Automatic retry mechanism: The scraper includes a retry mechanism to handle temporary network errors, ensuring that data is scraped successfully.
- 📝 Comprehensive logging: The scraper logs its operations, including info, warning, error, and debug messages, making it easier to monitor and troubleshoot.
- 🔍 Data validation and cleaning: The scraper includes data validation and cleaning mechanisms to ensure that the scraped data is accurate and consistent.
- 🎭 Random User-Agent rotation: The scraper rotates User-Agent headers to mimic different browsers, reducing the likelihood of being blocked by websites.

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/web-scraper.git
cd web-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from web_scraper import QuoteScraper

# Initialize scraper
scraper = QuoteScraper('https://quotes.toscrape.com')

# Scrape with threading
quotes = scraper.scrape_with_threading(num_pages=3)

# Save results
scraper.save_to_multiple_formats(quotes, 'quotes_output')
```

### Async Scraping

```python
import asyncio

# Scrape asynchronously
quotes = asyncio.run(scraper.scrape_multiple_pages_async(num_pages=3))
```

### Data Analysis

```python
# Analyze scraped quotes
analysis = scraper.analyze_quotes(quotes)
print(analysis)
```

## Configuration

The scraper can be configured through the following parameters:

- `base_url`: The target website URL
- `output_dir`: Directory for saving output files (default: 'output')
- `num_pages`: Number of pages to scrape
- `max_workers`: Maximum number of threads for parallel scraping

## Output Formats

The scraper supports the following output formats:

1. CSV: Comma-separated values file
2. JSON: JavaScript Object Notation file
3. Excel: Microsoft Excel spreadsheet

## Testing

Run the test suite:

```bash
python -m unittest test_web_scraper.py
```

## Project Structure

```
web-scraper/
├── web_scraper.py       # Main scraper implementation
├── test_web_scraper.py  # Test suite
├── requirements.txt     # Project dependencies
├── output/             # Output directory for scraped data
└── logs/               # Logging directory
```

## Dependencies

- requests: HTTP library for making requests
- beautifulsoup4: HTML parsing
- pandas: Data manipulation and analysis
- aiohttp: Async HTTP client/server
- fake-useragent: Random user agent generation
- retry: Retry mechanism for failed requests
- openpyxl: Excel file support

## Error Handling

The scraper includes comprehensive error handling for:

- Network errors
- Parsing errors
- Invalid data
- File I/O errors
- Rate limiting

## Logging

Logs are written to `scraper.log` and include:

- Info level: General operation information
- Warning level: Non-critical issues
- Error level: Critical failures
- Debug level: Detailed debugging information

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
