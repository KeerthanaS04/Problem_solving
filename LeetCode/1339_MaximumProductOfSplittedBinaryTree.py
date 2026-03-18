from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def calculate_total_sum(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return node.val+calculate_total_sum(node.left)+calculate_total_sum(node.right)
        def find_max_product(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            subtree_sum = node.val+find_max_product(node.left)+find_max_product(node.right)

            nonlocal max_product, total_sum

            # the product will be s*(t-s)
            if subtree_sum<total_sum:
                max_product = max(max_product, subtree_sum*(total_sum-subtree_sum))
            return subtree_sum
        MOD = 10**9+7
        total_sum = calculate_total_sum(root)
        max_product = 0
        find_max_product(root)
        return max_product%MOD