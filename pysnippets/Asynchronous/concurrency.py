import asyncio
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def task(name, delay):
    """Simulates an async task with a delay"""
    logging.info(f"Task {name} starting")
    await asyncio.sleep(delay)
    logging.info(f"Task {name} completed")
    return f"Result from task {name}"

async def main():
    # Create multiple tasks to run concurrently
    tasks = [
        asyncio.create_task(task("A", 2)),
        asyncio.create_task(task("B", 1)),
        asyncio.create_task(task("C", 3))
    ]
    
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    
    # Process results
    for result in results:
        logging.info(result)

if __name__ == "__main__":
    asyncio.run(main())