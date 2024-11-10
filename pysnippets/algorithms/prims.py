def prims(cost_matrix):
    n = len(cost_matrix)
    if n == 0:
        print("Empty graph, no edges to process.")
        return

    visited = [False] * n
    visited[0] = True  # Start with vertex 0
    mincost = 0
    edges_in_mst = 0

    while edges_in_mst < n - 1:
        min_edge = float('inf')
        a = b = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and cost_matrix[i][j] < min_edge:
                        min_edge = cost_matrix[i][j]
                        a, b = i, j

        if a != -1 and b != -1:  # Valid edge found
            print(f"Edge from vertex {a} to {b} with cost = {min_edge}")
            visited[b] = True
            mincost += min_edge
            cost_matrix[a][b] = cost_matrix[b][a] = float('inf')  # Avoid reusing this edge
            edges_in_mst += 1

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