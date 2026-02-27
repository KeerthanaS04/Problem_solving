from collections import defaultdict
from typing import List
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def count_subarrays_with_target_sum(nums: List[int]) -> int:
            prefix_sum_count = defaultdict(int)
            prefix_sum_count[0] = 1

            count = 0
            curr_sum = 0

            for num in nums:
                curr_sum+=num
                count+=prefix_sum_count[curr_sum-target]
                prefix_sum_count[curr_sum]+=1
            return count
        rows, cols = len(matrix), len(matrix[0])
        result = 0

        # fix top row of submatrix
        for top_row in range(rows):
            #Initialize column sums for current top row
            col_sums = [0]*cols
            # Extended bottom row of submatrix
            for bottom_row in range(top_row, rows):
                for col in range(cols):
                    col_sums[col]+=matrix[bottom_row][col]
                result+=count_subarrays_with_target_sum(col_sums)
        return result