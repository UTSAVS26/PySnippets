 // Start Generation Here

# Graph Traversal Algorithms

Welcome to the **Traversal** module of the `pysnippets` library! This module provides efficient and versatile graph traversal algorithms implemented in Python. Whether you're working with simple unweighted graphs or complex weighted ones, our traversal tools are designed to help you explore and analyze graph data structures effectively.

## Table of Contents

- [Overview](#overview)
- [Data Structures](#data-structures)
  - [Graph](#graph)
  - [Node](#node)
  - [SearchResult](#searchresult)
  - [NodeColor](#nodecolor)
- [Traversal Algorithms](#traversal-algorithms)
  - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
  - [Iterative Deepening Depth-First Search (IDDFS)](#iterative-deepening-depth-first-search-iddfs)
- [Usage](#usage)
  - [Setting Up the Graph](#setting-up-the-graph)
  - [Performing BFS](#performing-bfs)
  - [Performing IDDFS](#performing-iddfs)
  - [Finding Shortest Paths](#finding-shortest-paths)
- [Logging](#logging)
- [Testing](#testing)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

Graph traversal is a fundamental concept in computer science, enabling the exploration of nodes and edges within a graph. The Traversal module offers:

- **Breadth-First Search (BFS):** Explores the neighbor nodes level by level.
- **Iterative Deepening Depth-First Search (IDDFS):** Combines the depth-first search's space efficiency and breadth-first search's completeness.

These algorithms are essential for tasks such as pathfinding, network analysis, and solving puzzles or games.

## Data Structures

### Graph

The `Graph` class represents a graph data structure, supporting both directed and undirected graphs, as well as weighted and unweighted edges.

```python
from data_classes import Graph

# Create an undirected, unweighted graph
graph = Graph()

# Create a directed, weighted graph
weighted_graph = Graph(directed=True, weighted=True)
```

**Key Attributes:**

- `nodes`: A dictionary mapping node identifiers to `Node` objects.
- `directed`: Boolean indicating if the graph is directed.
- `weighted`: Boolean indicating if the graph is weighted.
- `weights`: A dictionary storing edge weights.

**Key Methods:**

- `add_node(node_id)`: Adds a node to the graph.
- `add_edge(u, v, weight)`: Adds an edge between nodes `u` and `v` with an optional `weight`.
- `get_weight(u, v)`: Retrieves the weight of the edge `(u, v)`.
- `reset_nodes()`: Resets node metadata before a new traversal.

### Node

The `Node` class encapsulates the properties of a graph node, including its identifier, neighbors, and traversal metadata.

```python
from data_classes import Node, NodeColor

node = Node(id='A')
node.neighbors.add('B')
node.color = NodeColor.GRAY
```

**Attributes:**

- `id`: Unique identifier for the node.
- `neighbors`: A set of adjacent node identifiers.
- `color`: Current color state (`WHITE`, `GRAY`, `BLACK`) used in traversal algorithms.
- `distance`: Distance from the start node.
- `parent`: Reference to the parent node in the traversal path.
- `discovery_time`: Timestamp when the node was first discovered.
- `finish_time`: Timestamp when the node's processing was completed.

### SearchResult

The `SearchResult` class stores the outcome of traversal algorithms, including the order of visited nodes, distances from the start node, and parent relationships.

```python
from data_classes import SearchResult

result = SearchResult(
    visited=['A', 'B', 'C'],
    distances={'A': 0, 'B': 1, 'C': 2},
    parents={'A': None, 'B': 'A', 'C': 'B'}
)
```

**Attributes:**

- `visited`: List of nodes in the order they were visited.
- `distances`: Dictionary mapping each node to its distance from the start node.
- `parents`: Dictionary mapping each node to its parent node in the traversal tree.
- `discovery_times`: (Optional) Dictionary of discovery times for each node.
- `finish_times`: (Optional) Dictionary of finish times for each node.

### NodeColor

An enumeration representing the state of a node during traversal.

```python
from data_classes import NodeColor

print(NodeColor.WHITE)  # Output: NodeColor.WHITE
```

- `WHITE`: Unvisited node.
- `GRAY`: Node is being visited.
- `BLACK`: Node has been fully explored.

## Traversal Algorithms

### Breadth-First Search (BFS)

**Breadth-First Search (BFS)** explores nodes level by level, starting from the source node and moving outward. It's particularly useful for finding the shortest path in unweighted graphs.

**Functions:**

- `breadth_first_search(graph, start, target=None, max_depth=None)`: Performs BFS on the given graph.
- `bfs_level_order(graph, start)`: Returns nodes grouped by their levels from the start node.
- `find_shortest_path(graph, start, end)`: Retrieves the shortest path between two nodes.

### Iterative Deepening Depth-First Search (IDDFS)

**Iterative Deepening Depth-First Search (IDDFS)** combines the depth-first search's space efficiency with the breadth-first search's completeness. It performs DFS to increasing depth limits until the target is found.

**Function:**

- `iterative_deepening_search(graph, start, target=None, max_depth=100)`: Executes IDDFS on the given graph.

## Usage

### Setting Up the Graph

Before performing traversals, define your graph structure.

```python
from data_classes import Graph

# Initialize graph
graph = Graph()

# Add edges (u, v)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# For weighted graphs
weighted_graph = Graph(weighted=True)
weighted_graph.add_edge('A', 'B', weight=5)
weighted_graph.add_edge('A', 'C', weight=3)
```

### Performing BFS

```python
from bfs import breadth_first_search

# Perform BFS from node 'A'
result = breadth_first_search(graph, start='A')

print("Visited Order:", result.visited)
print("Distances:", result.distances)
print("Parents:", result.parents)
```

### Performing IDDFS

```python
from iterative_deepening import iterative_deepening_search

# Perform IDDFS from node 'A' targeting node 'E'
result = iterative_deepening_search(graph, start='A', target='E')

print("Path Found:", result.visited)
```

### Finding Shortest Paths

```python
from bfs import find_shortest_path

# Find shortest path from 'A' to 'E'
path = find_shortest_path(graph, start='A', end='E')

print("Shortest Path:", path)
```

## Logging

The Traversal module integrates logging to help debug and monitor algorithm execution. Logs are configured using the `logger_config` module.

```python
from logger_config import setup_logger

logger = setup_logger('bfs')

logger.info("Starting BFS")
```

Logs include information messages, debug details, and error reports, facilitating easier troubleshooting and performance monitoring.

## Testing

Comprehensive unit tests are provided to ensure the reliability of traversal algorithms. Tests cover various scenarios, including:

- Validating weighted and unweighted graphs.
- Ensuring node coloring states after traversal.
- Handling invalid inputs gracefully.

To run the tests:

```bash
python -m unittest pysnippets/Traversal/test_all.py
```

## Examples

### Example 1: Basic BFS

```python
from data_classes import Graph
from bfs import breadth_first_search

# Setup graph
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# Perform BFS
result = breadth_first_search(graph, start='A')

print("Visited Order:", result.visited)
# Output: ['A', 'B', 'C', 'D', 'E']
```

### Example 2: Finding Shortest Path

```python
from data_classes import Graph
from bfs import find_shortest_path

# Setup graph
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# Find shortest path from 'A' to 'E'
path = find_shortest_path(graph, start='A', end='E')

print("Shortest Path:", path)
# Output: ['A', 'B', 'D', 'E']
```

### Example 3: IDDFS with Target

```python
from data_classes import Graph
from iterative_deepening import iterative_deepening_search

# Setup graph
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# Perform IDDFS to find 'E'
result = iterative_deepening_search(graph, start='A', target='E')

print("Path Found:", result.visited)
# Output: ['A', 'B', 'D', 'E']
```

## Contributing

Contributions are welcome! If you'd like to enhance the Traversal module, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Submit a pull request detailing your changes.

## License

This project is licensed under the [MIT License](LICENSE).

```

