from collections import deque

def topological_ordering():
    n = int(input("Enter the number of vertices: "))
    adj_matrix = []
    print("Enter the adjacency matrix:")
    
    for i in range(n):
        adj_matrix.append(list(map(int, input().split())))
    
    # Step 1: Calculate the in-degrees of each vertex
    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                in_degree[j] += 1

    # Step 2: Use a queue to keep track of vertices with zero in-degree
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    top_order = []

    while queue:
        node = queue.popleft()
        top_order.append(node + 1)  # Store 1-indexed node

        # Reduce the in-degree of all neighbors
        for i in range(n):
            if adj_matrix[node][i] == 1:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

    if len(top_order) != n:
        print("There exists a cycle in the graph. Topological ordering is not possible.")
    else:
        print("Topological Ordering: ", ' '.join(map(str, top_order)))

if __name__ == "__main__":
    topological_ordering()