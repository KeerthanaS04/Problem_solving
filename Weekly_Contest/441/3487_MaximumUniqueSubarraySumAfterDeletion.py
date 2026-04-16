from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_val = max(nums)

        # if all numbers are non positive, return the max_value
        if max_val<=0:
            return max_val
        
        total = 0
        seen = set()

        for num in nums:
            if num<0 or num in seen:
                continue
            total+=num
            seen.add(num)
        return total