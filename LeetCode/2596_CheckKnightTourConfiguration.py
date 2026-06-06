from typing import List
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0]!=0:
            return False
        n = len(grid)

        # create a position mapping: val->(row, col)
        pos = [None]*(n*n)
        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                pos[val] = (r, c)
        
        for i in range(len(pos)-1):
            curr_pos = pos[i]
            next_pos = pos[i+1]

            row_diff = abs(curr_pos[0]-next_pos[0])
            col_diff = abs(curr_pos[1]-next_pos[1])
            valid_move = (row_diff==2 and col_diff==1) or (row_diff==1 and col_diff==2)

            if not valid_move:
                return False
        return True