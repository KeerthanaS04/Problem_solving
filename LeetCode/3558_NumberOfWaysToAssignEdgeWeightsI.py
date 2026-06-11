from typing import List
import collections
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(edges)+1

        if n==1:
            return 0
        
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = collections.deque([1])
        seen = {1}
        step = 0

        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            step+=1
        return pow(2, step-2, MOD) if step>0 else 0