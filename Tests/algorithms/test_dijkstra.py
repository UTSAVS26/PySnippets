import unittest
from pysnippets.algorithms.dijkstra import dijkstra  

class TestDijkstra(unittest.TestCase):

    def test_basic_graph(self):
        # Test case for normal behavior on a basic graph
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }
        self.assertEqual(dijkstra(graph, 'A'), {'A': 0, 'B': 1, 'C': 3, 'D': 4})

    def test_disconnected_graph(self):
        # Test case for a disconnected graph
        graph = {
            'A': {'B': 1},
            'B': {'A': 1},
            'C': {}
        }
        self.assertEqual(dijkstra(graph, 'A'), {'A': 0, 'B': 1, 'C': float('inf')})

    def test_empty_graph(self):
        # Test case for an empty graph
        graph = {}
        self.assertEqual(dijkstra(graph, 'A'), {})  # Should handle gracefully

    def test_single_node(self):
        graph = {'A': {}}
        self.assertEqual(dijkstra(graph, 'A'), {'A': 0})

if __name__ == '__main__':
    unittest.main()
