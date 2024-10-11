import unittest
from pysnippets.algorithms.topological_ordering import topological_ordering

class TestTopologicalOrdering(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D'],
            'D': []
        }

    def test_topological_ordering(self):
        order = topological_ordering(self.graph)
        expected_order = ['A', 'B', 'C', 'D']  # One possible valid topological order
        self.assertEqual(order, expected_order)

if __name__ == '__main__':
    unittest.main()
