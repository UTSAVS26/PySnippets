# pysnippets/queues.py

class QueueFullError(Exception):
    """Custom exception for when the queue is full."""
    pass

class QueueEmptyError(Exception):
    """Custom exception for when the queue is empty."""
    pass

class Queue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if (self.tail + 1) % self.k == self.head:
            raise QueueFullError("The queue is full")
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
            if self.head == -1:
                self.head = 0

    def dequeue(self):
        if self.head == -1:
            raise QueueEmptyError("The queue is empty")
        else:
            temp = self.queue[self.head]
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.k
            return temp

    def printQueue(self):
        if self.head == -1:
            print("No element in the queue")
        else:
            i = self.head
            while True:
                print(self.queue[i], end=" ")
                if i == self.tail:
                    break
                i = (i + 1) % self.k
            print()
