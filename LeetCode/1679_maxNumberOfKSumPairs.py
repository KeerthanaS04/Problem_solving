from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        count = 0

        while l<r:
            curr_sum = nums[l]+nums[r]

            if curr_sum==k:
                count+=1
                l+=1
                r-=1
            elif curr_sum>k:
                r-=1
            else:
                l+=1
        return count