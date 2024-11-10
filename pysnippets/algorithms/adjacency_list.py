class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

def create_graph(adj_list, edges):
    no_of_nodes = len(adj_list)
    for i, neighbors in edges.items():
        last = None
        for val in neighbors:
            if val >= no_of_nodes or val < 0:
                raise ValueError(f"Invalid node value {val}. It must be between 0 and {no_of_nodes - 1}.")
            new_node = Node(val)
            if adj_list[i] is None:
                adj_list[i] = new_node
            else:
                last.next = new_node
            last = new_node

def display_graph(adj_list):
    result = []
    for i, node in enumerate(adj_list):
        node_list = [i]
        ptr = node
        while ptr:
            node_list.append(ptr.vertex)
            ptr = ptr.next
        result.append(node_list)
    return result  # Return the adjacency list as a nested list structure

def delete_graph(adj_list):
    for i in range(len(adj_list)):
        ptr = adj_list[i]
        while ptr:
            temp = ptr
            ptr = ptr.next
            del temp
        adj_list[i] = None

if __name__ == "__main__":
    # Sample input to simulate the original manual entry example
    no_of_nodes = 5
    edges = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [2, 1, 4],
        4: [3]
    }

    # Initialize adjacency list with None for each node
    adj_list = [None] * no_of_nodes

    # Create, display, and then delete the graph
    create_graph(adj_list, edges)
    print("The adjacency list is given by:")
    for line in display_graph(adj_list):
        print(" --> ".join(map(str, line)))
    delete_graph(adj_list)
