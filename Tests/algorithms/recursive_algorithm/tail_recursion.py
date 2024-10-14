import unittest

def tail_recursion(n, accumulator=0):
    if n <= 0:
        return accumulator
    else:
        return tail_recursion(n - 1, accumulator + n)

class TestTailRecursion(unittest.TestCase):

    def test_tail_recursion(self):
        self.assertEqual(tail_recursion(5), 15)
        self.assertEqual(tail_recursion(0), 0)
        self.assertEqual(tail_recursion(1), 1)
        self.assertEqual(tail_recursion(10), 55)

if __name__ == '__main__':
    unittest.main()
