import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class Fibonacci:
    n: int

    def calculate(self) -> int:
        if self.n < 0:
            raise ValueError("Input must be a non-negative integer")
        return self._fibonacci_recursive(self.n)

    def _fibonacci_recursive(self, current: int) -> int:
        if current in (0, 1):
            return current
        result = self._fibonacci_recursive(current - 1) + self._fibonacci_recursive(current - 2)
        logging.info(f"Fibonacci({current}) = {result}")
        return result

# Sample usage
if __name__ == "__main__":
    fib_instance = Fibonacci(10)
    print(f"Fibonacci of 10 is {fib_instance.calculate()}")  # Output: 55 