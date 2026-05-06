from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            curr_path = node.val + left + right

            nonlocal max_sum
            max_sum = max(max_sum, curr_path)
            return node.val + max(left, right)
        max_sum = float('-inf')
        dfs(root)
        return max_sum