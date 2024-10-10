import unittest
from pysnippets.algorithms.prims import prims

class TestPrimsAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'B': 1, 'C': 3},
            'B': {'A': 1, 'C': 3, 'D': 6},
            'C': {'A': 3, 'B': 3, 'D': 4},
            'D': {'B': 6, 'C': 4}
        }

    def test_prims_algorithm(self):
        mst = prims(self.graph, 'A')
        expected_mst = {
            'A': {'B': 1, 'C': 3},
            'B': {'A': 1},
            'C': {'A': 3, 'D': 4},
            'D': {'C': 4}
        }
        self.assertEqual(mst, expected_mst)

if __name__ == '__main__':
    unittest.main()