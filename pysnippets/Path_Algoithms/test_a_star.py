import unittest
from data_classes import Graph
from a_star import a_star
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class TestAStar(unittest.TestCase):
    def setUp(self):
        vertices = {(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)}
        edges = {
        (0, 0): {(1, 0): 1},
        (1, 0): {(1, 1): 1, (0, 0): 1},
        (1, 1): {(2, 1): 1, (1, 0): 1},
        (2, 1): {(2, 2): 1, (1, 1): 1},
        (2, 2): {(2, 1): 1}
        }
        self.graph = Graph(vertices, edges)
        self.graph.vertices = {
            (0, 0), (1, 0), (1, 1), (2, 1), (2, 2)
        }
        self.graph.edges = {
            (0, 0): {(1, 0): 1},
            (1, 0): {(1, 1): 1, (0, 0): 1},
            (1, 1): {(2, 1): 1, (1, 0): 1},
            (2, 1): {(2, 2): 1, (1, 1): 1},
            (2, 2): {(2, 1): 1}
        }
    
    def test_valid_path(self):
        path, cost = a_star(self.graph, (0, 0), (2, 2))
        self.assertEqual(path, [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)])
        self.assertEqual(cost, 4)
    
    def test_no_path(self):
        self.graph.edges = {
            (0, 0): {(1, 0): 1},
            (1, 0): {(0, 0): 1},
            (2, 2): {}  # Disconnected node
        }
        with self.assertRaises(ValueError):
            a_star(self.graph, (0, 0), (2, 2))
    
    def test_same_start_end(self):
        path, cost = a_star(self.graph, (1, 1), (1, 1))
        self.assertEqual(path, [(1, 1)])
        self.assertEqual(cost, 0)

if __name__ == "__main__":
    unittest.main()