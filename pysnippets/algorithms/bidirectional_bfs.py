from collections import deque

def bidirectional_search(graph, start, target):
    '''
    Performs a bidirectional search on an undirected graph and returns the shortest path between two nodes.
    Simultaneously uses two breadth-first searches (BFS) from the start and target nodes.
    When the two searches meet, the path is reconstructed by backtracking to the start and target nodes.

    Args:
        graph (dict): A dictionary representing an undirected graph where keys are node identifiers and values
                      are lists of neighboring nodes.
        start: The starting node in the graph for the search. Represents a key in the `graph` dictionary.
        target: The target node in the graph for the search. Represents a key in the `graph` dictionary.

    Returns:
        list: A list representing the shortest path from `start` to `target`. If no path exists, returns `None`.
    '''
    if not isinstance(graph, dict):
        raise TypeError("Graph should be a dictionary with nodes as keys and lists of neighbors as values.")
    if start == target:
        return [start]
    if start not in graph or target not in graph:
        raise ValueError(f"Start ({start}) and target ({target}) nodes must exist in the graph.")

    queue_start = deque([start])
    queue_target = deque([target])

    visited_start = {start}
    visited_target = {target}

    parents_start = {start: None}
    parents_target = {target: None}

    while queue_start and queue_target:
        # Perform BFS from the start side
        path = bfs(graph, visited_start, queue_start, parents_start, visited_target)
        if path:
            return path

        # Perform BFS from the target side
        path = bfs(graph, visited_target, queue_target, parents_target, visited_start)
        if path:
            return path

    return None  # No path found

def bfs(graph, visited, queue, parents, other_visited):
    '''
    Breadth-first search from the current node to seek neighbours and check for intersection with the other search.

    Args:
        graph (dict): The graph represented as a dictionary where each key is a node and its value is a list
                      of neighboring nodes.
        visited (set): A set of nodes already visited in this direction of the search.
        queue (deque): The BFS queue holding nodes to explore.
        parents (dict): A dictionary mapping each visited node to its parent node.
        other_visited (set): A set of nodes visited by the BFS running in the opposite direction.

    Returns:
        list or None: Returns the complete path if an intersection is found, otherwise `None`.
    '''
    current_node = queue.popleft()
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            parents[neighbor] = current_node
            visited.add(neighbor)
            queue.append(neighbor)

            if neighbor in other_visited:
                # Reconstruct the path from start to target through the meeting node
                return reconstruct_path(parents, current_node, neighbor)
    return None

def reconstruct_path(parents, start_node, meeting_node):
    '''
    Reconstruct the path from the start node to the meeting node by using the parent nodes.

    Args:
        parents (dict): A dictionary where each key is a node and the value is the parent node in the path.
        start_node: The starting node of the search.
        meeting_node: The node where the bidirectional search from start and target meets.

    Returns:
        list: A list of nodes representing the path from start_node to the meeting_node.
    '''
    path = []
    # Backtrack from the meeting node to the start node
    node = meeting_node
    while node is not None:
        path.append(node)
        node = parents[node]
    
    path.reverse()
    return path

# Example usage:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start, target = 'A', 'F'
    path = bidirectional_search(graph, start, target)
    print(f"Shortest path from {start} to {target}: {path}")