import unittest

def indirect_recursion_a(n):
    if n <= 0:
        return 0
    else:
        return n + indirect_recursion_b(n - 1)

def indirect_recursion_b(n):
    if n <= 0:
        return 0
    else:
        return indirect_recursion_a(n - 1)

class TestIndirectRecursion(unittest.TestCase):

    def test_indirect_recursion(self):
        self.assertEqual(indirect_recursion_a(5), 15)
        self.assertEqual(indirect_recursion_a(0), 0)
        self.assertEqual(indirect_recursion_a(1), 1)
        self.assertEqual(indirect_recursion_a(10), 55)

if __name__ == '__main__':
    unittest.main()
