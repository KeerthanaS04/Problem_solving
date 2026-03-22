from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_90_cw(matrix: List[List[int]]) -> None:
            n = len(matrix)
            for layer in range(n//2):
                first = layer
                last = n-1-layer

                # rotate elements in the current layer
                for i in range(first, last):
                    offset = i-first

                    # save top element
                    temp = matrix[first][i]
                    # move left to top
                    matrix[first][i] = matrix[last-offset][first]
                    # move bottom to left
                    matrix[last-offset][first] = matrix[last][last-offset]
                    # move right to bottom
                    matrix[last][last-offset] = matrix[i][last]
                    # move top(saved) to right
                    matrix[i][last] = temp
        for rotation_count in range(4):
            if mat==target:
                return True
            rotate_90_cw(mat)
        return False