from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        curr_rotation_val = sum(i*val for i, val in enumerate(nums))
        n = len(nums)
        total_sum = sum(nums)
        max_rotation_val = curr_rotation_val

        for rotation in range(1,n):
            curr_rotation_val = curr_rotation_val+total_sum-n*nums[n-rotation]
            max_rotation_val = max(max_rotation_val, curr_rotation_val)
        return max_rotation_val