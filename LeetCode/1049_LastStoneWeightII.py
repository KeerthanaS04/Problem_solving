from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        n = len(stones)
        target = total_sum//2
        dp = [[0]*(target+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(target+1):
                # don't include the curr stone
                dp[i][j] = dp[i-1][j]
                # include the curr stone if it fits
                if stones[i-1]<=j:
                    dp[i][j] = max(
                        dp[i][j], dp[i-1][j-stones[i-1]]+stones[i-1]
                    )
        return total_sum-2*dp[n][target]