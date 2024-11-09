import logging
from dataclasses import dataclass
from pysnippets.Memoisation.decorator import memoize

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class FibonacciCalculator:
    @staticmethod
    @memoize
    def fibonacci(n: int) -> int:
        if n <= 0:
            raise ValueError("Input must be a positive integer.")
        elif n == 1 or n == 2:
            return 1
        return FibonacciCalculator.fibonacci(n-1) + FibonacciCalculator.fibonacci(n-2) 