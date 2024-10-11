import unittest
from pysnippets.algorithms.dfs import dfs  # Assuming dfs is implemented in this module

class TestDFSAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D'],
            'D': ['B', 'C']
        }

    def test_dfs_algorithm(self):
        visited = dfs(self.graph, 'A')
        expected_visited = ['A', 'B', 'C', 'D']  # Adjust this based on your DFS implementation
        self.assertEqual(visited, expected_visited)

if __name__ == '__main__':
    unittest.main()
