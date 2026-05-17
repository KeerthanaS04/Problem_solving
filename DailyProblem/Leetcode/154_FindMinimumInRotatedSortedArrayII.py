from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l<r:
            mid = (l+r)>>1
            if nums[mid]>nums[r]:
                l = mid+1
            elif nums[mid]<nums[r]:
                r = mid
            # cannot determine which side contains min, safely shrinks from right
            else:
                r-=1
        return nums[l]