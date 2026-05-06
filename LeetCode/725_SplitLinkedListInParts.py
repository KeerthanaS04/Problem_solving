from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total_node = 0
        curr = head
        while curr:
            total_node+=1
            curr = curr.next
        
        # calculate the base size and number of parts that needs an extra node
        base_size, extra_node = divmod(total_node, k)
        res = [None]*k
        curr = head

        for i in range(k):
            if curr is None:
                break

            res[i] = curr
            curr_size = base_size + (1 if i<extra_node else 0)

            # traverse the last node of the current part
            for _ in range(1, curr_size):
                curr = curr.next
            
            # disconnect curr part from the rest of the list
            next_head = curr.next
            curr.next = None
            curr = next_head
        return res