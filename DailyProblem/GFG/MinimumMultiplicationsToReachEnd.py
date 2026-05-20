from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        mod = 1000
        queue = deque()
        visited = [-1]*mod

        queue.append((start, 0))
        visited[start] = 1

        while queue:
            num, steps = queue.popleft()
            if num==end:
                return steps
            
            for val in arr:
                temp = (num*val)//mod

                if visited[temp]==-1:
                    visited[temp] = 1
                    queue.append((temp, steps+1))
        return -1