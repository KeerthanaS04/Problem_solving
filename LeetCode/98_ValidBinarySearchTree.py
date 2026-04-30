from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_traversal(node: Optional[TreeNode]) -> bool:
            # empty tree is valid
            if node is None:
                return True
            
            # validate left subtree
            if not inorder_traversal(node.left):
                return False
            
            # check curr node val against prev val
            nonlocal prev_val
            if prev_val>=node.val:
                return False
            return inorder_traversal(node.right)
        prev_val = -inf
        return inorder_traversal(root)