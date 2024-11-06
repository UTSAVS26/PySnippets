from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Node:
    data: any
    next: 'Node' = None

def insert_end(head: Node, data: any) -> Node:
    """Insert a node at the end of the singly linked list."""
    new_node = Node(data)
    if head is None:
        return new_node

    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node
    return head

def delete_node(head: Node, key: any) -> Node:
    """Delete a node with a specific value from the singly linked list."""
    current_node = head

    if current_node is not None and current_node.data == key:
        return current_node.next

    while current_node is not None and current_node.next is not None:
        if current_node.next.data == key:
            current_node.next = current_node.next.next
            return head
        current_node = current_node.next

    logging.warning(f"Key {key} not found in the list.")
    return head

def display(head: Node) -> list:
    """Display the singly linked list."""
    result = []
    current_node = head
    while current_node:
        result.append(current_node.data)
        current_node = current_node.next
    return result
