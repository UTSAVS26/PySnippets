import unittest
from pysnippets.algorithms.breadth_first_search import bfs  

class TestBFS(unittest.TestCase):

    def test_connected_graph(self):
        # Test case for normal behavior on a connected graph
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C']
        }
        self.assertEqual(bfs(graph, 'A'), ['A', 'B', 'C', 'D'])  # Order may vary

    def test_disconnected_graph(self):
        # Test case for a disconnected graph
        graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        }
        self.assertEqual(bfs(graph, 'A'), ['A', 'B'])  # Only reachable nodes

    def test_empty_graph(self):
        # Test case for an empty graph
        graph = {}
        self.assertEqual(bfs(graph, 'A'), [])  # Should handle gracefully

if __name__ == '__main__':
    unittest.main()
