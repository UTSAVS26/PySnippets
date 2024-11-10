import asyncio
import logging

async def limited_access(sem, item):
    async with sem:
        logging.info(f"Processing {item}")
        await asyncio.sleep(2)  # Simulate work
        logging.info(f"Finished processing {item}")

async def main():
    sem = asyncio.Semaphore(2)  # Limit concurrent access to 2
    tasks = [asyncio.create_task(limited_access(sem, i)) for i in range(5)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
