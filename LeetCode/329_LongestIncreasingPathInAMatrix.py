from typing import List
from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(row: int, col: int) -> int:
            max_path_length = 0
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc

                if 0<=next_row<rows and 0<=next_col<cols and matrix[next_row][next_col]>matrix[row][col]:
                    max_path_length = max(max_path_length, dfs(next_row, next_col))
            return max_path_length + 1

        rows = len(matrix)
        cols = len(matrix[0])
        max_path = 0
        for i in range(rows):
            for j in range(cols):
                max_path = max(max_path, dfs(i, j))
        return max_path