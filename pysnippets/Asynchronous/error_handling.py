import asyncio
import logging

async def fetch_data(url):
    try:
        logging.info(f"Attempting to fetch data from {url}")
        await asyncio.sleep(1)  # Simulate a network delay
        if url == "http://error.com":
            raise ValueError("Invalid URL")
        return f"Data from {url}"
    except ValueError as e:
        logging.error(f"Error fetching data: {e}")
        return None

async def main():
    urls = ["http://example.com", "http://error.com"]
    for url in urls:
        result = await fetch_data(url)
        if result:
            logging.info(f"Successfully received data: {result}")
        else:
            logging.info("Failed to fetch data")

if __name__ == "__main__":
    asyncio.run(main()) 