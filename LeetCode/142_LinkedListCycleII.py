from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                start_ptr = head

                # move both pointers one step at a time, the meeting point is the start of the cycle
                while start_ptr != slow:
                    start_ptr = start_ptr.next
                    slow = slow.next
                return start_ptr
        return None