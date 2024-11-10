import unittest
from pysnippets.algorithms.bellman_ford import Graph

class TestBellmanFordAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': -3, 'D': 2},
            'C': {'D': 3},
            'D': {}
        }

    def test_bellman_ford_algorithm(self):
        distances, predecessors = Graph.bellman_ford(self.graph, 'A')
        expected_distances = {
            'A': 0,
            'B': 1,
            'C': -2,
            'D': 0
        }
        expected_predecessors = {
            'A': None,
            'B': 'A',
            'C': 'B',
            'D': 'B'
        }
        self.assertEqual(distances, expected_distances)
        self.assertEqual(predecessors, expected_predecessors)

    def test_negative_cycle(self):
        self.graph['C']['A'] = -5  # Introducing a negative cycle
        with self.assertRaises(ValueError):
            Graph.bellman_ford(self.graph, 'A')

if __name__ == '__main__':
    unittest.main()