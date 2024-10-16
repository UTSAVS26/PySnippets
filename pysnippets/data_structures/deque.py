class Deque:
    """Double-Ended Queue (Deque) implementation using a list."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.items) == 0

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.items.append(item)

    def remove_front(self):
        """Remove and return the item from the front of the deque."""
        if self.is_empty():
            return "Deque is empty."
        return self.items.pop(0)

    def remove_rear(self):
        """Remove and return the item from the rear of the deque."""
        if self.is_empty():
            return "Deque is empty."
        return self.items.pop()

    def size(self):
        """Return the size of the deque."""
        return len(self.items)

    def display(self):
        """Display the elements in the deque."""
        return self.items

# Example usage
if __name__ == "__main__":
    deque = Deque()
    deque.add_rear(10)
    deque.add_rear(20)
    deque.add_front(5)
    print("Deque:", deque.display())  # Output: [5, 10, 20]
    deque.remove_front()
    print("After Removing Front:", deque.display())  # Output: [10, 20]
    deque.remove_rear()
    print("After Removing Rear:", deque.display())  # Output: [10]
