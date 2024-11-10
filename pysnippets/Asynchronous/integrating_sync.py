import asyncio
import logging

def synchronous_function():
    logging.info("Running synchronous function")

async def main():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, synchronous_function)

if __name__ == "__main__":
    asyncio.run(main()) 