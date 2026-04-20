class Solution:
    def derangeCount(self, n: int) -> int:
        N = 1<<n
        dp = [[-1]*N for _ in range(n+1)]

        def f(i, mask):
            if i==n:
                return 1
            if dp[i][mask]!=-1:
                return dp[i][mask]
            
            ans = 0
            for j in range(n):
                # if j is already used
                if mask&(1<<j):
                    continue
                # avoid placing element at the same position
                if j==i:
                    continue

                ans+=f(i+1, mask|(1<<j))
            dp[i][mask] = ans
            return ans
        return f(0,0)