class Solution:
    def checkValidPoint(self, s: str) -> bool:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        # only * can be valid
        for i, char in enumerate(s):
            dp[i][i] = (char=='*')

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                # check if s[i] and s[j] can form a matching pair
                is_matching = (
                    s[i] in '(*' and s[j] in '*)' and (i+1==j or dp[i+1][j-1])
                )

                # try to split the substring at any position k
                can_split = any(
                    dp[i][k] and dp[k][j] for k in range(i,j)
                )

                # substring is valid if either case works
                dp[i][j] = is_matching or can_split
        return dp[0][n-1]