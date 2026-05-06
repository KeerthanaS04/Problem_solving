from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # if the left child exists and has the same val, extend the left path
            left_path = left+1 if node.left and node.left.val==node.val else 0
            # if the right child exists and has the same val, extend the right path
            right_path = right+1 if node.right and node.right.val==node.val else 0

            self.max_length = max(self.max_length, left_path+right_path)
            return max(left_path, right_path)
        dfs(root)
        return self.max_length