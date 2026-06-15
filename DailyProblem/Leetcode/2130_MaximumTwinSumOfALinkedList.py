from typing import Optional
class ListNode:
    def __init(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        n = len(values)

        max_sum = max(values[i]+values[n-i-1] for i in range(n//2))
        return max_sum