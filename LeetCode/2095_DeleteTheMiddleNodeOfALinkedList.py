from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = dummy # slow starts before head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next # slow will reach exactly before the middle
        return dummy.next