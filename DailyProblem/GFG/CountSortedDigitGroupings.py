class Solution:
    def validGroups(self, s):
        n = len(s)

        # maximum possible digit sum = 9*100=900
        memo = [[-1]*901 for _ in range(n)]

        def dfs(idx, prev_sum):
            if idx==n:
                return 1
            if memo[idx][prev_sum]!=-1:
                return memo[idx][prev_sum]
            count = 0
            curr_sum = 0

            for i in range(idx, n):
                curr_sum+=int(s[i])

                if curr_sum>=prev_sum:
                    count+=dfs(i+1, curr_sum)
            memo[idx][prev_sum]=count
            return count
        return dfs(0,0)