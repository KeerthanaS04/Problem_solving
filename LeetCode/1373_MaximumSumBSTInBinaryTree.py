from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int, int, int]:
            if node is None:
                return 1, float('inf'), float('-inf'), 0
            
            left_is_bst, left_max, left_min, left_sum = dfs(node.left)
            right_is_bst, right_max, right_min, right_sum = dfs(node.right)

            # check whether the subtree is valid bst or not
            if left_is_bst and right_is_bst and left_max<node.val<right_min:
                curr_sum = node.val+left_sum+right_sum

                nonlocal max_sum
                max_sum = max(max_sum, curr_sum)

                return (1, min(left_min, node.val), max(right_max, node.val), curr_sum)
            return 0,0,0,0
        max_sum = 0
        dfs(root)
        return max_sum