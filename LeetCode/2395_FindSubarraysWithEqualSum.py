from typing import List
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums)-1):
            curr_sum = nums[i]+nums[i+1]

            if curr_sum in seen:
                return True
        return False