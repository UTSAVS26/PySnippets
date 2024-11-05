class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.keys = []  # List of keys
        self.children = []  # List of child pointers
        self.leaf = leaf  # Boolean to indicate if the node is a leaf

    # Function to traverse all nodes in a subtree rooted with this node
    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[len(self.keys)].traverse()

    # Function to search a key in the subtree rooted with this node
    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1

        if i < len(self.keys) and self.keys[i] == k:
            return self

        if self.leaf:
            return None

        return self.children[i].search(k)


class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t  # Minimum degree

    # Function to traverse the tree
    def traverse(self):
        if self.root is not None:
            self.root.traverse()

    # Function to search a key in this tree
    def search(self, k):
        return self.root.search(k) if self.root else None

    # Function to insert a new key in this tree
    def insert(self, k):
        if self.root is None:
            self.root = BTreeNode(self.t, leaf=True)
            self.root.keys = [k]
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                s = BTreeNode(self.t, leaf=False)
                s.children.insert(0, self.root)
                self.split_child(s, 0)
                i = 0
                if s.keys[0] < k:
                    i += 1
                self.insert_non_full(s.children[i], k)
                self.root = s
            else:
                self.insert_non_full(self.root, k)

    # Function to split the child of a node
    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    # Function to insert a new key into a non-full node
    def insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k)

