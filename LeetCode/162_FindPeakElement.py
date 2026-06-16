from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        first_true_idx = -1

        while l<=r:
            mid = (l+r)//2
            # feasible condition nums[mid]>nums[mid+1]
            # for last element, treat as feasible nums[n] = -inf
            if mid==n-1 or nums[mid]>nums[mid+1]:
                first_true_idx = mid
                r = mid-1
            else:
                l = mid+1
        return first_true_idx