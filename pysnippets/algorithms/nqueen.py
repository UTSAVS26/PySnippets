def display(board):
    """Display the N-Queens board solution."""
    for row in board:
        print(" ".join(row))
    print("\n")

def place(t, i):
    """Check if the queen can be placed at the current position without conflicts."""
    for j in range(i):
        if t[i] == t[j] or abs(t[i] - t[j]) == abs(i - j):
            return False
    return True

def n_queens(n):
    """Solve the N-Queens problem and return all solutions as lists of boards."""
    t = [0] * n
    solutions = []
    s = 0

    def solve(i):
        nonlocal s
        if i == n:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for k in range(n):
                board[k][t[k]] = 'Q'
            solutions.append(board)
            s += 1
        else:
            for t[i] in range(n):
                if place(t, i):
                    solve(i + 1)

    solve(0)
    return solutions

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    solutions = n_queens(n)
    for index, solution in enumerate(solutions, start=1):
        print(f"The {index} solution")
        display(solution)
