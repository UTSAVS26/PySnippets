import unittest

def tree_recursion(n):
    if n <= 1:
        return n
    else:
        return tree_recursion(n - 1) + tree_recursion(n - 2)

class TestTreeRecursion(unittest.TestCase):

    def test_tree_recursion(self):
        self.assertEqual(tree_recursion(5), 5)  # Fibonacci(5)
        self.assertEqual(tree_recursion(0), 0)  # Fibonacci(0)
        self.assertEqual(tree_recursion(1), 1)  # Fibonacci(1)
        self.assertEqual(tree_recursion(2), 1)  # Fibonacci(2)
        self.assertEqual(tree_recursion(3), 2)  # Fibonacci(3)
        self.assertEqual(tree_recursion(4), 3)  # Fibonacci(4)

if __name__ == '__main__':
    unittest.main()
