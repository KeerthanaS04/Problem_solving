class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def preOrder(self, root):
        res = []

        def traverse_preorder(node):
            if node is None:
                return
            res.append(node.data)
            traverse_preorder(node.left)
            traverse_preorder(node.right)

        traverse_preorder(root)
        return res