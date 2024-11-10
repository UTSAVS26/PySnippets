import unittest
from pysnippets.algorithms.astar import astar

class TestAStarAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'B': 1, 'C': 3},
            'B': {'A': 1, 'C': 3, 'D': 6},
            'C': {'A': 3, 'B': 3, 'D': 4},
            'D': {'B': 6, 'C': 4}
        }
        self.heuristics = {
            'A': 7,
            'B': 6,
            'C': 2,
            'D': 1
        }

    def test_astar_algorithm(self):
        path = astar(self.graph, self.heuristics, 'A', 'D')
        expected_path = ['A', 'C', 'D']
        self.assertEqual(path, expected_path)

    def test_unreachable_destination(self):
        path = astar(self.graph, self.heuristics, 'A', 'Z')  # Non-existent node 'Z'
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()