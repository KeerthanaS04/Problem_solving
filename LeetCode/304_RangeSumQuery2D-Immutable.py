from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        # build prefix sum matrix
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                self.prefix_sum[i + 1][j + 1] = self.prefix_sum[i][j + 1] + self.prefix_sum[i + 1][j] - self.prefix_sum[i][j] + val
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # using inclusion-exclusion principle to calculate the sum of the region
        return (
            self.prefix_sum[row2 + 1][col2 + 1] 
            - self.prefix_sum[row1][col2 + 1] 
            - self.prefix_sum[row2 + 1][col1] 
            + self.prefix_sum[row1][col1]
        )