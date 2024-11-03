from collections import deque
def bidirectional_search(graph, start, target):
    queue_start = deque([start])
    queue_target = deque([target])

    visited_start = {start}
    visited_target = {target}

    parents_start = {start: None}
    parents_target = {target: None}

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

