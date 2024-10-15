# tests/test_queue.py

import unittest
from pysnippets.queues import queues, QueueFullError, QueueEmptyError

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(5)

    def test_enqueue_and_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_full_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)

        with self.assertRaises(QueueFullError) as context:
            self.queue.enqueue(6)
        self.assertEqual(str(context.exception), "The queue is full")

    def test_empty_queue(self):
        with self.assertRaises(QueueEmptyError) as context:
            self.queue.dequeue()
        self.assertEqual(str(context.exception), "The queue is empty")

    def test_print_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        from io import StringIO
        import sys

        old_stdout = sys.stdout
        sys.stdout = StringIO()

        self.queue.printQueue()
        output = sys.stdout.getvalue().strip()

        sys.stdout = old_stdout

        self.assertEqual(output, "1 2 3")

    def test_is_empty_and_full(self):
        self.assertTrue(self.queue.head == -1)
        self.queue.enqueue(1)
        self.assertFalse(self.queue.head == -1)
        self.assertFalse((self.queue.tail + 1) % self.queue.k == self.queue.head)

        for i in range(2, 6):
            self.queue.enqueue(i)
        self.assertTrue((self.queue.tail + 1) % self.queue.k == self.queue.head)

        self.queue.dequeue()
        self.assertFalse((self.queue.tail + 1) % self.queue.k == self.queue.head)

if __name__ == '__main__':
    unittest.main()
