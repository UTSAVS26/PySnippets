import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        try:
            if args in cache:
                logger.info(f"Fetching from cache for args: {args}")
                return cache[args]
            result = func(*args)
            cache[args] = result
            logger.info(f"Caching result for args: {args}")
            return result
        except Exception as e:
            logger.error(f"Error in memoize decorator: {e}")
            raise
    return wrapper 