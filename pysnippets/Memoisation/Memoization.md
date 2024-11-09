# Memoisation Module

## Overview

The **Memoisation** module is a comprehensive collection of mathematical and algorithmic functions optimized with memoization techniques to significantly enhance performance by caching previously computed results. This approach is particularly beneficial for functions that involve expensive recursive calls, such as those commonly found in combinatorial mathematics, dynamic programming, and other computationally intensive applications. By leveraging memoization, the module reduces the computational overhead of repetitive calculations, leading to substantial improvements in execution speed and efficiency.

## Features

- **Memoizer Class**: A class-based memoization decorator designed to cache function results based on input arguments. This allows for the efficient reuse of previously computed values, reducing the need for redundant calculations. The Memoizer Class is a versatile tool that can be applied to a wide range of functions, making it an essential component of the module.
- **Combinatorial Calculations**: The module includes optimized functions for computing combinations efficiently using memoization. This is particularly useful for problems involving permutations, combinations, and other combinatorial calculations that can be computationally expensive without memoization.
- **Mathematical Functions**: The module provides a suite of mathematical functions that have been optimized using memoization techniques:
  - **Factorial**: Calculate the factorial of a number with caching. This function leverages memoization to store previously computed factorials, ensuring that subsequent calculations are performed efficiently.
  - **Fibonacci**: Compute Fibonacci numbers efficiently. The Fibonacci function utilizes memoization to cache previously computed values, reducing the computational complexity of calculating Fibonacci numbers.
  - **Longest Common Subsequence (LCS)**: Determine the length of the LCS between two strings. This function employs memoization to cache intermediate results, making it more efficient than traditional recursive approaches.
  - **Knapsack Solver**: Solve the classic knapsack problem using memoization. The Knapsack Solver function leverages memoization to cache solutions to subproblems, reducing the computational overhead of solving this complex problem.

## Usage and Instructions

To utilize the Memoisation module effectively, follow these steps:

1. **Installation**: Ensure you have Python 3.6 or later installed. Clone the repository and navigate to the project directory.
2. **Importing the Module**: Import the Memoisation module in your Python script or project using `import memoisation`.
3. **Function Usage**: Use the provided functions as you would any other Python function. For example, to calculate the factorial of a number, use `memoisation.factorial(number)`.
4. **Memoizer Class**: To apply memoization to a custom function, use the `@memoisation.memoizer` decorator. This will enable caching of function results based on input arguments.

By following these instructions and leveraging the features of the Memoisation module, you can significantly improve the performance of your Python applications that involve computationally intensive mathematical and algorithmic operations.