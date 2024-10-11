class KruskalAlgorithm:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = [-1] * vertices
        self.cost = [[0] * vertices for _ in range(vertices)]

    def find(self, i):
        while self.parent[i] != -1:
            i = self.parent[i]
        return i

    def union(self, u, v):
        self.parent[u] = v

    def kruskal(self):
        mincost = 0
        ne = 0

        while ne < self.vertices - 1:
            min = float('inf')
            a = b = u = v = -1

            for i in range(self.vertices):
                for j in range(self.vertices):
                    if self.cost[i][j] < min:
                        min = self.cost[i][j]
                        a = u = i
                        b = v = j

            u = self.find(u)
            v = self.find(v)

            if u != v:
                print(f"Edge from vertex {a} to {b} with cost = {min}")
                mincost += min
                self.union(u, v)
                ne += 1

            self.cost[a][b] = self.cost[b][a] = float('inf')

        print(f"Cost of MST: {mincost}")

if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    kruskal = KruskalAlgorithm(n)
    print("Enter the cost matrix:")
    for i in range(n):
        kruskal.cost[i] = list(map(int, input().split()))
    kruskal.kruskal()