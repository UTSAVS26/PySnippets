import unittest
from bubble_sort_test import TestBubbleSort
from insertion_sort_test import TestInsertionSort
from merge_sort_test import TestMergeSort
from quick_sort_test import TestQuickSort
from cocktail_sort_test import TestCocktailSort
from heap_sort_test import TestHeapSort
from counting_sort_test import TestCountingSort
from radix_sort_test import TestRadixSort
from bucket_sort_test import TestBucketSort
from cocktail_shaker_sort_test import TestCocktailShakerSort

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBubbleSort))
    suite.addTest(unittest.makeSuite(TestInsertionSort))
    suite.addTest(unittest.makeSuite(TestMergeSort))
    suite.addTest(unittest.makeSuite(TestQuickSort))
    suite.addTest(unittest.makeSuite(TestCocktailSort))
    suite.addTest(unittest.makeSuite(TestHeapSort))
    suite.addTest(unittest.makeSuite(TestCountingSort))
    suite.addTest(unittest.makeSuite(TestRadixSort))
    suite.addTest(unittest.makeSuite(TestBucketSort))
    suite.addTest(unittest.makeSuite(TestCocktailShakerSort))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite()) 