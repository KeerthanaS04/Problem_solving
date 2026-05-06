from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right:
            return head
        
        dummy = ListNode(0, head)
        before_reverse = dummy
        for _ in range(left-1):
            before_reverse = before_reverse.next
        
        first_reversed = before_reverse.next # the first node that will be reversed, will become the last after reversal
        prev = before_reverse
        curr = first_reversed

        for _ in range(right-left+1):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        before_reverse.next = prev
        first_reversed.next = curr

        return dummy.next