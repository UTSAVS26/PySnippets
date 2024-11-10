class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print_solution(self, dist):
        print("Vertex Distance from Source:")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

    def print_negative_cycle(self, parent, start):
        print("Negative weight cycle detected:")
        cycle = []
        cycle.append(start)
        current = parent[start]
        while current != start:
            cycle.append(current)
            current = parent[current]
        cycle.append(start)
        cycle.reverse()
        print(" -> ".join(map(str, cycle)))

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        parent = [-1] * self.V  # To store the parent of each node in the shortest path
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u  # Update parent for the path

        # Check for negative weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                self.print_negative_cycle(parent, v)
                return

        self.print_solution(dist)

# Example usage:
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(0)