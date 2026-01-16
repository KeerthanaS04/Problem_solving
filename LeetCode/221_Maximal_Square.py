from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    dp[i+1][j+1] = min(
                        dp[i][j+1], # Top cell
                        dp[i+1][j], # Left cell
                        dp[i][j] # Top-left diagonal cell
                    ) + 1
                    max_side = max(max_side, dp[i+1][j+1])

        return max_side * max_side