class Node:
    """A node in a single linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    """Single linked list implementation."""
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

    def delete(self, key):
        """Deletes the first node that contains the given key."""
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        
        if not current:  # Key not found
            return "Node not found."
        
        if previous is None:  # Deleting the head node
            self.head = current.next
        else:
            previous.next = current.next

    def display(self):
        """Displays all elements in the list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes

# Example usage
if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print("Linked List:", sll.display())  # Output: [10, 20, 30]
    sll.delete(20)
    print("After deletion:", sll.display())  # Output: [10, 30]
