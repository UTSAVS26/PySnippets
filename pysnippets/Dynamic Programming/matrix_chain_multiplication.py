def f(arr, i, j):
    # Base condition
    if i == j:
        return 0
    
    mini = float('inf')
    
    # Partitioning loop
    for k in range(i, j):
        ans = f(arr, i, k) + f(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        mini = min(mini, ans)
    
    return mini

def matrix_multiplication(arr, N):
    i = 1
    j = N - 1
    return f(arr, i, j)

def main():
    arr = [5, 10, 15, 20, 25]
    n = len(arr)
    print("The minimum number of operations are", matrix_multiplication(arr, n))

if __name__ == "__main__":
    main()
