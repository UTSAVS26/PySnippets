import unittest
from pysnippets.algorithms.adjacency_matrix import create_graph

class TestGraphAdjacency(unittest.TestCase):

    def test_create_graph(self):
        no_of_nodes = 5
        adj = [[0] * no_of_nodes for _ in range(no_of_nodes)]
        neighbors_info = {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [2, 1, 4],
            4: [3]
        }
        create_graph(adj, no_of_nodes, neighbors_info)

        # Expected adjacency matrix based on the hardcoded input
        expected_adj = [
            [0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0]
        ]

        self.assertEqual(adj, expected_adj)

if __name__ == "__main__":
    unittest.main()
