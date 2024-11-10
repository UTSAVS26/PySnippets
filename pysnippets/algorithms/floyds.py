def floyds(cost_matrix):
    """
    Implements the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.

    Args:
        cost_matrix (list of list): The adjacency matrix representing the graph's edge weights.

    Returns:
        list of list: The shortest path matrix for all pairs of vertices.
    """
    n = len(cost_matrix)
    # Create a copy of the cost matrix to store shortest paths
    dist = [row[:] for row in cost_matrix]  # Make a deep copy

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update the distance if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def main():
    """
    Main function to input the graph and compute the shortest paths using Floyd-Warshall algorithm.
    """
    try:
        n = int(input("Enter the number of vertices: "))
        if n <= 0:
            raise ValueError("Number of vertices must be a positive integer.")

        print("Enter the cost matrix (use space-separated integers for each row):")
        cost_matrix = []
        for i in range(n):
            row = list(map(int, input(f"Enter row {i+1}: ").split()))
            if len(row) != n:
                raise ValueError("Each row must have the same number of elements as the number of vertices.")
            cost_matrix.append(row)

        # Floyd-Warshall algorithm to calculate shortest paths
        shortest_paths = floyds(cost_matrix)

        # Output the shortest path matrix
        print("\nAll Pairs Shortest Paths:")
        for i in range(n):
            for j in range(n):
                if shortest_paths[i][j] == float('inf'):
                    print(f"{'∞':>3}", end="  ")
                else:
                    print(f"{shortest_paths[i][j]:>3}", end="  ")
            print()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()