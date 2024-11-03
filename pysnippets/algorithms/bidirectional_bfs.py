from collections import deque
def bidirectional_search(graph, start, target):
    if start == target:
        return [start]

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
    path_start = []
    node = meeting_node
    while node is not None:
        path_start.append(node)
        node = parents_start[node]
    path_start.reverse()
    return path_start

def _remake_path_target(parents_target, meeting_node):
    node = meeting_node
    path_target = []
    while node is not None:
        path_target.append(node)
        node = parents_target[node]
    return path_target
