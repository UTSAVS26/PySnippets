class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """Insert a new key into the BST."""
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root, sorted_list):
    """Perform in-order traversal of the BST."""
    if root:
        inorder_traversal(root.left, sorted_list)
        sorted_list.append(root.val)
        inorder_traversal(root.right, sorted_list)

def tree_sort(arr):
    """Sort the array using Tree Sort."""
    if not arr:
        return arr
    
    root = None
    for key in arr:
        root = insert(root, key)
    
    sorted_list = []
    inorder_traversal(root, sorted_list)
    return sorted_list

