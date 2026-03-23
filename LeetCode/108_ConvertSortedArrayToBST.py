from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left>right:
                return None
            mid = (left+right)>>1
            root = TreeNode(
                val = nums[mid],
                left = build_bst(left, mid-1),
                right=build_bst(mid+1, right)
            )
            return root
        return build_bst(0, len(nums)-1)