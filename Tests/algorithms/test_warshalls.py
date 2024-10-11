import unittest
from pysnippets.algorithms.warshalls import warshall_algorithm

class TestWarshallsAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = [
            [0, 1, float('inf'), 1],
            [1, 0, 1, float('inf')],
            [float('inf'), 1, 0, 1],
            [1, float('inf'), 1, 0]
        ]

    def test_warshalls_algorithm(self):
        transitive_closure = warshall_algorithm(self.graph)
        expected_closure = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(transitive_closure, expected_closure)

if __name__ == '__main__':
    unittest.main()