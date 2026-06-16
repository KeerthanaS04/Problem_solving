from typing import List
class Solution:
    def minimumMountainRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1]*n
        right = [1]*n

        # calculate LIS (Longest Increasing Subsequence) from left
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    left[i] = max(left[i], left[j]+1)
        
        # calculate LIS from right (which gives us the longest decreasing subsequence)
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i]>nums[j]:
                    right[i] = max(right[i], right[j]+1)
        
        # find the maximum mountain length
        max_mountain_length = max(
            left[i]+right[i]-1 for i in range(n) if left[i]>1 and right[i]>1
        )
        return n-max_mountain_length