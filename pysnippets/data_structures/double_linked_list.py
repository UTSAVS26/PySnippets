class Node:
    """A node in a double linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    """Double linked list implementation."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Inserts a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, key):
        """Deletes the first node that contains the given key."""
        current = self.head
        while current and current.data != key:
            current = current.next

        if not current:  # Key not found
            return "Node not found."

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next  # Deleting the head node

        if current.next:
            current.next.prev = current.prev

    def display_forward(self):
        """Displays all elements from head to tail."""
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes

    def display_backward(self):
        """Displays all elements from tail to head."""
        nodes = []
        current = self.head
        if not current:
            return nodes
        while current.next:
            current = current.next
        while current:
            nodes.append(current.data)
            current = current.prev
        return nodes

# Example usage
if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print("Forward:", dll.display_forward())  # Output: [10, 20, 30]
    print("Backward:", dll.display_backward())  # Output: [30, 20, 10]
    dll.delete(20)
    print("After deletion (forward):", dll.display_forward())  # Output: [10, 30]
    print("After deletion (backward):", dll.display_backward())  # Output: [30, 10]
