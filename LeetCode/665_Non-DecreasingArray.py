from typing import List
from more_itertools import pairwise
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def non_decreasing(nums: List[int]) -> bool:
            return all(a<=b for a, b in pairwise(nums))
        
        n = len(nums)
        for i in range(n-1):
            a, b = nums[i], nums[i+1]

            if a>b:
                # lower nums[i] to nums[i+1]
                nums[i] = b
                if non_decreasing(nums):
                    return True
                
                # raise nums[i+1] to nums[i]
                # first restore nums[i] to its original value
                nums[i] = a
                nums[i+1] = a
                return non_decreasing(nums)
        # no violation found, array is non-decreasing
        return True