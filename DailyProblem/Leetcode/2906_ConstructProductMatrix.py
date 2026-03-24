from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        result = [[0]*cols for _ in range(rows)]
        MOD = 12345

        # calculate the suffix product from bottom right to top left
        suffix = 1
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                result[row][col] = suffix
                suffix = (suffix*grid[row][col])%MOD
        
        # multiply by prefix product from top left to bottom right
        prefix = 1
        for row in range(rows):
            for col in range(cols):
                result[row][col] = (result[row][col]*prefix)%MOD
                prefix = (prefix*grid[row][col])%MOD
        return result