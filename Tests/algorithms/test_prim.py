import unittest
from pysnippets.algorithms.prim import prim  

class TestPrim(unittest.TestCase):

    def test_basic_graph(self):
        # Test case for normal behavior on a basic graph
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 5)],
            'C': [('A', 4), ('B', 2), ('D', 1)],
            'D': [('B', 5), ('C', 1)]
        }
        result = prim(graph, 'A')
        expected = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)]
        self.assertEqual(result, expected)

    def test_disconnected_graph(self):
        # Test case for a disconnected graph
        graph = {
            'A': [('B', 1)],
            'B': [('A', 1)],
            'C': []
        }
        result = prim(graph, 'A')
        expected = [('A', 'B', 1)]
        self.assertEqual(result, expected)

    def test_empty_graph(self):
        # Test case for an empty graph
        graph = {}
        result = prim(graph, 'A')  # Should handle gracefully
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
