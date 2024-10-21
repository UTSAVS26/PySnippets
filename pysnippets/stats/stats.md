# Statistics Module - PySnippets

Welcome to the **Statistics Module**! This module provides a collection of statistical functions to aid in data analysis. It includes functions for calculating the mean, median, mode, quantiles, variance, standard deviation, Z-score normalization, and more.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [Mean-Median-Mode](#mean-median-mode)
    - [Mean](#mean)
    - [Median](#median)
    - [Mode](#mode)
  - [Quantile](#quantile)
  - [Variance](#variance)
  - [Standard Deviation](#standard-deviation)
  - [Z-Score Normalization](#z-score-normalization)
  - [Coefficient of Variation](#coefficient-of-variation)
  - [Interquartile Range (IQR)](#interquartile-range-iqr)
  - [Kurtosis](#kurtosis)
  - [Skewness](#skewness)
  - [Correlation](#correlation)

---

## Introduction

The **Statistics Module** provides essential statistical functions that can be used for performing various calculations on numerical datasets. Each function is designed to operate on lists of numbers, enabling quick analysis and insight extraction.

---

## Functionality

### Mean-Median-Mode

### Mean

This function calculates the mean (average) of a list of numbers.

```python
mean(data)
```

- **Args**:
  - `data` (list): A list of numbers.
- **Returns**:
  - `float`: The mean of the numbers.
- **Example**:
  ```python
  >>> mean([1, 2, 3, 4])
  2.5
  ```

---

### Median

This function calculates the median of a list of numbers.

```python
median(data)
```

- **Args**:
  - `data` (list): A list of numbers.
- **Returns**:
  - `float`: The median of the numbers.
- **Example**:
  ```python
  >>> median([1, 2, 3, 4, 5])
  3
  ```

---

### Mode

This function calculates the mode of a list of numbers.

```python
mode(data)
```

- **Args**:
  - `data` (list): A list of numbers.
- **Returns**:
  - `int` or `float`: The mode of the numbers.
- **Example**:
  ```python
  >>> mode([1, 2, 2, 3, 4])
  2
  ```

---

### Quantile

This function calculates the q-th quantile of a list of numbers.

```python
quantile(data, q)
```

- **Args**:
  - `data` (list): A list of numbers.
  - `q` (float): The quantile to calculate (between 0 and 1).
- **Returns**:
  - `float`: The q-th quantile of the numbers.
- **Example**:
  ```python
  >>> quantile([1, 2, 3, 4, 5], 0.5)
  3
  ```

---

### Variance

This function calculates the variance of a list of numbers.

```python
variance(data, population=True)
```

- **Args**:
  - `data` (list): A list of numbers.
  - `population` (bool): If True, calculate population variance; otherwise, sample variance.
- **Returns**:
  - `float`: The variance of the numbers.
- **Example**:
  ```python
  >>> variance([1, 2, 3, 4], population=True)
  1.25
  ```

---

### Standard Deviation

This function calculates the standard deviation of a list of numbers.

```python
standard_deviation(data, population=True)
```

- **Args**:
  - `data` (list): A list of numbers.
  - `population` (bool): If True, calculate population standard deviation; otherwise, sample.
- **Returns**:
  - `float`: The standard deviation of the numbers.
- **Example**:
  ```python
  >>> standard_deviation([1, 2, 3, 4], population=True)
  1.118033988749895
  ```

---

### Z-Score Normalization

This function normalizes a list of numbers using Z-score normalization.

```python
z_score_normalization(data)
```

- **Args**:
  - `data` (list): A list of numbers.
- **Returns**:
  - `list`: The normalized values.
- **Example**:
  ```python
  >>> z_score_normalization([1, 2, 3, 4, 5])
  [-1.4142135623730951, -0.7071067811865475, 0.0, 0.7071067811865475, 1.4142135623730951]
  ```

---

### Coefficient of Variation

This function calculates the Coefficient of Variation (CV) of a list of numbers.

```python
coefficient_of_variation(data)
```

- **Args**:
  - `data` (list): A list of numbers.
- **Returns**:
  - `float`: The CV, expressed as a percentage.
- **Example**:
  ```python
  >>> coefficient_of_variation([10, 20, 30])
  57.735026918962575
  ```

---

### Interquartile Range (IQR)

This function calculates the Interquartile Range (IQR) of a list of numbers.

```python
iqr(data)
```

- **Args**:
  - `data` (list): A list of numbers.
- **Returns**:
  - `float`: The IQR of the numbers.
- **Example**:
  ```python
  >>> iqr([1, 2, 3, 4, 5, 6, 7, 8])
  4.0
  ```

---

### Kurtosis

This function calculates the kurtosis of a list of numbers.

```python
kurtosis(data)
```

- **Args**:
  - `data` (list): A list of numbers.
- **Returns**:
  - `float`: The kurtosis of the numbers.
- **Example**:
  ```python
  >>> kurtosis([1, 2, 3, 4, 5])
  -1.3
  ```

---

### Skewness

This function calculates the skewness of a list of numbers.

```python
skewness(data)
```

- **Args**:
  - `data` (list): A list of numbers.
- **Returns**:
  - `float`: The skewness of the numbers.
- **Example**:
  ```python
  >>> skewness([1, 2, 2, 3, 4])
  0.0
  ```

---

### Correlation

This function calculates the correlation between two lists of numbers.

```python
correlation(x, y)
```

- **Args**:
  - `x` (list): A list of independent variable values.
  - `y` (list): A list of dependent variable values.
- **Returns**:
  - `float`: The correlation coefficient.
- **Example**:
  ```python
  >>> correlation([1, 2, 3], [4, 5, 6])
  1.0
  ```
