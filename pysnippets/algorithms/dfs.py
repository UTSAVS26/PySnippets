def dfs(graph, start, visited=None):
    """
    Performs Depth First Search (DFS) traversal on a graph.

    Args:
        graph (dict): The adjacency list representing the graph.
        start (str): The starting node for DFS traversal.
        visited (set): Keeps track of visited nodes to avoid cycles (default is None).

    Returns:
        visited (set): A set of visited nodes during the DFS traversal.

    Example:
        >>> graph = {
        ... 'A': ['B', 'C'],
        ... 'B': ['D', 'E'],
        ... 'C': ['F'],
        ... 'D': [],
        ... 'E': ['F'],
        ... 'F': []
        ... }
        >>> dfs(graph, 'A')
        A B D E F C
    """
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)  # Process the node (e.g., print it)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Example usage:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    dfs(graph, 'A')