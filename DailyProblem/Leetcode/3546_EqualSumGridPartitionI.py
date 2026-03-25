from typing import List
class Solution:
    def canPartition(self, grid: List[List[int]]) -> bool:
        total_sum = sum(sum(row) for row in grid)
        if total_sum%2:
            return False
        
        target_sum = total_sum//2

        # partition by cutting between rows
        prefix = 0
        for i, row in enumerate(grid):
            prefix+=sum(row)
            if prefix==target_sum and i!=len(grid)-1:
                return True
        
        # partition by cutting between columns
        prefix = 0
        # transpose the grid to iterate through columns
        for j, col in enumerate(zip(*grid)):
            prefix+=sum(col)

            if prefix==target_sum and j!=len(grid[0]-1):
                return True
        return False