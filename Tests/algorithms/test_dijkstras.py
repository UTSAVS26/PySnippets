import unittest
from pysnippets.algorithms.dijkstras import dijkstra

class TestDijkstrasAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'B': 1, 'C': 3},
            'B': {'A': 1, 'C': 3, 'D': 6},
            'C': {'A': 3, 'B': 3, 'D': 4},
            'D': {'B': 6, 'C': 4}
        }

    def test_dijkstras_algorithm(self):
        distances, previous_nodes = dijkstra(self.graph, 'A')
        expected_distances = {
            'A': 0,
            'B': 1,
            'C': 3,
            'D': 7
        }
        expected_previous_nodes = {
            'A': None,
            'B': 'A',
            'C': 'A',
            'D': 'C'
        }
        self.assertEqual(distances, expected_distances)
        self.assertEqual(previous_nodes, expected_previous_nodes)

if __name__ == '__main__':
    unittest.main()