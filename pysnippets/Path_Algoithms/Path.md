# Path Algorithms Package 🛣️

A Python package that provides a robust implementation of Dijkstra's shortest path algorithm. It comes with a graphical user interface, comprehensive logging, and robust error handling.

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Examples](#-examples)
- [Testing](#-testing)
- [Error Handling](#-error-handling)
- [Logging](#-logging)
- [GUI Interface](#-gui-interface)
- [Implementation Details](#-implementation-details)
- [Contributing](#-contributing)

## ✨ Features
- Implementation of Dijkstra's shortest path algorithm
- Graph representation using data classes
- Interactive GUI demonstration
- Comprehensive logging system
- Robust error handling
- Extensive test coverage
- Type hints for better code maintainability

## 🚀 Installation

1. Clone the repository
   ```
   git clone https://github.com/yourusername/pysnippets.git
   ```
2. Navigate to the package directory
   ```
   cd pysnippets/Path_Algorithms
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Define your graph
   ```python
   from Path_Algorithms import create_graph, dijkstra
   vertices = ['A', 'B', 'C', 'D']
   edges = {
       'A': {'B': 1, 'C': 4},
       'B': {'C': 2, 'D': 5},
       'C': {'D': 1},
       'D': {}
   }
   ```
5. Create graph instance
   ```python
   graph = create_graph(vertices, edges)
   ```
6. Find shortest path
   ```python
   path, distance = dijkstra(graph, 'A', 'D')
   print(f"Shortest path: {' -> '.join(path)}")
   print(f"Total distance: {distance}")
   ```
7. Launch the GUI demonstration
   ```python
   from Path_Algorithms import run_demo
   run_demo()
   ```

## 📖 Usage

The package provides a simple and intuitive API for creating and analyzing graphs. Here's a quick guide to get you started:

1. Define your graph
   ```python
   from Path_Algorithms import create_graph, dijkstra
   vertices = ['A', 'B', 'C', 'D']
   edges = {
       'A': {'B': 1, 'C': 4},
       'B': {'C': 2, 'D': 5},
       'C': {'D': 1},
       'D': {}
   }
   ```
2. Create graph instance
   ```python
   graph = create_graph(vertices, edges)
   ```
3. Find shortest path
   ```python
   path, distance = dijkstra(graph, 'A', 'D')
   print(f"Shortest path: {' -> '.join(path)}")
   print(f"Total distance: {distance}")
   ```
4. Launch the GUI demonstration
   ```python
   from Path_Algorithms import run_demo
   run_demo()
   ```

## 📚 API Reference

The package provides the following functions and classes:

- `create_graph(vertices: List[str], edges: Dict[str, Dict[str, int]]) -> Graph`: Creates a graph instance.
- `dijkstra(graph: Graph, start: str, end: str) -> Tuple[List[str], int]`: Finds the shortest path between two vertices.

## 🌟 Examples

Here are some examples to demonstrate the usage of the package:

1. Create a simple graph
   ```python
   vertices = ['A', 'B', 'C']
   edges = {
       'A': {'B': 1, 'C': 3},
       'B': {'C': 1},
       'C': {}
   }
   graph = create_graph(vertices, edges)
   ```
2. Find path from A to C
   ```python
   path, distance = dijkstra(graph, 'A', 'C')
   print(f"Path: {' -> '.join(path)}, Distance: {distance}")
   ```
3. Graph with no path between vertices
   ```python
   vertices = ['A', 'B']
   edges = {'A': {}, 'B': {}}
   graph = create_graph(vertices, edges)
   try:
       path, distance = dijkstra(graph, 'A', 'B')
   except ValueError as e:
       print(f"Error: {e}") # Output: Error: Path not found
   ```

## 🧪 Testing

To run the tests, use the following commands:

- Run all tests
   ```
   python -m unittest discover
   ```
- Run specific test file
   ```
   python -m unittest test_dijkstra.py
   ```

## 🚨 Error Handling

The package provides robust error handling. If a path between two vertices is not found, a `ValueError` is raised.

## 📝 Logging

The package provides comprehensive logging. You can set the minimum log level and the log format.

## 🖥️ GUI Interface

The package comes with an interactive GUI demonstration. You can launch it using the `run_demo` function.

## 📦 Implementation Details

The package is implemented using data classes for graph representation. The Dijkstra's shortest path algorithm is used for finding the shortest path.

## 🤝 Contributing

If you find any issues or have suggestions for improvements, feel free to contribute to the project. Please refer to the contribution guidelines for more details.

The markdown is formatted with:
1. Emoji icons for better visual organization
2. Code blocks with syntax highlighting
3. Clear section headers
4. Nested lists for detailed information
5. Table of contents for easy navigation
