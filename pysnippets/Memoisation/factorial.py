import logging
from dataclasses import dataclass
from pysnippets.Memoisation.decorator import memoize

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class FactorialCalculator:
    @staticmethod
    @memoize
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        elif n == 0 or n == 1:
            return 1
        return n * FactorialCalculator.factorial(n - 1) 