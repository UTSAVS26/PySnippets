class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_value = preorder.pop(0)
    root = TreeNode(root_value)
    inorder_index = inorder.index(root_value)
    root.left = build_tree(preorder, inorder[:inorder_index])
    root.right = build_tree(preorder, inorder[inorder_index + 1:])
    return root
