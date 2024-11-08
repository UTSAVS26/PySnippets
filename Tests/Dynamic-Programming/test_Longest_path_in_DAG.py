import unittest
from collections import defaultdict
from Longest_path_in_DAG import add_edge, find_longest_path

class TestLongestPath(unittest.TestCase):

    def test_basic_dag(self):
        graph = defaultdict(list)
        add_edge(graph, 0, 1, 3)
        add_edge(graph, 0, 2, 10)
        add_edge(graph, 0, 3, 14)
        add_edge(graph, 1, 3, 7)
        add_edge(graph, 1, 4, 51)
        add_edge(graph, 2, 3, 5)
        add_edge(graph, 3, 4, 11)
        
        num_vertices = 5
        source = 0
        result = find_longest_path(graph, num_vertices, source)
        expected_output = [0, 3, 10, 15, 54]  # Updated expected output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
