from collections import deque
def bidirectional_search(graph, start, target):
    '''
    Performs a bidirectional search on an undirected graph and returns the shortest path between two nodes.
    To do this, it simultaneously uses two breadth-first searches (BFS) from the start and target nodes.
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
        raise TypeError("Ensure graph is a dictionary with nodes as keys and lists of neighbors as values.")
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
        path = bfs(graph, visited_start, queue_start, parents_start, visited_target)
        if path:
            path_start = _remake_path_start(parents_start, path)
            path_target = _remake_path_target(parents_target, path)
            return path_start + path_target[1:]
        path = bfs(graph, visited_target, queue_target, parents_target, visited_start)
        if path:
            path_start = _remake_path_start(parents_start, path)
            path_target = _remake_path_target(parents_target, path)
            return path_start + path_target[1:]

def bfs(graph, visited, queue, parents, other_visited):
    '''
    breadth-first search from the current node to seek neighbours.

    Args:
        graph (dict): The graph represented as a dictionary where each key is a node and its value is a list
                      of neighboring nodes.
        visited (set): A set of nodes already visited in this direction of the search.
        queue (deque): The BFS queue holding nodes to explore.
        parents (dict): A dictionary mapping each visited node to its parent node, can be used to remake paths.
        other_visited (set): A set of nodes visited by the BFS running in the opposite direction.

    Returns:
        The meeting node if the current search intersects with the other search, otherwise `None`.
    '''
    current_node = queue.popleft()
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            parents[neighbor] = current_node
            visited.add(neighbor)
            queue.append(neighbor)

            if neighbor in other_visited:
                return neighbor
    return None

def _remake_path_start(parents_start, meeting_node):
    '''
    Create the path from the start node to the meeting node by using the parent nodes.

    Args:
        parents_start (dict): A dictionary where each key is a node and the value
                              is the parent node in the path from the start node.
        meeting_node: The node where the start and target nodes meet.

    Returns:
        list: A list of nodes representing the path from the start node to the meeting node.
    '''
    path_start = []
    node = meeting_node
    while node is not None:
        path_start.append(node)
        node = parents_start[node]
    path_start.reverse()
    return path_start

def _remake_path_target(parents_target, meeting_node):
    '''
    Create the path from the target node to the meeting node by tracing
    back through the parent nodes.

    Args:
        parents_target (dict): A dictionary where each key is a node and the value
                               is the parent node in the path from the target node.
        meeting_node: The node where the bidirectional search from start and target meets.

    Returns:
        list: A list of nodes representing the path from the meeting node to the target node.
    '''
    node = meeting_node
    path_target = []
    while node is not None:
        path_target.append(node)
        node = parents_target[node]
    return path_target
