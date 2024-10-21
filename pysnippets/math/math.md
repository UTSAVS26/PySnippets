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
  - [Complex Substraction](#complex-substraction)
  - [Complex Multiplication](#complex-multiplication)
- [Vectors](#vectors)
  - [Vector Addition](#vector-addition)
  - [Vector Substraction](#vector-substraction)
  - [Scalar Multipication](#scalar-multipication)
  - [Dot Product](#dot-product)
  - [Cross Product](#cross-product)
  - [Vector Magnitude](#vector-magnitude)
  - [Vector Normalization](#vector-normalization)
  - [Angle Between Vectors](#angle-between-vectors)
  - [Projection](#projection)
- [Polynomial Addition](#polynomial-addition)

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

### Complex Substraction

Subtract the second complex number from the first.

- **Args**:
  c1 (tuple): The first complex number as (real, imag).
  c2 (tuple): The second complex number as (real, imag).

- **Returns**:
  tuple: The difference of the two complex numbers as (real, imag).

- **Example**:
  ```python
  >>> subtract_complex((5, 7), (2, 3))
  (3, 4)
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

### Complex Multiplication

Multiply two complex numbers.

- **Args**:
  c1 (tuple): The first complex number as (real, imag).
  c2 (tuple): The second complex number as (real, imag).

- **Returns**:
  tuple: The product of the two complex numbers as (real, imag).

- **Example**:
  ```python
    >>> multiply_complex((1, 2), (3, 4))
    (-5, 10)
  ```

---

## Vectors

### Vector Addition

Adds two vectors element-wise.

```python
vector_addition(vector1, vector2)
```

- **Args**:
  v1 (list of int/float): First vector.
  v2 (list of int/float): Second vector.
- **Returns**:
  list: The sum of the two vectors.
- **Example**:
  ```python
  >>> vector_addition([1, 2, 3], [4, 5, 6])
  [5, 7, 9]
  ```

### Vector Substraction

Subsract vector v2 from v1

- **Args**:
  v1 (list of int/float): First vector.
  v2 (list of int/float): Second vector.
- **Returns**:
  list: The difference of the two vectors.
- **Example**:
  ```python
  >>> vector_substraction([1, 2, 3], [4, 5, 6])
  [-3, -3, -3]
  ```

### Scalar Multipication

Multiply a vector v by a scalar

- **Args**:
  v (list of int/float): The vector.
  scalar (int/float): The scalar to multiply by.
- **Returns**:
  list: The resulting vector after scalar multiplication.
- **Example**:
  ```python
  >>> scalar_multiplication([1,2,3],3)
  [3,6,9]
  ```

### Dot Product

Comuter the dot product of two vectors v1 nd v2

- **Args**:
  v1 (list of int/float): First vector.
  v2 (list of int/float): Second vector.

- **Returns**:
  int/float: The dot product of the two vectors.

- **Examle**:
  ```python
  >>>dot_product([1,2,3],[4,5,6])
  32
  ```

### Cross Product

compute the cross product of two 3D vector

- **Args**:
  v1 (list of int/float): First vector (3D).
  v2 (list of int/float): Second vector (3D).

- **Returns**:
  List of int/flowt: The resulting vector of v1 and v2

- **Example**:
  ```python
  cross_product([1,0,0],[0,1,0])
  [0,0,1]
  ```

### Vector Magnitude

compute the magnitude (length) of a vector

- **Args**:
  v (list of int/float): The vector.

- **Returns**:
  float: The magnitude of the vector

- **Example**:
  ```python
  >>> vector_magnitude([3,4])
  5.0
  ```

### Vector Normalization

Normalize a vector (i.e., scale it to have a magnitude of 1).

- **Args**:
  v (list of int/float): The vector.

- **Returns**:
  list of float: The normalized vector.

- **Example**:
  ```
  >>> vector_normalization([3,4])
  [0.6, 0.8]
  ```

### Angle Between Vectors

Calculate the angle (in radians) between two vectors.

- **Args**:
  v1 (list of int/float): First vector.
  v2 (list of int/float): Second vector.

- **Returns**:
  float: The angle in radians between the two vectors.

- **Example**:
  ```python
      >>> angle_between_vectors(v1, v2)
      1.5707963267948966  # (90 degrees in radians)
  ```

### Projection

Project vector v1 onto vector v2.

- **Args**:
  v1 (list of int/float): First vector.
  v2 (list of int/float): Second vector.

- **Returns**:
  list of float: The projection of v1 onto v2.

- **Example**:
  ```python
  >>> projection(v1, v2)
  [0.6623376623376623, 0.827922077922078, 0.9935064935064936]
  ```
  
## Polynomial Addition

### Introduction
The Polynomial Addition feature in the PySnippets Mathematics Module allows users to easily perform addition of polynomials. This functionality is essential for various mathematical computations involving polynomial expressions.

### Function Overview
The following functions and classes are available for handling polynomial addition.

#### Polynomial Class
The `Polynomial` class is designed to handle polynomial terms and provide methods for polynomial operations.

##### Methods:
- **add_term(coefficient, power)**: Adds a term to the polynomial.
- **display()**: Returns a string representation of the polynomial.

### Adding Polynomials
The `add_polynomials` function combines multiple polynomials into a single polynomial.

#### Function Signature
```python
def add_polynomials(polynomials: List[Polynomial]) -> Polynomial:
