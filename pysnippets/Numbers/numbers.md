# Number Formatting - PySnippets

Welcome to the **Number Formatting** module! This lightweight utility provides functionality to format numbers by adding commas as thousand separators, making large numbers easier to read.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [Format Number](#format-number)
  - [Format To 2 Decimal Places](#formatting-to-2-decimal-places)
  - [Pad With Zeros](#pad-with-zeros)
  - [Percentage Format](#percentage-format)
  - [Prime Factoriztion](#prime-factorization)
- [Usage Example](#usage-example)

---

## Introduction

The **Number Formatting** module is designed to enhance the readability of numerical values by formatting them with commas as thousand separators. This is particularly useful for displaying currency values, population counts, or any large numbers in a more user-friendly way.

---

## Functionality

### Format Number

This function takes a number as input and returns it as a formatted string with commas.

```python
format_number(num)
```

- **Args**:
  - `num` (int, float): The number to format.
- **Returns**:
  - `str`: The formatted number as a string.
- **Example**:
  ```python
  >>> format_number(1234567)
  '1,234,567'
  ```

---

### Formatting to 2 Decimal Places

This module provides a function to format a number to two decimal places.

- **Args**:
  - `num` (float or int): The number to format.
- **Returns**:
  - `str`: The formatted number as a string with two decimal places.
- **Example**:
  ```python
  >>> format_to_2_decimal(123.456)
  '123.46'
  ```

### pad_with_zeros

- **Args**:
  - `num` (int): The number to pad.
  - `width` (int): The total width of the output string.
- **Returns**:
  - `str`: The padded number as a string.
- **Example**:

  ```python
  from pad_with_zeros import pad_with_zeros

  print(pad_with_zeros(123, 6)) # Outputs: 000123
  ```

### percentage_format

- **Args**:
  - `num` (float or int): The part value.
  - `total` (float or int): The total value.
  - `decimals` (int, optional): The number of decimal places.
- **Returns**:
  - `str`: The formatted percentage as a string.
- **Example**:

  ```python
  from percentage_format import percentage_format

  print(percentage_format(50, 200)) # Outputs: 25.00%
  ```

### prime_factorization

- **Args**:

  - `num` (int): The number to factorize.

- **Returns**:
  - `list`: A list of prime factors.
- **Example**:

  ```python
  >>> prime_factorization(28)
  [2, 2, 7]
  ```
