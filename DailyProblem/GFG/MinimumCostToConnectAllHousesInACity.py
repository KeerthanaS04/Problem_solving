class Solution:
    def minCost(self, houses):
        n, ans = len(houses), 0
        vis = [0]*n
        d = [float('inf')]*n
        d[0] = 0

        for _ in range(n):
            m, u = float('inf'), -1
            for i in range(n):
                if not vis[i] and d[i]<m:
                    m = d[i]
                    u = i
            vis[u] = 1
            ans+=m

            for v in range(n):
                if not vis[i]:
                    d[v] = min(d[v], abs(houses[u][0] - houses[v][0])+abs(houses[u][1]-houses[v][1]))
        return ans