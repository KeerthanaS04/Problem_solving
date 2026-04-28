from functools import cache
from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        @cache
        def dfs(row: int, col: int, open_count: int) -> bool:
            # update the open parentheses count based on curr cell
            delta = 1 if grid[row][col]=='(' else -1
            open_count+=delta

            # pruning: invalid if negative count or impossible to balance
            if open_count<0:
                return False
            
            # maximum possible closing parentheses from curr position to end
            remaining_steps = (rows-row-1)+(cols-col-1)
            if open_count>remaining_steps:
                return False
            
            if row==rows-1 and col==cols-1:
                return open_count==0
            
            # try moving right and down
            directions = [(0,1),(1,0)]
            for dx, dy in directions:
                next_row, next_col = row+dx, col+dy
                if 0<=next_row<rows and 0<=next_col<cols:
                    if dfs(next_row, next_col, open_count):
                        return True
            return False
        
        rows, cols = len(grid), len(grid[0])
        if (rows+cols-1)%2!=0:
            return False
        
        if grid[0][0]==')' or grid[rows-1][cols-1]=='(':
            return False
        return dfs(0,0,0)