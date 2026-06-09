from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # using Kadane's algorithm
        # for both maximum and minimum sum subarray (i.e, positive and negative sum)
        max_sum = 0
        min_sum = 0
        max_absolute = 0

        for num in nums:
            max_sum = max(max_sum, 0)+num
            min_sum = min(min_sum, 0)+num
            max_absolute = max(max_absolute, max_sum, abs(min_sum))
        return max_absolute