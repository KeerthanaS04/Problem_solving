from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0]*(n+1)
        right = [0]*(n+1)

        # left to right
        for i, num in enumerate(nums, 1):
            if num==1:
                left[i] = 1+left[i-1]
            else:
                left[i] = 0
        
        # right to left
        for i in range(n-1, -1, -1):
            if nums[i]==1:
                right[i] = 1+right[i+1]
            else:
                right[i] = 0
        
        max_length = 0
        for i in range(n):
            max_length = max(max_length, left[i]+right[i+1])
        return max_length