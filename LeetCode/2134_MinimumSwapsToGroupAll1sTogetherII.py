from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = nums.count(1)
        curr_ones = sum(nums[:total_ones])
        max_ones = curr_ones
        n = len(nums)

        # to cover full circle
        for r in range(total_ones, n+total_ones):
            curr_ones+=nums[r%n]
            l = r-total_ones
            curr_ones-=nums[l%n]
            max_ones = max(max_ones, curr_ones)
        return total_ones-max_ones