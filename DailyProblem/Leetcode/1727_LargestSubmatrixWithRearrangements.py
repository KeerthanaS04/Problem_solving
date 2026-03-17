from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    matrix[i][j] = matrix[i-1][j]+1
        max_area = 0
        # for each row, find out the maximum rectangle area
        for row in matrix:
            row.sort(reverse=True)
            for width, height in enumerate(row, start=1):
                curr_area = width*height
                max_area = max(max_area, curr_area)
        return max_area