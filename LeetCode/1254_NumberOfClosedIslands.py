from typing import List
class Solution:
    def closedIslands(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int) -> int:
            not_boundary = int(0<r<rows-1 and 0<c<cols-1)
            grid[r][c] = 1

            for i in range(4):
                nr = r+directions[i]
                nc = c+directions[i+1]

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==0:
                    not_boundary&=dfs(nr,nc)
            return not_boundary
        rows, cols = len(grid), len(grid[0])
        directions = [-1,0,1,0,-1]
        closed_island_cnt = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0 and dfs(row,col):
                    closed_island_cnt+=1
        return closed_island_cnt