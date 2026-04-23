from typing import List
from bisect import bisect_left
from itertools import accumulate
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = list(accumulate(nums, initial=0))
        res = []

        for target in queries:
            # find the first index where nums[idx]>target
            right_idx = bisect_left(nums, target+1)

            decrease_oper = (prefix_sums[-1]-prefix_sums[right_idx]) - (len(nums)-right_idx)*target

            # find the first idx where nums[idx]>=target
            left_idx = bisect_left(nums, target)
            increase_oper = target*left_idx - prefix_sums[left_idx]
            total = increase_oper+decrease_oper
            res.append(total)
        return res