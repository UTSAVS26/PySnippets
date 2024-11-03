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
