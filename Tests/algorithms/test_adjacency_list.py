import unittest
from pysnippets.algorithms.adjacency_list import Node, create_graph, display_graph, delete_graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.adj_list = [None] * 5  # Prepare adjacency list with 5 nodes
        self.edges = {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [2, 1, 4],
            4: [3]
        }

    def test_create_graph(self):
        create_graph(self.adj_list, self.edges)
        expected_structure = [
            [0, 1, 2],
            [1, 0, 3],
            [2, 0, 3],
            [3, 2, 1, 4],
            [4, 3]
        ]
        self.assertEqual(display_graph(self.adj_list), expected_structure)

    def test_invalid_node(self):
        invalid_edges = {
            0: [1, 6]  # Node '6' is out of range for a graph with 5 nodes
        }
        with self.assertRaises(ValueError):
            create_graph(self.adj_list, invalid_edges)

    def test_delete_graph(self):
        create_graph(self.adj_list, self.edges)
        delete_graph(self.adj_list)
        self.assertTrue(all(node is None for node in self.adj_list))

if __name__ == "__main__":
    unittest.main()
