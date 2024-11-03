## Problem Statement
The N-Queens problem involves placing `N` queens on an `N x N` chessboard so that no two queens threaten each other. This means no two queens can be in the same row, column, or diagonal. Your goal is to find all possible solutions to place the queens on the board.

The input is a single integer `N`, representing the board size and the number of queens.

### Objective
- Print each valid configuration of the board where the queens are placed in non-threatening positions.
- Display the total number of valid solutions.

### Example
```plaintext
Input: N = 4

Output:
Solution:
[0, 0, 1, 0]
[1, 0, 0, 0]
[0, 0, 0, 1]
[0, 1, 0, 0]

Solution:
[0, 1, 0, 0]
[0, 0, 0, 1]
[1, 0, 0, 0]
[0, 0, 1, 0]

Total possible solutions for N=4: 2
```

### Constraints
- `N` is a positive integer.
- `1 <= N <= 10`

## Solution
This solution uses a **backtracking approach** to solve the N-Queens problem.

### Approach

**1. Board Initialization:**
   - Initialize a 2D list `board` with zeros, where `0` represents an empty cell and `1` represents a queen.

**2. Validity Checks:**
   - We need two helper functions, `check_column` and `check_diagonal`, to verify if placing a queen on a particular cell threatens any existing queens.
   - `check_column`: Checks if any queen is already placed in the same column in previous rows.
   - `check_diagonal`: Checks both the left and right diagonals to ensure no queen is on the path.

**3. Backtracking:**
   - The `nqueen` function places queens one by one, row by row. If a queen can be safely placed in a cell, the function places it and recursively calls itself to place the next queen in the next row.
   - If a solution is found (all queens are placed), it prints the board configuration and increments the solution count.
   - The function then removes the queen from the current cell and tries the next position (backtracking).

### Time and Space Complexity
- **Time Complexity:** `O(N!)` due to the factorial nature of permutations required to explore all possibilities.
- **Space Complexity:** `O(N^2)` to store the board configuration for each recursive call.

### Code Implementation

Python:
```python
n = int(input("Enter the value of N: "))
board = [[0 for _ in range(n)] for _ in range(n)]

def check_column(board, row, column):
    # Check if any queen is in the same column in previous rows
    for i in range(row, -1, -1):
        if board[i][column] == 1:
            return False
    return True

def check_diagonal(board, row, column):
    # Check left diagonal
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check right diagonal
    for i, j in zip(range(row, -1, -1), range(column, n, 1)):
        if board[i][j] == 1:
            return False
    return True

total_solutions = 0
def nqueen(board, row):
    global total_solutions
    # If all queens are placed, print the board and increment the solution count
    if row == n:
        total_solutions += 1
        print("Solution:")
        for row in board:
            print(row)
        print()
        return True

    # Try placing a queen in each column for the current row
    for i in range(n):
        if check_column(board, row, i) and check_diagonal(board, row, i):
            # Place queen
            board[row][i] = 1
            # Recurse to place queen in next row
            nqueen(board, row + 1)
            # Remove queen (backtrack)
            board[row][i] = 0

if __name__ == "__main__":
    nqueen(board, 0)
    print(f"Total possible solutions for N={n}: {total_solutions}")
```

### Conclusion
This backtracking solution efficiently finds all possible placements for `N` queens on an `N x N` board. The program systematically checks each cell, exploring all possible placements, and backtracks when a configuration does not work. This approach ensures that every valid solution is found.