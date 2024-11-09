import unittest
from Sorting.topological_sort import topological_sort, Graph

class TestTopologicalSort(unittest.TestCase):
    def test_topological_sort_valid_dag(self):
        nodes = ["A", "B", "C", "D", "E", "F"]
        edges = [("A", "D"), ("F", "B"), ("B", "D"), ("F", "A"), ("D", "C")]
        graph = Graph(nodes=nodes, edges=edges)
        result = topological_sort(graph)
        valid_orders = [
            ['F', 'E', 'B', 'A', 'D', 'C'],
            ['E', 'F', 'B', 'A', 'D', 'C'],
            ['F', 'B', 'E', 'A', 'D', 'C'],
            # Additional valid topological orders can be added here
        ]
        self.assertIn(result, valid_orders)

    def test_topological_sort_empty_graph(self):
        graph = Graph(nodes=[], edges=[])
        expected = []
        result = topological_sort(graph)
        self.assertEqual(result, expected)

    def test_topological_sort_single_node(self):
        graph = Graph(nodes=["A"], edges=[])
        expected = ["A"]
        result = topological_sort(graph)
        self.assertEqual(result, expected)

    def test_topological_sort_cycle(self):
        nodes = ["A", "B", "C"]
        edges = [("A", "B"), ("B", "C"), ("C", "A")]
        graph = Graph(nodes=nodes, edges=edges)
        with self.assertRaises(ValueError):
            topological_sort(graph)

    def test_topological_sort_disconnected_graph(self):
        nodes = ["A", "B", "C", "D"]
        edges = [("A", "B"), ("C", "D")]
        graph = Graph(nodes=nodes, edges=edges)
        result = topological_sort(graph)
        # Verify that dependencies are maintained
        self.assertTrue(
            result.index("A") < result.index("B") and
            result.index("C") < result.index("D")
        )

    def test_topological_sort_multiple_valid_orders(self):
        nodes = ["1", "2", "3", "4"]
        edges = [("1", "2"), ("1", "3"), ("3", "4")]
        graph = Graph(nodes=nodes, edges=edges)
        result = topological_sort(graph)
        valid_orders = [
            ["1", "2", "3", "4"],
            ["1", "3", "2", "4"],
            # Additional valid orders can be included
        ]
        self.assertIn(result, valid_orders)

if __name__ == "__main__":
    unittest.main() 