from collections import deque
from itertools import pairwise
from typing import List
from math import inf
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        dist = [[inf]*cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        queue = deque([(0, 0)])
        directions = (-1,0,1,0,-1)

        # BFS
        while queue:
            curr_x, curr_y = queue.popleft()
            for dx, dy in pairwise(directions):
                next_x, next_y = curr_x + dx, curr_y + dy
                if (0<=next_x<rows) and (0<=next_y<cols) and (dist[next_x][next_y] > dist[curr_x][curr_y] + grid[next_x][next_y]):
                    dist[next_x][next_y] = dist[curr_x][curr_y] + grid[next_x][next_y]
                    queue.append((next_x, next_y))
        
        return dist[-1][-1] < health