class Solution:
    def countWays(self, n, sum):
        MOD = 10**9+7
        # dp[i][j] = number of i-digit numbers with digit sum j
        dp = [[0]*(sum+1) for _ in range(n+1)]
        dp[0][0] = 1

        # first digit cannot be 0
        for d in range(1, 10):
            if d<=sum:
                dp[1][d] = 1
        
        for i in range(2, n+1):
            for j in range(1, sum+1):
                for d in range(1, 10):
                    if j>=d:
                        dp[i][j] = (dp[i][j]+dp[i-1][j-d])%MOD
        return -1 if dp[n][sum]==0 else dp[n][sum]