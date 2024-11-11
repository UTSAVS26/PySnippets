from dataclasses import dataclass
import logging
from typing import Optional, Any, List

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Node:
    data: Any
    next: 'Node' = None  # Type hint for forward reference

def insert_end(head: Optional[Node], data: Any) -> Node:
    """Insert a node at the end of the circular linked list."""
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        logging.info(f"Inserted {data} as the first node.")
        return new_node

    last_node = head
    while last_node.next != head:
        last_node = last_node.next
    last_node.next = new_node
    new_node.next = head
    logging.info(f"Inserted {data} at the end of the list.")
    return head

def delete_node(head: Optional[Node], key: Any) -> Optional[Node]:
    """Delete a node with a specific value from the circular linked list."""
    if head is None:
        logging.warning("Attempted to delete from an empty list.")
        return None

    current_node = head
    previous_node = None

    # Case: Head needs to be deleted
    if current_node.data == key:
        if current_node.next == head:  # Only one node
            logging.info(f"Deleted the only node with key {key}.")
            return None
        # Find the last node to update its next pointer
        while current_node.next != head:
            current_node = current_node.next
        current_node.next = head.next
        logging.info(f"Deleted head node with key {key}.")
        return head.next

    # Case: Delete a non-head node
    while current_node.next != head:
        if current_node.next.data == key:
            current_node.next = current_node.next.next
            logging.info(f"Deleted node with key {key}.")
            return head
        current_node = current_node.next

    logging.warning(f"Key {key} not found in the list.")
    return head

def display(head: Optional[Node]) -> List[Any]:
    """Display the circular linked list as a list of node data."""
    if head is None:
        logging.info("Display requested on an empty list.")
        return []

    result = []
    current_node = head
    while True:
        result.append(current_node.data)
        current_node = current_node.next
        if current_node == head:
            break
    logging.info(f"List contents: {result}")
    return result