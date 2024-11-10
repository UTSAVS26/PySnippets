# Complex Number Python Package

A comprehensive Python package for performing complex number operations with ease and efficiency. This package provides a robust set of tools to handle complex arithmetic, parsing, and advanced operations, accompanied by thorough logging and error handling mechanisms.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Creating Complex Numbers](#creating-complex-numbers)
  - [Arithmetic Operations](#arithmetic-operations)
  - [Advanced Operations](#advanced-operations)
  - [Parsing Complex Numbers](#parsing-complex-numbers)
- [API Reference](#api-reference)
  - [Classes](#classes)
    - [ComplexNumber](#complexnumber)
  - [Functions](#functions)
    - [power](#power)
    - [parse_complex](#parse_complex)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Arithmetic Operations:** Addition, subtraction, multiplication, and division of complex numbers.
  - `add(self, other: 'ComplexNumber') -> 'ComplexNumber'`: Adds two complex numbers.
  - `subtract(self, other: 'ComplexNumber') -> 'ComplexNumber'`: Subtracts one complex number from another.
  - `multiply(self, other: 'ComplexNumber') -> 'ComplexNumber'`: Multiplies two complex numbers.
  - `divide(self, other: 'ComplexNumber') -> 'ComplexNumber'`: Divides one complex number by another.
- **Advanced Operations:** Magnitude calculation, conjugation, and exponentiation.
  - `magnitude(self) -> float`: Calculates the magnitude of a complex number.
  - `conjugate(self) -> 'ComplexNumber'`: Calculates the conjugate of a complex number.
- **Parsing:** Convert string representations of complex numbers into `ComplexNumber` objects.
  - `parse_complex(complex_str: str) -> 'ComplexNumber'`: Parses a string representation of a complex number into a `ComplexNumber` object.
- **Logging:** Detailed logging of operations for debugging and monitoring.
- **Error Handling:** Custom exceptions for robust error management.
  - `ComplexNumberError(Exception)`: Base exception class for ComplexNumber operations.
  - `DivisionByZeroError(ComplexNumberError)`: Exception raised when attempting to divide by zero.
- **Testing:** Comprehensive unit tests ensuring reliability and correctness.

## Installation

Ensure you have Python 3.6 or higher installed. You can install the package using `pip`:
```bash
pip install pysnippets-complex-number
```

Alternatively, clone the repository and install manually:

```bash
git clone https://github.com/yourusername/pysnippets-complex-number.git
cd pysnippets-complex-number
pip install .
```
