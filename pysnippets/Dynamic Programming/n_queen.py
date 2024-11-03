n = int(input("Enter the value of N: "))
board = [[0 for _ in range(n)] for _ in range(n)]

def check_column(board, row, column):
    for i in range(row, -1, -1):
        if board[i][column] == 1:
            return False
    return True

def check_diagonal(board, row, column):
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, n, 1)):
        if board[i][j] == 1:
            return False
    return True


total_solutions = 0
def nqueen(board, row):
    global total_solutions
    if row == n:
        total_solutions += 1
        print("Solution:")
        for row in board:
            print(row)
        print()
        return True

    for i in range(n):
        if check_column(board, row, i) and check_diagonal(board, row, i):
            board[row][i] = 1
            nqueen(board, row + 1)
            board[row][i] = 0

if __name__ == "__main__":
    nqueen(board, 0)
    print(f"Total possible solutions for  {n}= {total_solutions}")
    