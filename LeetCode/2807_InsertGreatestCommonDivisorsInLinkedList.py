from math import gcd
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, curr_node = head, head.next

        while curr_node:
            gcd_val = gcd(prev_node.val, curr_node.val)
            prev_node.next = ListNode(gcd_val, curr_node)
            prev_node, curr_node = curr_node, curr_node.next
        return head