import asyncio
import logging

class AsyncContextManager:
    async def __aenter__(self):
        logging.info("Enter context")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        logging.info("Exit context")

async def main():
    async with AsyncContextManager():
        logging.info("Doing work inside the context")

if __name__ == "__main__":
    asyncio.run(main()) 