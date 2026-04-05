class Solution:
    def totalWays(self, arr, target):
        total_sum = sum(arr)

        # negative = x
        # total_sum = s, positive = s-x
        # (s-x)-x = target => x = (s-target)//2
        if total_sum<abs(target) or (total_sum-target)%2!=0:
            return 0
        n = len(arr)
        negative_target = (total_sum-target)//2
        dp = [[0]*(negative_target+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            curr_num = arr[i-1]
            for j in range(negative_target+1):
                dp[i][j] = dp[i-1][j]

                if j>=curr_num:
                    dp[i][j]+=dp[i-1][j-curr_num]
        return dp[n][negative_target]