class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

def tree_sort(arr):
    if len(arr) == 0:
        return []
    root = Node(arr[0])
    for i in range(1, len(arr)):
        insert(root, arr[i])
    result = []
    inorder(root, result)
    return result
