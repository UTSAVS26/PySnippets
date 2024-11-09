import asyncio
import logging

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i
        logging.info(f"Yielded {i}")

async def main():
    async for value in async_generator():
        logging.info(f"Received {value}")

if __name__ == "__main__":
    asyncio.run(main()) 