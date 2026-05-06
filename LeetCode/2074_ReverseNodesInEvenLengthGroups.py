from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_group(group_head: Optional[ListNode], group_size: int) -> Optional[ListNode]:
            prev = None
            curr_node = group_head
            tail_node = group_head

            nodes_reversed = 0
            while curr_node and nodes_reversed<group_size:
                next_temp = curr_node.next
                curr_node.next = prev
                prev = curr_node
                curr_node = next_temp
                nodes_reversed+=1
            
            # connect the tail of the reversed group to remaining list
            tail_node.next = curr_node
            return prev
        
        # count total number of nodes in the list
        total_node = 0
        temp_node = head
        while temp_node:
            total_node+=1
            temp_node = temp_node.next
        
        dummy = ListNode(0, head)
        prev_node_tail = dummy
        group_size = 1

        while (1+group_size)*group_size//2 <= total_node and prev_node_tail:
            if group_size%2==0: # reverse the current group if its size is even
                prev_node_tail.next = reverse_group(prev_node_tail.next, group_size)
            
            # move prev_node_tail to the tail of the current group
            nodes_traversed = 0
            while prev_node_tail and nodes_traversed<group_size:
                prev_node_tail = prev_node_tail.next
                nodes_traversed+=1
            group_size+=1
        
        # handle the last group
        nodes_processed = (group_size-1)*group_size//2
        remaining_nodes = total_node - nodes_processed

        if remaining_nodes>0 and remaining_nodes%2==0:
            prev_node_tail.next = reverse_group(prev_node_tail.next, remaining_nodes)
        return dummy.next