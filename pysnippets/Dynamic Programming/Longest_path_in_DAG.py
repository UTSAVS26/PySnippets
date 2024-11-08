from collections import defaultdict

def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))


def topological_sort(v, visited, stack, graph):
    visited[v] = True  # Mark the current node as visited

    for neighbor, _ in graph[v]:
        if not visited[neighbor]:
            topological_sort(neighbor, visited, stack, graph)
    stack.append(v)  # Add the vertex to the stack once all adjacent vertices are visited

def find_longest_path(graph, num_vertices, source):
    # Initialize distances as negative infinity for all vertices, set source distance to 0
    distances = [-float('inf')] * num_vertices
    distances[source] = 0
    stack = []  # Stack to store the topological order
    visited = [False] * num_vertices  # Mark all vertices as not visited

    # Perform topological sort on all vertices
    for i in range(num_vertices):
        if not visited[i]:
            topological_sort(i, visited, stack, graph)

    # Process vertices in topological order to find longest path
    while stack:
        u = stack.pop()  
        # Update distances of all adjacent vertices if a longer path is found
        if distances[u] != -float('inf'):
            for v, weight in graph[u]:
                if distances[v] < distances[u] + weight:
                    distances[v] = distances[u] + weight

    return distances 

# Example 
if __name__ == "__main__":
    # Define graph as a Directed Acyclic Graph (DAG) with weighted edges
    graph = defaultdict(list)
    add_edge(graph, 0, 1, 3)
    add_edge(graph, 0, 2, 10)
    add_edge(graph, 0, 3, 14)
    add_edge(graph, 1, 3, 7)
    add_edge(graph, 1, 4, 51)
    add_edge(graph, 2, 3, 5)
    add_edge(graph, 3, 4, 11)
    
    num_vertices = 5  
    source = 0  

    
    longest_distances = find_longest_path(graph, num_vertices, source)

    # Display the longest path distances from the source
    print(f"Longest distances from source vertex {source}:")
    for vertex, distance in enumerate(longest_distances):
        if distance == -float('inf'):
            print(f"Vertex {vertex} is unreachable from source, Distance: -Infinity")
        else:
            print(f"Vertex {vertex} - Distance: {distance}")


# Output:
# Longest distances from source vertex 0:
# Vertex 0 - Distance: 0
# Vertex 1 - Distance: 3
# Vertex 2 - Distance: 10
# Vertex 3 - Distance: 15
# Vertex 4 - Distance: 54
