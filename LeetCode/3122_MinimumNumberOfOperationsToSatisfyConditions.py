from typing import List
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')*10 for _ in range(cols)]]

        for col in range(cols):
            val_count = [0]*10
            for row in range(rows):
                val_count[grid[row][col]] += 1

                # base case: first column can be any value
                # operations needed = total cells-cells already have target val
                if col==0:
                    for target_val in range(10):
                        dp[col][target_val] = rows-val_count[target_val]
                else:
                    for curr_val in range(10):
                        for prev_val in range(10):
                            if prev_val!=curr_val:
                                operations_needed = dp[col-1][prev_val]+rows-val_count[curr_val]
                                dp[col][curr_val] = min(dp[col][curr_val], operations_needed)
        return min(dp[-1])