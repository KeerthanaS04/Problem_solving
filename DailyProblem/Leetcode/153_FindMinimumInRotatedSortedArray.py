from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        first_true_idx = -1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]<=nums[n-1]:
                first_true_idx = mid
                r = mid-1
            else:
                l = mid+1
        return nums[first_true_idx]