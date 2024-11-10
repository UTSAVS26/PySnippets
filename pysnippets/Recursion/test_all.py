import unittest
from factorial import Factorial
from fibonacci import Fibonacci
from binary_search import BinarySearch
from subsets import Subsets
from permutations import Permutations
from merge_sort import MergeSort
from quick_sort import QuickSort

class TestRecursionSnippets(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(Factorial(0).calculate(), 1)
        self.assertEqual(Factorial(1).calculate(), 1)
        self.assertEqual(Factorial(5).calculate(), 120)
        self.assertEqual(Factorial(10).calculate(), 3628800)

    def test_fibonacci(self):
        self.assertEqual(Fibonacci(0).calculate(), 0)
        self.assertEqual(Fibonacci(1).calculate(), 1)
        self.assertEqual(Fibonacci(5).calculate(), 5)
        self.assertEqual(Fibonacci(10).calculate(), 55)

    def test_binary_search(self):
        self.assertEqual(BinarySearch([1, 2, 3, 4, 5], 3).search(), 2)
        self.assertEqual(BinarySearch([1, 2, 3, 4, 5], 1).search(), 0)
        self.assertEqual(BinarySearch([1, 2, 3, 4, 5], 5).search(), 4)
        self.assertEqual(BinarySearch([1, 2, 3, 4, 5], 6).search(), -1)

    def test_subsets(self):
        self.assertEqual(sorted(Subsets([1, 2, 3]).generate(), key=lambda x: (len(x), x)),
                         sorted([[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], key=lambda x: (len(x), x)))
        self.assertEqual(sorted(Subsets([1]).generate(), key=lambda x: (len(x), x)),
                         sorted([[], [1]], key=lambda x: (len(x), x)))
        self.assertEqual(sorted(Subsets([]).generate(), key=lambda x: (len(x), x)),
                         sorted([[]], key=lambda x: (len(x), x)))

    def test_permutations(self):
        self.assertEqual(sorted(Permutations("abc").generate()), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        self.assertEqual(sorted(Permutations("a").generate()), sorted(['a']))
        self.assertEqual(sorted(Permutations("").generate()), sorted(['']))

    def test_merge_sort(self):
        self.assertEqual(MergeSort([34, 7, 23, 32, 5, 62]).sort(), [5, 7, 23, 32, 34, 62])
        self.assertEqual(MergeSort([1, 2, 3, 4, 5]).sort(), [1, 2, 3, 4, 5])
        self.assertEqual(MergeSort([5, 4, 3, 2, 1]).sort(), [1, 2, 3, 4, 5])

    def test_quick_sort(self):
        self.assertEqual(QuickSort([10, 80, 30, 90, 40, 50, 70]).sort(), [10, 30, 40, 50, 70, 80, 90])
        self.assertEqual(QuickSort([1, 2, 3, 4, 5]).sort(), [1, 2, 3, 4, 5])
        self.assertEqual(QuickSort([5, 4, 3, 2, 1]).sort(), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()