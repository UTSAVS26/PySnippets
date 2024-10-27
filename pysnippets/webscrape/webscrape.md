# Advanced Web Scraper

A robust, feature-rich web scraping tool built in Python for extracting quotes from websites. This scraper supports multiple scraping methods, data analysis, and various output formats.

## Features

- 🚀 Multiple scraping methods:
  - Synchronous scraping with retry mechanism
  - Threaded scraping for parallel execution
  - Asynchronous scraping for improved performance
- 📊 Data analysis capabilities
- 💾 Multiple output formats (CSV, JSON, Excel)
- 🔄 Automatic retry mechanism
- 📝 Comprehensive logging
- 🔍 Data validation and cleaning
- 🎭 Random User-Agent rotation

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
