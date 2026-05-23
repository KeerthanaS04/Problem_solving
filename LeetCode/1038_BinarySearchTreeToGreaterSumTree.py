from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse_inorder_traversal(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            # traverse the right
            reverse_inorder_traversal(node.right)
            nonlocal running_sum
            running_sum+=node.val
            node.val=running_sum

            # traverse the left
            reverse_inorder_traversal(node.left)
        running_sum = 0
        reverse_inorder_traversal(root)
        return root