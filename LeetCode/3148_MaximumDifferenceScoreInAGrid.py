from math import inf
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0]*cols for _ in range(rows)]
        max_score = -inf

        for i in range(rows):
            for j in range(cols):
                curr_val = grid[i][j]
                min_prev = inf

                # check we can come from above
                if i>0:
                    min_prev = min(min_prev, grid[i-1][j])
                # check we can come from left
                if j>0:
                    min_prev = min(min_prev, grid[i][j-1])
                
                max_score = max(max_score, curr_val-min_prev)
                dp[i][j] = min(curr_val, min_prev)
        return max_score