import asyncio
import logging

async def cancellable_task():
    try:
        logging.info("Task started")
        await asyncio.sleep(10)  # Long running task
        logging.info("Task completed")
    except asyncio.CancelledError:
        logging.info("Task was cancelled")
        raise

async def main():
    task = asyncio.create_task(cancellable_task())
    await asyncio.sleep(1)  # Let the task start
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        logging.info("Main noticed that the task was cancelled")

if __name__ == "__main__":
    asyncio.run(main()) 