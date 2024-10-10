# __init__.py

from .scraper import scrape_static_quotes, scrape_dynamic_quotes, save_quotes_to_csv, scrape_multiple_pages

__all__ = [
    'scrape_static_quotes',
    'scrape_dynamic_quotes',
    'save_quotes_to_csv',
    'scrape_multiple_pages'
]
