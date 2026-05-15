class Solution:
    def optimalKeys(self, n: int) -> int:
        dp = [0]*(n+1)

        # base case: if only press 'A', then maxi characters = no of key presses
        for i in range(1, n+1):
            dp[i] = i
        
        # try every possible break point
        for i in range(1, n+1):
            # j = point before doing ctrl A, C, V
            for j in range(1, i-2):
                # 2 operations for ctrl A, C and rest are ctrl V
                dp[i] = max(dp[i], dp[j]*(i-j-1))
        return dp[n]