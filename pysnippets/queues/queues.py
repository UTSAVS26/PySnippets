class QueueFullError(Exception):
    """Custom exception for when the queue is full."""
    pass

class QueueEmptyError(Exception):
    """Custom exception for when the queue is empty."""
    pass

class Queue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data) -> None:
        """Adds an element to the end of the queue."""
        if (self.tail + 1) % self.k == self.head:
            raise QueueFullError("The queue is full")
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
            if self.head == -1:
                self.head = 0

    def dequeue(self):
        """Removes and returns the front element of the queue."""
        if self.head == -1:
            raise QueueEmptyError("The queue is empty")
        else:
            temp = self.queue[self.head]
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.k
            return temp

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return self.head == -1

    def is_full(self) -> bool:
        """Checks if the queue is full."""
        return (self.tail + 1) % self.k == self.head

    def printQueue(self) -> None:
        """Prints the elements of the queue."""
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

    def __str__(self) -> str:
        """String representation of the queue."""
        if self.is_empty():
            return "[]"
        elements = []
        i = self.head
        while True:
            elements.append(self.queue[i])
            if i == self.tail:
                break
            i = (i + 1) % self.k
        return "[" + ", ".join(map(str, elements)) + "]"
