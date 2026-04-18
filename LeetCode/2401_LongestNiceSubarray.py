from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 0
        mask = 0
        l = 0

        for r, num in enumerate(nums):
            # check if curr num shares any bits with existing windows
            while mask&num:
                mask^=nums[l]
                left+=1
            # add num to window by ORing
            mask|=num

            curr_length = r-l+1
            max_length = max(max_length, curr_length)
        return max_length