import asyncio
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_data(url):
    logging.info(f"Fetching data from {url}")
    await asyncio.sleep(1)  # Simulate network delay
    return f"Data from {url}"

async def main():
    result = await fetch_data("http://example.com")
    logging.info(f"Received: {result}")

if __name__ == "__main__":
    asyncio.run(main())
