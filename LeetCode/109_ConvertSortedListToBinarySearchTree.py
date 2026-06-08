from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def bst(l: int, r: int) -> Optional[TreeNode]:
            if l>r:
                return None
            mid = (l+r)//2
            left_subtree = bst(l, mid-1)
            right_subtree = bst(mid+1, r)

            root = TreeNode(values[mid], left_subtree, right_subtree)
            return root
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return bst(0, len(values)-1)