import unittest
from logger_config import setup_logger
from data_classes import Graph, NodeColor
from bfs import breadth_first_search


logger = setup_logger('test_all')

class TestGraphTraversalAlgorithms(unittest.TestCase):
    def setUp(self):
        # Test graphs setup
        self.small_graph = Graph()
        small_edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
        for u, v in small_edges:
            self.small_graph.add_edge(u, v)

        self.large_graph = Graph()
        large_edges = [
            (0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
            (3, 7), (4, 7), (5, 8), (6, 8), (7, 9), (8, 9)
        ]
        for u, v in large_edges:
            self.large_graph.add_edge(u, v)

        # Weighted graph setup
        self.weighted_graph = Graph(weighted=True)
        weighted_edges = [
            (0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5),
            (2, 3, 8), (2, 4, 10), (3, 4, 2), (3, 5, 6),
            (4, 5, 3)
        ]
        for u, v, w in weighted_edges:
            self.weighted_graph.add_edge(u, v, w)

    def test_weighted_graph(self):
        self.assertEqual(
            self.weighted_graph.get_weight(0, 1), 4
        )
        self.assertEqual(
            self.weighted_graph.get_weight(2, 4), 10
        )

    def test_node_coloring(self):
        result = breadth_first_search(self.small_graph, 0)
        for node_id in result.visited:
            self.assertEqual(
                self.small_graph.nodes[node_id].color,
                NodeColor.BLACK
            )

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            breadth_first_search(self.small_graph, 99)

if __name__ == '__main__':
    unittest.main() 