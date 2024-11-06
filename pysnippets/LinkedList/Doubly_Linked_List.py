from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Node:
    data: any
    next: 'Node' = None
    prev: 'Node' = None

def insert_end(head: Node, data: any) -> Node:
    """Insert a node at the end of the doubly linked list."""
    new_node = Node(data)
    if head is None:
        return new_node

    last_node = head
    while last_node.next:
        last_node = last_node.next
    last_node.next = new_node
    new_node.prev = last_node
    return head

def delete_node(head: Node, key: any) -> Node:
    """Delete a node with a specific value from the doubly linked list."""
    current_node = head

    if current_node is not None and current_node.data == key:
        head = current_node.next
        if head:
            head.prev = None
        return head

    while current_node is not None and current_node.data != key:
        current_node = current_node.next

    if current_node is None:
        logging.warning(f"Key {key} not found in the list.")
        return head

    if current_node.next:
        current_node.next.prev = current_node.prev
    if current_node.prev:
        current_node.prev.next = current_node.next

    return head

def display(head: Node) -> list:
    """Display the doubly linked list."""
    result = []
    current_node = head
    while current_node:
        result.append(current_node.data)
        current_node = current_node.next
    return result
