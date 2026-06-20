from typing import List
class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        dp = [float('inf')]*n
        dp[0] = 0

        for i, x in restrictions:
            dp[i] = min(dp[i], x)

        # left->right
        for i in range(n-1):
            dp[i+1] = min(dp[i+1], dp[i]+diff[i])
        
        # right->left
        for i in reversed(range(n-1)):
            dp[i] = min(dp[i], dp[i+1]+diff[i])
        return max(dp)