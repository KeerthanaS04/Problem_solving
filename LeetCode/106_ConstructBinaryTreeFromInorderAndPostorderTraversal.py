from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: left->root->right
        # postorder: left->right->root
        def dfs(inorder_start: int, postorder_start: int, subtree_size: int) -> Optional[TreeNode]:
            if subtree_size<=0:
                return None
            
            # the last element in postorder range is the root of the current subtree
            root_val = postorder[postorder_start+subtree_size-1]

            # find root's index in inorder
            root_inorder_idx = inorder_index_map[root_val]
            left_subtree_size = root_inorder_idx-inorder_start

            # recursively build left subtree
            # left subtree elements in inorder: [inorder_start, root_inorder_idx]
            # left subtree elements in postorder: [postorder_start, postorder_start+left_subtree_size]
            left_subtree = dfs(inorder_start, postorder_start, left_subtree_size)

            # recursively build right subtree
            # right subtree elements in inorder: [root_inorder_idx+1, inorder_start+subtree_size]
            # right subtree elements in postorder: [postorder_start+left_subtree_size, postorder_start+subtree_size-1]
            right_subtree = dfs(root_inorder_idx+1, postorder_start+left_subtree_size, subtree_size-left_subtree_size-1)

            return TreeNode(root_val, left_subtree, right_subtree)
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        return dfs(0, 0, len(inorder))