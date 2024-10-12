import unittest
from pysnippets.data_structures.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)

    def test_enqueue(self):
        self.queue.enqueue(40)
        self.assertEqual(self.queue.display(), [10, 20, 30, 40])

    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.display(), [20, 30])

    def test_is_empty(self):
        self.assertFalse(self.queue.is_empty())
        empty_queue = Queue()
        self.assertTrue(empty_queue.is_empty())

if __name__ == '__main__':
    unittest.main()
