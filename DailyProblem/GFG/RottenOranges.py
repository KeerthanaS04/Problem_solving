from collections import deque
class Solution:
    def orangesRot(self, mat):
        rows, cols = len(mat), len(mat[0])
        fresh_count = 0
        queue = deque()

        # calculate the rotten and fresh oranges
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]==2:
                    queue.append((row, col))
                elif mat[row][col]==1:
                    fresh_count+=1
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        minutes = 0

        while queue and fresh_count>0:
            minutes+=1
            curr_size = len(queue)
            for _ in range(curr_size):
                curr_row, curr_col = queue.popleft()
                for row_delta, col_delta in directions:
                    next_row = curr_row+row_delta
                    next_col = curr_col+col_delta

                    if (0<=next_row<rows and 0<=next_col<cols and mat[next_row][next_col]==1):
                        mat[next_row][next_col] = 2
                        queue.append((next_row, next_col))
                        fresh_count-=1

                        # Early termination
                        if fresh_count==0:
                            return minutes
        return -1 if fresh_count>0 else 0