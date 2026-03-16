from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        # find all rottem oranges and count fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    queue.append((row, col))
                elif grid[row][col]==1:
                    fresh_count+=1
        
        minutes = 0
        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        # BFS
        while queue and fresh_count>0:
            minutes+=1

            curr_size = len(queue)
            for _ in range(curr_size):
                curr_row, curr_col = queue.popleft()

                # check all 4 adjacent cells
                for dr, dc in directions:
                    next_row = curr_row+dr
                    next_col = curr_col+dc

                    if (0<=next_row<rows and 0<=next_col<cols and grid[next_row][next_col]==1):
                        grid[next_row][next_col]==2
                        queue.append((next_row, next_col))
                        fresh_count-=1

                        # Early termination
                        if fresh_count==0:
                            return minutes
        return -1 if fresh_count>0 else 0