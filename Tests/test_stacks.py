import unittest
from pysnippets.stacks import stacks  # Correct import for your Stack class


# Custom exceptions for the Stack class
class StackUnderflowError(Exception):
    pass

class EmptyStackError(Exception):
    pass

# Sample Stack implementation for demonstration purposes
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Stack Underflow")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

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
        with self.assertRaises(StackUnderflowError) as context:
            self.stack.pop()
        self.assertEqual(str(context.exception), "Stack Underflow")

    def test_peek_empty(self):
        with self.assertRaises(EmptyStackError) as context:
            self.stack.peek()
        self.assertEqual(str(context.exception), "Stack is empty")

if __name__ == '__main__':
    unittest.main()
