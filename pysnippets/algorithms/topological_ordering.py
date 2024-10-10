def topological_ordering():
    n = int(input("Enter the number of vertices: "))
    a = []
    print("Enter the adjacency matrix:")
    for i in range(n):
        a.append(list(map(int, input().split())))

    to = [0] * n
    colsum = [0] * n

    for k in range(n):
        for i in range(n):
            if colsum[i] != -1:
                colsum[i] = 0
            for j in range(n):
                colsum[i] += a[j][i]

        for i in range(n):
            if colsum[i] == 0:
                to[k] = i + 1
                colsum[i] = -1
                for j in range(n):
                    a[i][j] = 0
                break

    print("Topological Ordering: ", end="")
    for i in range(n):
        print(to[i], end=" ")
    print()

if __name__ == "__main__":
    topological_ordering()