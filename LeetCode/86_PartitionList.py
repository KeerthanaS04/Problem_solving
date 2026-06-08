from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode()
        right_dummy = ListNode()

        left_tail = left_dummy
        right_tail = right_dummy

        while head:
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            elif head.val > x:
                right_tail.next = head
                right_tail = right_tail.next
            head = head.next
        
        # terminate the right partition
        right_tail.next = None
        # connect the left and right partitions
        left_tail.next = right_dummy.next
        return left_dummy.next