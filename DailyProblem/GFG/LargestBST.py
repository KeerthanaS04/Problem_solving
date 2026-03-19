from math import inf
from typing import Optional
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def largestBst(self, root: Optional[Node]) -> int:
        def dfs(node):
            if node is None:
                return inf, -inf, 0
            
            left_min, left_max, left_size = dfs(node.left)
            right_min, right_max, right_size = dfs(node.right)

            # check whether the subtree is valid or not
            if left_max<node.data<right_min:
                curr_size = left_size+right_size+1
                self.max_bst_size = max(self.max_bst_size, curr_size)
                return min(left_min, node.data), max(right_max, node.data), curr_size
            return -inf, inf, 0
        self.max_bst_size = 0
        dfs(root)
        return self.max_bst_size