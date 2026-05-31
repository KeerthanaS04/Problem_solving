from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values=[]
        curr=head
        while curr:
            values.append(curr.val)
            curr=curr.next
        
        stack=[]
        n=len(values)
        res=[0]*n

        for i in range(n-1, -1, -1):
            while stack and stack[-1]<=values[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(values[i])
        return res