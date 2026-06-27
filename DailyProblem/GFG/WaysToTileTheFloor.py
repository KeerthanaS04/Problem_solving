from collections import deque
class Solution:
    def countWays(self, n, m):
        MOD = 10**9 + 7
        dp = deque()

        for i in range(1, n+1):
            if i<m:
                dp.append(1)
            elif i==m:
                dp.append(2)
            else:
                ways = (dp[-1]+dp[0])%MOD
                dp.popleft()
                dp.append(ways)
        return dp[-1]