from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root->left->right
        # inorder: left->root->right
        def dfs(preorder_start: int, inorder_start: int, subtree_size: int) -> Optional[TreeNode]:
            if subtree_size<=0:
                return None
            
            root_val = preorder[preorder_start]
            # find root's index in inorder
            root_inorder_idx = inorder_index_map[root_val]
            # calculate left subtree size
            left_subtree_size = root_inorder_idx-inorder_start

            left_child = dfs(preorder_start+1, inorder_start, left_subtree_size)
            right_child = dfs(preorder_start+1+left_subtree_size, root_inorder_idx+1, subtree_size-left_subtree_size-1)
            return TreeNode(root_val, left_child, right_child)
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        return dfs(0, 0, len(inorder))