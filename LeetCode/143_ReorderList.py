from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder(self, head: Optional[ListNode]) -> None:
        slow_ptr, fast_ptr = head

        # find the middle
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # split the list into halves
        sec_half_head = slow_ptr.next
        slow_ptr.next = None

        # reverse the second half of the list
        prev_node = None
        curr_node = sec_half_head
        while curr_node:
            next_temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_temp
        
        # prev_node now points to the head of the reversed second half
        reversed_sec_half = prev_node
        first_half = head

        while reversed_sec_half:
            first_half_next = first_half.next
            sec_half_next = reversed_sec_half.next

            # connect nodes alternatively
            first_half.next = reversed_sec_half
            reversed_sec_half.next = first_half_next

            first_half = first_half_next
            reversed_sec_half = sec_half_next