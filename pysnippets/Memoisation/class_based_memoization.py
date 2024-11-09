import logging
from dataclasses import dataclass, field
from typing import Dict, Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Memoizer:
    cache: Dict[Tuple, int] = field(default_factory=dict)
    
    def memoize(self, func):
        def wrapper(*args):
            try:
                if args in self.cache:
                    logger.info(f"Fetching from cache for args: {args}")
                    return self.cache[args]
                result = func(*args)
                self.cache[args] = result
                logger.info(f"Caching result for args: {args}")
                return result
            except Exception as e:
                logger.error(f"Error in Memoizer: {e}")
                raise
        return wrapper

@dataclass
class CombinatorialCalculator:
    memoizer: Memoizer = field(default_factory=Memoizer)
    
    @staticmethod
    def combination(n: int, k: int) -> int:
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return CombinatorialCalculator.combination(n-1, k-1) + CombinatorialCalculator.combination(n-1, k)
    
    def get_combination(self, n: int, k: int) -> int:
        decorated_combination = self.memoizer.memoize(CombinatorialCalculator.combination)
        return decorated_combination(n, k) 