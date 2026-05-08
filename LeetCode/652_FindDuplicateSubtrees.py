from typing import Optional, List
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> str:
            if node is None:
                return '#'
            left_serialization = dfs(node.left)
            right_serialization = dfs(node.right)

            subtree_serialization = f'{node.val},{left_serialization},{right_serialization}'
            subtree_count[subtree_serialization]+=1

            if subtree_count[subtree_serialization]==2:
                duplicate.append(node)
            return subtree_serialization
        duplicate = []
        subtree_count = Counter()
        dfs(root)
        return duplicate