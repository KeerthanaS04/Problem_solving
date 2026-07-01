from collections import deque
from math import inf
from typing import List
from itertools import pairwise
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return False
        
        # union by size: attach smaller to larger
        if self.size[root_a]>self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        return True

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # if start or end position has a thief, no safe path exists
        if grid[0][0] or grid[n-1][n-1]:
            return 0
        
        # calculate minimum distance from each cell to the nearest thief using BFS
        queue = deque()
        dist_to_thief = [[inf]*n for _ in range(n)]

        # initialize BFS queue with all thief positions
        for r in range(n):
            for c in range(n):
                if grid[r][c]: # found thief
                    queue.append((r, c))
                    dist_to_thief[r][c] = 0
        
        directions = (-1,0,1,0)

        # bfs to calculate distances
        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in pairwise(directions):
                next_r, next_c = curr_r+dr, curr_c+dc
                # check if the next cell is valid and hasn't been visited
                if 0 <= next_r < n and 0 <= next_c < n and dist_to_thief[next_r][next_c]==inf:
                    dist_to_thief[next_r][next_c] = dist_to_thief[curr_r][curr_c]+1
                    queue.append((next_r, next_c))
        
        # sort all cells by their distance to the nearest thief in descending order
        cells_by_dist = []
        for r in range(n):
            for c in range(n):
                cells_by_dist.append((dist_to_thief[r][c], r, c))
        cells_by_dist.sort(reverse=True)

        # the union find to connect cells, starting from highest distance
        union_find = UnionFind(n*n)

        for dist, r, c in cells_by_dist:
            # try to connect current cell with adjacent cells of same or higher distance
            for dr, dc in pairwise(directions):
                next_r, next_c = r+dr, c+dc
                if 0 <= next_r < n and 0 <= next_c < n and dist_to_thief[next_r][next_c]>=dist:
                    union_find.union(r*n+c, next_r*n+next_c)
        
            # check if start and end cells are connected
            start_idx = 0
            end_idx = n*n-1

            if union_find.find(start_idx) == union_find.find(end_idx):
                return int(dist)
        return 0