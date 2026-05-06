from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        stack = []
        for val in values:
            while stack and stack[-1]<val:
                stack.pop()
            stack.append(val)
        
        dummy = ListNode()
        curr = dummy
        for val in stack:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next