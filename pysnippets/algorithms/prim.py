import heapq

def prim(graph, start):
    """
    Performs Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.

    Args:
        graph (dict): The graph represented as an adjacency list where keys are nodes, and values are lists of tuples (neighbor, weight).
        start (str): The starting node for the algorithm.

    Returns:
        list: A list of edges representing the Minimum Spanning Tree (MST).

    Example:
        >>> graph = {
        ... 'A': [('B', 1), ('C', 4)],
        ... 'B': [('A', 1), ('C', 2), ('D', 5)],
        ... 'C': [('A', 4), ('B', 2), ('D', 1)],
        ... 'D': [('B', 5), ('C', 1)]
        ... }
        >>> prim(graph, 'A')
        [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)]
    """
    if not graph or start not in graph:
        raise ValueError("Graph is empty or the starting node is not in the graph.")
    
    priority_queue = [(0, start, None)]
    mst = []
    visited = set()

    while priority_queue:
        weight, current_node, from_node = heapq.heappop(priority_queue)

        # Skip already visited nodes
        if current_node in visited:
            continue

        visited.add(current_node)

        if from_node is not None:
            mst.append((from_node, current_node, weight))

        for neighbor, edge_weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))

    if len(visited) != len(graph):
        print("Warning: The graph is disconnected, not all nodes are included in the MST.")

    return mst

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    mst = prim(graph, 'A')
    print(mst)  # Output: [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)]