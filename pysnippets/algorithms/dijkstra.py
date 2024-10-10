import heapq

def dijkstra(graph, start):
    """
    Performs Dijkstra's algorithm to find the shortest path from the start node to all other nodes.

    Args:
        graph (dict): The graph represented as an adjacency list where keys are nodes, and values are lists of tuples (neighbor, weight).
        start (str): The starting node for the algorithm.

    Returns:
        dict: A dictionary where keys are nodes and values are the shortest distances from the start node.

    Example:
        >>> graph = {
        ... 'A': [('B', 1), ('C', 4)],
        ... 'B': [('C', 2), ('D', 5)],
        ... 'C': [('D', 1)],
        ... 'D': []
        ... }
        >>> dijkstra(graph, 'A')
        {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    """
    priority_queue = [(0, start)]
    distances = {start: 0}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
      
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
         
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
