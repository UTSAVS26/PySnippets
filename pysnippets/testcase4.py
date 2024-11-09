class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.value < max_val):
        return False
    return is_bst(root.left, min_val, root.value) and is_bst(root.right, root.value, max_val)
