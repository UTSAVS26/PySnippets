from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Node:
    data: any
    next: 'Node' = None  # Type hint for forward reference

def insert_end(head: Node, data: any) -> Node:
    """Insert a node at the end of the circular linked list."""
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        return new_node

    last_node = head
    while last_node.next != head:
        last_node = last_node.next
    last_node.next = new_node
    new_node.next = head
    return head

def delete_node(head: Node, key: any) -> Node:
    """Delete a node with a specific value from the circular linked list."""
    if head is None:
        logging.warning("Attempted to delete from an empty list.")
        return None

    current_node = head
    previous_node = None  # noqa: F841

    if current_node.data == key:
        if current_node.next == head:
            return None
        while current_node.next != head:
            current_node = current_node.next
        current_node.next = head.next
        return head.next

    while current_node.next != head:
        if current_node.next.data == key:
            current_node.next = current_node.next.next
            return head
        current_node = current_node.next

    logging.warning(f"Key {key} not found in the list.")
    return head

def display(head: Node) -> list:
    """Display the circular linked list."""
    if head is None:
        return []

    result = []
    current_node = head
    while True:
        result.append(current_node.data)
        current_node = current_node.next
        if current_node == head:
            break
    return result
