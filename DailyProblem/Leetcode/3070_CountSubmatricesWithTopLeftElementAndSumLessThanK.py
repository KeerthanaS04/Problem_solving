from typing import List
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        prefix_sum = [[0]*(cols+1) for _ in range(rows+1)]
        count = 0

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                # sum = sum_above+sum_left-sum_diagonal+curr_element (using inclusion-exclusion principle)
                prefix_sum[i][j] = prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+grid[i-1][j-1]

                if prefix_sum[i][j]<=k:
                    count+=1
        return count