from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # place each positive integer at its correct position by mapping
        for i in range(n):
            # keep swapping curr element to its correct position
            while (1<=nums[i]<=n and nums[i]!=nums[i-1]):
                target_idx = nums[i]-1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # find the first position where element doesn't match expected value
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        
        # all positions contain correct values
        return n+1