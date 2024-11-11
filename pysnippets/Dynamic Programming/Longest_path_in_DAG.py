from dataclasses import dataclass
from collections import defaultdict
import logging

@dataclass
class Edge:
    u: int
    v: int
    weight: int

def add_edge(graph, edge: Edge):
    graph[edge.u].append((edge.v, edge.weight))

def topological_sort(v, visited, stack, graph):
    visited[v] = True
    for neighbor, _ in graph[v]:
        if not visited[neighbor]:
            topological_sort(neighbor, visited, stack, graph)
    stack.append(v)

def find_longest_path(graph, num_vertices, source):
    try:
        distances = [-float('inf')] * num_vertices
        distances[source] = 0
        stack = []
        visited = [False] * num_vertices

        for i in range(num_vertices):
            if not visited[i]:
                topological_sort(i, visited, stack, graph)

        while stack:
            u = stack.pop()
            if distances[u] != -float('inf'):
                for v, weight in graph[u]:
                    if distances[v] < distances[u] + weight:
                        distances[v] = distances[u] + weight

        return distances
    except Exception as e:
        logging.error(f"Error in find_longest_path function: {e}")
        return None

# Test cases
def test_find_longest_path():
    graph = defaultdict(list)
    edges = [
        Edge(0, 1, 3),
        Edge(0, 2, 10),
        Edge(0, 3, 14),
        Edge(1, 3, 7),
        Edge(1, 4, 51),
        Edge(2, 3, 5),
        Edge(3, 4, 11)
    ]
    for edge in edges:
        add_edge(graph, edge)

    num_vertices = 5
    source = 0
    longest_distances = find_longest_path(graph, num_vertices, source)

    print(f"Longest distances from source vertex {source}:")
    for vertex, distance in enumerate(longest_distances):
        if distance == -float('inf'):
            print(f"Vertex {vertex} is unreachable from source, Distance: -Infinity")
        else:
            print(f"Vertex {vertex} - Distance: {distance}")

if __name__ == "__main__":
    test_find_longest_path()
