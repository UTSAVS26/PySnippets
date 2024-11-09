from dataclasses import dataclass
import logging

from exceptions import DivisionByZeroError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ComplexNumber:
    real: float
    imaginary: float

    def add(self, other: 'ComplexNumber') -> 'ComplexNumber':
        result = ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        logger.info(f"Adding {self} + {other} = {result}")
        return result

    def subtract(self, other: 'ComplexNumber') -> 'ComplexNumber':
        result = ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        logger.info(f"Subtracting {self} - {other} = {result}")
        return result

    def multiply(self, other: 'ComplexNumber') -> 'ComplexNumber':
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        result = ComplexNumber(real, imaginary)
        logger.info(f"Multiplying {self} * {other} = {result}")
        return result

    def divide(self, other: 'ComplexNumber') -> 'ComplexNumber':
        try:
            denominator = other.real ** 2 + other.imaginary ** 2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            result = ComplexNumber(real, imaginary)
            logger.info(f"Dividing {self} / {other} = {result}")
            return result
        except ZeroDivisionError:
            raise DivisionByZeroError("Cannot divide by zero complex number.")

    def magnitude(self) -> float:
        mag = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        logger.info(f"Magnitude of {self} = {mag}")
        return mag

    def conjugate(self) -> 'ComplexNumber':
        result = ComplexNumber(self.real, -self.imaginary)
        logger.info(f"Conjugate of {self} = {result}")
        return result

    def __str__(self):
        return f"{self.real} + {self.imaginary}i" 