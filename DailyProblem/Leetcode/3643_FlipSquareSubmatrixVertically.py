from typing import List
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for row_idx in range(x, x+k//2):
            mirror_row_idx = x+k-1-(row_idx-x)
            for col_idx in range(y, y+k):
                grid[row_idx][col_idx], grid[mirror_row_idx][col_idx] = grid[mirror_row_idx][col_idx], grid[row_idx][col_idx]
        return grid
