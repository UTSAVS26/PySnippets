from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def serialize(root):
    data, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            data.append(str(node.value))
            queue.append(node.left)
            queue.append(node.right)
        else:
            data.append('#')
    return ' '.join(data)

def deserialize(data):
    if data == '#':
        return None
    nodes = data.split()
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    index = 1
    while queue:
        node = queue.popleft()
        if nodes[index] != '#':
            node.left = TreeNode(int(nodes[index]))
            queue.append(node.left)
        index += 1
        if nodes[index] != '#':
            node.right = TreeNode(int(nodes[index]))
            queue.append(node.right)
        index += 1
    return root
