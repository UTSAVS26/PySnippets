import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

@dataclass
class Factorial:
    n: int

    def calculate(self) -> int:
        if self.n < 0:
            raise ValueError("Input must be a non-negative integer")
        return self._factorial_recursive(self.n)

    def _factorial_recursive(self, current: int) -> int:
        if current == 0:
            return 1
        else:
            result = current * self._factorial_recursive(current - 1)
            logging.info(f"Factorial({current}) = {result}")
            return result

# Sample usage
if __name__ == "__main__":
    factorial_instance = Factorial(5)
    print(f"Factorial of 5 is {factorial_instance.calculate()}")  # Output: 120 