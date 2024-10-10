def warshall_algorithm(n, adjacency_matrix):
    # Initialize the transitive closure matrix
    transitive_closure = [[adjacency_matrix[i][j] for j in range(n)] for i in range(n)]

    # Apply Warshall's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                transitive_closure[i][j] = transitive_closure[i][j] or (transitive_closure[i][k] and transitive_closure[k][j])

    return transitive_closure

def main():
    n = int(input("Enter the number of vertices: "))
    adjacency_matrix = []

    print("Enter the adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    transitive_closure = warshall_algorithm(n, adjacency_matrix)

    print("Transitive closure:")
    for row in transitive_closure:
        print("\t".join(map(str, row)))

if __name__ == "__main__":
    main()