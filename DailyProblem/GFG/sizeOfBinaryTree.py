class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getSize(self, root):
        if root is None:
            return 0
        
        # count curr_node+left_subtree+right_subtree
        return 1 + self.getSize(root.left) + self.getSize(root.right)