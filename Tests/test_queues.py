import unittest
from pysnippets.queues import queues  # Assuming queues.py defines the Queue class

class QueueFullError(Exception):
    """Custom exception for when the queue is full."""
    pass

class QueueEmptyError(Exception):
    """Custom exception for when the queue is empty."""
    pass

class TestQueue(unittest.TestCase):
    def setUp(self):
        """
        This method is called before every test case.
        Here, we initialize an empty queue.
        """
        self.queue = queues.Queue(5)  # Use the actual Queue class

    def test_enqueue_and_dequeue(self):
        """
        Tests enqueueing and dequeueing elements from the queue.
        """
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_full_queue(self):
        """
        Tests enqueueing to a full queue and raising QueueFullError.
        """
        for i in range(1, 6):
            self.queue.enqueue(i)

        with self.assertRaises(QueueFullError) as context:
            self.queue.enqueue(6)
        self.assertEqual(str(context.exception), "The queue is full")

    def test_empty_queue(self):
        """
        Tests dequeueing from an empty queue and raising QueueEmptyError.
        """
        with self.assertRaises(QueueEmptyError) as context:
            self.queue.dequeue()
        self.assertEqual(str(context.exception), "The queue is empty")

    def test_print_queue(self):
        """
        Tests printing the contents of the queue.
        """
        for i in range(1, 4):
            self.queue.enqueue(i)

        from io import StringIO
        import sys

        old_stdout = sys.stdout
        sys.stdout = StringIO()

        self.queue.printQueue()
        output = sys.stdout.getvalue().strip()

        sys.stdout = old_stdout

        self.assertEqual(output, "1 2 3")

    def test_is_empty_and_full(self):
        """
        Tests the is_empty() and is_full() methods of the queue.
        """
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.assertFalse(self.queue.is_full())

        for i in range(2, 6):
            self.queue.enqueue(i)
        self.assertTrue(self.queue.is_full())

        self.queue.dequeue()
        self.assertFalse(self.queue.is_full())

if __name__ == '__main__':
    unittest.main()