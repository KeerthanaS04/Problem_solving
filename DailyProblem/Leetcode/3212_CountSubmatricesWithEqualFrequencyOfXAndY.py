from typing import List
class Solution:
    def numberOfSubmatrices(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        prefix_sum = [[[0]*2 for _ in range(cols+1)] for _ in range(rows+1)]
        count=0

        for row_idx, row_data in enumerate(grid, 1):
            for col_idx, cell_value in enumerate(row_data, 1):
                # using inclusion-exclusion principle
                prefix_sum[row_idx][col_idx][0] = prefix_sum[row_idx-1][col_idx][0]+prefix_sum[row_idx][col_idx-1][0]-prefix_sum[row_idx-1][col_idx-1][0]
                prefix_sum[row_idx][col_idx][1] = prefix_sum[row_idx-1][col_idx][1]+prefix_sum[row_idx][col_idx-1][1]-prefix_sum[row_idx-1][col_idx-1][1]

                # if current cell is not empty
                if cell_value!='.':
                    # X(88)&1 = 0, Y(89)&1 = 1
                    char_type = ord(cell_value)&1
                    prefix_sum[row_idx][col_idx][char_type]+=1
                
                # check whether it is valid - atleast one X and equal counts of X and Y
                if (prefix_sum[row_idx][col_idx][0]>0 and prefix_sum[row_idx][col_idx][0]==prefix_sum[row_idx][col_idx][1]):
                    count+=1
        return count