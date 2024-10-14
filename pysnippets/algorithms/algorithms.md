## Overview

This document provides a comprehensive overview of various algorithms implemented in Python. Each algorithm is structured with detailed descriptions, input/output specifications, and example usages. The purpose of this documentation is to serve as a reference for understanding the functionality and implementation of different algorithms commonly used in computer science and programming.

## Table of Contents

- [Binary Search](#binary-search)
- [Breadth-First Search (BFS)](#breadth-first-search-bfs)
- [Depth-First Search (DFS)](#depth-first-search-dfs)
- [Dijkstra's Algorithm](#dijkstras-algorithm)
- [Fibonacci Sequence](#fibonacci-sequence)
- [Floyd-Warshall Algorithm](#floyd-warshall-algorithm)
- [Kruskal's Algorithm](#kruskals-algorithm)
- [Prim's Algorithm](#prims-algorithm)
- [Topological Sorting](#topological-sorting)
- [Warshall's Algorithm](#warshalls-algorithm)

### Astar Algorithm

The Astar algorithm is a pathfinding and graph traversal algorithm that finds the shortest path from a start node to a target node using a heuristic to estimate the cost to reach the target.

- **Args**:
  - `maze` (list of list of int): A 2D grid representing the maze where `0` is a walkable cell and `1` is a wall.
  - `start` (tuple): The starting position in the maze (row, column).
  - `end` (tuple): The target position in the maze (row, column).
- **Returns**:

  - list: A list of tuples representing the path from the start to the end, or `None` if no path is found.

- **Example usage**:

```python
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 5)

path = astar(maze, start, end)
print(path)
```

---

### Bellman-Ford Algorithm

The Bellman-Ford algorithm is a graph algorithm that computes the shortest paths from a single source vertex to all other vertices in a weighted graph. It can handle graphs with negative weight edges and detect negative weight cycles.

- **Args**:

  - `src` (int): The source vertex from which to calculate the shortest path.

- **Returns**:

  - None. The function prints the shortest distances from the source vertex to all other vertices.

- **Example usage**:

```python
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
```

---

### Breadth-First Search (BFS)

Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at a given source node and explores all its neighbors at the present depth prior to moving on to nodes at the next depth level.

- **Args**:

  - `graph` (dict): A dictionary representing the graph, where keys are node identifiers and values are lists of neighboring nodes.
  - `start` (any): The starting node for the BFS traversal.

- **Returns**:

  - None. The function prints the nodes in the order they are visited.

- **Example usage**:

```python
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
```

---

### Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half, comparing the target value to the middle element of the array.

- **Args**:

  - `arr` (list): A sorted list of elements to search through.
  - `target` (int/float): The element to search for in the array.

- **Returns**:

  - int: The index of the target if found, -1 if not found.

- **Example usage**:

```python
if __name__ == "__main__":
    result = binary_search([1, 2, 3, 4, 5], 3)
    print(result)  # Output: 2
```

---

### Breadth-First Search (BFS)

Performs Breadth First Search (BFS) traversal on a graph.

- **Args**:

  - `graph` (dict): The adjacency list representing the graph.
  - `start` (str): The starting node for BFS traversal.

- **Returns**:

  - None: Prints nodes in BFS order during traversal.

- **Example usage**:

```python
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    bfs(graph, 'A')  # Output: A B C D E F
```

---

### Depth-First Search (DFS)

Performs Depth First Search (DFS) traversal on a graph.

- **Args**:

  - `graph` (dict): The adjacency list representing the graph.
  - `start` (str): The starting node for DFS traversal.
  - `visited` (set): Keeps track of visited nodes to avoid cycles (default is None).

- **Returns**:

  - None: Prints nodes in DFS order during traversal.

- **Example usage**:

```python
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    dfs(graph, 'A')  # Output: A B D E F C
```

---

### Dijkstra's Algorithm

Performs Dijkstra's algorithm to find the shortest path from the start node to all other nodes.

- **Args**:

  - `graph` (dict): The graph represented as an adjacency list where keys are nodes, and values are lists of tuples (neighbor, weight).
  - `start` (str): The starting node for the algorithm.

- **Returns**:

  - dict: A dictionary where keys are nodes and values are the shortest distances from the start node.

- **Example usage**:

```python
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

---

### Fibonacci Sequence

Generates the Fibonacci sequence up to the nth term.

- **Args**:

  - `n` (int): The number of terms to generate.

- **Returns**:

  - list: A list containing the Fibonacci sequence up to the nth term.

- **Example usage**:

```python
if __name__ == "__main__":
    print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
```

---

### Floyd-Warshall Algorithm

Computes the shortest paths between all pairs of vertices in a weighted graph using the Floyd-Warshall algorithm.

- **Args**:

  - `cost_matrix` (list of list of int): A square matrix where the element at row `i` and column `j` represents the cost of the edge from vertex `i` to vertex `j`. A value of `inf` represents no direct edge between the vertices.

- **Returns**:

  - list of list of int: A matrix where the element at row `i` and column `j` represents the shortest distance from vertex `i` to vertex `j`.

- **Example usage**:

```python
if __name__ == "__main__":
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
```

---

### Kruskal's Algorithm

Kruskal's algorithm finds the minimum spanning tree (MST) for a connected, weighted graph. It adds edges one by one, ensuring that no cycles are formed, until the MST is complete.

- **Args**:

  - `vertices` (int): The number of vertices in the graph.
  - `cost` (list of list of int): A square matrix representing the costs between vertices. A value of `inf` represents no direct edge between the vertices.

- **Returns**:

  - None: Prints the edges included in the MST and the total cost of the MST.

- **Example usage**:

```python
if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    kruskal = KruskalAlgorithm(n)
    print("Enter the cost matrix:")
    for i in range(n):
        kruskal.cost[i] = list(map(int, input().split()))
    kruskal.kruskal()
```

---

### Prim's Algorithm

Performs Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.

- **Args**:

  - `graph` (dict): The graph represented as an adjacency list where keys are nodes, and values are lists of tuples (neighbor, weight).
  - `start` (str): The starting node for the algorithm.

- **Returns**:

  - list: A list of edges representing the Minimum Spanning Tree (MST).

- **Example usage**:

```python
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    print(prim(graph, 'A'))  # Output: [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)]
```

---

### Topological Sorting

Computes the topological ordering of a directed acyclic graph (DAG) using Kahn's algorithm.

- **Args**:

  - None: Inputs the number of vertices and the adjacency matrix from the user.

- **Returns**:

  - None: Prints the topological ordering of the vertices.

- **Example usage**:

```python
if __name__ == "__main__":
    topological_ordering()
```

---

### Warshall's Algorithm

Computes the transitive closure of a directed graph using Warshall's algorithm.

- **Args**:

  - `n` (int): The number of vertices in the graph.
  - `adjacency_matrix` (list of list of int): The adjacency matrix of the graph where `adjacency_matrix[i][j]` is 1 if there is an edge from vertex `i` to vertex `j`, and 0 otherwise.

- **Returns**:

  - list of list of int: The transitive closure matrix where `transitive_closure[i][j]` is 1 if there is a path from vertex `i` to vertex `j`, and 0 otherwise.

- **Example usage**:

```python
if __name__ == "__main__":
    main()
```

---
