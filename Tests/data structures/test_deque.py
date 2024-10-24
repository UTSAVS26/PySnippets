import unittest
from pysnippets.data_structures.deque import Deque

class TestDeque(unittest.TestCase):

    def setUp(self):
        self.deque = Deque()
        self.deque.add_rear(10)
        self.deque.add_rear(20)
        self.deque.add_front(5)

    def test_add_front(self):
        self.deque.add_front(0)
        self.assertEqual(self.deque.display(), [0, 5, 10, 20])

    def test_add_rear(self):
        self.deque.add_rear(30)
        self.assertEqual(self.deque.display(), [5, 10, 20, 30])

    def test_remove_front(self):
        self.assertEqual(self.deque.remove_front(), 5)
        self.assertEqual(self.deque.display(), [10, 20])

    def test_remove_rear(self):
        self.assertEqual(self.deque.remove_rear(), 20)
        self.assertEqual(self.deque.display(), [5, 10])

    def test_is_empty(self):
        self.assertFalse(self.deque.is_empty())
        empty_deque = Deque()
        self.assertTrue(empty_deque.is_empty())

if __name__ == '__main__':
    unittest.main()
