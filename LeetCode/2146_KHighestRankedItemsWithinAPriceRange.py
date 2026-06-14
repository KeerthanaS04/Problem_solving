from typing import List
from collections import deque
from itertools import pairwise
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        start_row, start_col = start
        min_price, max_price = pricing

        # initialize the queue with starting position
        bfs_queue = deque([(start_row, start_col)])
        # priority queue to store the valid items
        valid_items = []

        # check if starting cell is a valid item
        if min_price <= grid[start_row][start_col] <= max_price:
            valid_items.append((0, grid[start_row][start_col], start_row, start_col))
        
        # mark the starting cell as visited
        grid[start_row][start_col] = 0
        directions = (-1,0,1,0,-1)
        curr_dist = 0

        while bfs_queue:
            curr_dist += 1
            level_size = len(bfs_queue)
            for _ in range(level_size):
                curr_row, curr_col = bfs_queue.popleft()

                # explore all 4 directions
                for dr, dc in pairwise(directions):
                    next_row = curr_row + dr
                    next_col = curr_col + dc

                    # check if next cell is valid and unvisited
                    if (0<=next_row<rows and 0<=next_col<cols and grid[next_row][next_col]>0):
                        # check if cell price is on the range
                        if min_price <= grid[next_row][next_col] <= max_price:
                            valid_items.append((curr_dist, grid[next_row][next_col], next_row, next_col))
                        # mark cell as visited
                        grid[next_row][next_col] = 0
                        bfs_queue.append((next_row, next_col))
        valid_items.sort()
        return [[row, col] for _, _, row, col in valid_items[:k]]