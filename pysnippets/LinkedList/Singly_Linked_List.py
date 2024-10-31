
class Node:
    def __init__(self, data):
        self.data = data  # Assign data to the node
        self.next = None  # Initialize next as null

# Function to insert a node at the end of the singly linked list
def insert_end(head, data):
    new_node = Node(data)  # Create a new node
    if head is None:  # If the list is empty
        return new_node  # Return the new node as the head
    temp = head
    while temp.next:  # Traverse to the end of the list
        temp = temp.next
    temp.next = new_node  # Link the new node at the end
    return head  # Return the head of the list

# Function to delete a node with a specific value
def delete_node(head, key):
    temp = head

    # If the head node holds the key
    if temp is not None and temp.data == key:
        head = temp.next  # Change head
        return head

    # Search for the key to be deleted
    while temp is not None and temp.next is not None:
        if temp.next.data == key:
            temp.next = temp.next.next  # Unlink the node
            return head
        temp = temp.next

    return head  # Return the head of the list

# Function to display the singly linked list
def display(head):
    result = []
    temp = head
    while temp:
        result.append(temp.data)  # Collect data from each node
        temp = temp.next
    return result  # Return the list of node values
