import unittest
from pysnippets.algorithms.depth_first_search import dfs  

class TestDFS(unittest.TestCase):

    def test_connected_graph(self):
        # Test case for normal behavior on a connected graph
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C']
        }
        self.assertEqual(dfs(graph, 'A'), ['A', 'B', 'D', 'C'])  # Order may vary

    def test_disconnected_graph(self):
        # Test case for a disconnected graph
        graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        }
        self.assertEqual(dfs(graph, 'A'), ['A', 'B'])  # Only reachable nodes

    def test_empty_graph(self):
        # Test case for an empty graph
        graph = {}
        self.assertEqual(dfs(graph, 'A'), [])  # Should handle gracefully

if __name__ == '__main__':
    unittest.main()
