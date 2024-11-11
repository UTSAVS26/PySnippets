# Linked List Implementations

This directory contains implementations of various types of linked lists in Python, including:

- Circular Linked List
- Doubly Linked List
- Singly Linked List

## Overview

Linked lists are a fundamental data structure that consist of nodes, where each node contains data and a reference (or link) to the next node in the sequence. This allows for efficient insertion and deletion of elements, as opposed to arrays where elements must be shifted.

### Types of Linked Lists

1. **Singly Linked List**: Each node points to the next node, and the last node points to `None`.
2. **Doubly Linked List**: Each node points to both the next and the previous nodes, allowing traversal in both directions.
3. **Circular Linked List**: The last node points back to the first node, forming a circle.

## Features

Each linked list implementation includes the following functions:

- **Insert a Node at the End**: Adds a new node with the specified data at the end of the list.
- **Delete a Node by Value**: Removes the first node that contains the specified value.
- **Display the Linked List**: Returns a list of all node values in the linked list.

## Function Descriptions

### 1. `insert_end(head: Node, data: any) -> Node`
- **Purpose**: Inserts a new node with the given data at the end of the linked list.
- **Parameters**:
  - `head`: The head node of the linked list.
  - `data`: The data to be stored in the new node.
- **Returns**: The head of the linked list.

### 2. `delete_node(head: Node, key: any) -> Node`
- **Purpose**: Deletes the first node that contains the specified key.
- **Parameters**:
  - `head`: The head node of the linked list.
  - `key`: The value of the node to be deleted.
- **Returns**: The head of the linked list after deletion.

### 3. `display(head: Node) -> list`
- **Purpose**: Returns a list of all node values in the linked list.
- **Parameters**:
  - `head`: The head node of the linked list.
- **Returns**: A list containing the data of each node.

## Usage

You can import the linked list classes and functions into your Python scripts. Each implementation uses a `Node` class defined with `dataclasses` for better readability and maintainability.

### Example Usage

```python
from Circular_Linked_List import insert_end, delete_node, display
head = None
head = insert_end(head, 1)
head = insert_end(head, 2)
head = insert_end(head, 3)
print(display(head)) # Output: [1, 2, 3]
head = delete_node(head, 2)
print(display(head)) # Output: [1, 3]
```

```bash
python -m unittest test_linked_lists.py
```

## Explanation of the Approach
The approach taken in the linked list implementations focuses on:

- Clarity and Readability: Each function is clearly defined with descriptive names and docstrings, making it easy for users to understand the purpose and usage of each function.

- Data Classes: The use of dataclasses for the Node class simplifies the code and enhances readability by automatically generating special methods like __init__() and __repr__().

- Logging: The inclusion of logging provides a way to track operations and catch potential issues, such as attempting to delete from an empty list or trying to delete a non-existent key.

- Testing: A dedicated test file ensures that all functionalities are covered and work as expected, promoting reliability and maintainability.

- Modularity: Each linked list type is implemented in its own file, allowing for easy extension and modification without affecting other implementations.
This structured approach not only enhances the usability of the linked list implementations but also serves as a solid foundation for further development and learning. If you have any more requests or need further modifications, feel free to ask!

