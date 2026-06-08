class Node:
    def __init__(self, x):
        self.data=x
        self.next=None

class Solution:
    def compute(self, head):
        # reverse the linked list
        prev=None
        curr=head

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        head=prev
        # remove nodes having greater value on th left
        curr=head.next
        prev=head
        mx=head.data

        while curr:
            if curr.data<mx:
                prev.next=curr.next
                curr=prev.next
            else:
                mx=max(mx, curr.data)
                prev=curr
                curr=curr.next
        
        # reverse again to restore original order
        prev=None
        curr=head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev