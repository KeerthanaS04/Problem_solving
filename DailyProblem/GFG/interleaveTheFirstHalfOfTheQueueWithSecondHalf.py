from collections import deque
class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        q1 = deque()

        for _ in range(n//2):
            q1.append(q.popleft())
        
        ans = deque()
        while q1:
            ans.append(q1.popleft())
            ans.append(q.popleft())
        
        q.extend(ans)