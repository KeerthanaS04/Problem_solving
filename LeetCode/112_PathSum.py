from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], curr_sum: int) -> bool:
            if node is None:
                return False
            curr_sum += node.val
            if node.left is None and node.right is None:
                return curr_sum == targetSum
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        return dfs(root, 0)