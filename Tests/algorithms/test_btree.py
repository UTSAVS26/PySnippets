import unittest
from pysnippets.algorithms.btree import BTree  # Adjust the import path as needed

class TestBTree(unittest.TestCase):

    def setUp(self):
        # Set up a B-Tree with a minimum degree of 3 for testing
        self.t = 3
        self.btree = BTree(self.t)
        # Data for testing
        self.keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]

    def test_insert_and_traverse(self):
        # Insert keys into the B-Tree
        for key in self.keys_to_insert:
            self.btree.insert(key)
        
        # Capture the output of the traversal
        import io
        import sys
        output = io.StringIO()
        sys.stdout = output
        self.btree.traverse()
        sys.stdout = sys.__stdout__  # Reset redirect

        # Expected traversal order
        expected_output = "5 6 7 10 12 17 20 30"
        self.assertEqual(output.getvalue().strip(), expected_output)

    def test_search_existing_key(self):
        # Insert keys into the B-Tree
        for key in self.keys_to_insert:
            self.btree.insert(key)
        
        # Search for an existing key
        result = self.btree.search(12)
        self.assertIsNotNone(result)
        self.assertIn(12, result.keys)

    def test_search_non_existing_key(self):
        # Insert keys into the B-Tree
        for key in self.keys_to_insert:
            self.btree.insert(key)
        
        # Search for a non-existing key
        result = self.btree.search(99)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
