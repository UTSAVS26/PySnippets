import sys

def minimum(a, b):
    return a if a < b else b

def dijkstra(cost, src, n):
    d = [sys.maxsize] * n
    s = [False] * n
    d[src] = 0

    for _ in range(n - 1):
        min_distance = sys.maxsize
        w = -1
        for j in range(n):
            if not s[j] and d[j] < min_distance:
                min_distance = d[j]
                w = j
        s[w] = True

        for v in range(n):
            if not s[v] and cost[w][v] != sys.maxsize:
                d[v] = minimum(d[v], d[w] + cost[w][v])

    return d

def main():
    n = int(input("Enter number of vertices: "))
    cost = []
    print("Enter cost matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        cost.append(row)

    src = int(input("Enter source vertex: "))
    shortest_distances = dijkstra(cost, src, n)
    print("Shortest distances from the source:")
    print(" ".join(map(str, shortest_distances)))

if __name__ == "__main__":
    main()