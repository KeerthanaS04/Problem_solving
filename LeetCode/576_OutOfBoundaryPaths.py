from functools import lru_cache
from itertools import pairwise

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        directions = (-1,0,1,0,-1)

        @lru_cache(None)
        def dfs(row: int, col: int, moves_left: int) -> int:
            # check if current position are out of bounds
            if not (0<=row<m) or not (0<=col<n):
                return int(moves_left>=0)
            
            if moves_left<=0:
                return 0
            count = 0
            for dx, dy in pairwise(directions):
                next_row = row+dx
                next_col = col+dy
                count = (count+dfs(next_row, next_col, moves_left-1))%MOD
            return count
        return dfs(startRow, startColumn, maxMove)