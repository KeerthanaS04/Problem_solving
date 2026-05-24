from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None):
        self.val=int(x)
        self.next=next
        self.random=random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # dictionary to map original nodes to their corresponding nodes
        original_to_copy = {}
        dummy = Node(0)
        tail = dummy

        # first pass: create all nodes and build the next pointers
        curr = head
        while curr:
            new_node = Node(curr.val)

            # link the new_node to the curr_list
            tail.next=new_node
            tail=tail.next

            # store mapping from original to copied value
            original_to_copy[curr]=new_node
            curr=curr.next
        
        # second pass: set up the random pointers using the mapping
        curr=head
        while curr:
            # set random pointer of copied node to the copied version of the random node
            if curr.random:
                original_to_copy[curr].random = original_to_copy[curr.random]
            else:
                original_to_copy[curr].random = None
            curr = curr.next
        return dummy.next