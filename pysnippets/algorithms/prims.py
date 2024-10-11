def prims(cost_matrix):
    n = len(cost_matrix)
    visited = [False] * n
    visited[0] = True
    mincost = 0
    ne = 0

    while ne < n - 1:
        min_edge = float('inf')
        a = b = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and cost_matrix[i][j] < min_edge:
                        min_edge = cost_matrix[i][j]
                        a, b = i, j

        print(f"Edge from vertex {a} to {b} with cost = {min_edge}")
        visited[b] = True
        mincost += min_edge
        cost_matrix[a][b] = cost_matrix[b][a] = float('inf')
        ne += 1

    print(f"Cost of MST: {mincost}")

def main():
    n = int(input("Enter the number of vertices: "))
    cost_matrix = []

    print("Enter the cost matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        cost_matrix.append(row)

    prims(cost_matrix)

if __name__ == "__main__":
    main()