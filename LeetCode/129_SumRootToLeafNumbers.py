from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def sumNumber(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], curr_num: int) -> int:
            if node is None:
                return 0
            
            curr_num = curr_num*10+node.val
            if node.left is None and node.right is None:
                return curr_num
            
            left_sum = dfs(node.left, curr_num)
            right_sum = dfs(node.right, curr_num)
        return dfs(root, 0)