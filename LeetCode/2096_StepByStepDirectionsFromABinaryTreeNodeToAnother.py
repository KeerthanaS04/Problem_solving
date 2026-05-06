from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_lca(node: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
            # p: startValue, q: destValue
            if node is None or node.val in (p, q):
                return node
            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)

            # if both left and right are not None, then this node is the LCA
            if left and right:
                return node
            
            # otherwise, return the non-None child
            return left or right
        
        def find_path(node: Optional[TreeNode], target: int, path: List[str]) -> bool:
            if node is None:
                return False
            if node.val == target:
                return True
            
            path.append('L')
            if find_path(node.left, target, path):
                return True

            path[-1] = 'R'
            if find_path(node.right, target, path):
                return True
            path.pop()
            return False
        
        lca_node = find_lca(root, startValue, destValue)
        path_start: List[str] = []
        path_dest: List[str] = []

        find_path(lca_node, startValue, path_start)
        find_path(lca_node, destValue, path_dest)

        return 'U'*len(path_start) + ''.join(path_dest)