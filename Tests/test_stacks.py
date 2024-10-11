import unittest
from pysnippets.stacks import stacks

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

    def test_pop_empty(self):
        with self.assertRaises(Exception) as context:
            self.stack.pop()
        self.assertEqual(str(context.exception), "Stack Underflow")

    def test_peek_empty(self):
        with self.assertRaises(Exception) as context:
            self.stack.peek()
        self.assertEqual(str(context.exception), "Stack is empty")

if __name__ == '__main__':
    unittest.main()
