class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]

        for start in range(n-1, 0, -1):
            for end in range(start+1, n+1):
                # initialize with the worst case
                # if we pick j-1, and its wrong, we only need to check range[i, j-1)
                dp[start][end] = (end-1)+dp[start][end-1]
                for guess in range(start, end):
                    curr_cost = guess+max(
                        dp[start][guess-1], dp[guess+1][end]
                    )
                    dp[start][end] = min(dp[start][end], curr_cost)
        return dp[1][n]