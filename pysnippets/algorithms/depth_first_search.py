def dfs(graph, start, visited=None):
    """
    Performs Depth First Search (DFS) traversal on a graph.

    Args:
        graph (dict): The adjacency list representing the graph.
        start (str): The starting node for DFS traversal.
        visited (set): Keeps track of visited nodes to avoid cycles (default is None).

    Returns:
        list: The list of nodes in DFS order.

    Example:
        >>> graph = {
        ... 'A': ['B', 'C'],
        ... 'B': ['D', 'E'],
        ... 'C': ['F'],
        ... 'D': [],
        ... 'E': ['F'],
        ... 'F': [],
        ... }
        >>> dfs(graph, 'A')
        A B D E F C
    """
    if not isinstance(graph, dict):
        raise TypeError("Graph should be a dictionary with nodes as keys and lists of neighbors as values.")
    
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph.")

    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return list(visited)  # Return the order of visited nodes

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    visited_nodes = dfs(graph, 'A')  # Output: A B D E F C
    print("\nVisited Nodes:", visited_nodes)