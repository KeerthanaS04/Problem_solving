class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
class Solution:
    def solve(self, node):
        if node is None:
            return 0
        
        left_sum = self.solve(node.left)
        right_sum = self.solve(node.right)

        curr_val = node.data
        node.data = left_sum+right_sum

        return left_sum+right_sum+curr_val
    
    def toSumTree(self, root):
        self.solve(root)