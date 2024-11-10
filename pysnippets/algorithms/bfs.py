from collections import deque
from typing import Dict, List

def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    visited = set()
    queue = deque([start])
    visited.add(start)
    order_of_visit = []  # To store the order of visited nodes

    while queue:
        vertex = queue.popleft()
        order_of_visit.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order_of_visit

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
    order = bfs(graph, 'A')
    print("Order of visit:", order)