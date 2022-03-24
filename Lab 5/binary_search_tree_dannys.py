class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None

    def insert(self, key):
        if self is None:
            return TreeNode(key)

        else:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                elif self.right is None:
                    self.right = TreeNode(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                elif self.left is None:
                    self.left = TreeNode(key)


class BinarySearchTree:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.key = key
        self.data = None
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        if self.data == self.left == self.right == self.key == self.root == None:
            return True
        else:
            return False

    def insert(self, newKey):
        if self.is_empty():
            self.root = newKey
        else:
            if newKey < self.root:
                if self.left is None:
                    self.left = TreeNode(newKey)
                    self.left.root = self.root
                else:
                    self.left.insert(newKey)
            if newKey > self.root:
                if self.right is None:
                    self.right = BinarySearchTree(newKey)
                    self.right.root = self.root
                else:
                    self.right.insert(newKey)


tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(3)



print(tree.root)
print(tree.root.left.key)
print(tree.root.left.left.key)







