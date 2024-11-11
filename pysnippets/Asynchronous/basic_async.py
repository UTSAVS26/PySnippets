import asyncio
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def greet(name):
    """Simple async function that simulates a delayed greeting with error handling"""
    try:
        logging.info(f"Starting greeting for {name}")
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
            
        await asyncio.sleep(1)  # Simulate some async work
        logging.info(f"Hello, {name}!")
        return f"Greeting completed for {name}"
    except ValueError as e:
        logging.error(f"ValueError in greet: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error in greet: {e}")
        raise

async def process_names(names):
    """Process multiple greetings concurrently with error handling"""
    try:
        logging.info("Starting to process names")
        if not names:
            raise ValueError("Names list cannot be empty")
            
        tasks = [asyncio.create_task(greet(name)) for name in names]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter out exceptions and log them
        processed_results = []
        for result in results:
            if isinstance(result, Exception):
                logging.error(f"Error during processing: {result}")
            else:
                processed_results.append(result)
                
        return processed_results
    except ValueError as e:
        logging.error(f"ValueError in process_names: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error in process_names: {e}")
        raise

async def main():
    try:
        # List of names to greet, including some that will cause errors
        names = ["Alice", "Bob", "Charlie", 123, None]
        
        # Process all greetings concurrently
        results = await process_names(names)
        
        # Log successful results
        for result in results:
            logging.info(result)
            
    except ValueError as e:
        logging.error(f"ValueError in main: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in main: {e}")
    finally:
        logging.info("Finished processing all greetings")

if __name__ == "__main__":
    asyncio.run(main())