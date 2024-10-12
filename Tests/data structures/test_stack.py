import unittest
from pysnippets.data_structures.stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)

    def test_push(self):
        self.stack.push(40)
        self.assertEqual(self.stack.display(), [10, 20, 30, 40])

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 30)
        self.assertEqual(self.stack.display(), [10, 20])

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 30)

    def test_is_empty(self):
        self.assertFalse(self.stack.is_empty())
        empty_stack = Stack()
        self.assertTrue(empty_stack.is_empty())

if __name__ == '__main__':
    unittest.main()
