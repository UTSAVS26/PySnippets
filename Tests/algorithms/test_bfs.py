import unittest
from pysnippets.algorithms.bfs import bfs

class TestBFSAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D'],
            'D': ['B', 'C']
        }

    def test_bfs_algorithm(self):
        bfs_result = bfs(self.graph, 'A')
        expected_bfs_result = ['A', 'B', 'C', 'D']
        self.assertEqual(bfs_result, expected_bfs_result)

if __name__ == '__main__':
    unittest.main()
