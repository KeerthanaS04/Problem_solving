class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Find the minimum ASCII sum of deleted characters to make two strings equal

        Args:
            s1: First Input string
            s2: Second Input string

        Returns:
            Minimum ASCII sum of deleted characters
        """
        len_s1, len_s2 = len(s1), len(s2)

        # Create the dp table
        dp = [[0]*(len_s2+1) for _ in range(len_s1+1)]

        # First Column: delete all characters from s1[0:i]
        for i in range(1, len_s1+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        # First Row: delete all characters from s2[0:j]
        for j in range(1, len_s2+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        # Fill the dp table
        for i in range(1, len_s1+1):
            for j in range(1, len_s2+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] =  min(dp[i-1][j]+ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]))

        return dp[len_s1][len_s2]