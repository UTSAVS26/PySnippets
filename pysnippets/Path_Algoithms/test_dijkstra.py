import unittest
from utils import create_graph
from dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        vertices = ['A', 'B', 'C', 'D']
        edges = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }
        self.graph = create_graph(vertices, edges)

    def test_shortest_path(self):
        path, distance = dijkstra(self.graph, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
        self.assertEqual(distance, 4)

    def test_no_path(self):
        graph = create_graph(['A', 'B'], {'A': {}, 'B': {}})
        with self.assertRaises(ValueError):
            dijkstra(graph, 'A', 'B')

    def test_same_start_end(self):
        path, distance = dijkstra(self.graph, 'A', 'A')
        self.assertEqual(path, ['A'])
        self.assertEqual(distance, 0)

if __name__ == '__main__':
    unittest.main() 