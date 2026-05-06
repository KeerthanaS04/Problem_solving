from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            curr_diameter = left_height + right_height
            self.diameter = max(self.diameter, curr_diameter)

            # return the height of this subtree
            return 1+max(left_height, right_height)
        dfs(root)
        return self.diameter