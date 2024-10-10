from collections import deque

def bfs(graph, start):
  """
  Performs Breadth First Search (BFS) traversal on a graph.

  Args:
      graph (dict): The adjaceny list representing the graph.
      start (str): The starting node for BFS traversal.

  Returns:
      None: Prints nodes in BFS order during traversal.

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
      A B C D E F
  """
  visited = set()
  queue = deque([start])

  visited.add(start)

  while queue:
    vertex = queue.popleft()
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

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
    bfs(graph, 'A')
