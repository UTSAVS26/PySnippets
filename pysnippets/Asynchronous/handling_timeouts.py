import asyncio
import logging

async def fetch_with_timeout(url, timeout):
    logging.info(f"Fetching {url} with a timeout of {timeout} seconds")
    try:
        await asyncio.wait_for(asyncio.sleep(3), timeout=timeout)  # Simulate a delay that might exceed timeout
        logging.info("Fetch successful")
        return f"Data from {url}"
    except asyncio.TimeoutError:
        logging.error("Fetch timed out")
        return None

async def main():
    result = await fetch_with_timeout("http://example.com", 2)
    if result is None:
        logging.info("Operation timed out")
    else:
        logging.info(f"Received: {result}")

if __name__ == "__main__":
    asyncio.run(main()) 