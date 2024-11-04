# test_circular_linked_list.py

import unittest
from pysnippets.LinkedList.Circular_Linked_List import insert_end, delete_node, display

class TestCircularLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.head = None  # Initialize the head of the circular linked list

    def test_insert_end(self):
        self.head = insert_end(self.head, 10)
        self.head = insert_end(self.head, 20)
        self.head = insert_end(self.head, 30)
        self.assertEqual(display(self.head), [10, 20, 30], "Expected [10, 20, 30]")

    def test_delete_node(self):
        self.head = insert_end(self.head, 10)
        self.head = insert_end(self.head, 20)
        self.head = insert_end(self.head, 30)
        
        self.head = delete_node(self.head, 20)
        self.assertEqual(display(self.head), [10, 30], "Expected [10, 30]")

    def test_delete_non_existing_node(self):
        self.head = insert_end(self.head, 10)
        self.head = insert_end(self.head, 20)
        self.head = insert_end(self.head, 30)
        
        self.head = delete_node(self.head, 40)  # Should not change the list
        self.assertEqual(display(self.head), [10, 20, 30], "Expected [10, 20, 30]")

    def test_delete_head(self):
        self.head = insert_end(self.head, 10)
        self.head = insert_end(self.head, 20)
        self.head = insert_end(self.head, 30)
        
        self.head = delete_node(self.head, 10)
        self.assertEqual(display(self.head), [20, 30], "Expected [20, 30]")

if __name__ == "__main__":
    unittest.main()
