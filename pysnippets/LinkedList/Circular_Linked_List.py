class Node:
    def __init__(self, data):
        self.data = data  # Assign data to the node
        self.next = None  # Initialize next as null

# Function to insert a node at the end of the circular linked list
def insert_end(head, data):
    new_node = Node(data)  # Create a new node
    if head is None:  # If the list is empty
        new_node.next = new_node  # Point it to itself
        return new_node  # Return the new node as the head

    temp = head
    while temp.next != head:  # Traverse to the last node
        temp = temp.next
    temp.next = new_node  # Link the new node after the last node
    new_node.next = head  # Complete the circle
    return head  # Return the head of the list

# Function to delete a node with a specific value
def delete_node(head, key):
    if head is None:  # If the list is empty
        return None
    
    temp = head
    prev = None

    # If the head node holds the key
    if temp.data == key:
        if temp.next == head:  # Only one node in the list
            return None  # List becomes empty
        else:
            while temp.next != head:  # Find the last node
                temp = temp.next
            temp.next = head.next  # Link last node to the second node
            return head.next  # Return the new head

    # Search for the key to be deleted
    while temp.next != head:
        if temp.next.data == key:
            temp.next = temp.next.next  # Unlink the node
            return head
        temp = temp.next

    return head  # Return the head of the list

# Function to display the circular linked list
def display(head):
    if head is None:  # If the list is empty
        return []
    
    result = []
    temp = head
    while True:
        result.append(temp.data)  # Collect data from each node
        temp = temp.next
        if temp == head:  # Stop when we reach back to the head
            break
    return result  # Return the list of node values
