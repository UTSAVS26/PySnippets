import unittest
from pysnippets.algorithms.floyds import floyds

class TestFloydsAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'A': 0, 'B': 1, 'C': float('inf'), 'D': float('inf')},
            'B': {'A': 1, 'B': 0, 'C': 3, 'D': float('inf')},
            'C': {'A': float('inf'), 'B': 3, 'C': 0, 'D': 4},
            'D': {'A': float('inf'), 'B': float('inf'), 'C': 4, 'D': 0}
        }

    def test_floyds_algorithm(self):
        dist = floyds(self.graph)
        expected_dist = {
            'A': {'A': 0, 'B': 1, 'C': 4, 'D': 8},
            'B': {'A': 1, 'B': 0, 'C': 3, 'D': 7},
            'C': {'A': 4, 'B': 3, 'C': 0, 'D': 4},
            'D': {'A': 8, 'B': 7, 'C': 4, 'D': 0}
        }
        self.assertEqual(dist, expected_dist)

if __name__ == '__main__':
    unittest.main()