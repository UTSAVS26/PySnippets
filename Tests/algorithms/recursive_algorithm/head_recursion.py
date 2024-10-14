import unittest

def head_recursion(n):
    if n <= 0:
        return 0
    else:
        head_recursion(n - 1)
        return n

class TestHeadRecursion(unittest.TestCase):

    def test_head_recursion(self):
        result = 0
        for i in range(1, 6):
            result += head_recursion(i)
        self.assertEqual(result, 15)  # Sum from 1 to 5
        self.assertEqual(head_recursion(0), 0)
        self.assertEqual(head_recursion(1), 1)
        self.assertEqual(head_recursion(3), 3)  # Should return 3 after calls

if __name__ == '__main__':
    unittest.main()
