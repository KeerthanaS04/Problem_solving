from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], curr_sum: int) -> None:
            if node is None:
                return
            curr_sum += node.val
            curr_path.append(node.val)

            # check if we've reached a node with target val
            if node.left is None and node.right is None and curr_sum == targetSum:
                res.append(curr_path[:])
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            # backtrack
            curr_path.pop()
        res: List[List[int]] = []
        curr_path: List[int] = []
        dfs(root, 0)
        return res