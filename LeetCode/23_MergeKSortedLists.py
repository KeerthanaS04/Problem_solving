from typing import List, Optional
from heapq import heapify, heappop, heappush
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # add comparison method to ListNode for heap operations
        setattr(ListNode, "__lt__", lambda self, other: self.val<other.val)

        # priority queue with all non null heads
        priority_queue = [head for head in lists if head]
        # convert list to min-heap
        heapify(priority_queue)

        # to simplify list construction
        dummy_head = ListNode()
        curr_node = dummy_head

        while priority_queue:
            min_node = heappop(priority_queue)

            # if extracted node has a next node, add it to the heap
            if min_node.next:
                heappush(priority_queue, min_node.next)
            
            # append the min_node to the result list
            curr_node.next = min_node
            curr_node = curr_node.next
        return dummy_head.next