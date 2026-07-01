from itertools import pairwise
from typing import List
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, node_a: int, node_b: int) -> bool:
        root_a, root_b = self.find(node_a), self.find(node_b)

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
    
    def connected(self, node_a: int, node_b: int) -> bool:
        return self.find(node_a) == self.find(node_b)
    
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Kruskal's algorithm
        rows, cols = len(heights), len(heights[0])
        union_find = UnionFind(rows*cols)

        # build all edges with their weights (efforts)
        edges = []
        directions = (0,1,0)
        for r in range(rows):
            for c in range(cols):
                for dr, dc in pairwise(directions):
                    next_r, next_c = r+dr, c+dc
                    if 0 <= next_r < rows and 0 <= next_c < cols:
                        effort = abs(heights[r][c]-heights[next_r][next_c])
                        # convert 2D coordinates to 1D index for union-find
                        curr_idx = r*cols+c
                        neighbor_idx = next_r*cols+next_c
                        edges.append((effort, curr_idx, neighbor_idx))
        
        edges.sort()
        # process edges in order of increasing effort
        for effort, cell_a, cell_b in edges:
            union_find.union(cell_a, cell_b)
            start_idx = 0
            end_idx = rows*cols-1

            if union_find.connected(start_idx, end_idx):
                return effort
        return 0