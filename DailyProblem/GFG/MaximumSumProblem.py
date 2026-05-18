class Solution:
    def solve(self, n, dp):
        if n==0 or n==1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n] = max(
            n,
            self.solve(n//2, dp)+self.solve(n//3, dp)+self.solve(n//4, dp)
        )
        return dp[n]
    def maxSum(self, n):
        dp = [-1]*(n+1)
        return self.solve(n, dp)