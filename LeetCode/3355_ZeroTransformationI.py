from typing import List
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[int]) -> bool:
        diff_arr = [0]*(len(nums)+1)

        # for each query, we increment at left and decrement at right+1
        for l, r, in queries:
            diff_arr[l]+=1
            diff_arr[r+1]-=1
        
        # accumulate the diff values to get the actual reduction at each pos
        cumulative_reduction = 0
        for num_val, diff_val in zip(nums, diff_arr):
            cumulative_reduction+=diff_val

            # if original val is greater than the total reduction, we cannot reduce this element to 0
            if num_val>cumulative_reduction:
                return False
        return True