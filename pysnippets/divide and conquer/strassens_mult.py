def mult(mat1, mat2, row, col, n, ans):
    if n > 2:
        mult(mat1, mat2, row, col, int(n / 2), ans)
        mult(mat1, mat2, row + int(n / 2), col, int(n / 2), ans)
        mult(mat1, mat2, row, col + int(n / 2), int(n / 2), ans)
        mult(mat1, mat2, row + int(n / 2), col + int(n / 2), int(n / 2), ans)
    elif n == 2:
        a = (mat1[row][col] + mat1[row + 1][col + 1]) * (mat2[row][col] + mat2[row + 1][col + 1])
        b = (mat1[row + 1][col] + mat1[row + 1][col + 1]) * (mat2[row][col])
        c = (mat2[row][col + 1] - mat2[row + 1][col + 1]) * (mat1[row][col])
        d = (mat2[row + 1][col] - mat2[row][col]) * (mat1[row + 1][col + 1])
        e = (mat1[row][col] + mat1[row][col + 1]) * (mat2[row + 1][col + 1])
        f = (mat1[row + 1][col] - mat1[row][col]) * (mat2[row][col] + mat2[row][col + 1])
        g = (mat1[row][col + 1] - mat1[row + 1][col + 1]) * (mat2[row + 1][col] + mat2[row + 1][col + 1])
        
        ans[row][col] = a + d - e + g
        ans[row][col + 1] = c + e
        ans[row + 1][col] = b + d
        ans[row + 1][col + 1] = a + c - b + f

# Predefined 4x4 matrices
mat1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

mat2 = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

# Initialize answer matrix
n = 4
ans = [[0 for _ in range(n)] for _ in range(n)]

# Perform matrix multiplication
mult(mat1, mat2, 0, 0, n, ans)

# Display result
print("Matrix multiplied:")
for row in ans:
    print(" ".join(map(str, row)))
