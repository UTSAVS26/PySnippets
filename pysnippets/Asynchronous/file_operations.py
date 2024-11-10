import asyncio
import aiofiles
import logging

async def read_file_async(path):
    async with aiofiles.open(path, mode='r') as file:
        content = await file.read()
        logging.info(f"Read content: {content[:100]}")  # Display first 100 characters
    return content

async def main():
    await read_file_async('example.txt')
    logging.info("File read successfully")

if __name__ == "__main__":
    asyncio.run(main()) 