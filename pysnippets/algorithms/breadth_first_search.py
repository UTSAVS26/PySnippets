from collections import deque
from typing import Dict, List, Any

def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Performs Breadth First Search (BFS) traversal on a graph.

    Args:
        graph (dict): The adjacency list representing the graph.
        start (Any): The starting node for BFS traversal.

    Returns:
        List[Any]: A list of nodes in BFS order during traversal.

    Example:
        >>> graph = {
        ... 'A': ['B', 'C'],
        ... 'B': ['D', 'E'],
        ... 'C': ['F'],
        ... 'D': [],
        ... 'E': ['F'],
        ... 'F': []
        ... }
        >>> bfs(graph, 'A')
        ['A', 'B', 'C', 'D', 'E', 'F']
    """
    # Edge case: start node is not in the graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph.")

    visited = set()
    queue = deque([start])
    visited.add(start)

    traversal_order = []

    while queue:
        vertex = queue.popleft()
        traversal_order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

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
    result = bfs(graph, 'A')
    print(result)  # Output: ['A', 'B', 'C', 'D', 'E', 'F']