def warshall_algorithm(n, adjacency_matrix):
    """
    Applies Warshall's algorithm to find the transitive closure of a directed graph.

    Args:
        n (int): The number of vertices in the graph.
        adjacency_matrix (list of list): The adjacency matrix representing the graph.

    Returns:
        list of list: The transitive closure matrix.
    """
    # Initialize the transitive closure matrix
    transitive_closure = [[adjacency_matrix[i][j] for j in range(n)] for i in range(n)]

    # Apply Warshall's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update the transitive closure matrix if a path exists through vertex k
                if transitive_closure[i][j] == 0:  # Only update if it's currently 0
                    transitive_closure[i][j] = transitive_closure[i][k] and transitive_closure[k][j]

    return transitive_closure

def main():
    try:
        n = int(input("Enter the number of vertices: "))
        if n <= 0:
            print("The number of vertices must be positive!")
            return

        adjacency_matrix = []

        print("Enter the adjacency matrix (each row of the matrix should be space-separated values):")
        for i in range(n):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            if len(row) != n:
                print(f"Row {i + 1} does not contain {n} elements. Please try again.")
                return
            adjacency_matrix.append(row)

        transitive_closure = warshall_algorithm(n, adjacency_matrix)

        print("Transitive closure:")
        for row in transitive_closure:
            print("\t".join(map(str, row)))

    except ValueError:
        print("Invalid input! Please enter integers.")

if __name__ == "__main__":
    main()