def create_graph(adj, no_of_nodes, neighbors_info, is_directed=False):
    """
    Creates an adjacency matrix for a graph.

    Parameters:
    adj (list): The adjacency matrix to be updated.
    no_of_nodes (int): The number of nodes in the graph.
    neighbors_info (dict): A dictionary where keys are node indices and values are lists of neighbors.
    is_directed (bool): Flag indicating if the graph is directed. Default is False (undirected graph).
    """
    for i in range(no_of_nodes):
        # Initialize the adjacency matrix for each node
        adj[i] = [0] * no_of_nodes
        neighbors = neighbors_info.get(i, [])
        
        # Update the adjacency matrix for neighbors
        for neighbor in neighbors:
            adj[i][neighbor] = 1
            if not is_directed:
                adj[neighbor][i] = 1  # Add reverse edge for undirected graphs

def display_graph(adj, no_of_nodes):
    """
    Displays the adjacency matrix of the graph.

    Parameters:
    adj (list): The adjacency matrix to display.
    no_of_nodes (int): The number of nodes in the graph.
    """
    print("\nThe adjacency matrix is:")
    # Print the column headers (vertices)
    print("\t", end="")
    for i in range(no_of_nodes):
        print(f"v{i+1}\t", end="")
    print()
    
    # Print the adjacency matrix
    for i in range(no_of_nodes):
        print(f"v{i+1}\t", end="")
        for j in range(no_of_nodes):
            print(f"{adj[i][j]}\t", end="")
        print()

if __name__ == "__main__":
    # Input section
    no_of_nodes = 5
    neighbors_info = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [2, 1, 4],
        4: [3]
    }

    adj = [[0] * no_of_nodes for _ in range(no_of_nodes)]
    
    # Set is_directed to True for a directed graph, False for an undirected graph
    is_directed = False
    
    # Create the graph (adjacency matrix)
    create_graph(adj, no_of_nodes, neighbors_info, is_directed)
    
    # Display the adjacency matrix
    display_graph(adj, no_of_nodes)