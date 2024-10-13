# test_disjointsets

import unittest
from pysnippets.disjoint.disjointsets import DisjointSet

class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        self.ds = DisjointSet(10)  # Create a Disjoint Set with 10 elements

    def test_initial_parents(self):
        # Check that each element is its own parent initially
        for i in range(10):
            self.assertEqual(self.ds.find(i), i)

    def test_union_and_find(self):
        # Perform some union operations
        self.ds.union(1, 2)
        self.ds.union(2, 3)

        # After union, 1, 2, and 3 should have the same root
        self.assertEqual(self.ds.find(1), self.ds.find(2))
        self.assertEqual(self.ds.find(2), self.ds.find(3))

        # Check that 1 and 3 are connected
        self.assertTrue(self.ds.connected(1, 3))

    def test_disjoint_sets(self):
        # Check that disjoint sets are not connected
        self.ds.union(4, 5)
        self.assertFalse(self.ds.connected(1, 4))

    def test_union_by_rank(self):
        # Check that union by rank works
        self.ds.union(1, 2)
        self.ds.union(3, 4)
        self.ds.union(2, 4)

        # Now 1 and 4 should be connected
        self.assertTrue(self.ds.connected(1, 4))
        self.assertEqual(self.ds.find(1), self.ds.find(4))

    def test_path_compression(self):
        # Check if path compression works
        self.ds.union(0, 1)
        self.ds.union(1, 2)
        self.ds.union(2, 3)
        self.ds.union(3, 4)

        # After several unions, path compression should lead to 0 being the root
        self.assertEqual(self.ds.find(4), self.ds.find(0))

if __name__ == "__main__":
    unittest.main()
