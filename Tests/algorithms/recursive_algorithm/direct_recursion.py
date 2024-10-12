import unittest

def direct_recursion(n):
    if n <= 0:
        return 0
    else:
        return n + direct_recursion(n - 1)

class TestDirectRecursion(unittest.TestCase):

    def test_direct_recursion(self):
        self.assertEqual(direct_recursion(5), 15)
        self.assertEqual(direct_recursion(0), 0)
        self.assertEqual(direct_recursion(1), 1)
        self.assertEqual(direct_recursion(10), 55)

if __name__ == '__main__':
    unittest.main()
