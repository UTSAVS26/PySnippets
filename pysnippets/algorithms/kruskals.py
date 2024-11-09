class KruskalAlgorithm:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = list(range(vertices))  # Initialize each node as its own parent
        self.rank = [0] * vertices  # Initialize rank for union by rank
        self.edges = []

    def find(self, i):
        # Path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
        # Union by rank
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

    def kruskal(self, cost_matrix):
        # Extract all edges and their corresponding weights
        self.edges = []
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):  # To avoid duplicate edges for undirected graph
                if cost_matrix[i][j] != float('inf'):  # Skip non-existent edges
                    self.edges.append((cost_matrix[i][j], i, j))

        # Sort edges by cost
        self.edges.sort()

        mincost = 0
        for cost, u, v in self.edges:
            if self.find(u) != self.find(v):
                print(f"Edge from vertex {u} to {v} with cost = {cost}")
                mincost += cost
                self.union(u, v)

        print(f"Cost of MST: {mincost}")

if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    cost_matrix = []
    print("Enter the cost matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        cost_matrix.append(row)

    kruskal = KruskalAlgorithm(n)
    kruskal.kruskal(cost_matrix)