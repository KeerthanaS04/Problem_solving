from typing import List
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()

        # position of each idx in the original array
        pos = [0] * n
        for i in range(1, n):
            pos[arr[i][1]] = i

        # number of levels for binary lifting
        LOG = 1
        while (1<<LOG) < n:
            LOG += 1
        
        # binary lifting table
        up = [[0]*(LOG) for _ in range(n)]

        # compute farthest reachable idx in one hop
        r = 0
        for l in range(n):
            if r<l:
                r = l
            while r+1<n and arr[r+1][0]-arr[r][0] <= maxDiff:
                r += 1
            up[l][0] = r
        
        # binary lifting table
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
        
        ans = []
        for u, v in queries:
            src = pos[u]
            dest = pos[v]

            if src>dest:
                src, dest = dest, src
            
            if src == dest:
                ans.append(0)
                continue

            curr = src
            hops = 0

            # binary lifting to find minimum hops
            for j in range(LOG-1, -1, -1):
                if up[curr][j] < dest:
                    curr = up[curr][j]
                    hops += 1<<j
            
            if up[curr][0]>=dest:
                ans.append(hops)
            else:
                ans.append(-1)
        return ans