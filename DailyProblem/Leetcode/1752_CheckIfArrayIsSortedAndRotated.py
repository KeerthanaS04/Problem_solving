from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        break_count = 0
        for i, val in enumerate(nums):
            if nums[i-1]>val:
                break_count+=1
        return break_count<=1