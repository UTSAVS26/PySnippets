class Stack:
    """Stack implementation using a list (LIFO: Last In, First Out)."""
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack."""
        if self.is_empty():
            return "Stack is empty."
        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if self.is_empty():
            return "Stack is empty."
        return self.items[-1]

    def size(self):
        """Return the size of the stack."""
        return len(self.items)

    def display(self):
        """Display the elements in the stack."""
        return self.items

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack:", stack.display())  # Output: [10, 20, 30]
    print("Pop:", stack.pop())        # Output: 30
    print("After Pop:", stack.display())  # Output: [10, 20]
