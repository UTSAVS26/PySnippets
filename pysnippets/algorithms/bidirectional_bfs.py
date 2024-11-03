from collections import deque
def bidirectional_search(graph, start, target):
    queue_start = deque([start])
    queue_target = deque([target])

    visited_start = {start}
    visited_target = {target}

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

def _remake_path():
