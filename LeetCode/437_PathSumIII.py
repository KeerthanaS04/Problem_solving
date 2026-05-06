from collections import Counter
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if node is None:
                return 0
            
            curr_sum += node.val
            path_count = prefix_sum_count[curr_sum-targetSum]
            prefix_sum_count[curr_sum] += 1

            path_count += dfs(node.left, curr_sum)
            path_count += dfs(node.right, curr_sum)

            # remove curr sum from counter as we return up the tree
            prefix_sum_count[curr_sum] -= 1
            return path_count
        # to handle paths starting from the root
        prefix_sum_count = Counter({0: 1})
        return dfs(root, 0)