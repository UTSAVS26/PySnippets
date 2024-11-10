import unittest
from pysnippets.algorithms.kruskals import KruskalAlgorithm

class TestKruskalsAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': {'B': 1, 'C': 3},
            'B': {'A': 1, 'C': 3, 'D': 6},
            'C': {'A': 3, 'B': 3, 'D': 4},
            'D': {'B': 6, 'C': 4}
        }

    def test_kruskals_algorithm(self):
        mst = KruskalAlgorithm.kruskal(self.graph)
        expected_mst = [
            ('A', 'B', 1),
            ('A', 'C', 3),
            ('C', 'D', 4)
        ]
        self.assertEqual(sorted(mst), sorted(expected_mst))

    def test_disconnected_graph(self):
        graph = {'A': {}, 'B': {}}
        mst = KruskalAlgorithm.kruskal(graph)
        self.assertEqual(mst, [])

if __name__ == '__main__':
    unittest.main()
