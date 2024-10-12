class Queue:
    """Queue implementation using a list (FIFO: First In, First Out)."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if self.is_empty():
            return "Queue is empty."
        return self.items.pop(0)

    def size(self):
        """Return the size of the queue."""
        return len(self.items)

    def display(self):
        """Display the elements in the queue."""
        return self.items

# Example usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue:", queue.display())  # Output: [10, 20, 30]
    print("Dequeue:", queue.dequeue())  # Output: 10
    print("After Dequeue:", queue.display())  # Output: [20, 30]
