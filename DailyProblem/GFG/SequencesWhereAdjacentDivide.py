class Solution:
    def solve(self, n, m, prev, dp):
        if n==0:
            return 1

        if dp[n][prev+1] != -1:
            return dp[n][prev+1]

        res = 0
        for i in range(1, m+1):
            if prev==-1:
                res += self.solve(n-1, m, i, dp)
            elif prev % i == 0 or i % prev == 0:
                res += self.solve(n-1, m, i, dp)
        dp[n][prev+1] = res
        return res

    def count(self, n: int, m: int) -> int:
        dp = [[-1]*(m+2) for _ in range(n+1)]
        return self.solve(n, m, -1, dp)