# Recursion Code Snippets

Welcome to the Recursion Code Snippets repository! This collection is designed to provide a comprehensive set of examples and explanations for various recursive algorithms and techniques. Whether you are a beginner looking to understand the basics of recursion or an advanced programmer seeking to refine your skills, this repository has something for you.

## Table of Contents

1. [Introduction to Recursion](#introduction-to-recursion)
2. [Basic Recursion Examples](#basic-recursion-examples)
    - [Factorial](#factorial)
    - [Fibonacci Sequence](#fibonacci-sequence)
3. [Intermediate Recursion Examples](#intermediate-recursion-examples)
    - [Binary Search](#binary-search)
    - [Tower of Hanoi](#tower-of-hanoi)
4. [Advanced Recursion Examples](#advanced-recursion-examples)
    - [Merge Sort](#merge-sort)
    - [Quick Sort](#quick-sort)
5. [Tail Recursion](#tail-recursion)
6. [Memoization and Dynamic Programming](#memoization-and-dynamic-programming)
7. [Common Pitfalls and Best Practices](#common-pitfalls-and-best-practices)
8. [References and Further Reading](#references-and-further-reading)

## Introduction to Recursion

Recursion is a powerful technique in computer science where a function calls itself in order to solve a problem. It is often used to break down complex problems into simpler, more manageable sub-problems. Understanding recursion is essential for tackling many algorithmic challenges.

## Basic Recursion Examples

### Factorial

The factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n`. It is denoted by `n!`.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### Fibonacci Sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

## Intermediate Recursion Examples

### Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half.

```python
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
```

### Tower of Hanoi

The Tower of Hanoi is a mathematical puzzle where you have three rods and a number of disks of different sizes which can slide onto any rod.

```python
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)
```

## Advanced Recursion Examples

### Merge Sort

Merge sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

### Quick Sort

Quick sort is an efficient, in-place, comparison-based, divide and conquer sorting algorithm.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
```

## Tail Recursion

Tail recursion is a special case of recursion where the recursive call is the last operation in the function. This can be optimized by the compiler to improve performance.

```python
def tail_recursive_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_recursive_factorial(n - 1, n * accumulator)
```

## Memoization and Dynamic Programming

Memoization is an optimization technique used to speed up recursive algorithms by storing the results of expensive function calls and reusing them when the same inputs occur again.

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]
```

## Common Pitfalls and Best Practices

- **Base Case:** Always ensure that your recursive function has a base case to prevent infinite recursion.
- **Stack Overflow:** Be mindful of the maximum recursion depth in Python, which can lead to a stack overflow.
- **Efficiency:** Use memoization or iterative solutions for problems with overlapping subproblems to improve efficiency.
- **Readability:** Keep your recursive functions clean and readable by clearly defining the base case and recursive case.

## References and Further Reading

- [Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein](https://mitpress.mit.edu/books/introduction-algorithms)
- [The Art of Computer Programming by Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/taocp.html)
- [Python Documentation on Recursion](https://docs.python.org/3/tutorial/datastructures.html#recursion)

Thank you for exploring the Recursion Code Snippets repository. We hope these examples and explanations help you master the art of recursion. Happy coding!