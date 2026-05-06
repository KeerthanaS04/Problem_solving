from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # count the total number of nodes
        curr = head
        total_node = 0
        while curr:
            total_node+=1
            curr = curr.next
        k = k%total_node

        if k==0: # no rotation needed
            return head
        
        slow = head
        fast = head
        for _ in range(k):
            fast = fast.next
        
        # move both pointers until we reach the last node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head