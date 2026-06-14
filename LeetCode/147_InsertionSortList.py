from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(float('-inf'))
        dummy.next = head

        prev_node = head
        curr_node = head.next

        while curr_node:
            if prev_node.val<=curr_node.val:
                prev_node = curr_node
                curr_node = curr_node.next
                continue

            insert_pos = dummy
            while insert_pos.next and insert_pos.next.val<curr_node.val:
                insert_pos = insert_pos.next
            
            # remove curr_node from the list
            next_to_process = curr_node.next
            prev_node.next = next_to_process

            # insert curr_node at the correct position
            curr_node.next = insert_pos.next
            insert_pos.next = curr_node
            curr_node = next_to_process
        return dummy.next