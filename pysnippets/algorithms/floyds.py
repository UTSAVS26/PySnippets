def floyds(cost_matrix):
    n = len(cost_matrix)
    dist = list(map(lambda i: list(map(lambda j: j, i)), cost_matrix))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def main():
    n = int(input("Enter the number of vertices: "))
    print("Enter the cost matrix:")
    cost_matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        cost_matrix.append(row)

    shortest_paths = floyds(cost_matrix)

    print("All Pairs Shortest Paths:")
    for row in shortest_paths:
        print("\t".join(map(str, row)))

if __name__ == "__main__":
    main()