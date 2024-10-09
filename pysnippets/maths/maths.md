# Mathematics - PySnippets

Wellcome To PySnippet's Mathematics Module Section, This Section Contains The Documatation Of Each And Every Function That Is Available In The Mathematics Module.

## Table of Contents

- [Introduction](#introduction)
- [Matrix Operations](#matrix-operations)
  - [Matrix Inverse](#matrix-inverse)
  - [Matrix Addition](#matrix-addition)
  - [Matrix Transpose](#matrix-transpose)
  - [Matrix Multiplication](#matrix-multiplication)
  - [Matrix Sclar Multiplication](#matrix-sclar-multiplication)
- [Determinant](#determinant)
  - [Determinant](#determinant-of-a-matrix)
  - [Minor](#minor)
  - [Cofactor](#cofactor)
  - [Adjugate](#adjugate)
- [Complex Numbers](#complex-numbers)
  - [Complex Addition](#complex-addition)
  - [Complex Conjugate](#complex-conjugate)

---

## Introduction

The **Mathematics Module** simplifies the handling of matrix operations and complex numbers. It is designed to be easy to use with clean syntax and built-in error handling for invalid inputs.

---

## Matrix Operations

### Matrix Inverse

Calculates the inverse of a square matrix.

```python
matrix_inverse(matrix)
```

- **Args**: A square matrix `matrix`.
- **Returns**: The inverse of the matrix.
- **Example**:
  ```python
  >>> matrix_inverse([[1, 2], [3, 4]])
  [[-2.0, 1.0], [1.5, -0.5]]
  ```

### Matrix Addition

Performs element-wise addition of two matrices.

```python
matrix_addition(matrix_a, matrix_b)
```

- **Args**: Two matrices `matrix_a` and `matrix_b`.
- **Returns**: The resulting matrix after addition.
- **Example**:
  ```python
  >>> matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]])
  [[6, 8], [10, 12]]
  ```

### Matrix Multiplication

Multiplies two matrices using matrix multiplication rules.

```python
matrix_multiplication(matrix_a, matrix_b)
```

- **Args**: Two matrices `matrix_a` and `matrix_b`.
- **Returns**: The product matrix.
- **Example**:
  ```python
  >>> matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]])
  [[19, 22], [43, 50]]
  ```

### Matrix Transpose

Calculates the transpose of a given matrix.

```python
transpose(matrix)
```

- **Args**: A matrix `matrix`.
- **Returns**: The transposed matrix.
- **Example**:
  ```python
  >>> matrix_transpose([[1, 2], [3, 4]])
  [[1, 3], [2, 4]]
  ```

### Matrix Scalar Multiplication

Multiplies a matrix by a scalar value.

```python
matrix_scalar_multiplication(matrix, scalar)
```

- **Args**: A matrix `matrix` and a scalar value `scalar`.
- **Returns**: The resulting matrix after scalar multiplication.
- **Example**:
  ```python
  >>> matrix_scalar_multiplication([[1, 2], [3, 4]], 2)
  [[2, 4], [6, 8]]
  ```

---

## Determinant

### Determinant of a Matrix

Calculates the determinant of a square matrix.

```python
determinant(matrix)
```

- **Args**: A square matrix `matrix`.
- **Returns**: The determinant of the matrix.
- **Example**:
  ```python
  >>> determinant([[1, 2], [3, 4]])
  -2
  ```

### Minor

Calculates the minor of a matrix element.

```python
minor(matrix, row, col)
```

- **Args**: A matrix `matrix`, row index `row`, and column index `col`.
- **Returns**: The minor of the element at the specified row and column.
- **Example**:
  ```python
  >>> minor([[1, 2], [3, 4]], 0, 0)
  4
  ```

### Cofactor

Calculates the cofactor of a matrix element.

```python
cofactor(matrix, row, col)
```

- **Args**: A matrix `matrix`, row index `row`, and column index `col`.
- **Returns**: The cofactor of the element at the specified row and column.
- **Example**:
  ```python
  >>> cofactor([[1, 2], [3, 4]], 0, 0)
  4
  ```

---

## Complex Numbers

### Complex Addition

Adds two complex numbers.

```python
complex_addition(complex_a, complex_b)
```

- **Args**: Two complex numbers `complex_a` and `complex_b`.
- **Returns**: The sum of the complex numbers.
- **Example**:
  ```python
  >>> complex_addition(1 + 2j, 3 + 4j)
  (4+6j)
  ```

### Complex Conjugate

Finds the conjugate of a complex number.

```python
complex_conjugate(complex_number)
```

- **Args**: A complex number `complex_number`.
- **Returns**: The conjugate of the complex number.
- **Example**:
  ```python
  >>> complex_conjugate(3 + 4j)
  (3-4j)
  ```

---
