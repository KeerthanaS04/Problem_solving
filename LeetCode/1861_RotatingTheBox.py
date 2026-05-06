from collections import deque
from typing import List
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])
        rotated_box = [[None]*rows for _ in range(cols)]

        # 90 degree clockwise rotation
        for row in range(rows):
            for col in range(cols):
                rotated_box[col][rows-1-row] = boxGrid[row][col]
        
        # apply gravity to make stones fall down in the rotated box
        for col in range(rows):
            empty_pos = deque()

            # process from bottom to top
            for row in range(cols-1,-1,-1):
                if rotated_box[row][col]=='*':
                    # stones cannot fall past obstacles
                    empty_pos.clear()
                elif rotated_box[row][col]=='.':
                    # empty space, add to queue
                    empty_pos.append(row)
                elif rotated_box[row][col]=='#' and empty_pos:
                    # stone found with empty space below
                    lowest_empty = empty_pos.popleft()
                    rotated_box[lowest_empty][col] = '#'
                    rotated_box[row][col] = '.'
                    empty_pos.append(row)
        return rotated_box