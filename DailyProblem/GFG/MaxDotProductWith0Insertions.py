class Solution:
    def maxDotProduct(self, a, b):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            k = min(i, m)
            for j in range(1, k + 1):
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i-1][j-1] + a[i-1] * b[j-1]
                )
        return dp[n][m]