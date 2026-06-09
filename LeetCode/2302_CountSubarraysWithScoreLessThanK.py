from typing import List
from itertools import accumulate
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sums = list(accumulate(nums, initial=0))
        total_count = 0

        for end_idx in range(1, len(prefix_sums)):
            l, r = 1, end_idx
            first_true_idx = end_idx+1

            while l<=r:
                mid = (l+r)//2
                subarray_sum = prefix_sums[end_idx]-prefix_sums[end_idx-mid]

                if subarray_sum>=k:
                    first_true_idx = mid
                    r = mid-1
                else:
                    l = mid+1
            total_count+=first_true_idx-1
        return total_count