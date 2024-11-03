import unittest
from pysnippets.algorithms.bidirectional_bfs import bidirectional_search
class TestBidirectionalBFS(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E', 'G'],
            'G': ['F']
        }

    def test_no_path(self):
        disconnected_graph = {
            'A': ['B'],
            'B': ['A'],
            'C': ['D'],
            'D': ['C']
        }
        path = bidirectional_search(disconnected_graph, 'A', 'D')
        self.assertIsNone(path)

    def test_path(self):
        path = bidirectional_search(self.graph, 'A', 'G')
        self.assertEqual(path, ['A', 'C', 'F', 'G'])

    def test_disconnected_graph(self):
        two_node_graph = {'A': [], 'B': []}
        path = bidirectional_search(two_node_graph, 'A', 'B')
        self.assertIsNone(path)

    def test_invalid_node(self):
        with self.assertRaises(ValueError):
            bidirectional_search(self.graph, 'A', 'Z')

    def test_single_node_graph(self):
        single_node_graph = {'A': []}
        path = bidirectional_search(single_node_graph, 'A', 'A')
        self.assertEqual(path, ['A'])

    def test_graph_is_dictionary(self):
        invalid_graph = ['hello']
        with self.assertRaises(TypeError):
            bidirectional_search(invalid_graph, 'hello', 'hello')



