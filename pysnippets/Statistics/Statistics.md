# Statistics Module - PySnippets

Welcome to the **Statistics Module**! This module provides a collection of statistical functions to aid in data analysis. It includes functions for calculating the mean, median, mode, quantiles, variance, standard deviation, and Z-score normalization of a dataset.

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
- [Usage Examples](#usage-examples)

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


Feel free to reach out if you have any questions about how to use the Statistics Module!
