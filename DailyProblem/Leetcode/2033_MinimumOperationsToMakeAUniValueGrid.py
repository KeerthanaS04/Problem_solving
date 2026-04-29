from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # flatten the grid into a 1D list
        flatten_values = []
        ref_remainder = grid[0][0]%x

        for row in grid:
            for val in row:
                if val%x!=ref_remainder:
                    return -1
                flatten_values.append(val)
        
        flatten_values.sort()
        median_idx = len(flatten_values)//2
        median_val = flatten_values[median_idx]

        total_operations = sum(abs(val-median_val)//x for val in flatten_values)
        return total_operations