def create_graph(adj, no_of_nodes, neighbors_info):
    for i in range(no_of_nodes):
        adj[i] = [0] * no_of_nodes
        neighbors = neighbors_info.get(i, [])
        for neighbor in neighbors:
            adj[i][neighbor] = 1

def display_graph(adj, no_of_nodes):
    print("\nThe adjacency matrix is:")
    print("\t", end="")
    for i in range(no_of_nodes):
        print(f"v{i+1}\t", end="")
    print()
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
    create_graph(adj, no_of_nodes, neighbors_info)
    display_graph(adj, no_of_nodes)
