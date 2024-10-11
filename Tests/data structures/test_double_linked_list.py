import unittest
from pysnippets.data_structures.double_linked_list import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up a double linked list for testing."""
        self.dll = DoubleLinkedList()
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)

    def test_append(self):
        """Test appending nodes to the double linked list."""
        self.assertEqual(self.dll.display_forward(), [10, 20, 30])
        self.dll.append(40)
        self.assertEqual(self.dll.display_forward(), [10, 20, 30, 40])

    def test_delete(self):
        """Test deleting nodes from the double linked list."""
        self.dll.delete(20)
        self.assertEqual(self.dll.display_forward(), [10, 30])

    def test_delete_head(self):
        """Test deleting the head node."""
        self.dll.delete(10)
        self.assertEqual(self.dll.display_forward(), [20, 30])

    def test_delete_nonexistent(self):
        """Test attempting to delete a nonexistent node."""
        result = self.dll.delete(50)
        self.assertEqual(result, "Node not found.")
        self.assertEqual(self.dll.display_forward(), [10, 20, 30])

    def test_display_backward(self):
        """Test backward traversal."""
        self.assertEqual(self.dll.display_backward(), [30, 20, 10])

if __name__ == '__main__':
    unittest.main()
