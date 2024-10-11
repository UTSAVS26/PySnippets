import unittest
from pysnippets.data_structures.single_linked_list import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up a linked list for testing."""
        self.sll = SingleLinkedList()
        self.sll.append(10)
        self.sll.append(20)
        self.sll.append(30)

    def test_append(self):
        """Test appending nodes to the linked list."""
        self.assertEqual(self.sll.display(), [10, 20, 30])
        self.sll.append(40)
        self.assertEqual(self.sll.display(), [10, 20, 30, 40])

    def test_delete(self):
        """Test deleting nodes from the linked list."""
        self.sll.delete(20)
        self.assertEqual(self.sll.display(), [10, 30])

    def test_delete_head(self):
        """Test deleting the head node."""
        self.sll.delete(10)
        self.assertEqual(self.sll.display(), [20, 30])

    def test_delete_nonexistent(self):
        """Test attempting to delete a nonexistent node."""
        result = self.sll.delete(50)
        self.assertEqual(result, "Node not found.")
        self.assertEqual(self.sll.display(), [10, 20, 30])

if __name__ == '__main__':
    unittest.main()
