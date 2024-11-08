from collections import defaultdict

def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))

# Helper function for topological sorting using Depth First Search (DFS)
def topological_sort(v, visited, stack, graph):
    visited[v] = True
    # Explore all neighbors of vertex v
    for neighbor, _ in graph[v]:
        if not visited[neighbor]:
            topological_sort(neighbor, visited, stack, graph)
    # Add current vertex to the stack (stores topological order)
    stack.append(v)

# Function to find the longest path in a Directed Acyclic Graph (DAG) from a source
def find_longest_path(graph, num_vertices, source):
    # Step 1: Perform topological sort
    stack = []
    visited = [False] * num_vertices
    for i in range(num_vertices):
        if not visited[i]:
            topological_sort(i, visited, stack, graph)

    # Step 2: Initialize distances as minus infinity, set source distance to 0
    distances = [-float('inf')] * num_vertices
    distances[source] = 0

    # Step 3: Process vertices in topological order
    while stack:
        u = stack.pop()
        # Update distances of all adjacent vertices of u
        if distances[u] != -float('inf'):
            for v, weight in graph[u]:
                if distances[v] < distances[u] + weight:
                    distances[v] = distances[u] + weight

    # Print the longest distances from the source
    print(f"Longest distances from source vertex {source}:")
    for i in range(num_vertices):
        if distances[i] == -float('inf'):
            print(f"Vertex {i} is unreachable from source, Distance: -Infinity")
        else:
            print(f"Vertex {i} - Distance: {distances[i]}")

# Example usage
if __name__ == "__main__":
    num_vertices = 5  # Number of vertices in the graph
    graph = defaultdict(list)

    # Adding edges to the graph (u -> v with weight w)
    add_edge(graph, 0, 1, 3)
    add_edge(graph, 0, 2, 10)
    add_edge(graph, 0, 3, 14)
    add_edge(graph, 1, 3, 7)
    add_edge(graph, 1, 4, 51)
    add_edge(graph, 2, 3, 5)
    add_edge(graph, 3, 4, 11)
    
    source_vertex = 0
    find_longest_path(graph, num_vertices, source_vertex)

# Output:
# Longest distances from source vertex 0:
# Vertex 0 - Distance: 0
# Vertex 1 - Distance: 3
# Vertex 2 - Distance: 10
# Vertex 3 - Distance: 15
# Vertex 4 - Distance: 54
